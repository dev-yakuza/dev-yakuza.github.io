---
layout: 'post'
permalink: '/react/root-import/'
paginate_path: '/react/:num/root-import/'
lang: 'ja'
categories: 'react'
comments: true

title: 'Reactでroot importする方法'
description: 'React(リアクト)でコンポーネント(Component)を呼ぶ時(import)、rootフォルダーを基準にして参照できるように設定して見ます。'
image: '/assets/images/category/react/2019/root-import/background.jpg'
---

## 概要
React Native(RN リアクトネイティブ)でも紹介したroot importをReact(リアクト)でも適用して見ます。なぜroot importを使うか、問題点は何にか知りたい方はReact Native(RN リアクトネイティブ)のブログを参考してください。

- [リアクトネイティブ(React Native)でrootからimportする]({{site.url}}/react-native/root-import/){:target="_blank"}

このブログポストで使うソースコードはギットハブ(Github)に公開されております。

- Github: [https://github.com/dev-yakuza/react_root_import](https://github.com/dev-yakuza/react_root_import){:target="_blank"}

## プロジェクト準備
このブログポストで使うReact(リアクト)プロジェクトはWebpack(ウェブパック)とTypescript(タイプスクリプト)、styled-componentsが適用されたプロジェクトをベースにしています。もっと詳しく内容は以前のブログポストを参考してください。

- [WebpackでReactを始める]({{site.url}}/{{page.categories}}/start/){:target="_blank"}
- [ReactでTypescriptを使う方法]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}
- [Reactでstyled-componentsを使う方法]({{site.url}}/{{page.categories}}/styled-components/){:target="_blank"}

以前のブログポストでプロジェクトを生成したら下記のようなフォルダ構造が出来上がります。私たちはreact_styled-componentsの名前ではなくreact_root_importの名前でプロジェクトを生成しました。

```bash
|-- src
|   |-- index.html
|   |-- App.tsx
|-- .babelrc
|-- package.json
|-- webpack.config.js
```

{% include in-feed-ads.html %}

## babel-plugin-root-import
rootフォルダから参照するため`babel-plugin-root-import`を下記のコマンドでインストールします。

```bash
npm install babel-plugin-root-import --save-dev
```

React(リアクト)プロジェクトの`.babelrc`を開いて下記のように修正します。

```json
{
  "presets": [
    ...
  ],
  "plugins": [
    [
      "babel-plugin-root-import",
      {
        "rootPathPrefix": "~",
        "rootPathSuffix": "src"
      }
    ]
  ],
  "env": {
    ...
  }
}
```

私のフォルダ構造を見たら分かると思いますが`src`フォルダへ全てのソースコードを管理しています。したがって`root`フォルダではなく`src`フォルダを基準に設定しました。

## Webpack設定
rootフォルダを参照できるように`webpack.config.js`を開いて下記のように修正します。

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
    ...
  },
  resolve: {
    extensions: ['.ts', '.tsx', '.js', '.jsx'],
  },
  plugins: [
    ...
  ],
};
```

## Typescript
Typescript(タイプスクリプト)を使ってない方は上の設定だけ解決出来ます。私はReact(リアクト)プロジェクトでTypescript(タイプスクリプト)を使っているのでTypescript(タイプスクリプト)もrootフォルダを認識できるように設定します。

React(リアクト)プロジェクトの`tsconfig.json`ファイルを開いて下記のように修正します。

```json
{
  "compilerOptions": {
    ...
    "baseUrl": "./src", // all paths are relative to the baseUrl
    "paths": {
      "~/*": ["*"] // resolve any `~/foo/bar` to `<baseUrl>/foo/bar`
    }
  },
  ...
}
```

{% include in-feed-ads.html %}

## ソースコード修正
上で設定した内容を確認するためソースコードを修正して見ます。`src/Components/Title/index.tsx`を生成して下記のように修正します。

```js
import * as React from 'react';
import Styled from 'styled-components';

const Label = Styled.h1`
  color: red;
`;
interface Props {
  label: string;
}

const Title = ({ label }: Props) => {
  return <Label>{label}</Label>;
};

export default Title;
```

そして`src/Features/Top/index.tsx`を生成して下記のように修正します。

```js
import * as React from 'react';

import Title from '~/Components/Title';

interface Props {}

const Top = ({  }: Props) => {
  return <Title label="Hello World!" />;
};

export default Top;
```

最後に、`src/App.tsx`を開いて下記のように修正します。

```js
import * as React from 'react';
import * as ReactDOM from 'react-dom';

import Top from './Features/Top';

interface Props {}

const App = ({  }: Props) => {
  return <Top />;
};

ReactDOM.render(<App />, document.getElementById('app'));
```

{% include in-feed-ads.html %}

## 確認
上で設定した内容がうまく動作するか確認するため下記のコマンドでWebpack(ウェブパック)テストサーバーを実行します。

```bash
npm start
```

ブラウザで`http://localhost:8080/`を開いたら`Hello World!`が表示されることが確認出来ます。
下記のコマンドでWebpack(ウェブパック)を使ってReact(リアクト)プロジェクトをビルド(build)して見ます。

```bash
npm run build
```

そしたら`dist`フォルダへファイルたちが生成されることが確認出来ます。

## 確認
これでReact(リアクト)プロジェクトでも`import`する時、`../../../../`ではなく`~/`を使えるようになりました。ソースコードでも分かると思いますが、私は参照するコンポーネント(Component)がフォルダ中にある場合`./`を使って参照します。フォルダの外にある場合`~/`を使って参照しています。
