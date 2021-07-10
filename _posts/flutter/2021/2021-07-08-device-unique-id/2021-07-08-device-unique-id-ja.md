---
layout: 'post'
permalink: '/flutter/widget/device-unique-id/'
paginate_path: '/flutter/:num/widget/device-unique-id/'
lang: 'ja'
categories: 'flutter'
comments: true

title: '[Flutter] Device Unique ID'
description: Flutterでユーザの端末のユニークIDを取得するため、device_info_plusパッケージを使う方法について説明します。
image: '/assets/images/category/flutter/background.png'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [device_info_plusのインストール](#device_info_plusのインストール)
- [Device unique IDの取得](#device-unique-idの取得)
- [完了](#完了)

</div>

## 概要

アプリを開発する時、ユーザのデバイスを識別するため、デバイスのユニークID(Device Unique ID)が必要な場合があります。今回のブログポストでは`device_info_plus`パッケージを使ってユーザのデバイスユニークIDを取得する方法について説明します。

- device_info_plus: [https://pub.dev/packages/device_info_plus](https://pub.dev/packages/device_info_plus){:rel="nofollow noreferrer" target="_blank"}

## device_info_plusのインストール

ユーザデバイスのユニークIDを取得するためには、`device_info_plus`パッケージを使う必要があります。`device_info_plus`パッケージを使うため、次のコマンドを実行して`device_info_plus`パッケージをインストールします。

```bash
flutter pub add device_info_plus
```

## Device unique IDの取得

`device_info_plus`パッケージはデバイスのユニークIDを取得する機能は提供してないです。したがって、私たちは`device_info_plus`パッケージの機能を使うためユーザのデバイスユニークIDを生成する関数を作る必要があります。

次はユーザのデバイスユニークIDを取得するため私が使っている関数のコードです。

```dart
Future<String> getDeviceUniqueId() async {
  var deviceIdentifier = 'unknown';
  var deviceInfo = DeviceInfoPlugin();

  if (Platform.isAndroid) {
    var androidInfo = await deviceInfo.androidInfo;
    deviceIdentifier = androidInfo.androidId!;
  } else if (Platform.isIOS) {
    var iosInfo = await deviceInfo.iosInfo;
    deviceIdentifier = iosInfo.identifierForVendor!;
  } else if (Platform.isLinux) {
    var linuxInfo = await deviceInfo.linuxInfo;
    deviceIdentifier = linuxInfo.machineId!;
  } else if (kIsWeb) {
    var webInfo = await deviceInfo.webBrowserInfo;
    deviceIdentifier = webInfo.vendor! +
        webInfo.userAgent! +
        webInfo.hardwareConcurrency.toString();
  }

  return deviceIdentifier;
}
```

上の関数を使うと`iOS`と`Android`だけではなく`Linux`と`Web`でも使えます。

## 完了

これでFlutterで`device_info_plus`パッケージを使ってユーザのデバイスユニークID(Device Unique ID)を取得する方法についてみてみました。皆さんも上のコードを使ってユーザのデバイスユニークIDを取得して使ってみてください。
