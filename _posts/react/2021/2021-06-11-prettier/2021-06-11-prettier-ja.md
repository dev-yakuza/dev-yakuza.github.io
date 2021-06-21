---
layout: 'post'
permalink: '/react/prettier/'
paginate_path: '/react/:num/prettier/'
lang: 'ja'
categories: 'react'
comments: true

title: '[React] Prettier'
description: 'ReactでPrettierを使ってコードのフォーマットを同一する方法を説明します。'
image: '/assets/images/category/react/2021/prettier/background.png'
published: false
---

<div id="contents_list" markdown="1">

## 目次

</div>

## ブログシリーズ

このブログはシリーズで作成されております。次はブログシリーズのリストです。

- [React] Prettier
- [[React] ESLint]({{site.url}}/{{page.categories}}/eslint/){:target="_blank"}
- [[React] Husky, lint-staged]({{site.url}}/{{page.categories}}/husky-lint-staged/){:target="_blank"}
- [[React] GitHub Actions]({{site.url}}/{{page.categories}}/github-actions/){:target="_blank"}

## 概要

一人でサービスを開発するときはコードフォーマット（スペース、タブ、クォーテーションなど）は特に問題にはなりません。しかし、他の人と一緒にサービスを開発するときは、各開発者が使ってるコードフォーマットが違う可能性があります。このようにコードフォーマットが違うとコードが読みづらくなったり、予想できないバーグなどが発生します。

Prettierはコードフォーマッタ(Code formatter)で事前にコードフォーマットを定義して、そのフォーマットに合わせてコードを直す役割をします。

今回のブログポストではReactでPrettierを使ってコードフォーマットを同一する方法について説明します。

## プロジェクト準備

ReactでPrettierを使うため、`create-react-app`でプロジェクトを生成します。`create-react-app`をよく知らない方は下記のリンクを参考してください。

- [create-react-app]({{site.url}}/{{page.categories}}/create-react-app/start/){:target="_blank"}

そしたら、次のコマンドを使ってPrettierを使うReactプロジェクトを生成します。

```bash
npx create-react-app prettier_example
```

{% include in-feed-ads.html %}

## Prettierのインストール

ReactでPrettierを使うためにはPrettierライブラリをインストールする必要があります。下記のコマンドを使ってPrettierライブラリをインストールします。

```bash
# cd prettier_example
npm install --save-dev prettier
```

## Prettierの設定

ReactでPrettierを使うためには使うコードフォーマットを事前に定義する必要があります。コードフォーマットを事前に定義するため、`.prettierrc.js`ファイルを生成して下記のように修正します。

```js
module.exports = {
  jsxBracketSameLine: true,
  singleQuote: true,
  trailingComma: 'all',
  printWidth: 100,
};
```

Prettierの公式サイトで設定可能な他のオプションを確認することができます。

- Prettierの公式サイト: [Options](https://prettier.io/docs/en/options.html){:rel="noopener" target="_blank"}

上のオプションを確認して、各プロジェクトに合わせてオプションを設定してみてください。

## フォーマットチェック

次のコマンドを使って私たちが定義したPrettierのオプションを守ってないファイルを探すことができます。

```bash
npx prettier --check ./src
```

コマンドを実行すると下記のように定義したオプションを守ってないファイルリストが表示されます。

```bash
[warn] public/index.html
[warn] src/App.js
[warn] src/index.css
[warn] src/index.js
[warn] src/reportWebVitals.js
[warn] Code style issues found in the above file(s). Forgot to run Prettier?
```

## フォーマッティング

次のコマンドを使って私たちが定義したPrettierのオプションを使ってコードフォーマッティングをすることができます。

```bash
prettier --write ./src
```

上のコマンドを実行すると次のようにフォーマッティングされたファイルリストが表示されます。

```bash
.prettierrc.js 40ms
package-lock.json 441ms
package.json 25ms
public/index.html 55ms
public/manifest.json 4ms
README.md 49ms
src/App.css 44ms
src/App.js 17ms
src/App.test.js 10ms
src/index.css 7ms
src/index.js 6ms
src/reportWebVitals.js 8ms
src/setupTests.js 3ms
```

このようにファイルをフォーマッティングした後、再び次のコマンドを実行してコードのフォーマットを確認すると、

```bash
npx prettier --check ./src
```

次のように全てのファイルがうまくフォーマッティングされたことが確認できます。

```bash
Checking formatting...
All matched files use Prettier code style!
```

## package.jsonの設定

上で使った`check`コアマンドと`write`コマンドをもっと簡単に使えるようにするため`package.json`ファイルを開いて下記のように修正します。

```json
"scripts": {
  ...
  "format": "prettier --check ./src",
  "format:fix": "prettier --write ./src"
},
```

このように`package.json`ファイルを修正すると、次のコマンドを使ってPrettierを使うことができます。

```bash
npm run format
npm run format:fix
```

{% include in-feed-ads.html %}

## エディターの設定

Prettierは色んなエディターで使うことができます。Prettierの公式サイトでPrettierが使えるエディターを確認することができます。

- Prettierの公式サイト: [Editor Integration](https://prettier.io/docs/en/editors.html){:rel="noopener" target="_blank"}

ここでは`VSCode`で設定する方法を簡単に見てみます。次のリンクを使ってVSCodeのPrettierプラグインをインストールします。

- VSCodeのプラグイン: [Prettier - Code formatter](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode){:rel="noopener" target="_blank"}

インストールされたら、VSCodeを開いて`(macOS) cmd + shift + p`または`(windows) ctrl + shift + p`キーを押して、`open settings`を検索します。

![vscode command palette](/assets/images/category/react/2021/prettier/vscode-command-palette.jpg)

`Preference: Open Setting(JSON)`を選択して当該ファイルを次のように修正します。

```json
{
  ...
  "editor.formatOnSave": true,
  "[typescriptreact]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[typescript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[javascript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[javascriptreact]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[json]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  }
}
```

または簡単に次のように設定します。

```json
{
  ...
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode"
}
```

このように設定したら、VSCodeでファイルを修正して保存すると、自動でコードがフォーマットされることが確認できます。

## 完了

これでReactプロジェクトでPrettierを設定する方法について説明しました。Prettierを使って上手くフォーマティングされたコードを管理してみてください。
