---
layout: 'post'
permalink: '/react-native/react-native-analytics-bridge/'
paginate_path: '/react-native/:num/react-native-analytics-bridge/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'Google Analytics'
description: 'リアクトネイティブ(React Native)で開発したアプリをグーグルアナリティクス(Google Analytics)を使ってアプリを分析してみましょう。'
image: '/assets/images/category/react-native/react-native-analytics-bridge.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [ライブラリインストール](#ライブラリインストール)
- [Google Analytics](#google-analytics)
- [分析コード](#分析コード)
- [お知らせ](#お知らせ)
- [参考](#参考)

</div>

## 概要

グーグルアナリティクス([Google Analytics](https://marketingplatform.google.com/about/analytics/){:rel="nofollow noreferrer" target="_blank"})を使ってリアクトネイティブ(React Native)で開発したアプリを分析することができます。グーグルアナリティクス(Google Analytics)を使ってリアクトネイティブ(React Native)アプリを分析してみましょう。

このライブラリはdeprecatedされました。 もしGoogle Analyticsを使いたい方は、`Firebase Analytics`を使ってください。詳しくは下記のブログを参考してください。

- [Firebase Analytics]({{site.url}}/{{page.categories}}/react-native-firebase-analytics/){:target="_blank"}

## ライブラリインストール

リアクトネイティブ(React Native)アプリとグーグルアナリティクス(Google Analytics)を連携するためには[GoogleAnalyticsBridge](https://github.com/idehub/react-native-google-analytics-bridge#installation-and-linking-libraries){:rel="nofollow noreferrer" target="_blank"}ライブラリをインストルする必要があります。下記のコマンドを実行して```GoogleAnalyticsBridge```ライブラリをインストールしてください。

```bash
npm install --save react-native-google-analytics-bridge
```

下のコマンドでリアクトネイティブ(React Native)と```GoogleAnalyticsBridge```を連携してください。

```bash
react-native link react-native-google-analytics-bridge
```

react-native-google-analytics-bridgeライブラリを使う準備が終わりました。今まからグーグルアナリティクス(Google Analytics)を連動する準備をする必要があります。

{% include in-feed-ads.html %}

## Google Analytics

下のリンクを押してグーグルアナリティクス(Google Analytics)サイトへ移動します。

- グーグルアナリティクス(Google Analytics): [https://analytics.google.com/analytics/web/](https://analytics.google.com/analytics/web/){:rel="nofollow noreferrer" target="_blank"}

ログイン後左下の```Admin```メニューを選択します。

![create account for mobile](/assets/images/category/react-native/react-native-analytics-bridge/create-account-for-mobile.jpg)

左上の```+ Create Account```を押します。

![click create account](/assets/images/category/react-native/react-native-analytics-bridge/click-create-account.jpg)

リアクトネイティブ(React Native)で作ったアプリの情報を入力して一番下の```Get Tracking ID```を押してトラッキングアイディ(Tracking ID)を生成します。

![insert-app-info](/assets/images/category/react-native/react-native-analytics-bridge/insert-app-info.jpg)

react-native-google-analytics-bridgeライブラリとグーグルアナリティクス(Google Analytics)の連動する準備が終わりました。実際トラッキングアイディ(Tracking ID)を使ってリアクトネイティブ(React Native)で作ったアプリを分析してみます。

{% include in-feed-ads.html %}

## 分析コード

リアクトネイティブ(React Native)で開発したアプリへグーグルアナリティクス(Google Analytics)で分析したいページへ下記のコードを追加します。

```js
...
import { GoogleAnalyticsTracker } from "react-native-google-analytics-bridge";
...

...
let tracker = new GoogleAnalyticsTracker("UA-12345-1");
tracker.trackScreenView("Home");
...
```

はい、これで終わりました。簡単ですね？下記のコードへ自分のグーグルアナリティクス(Google Analytics)のトラッキングアイディ(Tracking ID)を入力します。

```js
new GoogleAnalyticsTracker("自分のトラッキングアイディ")
```

トラッキングしたいページの識別するためのタイトルを入力します。

```js
tracker.trackScreenView("Home");
```

私たちはこのコードを```render()```へ入れて使ってます。どこがいい場所かは皆さんが判断して入れたらいいと思います。

もっと深い分析がしたい方は公式サイトを参考してreact-native-google-analytics-bridgeの色んな機能を使ってみてください。

- [react-native-google-analytics-bridge](https://github.com/idehub/react-native-google-analytics-bridge#usage){:rel="nofollow noreferrer" target="_blank"}

{% include in-feed-ads.html %}

## お知らせ

私たちはアプリの分析だけではなくグーグルのファイアベース(Google firebase)の色んな機能を使うためreact-native-firebaseを使ってアプリを分析することにしました。別の機能のためreact-native-firebaseライブラリを設定するだけで児童にアプリを分析してくれます。react-native-firebaseライブラリの設定に関しては[Firebase Admob]({{site.url}}/{{page.categories}}/react-native-firebase-admob/){:target="_blank"}のブログをみてください。

## 参考

- 公式サイト: [GoogleAnalyticsBridge](https://github.com/idehub/react-native-google-analytics-bridge#installation-and-linking-libraries){:rel="nofollow noreferrer" target="_blank"}
