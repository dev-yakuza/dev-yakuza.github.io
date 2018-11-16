---
layout: 'post'
permalink: '/react-native/react-navigation/'
paginate_path: '/react-native/:num/react-navigation/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'react-navigation'
description: 'react-navigationを使ってアプリを開発して見ましょう。'
image: '/assets/images/category/react-native/react-navigation.jpg'
---


## react-nativeプロジェクト生成
typescriptとstyled-componentsを適用したプロジェクトで進めます。RNへtypescriptとstyled-componentsを適用する方法は以前のブログをご参考してください。
- [typescript]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}
- [styled-components]({{site.url}}/{{page.categories}}/styled-components/){:target="_blank"}

## react-navigationインストール
react-navigationライブラリを下記のコマンドでインストールします。

{% include_relative common/installation.md %}

- react-navigation: react-navigationのライブラリです。
- @types/react-navigation: typescriptへ必要なreact-navigationのタイプです。

## 使い方
react-navigationを使うたくさんの方法が公式サイトへ詳しく載せております。ここには私たちが実際プロジェクトを進めながら使った内容をちょっとちょっと追加する予定です。
- 公式サイト: [react-navigation](https://reactnavigation.org/docs){:rel="nofollow noreferrer" target="_blank" }

### stack navigation
基本的スタックナビゲーションを使う方法です。

{% include_relative common/stack-navigation.md %}

- ```Navigator.tsx```へナビゲーションで使う画面とデフォルト画面を設定します。
- ```createStackNavigator```で生成された画面は基本的propsへnavigationを持ってます。
- ```this.props.navigation.navigate```を使って画面遷移します。
- ```this.props.navigation.goBack```を使って以前のページへ戻ります。

## Navigation barを隠す
下記のコードでnavigation barを隠せます。

{% include_relative common/hide-navigation-bar.md %}

- static navigationOptions: Navigationのオプションを設定します。
- { header: null }: navigation header barを非表示します。

## 参考
- 公式サイト: [react-navigation](https://reactnavigation.org/docs){:rel="nofollow noreferrer" target="_blank" }