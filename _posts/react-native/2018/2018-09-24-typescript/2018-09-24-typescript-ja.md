---
layout: 'post'
permalink: '/react-native/typescript/'
paginate_path: '/react-native/:num/typescript/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'React NativeでTypeScriptを使う方法'
description: 'React NativeプロジェクトへTypeScriptを適用して開発してみよう。'
image: '/assets/images/category/react-native/typescript.jpg'
---


<div id="contents_list" markdown="1">

## 目次

- [React Nativeプロジェクト生成](#react-nativeプロジェクト生成)
- [TypeScriptへ必要なライブラリをインストール](#typescriptへ必要なライブラリをインストール)
  - [TypeScriptライブラリ](#typescriptライブラリ)
- [TypeScript設定](#typescript設定)
  - [tsconfig.jsonを作る](#tsconfigjsonを作る)
- [React Native CLIでTypeScriptを始める](#react-native-cliでtypescriptを始める)
- [TypeScriptでコーディングする](#typescriptでコーディングする)
- [完了](#完了)

</div>

## React Nativeプロジェクト生成

下記のコマンドを使ってReact Nativeのプロジェクトを生成します。

```bash
react-native init proejct-name
```

## TypeScriptへ必要なライブラリをインストール

TypeScriptが動作出来るようにするため必要なライブラリをインストールします。

```bash
npm install typescript @types/react @types/react-native --save-dev
```

### TypeScriptライブラリ

- typescript: TypeScriptをインストール。
- @types/react: TypeScriptへ必要なreactのtypeをインストール。
- @types/react-native: TypeScriptへ必要なReact Nativeのtypeをインストール。

{% include in-feed-ads.html %}

## TypeScript設定

TypeScriptを設定してReact Nativeが動作出来るようにします。

### tsconfig.jsonを作る

プロジェクトのrootフォルダへ```tsconfig.json```ファイルを作成して下記の内容をコピペします。

```json
{
  "compilerOptions": {
    "allowJs": true,
    "allowSyntheticDefaultImports": true,
    "esModuleInterop": true,
    "isolatedModules": true,
    "jsx": "react",
    "lib": ["es6", "es2017"],
    "moduleResolution": "node",
    "noEmit": true,
    "strict": true,
    "target": "esnext",
    "skipLibCheck": true
  },
  "exclude": ["node_modules", "babel.config.js", "metro.config.js", "jest.config.js"]
}
```

詳しい内容は公式ホームページを参考してください。

- [TypeScript - tsconfig.json](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html){:rel="nofollow noreferrer" target="_blank"}
- [TypeScript - compile options](https://www.typescriptlang.org/docs/handbook/compiler-options.html){:rel="nofollow noreferrer" target="_blank"}

## React Native CLIでTypeScriptを始める

このような設定がやりたくない場合、下記のReact Native CLIコマンドでTypeScriptをベースにするReact Nativeプロジェクトを生成することが出来ます。

```bash
npx react-native init SampleProject --template react-native-template-typescript
```

## TypeScriptでコーディングする

App.jsをApp.tsxにファイル名を変更してTypeScriptスタイルでコーディングします。

- Class Component

```js
import React from 'react';
...
interface Props {}
interface State {}
...
export default class App extends React.Component<Props, State> {
```

- Function Component

```js
import React from 'react';
...
interface Props {}
...
const App = ({  }: Props) => {
...
```

## 完了

これでReact NativeでTypeScriptを適用してTypeScriptを使う方法についてみてみました。今からReact NativeプロジェクトでもTypeScriptを使ってタイプをチェックしてみてください。
