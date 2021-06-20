---
layout: 'post'
permalink: '/flutter/app-icon/'
paginate_path: '/flutter/:num/app-icon/'
lang: 'ja'
categories: 'flutter'
comments: true

title: '[Flutter] アプリのアイコン変更'
description: 今回のブログポストではFlutterでアプリのアイコンを変更する方法について説明します。
image: '/assets/images/category/flutter/background.png'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [イメージファイルの準備](#イメージファイルの準備)
- [flutter_launcher_iconsのインストール](#flutter_launcher_iconsのインストール)
- [アプリのアイコン設定](#アプリのアイコン設定)
- [アプリのアイコン生成](#アプリのアイコン生成)
- [確認](#確認)
- [完了](#完了)

</div>

## 概要

Flutterを使ってアプリを開発してみようかと思います。今回のブログポストではFlutterでアプリのアイコンを変更する方法について説明します。

アプリのアイコンを変更するためにはアンドロイドとiOSに合わせてイメージを生成して、各プラットフォームにアプリのアイコンを設定する必要があります。しかし、`flutter_launcher_icons`パッケージを使うと、アプリのアイコンをもっと簡単に変更することができます。

- [flutter_launcher_icons](https://pub.dev/packages/flutter_launcher_icons){:rel="nofollow noreferrer" target="_blank"}

## イメージファイルの準備

まず、アプリのアイコンに使うイメージが必要です。イメージファイルは下記の条件に合わせて作る必要があります。

- PNGファイル
- 1024px x 1024px以上のサイズ
- ファイルサイズは最大1024KB

準備したファイルを`assets/app-icon.png`に保存します。

## flutter_launcher_iconsのインストール

flutter_launcher_iconsパッケージを使うため、flutter_launcher_iconsパッケージをインストールする必要があります。

下記のコマンドを実行してflutter_launcher_iconsパッケージをインストールします。

```bash
flutter pub add flutter_launcher_icons --dev
```

## アプリのアイコン設定

次はアプリのアイコンで生成するイメージファイルを設定する必要があります。`pubspec.yaml`ファイルを開いて一番下に下記の内容を追加します。

```yaml
...
flutter_icons:
  android: "launcher_icon"
  ios: true
  image_path: "assets/app-icon.png"
```

## アプリのアイコン生成

下記のコマンドを実行して、flutter_launcher_iconsパッケージを使ってアプリのアイコンを生成します。

```bash
flutter pub run flutter_launcher_icons:main
```

## 確認

Flutterのプロジェクトを再実行すると、次のようにアプリのアイコンが上手く変更されたことが確認できます。

![Flutter - App icon](/assets/images/category/flutter/2021/app-icon/app-icon.jpg)

## 完了

これでFlutterでアプリのアイコンを変更する方法についてみてみました。`flutter_launcher_icons`のパッケージを使うとこのように簡単にFlutterのアプリのアイコンを変更することができます。
