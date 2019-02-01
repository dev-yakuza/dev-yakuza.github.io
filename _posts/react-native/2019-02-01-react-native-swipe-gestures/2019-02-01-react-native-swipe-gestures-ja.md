---
layout: 'post'
permalink: '/react-native/react-native-swipe-gestures/'
paginate_path: '/react-native/:num/react-native-swipe-gestures/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'スワイプ検知'
description: 'RN(React Native)プロジェクトでユーザが画面でどの方向でスワイプ(Swipe)したか検知するためreact-native-gesturesを使ってみましょう。 '
image: '/assets/images/category/react-native/react-native-swipe-gestures.jpg'
---


## 概要
RN(React Native)プロジェクトを進めてる時ユーザのスワイプ(Swipe)の方向について別のアクションをする機能を追加することになりました。そして検索したら```react-native-swipe-gestures```と呼ばれるライブラリを発見して適用してみました。このブログでは```react-native-swipe-gestures```のインストールと使い方について説明します。

- react-native-swipe-gestures公式サイト: [https://github.com/glepur/react-native-swipe-gestures](https://github.com/glepur/react-native-swipe-gestures){:rel="nofollow noreferrer" target="_blank"}

## インストール
下記のコマンドで```react-native-swipe-gestures```ライブラリをインストールします。

```bash
npm install --save react-native-swipe-gestures
```

## 使い方
RN(React Native)でユーザのスワイプ(Swipe)を検知するため下記のようにソースを修正します。


{% raw %}
```js
...
import GestureRecognizer from 'react-native-swipe-gestures';
...

render() {
  <GestureRecognizer
          onSwipeLeft={this._onSwipeLeft}
          onSwipeRight={this._onSwipeRight}
          config={{
            velocityThreshold: 0.3,
            directionalOffsetThreshold: 80,
          }}
          style={{
            flex: 1,
          }}>
          ...
  </GestureRecognizer>
}
...
private _onSwipeLeft = gestureState => {
  ...
  this.setState({
    ...
  });
};

private _onSwipeRight = gestureState => {
  ...
  this.setState({
    ...
  });
  ...
};
```
{% endraw %}

## 完了
これでRN(React Native)でユーザのスワイプ(Swipe)を検知する方法についてみてみました。簡単な機能もどんどんコーディングをしなくてコピペーしてる自分をみつけました。。。```react-native-swipe-gestures```ソースはそんな長くないのでソースを見って自ら作っても面白いと思います。


## 参考
- react-native-swipe-gestures公式サイト: [https://github.com/glepur/react-native-swipe-gestures](https://github.com/glepur/react-native-swipe-gestures){:rel="nofollow noreferrer" target="_blank"}