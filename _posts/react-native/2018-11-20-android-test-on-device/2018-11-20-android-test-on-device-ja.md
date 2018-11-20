---
layout: 'post'
permalink: '/react-native/android-test-on-device/'
paginate_path: '/react-native/:num/android-test-on-device/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'アンドロイドデバイステスト'
description: 'RN(react native)で開発したプロジェクトをアンドロイド(Android)デバイスでテストしてみましょう。'
image: '/assets/images/category/react-native/android-test-on-device.jpg'
---


## 概要
アンドロイド(Android)開発する時やっぱりエミュレータで開発はきついですね。RN(react native)をアンドロイド用に開発する時エミュレータではなくアンドロイド(Android)デバイスでテストできるように設定してみます。RN(react native)をiOSデバイスでテストする方法が知りたい方は以前のブログ[iOSデバイステスト]({{site.url}}/{{page.categories}}/ios-test-on-device/){:target="_blank"}を確認してください。

## 準備物
当然な話ですがRN(react native)プロジェクトをアンドロイド(Android)デバイスでテストするためには下記の準備物が必要です。

- アンドロイドスタジオ(Android Studio)
- アンドロイド(Android)デバイス
- RN(react native)プロジェクト

PCへRN(react native)開発環境を設定する方法が知りたい方は以前のブログ[RNインストル]({{site.url}}/{{page.categories}}/installation/){:target="_blank"}を参考してください。

## アンドロイドデバイステスト
RN(react native)の公式サイトへRN(react native)をアンドロイド(Android)でテストする方法が詳しく載せています。それをみながらやってみましょう。

- 公式サイト: [https://facebook.github.io/react-native/docs/running-on-device](https://facebook.github.io/react-native/docs/running-on-device){:rel="nofollow noreferrer" target="_blank"}

## アンドロイドデバイス設定
使ってるアンドロイド(Android)デバイスの開発者オプションを有効化する必要があります。アンドロイド(Android)デバイスの```設定``` > ```デバイス情報```の```ビルド番号```を何回か押すと開発者オプションが有効化されます。

開発者オプションが有効化されたら、```USBデバッグ```機能を有効化する必要があります。```設定``` > ```開発オプション``` > ```USBデバッグ```メニューを選択してUSBデバッグ機能を有効化させます。

## アンドロイドデバイス接続
アンドロイド(Android)デバイスをUSBを使ってPCと接続します。アンドロイド(Android)デバイスでUSBでデバッグを許可するか聞かれたら許可してテストできる状態を作ります。

## アンドロイドデバイスで実行
アンドロイド(Android)デバイスが接続された状態でアンドロイドスタジオ(Android Studio)を実行して左上の```Debug app```ボタン(虫の上に矢印があるボタン)を押したらエミュレータ以外にも自分のデバイスが見えます。自分のデバイスを押して```OK```ボタンを押したら開発したRN(react native)アプリが起動されることが確認できます。

注意：これはデバイスでテストするための実行です。したがって、エミュレータと同じようにPCへRN(react native)の開発サーバーが立ち上がってそのサーバーとデバイスが連動してテストが出来る仕組みです。したがって同じWifi/ネットワークの環境じゃないとデバイスがサーバーを見つかれないのでテストが出来ないです。

## 完了
アンドロイド(Android)デバイスでRN(react native)を起動する方法を紹介しました。今からは実際のデバイスでテストしてみてください。