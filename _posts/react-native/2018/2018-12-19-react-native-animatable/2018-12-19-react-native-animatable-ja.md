---
layout: 'post'
permalink: '/react-native/react-native-animatable/'
paginate_path: '/react-native/:num/react-native-animatable/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'react-native-animatable'
description: 'react-native-animatableを使って簡単にリアクトネイティブ(React Native)へアニメーションを追加してみましょう。'
image: '/assets/images/category/react-native/react-native-animatable.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [ライブラリインストール](#ライブラリインストール)
- [基本的な使い方](#基本的な使い方)
- [イベントを通じて使い方](#イベントを通じて使い方)
- [styled-components](#styled-components)
- [使えるアニメーション](#使えるアニメーション)
- [完了](#完了)
- [参考](#参考)

</div>

## 概要

基本的に結構使ってるアニメーションを纏めた[react-native-animatable](https://github.com/oblador/react-native-animatable){:rel="nofollow noreferrer" target="_blank"}ライブラリを使ってアニメーションを利用する方法について説明します。

このブログではリアクトネイティブ(React Native)に```typescript```と```styled-components```が適用されたプロジェクトで説明します。リアクトネイティブ(React Native)で```typescript```と```styled-components```を適用する方法については以前のブログを確認してください。

- [typescript]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}
- [styled-components]({{site.url}}/{{page.categories}}/styled-components/){:target="_blank"}

## ライブラリインストール

react-native-animatableライブラリを使うため、下記のコマンドでライブラリをインストールします。

```bash
npm install react-native-animatable --save
```

{% include in-feed-ads.html %}

## 基本的な使い方

下記のようにアニメーションを追加した部分にソースを追加します。

- Functional Component

```js
...
import * as Animatable from 'react-native-animatable';
...

const App = () => {
  ...
  return (
    <Animatable.Text animation="zoomInUp">Zoom me up, Scotty</Animatable.Text>
  );
}
```

- Class Component

```js
...
import * as Animatable from 'react-native-animatable';
...

export default class App extends React.Component<Props, State> {
  ...
  render() {
    ...
    return (
      <Animatable.Text animation="zoomInUp">Zoom me up, Scotty</Animatable.Text>
    );
  }
  ...
}
```

## イベントを通じて使い方

リアクトネイティブ(React Native)の```ref```を使ってユーザーイベントが発生した時、アニメーションが実行されるように作れます。

- Functional Component

```js
...
import * as Animatable from 'react-native-animatable';
...

const Page = () => {
  const AnimationRef = useRef(null);
  ...
  const _onPress = () => {
    if(AnimationRef) {
      AnimationRef.current?.bounce();
    }
  }
  ...
  return (
    <TouchableWithoutFeedback onPress={_onPress}>
      <Animatable.View ref={AnimationRef}>
        <Text>Bounce me!</Text>
      </Animatable.View>
    </TouchableWithoutFeedback>
  );
}
```

- Class Component

```js
...
import * as Animatable from 'react-native-animatable';
...

export default class Page extends React.Component<Props, State> {
  private AnimationRef;
  ...
  render() {
    ...
    return (
      <TouchableWithoutFeedback onPress={this._onPress}>
        <Animatable.View ref={ref => (this.AnimationRef = ref)}>
          <Text>Bounce me!</Text>
        </Animatable.View>
      </TouchableWithoutFeedback>
    );
  }
  ...
  private _onPress = () => {
    this.AnimationRef.bounce();
  }
  ...
}
```

{% include in-feed-ads.html %}

## styled-components

styled-componentsで作ったコンポーネント(component)にアニメーションを適用する方法です。

- Functional Component

```js
...
import styled from 'styled-components/native';
import * as Animatable from 'react-native-animatable';
...
const StyledImage = Animatable.createAnimatableComponent(styled.Image``);
...
const App = () => {
  ...
  return (
    <StyledImage
      animation="bounceIn"
      delay={1000}
      useNativeDriver={true}
      source={src}
    />
  );
}
```

- Class Component

```js
...
import styled from 'styled-components/native';
import * as Animatable from 'react-native-animatable';
...
const StyledImage = Animatable.createAnimatableComponent(styled.Image``);
...
export default class App extends React.Component<Props, State> {
  ...
  render() {
    ...
    return (
      <StyledImage
        animation="bounceIn"
        delay={1000}
        useNativeDriver={true}
        source={src}
      />
    );
  }
  ...
}
```

## 使えるアニメーション

使えるアニメーションは```react-native-animatable```の公式レポジトリ(Repository)で例と一緒に確認できます。

- [https://github.com/oblador/react-native-animatable](https://github.com/oblador/react-native-animatable){:rel="nofollow noreferrer" target="_blank"}

下記は使えるアニメーションのリストです。

- bounce
- flash
- jello
- pulse
- rotate
- rubberBand
- shake
- swing
- tada
- wobble
- bounceIn
- bounceInDown
- bounceInUp
- bounceInLeft
- bounceInRight
- bounceOut
- bounceOutDown
- bounceOutUp
- bounceOutLeft
- bounceOutRight
- fadeIn
- fadeInDown
- fadeInDownBig
- fadeInUp
- fadeInUpBig
- fadeInLeft
- fadeInLeftBig
- fadeInRight
- fadeInRightBig
- fadeOut
- fadeOutDown
- fadeOutDownBig
- fadeOutUp
- fadeOutUpBig
- fadeOutLeft
- fadeOutLeftBig
- fadeOutRight
- fadeOutRightBig
- flipInX
- flipInY
- flipOutX
- flipOutY
- lightSpeedIn
- lightSpeedOut
- slideInDown
- slideInUp
- slideInLeft
- slideInRight
- slideOutDown
- slideOutUp
- slideOutLeft
- slideOutRight
- zoomIn
- zoomInDown
- zoomInUp
- zoomInLeft
- zoomInRight
- zoomOut
- zoomOutDown
- zoomOutUp
- zoomOutLeft
- zoomOutRight

## 完了

簡単なアニメーションを早く導入したい時、```react-native-animatable```ライブラリを使うことをおすすめします。

## 参考

- [https://github.com/oblador/react-native-animatable](https://github.com/oblador/react-native-animatable){:rel="nofollow noreferrer" target="_blank"}
