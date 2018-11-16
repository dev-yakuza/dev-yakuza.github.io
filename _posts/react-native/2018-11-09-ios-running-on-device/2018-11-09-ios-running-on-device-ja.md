---
layout: 'post'
permalink: '/react-native/ios-running-on-device/'
paginate_path: '/react-native/:num/ios-running-on-device/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'iOSビルドやテスト'
description: 'RN(react native)で開発したプロジェクトをビルドしてデバイスでテストしてみましょう。'
image: '/assets/images/category/react-native/ios-running-on-device.jpg'
---


## 概要
以前のブログでRN(react native)で開発したプロジェクトをデバイスでテストしてみました。([デバイステスト]({{site.url}}/{{page.categories}}/ios-test-on-device/){:target="_blank"}) 皆さん、特に問題ありませんでしたか？今まで結構テストしたのでRN(react native)のプロジェクトをリリースするためビルドして実際のデバイスでテストしてみます。

ここではRN(react native)のプロジェクトをビルドする方法とビルドしたファイルをテストデバイスへアップして確認する方法について説明します。実際マーケットへアップロードする内容は含まれてないです。

## iOS / Mac
開発者アカウント生成とデバイスとの連携は以前のブログを参考してください。([デバイステスト]({{site.url}}/{{page.categories}}/ios-test-on-device/){:target="_blank"}) ここにはRN(react native)のプロジェクトをリリースするためのビルド方法とビルドしたファイルをデバイスでテストする方法について紹介します。

### リリースビルド準備
公式サイト([react-native](https://facebook.github.io/react-native/docs/ios-running-on-device#building-your-app-for-production){:rel="nofollow noreferrer" target="_blank"})へ全ての説明があります。それを見ながらやってみます。

#### HTTPS通信の設定
アップルはアプリが外部のシステムと```HTTP```通信をする時```HTTPS```で通信しないとダメになる機能を入れました。しかし、RN(react native)を開発する時はPCに開発サーバーを立ち上げてそのサーバーと通信してアプリを起動するのでRN(react native)は基本この機能を無効化してます。実際ビルドしてリリースすると開発サーバーとは通信しないのでこの無効化してる部分を消す必要があります。RN(react native)のプロジェクトフォルダから```/ios/プロジェクト名/info.plist```のファイルを開いて下記の部分を探して消します。

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

#### ビルドスキマ変更
RN(react native)のプロジェクトをビルドするためにはビルドスキマ(build schme)を```Debug```から```Release```で変更する必要があります。RN(react native)のプロジェクトがあるフォルダから```ios/プロジェクト名.xcodeproj```ファイルを実行します。

xcodeが実行されたら上部のメニューから```Product```メニューの```Scheme```メニューで```Edit Scheme```を選択します。

![change build scheme](/assets/images/category/react-native/ios-running-on-device/change-scheme.png)

下記のような画面が表示されたら左の```Run```を選択して右の```Build Configuration```を```Debug```から```Release```に変更して下の```Close```ボタンを押します。

![change build scheme to Release from Debug](/assets/images/category/react-native/ios-running-on-device/change-debug-to-release.png)

注意:ここもまた開発する時は```Release```から```Debug```に戻せる必要があります。

#### bundleファイル指定
最後にbundleファイルを指定します。RN(react native)で開発する時は開発サーバー(localhost)からjs(javascript)のファイルを提供しますがリリースする時は```react```と同じように一つのbundleファイルを生成してそのファイルを利用します。したがってリリースではjs(javascript)がビルドされた一つのbundleファイルを活用するように指定する必要があります。RN(react natie)があるフォルダで```ios/プロジェクト名/AppDelegate.m```ファイルを開いてか下記のように修正します。

```
#ifdef DEBUG
    jsCodeLocation = [[RCTBundleURLProvider sharedSettings] jsBundleURLForBundleRoot:@"index" fallbackResource:nil];
#else
    jsCodeLocation = [[NSBundle mainBundle] URLForResource:@"main" withExtension:@"jsbundle"];
#endif
```

#### デバイスで起動
全ての設定が終わりました。RN(react native)をビルドする前にデバイスで確認してみましょう。デバイスでテストした時と同じようにUSBでMacとアイホンを接続してビルドターゲットをデバイスで設定した後、矢印を押して実行します。

![device test](/assets/images/category/react-native/ios-running-on-device/device-test.png)

デバイステストとは違ってjs(javascript)がビルドされたbundleファイルを使うのでMacとアイホンが同じWifi/Network上へある必要とインストールした後デバイスがMacと接続してる必要がありません。しかし、正式にインストールではないので一定期間が経過すると、そのアプリを使うことが出来ません。
## 参考
- 公式サイト: [react native](https://facebook.github.io/react-native/docs/ios-running-on-device){:rel="nofollow noreferrer" target="_blank"}
