---
layout: 'post'
permalink: '/react-native/react-native-lottie/'
paginate_path: '/react-native/:num/react-native-lottie/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'アフターエフェクト(AEF)'
description: 'RN(React Native)プロジェクトでアドビのアフターエフェクト(Adobe After Effects)で作ったアニメーションを適用してみましょう'
image: '/assets/images/category/react-native/react-native-lottie.jpg'
---


## 概要
最近アプリに躍動感を入れるためマイクロインタラクション(Microinteractions)をたくさん使っています。このブログでは```アドビのアフターエフェクト(Adobe After Effects)```で作ったアニメーションをAirbnbが作った```lottie```ライブラリを使ってRN(React Native)に適用する方法について説明します。

- lottie公式サイト: [https://airbnb.design/lottie/](https://airbnb.design/lottie/){:rel="nofollow noreferrer" target="_blank"}

## インストール
RN(React Native)で```lottie```ライブラリを使うため下のコマンドを実行して```lottie-react-native```ライブラリをインストールします。

```bash
npm install --save lottie-react-native
```

## ライブラリ連結
RN(React Native)で```lottie```ライブラリを使うため```lottie-react-native```ライブラリをインストールを完了したら下記の方法でOSに合わせてライブラリを接続します。

### iOS
RN(React Native)で```lottie```ライブラリをiOSで使うため下記のように```lottie-react-native```ライブラリをRN(React Native)プロジェクトと連結します。

```bash
react-native link lottie-ios
react-native link lottie-react-native
```

そして```ios/[project_name].xcodeproj```か```ios/[project_name].xcworkspace```ファイルを開いてxcodeを実行します。その後、下のように追加設定をしてください。

![lottie ios追加設定](/assets/images/category/react-native/react-native-lottie/ios-settings.png)

1. 下のメニューでプロジェクト名を選択
1. ```TARGETS```でプロジェクト名を選択
1. 上部にあるメニューで```General```を選択
1. スクロールして下に行くと```Embedded Binaries```項目が見える。```+```ボタンを押して```Lottie.framework```を検索、```ios```用を選択して追加します。

![lottie ios framework追加設定](/assets/images/category/react-native/react-native-lottie/add-lottie-framework.png)

### アンドロイド
上のように```iOS```を連結したら```lottie```ライブラリをアンドロイドで使うため他にすることはありません。下記のコマンドが実行された時、アンドロイドは```lottie-react-native```と連結されました。

```bash
react-native link lottie-react-native
```

## 使い方
RN(React Native)でlottieを使うためにはアドビのアフターエフェクト(Adobe After Effects)で作ったアニメーションファイルが必要になりますアドビのアフターエフェクト(Adobe After Effects)でlottieに必要なアニメーションファイルを作る方法についてはこのブログでは説明しません。下記のリンクを参考してアドビのアフターエフェクト(Adobe After Effects)からlottieのアニメーションファイルを生成してください。

- [https://github.com/airbnb/lottie-web](https://github.com/airbnb/lottie-web){:rel="nofollow noreferrer" target="_blank"}

または下記のサイトで必要なマイクロインタラクション(Microinteractions)ファイルを検索してください。

- [https://lottiefiles.com/](https://lottiefiles.com/){:rel="nofollow noreferrer" target="_blank"}

アドビのアフターエフェクト(Adobe After Effects)や上のサイトからダウンロードしたファイルは```json```形式になっております。

RN(React Native)でlottieを利用してマイクロインタラクション(Microinteractions)を適用するため下記のようにコードを作成します。

```js
...
import LottieView from 'lottie-react-native';
...
export default class BasicExample extends React.Component {
  render() {
    return (
      <LottieView
        source={require('./animation.json')}
        autoPlay
        loop
      />
    );
  }
}
...
```

## 完了
これでRN(React Native)でlottieを使ってマイクロインタラクション(Microinteractions)を実装しました。簡単ですね？lottieでアニメーションを適用するよりアニメーションを作ることがもっと大変と思います。私はアフターエフェクト(After Effects)ができないので[https://lottiefiles.com/](https://lottiefiles.com/){:rel="nofollow noreferrer" target="_blank"}サイトを使ってます。lottieを使って皆さんも皆さんのアプリに面白いマイクロインタラクション(Microinteractions)を入れってみてください。


## 参考
- lottie公式サイト: [https://airbnb.design/lottie/](https://airbnb.design/lottie/){:rel="nofollow noreferrer" target="_blank"}