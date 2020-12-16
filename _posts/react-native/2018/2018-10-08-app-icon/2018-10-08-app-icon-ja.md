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

<div id="contents_list" markdown="1">

## 目次

1. [Deprecated](#deprecated)
1. [概要](#概要)
1. [イメージ準備](#イメージ準備)
1. [ライブラリインストール](#ライブラリインストール)
1. [使い方](#使い方)
1. [参考](#参考)

</div>

## Deprecated

このブログポストはgenerator-rn-toolboxが`Deprecated`されたのでもう管理しません。generator-rn-toolboxの新しいライブラリである`react-native-make`を使うことをおすすめします。

react-native-makeに関しては下記のブログをご参考してください。

- [react-native-make]({{site.url}}/{{page.categories}}/react-native-make/){:target="_blank"}

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

{% include in-feed-ads.html %}

## 使い方

- 下記のコマンドでアイコンを作ります。

{% include_relative common/usage.md %}

アイコンが生成してプロジェクトへ反映しました。プロジェクトを実行してアイコンが反映されたかを確認しましょう。

{% include_relative common/start_project.md %}

アイコンがちゃんと表示できない方はシミュレータまたは端末のアプリを削除してもう一度プロジェクトを実行して見てください。

## 参考

- 公式サイト: [generator-rn-toolbox](https://github.com/bamlab/generator-rn-toolbox){:rel="nofollow noreferrer" target="_blank" }
