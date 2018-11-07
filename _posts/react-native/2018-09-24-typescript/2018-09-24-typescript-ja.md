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


## react-nativeプロジェクト生成
下記のコマンドを使ってRNのプロジェクトを生成します。

{% include react-native/create_new_project.md %}

## typescriptへ必要なライブラリをインストール
typescriptが動作出来るようにするため必要なライブラリをインストールします。

{% include_relative common/install_modules.md %}

### typescript ライブラリ
- typescript: typescriptをインストール。
- @types/react: typescriptへ必要なreactのtypeをインストール。
- @types/react-native: typescriptへ必要なreact-nativeのtypeをインストール。

### ビルド自動化のためのライブラリ
- react-native-typescript-transformer: typescriptをランタイム中に、自動にビルドするためのライブラリ

## typescript設定
typescriptを設定してreact-nativeが動作出来るようにします。

### tsconfig.jsonを作る
プロジェクトのrootフォルダへ```tsconfig.json```ファイルを作成して下記の内容をコピペします。

{% include_relative common/tsconfig_json.md %}

詳しい内容は公式ホームページを参考してください。
- [typescript - tsconfig.json](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html){:rel="nofollow noreferrer" :target="_blank"}
- [typescript - compile options](https://www.typescriptlang.org/docs/handbook/compiler-options.html){:rel="nofollow noreferrer" :target="_blank"}

### tslint.jsonを作る
typescriptの開発を便利にするためtslintを適用します。下記の内容をプロジェクトのrootフォルダへ```tslint.json```を作ってコピペします。

{% include_relative common/tslint_json.md %}

詳しい内容は公式ホームページを参考してください。
- [typescript - tslint](https://github.com/Microsoft/TypeScript-React-Starter#overriding-defaults){:rel="nofollow noreferrer" :target="_blank"}
- [tslint - configuration](https://palantir.github.io/tslint/usage/configuration/){:rel="nofollow noreferrer" :target="_blank"}

### rn-cli.config.jsを作る
[Bruno Lemos](https://www.facebook.com/brunolemos?fref=gc&dti=586400221495560){:rel="nofollow noreferrer" :target="_blank"}さんが```No need for rn-cli.config.js anymore since v0.57```でファイスブック(facebook)へコメントをくれって確認した結果、RN(react-native)のバージョン0.57以上は```rn-cli.config.js```が要らないです。ご参考してください。

~~typescriptをランタイム中に認識できることを助けてくれるライブラリの設定ファイルです。プロジェクトのrootフォルダへ```rn-cli.config.js```ファイルへ下記の内容を作成します。~~

{% include_relative common/rn_cli_config.md %}

## typescriptでコーディングする。
App.jsをApp.tsxにファイル名を変更してtypescriptスタイルでコーディングします。

{% include_relative common/typescript_code.md %}