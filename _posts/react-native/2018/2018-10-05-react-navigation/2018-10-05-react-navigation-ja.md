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

<div id="contents_list" markdown="1">

## 目次

1. [react-navigation V5](#react-native-v5)
1. [リアクトネイティブ(React Native)プロジェクト生成](#リアクトネイティブreact-nativeプロジェクト生成)
1. [react-navigationインストール](#react-navigationインストール)
    - [react-navigation V4](#react-navigation-v4)
        - [react-navigation-stack](#react-navigation-stack)
        - [react-navigation-tabs](#react-navigation-tabs)
        - [react-navigation-drawer](#react-navigation-drawer)
    - [react-navigation V3](#react-navigation-v3)
    - [react-native-gesture-handlerライブラリ連結](#react-native-gesture-handlerライブラリ連結)
1. [使い方](#使い方)
    - [使うナビゲーション](#使うナビゲーション)
        - [V4](#v4)
        - [V3](#v3)
    - [createAppContainer](#createappcontainer)
    - [createSwitchNavigator](#createswitchnavigator)
    - [createStackNavigator](#createstacknavigator)
    - [createBottomTabNavigator](#createbottomtabnavigator)
    - [ナビゲーション転換](#ナビゲーション転換)
1. [Navigation barを隠す](#navigation-barを隠す)
1. [参考](#参考)

</div>

## react-navigation V5

react-navigation V5に関しては別のブログポストを作成しました。V5に関して知りたい方は下記のリンクを押して確認してください。

- [react-navigation-v5]({{site.url}}/{{page.categories}}/react-navigation-v5/){:target="_blank"}

## リアクトネイティブ(React Native)プロジェクト生成

typescriptとstyled-componentsを適用したプロジェクトで進めます。RNへtypescriptとstyled-componentsを適用する方法は以前のブログをご参考してください。

- [typescript]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}
- [styled-components]({{site.url}}/{{page.categories}}/styled-components/){:target="_blank"}

## react-navigationインストール

### react-navigation V4

react-navigation ライブラリを下記のコマンドでインストールします。

```bash
npm install --save react-navigation react-native-gesture-handler react-native-reanimated react-native-screens
```

react-navigation V4からナビゲーションが細分化されました。下記のように使うナビゲーションによるライブラリを追加でインストールする必要があります。

#### react-navigation-stack

使えるナビゲーション

- createStackNavigator
- StackGestureContext
- Transitioner
- StackView
- StackViewCard
- StackViewTransitionConfigs
- Header
- HeaderTitle
- HeaderBackButton
- HeaderStyleInterpolator

インストールコマンド

```bash
npm install --save react-navigation-stack
```

#### react-navigation-tabs

使えるナビゲーション

- createBottomTabNavigator
- createMaterialTopTabNavigator
- BottomTabBar
- MaterialTopTabBar

インストールコマンド

```bash
npm install --save react-navigation-tabs
```

#### react-navigation-drawer

使えるナビゲーション

- createDrawerNavigator
- DrawerGestureContext
- DrawerRouter
- DrawerActions
- DrawerView
- DrawerNavigatorItems
- DrawerSidebar

インストールコマンド

```bash
npm install --save react-navigation-drawer
```

インストールが終わったら、iOSのモジュールを連動するため下記のコマンドを実行します。

```bash
cd ios
pod install
cd ...
```

{% include in-feed-ads.html %}

### react-navigation V3

react-navigationライブラリを下記のコマンドでインストールします。

```bash
npm install --save react-navigation react-native-gesture-handler
npm install --save-dev @types/react-navigation
```

### react-native-gesture-handlerライブラリ連結

下記のコマンドで```react-native-gesture-handler```ライブラリをリアクトネイティブ(React Native)プロジェクトへ連結します。

```bash
react-native link react-native-gesture-handler
```

## 使い方

react-navigationを使う色んな方法は公式サイトに詳しく載せております。詳しく内容はリンクを参考してください。

- 公式シアト: [https://reactnavigation.org/docs](https://reactnavigation.org/docs){:rel="nofollow noreferrer" target="_blank" }

私たちは公式サイトを参考して基本的な使い方を纏めてリポジトリ(Repository)を作りました。```react-navigation```を使う前このリポジトリ(Repository)を確認すると基本的な構造を作る時、ご参考になると思います。

- react-navigation-exercise V4: [https://github.com/dev-yakuza/react-navigation-v4-exercise](https://github.com/dev-yakuza/react-navigation-v4-exercise){:rel="nofollow noreferrer" target="_blank" }
- react-navigation-exercise V3: [https://github.com/dev-yakuza/react-navigation-exercise](https://github.com/dev-yakuza/react-navigation-exercise){:rel="nofollow noreferrer" target="_blank" }

このリポジトリ(Repository)に開発された内容を説明します。

{% include in-feed-ads.html %}

### 使うナビゲーション

使うナビゲーション(Navigation)を追加(import)して使います。

#### V4

```js
import {createSwitchNavigator, createAppContainer} from 'react-navigation';
import {
  createBottomTabNavigator,
  createMaterialTopTabNavigator,
} from 'react-navigation-tabs';
import {createStackNavigator} from 'react-navigation-stack';
```

#### V3

```js
import {
  createSwitchNavigator,
  createBottomTabNavigator,
  createStackNavigator,
  createAppContainer,
} from 'react-navigation';
```

### createAppContainer

アプリ(App)で```react-navigation```を使うためには```createAppContainer```をトップナビゲーション(Navigation)に使え必要があります。

### createSwitchNavigator

アプリ(App)に基本的にログイン機能があったら、```createSwitchNavigator```を使えことをおすすめします。私たちのリポジトリ(Repository)はSwitch Navigationを基本ナビゲーション(Navigaion)で使ってます。

```js
export default createAppContainer(
  createSwitchNavigator(
    {
      AuthLoading,
      Auth,
      MainNavi,
    },
    {
      initialRouteName: 'AuthLoading',
    }
  )
);
```

### createStackNavigator

この```createStackNavigator```はビュー(View)の上に別のビュー(View)を積む(Stack)ナビゲーション(Navigation)です。私たちはこのナビゲーション(Navigation)を使ってタブナビゲーション(Tab Navigation)上にフルスクリーンのビュー(View)を表示するとき、タブナビゲーション(Tab Navigation)中で別のビュー(View)を表示する時使います。

```js
const MainNavi = createStackNavigator({
  MainTab: {
    screen: MainTab,
    navigationOptions: ({ navigation }) => ({
      header: null,
    }),
  },
  FullDetail,
});
```

{% include in-feed-ads.html %}

### createBottomTabNavigator

この```createBottomTabNavigator```を使って下にタブナビゲーション(Tab Navigation)を表示します。

```js
const MainTab = createBottomTabNavigator({
  FirstTabStack,
  SecondTab,
  ThirdTab,
});
```

### ナビゲーション転換

ビュー(View)から別のビュー(View)に切り替える時、下記のコードを使います。

```js
this.props.navigation.navigate('MainTab');
```

## Navigation barを隠す

下記のコードでnavigation barを隠せます。

```js
...
export default class Home extends React.Component<Props, State> {
  static navigationOptions = { header: null };

  render() {
    return (
      <Container>
        <StyledText>Home screen!</StyledText>
      </Container>
    );
  }
}
...
```

- static navigationOptions: Navigationのオプションを設定します。
- { header: null }: navigation header barを非表示します。

## 参考

- 公式サイト: [react-navigation](https://reactnavigation.org/docs){:rel="nofollow noreferrer" target="_blank" }
