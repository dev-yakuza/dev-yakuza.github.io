---
layout: 'post'
permalink: '/react-native/android-test-on-device/'
paginate_path: '/react-native/:num/android-test-on-device/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'アンドロイドデバイステスト'
description: 'リアクトネイティブ(React Native)で開発したプロジェクトをアンドロイド(Android)デバイスでテストしてみましょう。'
image: '/assets/images/category/react-native/android-test-on-device.jpg'
---

<div id="contents_list" markdown="1">

## 目次

1. [概要](#概要)
1. [準備物](#準備物)
1. [アンドロイドデバイステスト](#アンドロイドデバイステスト)
1. [アンドロイドデバイス設定](#アンドロイドデバイス設定)
1. [アンドロイドデバイス接続](#アンドロイドデバイス接続)
1. [アンドロイドデバイスで実行](#アンドロイドデバイスで実行)
1. [アンドロイド5.0バージョン以下](#アンドロイド50バージョン以下)
1. [完了](#完了)

</div>

## 概要

アンドロイド(Android)開発する時やっぱりエミュレータで開発はきついですね。リアクトネイティブ(React Native)をアンドロイド用に開発する時エミュレータではなくアンドロイド(Android)デバイスでテストできるように設定してみます。リアクトネイティブ(React Native)をiOSデバイスでテストする方法が知りたい方は以前のブログ[iOSデバイステスト]({{site.url}}/{{page.categories}}/ios-test-on-device/){:target="_blank"}を確認してください。

このブログはシリーズです。下記のブログも確認してください。

- [アンドロイドビルドやテスト]({{site.url}}/{{page.categories}}/android-running-on-device/){:target="_blank"}
- [アンドロイド開発者登録]({{site.url}}/{{page.categories}}/android-enroll-google-play-developer/){:target="_blank"}
- [アンドロイドアプリストア登録]({{site.url}}/{{page.categories}}/android-google-play/){:target="_blank"}
- [Fastlaneを使ってアプリのデプロイを自動化する]({{site.url}}/{{page.categories}}/fastlane/){:target="_blank"}

## 準備物

当然な話ですがリアクトネイティブ(React Native)プロジェクトをアンドロイド(Android)デバイスでテストするためには下記の準備物が必要です。

- アンドロイドスタジオ(Android Studio)
- アンドロイド(Android)デバイス
- リアクトネイティブ(React Native)プロジェクト

PCへリアクトネイティブ(React Native)開発環境を設定する方法が知りたい方は以前のブログ[RNインストル]({{site.url}}/{{page.categories}}/installation/){:target="_blank"}を参考してください。

{% include in-feed-ads.html %}

## アンドロイドデバイステスト

リアクトネイティブ(React Native)の公式サイトへリアクトネイティブ(React Native)をアンドロイド(Android)でテストする方法が詳しく載せています。それをみながらやってみましょう。

- 公式サイト: [https://facebook.github.io/react-native/docs/running-on-device](https://facebook.github.io/react-native/docs/running-on-device){:rel="nofollow noreferrer" target="_blank"}

## アンドロイドデバイス設定

使ってるアンドロイド(Android)デバイスの開発者オプションを有効化する必要があります。アンドロイド(Android)デバイスの```設定``` > ```デバイス情報```の```ビルド番号```を何回か押すと開発者オプションが有効化されます。

開発者オプションが有効化されたら、```USBデバッグ```機能を有効化する必要があります。```設定``` > ```開発オプション``` > ```USBデバッグ```メニューを選択してUSBデバッグ機能を有効化させます。

## アンドロイドデバイス接続

アンドロイド(Android)デバイスをUSBを使ってPCと接続します。アンドロイド(Android)デバイスでUSBでデバッグを許可するか聞かれたら許可してテストできる状態を作ります。

## アンドロイドデバイスで実行

アンドロイド(Android)デバイスが接続された状態でアンドロイドスタジオ(Android Studio)を実行して左上の```Debug app```ボタン(虫の上に矢印があるボタン)を押したらエミュレータ以外にも自分のデバイスが見えます。自分のデバイスを押して```OK```ボタンを押したら開発したリアクトネイティブ(React Native)アプリが起動されることが確認できます。

注意：これはデバイスでテストするための実行です。したがって、エミュレータと同じようにPCへリアクトネイティブ(React Native)の開発サーバーが立ち上がってそのサーバーとデバイスが連動してテストが出来る仕組みです。したがって同じWifi/ネットワークの環境じゃないとデバイスがサーバーを見つかれないのでテストが出来ないです。

{% include in-feed-ads.html %}

## アンドロイド5.0バージョン以下

テストするデバイスがアンドロイド(Android)バージョン5.0以下の場合、別の設定をする必要があります。下記にある設定で私たちはアンドロイド4.4.2でリアクトネイティブ(React Native)プロジェクトを起動してテストしました。

リアクトネイティブ(React Native)プロジェクトフォルダで```android/app/build.gradle```ファイルを下記のように修正します。

```xml
defaultConfig {
    ...
    ndk {
        // abiFilters "armeabi-v7a", "x86"
    }
}
```

アンドロイドスタジオ(Android Studio)を開いて```gradle```を```sync```ボタンを押して同期化します。同期化が完了されたらリアクトネイティブ(React Native)プロジェクトを実行します。

```bash
react-native run-android
```

リアクトネイティブ(React Native)のサーバーがPCで実行されてデバイスにもアプリが上手くインストールされますが、赤画面のエラーが出ます。

デバイスを振って開発者メニュー(Developer Menu)を開きます。開発者メニューで```Dev Settings``` > ```Debug server host & port for device```を選択します。IPアドレスとポート(Port)を入力する画面が出ます。そこに自分のIPと8081ポートを入力します。(ex> 10.0.1.1:8081)また開発者メニューへ戻って```Reload JS```を押してプロジェクトを再起動します。

## 完了

アンドロイド(Android)デバイスでリアクトネイティブ(React Native)を起動する方法を紹介しました。今からは実際のデバイスでテストしてみてください。
