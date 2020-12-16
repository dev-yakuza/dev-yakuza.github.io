---
layout: 'post'
permalink: '/react/typescript/'
paginate_path: '/react/:num/typescript/'
lang: 'ja'
categories: 'react'
comments: true

title: 'ReactでTypescriptを使う方法'
description: 'React(リアクト)でTypescript(タイプスクリプト)を使うための方法について調べてみて、簡単にReact(リアクト)プロジェクトにTypescript(タイプスクリプト)を適用してみます。'
image: '/assets/images/category/react/2019/typescript/background.jpg'
---

## 概要
会社でReact(リアクト)で新しいプロジェクトをするこのになりました。それで久しぶりにReact(リアクト)を最初から設定するチャンスが出ってその内容をまとめることにしました。今回のブログではReact(リアクト)でTypescript(タイプスクリプト)を使う方法について調べてみて、React(リアクト)プロジェクトでTypescript(タイプスクリプト)を使ってみます。

このブログで扱うソースコードはギットハブ(Github)に公開されております。

- Github: [https://github.com/dev-yakuza/react_typescript](https://github.com/dev-yakuza/react_typescript){:target="_blank"}

React(リアクト)のプロジェクトを始めるためWebpack(ウェブパック)の設定に関しては以前のブログポストを参考してください。

- 以前のブログポスト:[WebpackでReactを始める]({{site.url}}/{{page.categories}}/start/){:target="_blank"}

## プロジェクトの準備
このブログポストで使うReact(リアクト)プロジェクトは以前のブログポストで紹介したWebpack(ウェブパック)をベースにしています。詳しく内容は以前のブログポストを確認してください。

- 以前のブログポスト:[WebpackでReactを始める]({{site.url}}/{{page.categories}}/start/){:target="_blank"}

以前のブログポストを使ってプロジェクトを生成すると下記のような構造が出来上がります。私たちはreact_startと言う名前ではなくreact_typescriptと言う名前でプロジェクトを生成しました。

```bash
|-- src
|   |-- index.html
|   |-- App.jsx
|-- .babelrc
|-- package.json
|-- webpack.config.js
```

## インストール
下記のコマンドでReact(リアクト)でTypescript(タイプスクリプト)を適用するため必要なライブラリをインストールします。

```bash
npm install --save-dev typescript @babel/preset-typescript ts-loader fork-ts-checker-webpack-plugin tslint, tslint-react
```

- typescript: Typescript(タイプスクリプト)を使います。
- @babel/preset-typescript: babel(バベル)でTypescript(タイプスクリプト)をビルドするためのライブラリ。
- ts-loader: Webpack(ウェブパック)でTypescript(タイプスクリプト)をコンパイルするため必要なライブラリ。
- fork-ts-checker-webpack-plugin: ts-loaderの性能を上げるためのライブラリ
- tslint, tslint-react: コードコンベンションをチェックするためのライブラリ。

{% include in-feed-ads.html %}

## Webpack設定
React(リアクト)でTypescript(タイプスクリプト)を使うため`webpack.config.js`を開いて下記のようにWebpack(ウェブパック)を設定します。

```js
const path = require('path');

const HtmlWebpackPlugin = require('html-webpack-plugin');

// For Typescript
const ForkTsCheckerWebpackPlugin = require('fork-ts-checker-webpack-plugin');

module.exports = {
  entry: {
    // For Typescript
    'js/app': ['./src/App.tsx'],
  },
  output: {
    path: path.resolve(__dirname, 'dist/'),
    publicPath: '/',
  },
  module: {
    rules: [
      // For Typescript
      {
        test: /\.(ts|tsx)$/,
        use: [
          'babel-loader',
          {
            loader: 'ts-loader',
            options: {
              transpileOnly: true,
            },
          },
        ],
        exclude: /node_modules/,
      },
    ],
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: './src/index.html',
      filename: 'index.html',
    }),
    // For typescript
    new ForkTsCheckerWebpackPlugin({ silent: true }),
  ],
};
```

修正した内容を確認してみます。

```js
// For Typescript
const ForkTsCheckerWebpackPlugin = require('fork-ts-checker-webpack-plugin');
```

Typescript(タイプスクリプト)でビルドする時、性能を上げるためのプラグインを読んできます。

```js
entry: {
  // For Typescript
  'js/app': ['./src/App.tsx'],
},
```

バンドルファイル(bundle)の開始ファイル(Entry)を`jsx`から`tsx`に変更します。

```js
{
  test: /\.(ts|tsx)$/,
  use: [
    'babel-loader',
    {
      loader: 'ts-loader',
      options: {
        transpileOnly: true,
      },
    },
  ],
  exclude: /node_modules/,
},
```

Webpack(ウェブパック)でTypescript(タイプスクリプト)を使うため`js|jsx`を`ts|tsx`で修正して、`ts-loader`を追加しました。ts-loaderのオプションは性能を上げるためのオプションです。

```js
plugins: [
  ...
  // For typescript
  new ForkTsCheckerWebpackPlugin({ silent: true }),
],
```

最後にTypescript(タイプスクリプト)のコンパイル速度を上げるためのプラグインを設定しました。

{% include in-feed-ads.html %}

## tsconfig.json
Typescript(タイプスクリプト)を使うため`tsconfig.json`を作って下記のように修正します。

```json
{
  "compilerOptions": {
    "target": "es6",
    "module": "esnext",
    "moduleResolution": "node",
    "noResolve": false,
    "noImplicitAny": false,
    "removeComments": false,
    "sourceMap": true,
    "allowJs": true,
    "jsx": "react",
    "allowSyntheticDefaultImports": true,
    "keyofStringsOnly": true
  },
  "typeRoots": ["node_modules/@types", "src/@type"],
  "exclude": [
    "node_modules",
    "build",
    "scripts",
    "acceptance-tests",
    "webpack",
    "jest",
    "src/setupTests.ts",
    "./node_modules/**/*"
  ],
  "include": ["./src/**/*", "@type"]
}
```

オプションに関する説明は省略します。詳細内容は下記のリンクを参考してください。

- [https://www.typescriptlang.org/docs/handbook/tsconfig-json.html](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html){:rel="nofollow noreferrer" target="_blank"}
- [https://www.typescriptlang.org/docs/handbook/compiler-options.html](https://www.typescriptlang.org/docs/handbook/compiler-options.html){:rel="nofollow noreferrer" target="_blank"}

## tslint.json
Typescriptを使うため`tslint.json`を生成して下記のように修正します。

```json
{
  "extends": ["tslint", "tslint-react"],
  "rules": {
    "align": [true, "parameters", "statements"],
    "jsx-alignment": false,
    "ban": false,
    "class-name": true,
    "comment-format": [true, "check-space"],
    "curly": true,
    "eofline": false,
    "forin": true,
    "indent": [true, "spaces"],
    "interface-name": [false],
    "jsdoc-format": true,
    "jsx-no-lambda": false,
    "jsx-no-multiline-js": false,
    "label-position": true,
    "max-line-length": [true, 120],
    "member-ordering": [
      true,
      {
        "order": [
          "public-before-private",
          "static-before-instance",
          "variables-before-functions"
        ]
      }
    ],
    "no-any": false,
    "no-arg": true,
    "no-bitwise": true,
    "no-console": [
      true,
      "log",
      "error",
      "debug",
      "info",
      "time",
      "timeEnd",
      "trace"
    ],
    "no-consecutive-blank-lines": true,
    "no-construct": true,
    "no-debugger": true,
    "no-duplicate-variable": true,
    "no-empty": false,
    "no-eval": true,
    "no-shadowed-variable": true,
    "no-string-literal": true,
    "no-switch-case-fall-through": true,
    "no-trailing-whitespace": false,
    "no-unused-expression": true,
    "no-use-before-declare": true,
    "one-line": [
      true,
      "check-catch",
      "check-else",
      "check-open-brace",
      "check-whitespace"
    ],
    "quotemark": [true, "single", "jsx-double"],
    "radix": true,
    "semicolon": [false],
    "switch-default": true,

    "trailing-comma": [false],

    "triple-equals": [true, "allow-null-check"],
    "typedef": [true, "parameter", "property-declaration"],
    "typedef-whitespace": [
      true,
      {
        "call-signature": "nospace",
        "index-signature": "nospace",
        "parameter": "nospace",
        "property-declaration": "nospace",
        "variable-declaration": "nospace"
      }
    ],
    "variable-name": [
      true,
      "ban-keywords",
      "check-format",
      "allow-leading-underscore",
      "allow-pascal-case"
    ],
    "whitespace": [
      true,
      "check-branch",
      "check-decl",
      "check-module",
      "check-operator",
      "check-separator",
      "check-type",
      "check-typecast"
    ]
  }
}
```

オプションに関する説明は下記のサイトを参考してください。

- [https://github.com/Microsoft/TypeScript-React-Starter#overriding-defaults](https://github.com/Microsoft/TypeScript-React-Starter#overriding-defaults){:rel="nofollow noreferrer" target="_blank"}
- [https://palantir.github.io/tslint/usage/configuration/](https://palantir.github.io/tslint/usage/configuration/){:rel="nofollow noreferrer" target="_blank"}

{% include in-feed-ads.html %}

## babel設定
babelを設定するため`.babelrc`を生成して下記のように修正します。

```json
{
  "presets": [
    [
      "@babel/preset-env",
      { "targets": { "browsers": ["last 2 versions", ">= 5% in KR"] } }
    ],
    "@babel/react",
    "@babel/typescript"
  ]
}
```

babel(バベル)でTypescript(タイプスクリプト)がコンパイルできるように`"@babel/typescript"`を追加しました。

## Typescriptスタイルコーディング
React(リアクト)でTypescript(タイプスクリプト)を使うため`./src/App.jsx`を`./src/App.tsx`で名前を変更して下記のように修正しました。

```js
import * as React from 'react';
import * as ReactDOM from 'react-dom';

interface Props {}

const App = ({  }: Props) => {
  return <h1>Hello World!</h1>;
};

ReactDOM.render(<App />, document.getElementById('app'));
```

## 確認
下記のコマンドで私たちが生成して設定した内容がうまく動いてるか確認します。

```bash
npm start
```

そしてブラウザを開いて`http://localhost:8080/`に移動すると`Hello World!`が見えることが確認できます。package.jsonのスクリプトである`"start": "webpack-dev-server --mode development",`を`"start": "webpack-dev-server --mode development --open",`ように`--open`のオプションを追加すると`npm start`でWebpack(ウェブパック)の開発サーバーを実行すると自動的ブラウザが立ち上がって`http://localhost:8080/`に移動します。

実行された開発サーバーをストップして、下記のコマンドでビルドしてみましょう。

```bash
npm run build
```

問題なく実行されたら`./dist/`フォルダが生成されてその下に`index.html`と`/js/app.js`が生成されることが確認できます。また、`index.html`を開いてみたら私たちが作ったindex.htmlと違って`<script type="text/javascript" src="/js/app.js"></script>`が追加されたことが確認できます。

## 参考
- [https://github.com/TypeStrong/ts-loader](https://github.com/TypeStrong/ts-loader){:rel="nofollow noreferrer" target="_blank"}
- [https://github.com/Realytics/fork-ts-checker-webpack-plugin](https://github.com/Realytics/fork-ts-checker-webpack-plugin){:rel="nofollow noreferrer" target="_blank"}
- [https://github.com/palantir/tslint-react](https://github.com/palantir/tslint-react){:rel="nofollow noreferrer" target="_blank"}