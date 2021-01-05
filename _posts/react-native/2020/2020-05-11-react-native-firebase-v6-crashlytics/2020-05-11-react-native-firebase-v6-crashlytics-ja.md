---
layout: 'post'
permalink: '/react-native/react-native-firebase-v6-crashlytics/'
paginate_path: '/react-native/:num/react-native-firebase-v6-crashlytics/'
lang: 'ja'
categories: 'react-native'
comments: true

title: react-native-firebase V6 Crashlytics
description: react-native-firebase(V6)を使ってFirebaseのCrashlyticsを使う方法について説明します。
image: '/assets/images/category/react-native/2020/react-native-firebase-v6-crashlytics/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [react-natiev-firebaseのインストールや準備](#react-natiev-firebaseのインストールや準備)
- [ライブラリインストール](#ライブラリインストール)
- [Firebaseプロジェクト設定](#firebaseプロジェクト設定)
  - [アンドロイドの設定](#アンドロイドの設定)
  - [iOSの設定](#iosの設定)
- [完了](#完了)

</div>

## 概要

React Nativeプロジェクトで[Firebase](https://firebase.google.com/){:rel="nofollow noreferrer" target="_blank"}の[Crashlytics](https://firebase.google.com/docs/crashlytics){:rel="nofollow noreferrer" target="_blank"}を使うため`react-native-firebase`を使う方法にてついて説明します。

- react-native-firebase(V6): [https://rnfirebase.io/](https://rnfirebase.io/){:rel="nofollow noreferrer" target="_blank"}

このブログポストはシリーズで作成されております。他の内容を確認したい方は下記のブログリストを参考してください。

- [react-native-firebase V6 インストール]({{site.url}}/{{page.categories}}/react-native-firebase-v6-installation/){:target="_blank"}
- react-native-firebase V6 Crashlytics
- [react-native-firebase V6 Admob]({{site.url}}/{{page.categories}}/react-native-firebase-v6-admob/){:target="_blank"}

react-native-firebaseの以前のバージョン(V5)を使う方法については下記のブログリストを参考してください。

- [Firebase Analytics]({{site.url}}/{{page.categories}}/react-native-firebase-analytics/){:target="_blank"}
- [Firebase Crashlytics]({{site.url}}/{{page.categories}}/firebase-crashlytics/){:target="_blank"}
- [Firebase Admob]({{site.url}}/{{page.categories}}/react-native-firebase-admob/){:target="_blank"}
- [react-native-firebase(V5)を使ってPush Message]({{site.url}}/{{page.categories}}/react-native-firebase-fcm/){:target="_blank"}

## react-natiev-firebaseのインストールや準備

下記のブログを参考してreact-native-firebaseをインストールして、Firebaseプロジェクトを生成します。

- [react-native-firebase V6 インストール]({{site.url}}/{{page.categories}}/react-native-firebase-v6-installation/){:target="_blank"}

## ライブラリインストール

下記のコマンドを使って`react-native-firebase`の`Crashlytics`をインストールします。

```bash
npm install --save @react-native-firebase/crashlytics
```

下記のコマンドを使ってiOSプロジェクトへreact-native-firebaseのCrashlyticsを連結します。

```bash
cd ios
pod install
```

## Firebaseプロジェクト設定

次はGoogleのファイアベース(Google Firebase)でプロジェクトへCrashlyticsを設定する必要があります。FirebaseのConsoleへ移動して、左のメニューで`Crashlytics`を選択します。

![crashlytics add sdk](/assets/images/category/react-native/2020/react-native-firebase-v6-crashlytics/crashlytics-add-sdk.jpg)

上にある`Add SDK`ボタンを押してSDKを追加します。そして、`Crashlytics`のタイトル横にあるプロジェクトを選択してiOS/アンドロイドで変更して、`Add SDK`を押してiOS、アンドロイド、両方へSDKを追加します。

### アンドロイドの設定

アンドロイドでは`Crashlytics`を使うため、`android/build.gradle`ファイルを開いて下記のように修正します。

```js
buildscript {
    ...
    dependencies {
        ...
        classpath 'com.google.gms:google-services:4.3.4'
        classpath 'com.google.firebase:firebase-crashlytics-gradle:2.4.1'
    }
}
```

そして`android/app/build.gradle`ファイルを開いて下記のように修正します。

```js
apply plugin: 'com.android.application'

apply plugin: 'com.google.gms.google-services'
apply plugin: 'com.google.firebase.crashlytics'
...
```

### iOSの設定

iOSはアンドロイドは違って特に設定をする必要がありません。

## 完了

これでFirebaseのCrashlyticsを使うため、react-native-firebaseライブラリを使う方法を説明しました。

![crashlytics integration](/assets/images/category/react-native/2020/react-native-firebase-v6-crashlytics/crashlytics-integration.jpg)

react-native-firebaseでCrashlyticsをうまく設定して、React Nativeプロジェクトを実行すると、上のような画面が確認できます。