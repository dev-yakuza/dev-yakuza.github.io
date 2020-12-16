---
layout: 'post'
permalink: '/react-native/typescript/'
paginate_path: '/react-native/:num/typescript/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'typescript'
description: 'RNプロジェクトへtypescriptを適用して開発してみよう。'
image: '/assets/images/category/react-native/typescript.jpg'
---


<div id="contents_list" markdown="1">

## 目次

1. [リアクトネイティブ(React Native)プロジェクト生成](#リアクトネイティブreact-nativeプロジェクト生成)
1. [typescriptへ必要なライブラリをインストール](#typescriptへ必要なライブラリをインストール)
    - [typescript ライブラリ](#typescript-ライブラリ)
1. [typescript設定](#typescript設定)
    - [tsconfig.jsonを作る](#tsconfigjsonを作る)
1. [React Native CLIでTypescriptを始める](#react-native-cliでtypescriptを始める)
1. [typescriptでコーディングする。](#typescriptでコーディングする)

</div>

## リアクトネイティブ(React Native)プロジェクト生成

下記のコマンドを使ってリアクトネイティブ(React Native)のプロジェクトを生成します。

{% include_cached react-native/create_new_project.md %}

## typescriptへ必要なライブラリをインストール

typescriptが動作出来るようにするため必要なライブラリをインストールします。

{% include_relative common/install_modules.md %}

### typescript ライブラリ

- typescript: typescriptをインストール。
- @types/react: typescriptへ必要なreactのtypeをインストール。
- @types/react-native: typescriptへ必要なリアクトネイティブ(React Native)のtypeをインストール。

{% include in-feed-ads.html %}

## typescript設定

typescriptを設定してリアクトネイティブ(React Native)が動作出来るようにします。

### tsconfig.jsonを作る

プロジェクトのrootフォルダへ```tsconfig.json```ファイルを作成して下記の内容をコピペします。

{% include_relative common/tsconfig_json.md %}

詳しい内容は公式ホームページを参考してください。

- [typescript - tsconfig.json](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html){:rel="nofollow noreferrer" target="_blank"}
- [typescript - compile options](https://www.typescriptlang.org/docs/handbook/compiler-options.html){:rel="nofollow noreferrer" target="_blank"}

## React Native CLIでTypescriptを始める

(0.60.2にバグがあるみたいです。)
このような設定がやりたくない場合、下記のReact Native CLIコマンドでTypescriptをベースにするReact Nativeプロジェクトを生成することが出来ます。

```bash
react-native init SampleProject --template typescript
```

## typescriptでコーディングする。

App.jsをApp.tsxにファイル名を変更してtypescriptスタイルでコーディングします。

- Class Component

```js
import React from 'react';
...
interface Props {}
interface State {}
...
export default class App extends React.Component<Props, State> {
```

- Functional Component

```js
import React from 'react';
...
interface Props {}
...
const App = ({  }: Props) => {
...
```
