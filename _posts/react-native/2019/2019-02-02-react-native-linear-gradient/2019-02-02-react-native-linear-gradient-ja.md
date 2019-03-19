---
layout: 'post'
permalink: '/react-native/react-native-linear-gradient/'
paginate_path: '/react-native/:num/react-native-linear-gradient/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'グラデーション(Gradient)'
description: 'RN(React Native)プロジェクトでreact-native-linear-gradientを使ってグラデーション(Gradient)バックグラウンド(background)を作ってみましょう。'
image: '/assets/images/category/react-native/react-native-linear-gradient.png'
---


## 概要
RN(React Native)にバックグラウンドでグラデーション(Gradient)を入れることは難しいです。このブログでは```react-native-linear-gradient```を使ってRN(React Native)プロジェクトにグラデーション(Gradient)背景を入れる方法について説明します。

- react-native-linear-gradient公式サイト: [https://github.com/react-native-community/react-native-linear-gradient](https://github.com/react-native-community/react-native-linear-gradient){:rel="nofollow noreferrer" target="_blank"}

## インストール
RN(React Native)でグラデーション(Gradient)を使うため下記のコマンドを実行して```react-native-linear-gradient```ライブラリをインストールします。

```bash
npm install --save react-native-linear-gradient
```

## ライブラリ連結
RN(React Native)で```react-native-linear-gradient```を使うため下のコマンドで```react-native-linear-gradient```ライブラリとRN(React Native)プロジェクトを連結します。

```bash
react-native link react-native-linear-gradient
```

## 使い方
RN(React Native)で```react-native-linear-gradient```を使ってグラデーション(Gradient)を実装する方法は下記のようです。 (ソースコードはreact-native-linear-gradient公式サイトからコピペ〜しました。)

```js
import LinearGradient from 'react-native-linear-gradient';

// Within your render function
<LinearGradient colors={['#4c669f', '#3b5998', '#192f6a']} style={styles.linearGradient}>
  <Text style={styles.buttonText}>
    Sign in with Facebook
  </Text>
</LinearGradient>

// Later on in your styles..
var styles = StyleSheet.create({
  linearGradient: {
    flex: 1,
    paddingLeft: 15,
    paddingRight: 15,
    borderRadius: 5
  },
  buttonText: {
    fontSize: 18,
    fontFamily: 'Gill Sans',
    textAlign: 'center',
    margin: 10,
    color: '#ffffff',
    backgroundColor: 'transparent',
  },
});
```

私たちは背景でグラデーション(Gradient)を使うため下のソースコードを使っています。

{% raw %}
```js
...
import LinearGradient from 'react-native-linear-gradient';
import styled from 'styled-components/native';
...
const Background = styled(LinearGradient)`
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
`;
...
<Background
  colors={[item.background[0], item.background[1]]}
  start={{
    x: item.direction.start.x,
    y: item.direction.start.y,
  }}
  end={{ x: item.direction.end.x, y: item.direction.end.y }}
/>
...
```
{% endraw %}

また、ページの切り替える時背景のグラデーション(Gradient)をスムーズ変えるためアニメーションを適用してます。アニメーションは下記のサイトを参考して作りました。

- グラデーションアニメーション例題: [AnimatedGradient](https://github.com/dslounge/rn-animated-gradient-example/tree/master/src/ColorExample/AnimatedGradient){:rel="nofollow noreferrer" target="_blank"}


## 完了
RN(React Native)で開発したアプリにグラデーション(Gradient)背景を入れってもっと美しいアプリを作ってみてください。


## 参考
- react-native-linear-gradient公式サイト: [https://github.com/react-native-community/react-native-linear-gradient](https://github.com/react-native-community/react-native-linear-gradient){:rel="nofollow noreferrer" target="_blank"}
- グラデーションアニメーション例題: [AnimatedGradient](https://github.com/dslounge/rn-animated-gradient-example/tree/master/src/ColorExample/AnimatedGradient){:rel="nofollow noreferrer" target="_blank"}