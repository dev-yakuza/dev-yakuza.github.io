---
layout: 'post'
permalink: '/react-native/react-native-support-tablet/'
paginate_path: '/react-native/:num/react-native-support-tablet/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'RN(React Naitve)タブレット対応'
description: 'RN(React Native)プロジェクトでタブレットを対応する方法について説明します。'
image: '/assets/images/category/react-native/react-native-support-tablet/background.jpg'
---


## 概要
RN(React Native)で私たちはクロスプラットフォームを作れます。このことは、アイホン(iPhone)、アンドロイドフォン(Android phone)以外にもアイパット(iPad)、アンドロイドタブレット(Android Tablet)を作成することができます。このブログではスマホ用で作成したアプリをタブレットに適用する方法について説明します。

## アンドロイド
アンドロイドは特別処理をする必要がありません。ここでは自分のアプリがどの端末に対応してるか確認する方法を説明します。

下記のリンクを押してグーグルプレイコンソル(Google Play Console)に接続します。

- グーグルプレイコンソル: [https://play.google.com/apps/publish/](https://play.google.com/apps/publish/){:rel="nofollow noreferrer" target="_blank"}

ログイン後、確認したいアプリを押します。

![グーグルプレイ：アンドロイドアプリデバイス対応リスト](/assets/images/category/react-native/react-native-support-tablet/android-support-devices.png)

左メニューで`Release management` > `Device catalog`を選択したら上のような画面が見えます。もし、`同意`する画面が出ったら、同意したら上のような画面が見えます。

![グーグルプレイ - アンドロイドアプリマケット情報修正](/assets/images/category/react-native/react-native-support-tablet/android-market-info.png)

左メニューで`Store presence` > `Store listing`を押して`TABLET`のイメージを追加してください。


## iOS
iOSも特にコーディングする必要はありません。RN(React Native)のプロジェクトフォルダで`ios/[project name].xcodeproj`、または `ios/[project name].xcworkspace`を押してxcodeを実行します。

![xcode universalアプリ設定](/assets/images/category/react-native/react-native-support-tablet/ios-universal-configuration.png)

上のように左のプロジェクト名、`TARGETS`もプロジェクト名を選択します。`Development Info`の`Devices`を選択して`Universal`を選択します

iOSもアンドロイド用にアプリストア(App store)の情報を修正してください。


## 完了
これでRN(React Native)で開発したアプリがスマホとタブレットを対応することになりました。タブレットを対応することは設定だけ変更すればできるもので、簡単です。またRN(React Native)は`Flexbox`を使ってるのでresponsiveの対応も簡単にできます。しかし、特定位置を指定する時、特定サイズを指定する時は画面のサイズを考えて作る必要があります。私は[react-native-device-info]({{site.url}}/{{page.categories}}/react-native-device-info/){:target="_blank"}の`DeviceInfo.isTablet()`を使って、デバイスに依存してる部分を処理しています。

