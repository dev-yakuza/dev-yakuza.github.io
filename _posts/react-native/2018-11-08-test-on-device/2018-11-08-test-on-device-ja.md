---
layout: 'post'
permalink: '/react-native/test-on-device/'
paginate_path: '/react-native/:num/test-on-device/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'デバイステスト'
description: 'RN(react native)で開発したプロジェクトをデバイスでテストしてみましょう。'
image: '/assets/images/category/react-native/test-on-device.jpg'
---


## 概要
RN(react native)で開発したプロジェクトをシミュレータでテストすることは大変ですね。今まで開発したRN(react native)プロジェkとをシミュレータではなくデバイスでテストしてみましょう。

## iOS / Mac
アイホンでテストするためにはMacが必要です。Mac、iOSデバイス(アイホン)とテストしたいプロジェクトを準備します。

![prepare iphone mac](/assets/images/category/react-native/test-on-device/mac-iphone.jpg)

### 開発アカウント生成
デバイスでテストするためにはアップル開発者アカウント(Apple developer account)が必要です。開発者登録じゃなくアカウントの生成なので無料で使うことが可能です。アップル開発者アカウントがある方はこの項目はスキップしても構わないです。

下のリンクを押してアップル開発者アカウント(Apple developer account)生成サイトに行きます。

- アップル開発者アカウント(Apple developer account): [https://developer.apple.com/](https://developer.apple.com/){:rel="nofollow noreferrer" :target="_blank"}

![apple developer site](/assets/images/category/react-native/test-on-device/apple-developer-site.png)

右上の```account```メニューを押します。

![apple developer site login](/assets/images/category/react-native/test-on-device/apple-developer-site-login.png)

アップルアカウントがある方はログインしてください。アカウントがない方は```Create Apple ID```でアップルアカウントを作ります。アップル開発者アカウントじゃなくアップルアカウントです。アイホンでアプリをダウンロードする時使ってるアカウントでログインすればいいです。

![agreement](/assets/images/category/react-native/test-on-device/agreement.png)

アップル開発者アカウントを使うための利用規約です。```By checking this box I confirm that I have read and agree to be bound by the Agreement above.```を押して同意して```Submit```を押して次のページへ遷移します。

![completed to create developer account](/assets/images/category/react-native/test-on-device/completed-create-account.png)

アップル開発者アカウント(Apple developer account)の生成が終わりました。

### デバイステスト
公式サイト([react native](https://facebook.github.io/react-native/docs/running-on-device){:rel="nofollow noreferrer" :target="_blank"})へ全ての内容が詳しく載せております。やってみましょう。

1. USBを使ってテストしたいデバイスとMacを接続します。
1. RN(react native)プロジェクトがあるフォルダへ```ios/[プロジェクト名].xcodeproj```ファイルを実行します。
1. xcodeが実行されたら左上のプロジェクト名を選択してプロジェクト名の右へある画面上の```General```タブを選択します。スクロールしてちょっと下に行くと```Signing```の項目が見えます。```Team```の項目の右へある```Add an Account...```ボタンを押します。

    ![signing in xcode](/assets/images/category/react-native/test-on-device/signing.png)

    上部で作ったアップル開発者アカウント(Apple developer account)のID/PWを入力して```Next```ボタンを押します。

    ![login signing in xcode](/assets/images/category/react-native/test-on-device/signing-login.png)

    ログイン後に出る画面の下にある```Download Manual Profiles```ボタンを押して後ウィンドウを閉じます。そしたら```Team```の横にある項目がドロップダウンメニューになったことが分かります。ドロップダウンメニューを開いて上で追加したアイディを選択します。

    ![signing error in xcode](/assets/images/category/react-native/test-on-device/signing-error.png)

    上のようなエラーが出る方はxcodeの同じ画面の上の所にある```Identity```の```Bundle Identifier```を変更てください。

    ![signing error solve in xcode](/assets/images/category/react-native/test-on-device/signing-error-solve.png)

    左にある```Targets```の項目で ```プロジェクト名Tests```を選択して```Team```横にあるドロップダウンメニューを押して```signing```(アイディを選択)をします。

    ![signing test target in xcode](/assets/images/category/react-native/test-on-device/signing-target-test.png)
1. 左上のシミュレータを選択するところでUSBで接続してるデバイスに変更して矢印を押してプロジェクトを実行します。

    ![device test in xcode](/assets/images/category/react-native/test-on-device/device-test.png)

    注意：これはデバイスでテストするためのビルドです。したがって、シミュレータと同じようにPCへRN(react native)の開発サーバーが立ち上がってそのサーバーとデバイスが連動してテストが出来る仕組みです。したがって同じWifi/ネットワークの環境じゃないとデバイスがサーバーを見つかれないのでテストが出来ないです。

1. ビルドが無事に終わったら下記のようなメッセージが出ます。

    ![security error](/assets/images/category/react-native/test-on-device/security-error.png)

    詳しく説明があるのでやってみましょう。デバイスの```設定```を実行します。```一般```を選択して ```プロファイルとデバイス管理```を選択します。```デベロッパAPP```項目にある自分のアップル開発アカウント(Apple developer account)を選択します。 ```APPを検証```を押します。その後xcodeに戻ってもう一回矢印を押してプロジェクトを実行して上手く起動することを確認します。

## アンドロイド(Android)
私たちがアンドロイド(Android)でテストする時内容を更新します。

## 参考
- 公式サイト: [react native](https://facebook.github.io/react-native/docs/running-on-device){:rel="nofollow noreferrer" :target="_blank"}
