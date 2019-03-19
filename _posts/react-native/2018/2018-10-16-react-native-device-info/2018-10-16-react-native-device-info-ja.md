---
layout: 'post'
permalink: '/react-native/react-native-device-info/'
paginate_path: '/react-native/:num/react-native-device-info/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'react-native-device-info'
description: 'ユーザーのデバイスの情報を取得するためreact-native-device-infoライブラリを使って見ましょう。'
image: '/assets/images/category/react-native/react-native-device-info.jpg'
---


## 概要
ユーザーのデバイス情報を取得するためRNプロジェクトへ[react-native-device-info](https://github.com/rebeccahughes/react-native-device-info){:rel="nofollow noreferrer" target="_blank" }ライブラリを使ってみmしょう。

## react-native-device-infoライブラリインストール
下記のコマンドでreact-native-device-infoをインストールします。

{% include_relative common/installation.md %}

インストールが終わったら下記のコマンドでreact-native-device-infoライブラリをRNプロジェクトへリンクさせます。

{% include_relative common/link.md %}

## 使い方
私たちは基本的使ったことがある場合、ブログを作成します。したがってここには私たちが実際使って分かった内容を追加する予定です。

使い方を詳しく知りたい方は公式サイトを見てください。
- 公式サイト: [react-native-device-info](https://github.com/rebeccahughes/react-native-device-info){:rel="nofollow noreferrer" target="_blank" }

## device locale
device localeの情報を取得する方法。

```js
...
import DeviceInfo from 'react-native-device-info';
...

export default class Home extends React.Component<Props, State> {
    render() {
        const deviceLocale = DeviceInfo.getDeviceLocale();
        // iOS: "en"
        // Android: "en-US"
        ...
    }
}
```

## Unique ID
アプリのUnique IDを取得する。

```js
...
import DeviceInfo from 'react-native-device-info';
...

export default class Home extends React.Component<Props, State> {
    render() {
        const uniqueID = DeviceInfo.getUniqueID();
        // E98948E4-498D-447B-A750-D632C30461A3
        ...
    }
}
```

## デバイス区分
下記のコードでアプリがスマホで起動中か、タブレットで起動中か確認できます。

```js
...
import DeviceInfo from 'react-native-device-info';
...

export default class Home extends React.Component<Props, State> {
    render() {
        const isTablet = DeviceInfo.isTablet();
        // tablet: true / phone: false
        ...
    }
}
```


## エラー対応
よく開発してきましたがデバイスでランダムでcrashが発生する問題が出ました。シミュレータでも下のメッセージが表示してきました。

```
RCTBridge required dispatch_sync to load RCTDevLoadingView. This may lead to deadlocks
```

上の問題を直すために下記のように```libRNDeviceInfo.a```を一番下に移動しまして解決しました。

![RCTBridge required dispatch_sync to load RCTDevLoadingView. error](/assets/images/category/react-native/react-native-device-info/error.png)

下のリンクはエラーを直す時参考した内容です。

- [github issue](https://github.com/rebeccahughes/react-native-device-info/issues/260#issuecomment-366835600){:rel="nofollow noreferrer" target="_blank" }

## 参考
- 公式サイト: [react-native-device-info](https://github.com/rebeccahughes/react-native-device-info){:rel="nofollow noreferrer" target="_blank" }