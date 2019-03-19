---
layout: 'post'
permalink: '/react-native/react-native-admob/'
paginate_path: '/react-native/:num/react-native-admob/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'グーグルアドモブ'
description: 'グーグルアドモブ(google admob)広告を使うためreact-native-admobライブラリを使ってみましょう。'
image: '/assets/images/category/react-native/react-native-admob.jpg'
---


## 概要
グーグルは広告プラットフォームでアドセンス(Adsense: [https://www.google.com/adsense/start/](https://www.google.com/adsense/start/){:rel="nofollow noreferrer" target="_blank"})とアドモブ(Admob: [https://www.google.com/admob/](https://www.google.com/admob/){:rel="nofollow noreferrer" target="_blank"})を持ってます。ここではアプリケーションへグーグルアドモブ(google admob)を使って広告を表示させる方法について話します。

グーグルのアドセンス(google adsense)とアドモブ(google admob)の違いはアドセンスはウェブサイト用のプラットホームでアドモブはスマホ用のフラットフォームのことです。私たちはブログ用の広告ですでにアドセンス(google adsense)を使ってます。ウェブへアドセンス(google adsense)を使う方法が気になる方は[google service]({{site.url}}/jekyll/google-service/)を確認してください。

## ライブラリインストール
グーグルのアドモブ(google admob)をRN(react native)へ使うためには[react-native-admob](https://github.com/sbugert/react-native-admob){:rel="nofollow noreferrer" target="_blank" }ライブラリをインストールする必要があります。

```bash
npm install react-native-admob@next --save
```

インストールが完了されたら下記のコマンドでreact-native-admobライブラリとRN(react native)のプロジェクトをリンクさせます。

```bash
react-native link react-native-admob
```

### iOS SDK インストール
グーグルアドモブ(Google admob)をiOS上で使うためには```Google Mobile Ads SDK```をインストールする必要があります。下のリンクを押してインストールする方法を確認してください。

- Google Mobile Ads SDK: [https://developers.google.com/admob/ios/quick-start](https://developers.google.com/admob/ios/quick-start#import_the_mobile_ads_sdk){:rel="nofollow noreferrer" target="_blank" }

このブログではファイルダウンロード形式を説明します。

- ダウンロードリンク: [https://developers.google.com/admob/ios/download](https://developers.google.com/admob/ios/download){:rel="nofollow noreferrer" target="_blank" }

上記のリンクを押してダウンロードサイトへ遷移して```Google Mobile Ads SDK```をダウンロードします。ダウンロードが完了されたら圧縮を解除します。

RN(react native)プロジェクトフォルドへ移動して```プロジェクト名.xcodeproj```ファイl流を実行します。

![add Google Mobile Ads SDK to ios ](/assets/images/category/react-native/react-native-admob/add_sdk.png)

xcodeが実行されたら左上のプロジェクト名を右クリックして```Add Files to [プロジェクト名]```を押します。上記でダウンロードした```Google Mobile Ads SDK```フォルダへ移動して```GoogleMobileAds.framework```ファイルを選択します。下にある```Copy items if needed```を洗濯して```add```を押して```Google Mobile Ads SDK```ライブラリを追加します。

## グーグルアドモブ会員登録
グーグルのアドモブ(Google admob)のサイトへ移動して会員登録をします。一般的な会員登録/ログインのプロセスなのでここでは省略します。

- グーグルアドモブ(Google admob)のサイト: [https://www.google.com/admob/](https://www.google.com/admob/){:rel="nofollow noreferrer" target="_blank" }

## グーグルアドモブ設定
グーグルアドモブ(Google admob)の使用法について見てみましょう。グーグルアドモブ(Google admob)を使うためにはグーグルアドモブ(Google admob)サイトに会員登録してログインしたら下のような画面が見えます。

![signin google admob](/assets/images/category/react-native/react-native-admob/signin_google_admob.png)

下の所にある```GET STARTED```ボタンを押してグーグルアドモブ(Google admob)の利用を始めます。

![configure admob](/assets/images/category/react-native/react-native-admob/configure_admob.png)

すでにアプリがマーケットへ登録されたかどうかを選択します。私たちはまだアプリを登録してないので```NO```を選択します。

![configure app name on admob](/assets/images/category/react-native/react-native-admob/configure_app_name.png)

グーグルアドモブ(Google admob)を使うためにアプリの名前を作成して広告を表示させたいプラットフォームを選択します。私たちはまず```iOS```を選択して進めます。

![completed to configure](/assets/images/category/react-native/react-native-admob/completed_configure.png)

グーグルアドモブ(Google admob)の登録が終わりました。次は何をすればいいかが親切に書いております。

1. まず、react-native-admobを設定する時必要な```App ID```をコピーします。
1. 広告のタイプ(ad unit)をグーグルアドモブ(Google admob)に設定します。
1. アプリをマーケットへ登録したらグーグルアドモブ(Google admob)へ連携する必要があります。

下にある```NEXT: CREATE AD UNIT```を押したら広告のタイプを設定する画面へ遷移します。

![select advertisement type](/assets/images/category/react-native/react-native-admob/select_ad_uni.png)

私たちはまずバナー広告をしてみます。```Banner```の下にある```SELECT```ボタンを押します。

![input banner name](/assets/images/category/react-native/react-native-admob/set_banner_name.png)

バナーの名前を設定します。グーグルアドモブ(Google admob)サービスでこのバナーを探すための名前ですので自分が認識できる名前で設定します。入力が終わったら```CREATE AD UNIT```を押して設定を終了します。

![finished configuration](/assets/images/category/react-native/react-native-admob/finished_configuration.png)

グーグルアドモブ(Google admob)のバナー設定が終わりました。また、出たApp IDとバナーのad unit IDをコピーします。

## react-native-admob
グーグルアドモブ(Google admob)へ設定したバナーをRN(react-native)で使うためにreact-native-admobの使う方法をみてみましょう。

### iOS設定
グーグルアドモブ(Google admob)をiOSで使うためには```ios/プロジェクト名/AppDelegate.m```のファイルを修正する必要があります。

```
#import <React/RCTRootView.h>

@import GoogleMobileAds;
```

上でダウンロードしてxcodeへ追加した```Google Mobile Ads SDK```ライブラリをインポートします。

```
self.window.rootViewController = rootViewController;

[GADMobileAds configureWithApplicationID:@"ca-app-pub-7987914246691031~8295071692"];

[self.window makeKeyAndVisible];
```

グーグルアドモブ(Google admob)を生成する時コピーしたApp Idを入れた```[GADMobileAds configureWithApplicationID:@"グーグルアドモブアプリID"];```コードを上記のような位置へ入れます。

これでiOSでグーグルアドモブ(Google admob)を使う準備ができました。

### react-native-admob使う
グーグルアドモブ(Google admob)へ設定したバナーを使うためバナーを表示したいファイルで```react-native-admob```ライブラリの```AdMobBanner```をインポーとします。

```js
import { AdMobBanner } from 'react-native-admob';
```

グーグルアドモブ(Google admob)バナーを表示したい位置へ下記のコードをコピペします。

```js
<AdMobBanner
    adSize="fullBanner"
    adUnitID="ad unit ID"
    testDevices={[AdMobBanner.simulatorId]}
    onAdFailedToLoad={error => console.log(error)}
/>
```
- adSize: 広告のサイズを決定します。サイズについては公式サイトを参考してください。([react-native-admob banner size](https://github.com/sbugert/react-native-admob#admobbanner){:rel="nofollow noreferrer" target="_blank"})
- adUnitID: グーグルアドモブ(Google admob)で生成したバナーユニットのアイディ(ad unit ID)をコピペします。
- testDevices: テスト用の端末のアイディを入れます。ここにはシミュレータのアイディを設定します。
- onAdFailedToLoad: 広告のローディングが失敗した時の処理を入れる部分です。

これで設定が終わりました。プロジェクトを実行して広告が上手く表示されるかを確認します。

## アンドロイド(Android)
~~アンドロイド(Android)の部分は実際開発する時、このブログへ追加します。~~
現在react-native-admobライブラリを使うことをやめました。したがって、アンドロイド(Android)部分は追加されません。

## お知らせ
私たちはreact-native-firebaseを使ってグーグルアドモブ(Google Admob)を表示することになりました。詳しく内容は[Firebase Admob]({{site.url}}/{{page.categories}}/react-native-firebase-admob/){:target="_blank"}のブログを参考してください。
