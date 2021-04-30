---
layout: 'post'
permalink: '/flutter/splash-screen/'
paginate_path: '/flutter/:num/splash-screen/'
lang: 'ja'
categories: 'flutter'
comments: true

title: '[Flutter] スプラッシュスクリーン'
description: 今回のブログポストではFlutterでスプラッシュスクリーンを変更する方法について説明します。
image: '/assets/images/category/flutter/background.png'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [イメージファイル準備](#イメージファイル準備)
- [flutter_native_splashインストール](#flutter_native_splashインストール)
- [スプラッシュイメージ設定](#スプラッシュイメージ設定)
- [flutter_native_splashパッケージオプション](#flutter_native_splashパッケージオプション)
- [スプラッシュイメージ生成](#スプラッシュイメージ生成)
- [Tip](#tip)
  - [初期データ](#初期データ)
  - [ステータスバー](#ステータスバー)
- [完了](#完了)

</div>

## 概要

Flutterを使ってアプリを開発してみようかと思います。今回のブログポストではFlutterでスプラッシュスクリーンを変更する方法について説明します。

スプラッシュスクリーンを変更するためにはアンドロイドとiOSに合わせてイメージを生成して、各プラットフォームに合わせてスプラッシュスクリーンを設定する必要があります。

- [Adding a splash screen to your mobile app](https://flutter.dev/docs/development/ui/advanced/splash-screen){:rel="nofollow noreferrer" target="_blank"}

しかし、`flutter_native_splash`パッケージを使うと、スプラッシュスクリーンをもっと簡単に変更することができます。

- [flutter_native_splash](https://pub.dev/packages/flutter_native_splash){:rel="nofollow noreferrer" target="_blank"}

## イメージファイル準備

公式ドキュメントにはイメージファイルに関して特に書いてありません。私は下記のようなイメージを使いました。

- PNGファイル
- 3000px X 3000pxサイズ以上のイメージ

準備したファイルを`assets/splash.png`に保存します。

## flutter_native_splashインストール

flutter_native_splashパッケージを使うためにはflutter_native_splashパッケージをインストールする必要があります。次のコマンドを実行してflutter_native_splashパッケージをインストールします。

```bash
flutter pub add flutter_native_splash
```

## スプラッシュイメージ設定

次はスプラッシュスクリーンで使うイメージファイルを設定する必要があります。`pubspec.yaml`ファイルを開いて下記の内容をファイル下に追加します。

```yaml
...
flutter_native_splash:
  color: "#FFFFFF"
  image: assets/splash.png
  fullscreen: true
```

## flutter_native_splashパッケージオプション

flutter_native_splashパッケージは色んなオプションを持っています。

- color: スプラッシュスクリーンの背景の色
- background_image: スプラッシュスクリーンの背景イメージ
- image: スプラッシュスクリーンのイメージ
- color_dark: デバイス設定がダークモードの時の背景の色
- background_image_dark: デバイス設定がダークモードの場合の背景イメージ
- image_dark: デバイス設定がダークモードの場合のスプラッシュスクリーンのイメージ
- android_gravity: アンドロイドのスプラッシュイメージの位置を設定します。(bottom, center, center_horizontal, center_vertical, clip_horizontal, clip_vertical, end, fill, fill_horizontal, fill_vertical, left, right, start, top)
- ios_content_mode: iOSでスプラッシュイメージの位置を設定します。(scaleToFill, scaleAspectFit, scaleAspectFill, center, top, bottom, left, right, topLeft, topRight, bottomLeft, bottomRight)
- web_image_mode: ウェブでスプラッシュイメージの位置を設定します。(center, contain, stretch, cover)
- fullscreen: スプラッシュスクリーンをフールスクリーンで表示する(true, false)
- info_plist_files: info.plistの名前を変更した場合、当該ファイルを設定するためオプション

## スプラッシュイメージ生成

flutter_native_splashパッケージのオプションを設定したら、次のコマンドを実行してスプラッシュイメージを生成します。

```bash
flutter pub run flutter_native_splash:create
```

{% include in-feed-ads.html %}

## Tip

flutter_native_splashパッケージを使ってスプラッシュイメージを生成したら、特に修正しなくてもスプラッシュスクリーンが表示されます。

スプラッシュスクリーンを次のTipと一緒に使うとより便利です。

### 初期データ

普通スプラッシュスクリーンを画面に表示した後、初期データを持ってきます。この時次のように`Future`と`async-await`を使ってスプラッシュスクリーンを表示した状態でデータを取ってくることができます。

```dart
import 'package:flutter/material.dart';

Future<void> main() async {
  bool data = await fetchData();
  print(data);

  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Home(),
    );
  }
}

Future<bool> fetchData() async {
  bool data = false;

  // Change to API call
  await Future.delayed(Duration(seconds: 3), () {
    data = true;
  });

  return data;
}
...
```

`main`関数を`async-await`で変更した後、`runApp`を使って、アプリを実行する前データを取ってきます。この構造にすると、スプラッシュスクリーンを表示した状態でデータを取ってくることができます。

### ステータスバー

このブログポストでは`pubspec.yaml`へ`fullscreen: true`を設定してスプラッシュスクリーンを生成しました。flutter_native_splashのバグか分からないですが、iOSではアプリが実行された後、ステータスバー(Status Bar)が表示されません。それで、次のようにコードを修正してステータスバーを表示します。

```dart
...
import 'package:flutter/services.dart';
...
class Home extends StatelessWidget {
  Home() {
    SystemChrome.setEnabledSystemUIOverlays(SystemUiOverlay.values);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Home'),
      ),
      body: Center(
        child: Text('Hello world!'),
      ),
    );
  }
}
```

## 完了

これでFlutterでスプラッシュスクリーンを変更する方法についてみてみました。`flutter_native_splash`パッケージを使うとこのようにもっと簡単にFlutterアプリのスプラッシュスクリーンを変更することができます。
