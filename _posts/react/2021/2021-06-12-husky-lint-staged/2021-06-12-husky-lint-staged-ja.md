---
layout: 'post'
permalink: '/react/husky-lint-staged/'
paginate_path: '/react/:num/husky-lint-staged/'
lang: 'ja'
categories: 'react'
comments: true

title: '[React] husky, lint-staged'
description: 'Reactでhuskyとlint-stagedと使ってGitにコミットする時、ESLintとPrettierを実行するように設定してみます。'
image: '/assets/images/category/react/2021/husky-lint-staged/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [プロジェクト準備](#プロジェクト準備)
- [husky](#husky)
- [lint-staged](#lint-staged)
- [huskyとlint-stagedの設定](#huskyとlint-stagedの設定)
- [完了](#完了)

</div>

## ブログシリーズ

このブログはシリーズで作成されております。次はブログシリーズのリストです。

- [[React] Prettier]({{site.url}}/{{page.categories}}/prettier/){:target="_blank"}
- [[React] ESLint]({{site.url}}/{{page.categories}}/eslint/){:target="_blank"}
- [React] Husky, lint-staged
- [[React] GitHub Actions]({{site.url}}/{{page.categories}}/github-actions/prettier-eslint/){:target="_blank"}

## 概要

以前のブログシリーズでcreate-react-appで生成したReactプロジェクトにPrettierとESLintをインストールして設定する方法について説明しました。

今回のブログポストでは`husky`と`lint-staged`を使ってPrettierとESLintを活用する方法について説明します。

## プロジェクト準備

Reactのhuskyとlint-stagedを使うため、`create-react-app`でプロジェクトを生成してみます。`create-react-app`に詳しくない方は下記のリンクを確認してください。

- [create-react-app]({{site.url}}/{{page.categories}}/create-react-app/start/){:target="_blank"}

次のコマンドを実行してhuskyとlint-stagedを使うReactプロジェクトを生成します。

```bash
npx create-react-app husky_lint_example --template=typescript
```

私は主に`TypeScript`を使ってReactを開発してるので`--template=typescript`オプションを使ってプロジェクトを生成しました。このように生成されたReactプロジェクトにPrettierとESLintを設定します。PrettierとESLintを設定する方法については下記のリンクを参考してください。

- [Prettier]({{site.url}}/{{page.categories}}/prettier/){:target="_blank"}
- [ESLint]({{site.url}}/{{page.categories}}/eslint/){:target="_blank"}

{% include in-feed-ads.html %}

## husky

GitはHookと言う機能があります。Gitで特定なイベント（コミット、プシューなど）を実行する時、そのイベントにHookを設定してHookに設定されたスクリプトを実行することができます。

huskyとはGit Hookを簡単に使えるように助けてくれるツールです。

- huskyの公式サイト: [https://typicode.github.io/husky/](https://typicode.github.io/husky/){:rel="noopener" target="_blank"}

そしたら、下記のコマンドを実行してhuskyをインストールします。

```bash
npm install --save-dev husky
```

## lint-staged

huskyと一緒によく使えてるlint-stagedはGitのStagedされたファイルに特定なコマンドを実行するように助けてくれるツールです。

- lint-stagedの公式ページ: [https://github.com/okonet/lint-staged](https://github.com/okonet/lint-staged){:rel="noopener" target="_blank"}

GitのStagedされた状態とはgit addコマンドで修正されたファイルをコミットするため追加をした状態を意味します。このようにStaged状態のファイルは再び修正をするとgit addをしてまた追加する必要があります。

lint-stagedはStagedされたファイルを修正した後、git addをしなくても問題ないようにするツールです。

そしたらhuskyと一緒にlint-stagedを使うため下記のコマンドを実行してlint-stagedをインストールします。

```bash
npm install --save-dev lint-staged
```

## huskyとlint-stagedの設定

今からhuskyとlint-stagedを使ってGitのCommitを使う時、ESLintとPrettierを実行するように設定をしてみます。

huskyとlint-stagedを設定するため`package.json`ファイルを開いて下記のように修正します。

```json
{
  ...
  "scripts": {
    ...
  },
  "lint-staged": {
    "src/**/*.{ts,tsx}": [
      "eslint --ext .tsx --ext .ts ./src --fix"
    ],
    "./src/**": [
      "prettier --write ."
    ]
  },
  "husky": {
    "hooks": {
      "pre-commit": "lint-staged"
    }
  },
  ...
}
```

このように修正するとGitを使ってCommitをする時、huskyのpre-commitに登録されたlint-stagedが実行され、lint-stagedに登録されたESLintとPrettierのコマンドが実行されます。

## 完了

これでReactプロジェクトでhuskyとlint-stagedを使ってESLintとPrettierを実行する方法について説明しました。今からhuskyとlint-stagedで自動化されたESLintとPrettierを使ってみてください。
