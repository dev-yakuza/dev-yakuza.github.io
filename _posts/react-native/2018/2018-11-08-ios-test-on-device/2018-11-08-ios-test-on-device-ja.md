---
layout: 'post'
permalink: '/react-native/ios-test-on-device/'
paginate_path: '/react-native/:num/ios-test-on-device/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'iOSデバイステスト'
description: 'リアクトネイティブ(React Native)で開発したプロジェクトをiOSデバイスでテストしてみましょう。'
image: '/assets/images/category/react-native/ios-test-on-device.jpg'
---

<div id="contents_list" markdown="1">

## 目次

1. [概要](#概要)
1. [iOS / Mac](#ios--mac)
    - [開発アカウント生成](#開発アカウント生成)
    - [デバイステスト](#デバイステスト)
1. [参考](#参考)

</div>

## 概要

リアクトネイティブ(React Native)で開発したプロジェクトをシミュレータでテストすることは大変ですね。今まで開発したリアクトネイティブ(React Native)プロジェkとをシミュレータではなくデバイスでテストしてみましょう。

このブログはシリーズです。下記のブログも確認してください。

- [iOSビルドやテスト]({{site.url}}/{{page.categories}}/ios-running-on-device/){:target="_blank"}
- [iOS開発者登録]({{site.url}}/{{page.categories}}/ios-enroll-developer-program/){:target="_blank"}
- [iOS証明書(Certification)]({{site.url}}/{{page.categories}}/ios-certification/){:target="_blank"}
- [iOS TestFlight]({{site.url}}/{{page.categories}}/ios-testflight/){:target="_blank"}
- [iOS App store 登録]({{site.url}}/{{page.categories}}/ios-app-store/){:target="_blank"}
- [Fastlaneを使ってアプリのデプロイを自動化する]({{site.url}}/{{page.categories}}/fastlane/){:target="_blank"}

リアクトネイティブ(React Native)をアンドロイド(Android)デバイスでテストする方法が知りたい方は[アンドロイドデバイステスト]({{site.url}}/{{page.categories}}/android-test-on-device/){:target="_blank"}を確認してください。

{% include in-feed-ads.html %}

## iOS / Mac

アイホンでテストするためにはMacが必要です。Mac、iOSデバイス(アイホン)とテストしたいプロジェクトを準備します。

![prepare iphone mac](/assets/images/category/react-native/ios-test-on-device/mac-iphone.jpg)

PCでリアクトネイティブ(React Native)の開発環境を設定する方法が知りたい方は以前のブログ[リアクトネイティブ(React Native)インストール]({{site.url}}/{{page.categories}}/installation/){:target="_blank"}を参考してください。

### 開発アカウント生成

デバイスでテストするためにはアップル開発者アカウント(Apple developer account)が必要です。開発者登録じゃなくアカウントの生成なので無料で使うことが可能です。アップル開発者アカウントがある方はこの項目はスキップしても構わないです。

下のリンクを押してアップル開発者アカウント(Apple developer account)生成サイトに行きます。

- アップル開発者アカウント(Apple developer account): [https://developer.apple.com/](https://developer.apple.com/){:rel="nofollow noreferrer" target="_blank"}

![apple developer site](/assets/images/category/react-native/ios-test-on-device/apple-developer-site.jpg)

右上の```account```メニューを押します。

![apple developer site login](/assets/images/category/react-native/ios-test-on-device/apple-developer-site-login.jpg)

アップルアカウントがある方はログインしてください。アカウントがない方は```Create Apple ID```でアップルアカウントを作ります。アップル開発者アカウントじゃなくアップルアカウントです。アイホンでアプリをダウンロードする時使ってるアカウントでログインすればいいです。

![agreement](/assets/images/category/react-native/ios-test-on-device/agreement.jpg)

アップル開発者アカウントを使うための利用規約です。```By checking this box I confirm that I have read and agree to be bound by the Agreement above.```を押して同意して```Submit```を押して次のページへ遷移します。

![completed to create developer account](/assets/images/category/react-native/ios-test-on-device/completed-create-account.jpg)

アップル開発者アカウント(Apple developer account)の生成が終わりました。

{% include in-feed-ads.html %}

### デバイステスト

公式サイト([react native](https://facebook.github.io/react-native/docs/running-on-device){:rel="nofollow noreferrer" target="_blank"})へ全ての内容が詳しく載せております。やってみましょう。

1. USBを使ってテストしたいデバイスとMacを接続します。
1. リアクトネイティブ(React Native)プロジェクトがあるフォルダへ```ios/[プロジェクト名].xcodeproj```ファイルを実行します。
1. xcodeが実行されたら左上のプロジェクト名を選択してプロジェクト名の右へある画面上の```General```タブを選択します。スクロールしてちょっと下に行くと```Signing```の項目が見えます。```Team```の項目の右へある```Add an Account...```ボタンを押します。

    ![signing in xcode](/assets/images/category/react-native/ios-test-on-device/signing.jpg)

    上部で作ったアップル開発者アカウント(Apple developer account)のID/PWを入力して```Next```ボタンを押します。

    ![login signing in xcode](/assets/images/category/react-native/ios-test-on-device/signing-login.jpg)

    ログイン後に出る画面の下にある```Download Manual Profiles```ボタンを押して後ウィンドウを閉じます。そしたら```Team```の横にある項目がドロップダウンメニューになったことが分かります。ドロップダウンメニューを開いて上で追加したアイディを選択します。

    ![signing error in xcode](/assets/images/category/react-native/ios-test-on-device/signing-error.jpg)

    上のようなエラーが出る方はxcodeの同じ画面の上の所にある```Identity```の```Bundle Identifier```を変更てください。

    ![signing error solve in xcode](/assets/images/category/react-native/ios-test-on-device/signing-error-solve.jpg)

    左にある```Targets```の項目で ```プロジェクト名Tests```を選択して```Team```横にあるドロップダウンメニューを押して```signing```(アイディを選択)をします。

    ![signing test target in xcode](/assets/images/category/react-native/ios-test-on-device/signing-target-test.jpg)
1. 左上のシミュレータを選択するところでUSBで接続してるデバイスに変更して矢印を押してプロジェクトを実行します。

    ![device test in xcode](/assets/images/category/react-native/ios-test-on-device/device-test.jpg)

    注意：これはデバイスでテストするためのビルドです。したがって、シミュレータと同じようにPCへリアクトネイティブ(React Native)の開発サーバーが立ち上がってそのサーバーとデバイスが連動してテストが出来る仕組みです。したがって同じWifi/ネットワークの環境じゃないとデバイスがサーバーを見つかれないのでテストが出来ないです。

1. ビルドが無事に終わったら下記のようなメッセージが出ます。

    ![security error](/assets/images/category/react-native/ios-test-on-device/security-error.jpg)

    詳しく説明があるのでやってみましょう。デバイスの```設定```を実行します。```一般```を選択して ```プロファイルとデバイス管理```を選択します。```デベロッパAPP```項目にある自分のアップル開発アカウント(Apple developer account)を選択します。 ```APPを検証```を押します。その後xcodeに戻ってもう一回矢印を押してプロジェクトを実行して上手く起動することを確認します。

## 参考

- 公式サイト: [react native](https://facebook.github.io/react-native/docs/running-on-device){:rel="nofollow noreferrer" target="_blank"}

