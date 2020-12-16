---
layout: 'post'
permalink: '/react/styled-components/'
paginate_path: '/react/:num/styled-components/'
lang: 'ja'
categories: 'react'
comments: true

title: 'Reactでstyled-componentsを使う方法'
description: 'React(リアクト)でstyled-componentsを使う方法について見てみましょう。'
image: '/assets/images/category/react/2019/styled-components/background.jpg'
---

## 概要
会社でReact(リアクト)で新しいプロジェクトをするこのになりました。それで久しぶりにReact(リアクト)を最初から設定するチャンスが出ってその内容をまとめることにしました。このブログポストではReact(リアクト)でstyled-componentsを使う方法について調べるし、React(リアクト)プロジェクトでstyled-componentsを使って見ます。

このブログで扱うソースコードはギットハブ(Github)に公開されております。

- Github: [https://github.com/dev-yakuza/react_styled-components](https://github.com/dev-yakuza/react_styled-components){:target="_blank"}

今回のブログポストで使ったソースコードは以前のブログを参考して作りました。

- 以前のブログ: [ReactでTypescriptを使う方法]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}

## プロジェクト準備
このブログポストで使うReact(リアクト)プロジェクトはWebpack(ウェブパック)とTypescript(タイプスクリプト)が適用されたプロジェクトをベースにしています。詳しく内容は以前のブログポストを確認してください。

- [WebpackでReactを始める]({{site.url}}/{{page.categories}}/start/){:target="_blank"}
- [ReactでTypescriptを使う方法]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}

以前のブログポストを使ってプロジェクトを生成すると下記のような構造が出来上がります。私たちはreact_typescriptと言う名前ではなくreact_styled-componentsと言う名前でプロジェクトを生成しました。

```bash
|-- src
|   |-- index.html
|   |-- index.tsx
|-- .babelrc
|-- package.json
|-- webpack.config.js
```

## インストール
下記のコマンドでReact(リアクト)でstyled-componentsを使うため必要なライブラリをインストールします。

```bash
npm install --save-dev styled-components @types/styled-components babel-plugin-styled-components cross-env
```

- styled-components: styled-componentsを使います。
- @types/styled-components: styled-componentsを使ってTypescript(タイプスクリプト)を使うためのライブラリ。
- babel-plugin-styled-components: styled-componentsのclass名を分かりやすくしてくれるライブラリ。
- cross-env: MacとWindowsで同じコマンドで環境変数を設定するためのライブラリ。

{% include in-feed-ads.html %}

## package.json修正
下記のように`package.json`のスクリプト部分を修正します。

```js
"scripts": {
  "start": "cross-env NODE_ENV=development webpack-dev-server --open",
  "prebuild": "rimraf dist",
  "build": "cross-env NODE_ENV=production webpack --progress"
},
```

以前のWebpack(Webpack)のモードを設定するため`--mode development`と`--mode production`を使いましたが、この部分を環境変数で設定するように修正しました。

## Webpack修正
下記のように`webpack.config.js`ファイルを修正します。

```js
...
module.exports = {
  mode: process.env.NODE_ENV,
  ...
};
...
```

以前はコマンドでモードを設定しましたが、環境変数で設定するため`mode`を追加しました。

## babel設定
下記のように`.babelrc`ファイルを修正します。

```json
{
  "presets": [
    ...
  ],
  "env": {
    "development": {
      "plugins": ["babel-plugin-styled-components"]
    }
  }
}
```

環境変数がdevelopmentの場合、class名を分かりやすくさせるためbabel-plugin-styled-componentsを設定しました。環境変数がproductionの場合class名がhash化されて人が認識づらくさせます。

[環境変数がdevelopmentの場合]

![Reactでstyled-componentsを使う - 環境変数がdevelopmentの場合、class名](/assets/images/category/react/2019/styled-components/styled-components-in-development.jpg)

[環境変数がproductionの場合]

![Reactでstyled-componentsを使う - 環境変数がproductionの場合、class名](/assets/images/category/react/2019/styled-components/styled-components-in-production.jpg)

{% include in-feed-ads.html %}

## styled-componentsスタイルコーディング
React(リアクト)でstyled-componentsを使うため`./src/index.tsx`を下記のように修正します。

```js
import * as React from 'react';
import * as ReactDOM from 'react-dom';
import Styled from 'styled-components';

const Title = Styled.h1`
  color: red;
`;
interface Props {}

const App = ({  }: Props) => {
  return <Title>Hello World!</Title>;
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

## エラー対応
React(リアクト)プロジェクトを確認するため`npm start`を実行する時は問題ありませんでしたが、`npm run build`を使ってビルドする時下記のエラーが出ました。

```bash
ERROR in /git_repository/react_styled-components/node_modules/@types/react-native/globals.d.ts
ERROR in /git_repository/react_styled-components/node_modules/@types/react-native/globals.d.ts(36,15):
TS2300: Duplicate identifier 'FormData'.

ERROR in /git_repository/react_styled-components/node_modules/@types/react-native/globals.d.ts
ERROR in /git_repository/react_styled-components/node_modules/@types/react-native/globals.d.ts(81,5):
TS2717: Subsequent property declarations must have the same type.  Property 'body' must be of type 'BodyInit', but here has type 'string | ArrayBuffer | DataView | Int8Array | Uint8Array | Uint8ClampedArray | Int16Array | Uint16Array | Int32Array | Uint32Array | Float32Array | Float64Array | Blob | FormData'.

ERROR in /git_repository/react_styled-components/node_modules/@types/react-native/globals.d.ts
ERROR in /git_repository/react_styled-components/node_modules/@types/react-native/globals.d.ts(107,14):
TS2300: Duplicate identifier 'RequestInfo'.

ERROR in /git_repository/react_styled-components/node_modules/@types/react-native/globals.d.ts
ERROR in /git_repository/react_styled-components/node_modules/@types/react-native/globals.d.ts(126,13):
TS2403: Subsequent variable declarations must have the same type.  Variable 'Response' must be of type '{ new (body?: BodyInit, init?: ResponseInit): Response; prototype: Response; error(): Response; redirect(url: string, status?: number): Response; }', but here has type '{ new (body?: string | ArrayBuffer | DataView | Int8Array | Uint8Array | Uint8ClampedArray | Int16Array | Uint16Array | Int32Array | Uint32Array | Float32Array | Float64Array | Blob | FormData, init?: ResponseInit): Response; prototype: Response; error: () => Response; redirect: (url: string, status?: number) => Res...'.

ERROR in /git_repository/react_styled-components/node_modules/@types/react-native/globals.d.ts
ERROR in /git_repository/react_styled-components/node_modules/@types/react-native/globals.d.ts(249,14):
TS2300: Duplicate identifier 'XMLHttpRequestResponseType'.

ERROR in /git_repository/react_styled-components/node_modules/@types/react-native/index.d.ts
ERROR in /git_repository/react_styled-components/node_modules/@types/react-native/index.d.ts(9418,18):
TS2717: Subsequent property declarations must have the same type.  Property 'geolocation' must be of type 'Geolocation', but here has type 'GeolocationStatic'.

ERROR in /git_repository/react_styled-components/node_modules/@types/react-native/index.d.ts
ERROR in /git_repository/react_styled-components/node_modules/@types/react-native/index.d.ts(9421,11):
TS2451: Cannot redeclare block-scoped variable 'navigator'.

ERROR in /git_repository/react_styled-components/node_modules/typescript/lib/lib.dom.d.ts
ERROR in /git_repository/react_styled-components/node_modules/typescript/lib/lib.dom.d.ts(5353,11):
TS2300: Duplicate identifier 'FormData'.

ERROR in /git_repository/react_styled-components/node_modules/typescript/lib/lib.dom.d.ts
ERROR in /git_repository/react_styled-components/node_modules/typescript/lib/lib.dom.d.ts(5363,13):
TS2300: Duplicate identifier 'FormData'.

ERROR in /git_repository/react_styled-components/node_modules/typescript/lib/lib.dom.d.ts
ERROR in /git_repository/react_styled-components/node_modules/typescript/lib/lib.dom.d.ts(17123,11):
TS2320: Interface 'Window' cannot simultaneously extend types 'GlobalFetch' and 'WindowOrWorkerGlobalScope'.
  Named property 'fetch' of types 'GlobalFetch' and 'WindowOrWorkerGlobalScope' are not identical.

ERROR in /git_repository/react_styled-components/node_modules/typescript/lib/lib.dom.d.ts
ERROR in /git_repository/react_styled-components/node_modules/typescript/lib/lib.dom.d.ts(18152,13):
TS2451: Cannot redeclare block-scoped variable 'navigator'.

ERROR in /git_repository/react_styled-components/node_modules/typescript/lib/lib.dom.d.ts
ERROR in /git_repository/react_styled-components/node_modules/typescript/lib/lib.dom.d.ts(18568,6):
TS2300: Duplicate identifier 'RequestInfo'.

ERROR in /git_repository/react_styled-components/node_modules/typescript/lib/lib.dom.d.ts
ERROR in /git_repository/react_styled-components/node_modules/typescript/lib/lib.dom.d.ts(18746,6):
TS2300: Duplicate identifier 'XMLHttpRequestResponseType'.

ERROR in /git_repository/react_styled-components/node_modules/typescript/lib/lib.dom.iterable.d.ts
ERROR in /git_repository/react_styled-components/node_modules/typescript/lib/lib.dom.iterable.d.ts(67,11):
```

この問題を解決するため`tsconfig.json`を下記のように修正しました。

```json
{
  "compilerOptions": {
    ...
    "skipLibCheck": true
  },
  ...
}
```