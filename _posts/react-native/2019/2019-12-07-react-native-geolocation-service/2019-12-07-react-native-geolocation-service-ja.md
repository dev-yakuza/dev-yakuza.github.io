---
layout: 'post'
permalink: '/react-native/react-native-geolocation-service/'
paginate_path: '/react-native/:num/react-native-geolocation-service/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'React Nativeで現在位置情報を取得する方法'
description: 'react-native-geolocation-serviceライブラリを使ってReact Nativeで現在位置を取得する方法について調べてみましょう。'
image: '/assets/images/category/react-native/2019/react-native-geolocation-service/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

1. [概要](#概要)
1. [react-native-geolocation-serviceインストール](#react-native-geolocation-serviceインストール)
1. [ライブラリのリンク](#ライブラリのリンク)
    - [0.60以上](#060以上)
    - [0.59以下](#059以下)
1. [権限設定](#権限設定)
    - [iOS権限設定](#ios権限設定)
    - [アンドロイド権限設定](#アンドロイド権限設定)
1. [使い方](#使い方)
    - [現在の位置情報を取得](#現在の位置情報を取得)
    - [ユーザの位置情報追跡](#ユーザの位置情報追跡)
1. [完了](#完了)

</div>

## 概要

このブログポストではReact Nativeで現在位置情報を取得する方法について調べてみます。位置情報を取得するため、使うライブラリは`react-native-geolocation-service`で、下記のリンクで詳細情報を見ることができます。

- [react-native-geolocation-service](https://github.com/Agontuk/react-native-geolocation-service){:rel="nofollow noreferrer" target="_blank"}

ブログを作成しながら作ったソースコードがあります。ソースコードを確認したい方は、下記のリンクを参考してください。

- github: [react-native-geolocation-service-example](https://github.com/dev-yakuza/react-native-geolocation-service-example){:target="_blank"}

例題ソースコードは下記の内応が適用されています。詳しく知りたい方は下記のリンクを参考してください。

- [typescript]({{site.url}}/react-native/typescript/){:target="_blank"}
- [styled-components]({{site.url}}/react-native/styled-components/){:target="_blank"}
- [root-import]({{site.url}}/react-native/root-import/){:target="_blank"}

{% include in-feed-ads.html %}

## react-native-geolocation-serviceインストール

下記のコマンドでreact-native-geolocation-serviceをインストールしてください。

```bash
npm install --save react-native-geolocation-service
```

## ライブラリのリンク

インストールしたライブラいをReact Nativeプロジェクトへリンクする必要があります。

### 0.60以上

下記のコマンドを使ってiOSへライブラリをリンクします。

```bash
cd ios
pod install
```

React Naitveのプロジェクトでreact-native-geolocation-serviceを使うためSwiftをサポートする必要があります。Swiftをサポートするため`ios/[proejct name]xcworkspace`ファイルを開いてXcodeを実行します。

![react-native-geolocation-service enable swift support](/assets/images/category/react-native/2019/react-native-geolocation-service/enable_swift_support_create_file.jpg)


Xcodeを実行したら左上のプロジェクトにあるフォルドをマウスの右クリックして`New File...`を選択します。

![react-native-geolocation-service select swift file](/assets/images/category/react-native/2019/react-native-geolocation-service/enable_swift_support_select_swift.jpg)


上のような画面が見えてら、`Swift File`を選択して右下の`Next`を選択します。

![react-native-geolocation-service select file name](/assets/images/category/react-native/2019/react-native-geolocation-service/enable_swift_support_create.jpg)


敵とにファイルの名前を決めて、右下の`Create`ボタンを押します。

![react-native-geolocation-service select create bridging header](/assets/images/category/react-native/2019/react-native-geolocation-service/enable_swift_support_create_bridging_header.jpg)


上のような画面が出ると右下の`Create Bridging Header`を選択してSwiftをサポートするようにします。

### 0.59以下

React Nativeのバージョン0.59以下の場合、公式サイトを参考してリンクしてください。

- [Manually link the library on iOS](https://github.com/Agontuk/react-native-geolocation-service#manually-link-the-library-on-ios){:rel="nofollow noreferrer" target="_blank"}
- [Manually link the library on Android](https://github.com/Agontuk/react-native-geolocation-service#android){:rel="nofollow noreferrer" target="_blank"}

## 権限設定

### iOS権限設定

iOSで位置情報を使うためには、`ios/[Project Name]/info.plist`へ下記のように権限を設定する必要があります。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  ...
  <key>NSLocationWhenInUseUsageDescription</key>
  <string>Program requires GPS to track cars and job orders</string>
  <key>NSLocationAlwaysUsageDescription</key>
  <string>Program requires GPS to track cars and job orders</string>
  <key>NSLocationAlwaysAndWhenInUseUsageDescription</key>
  <string>Program requires GPS to track cars and job orders</string>
  ...
</dict>
</plist>
```

アプリが起動中だけ、位置情報を取得する場合、`NSLocationWhenInUseUsageDescription`だけ設定すれば大丈夫です。

アプリがバックグラウンドでも位置情報を取得する必要がある場合、`NSLocationAlwaysUsageDescription`と`NSLocationAlwaysAndWhenInUseUsageDescription`も設定する必要があり、下記のように`Background Modes`の`Location updates`を設定する必要があります。

バックグラウンドで位置情報を取得するためXcodeを開いて下記のように`+ Capability`を選択します。

![react-native-geolocation-service select capability for location updates background modes](/assets/images/category/react-native/2019/react-native-geolocation-service/select-capability.jpg)

下記のように`Capability`を検索する画面が出ると、`Background Modes`を検索して、検索結果をダブルクリックして追加します。

![react-native-geolocation-service search background modes for location updates background modes](/assets/images/category/react-native/2019/react-native-geolocation-service/search-background-modes.jpg)

ダブルクリックして`Background Modes`を追加したら、`Background Modes`の`Location updates`を選択して追加します。

![react-native-geolocation-service search background modes for location updates background modes](/assets/images/category/react-native/2019/react-native-geolocation-service/add-location-updates.jpg)


このように設定を完了したら、Javascriptで下記のようにソースコードを修正して権限を取得する必要があります。

```js
import {Platform} from 'react-native';
import Geolocation from 'react-native-geolocation-service';
...
useEffect(() => {
  if (Platform.OS === 'ios') {
    Geolocation.requestAuthorization('always');
  }
}, []);
...
```

### アンドロイド権限設定

アンドロイドで位置情報を使うため、`android/app/src/main/AndroidManifest.xml`ファイルを開いて下記のように修正します。

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
  package="com.reactnativegeolocationserviceexample">

    ...
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
    ...

    <application
```

{% include in-feed-ads.html %}

## 使い方

react-native-geolocationライブラリを使って、下記のように位置情報を取得することができます。

### 現在の位置情報を取得

現在位置情報を取得するためには、下記のコードを使います。

```js
Geolocation.getCurrentPosition(
    (position) => {
        console.log(position);
    },
    (error) => {
        // See error code charts below.
        console.log(error.code, error.message);
    },
    { enableHighAccuracy: true, timeout: 15000, maximumAge: 10000 }
);
```

現在位置情報を画面に表示する例題は下記です。

```js
import React, {useState, useEffect} from 'react';
import Styled from 'styled-components/native';
import Geolocation from 'react-native-geolocation-service';

const Container = Styled.View`
    flex: 1;
    justify-content: center;
    align-items: center;
`;

const Label = Styled.Text`
    font-size: 24px;
`;

interface ILocation {
  latitude: number;
  longitude: number;
}

const CurrentPosition = () => {
  const [location, setLocation] = useState<ILocation | undefined>(undefined);

  useEffect(() => {
    Geolocation.getCurrentPosition(
      position => {
        const {latitude, longitude} = position.coords;
        setLocation({
          latitude,
          longitude,
        });
      },
      error => {
        console.log(error.code, error.message);
      },
      {enableHighAccuracy: true, timeout: 15000, maximumAge: 10000},
    );
  }, []);

  return (
    <Container>
      {location ? (
        <>
          <Label>Latitude: {location.latitude}</Label>
          <Label>Latitude: {location.longitude}</Label>
        </>
      ) : (
        <Label>Loading...</Label>
      )}
    </Container>
  );
};

export default CurrentPosition;
```

上のソースコードの結果が次になります。

![react-native-geolocation-serviceユーザの現在位置情報](/assets/images/category/react-native/2019/react-native-geolocation-service/react-native-geolocation-current-position.jpg)

{% include in-feed-ads.html %}

### ユーザの位置情報追跡

react-native-geolocation-serviceを使ってユーザの現在位置情報の取得以外にも、ユーザの位置情報を追跡することができます。

ユーザの位置情報追跡にするためのソースコードは下記になります。

```js
_watchId = Geolocation.watchPosition(
  position => {
    const {latitude, longitude} = position.coords;
    setLocation({latitude, longitude});
  },
  error => {
    console.log(error);
  },
  {
    enableHighAccuracy: true,
    distanceFilter: 0,
    interval: 5000,
    fastestInterval: 2000,
  },
);
```

ユーザの位置情報の追跡が終わったら、下記のコードを使って終了します。

```js
if (_watchId !== null) {
  Geolocation.clearWatch(_watchId);
}
```

ユーザの位置情報を追跡する全体ソースコードは次になります。

```js
import React, {useState, useEffect} from 'react';
import Styled from 'styled-components/native';
import Geolocation from 'react-native-geolocation-service';

const Container = Styled.View`
    flex: 1;
    justify-content: center;
    align-items: center;
`;

const Label = Styled.Text`
    font-size: 24px;
`;

interface ILocation {
  latitude: number;
  longitude: number;
}

const WatchLocation = () => {
  const [location, setLocation] = useState<ILocation | undefined>(undefined);

  useEffect(() => {
    const _watchId = Geolocation.watchPosition(
      position => {
        const {latitude, longitude} = position.coords;
        setLocation({latitude, longitude});
      },
      error => {
        console.log(error);
      },
      {
        enableHighAccuracy: true,
        distanceFilter: 0,
        interval: 5000,
        fastestInterval: 2000,
      },
    );

    return () => {
      if (_watchId) {
        Geolocation.clearWatch(_watchId);
      }
    };
  }, []);

  return (
    <Container>
      {location ? (
        <>
          <Label>Latitude: {location.latitude}</Label>
          <Label>Latitude: {location.longitude}</Label>
        </>
      ) : (
        <Label>Loading...</Label>
      )}
    </Container>
  );
};

export default WatchLocation;
```

シミュレーターでユーザの位置情報を追跡するためには次の画面ように`Debug > Location`メニューで`City Run, City Bicycle Ride, Freeway Drive`中で1つのメニューを選択したら位置情報が更新されることが確認できます。

![react-native-geolocation-serviceユーザの位置情報追跡](/assets/images/category/react-native/2019/react-native-geolocation-service/react-native-geolocation-watch-position.jpg)

## 完了

これでreact-native-geolocation-serviceを使ってユーザの位置情報を取得する方法について見てみました。また、`watchPosition`を使ってユーザの位置情報を追跡する方法もみてみました。
