---
layout: 'post'
permalink: '/react-native/ios-change-simulator/'
paginate_path: '/react-native/:num/ios-change-simulator/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'iOSシミュレータ変更'
description: 'リアクトネイティブ(React Native)をiOSでシミュレータでテストする時シミュレータを変更する方法を紹介します。'
image: '/assets/images/category/react-native/ios-change-simulator.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [iOSシミュレータ確認](#iosシミュレータ確認)
- [シミュレータ変更](#シミュレータ変更)
- [完了](#完了)

</div>

## 概要

リアクトネイティブ(React Native)でアプリを開発する時いつも下記のコマンドでiOSを開発します。

```bash
npm run ios
```

開発する時は特に問題ないですが開発が終わって様々なデバイス(device)でテストしたい時はいつも不便でした。だから、コマンドを使ってシミュレータ(simulator)を変更する方法を紹介します。

## iOSシミュレータ確認

現在使用可能なiOSシミュレータ(simulator)を確認します。

```bash
xcrun simctl list devices
```

コマンドを実行すると下記のように使えるシミュレータのリストが確認できます。

```bash
iPhone 8 (066D55DB-AB0A-41D3-84A0-612E68F88063)
iPhone 8 Plus (3AA8DBD0-20FF-4FA4-8745-F63F6A078E6E)
iPhone 11 (DD6577E9-8092-479F-8DE4-0F2D00326574)
iPhone 11 Pro (41166CD6-5270-4919-BE03-272D1835E3E1)
iPhone 11 Pro Max (BE84015E-FC1C-42EA-B708-73258190ED6F)
iPhone SE (2nd generation) (8CEB8C23-1BB7-4B2F-A51F-4C2623F4BCEF)
iPad Pro (9.7-inch) (3495B155-8378-4A8B-817E-D0CAB8A793F0)
iPad (7th generation) (DBF8AFFF-D166-4ACB-8041-59A414FBB8F8)
iPad Pro (11-inch) (2nd generation) (5283A04B-EFE1-41F9-944B-C66EFF1E1498)
iPad Pro (12.9-inch) (4th generation) (DDAD2AAE-3506-4456-9F8F-29BA7DF0B1A3)
iPad Air (3rd generation) (526BEA39-E657-47AF-A7A2-22BA93D81FA1)
```

## シミュレータ変更

下のコマンドを使って使用したいシミュレータ(simulator)をリアクトネイティブ(React Native)を実行します。

```bash
npm run ios -- --simulator="iPhone 5s"
```

下記のコマンドリストはシミュレータ(simulator)を変更する例です。

```bash
npm run ios -- --simulator="iPhone 5s"
npm run ios -- --simulator="iPhone 6"
npm run ios -- --simulator="iPhone 6 Plus"
npm run ios -- --simulator="iPhone 6s"
npm run ios -- --simulator="iPhone 6s Plus"
npm run ios -- --simulator="iPhone 7"
npm run ios -- --simulator="iPhone 7 Plus"
npm run ios -- --simulator="iPhone 8"
npm run ios -- --simulator="iPhone 8 Plus"
npm run ios -- --simulator="iPhone SE"
npm run ios -- --simulator="iPhone X"
npm run ios -- --simulator="iPhone XR"
npm run ios -- --simulator="iPhone XS"
npm run ios -- --simulator="iPhone Xs Max"
npm run ios -- --simulator="iPad Air"
npm run ios -- --simulator="iPad Air 2"
npm run ios -- --simulator="iPad"
npm run ios -- --simulator="iPad Pro"
```

## 完了

これでReact Nativeプロジェクトをシミュレータで確認する時、基本シミュレータではないシミュレータを実行する方法について見てみました。今後、皆さんも上のコマンドを使って色んなシミュレータでテストしてみてください。
