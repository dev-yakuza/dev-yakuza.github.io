---
layout: 'post'
permalink: '/react-native/app-icon/'
paginate_path: '/react-native/:num/app-icon/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'App icon'
description: 'generator-rn-toolboxを使ってアプリアイコンを作って見ましょう。'
image: '/assets/images/category/react-native/app-icon.jpg'
---


## 概要
mac osx上で [generator-rn-toolbox](https://github.com/bamlab/generator-rn-toolbox){:rel="nofollow noreferrer" target="_blank" }を使ってアプリアイコンを作る方法を説明します。

## イメージ準備
アプリアイコンで使う1024x1024pxサイズのイメージを準備します。

## ライブラリインストール
下記のコマンドでライブラリをインストールします。

{% include_relative common/installation.md %}

- generator-rn-toolbox: RNのプロジェクトを助けてくれるツールを提供してるライブラリです。詳しくは公式サイトを参考して下さい。（公式サイト：[generator-rn-toolbox](https://github.com/bamlab/generator-rn-toolbox){:rel="nofollow noreferrer" target="_blank" }）
- yo: generator-rn-toolboxを起動するためのライブラリです。

アプリアイコンを生成するためには```imagemagick```のインストールが必要です。

{% include_relative common/imagemagick_installation.md %}

## 使い方
- 下記のコマンドでアイコンを作ります。

{% include_relative common/usage.md %}

アイコンが生成してプロジェクトへ反映しました。プロジェクトを実行してアイコンが反映されたかを確認しましょう。

{% include_relative common/start_project.md %}

アイコンがちゃんと表示できない方はシミュレータまたは端末のアプリを削除してもう一度プロジェクトを実行して見てください。

## 参考
- 公式サイト: [react-navigation](https://reactnavigation.org/docs){:rel="nofollow noreferrer" target="_blank" }