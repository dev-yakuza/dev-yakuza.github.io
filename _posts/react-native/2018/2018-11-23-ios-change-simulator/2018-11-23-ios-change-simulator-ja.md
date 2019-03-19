---
layout: 'post'
permalink: '/react-native/ios-change-simulator/'
paginate_path: '/react-native/:num/ios-change-simulator/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'iOSシミュレータ変更'
description: 'RN(react native)をiOSでシミュレータでテストする時シミュレータを変更する方法を紹介します。'
image: '/assets/images/category/react-native/ios-change-simulator.jpg'
---


## 概要
RN(react native)でアプリを開発する時いつも下記のコマンドでiOSを開発します。

```bash
react-native run-ios
```

開発する時は特に問題ないですが開発が終わって様々なデバイス(device)でテストしたい時はいつも不便でした。だから、コマンドを使ってシミュレータ(simulator)を変更する方法を紹介します。

## iOSシミュレータ確認
現在使用可能なiOSシミュレータ(simulator)を確認します。

```bash
xcrun simctl list devices
```

## シミュレータ変更
下のコマンドを使って使用したいシミュレータ(simulator)をRN(react native)を実行します。

```bash
react-native run-ios --simulator="iPhone 5s"
```

下記のコマンドリストはシミュレータ(simulator)を変更する例です。

```bash
react-native run-ios --simulator="iPhone 5s"
react-native run-ios --simulator="iPhone 6"
react-native run-ios --simulator="iPhone 6 Plus"
react-native run-ios --simulator="iPhone 6s"
react-native run-ios --simulator="iPhone 6s Plus"
react-native run-ios --simulator="iPhone 7"
react-native run-ios --simulator="iPhone 7 Plus"
react-native run-ios --simulator="iPhone 8"
react-native run-ios --simulator="iPhone 8 Plus"
react-native run-ios --simulator="iPhone SE"
react-native run-ios --simulator="iPhone X"
react-native run-ios --simulator="iPhone XR"
react-native run-ios --simulator="iPhone XS"
react-native run-ios --simulator="iPhone XS Max"
react-native run-ios --simulator="iPad Air"
react-native run-ios --simulator="iPad Air 2"
react-native run-ios --simulator="iPad"
react-native run-ios --simulator="iPad Pro"
```
