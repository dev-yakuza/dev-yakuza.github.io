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

```bash
npm install --save react-navigation
npm install --save react-native-gesture-handler
```

## react-native-gesture-handlerライブラリ連結
下記のコマンドで```react-native-gesture-handler```ライブラリをRN(react-native)プロジェクトへ連結します。

```bash
react-native link react-native-gesture-handler
```

## 使い方
react-navigationを使う色んな方法は公式サイトに詳しく載せております。詳しく内容はリンクを参考してください。

- 公式シアト: [https://reactnavigation.org/docs](https://reactnavigation.org/docs){:rel="nofollow noreferrer" target="_blank" }

私たちは公式サイトを参考して基本的な使い方を纏めてリポジトリ(Repository)を作りました。```react-navigation```を使う前このリポジトリ(Repository)を確認すると基本的な構造を作る時、ご参考になると思います。

- react-navigation-exercise: [https://github.com/dev-yakuza/react-navigation-exercise](https://github.com/dev-yakuza/react-navigation-exercise){:rel="nofollow noreferrer" target="_blank" }

このリポジトリ(Repository)に開発された内容を説明します。

### 使うナビゲーション
使うナビゲーション(Navigation)を追加(import)して使います。

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

### createBottomTabNavigator
この```createBottomTabNavigator```を使って下にタブナビゲーション(Tab Navigation)を表示します。
이 함수를 사용하여 하단에 탭 네비게이션(Tab navigation)을 표시합니다.

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