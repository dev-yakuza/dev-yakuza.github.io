---
layout: 'post'
permalink: '/flutter/firebase/crashlytics/'
paginate_path: '/flutter/:num/firebase/crashlytics/'
lang: 'ja'
categories: 'flutter'
comments: true

title: '[Flutter] Firebase Crashlytics'
description: 今回のブログポストではFlutterでFirebaseのCrashlyticsを連動して使う方法について説明します。
image: '/assets/images/category/flutter/background.png'
published: false
---

<div id="contents_list" markdown="1">

## 目次

</div>

## 概要

今回のブログポストではFlutterで開発されたアプリが強制終了された時、これを感知するため`Firebase`の`Crashlytics`を設定する方法について紹介します。

- [firebase_crashlytics](https://pub.dev/packages/firebase_crashlytics){:rel="nofollow noreferrer" target="_blank" }

`Firebase`の`Crashlytics`を使うためFlutterプロジェクトに`firebase_crashlytics`を設定して使う方法について説明します。

## ブログシリーズ

このブログはシリーズで作成されております。次のリンクを使って他のブログポストは下記のリンクで確認できます。

- [[Flutter] Firebase Core]({{site.url}}/{{page.categories}}/firebase/core/){:target="_blank"}
- [[Flutter] Firebase Analytics]({{site.url}}/{{page.categories}}/firebase/analytics/){:target="_blank"}
- [Flutter] Firebase Crashlytics

## Firebaseプロジェクト生成や設定

FlutterでFirebaseを使うためにはFirebaseプロジェクトを生成して、`firebase_core`パッケージをインストールする必要があります。下記のリンクで詳しい内容を確認してください。

- [[Flutter] Firebase Core]({{site.url}}/{{page.categories}}/firebase/core/){:target="_blank"}

{% include in-feed-ads.html %}

## Firebaseプロジェクト設定

次はグーグルのファイアベース(Google Firebase)でプロジェクトにCrashlyticsを設定する必要があります。FirebaseのConsoleを移動した後、左メニューで`Crashlytics`を選択します。

![crashlytics add sdk](/assets/images/category/react-native/2020/react-native-firebase-v6-crashlytics/crashlytics-add-sdk.jpg)

上にある`Add SDK`ボタンを押してSDKを追加します。また、上の`Crashlytics`タイトルの横にあるプロジェクトを選択してiOS/アンドロイドを変更して、`Add SDK`を押してiOSとアンドロイド、両方SDKを追加します。

## firebase_crashlyticsインストール

FlutterプロジェクトでFirebase Crashlyticsを使うためには`firebase_crashlytics`パッケージをインストールする必要があります。次のコマンドを実行して`firebase_crashlytics`パッケージをインストールします。

```dart
flutter pub pub add firebase_crashlytics
```

## Gradle修正

FlutterプロジェクトのアンドロイドでCrashlyticsを使うためには`Gradle`ファイルを修正する必要があります。まず、`android/app/build.gradle`ファイルを開いてファイルの下を次のように修正します。

```js
...
apply plugin: 'com.google.gms.google-services'
apply plugin: 'com.google.firebase.crashlytics' // <<<<<<<<<<<<< Add this
```

その後、`android/build.gradle`ファイルを開いて下記のように修正します。

```js
buildscript {
    ...
    dependencies {
        ...
        classpath "org.jetbrains.kotlin:kotlin-gradle-plugin:$kotlin_version"
        classpath 'com.google.gms:google-services:4.3.5'
        classpath 'com.google.firebase:firebase-crashlytics-gradle:2.5.1' // <<<<<<<<<<<<<<<< Add this
    }
}
```

これでFlutterプロジェクトのアンドロイドでCrashlyticsを使う準備ができました。

## firebase_crashlyticsの使い方

Flutterで次のように`firebase_crashlytics`を使うと、アプリが強制終了された時、Firebase Crashlyticsにこれを報告することができます。

```dart
import 'dart:async';
import 'package:firebase_crashlytics/firebase_crashlytics.dart';

Future<void> main() async {

  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();

  runZonedGuarded(() {
    runApp(MyApp());
  }, FirebaseCrashlytics.instance.recordError);
}
```

`runZonedCuarded`を使って、アプリが実行中強制終了された時Firebase Crashlyticsに報告するように設定しました。

{% include in-feed-ads.html %}

## 強制終了テスト

次のコードを使うとアプリを強制終了させることができます。

```dart
FirebaseCrashlytics.instance.crash();
```

このコードをボタンや画面の移動などのイベントに連結して、アプリを強制終了させます。アプリが強制終了されたら、またアプリを実行してFirebase Crashlyticsに報告するようにします。

アプリの強制終了テストは端末で実行しなければならないし、強制終了後、Firebase Crashlyticsに報告できるように必ずアプリを再起動しなければならないです。

このように強制終了をしてFirebase Crashlyticsに報告をしたら、FirebaseのCrashlytics画面が次のように変更されたことが確認できます。

![crashlytics integration](/assets/images/category/react-native/2020/react-native-firebase-v6-crashlytics/crashlytics-integration.jpg)

## アンドロイドのmultiDexEnabled

`firebase_crashlytics`をインストールしてFlutterプロジェクトをアンドロイドで実行した時、`Debug Console`に次のようなエラーが発生しました。

```bash
Note: .pub-cache/hosted/pub.dartlang.org/firebase_core-1.0.4/android/src/main/java/io/flutter/plugins/firebase/core/FlutterFirebaseCorePlugin.java uses or overrides a deprecated API.
Note: Recompile with -Xlint:deprecation for details.
Note: Some input files use or override a deprecated API.
Note: Recompile with -Xlint:deprecation for details.
Note: .pub-cache/hosted/pub.dartlang.org/flutter_tts-3.0.0/android/src/main/java/com/tundralabs/fluttertts/FlutterTtsPlugin.java uses or overrides a deprecated API.
Note: Recompile with -Xlint:deprecation for details.

Note: .pub-cache/hosted/pub.dartlang.org/firebase_crashlytics-2.0.1/android/src/main/java/io/flutter/plugins/firebase/crashlytics/FlutterFirebaseCrashlyticsPlugin.java uses or overrides a deprecated API.
Note: Recompile with -Xlint:deprecation for details.
Note: .pub-cache/hosted/pub.dartlang.org/firebase_analytics-8.0.1/android/src/main/java/io/flutter/plugins/firebaseanalytics/FirebaseAnalyticsPlugin.java uses or overrides a deprecated API.
Note: Recompile with -Xlint:deprecation for details.
Note: .pub-cache/hosted/pub.dartlang.org/firebase_analytics-8.0.1/android/src/main/java/io/flutter/plugins/firebaseanalytics/FirebaseAnalyticsPlugin.java uses unchecked or unsafe operations.
Note: Recompile with -Xlint:unchecked for details.
```

これを解決するためには`multiDexEnabled`をアクティブにする必要があります。`android/app/build.gradle`ファイルを開いて下記のように修正します。

```js
defaultConfig {
    ...
    minSdkVersion 21
    targetSdkVersion 30
    versionCode flutterVersionCode.toInteger()
    versionName flutterVersionName
    multiDexEnabled true // <<<<<<<<<< Add this
}
```

## 完了

これでFLutterでFirebase Crashlyticsを使うためFlutterプロジェクトに`firebase_crashlytics`を設定する方法についてみてみました。これからFirebase Crashlyticsを使って開発したアプリの強制終了を分析してみてください。
