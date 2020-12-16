---
layout: 'post'
permalink: '/react-native/react-native-image-modal/'
paginate_path: '/react-native/:num/react-native-image-modal/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'react-native-image-modal'
description: 'react-native-image-modalを使ってイメージを全体画面で表示して、pinch拡大、縮小などをしてみましょう。'
image: '/assets/images/category/react-native/2020/react-native-image-modal/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [プレビュー](#プレビュー)
- [インストール](#インストール)
- [使い方](#使い方)
- [Properties](#properties)
- [機能](#機能)
- [例題プロジェクト](#例題プロジェクト)
- [Contribute](#contribute)
- [完了](#完了)

</div>

## 概要

イメージを選択したら全体画面で表示して拡大、縮小する機能があるコンポーネントが必要になりました。多分検索すると上手く作ったコンポーネントがあると思いますが、今回は時間を掛って`react-native-image-modal`と言うコンポーネントを作ってみました。

このブログポストでは私が作った`react-native-image-modal`を使う方法についてみてみます。

- Github: [react-native-image-modal](https://github.com/dev-yakuza/react-native-image-modal){:target="_blank"}

## プレビュー

まず、今回使うreact-native-image-modalは下記のように動作します。

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2020/react-native-image-modal/pinch-zoom-and-move.gif" alt="react-native-image-modal動作画面">
</div>

{% include in-feed-ads.html %}

## インストール

下記のコマンドでreact-native-image-modalをインストールします。

```bash
npm install --save react-native-image-modal
```

## 使い方

下記のようにイメージを全体サイズで表示したいコンポーネント中へreact-native-image-modalをインポートします。

```js
import ImageModal from 'react-native-image-modal';
```

下記のようにイメージモーダルを追加して使います。

```js
{% raw %}
<ImageModal
  swipeToDismiss={false}
  resizeMode="contain"
  imageBackgroundColor="#000000"
  style={{
    width: imageWidth,
    height: 250,
  }}
  source={{
    uri:
      'https://cdn.pixabay.com/photo/2018/01/11/09/52/three-3075752_960_720.jpg',
  }}
/>
{% endraw %}
```

## Properties

基本的なReact NativeのImageコンポーネントのPropsをそのまま使えます。このPropsは初めて画面へ表示される原本のイメージへ適用されます。（全体サイズモーダルのイメージには適用されません。）

下記にある内容はreact-native-image-modalへ専用のPropsです。

| Prop | 必須 | タイプ | 説明 |
|------|----------|------|-------------|
| swipeToDismiss | X | boolean | スワイプして画面を閉じます。(`default: true`)  |
| imageBackgroundColor | X | string | 原本イメージのバックグラウンドの色。 |
| overlayBackgroundColor | X | string | 全体画面サイズのモーダルのバックグラウンドの色。(`default: #000000`)  |
| onLongPressOriginImage | X | () => void | 原本のイメージを長押した時呼び出せるコールバック関数。 |
| renderHeader | X | (close: () => void) => JSX.Element | Array<JSX.Element> | 全画面サイズモーダルのヘッダーの部分をカスタマイズする時使います。 |
| renderFooter | X | (close: () => void) => JSX.Element | Array<JSX.Element> | 全画面サイズモーダルのフッターをカスタマイズする時使います。 |
| onTap | X | (eventParams: {locationX: number; locationY: number; pageX: number; pageY: number;}) => void  | 全画面サイズモーダルのイメージを一回タップする時呼び出せるコールバック関数。 |
| onDoubleTap | X | () => void | 全画面サイズモーダルのイメージを二回タップする時呼び出せるコールバック関数。 |
| onLongPress | X | () => void | 全画面サイズモーダルのイメージを長押す時呼び出せるコールバック関数。 |
| onOpen | X | () => void | 全画面サイズモーダルが開く時のコールバック |
| didOpen | X | () => void | 全画面サイズモーダルが完全に開いた後のコールバック  |
| onMove | X | (position: {type: string; positionX: number; positionY: number; scale: number; zoomCurrentDistance: number;}) => void  | 全画面サイズモーダルのイメージを移動する時のコールバック |
| responderRelease | X | (vx?: number, scale?: number) => void | タッチイベントが終わる時のコールバック |
| willClose | X | () => void | 全画面サイズモーダルが閉じる前のコールバック |
| onClose | X | () => void | 全画面サイズモーダルが閉じる時のコールバック |

{% include in-feed-ads.html %}

## 機能

react-native-image-modalは甲斐のような機能を持っています。

- イメージモダールを開く/閉じる

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2020/react-native-image-modal/open-and-close-image-modal.gif" alt="react-native-image-modalイメージモダールを開く/閉じる">
</div>

- イメージをpinchで拡大、縮小、移動

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2020/react-native-image-modal/pinch-zoom-and-move.gif" alt="react-native-image-modalイメージをpinchで拡大、縮小、移動">
</div>

- イメージをダブルタップで拡大、縮小

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2020/react-native-image-modal/double-tap-zoom.gif" alt="react-native-image-modalイメージをダブルタップで拡大、縮小">
</div>

- スワイプでモーダルを閉じる

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2020/react-native-image-modal/swipe-to-dismiss.gif" alt="react-native-image-modalスワイプでモーダルを閉じる">
</div>

{% include in-feed-ads.html %}

## 例題プロジェクト

Githubリポジトリへ例題プロジェクトも含まれています。

- Github: [react-native-image-modal](https://github.com/dev-yakuza/react-native-image-modal){:target="_blank"}

例題ソースを確認するため下記のようにGithubリポジトリをクロンします。

```bash
git clone https://github.com/dev-yakuza/react-native-image-modal.git
```

例題プロジェクトへ必要なライブラリをインストールします。

```bash
cd Example
npm install

# iOS
cd ios
pod install
```

下記のコマンドを使って例題プロジェクトを実行します。

```bash
# Example folder
# iOS
npm run ios
# Android
npm run android
```

## Contribute

初めて作ったopensourceなので、完璧ではないと思います。もし、バグや機能を追加したい方がいるならプルリ投げてください。

少しでも楽にContributeできるように、このプロジェクトを開発する方法について共有します。

- プロジェクトをクロンします。

```bash
git clone https://github.com/dev-yakuza/react-native-image-modal.git
```

- 下記のコマンドで開発環境を構築してタイプスクリプトを実行します。

```bash
npm install
npm start
```

- 下記のコマンドで開発用のプロジェクトを実行します。

```bash
cd Develop
npm install

# android
npm run android

# ios
cd ios
pod install
cd ..
npm run ios
```

## 完了

これで私が初めて作ったOpensource、react-native-image-modalを使う方法についてみてみました。たくさんの方へ役に立てほしいです。