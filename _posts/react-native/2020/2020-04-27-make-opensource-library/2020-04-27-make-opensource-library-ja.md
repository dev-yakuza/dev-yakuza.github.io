---
layout: 'post'
permalink: '/react-native/make-opensource-library/'
paginate_path: '/react-native/:num/make-opensource-library/'
lang: 'ja'
categories: 'react-native'
comments: true

title: React Native用オープンソースを作る方法
description: React Native用のオープンソースを作る方法について説明します。
image: '/assets/images/category/react-native/2020/make-opensource-library/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [NPM](#npm)
- [GitHubリポジトリ](#githubリポジトリ)
- [package.json](#packagejson)
- [開発環境構成](#開発環境構成)
- [ライブラリを開発する](#ライブラリを開発する)
- [配布する](#配布する)
- [完了](#完了)

</div>

## 概要

React Nativeで開発したら、いつも他の人が作ったオープンソースをたくさん使って開発しました。これを見て、私もオープンソースを作ってみようとは思いましたが、時間がないと言い訳しながら作ってなかったです。

しかし、時間があって、作ってみようと思ったら、どこから作ればいいか全然わかりませんでした。皆さんも私のようにオープンソースを作りたいですが、どこからスタートすればいいか分からない方のため、オープンソースを作る方法について共有します。

下記のリンクは自分が作ったオープンソースです。

- NPM: [react-native-image-modal](https://www.npmjs.com/package/react-native-image-modal){:rel="nofollow noreferrer" target="_blank"}

## NPM

このブログで紹介するオープンソース作成方法はReact NativeのJavascript部分だけです。Nativeモジュールを作成する方法ではないことを事前に共有します。

今から作るJavascriptオープンソースを使うためにはNPM(Node Package Manager)へデプロイする必要があります。

- NPM: [react-native-image-modal](https://www.npmjs.com/package/react-native-image-modal){:rel="nofollow noreferrer" target="_blank"}

オープンソースを作成する前下記のブログポストを確認して、自分が開発するオープンソースをNPMへ配布できる状態を作ってください。

- [NPMに自分のライブラリを配布する]({{site.url}}/share/deploy-npm-library/){:target="_blank"}

## GitHubリポジトリ

オープンソースを共有する最高の方法はGitHubですね。今から作るオープンソースライブラリのソースコードを共有するためGitHubリポジトリを生成します。

まだ、GitHubのアカウンどを持ってない方は、下記のリンクを使って無料で会員登録してください。

- GitHub:[https://github.com/](https://github.com/){:rel="nofollow noreferrer" target="_blank"}

GitHubのリポジトリを生成する時、NPMへ既に配布されたライブラリと重複されてない名前で生成します。NPMで重複されたか確認する方法は下記のブログを参考してください。

- NPMに自分のライブラリを配布する: [npm info]({{site.url}}/share/deploy-npm-library/#npm-info){:target="_blank"}

GitHubリポジトリを作ったら、自分のローカルPCへCloneします。

```bash
git clone [Your repository URL]
```

{% include in-feed-ads.html %}

## package.json

Javascriptのオープンソースを開発して配布するため`package.json`ファイルが必要です。 下記のコマンドを使ってpackage.jsonを生成します。

```bash
# cd [Your Project folder]
npm init
```

package.jsonファイルを生成する方法について詳しい内容は下記のリンクを参考してください。

- NPMに自分のライブラリを配布する: [npm init]({{site.url}}/share/deploy-npm-library/#npm-init){:target="_blank"}

## 開発環境構成

私は`Typescript`を使ってReact Nativeのライブラリを開発してみました。今からTypescriptとReact Nativeを開発する環境を構築してみます。

まず、下記のコマンドを使ってReact Nativeのプロジェクトを生成します。

```bash
react-native init Develop
```

このプロジェクトはReact Nativeのライブラリを開発する時使う予定です。次は`tsconfig.json`ファイルを生成して下記のように修正します。

```json
{
  "compilerOptions": {
    "module": "esnext",
    "target": "es5",
    "lib": ["es6", "dom", "es2016", "es2017"],
    "sourceMap": true,
    "allowJs": false,
    "jsx": "react-native",
    "declaration": true,
    "declarationMap": true,
    "moduleResolution": "node",
    "forceConsistentCasingInFileNames": true,
    "noImplicitReturns": true,
    "noImplicitThis": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    "suppressImplicitAnyIndexErrors": true,
    "noUnusedLocals": true,
    "outDir": "dist",
    "skipLibCheck": true,
    "allowSyntheticDefaultImports": true,
    "removeComments": true
  },
  "include": ["src"],
  "exclude": ["node_modules", "Develop", "DevelopWithExpo", "Example", "ExampleWithExpo", "dist"]
}
```

オプションについての説明は省略します。ただし、`"include": ["src"],`を使って`src`フォルダへあるファイルをビルドする予定で、`"outDir": "dist",`オプションを使ってビルドした結果を`dist`フォルダへ保存する予定です。

次は`package.json`ファイルを開いて下記のように修正します。

```json
{
  ...
  "main": "dist/index.js",
  "types": "dist/index.d.ts",
  "scripts": {
    "lint": "eslint --ext .tsx --ext .ts src/",
    "format": "prettier --check ./src",
    "start": "rm -rf Develop/dist && tsc -w --outDir Develop/dist",
    "start:expo": "rm -rf DevelopWithExpo/dist && tsc -w --outDir DevelopWithExpo/dist",
    "prepare": "rm -rf dist && tsc"
  },
  "lint-staged": {
    "src/**/*.{ts,tsx}": [
      "eslint --ext .tsx --ext .ts src/ --fix"
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
  "peerDependencies": {
    "react": "*",
    "react-native": "*"
  },
  "devDependencies": {
    "@types/react": "*",
    "@types/react-native": "*",
    "@typescript-eslint/eslint-plugin": "2.25.0",
    "@typescript-eslint/parser": "2.25.0",
    "eslint": "6.8.0",
    "eslint-plugin-prettier": "3.1.2",
    "eslint-plugin-react": "7.19.0",
    "eslint-plugin-react-hooks": "2.5.1",
    "husky": "4.2.3",
    "lint-staged": "10.0.9",
    "prettier": "2.0.2",
    "react": "*",
    "react-native": "*",
    "typescript": "^3.7.5"
  },
}
```

一つ一つ詳しく見てみます。

```json
"main": "dist/index.js",
"types": "dist/index.d.ts",
```

NPMにライブラリのメインファイルとタイプファイルが何かを教えてあげます。

```json
"scripts": {
  "lint": "eslint --ext .tsx --ext .ts src/",
  "format": "prettier --check ./src",
  "start": "rm -rf Develop/dist && tsc -w --outDir Develop/dist",
  "start:expo": "rm -rf DevelopWithExpo/dist && tsc -w --outDir DevelopWithExpo/dist",
  "prepare": "rm -rf dist && tsc"
},
```

ライブラリを開発する時使うコマンドです。

`lint`と`format`は`eslint`と`prettier`を使って開発してるソースコードのFormattingを検査するコマンドです。また、下記にある`lint-staged`と`husky`の設定を使って`git commit`する時、Formattingを実行するようにしました。

```json
"lint-staged": {
  "src/**/*.{ts,tsx}": [
    "eslint --ext .tsx --ext .ts src/ --fix"
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
```

詳しい内容が知りたい方は下記のブログポストを参考してください。

- [React NativeでESLint, Prettierを使う方法]({{site.url}}/{{page.categories}}/eslint-prettier-husky-lint-staged/){:target="_blank"}

ライブラリを開発する時、`npm start`のコマンドを使ってTypescriptをビルドしながら、開発する予定です。また、`npm publish`を使って開発したライブラリを配布しますが、`prepare`コマンドを定義して配布前Typescriptをビルドするように設定しました。

詳しい内容は下記のブログを参考してください。

- NPMに自分のライブラリを配布する: [npm publish]({{site.url}}/share/deploy-npm-library/#npm-publish){:target="_blank"}

開発へ必要なライブラリを`devDepenencies`へ定義しました。次は下記のコマンドを使って必要なライブラリをインストールします。

```bash
npm install
```

インストールが完了されたら`.gitignore`ファイルと`.prettierignore`ファイルを生成して`node_modules`を追加します。

今開発する準備ができました。次は、どのようにライブラリを開発するか見てみます。

{% include in-feed-ads.html %}

## ライブラリを開発する

上で設定した開発環境を見ると、私たちは`src`フォルダへ開発するソースコードを追加しなきゃならないです。`src`フォルダへ`index.tsx`ファイルを生成して、下記のように修正します。

```js
import React from 'react';
import { View, Text } from 'react-native';

const LibraryName = (): JSX.Element => {
  return (
    <View>
      <Text>Hello World!</Text>
    </View>
  );
};

export default LibraryName;
```

そして`Develop`フォルダの`App.js`ファイルを開いて下記のように修正します。

```js
import React from 'react';
import {StyleSheet,   SafeAreaView} from 'react-native';

import LibraryName from './dist';

const App = () => {
  return (
    <SafeAreaView style={styles.container}>
      <LibraryName />
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

export default App;
```

そして、下記のコマンドを使って開発したTypescriptをビルドします。

```bash
npm start
```

上で作った`package.json`の`start`コマンドを見ると下記のようです。

```bash
"start": "rm -rf Develop/dist && tsc -w --outDir Develop/dist",
```

コマンドを詳しく見ると、`Develop/dist`フォルダを生成した後、`tsc`を使ってビルドして、結果物を`Develop/dist`フォルダへ保存します。また、`-w`オプションを使ってソースコードの変更がある場合、再ビルドするように設定しました。したがって、上のコマンドを実行した後、開発を進めます。

そして他の`Terminal`または、`CMD`を開いて下記のコマンドを実行します。

```bash
cd Develop
npm run ios
# npm run android
```

そしたら私たちが開発してるライブラリが下記のようにうまく表示されてることが確認できます。

![React Native用オープンソースを作る方法 - Hello world](/assets/images/category/react-native/2020/make-opensource-library/hello-world.jpg)

また、`src/index.tsx`ファイルを開いて内容を修正して見るとシミュレータの内容がうまく更新されることが確認できます。

## 配布する

このように開発したライブラリを配布するためには下記のコマンドを使います。

```bash
npm login
npm publish
```

コマンドについて詳しい説明は下記のブログを参考してください。

- [NPMに自分のライブラリを配布する]({{site.url}}/share/deploy-npm-library/){:target="_blank"}

## 完了

React Nativeのライブラリを開発する方法について簡単に見てみました。`NPM`へ配布するため、NPMに関するブログと一緒に見なきゃなので、ちょっと難しいかもしれないです。에 관한 블로그와 같이 보셔야 좀 더 이해하기 쉬울거 같네요.

皆さんも時間がある時、素敵なオープンソースを開発して、開発者の文化へ参加してみることはどうでしょうか？
