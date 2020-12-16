---
layout: 'post'
permalink: '/react/image-and-font/'
paginate_path: '/react/:num/image-and-font/'
lang: 'ja'
categories: 'react'
comments: true

title: 'Reactでイメージとウェブフォントを使う方法'
description: 'Webpack(ウェブパック)をベースに作ったReact(リアクト)プロジェクトへイメージ(image)とウェブフォント(font)を使う方法について説明します。'
image: '/assets/images/category/react/2019/image-and-font/background.jpg'
---

## 概要
会社でReact(リアクト)を使って新しプロジェクトを作ることになりました。それでWebpack(ウェブパック)を使ってReact(リアクト)プロジェクトを設定しています。今回のブログポストではWebpack(ウェブパック)をベースに作ったReact(リアクト)プロジェクトでリソース(Resource)であるイメージ(image)とウェブフォント(Font)を使う方法について説明します。

このブログで紹介してるソースコードはギットバう(Github)で確認できます。

- Github: [https://github.com/dev-yakuza/react_image_font](https://github.com/dev-yakuza/react_image_font){:rel="noopener" target="_blank"}

## プロジェクト準備
ここで使うReact(リアクト)プロジェクトは下記のような内容が適用されたプロジェクトです。詳しく内容は各ブログポストを確認してください。

- [WebpackでReactを始める]({{site.url}}/{{page.categories}}/start/){:target="_blank"}
- [ReactでTypescriptを使う方法]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}
- [Reactでstyled-componentsを使う方法]({{site.url}}/{{page.categories}}/styled-components/){:target="_blank"}
- [Reactでroot importする方法]({{site.url}}/{{page.categories}}/root-import/){:target="_blank"}
- [React Router]({{site.url}}/{{page.categories}}/react-router/){:target="_blank"}

以前のブログポストでプロジェクトを生成したら下記のようなフォルダ構造が出来上がります。私たちはreact_router라는の名前ではなくreact_image_fontの名前でプロジェクトを生成しました。

```bash
|-- src
|   |-- Components
|   |   |-- Title
|   |   |   |-- index.tsx
|   |-- Features
|   |   |-- Page1
|   |   |   |-- index.tsx
|   |   |-- Page2
|   |   |   |-- index.tsx
|   |   |-- Top
|   |   |   |-- index.tsx
|   |-- index.html
|   |-- App.tsx
|-- .babelrc
|-- package.json
|-- webpack.config.js
```

## モジュールインストール
Webpack(ウェブパック)をベースに作ったReact(リアクト)プロジェクトでイメージウェブフォントを使うためWebpack(ウェブパック)の`file-loader`、`url-loader`が必要です。下記のコマンドで`file-loader`、`url-loader`をインストールします。

```bash
npm install --save-dev file-loader, url-loader
```

- file-loader: Webpack(ウェブパック)で実際使ってるファイルをコピーする時使います。
- url-loader: Webpack(ウェブパック)でファイルサイズが小さなファイルをバンドルファイル(Bundle)で作る時使います。

{% include in-feed-ads.html %}

## Webpack修正
インストールしたモジュール(file-loader, url-loader)を使うため`webpack.config.js`を開いて下記のように修正します。

```js
...
module.exports = {
  mode: process.env.NODE_ENV,
  entry: {
    ...
  },
  output: {
    ...
  },
  module: {
    rules: [
      ...
      {
        // write image files under 10k to inline or copy image files over 10k
        test: /\.(jpg|jpeg|gif|png|svg|ico)?$/,
        use: [
          {
            loader: 'url-loader',
            options: {
              limit: 10000,
              fallback: 'file-loader',
              name: 'images/[name].[ext]',
            },
          },
        ],
      },
      {
        // write files under 10k to inline or copy files over 10k
        test: /\.(woff|woff2|eot|ttf|otf)$/,
        use: [
          {
            loader: 'url-loader',
            options: {
              limit: 10000,
              fallback: 'file-loader',
              name: 'fonts/[name].[ext]',
            },
          },
        ],
      },
    ],
  },
  resolve: {
    ...
  },
  plugins: [
    ...
  ],
  devServer: {
    ...
  },
};
```

2つの設定が似てるので1つの設定だけ詳しくみてみます。

```js
{
  // write image files under 10k to inline or copy image files over 10k
  test: /\.(jpg|jpeg|gif|png|svg|ico)?$/,
  use: [
    {
      loader: 'url-loader',
      options: {
        limit: 10000,
        fallback: 'file-loader',
        name: 'images/[name].[ext]',
      },
    },
  ],
},
```

- `test: /\.(jpg|jpeg|gif|png|svg|ico)?$/,`: 当該ファイルを扱いします。
- `loader: 'url-loader',`: url-loaderを使います。
- `limit: 10000,`: ファイルサイズが10kより小さい場合テキストで使った部分に直接入れます。(バンドルを作る)
- `fallback: 'file-loader',`: ファイルサイズが10kより大きい場合、file-loaderを使ってファイルをコピーします。
- `name: 'images/[name].[ext]',`: コピーする時ファイルをイメージ(image)フォルダにファイル名(name)と拡張子(ext)の形でコピーします。

## ウェブフォント適用
明確にウェブフォント(Font)が適用されたか確認するためGoogle Fontの[Aguafina Script](https://fonts.google.com/specimen/Aguafina+Script){:rel="nofollow noreferrer" target="_blank"}を使ってテストします。まず、下記のリンクでGoogle Fontに移動してウェブフォント(Font)をダウンロードします。

- Aguafina Script Font: [https://fonts.google.com/specimen/Aguafina+Script](https://fonts.google.com/specimen/Aguafina+Script){:rel="nofollow noreferrer" target="_blank"}

ウェブフォント(Font)をダウンロードしたら`src/Assets/Fonts`フォルダを作って当該ファイルをコピーします。そして`src/App.tsx`を開いて下記のように修正します。

```js
import * as React from 'react';
import * as ReactDOM from 'react-dom';
import { createGlobalStyle } from 'styled-components';

import Router from './Router';

const GlobalStyles = createGlobalStyle`
  @font-face {
    font-family:'AguafinaScript';
    src: url(${require('~/Assets/Fonts/AguafinaScript-Regular.ttf')});
  }
  body {
    font-family: 'AguafinaScript', sans-serif;
  }
`;

interface Props {}
const App = ({  }: Props) => {
  return (
    <>
      <GlobalStyles />
      <Router />
    </>
  );
};

ReactDOM.render(<App />, document.getElementById('app'));
```


私たちが作ったReact(リアクト)プロジェクトは[styled-components]({{site.url}}/{{page.categories}}/styled-components/){:target="_blank"}が適用されています。styled-componentsの`createGlobalStyle`を使ってグローバルスタイル(Global Style)を下記のように作りました。

```js
const GlobalStyles = createGlobalStyle`
  @font-face {
    font-family:'AguafinaScript';
    src: url(${require('~/Assets/Fonts/AguafinaScript-Regular.ttf')});
  }
  body {
    font-family: 'AguafinaScript', sans-serif;
  }
`;
```

- `src: url(${require('~/Assets/Fonts/AguafinaScript-Regular.ttf')});`: 私たちはurl-loaderとfile-loaderを使っていますので`require`を使って当該ファイルを読んできます。

このようにグローバルスタイル(Global Style)を下記のように適用しました。

```js
const App = ({  }: Props) => {
  return (
    <>
      <GlobalStyles />
      <Router />
    </>
  );
};
```

{% include in-feed-ads.html %}

## イメージを使う方法
イメージを使うため`src/Assets/images`フォルダを作ってイメージファイルをコピーします。ここには10kより大きなpngファイルと10kより小さいファイルを比較するため追加しました。そしてイメージを使う部分(`src/Features/Top/index.tsx`)を開いて下記のように修正します。

```js
...
const Top = ({ match, history, location }: Props) => {
  ...
  return (
    <div>
      ...
      <img src={require('~/Assets/Images/logo.jpg')} />
      <img src={require('~/Assets/Images/ic_account.jpg')} />
      <img src={require('~/Assets/Images/ic_account.svg')} />
    </div>
  );
};

export default Top;
```

ウェブフォント(Font)を使う時と同じように、`require`を使ってファイルを読んできました。

## 確認
今まで作った内容を確認するため下記のコマンドでWebpack(ウェブパック)開発サーバーを実行します。

```bash
npm start
```

そしたら下記のようにウェブフォント(Font)が適用された画面とイメージ(image)がローディングされた画面が見えます。

![WebpackをベースにしたReactプロジェクトでウェブフォントとイメージを使う方法](/assets/images/category/react/2019/image-and-font/check-with-webpack-dev-server.jpg)

右のソースコードを見れば分かると思いますが、10kより小さいファイルは1つのファイルでバンドリング(Bundle)されたことが確認できます。

下記のコマンドでビルド(Build)してみましょう。

```bash
npm run build
```

そしたら下記のように`dist`フォルダに10kより大きいイメージファイルとウェブフォント(Font)ファイルがコピーされたことが確認できます。

![WebpackをベースにしたReactプロジェクトでウェブフォント、イメージをコピー](/assets/images/category/react/2019/image-and-font/copy-image-font-file-with-webpack.jpg)

