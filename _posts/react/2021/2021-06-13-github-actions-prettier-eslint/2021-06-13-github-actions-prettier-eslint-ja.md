---
layout: 'post'
permalink: '/react/github-actions/prettier-eslint/'
paginate_path: '/react/:num/github-actions/prettier-eslint/'
lang: 'ja'
categories: 'react'
comments: true

title: '[React] GitHub ActionsでPrettierとESLintを使う方法'
description: 'Reactプロジェクトに設定したPrettierとESLintをGitHub Actionsを使って実行してみましょう。'
image: '/assets/images/category/react/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [GitHub Actions](#github-actions)
- [確認](#確認)
- [完了](#完了)

</div>

## ブログシリーズ

このブログはシリーズで作成されております。次はブログシリーズのリストです。

- [[React] Prettier]({{site.url}}/{{page.categories}}/prettier/){:target="_blank"}
- [[React] ESLint]({{site.url}}/{{page.categories}}/eslint/){:target="_blank"}
- [[React] Husky, lint-staged]({{site.url}}/{{page.categories}}/husky-lint-staged/){:target="_blank"}
- [React] GitHub Actions

## 概要

今までcreate-react-appで生成したReactプロジェクトにPrettierとESLintを設定して、huskyとlint-stagedを使ってPrettierとESLintを自動で実行されるようにしてみました。今回のブログポストではGitHub Actionsを使ってPull Requestが作られた時、PrettierとESLintを実行する予定です。

- GitHubの公式サイト: [Actions](https://github.com/features/actions){:rel="noopener" target="_blank"}

ここで紹介するコードは下記のリンクでい確認できます。

- GitHub: [Todo](https://github.com/dev-yakuza-example/todo){:rel="noopener" target="_blank"}

## GitHub Actions

そしたらGitHub Actionsを使うため、GitHub Actionsの設定ファイルを作ってみましょう。`./.github/workflows/main.yml`ファイルを生成して下記のように修正します。

```yaml
name: Check the source code
on:
  pull_request:
    branches:
      - main
jobs:
  test:
    name: Check the source code
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Install packages
        run: npm ci
      - name: Prettier
        run: npm run format
      - name: Lint
        run: npm run lint
```

コードをもっと詳しくみてみましょう。

{% include in-feed-ads.html %}

このGitHub Actionsの名前は`Check the source code`です。

```yaml
name: Check the source code
...
```

このGitHub Actionsは`main`ブランチに`Pull Request`が生成されると実行されます。

```yaml
...
on:
  pull_request:
    branches:
      - main
...
```

このGitHub Actionは`Check the source code`と言うFlowを持っていて、`ubuntu`の上で実行されます。

```yaml
...
jobs:
  test:
    name: Check the source code
    runs-on: ubuntu-latest
...
```

まず、現在Repositoryのソースコードを持ってきます。

```yaml
...
jobs:
  test:
    ...
    steps:
      - uses: actions/checkout@v2
...
```

持ってきたソースコードでNodeのパッケージをインストールして、すでに定義されたPrettierとESLintの`npm`スクリプトを実行します。

```yaml
...
jobs:
  test:
    ...
    steps:
      ...
      - name: Install packages
        run: npm ci
      - name: Prettier
        run: npm run format
      - name: Lint
        run: npm run lint
```

このように全ての内容を修正したら、次のコマンドを実行して当該内容をGitHubにアップロードします。

```bash
git add .
git commit -m 'Add GitHub Actions'
git push origin main
```

{% include in-feed-ads.html %}

## 確認

このように作ったGitHub Actionsを確認してみましょう。次のコマンドを実行して新しいブランチを作ります。

```bash
git checkout -b test-pr
```

そして`./src/App.tsx`ファイルを開いて下記のように修正します。

```js
const App = (): JSX.Element => {
  console.log('test!');
  return (
    ...
  );
};
```

その後、次のコマンドを実行して当該内容をGitHubにアップロードします。

```bash
git add .
git commit -m 'Add test code'
git push origin test-pr
```

もし、以前設定したhuskyとlint-stagedのせいで、`Commit`ができない場合、`./package.json`ファイルの下記の内容を探して消します。

```json
{
  ...
  "husky": {
    "hooks": {
      "pre-commit": "lint-staged"
    }
  },
  "lint-staged": {
    "src/**/*.{ts,tsx}": [
      "eslint --ext .tsx --ext .ts ./src"
    ],
    "./src/**": [
      "prettier --check ./src"
    ]
  },
  ...
}
```

そしてもう一度下記のコマンドを実行して修正した内容をGitHubにアップロードします。

```bash
git commit -m 'Add test code'
git push origin test-pr
```

このようにGitHubへ修正した内容をアップロードしたら、GitHubサイトに移動した後、`Pull requests`のタブを選択して、`New pull request`を押して新しいPull Requestを生成します。

![GitHub create pull request](/assets/images/category/react/2021/github-actions/create-pull-request.jpg)

GitHub Actionsを上手く設定したら、先作った`Pull request`の下に次のようにGitHub Actionsでエラーが発生することが確認できます。

![GitHub actions error](/assets/images/category/react/2021/github-actions/github-actions-error.jpg)

右にある`Details`を選択したら、GitHub Actionsで発生したエラーの詳しい内容を確認することができます。

![GitHub actions error details](/assets/images/category/react/2021/github-actions/github-actions-error-details.jpg)

私たちが設定したESLintのルールを守ってない部分があり、そこでエラーが発生したことが確認できます。このように私たちが設定したGitHub Actionga上手く動いてることが確認できます。

## 完了

これでGitHub Actionsを使ってPrettierとESLintを実行する方法について説明しました。huskyとlint-stagedを設定したので、事前に問題を発見できますが、開発者全員が同じ環境ではないので、GitHub Actionsを作って同じ環境でPrettierとESLintでソースコードを解析することができます。

PrettierとESLint以外にもGitHub Actionsで色んな機能を実装することができます。皆さんもGitHub Actionsを使って`CI/CD`を実装してみてください。
