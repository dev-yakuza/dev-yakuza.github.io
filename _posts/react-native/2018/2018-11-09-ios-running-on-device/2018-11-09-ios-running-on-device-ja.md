---
layout: 'post'
permalink: '/react-native/ios-running-on-device/'
paginate_path: '/react-native/:num/ios-running-on-device/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'iOSビルドやテスト'
description: 'リアクトネイティブ(React Native)で開発したプロジェクトをiOS用でビルドしてデバイスでテストしてみましょう。'
image: '/assets/images/category/react-native/ios-running-on-device.jpg'
---

<div id="contents_list" markdown="1">

## 目次

1. [概要](#概要)
1. [iOS / Mac](#ios--mac)
    - [リリースビルド準備](#リリースビルド準備)
        - [HTTPS通信の設定](#https通信の設定)
        - [Location権限説明追加](#location権限説明追加)
        - [ビルドスキマ変更](#ビルドスキマ変更)
        - [デバイスで起動](#デバイスで起動)
1. [参考](#参考)

</div>

## 概要

以前のブログでリアクトネイティブ(React Native)で開発したプロジェクトをデバイスでテストしてみました。([デバイステスト]({{site.url}}/{{page.categories}}/ios-test-on-device/){:target="_blank"}) 皆さん、特に問題ありませんでしたか？今まで結構テストしたのでリアクトネイティブ(React Native)のプロジェクトをリリースするためビルドして実際のデバイスでテストしてみます。

このブログはシリーズです。下記のブログも確認してください。

- [iOSデバイステスト]({{site.url}}/{{page.categories}}/ios-test-on-device/){:target="_blank"}
- [iOS開発者登録]({{site.url}}/{{page.categories}}/ios-enroll-developer-program/){:target="_blank"}
- [iOS証明書(Certification)]({{site.url}}/{{page.categories}}/ios-certification/){:target="_blank"}
- [iOS TestFlight]({{site.url}}/{{page.categories}}/ios-testflight/){:target="_blank"}
- [iOS App store 登録]({{site.url}}/{{page.categories}}/ios-app-store/){:target="_blank"}
- [Fastlaneを使ってアプリのデプロイを自動化する]({{site.url}}/{{page.categories}}/fastlane/){:target="_blank"}

ここではリアクトネイティブ(React Native)のプロジェクトをビルドする方法とビルドしたファイルをテストデバイスへアップして確認する方法について説明します。実際マーケットへアップロードする内容は含まれてないです。

## iOS / Mac

開発者アカウント生成とデバイスとの連携は以前のブログを参考してください。([デバイステスト]({{site.url}}/{{page.categories}}/ios-test-on-device/){:target="_blank"}) ここにはリアクトネイティブ(React Native)のプロジェクトをリリースするためのビルド方法とビルドしたファイルをデバイスでテストする方法について紹介します。

{% include in-feed-ads.html %}

### リリースビルド準備

公式サイト([react-native](https://facebook.github.io/react-native/docs/ios-running-on-device#building-your-app-for-production){:rel="nofollow noreferrer" target="_blank"})へ全ての説明があります。それを見ながらやってみます。

#### HTTPS通信の設定

アップルはアプリが外部のシステムと```HTTP```通信をする時```HTTPS```で通信しないとダメになる機能を入れました。しかし、リアクトネイティブ(React Native)を開発する時はPCに開発サーバーを立ち上げてそのサーバーと通信してアプリを起動するのでリアクトネイティブ(React Native)は基本この機能を無効化してます。実際ビルドしてリリースすると開発サーバーとは通信しないのでこの無効化してる部分を消す必要があります。リアクトネイティブ(React Native)のプロジェクトフォルダから```/ios/プロジェクト名/info.plist```のファイルを開いて下記の部分を探して消します。

```xml
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
    <key>NSExceptionDomains</key>
    <dict>
        <key>localhost</key>
        <dict>
            <key>NSExceptionAllowsInsecureHTTPLoads</key>
            <true/>
        </dict>
    </dict>
</dict>
```

注意：また開発する時はこの部分を復元する必要があります。上で説明したけど、開発する時は開発サーバー(localhost)との通信はHTTPでするからです。

アプリでHTTPSプロトコルじゃなくHTTPプロトコルで通信をする必要がある方は下記のようにlocalhostの部分だけ消します。

```xml
<key>NSAppTransportSecurity</key>
<dict>
  <key>NSAllowsArbitraryLoads</key>
      <true/>
</dict>
```

{% include in-feed-ads.html %}

#### Location権限説明追加

リアクトネイティブ(React Native)の`info.plist`を確認したら下記のようにLocaionと関係ある設定があります。과 관련된 설정이 있습니다.

```xml
<key>NSLocationWhenInUseUsageDescription</key>
<string></string>
```

使ってない場合は削除しても良いですが、私は広告のため位置情報を使ってるので下記のように修正しました。

```xml
<key>NSLocationAlwaysAndWhenInUseUsageDescription</key>
<string>$(PRODUCT_NAME) needs Location access for useful advertisement</string>
<key>NSLocationAlwaysUsageDescription</key>
<string>$(PRODUCT_NAME) needs Location access for useful advertisement</string>
<key>NSLocationWhenInUseUsageDescription</key>
<string>$(PRODUCT_NAME) needs Location access for useful advertisement</string>
```

この部分を修正しないとアプリをアプリストアコネクト(Appstore Connector)にアプローどする時問題が発生します。

#### ビルドスキマ変更

リアクトネイティブ(React Native)のプロジェクトをビルドするためにはビルドスキマ(build schme)を```Debug```から```Release```で変更する必要があります。リアクトネイティブ(React Native)のプロジェクトがあるフォルダから```ios/プロジェクト名.xcodeproj```ファイルを実行します。

xcodeが実行されたら上部のメニューから```Product```メニューの```Scheme```メニューで```Edit Scheme```を選択します。

![change build scheme](/assets/images/category/react-native/ios-running-on-device/change-scheme.jpg)

下記のような画面が表示されたら左の```Run```を選択して右の```Build Configuration```を```Debug```から```Release```に変更して下の```Close```ボタンを押します。

![change build scheme to Release from Debug](/assets/images/category/react-native/ios-running-on-device/change-debug-to-release.jpg)

注意:ここもまた開発する時は```Release```から```Debug```に戻せる必要があります。

{% include in-feed-ads.html %}

#### デバイスで起動

全ての設定が終わりました。リアクトネイティブ(React Native)をビルドする前にデバイスで確認してみましょう。デバイスでテストした時と同じようにUSBでMacとアイホンを接続してビルドターゲットをデバイスで設定した後、矢印を押して実行します。

![device test](/assets/images/category/react-native/ios-running-on-device/device-test.jpg)

デバイステストとは違ってjs(javascript)がビルドされたbundleファイルを使うのでMacとアイホンが同じWifi/Network上へある必要とインストールした後デバイスがMacと接続してる必要がありません。しかし、正式にインストールではないので一定期間が経過すると、そのアプリを使うことが出来ません。

{% include in-feed-ads.html %}

## 参考

- 公式サイト: [react native](https://facebook.github.io/react-native/docs/ios-running-on-device){:rel="nofollow noreferrer" target="_blank"}

