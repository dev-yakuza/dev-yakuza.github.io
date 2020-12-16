---
layout: 'post'
permalink: '/react-native/react-navigation-v5/'
paginate_path: '/react-native/:num/react-navigation-v5/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'react-navigation V5'
description: 'react-navigation V5をインストールして使う方法について共有します。'
image: '/assets/images/category/react-native/2018/react-navigation-v5/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [react-nativeプロジェクト生成](#react-nativeプロジェクト生成)
- [react-navigation V5インストール](#react-navigation-v5インストール)
- [追加的に必要なNavigationインストール](#追加的に必要なnavigationインストール)
  - [Stack Navigation](#stack-navigation)
  - [Drawer Navigation](#drawer-navigation)
  - [Bottom Tab Navigation](#bottom-tab-navigation)
  - [Material Bottom Tab Navigation](#material-bottom-tab-navigation)
  - [Material Top Tab Navigation](#material-top-tab-navigation)
- [使い方](#使い方)
  - [react-native-gesture-handler](#react-native-gesture-handler)
  - [NavigationContainer](#navigationcontainer)
  - [Auth処理](#auth処理)
  - [Stack Navigation 使い方](#stack-navigation-使い方)
  - [Drawer Navigation 使い方](#drawer-navigation-使い方)
  - [Bottom Tab Navigation 使い方](#bottom-tab-navigation-使い方)
  - [Material Bottom Tab Navigation 使い方](#material-bottom-tab-navigation-使い方)
  - [Material Top Tab Navigation 使い方](#material-top-tab-navigation-使い方)
  - [Drawer Open](#drawer-open)
  - [DrawerActions](#draweractions)
  - [setParams / getParams](#setparams--getparams)
- [Typescript](#typescript)
  - [navigation](#navigation)
  - [route](#route)
- [完了](#完了)
- [参考](#参考)

</div>

## 概要

react-navigationのバージョン5は結構色々変わりましたね。V3とV4はちょっと似てる感じがありましたが、V5は全然違うNavigationを使う感じでした。だから、このようにreact-navigation V5に関するブログポストを作成することにしました。

以前のバージョン(V3, V4)に関して知りたい方は、以前のブログを参考してください。

- [react-navigation]({{site.url}}/{{page.categories}}/react-navigation/){:target="_blank"}

react-navigationのV5に関する公式サイトは下記になります。

- 公式サイト: [https://reactnavigation.org](https://reactnavigation.org){:rel="nofollow noreferrer" target="_blank" }

このブログポストではreact-navigation V5を使う方法について説明します。

## react-nativeプロジェクト生成

ここで紹介するソースコードはtypescriptとstyled-componentsが適用されております。React Nativeへtypescriptとstyled-componentsを適用する方法に関しては以前のブログを参考してください。

- [typescript]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}
- [styled-components]({{site.url}}/{{page.categories}}/styled-components/){:target="_blank"}
- [root-import]({{site.url}}/{{page.categories}}/root-import/){:target="_blank"}

{% include in-feed-ads.html %}

## react-navigation V5インストール

react-navigation v5ライブラリを下記のコマンドでインストールします。

```bash
npm install --save @react-navigation/native
```

また、 react-navigation v5を使うために必要なライブラリたちを下記のコマンドでインストールします。

```bash
npm install --save react-native-reanimated react-native-gesture-handler react-native-screens react-native-safe-area-context @react-native-community/masked-view
```

インストールが終わったら、iOSフォルダに行って、下記のコマンドを実行します。

```bash
# cd ios
pod install
```

## 追加的に必要なNavigationインストール

react-navigation V4からNavigationを使うためには、使いたいNavigationを別々でインストールしました。V5も同じように使いたいNavigationを使うためには追加的にNavigationライブラリをインストールする必要があります。

### Stack Navigation

1つの画面の上に、他の画面を積み上げるように画面を遷移するNavigationをStack Navigationと言います。

<div class="half_image_container">
  <img class="half_image" src="/assets/images/category/react-native/2018/react-navigation-v5/stack.gif" alt="React Navigation V5 stack Navigation">
</div>
[イメージ: [reactnavigation.org 公式サイト](https://reactnavigation.org/docs/stack-navigator){:rel="nofollow noreferrer" target="_blank" }]

Stack Navigationを使うためには下記のコマンドで追加ライブラリをインストールする必要があります。

```bash
npm install --save @react-navigation/stack
```

### Drawer Navigation

主にメニューで使うNavigationでユーザのSwipeアクションで画面に表示されるNavigationです。

<div class="half_image_container">
  <img class="half_image" src="/assets/images/category/react-native/2018/react-navigation-v5/drawer.gif" alt="React Navigation V5 drawer Navigation">
</div>
[イメージ: [reactnavigation.org 公式サイト](https://reactnavigation.org/docs/drawer-navigator){:rel="nofollow noreferrer" target="_blank" }]

Drawer Navigationを使うためには下記のコマンドで追加ライブラリをインストールする必要があります。

```bash
npm install --save @react-navigation/drawer
```

### Bottom Tab Navigation

画面の下でTabで画面を切り替えるNavigationです。

<div class="half_image_container">
  <img class="half_image" src="/assets/images/category/react-native/2018/react-navigation-v5/bottom-tabs-demo.gif" alt="React Navigation V5 bottom-tabs-demo Navigation">
</div>
[イメージ: [reactnavigation.org 公式サイト](https://reactnavigation.org/docs/bottom-tab-navigator){:rel="nofollow noreferrer" target="_blank" }]

Bottom Tab Navigationを使うためには下記のコマンドで追加ライブラリをインストールする必要があります。

```bash
npm install --save @react-navigation/bottom-tabs
```

{% include in-feed-ads.html %}

### Material Bottom Tab Navigation

Bottom Tab Navigationと同じように画面の下でTabで画面を切り替えるNavigationです。ここにGoogleのMaterialデザインが適用されたNavigationになります。

<div class="half_image_container">
  <img class="half_image" src="/assets/images/category/react-native/2018/react-navigation-v5/material-bottom-tabs.gif" alt="React Navigation V5 Material Bottom Tab Navigation">
</div>
[イメージ: [reactnavigation.org 公式サイト](https://reactnavigation.org/docs/material-bottom-tab-navigator){:rel="nofollow noreferrer" target="_blank" }]

Material Bottom Tab Navigationを使うためには下記のコマンドで追加ライブラリをインストールする必要があります。

```bash
npm install --save @react-navigation/material-bottom-tabs react-native-paper
```

このNavigationは`react-native-vector-icons`と言うライブラリが追加的に必要になります。react-native-vector-iconsをインストールする方法については下記のリンクを参考してください。

- [react-native-vector-icons]({{site.url}}/{{page.categories}}/react-native-vector-icons/){:target="_blank"}

### Material Top Tab Navigation

GoogleのMaterialデザインが適用されたNavigationで、画面の上でTabで画面を切り替えるNavigationです。

<div class="half_image_container">
  <img class="half_image" src="/assets/images/category/react-native/2018/react-navigation-v5/material-top-tabs.gif" alt="React Navigation V5 material-top-tabs Navigation">
</div>
[イメージ: [reactnavigation.org 公式サイト](https://reactnavigation.org/docs/material-top-tab-navigator){:rel="nofollow noreferrer" target="_blank" }]

Material Top Tab Navigationを使うためには下記のコマンドで追加ライブラリをインストールする必要があります。

```bash
npm install --save @react-navigation/material-top-tabs react-native-tab-view
```

## 使い方

react-navigationを色んな方法が公式サイトに詳しく書いております。詳しい内容は下記のリンクを参考してください。

- 公式サイト: [https://reactnavigation.org/docs](https://reactnavigation.org/docs){:rel="nofollow noreferrer" target="_blank" }

このブログでは公式サイトを参考して基本的な使い方をまとめたリポジトリ(Repository)を作りました。`react-navigation`を使う前にこのリポジトリ(Repository)を確認したら、基本的な構造を作る時、役に立つと思います。

- react-navigation-exercise V5: [https://github.com/dev-yakuza/react-navigation-v5-exercise](https://github.com/dev-yakuza/react-navigation-v5-exercise){:rel="nofollow noreferrer" target="_blank" }

このリポジトリ(Repository)に実装された内容を説明します。

{% include in-feed-ads.html %}

### react-native-gesture-handler

react-navigationを使うためには`react-native-gesture-handler`をimportする必要があります。`index.js`ファイル、または`App.js`ファイル(react-navigationを使うコンポーネントのトップコンポーネント)を下記のように修正します。

```js
import 'react-native-gesture-handler';
...
```

### NavigationContainer

V4ではNavigationを使うためには`createAppContainer`を最後に使わなきゃならなかったんです。

```js
{% raw %}
import {createAppContainer} from 'react-navigation';
...
export default createAppContainer(
  ...
);
{% endraw %}
```

V5でもV4と同じように最後には`NavigationContainer`と言うコンポーネントを提供する必要があります。

```js
{% raw %}
import React from 'react';
import {NavigationContainer} from '@react-navigation/native';
...
export default () => {
  return (
    <NavigationContainer>
      ...
    </NavigationContainer>
  );
};
{% endraw %}
```

もう既に違さが見えますか？既存のreact-navigationは設定に近い感じでしたが、V5はReactのコンポーネントを使う感じです。

### Auth処理

V4ではAuth部分を処理するために`createSwitchNavigator`と言うNavigationを提供してくれました。

```js
{% raw %}
import {createSwitchNavigator, createAppContainer} from 'react-navigation';
...
import AuthLoading from './AuthLoading';
import Auth from './Auth';
...
export default createAppContainer(
  createSwitchNavigator(
    {
      AuthLoading,
      Auth,
      MainNavi,
    },
    {
      initialRouteName: 'AuthLoading',
    },
  ),
);
{% endraw %}
```

createSwitchNavigatorは上のように使うことができます。AuthLoadingと言うReactコンポーネントでログインをチェックして、ログインができてない場合はAuth画面を、ログインされたら、MainNavi画面に遷移させました。

V5では`createSwitchNavigator`がなくなりました。上のようにAuthを処理するためには下記のようにreact-navigationを使う必要があります。

```js
{% raw %}
import React, {useContext} from 'react';
import {NavigationContainer} from '@react-navigation/native';
...
import {UserContext} from '~/Context/User';
...
export default () => {
  const {userInfo} = useContext<IUserContext>(UserContext);

  return (
    <NavigationContainer>
      {userInfo ? <MainNavi /> : <LoginStackNavi />}
    </NavigationContainer>
  );
};
{% endraw %}
```

V5ではcreateSwitchNavigatorがありません。その代わり、V5はV4とは違ってReactのコンポーネント形式なので、Navigationの中で直接ログインをチェックしてどの画面を表示するか決めます。
公式サイトでも上のような方法を案内してるので、参考してみてください。

- 公式サイト: [react-navigation - Auth flow](https://reactnavigation.org/docs/auth-flow){:rel="nofollow noreferrer" target="_blank" }

### Stack Navigation 使い方

react-navigation V5では下記のようにStack Navigationを使いました。

```js
{% raw %}
...
import {createStackNavigator} from 'react-navigation-stack';
...
const MainNavi = createStackNavigator({
  MainTab: {
    screen: MainTab,
    navigationOptions: ({navigation}) => ({
      header: null,
    }),
  },
  FullDetail,
});
...
{% endraw %}
```

react-navigation V5では下記のようにStack Navigationを使います。

```js
{% raw %}
...
import {
  createStackNavigator,
} from '@react-navigation/stack';
...
const Stack = createStackNavigator();
...
const LoginStackNavi = () => {
  return (
    <Stack.Navigator
      screenOptions={{
        headerStyle: {
          backgroundColor: '#f4511e',
        },
        headerTintColor: '#fff',
        headerTitleStyle: {
          fontWeight: 'bold',
        },
      }}>
      <Stack.Screen
        name="SignIn"
        component={SignIn}
        options={{
          headerShown: false,
        }}
      />
      <Stack.Screen
        name="SignUp"
        component={SignUp}
        options={{headerBackTitleVisible: false}}
      />
      <Stack.Screen name="ResetPassword" component={ResetPassword} />
    </Stack.Navigator>
  );
};
{% endraw %}
```

react-navigation V5でStack Navigation全部に共通的にプロパティを適用したい場合、 `Stack.Navigator`の`screenOptions`を使います。

逆に、各画面だけにプロパティを適用したいばあいは、`Stack.Screen`の`options`を使います。

上の例題ではよく使うHeader Barを隠すため、`options`の`headerShown`を使いました。

```js
{% raw %}
<Stack.Screen
  name="SignIn"
  component={SignIn}
  options={{
    headerShown: false,
  }}
/>
{% endraw %}
```

また、戻るボタンのタイトルを隠すため、`options`の`headerBackTitleVisible`も使ってみました。

```js
{% raw %}
<Stack.Screen
  name="SignUp"
  component={SignUp}
  options={{headerBackTitleVisible: false}}
/>
{% endraw %}
```

{% include in-feed-ads.html %}

### Drawer Navigation 使い方

react-navigation V5では下記のようにDrawer Navigationを使います。

```js
{% raw %}
...
import {
  createDrawerNavigator,
  DrawerContentScrollView,
  DrawerItemList,
  DrawerItem,
  DrawerContentComponentProps,
  DrawerContentOptions,
  DrawerNavigationProp,
} from '@react-navigation/drawer';
...
const Drawer = createDrawerNavigator();
...
const CustomDrawerContent = (
  props: DrawerContentComponentProps<DrawerContentOptions>,
  logout: () => void,
) => {
  return (
    <DrawerContentScrollView {...props}>
      <DrawerItemList {...props} />
      <DrawerItem label="Logout" onPress={() => logout()} />
    </DrawerContentScrollView>
  );
};
const DrawNavi = () => {
  const {logout} = useContext<IUserContext>(UserContext);

  return (
    <Drawer.Navigator
      drawerContent={props => CustomDrawerContent(props, logout)}>
      <Drawer.Screen name="TabNavi" component={TabNavi} />
      <Drawer.Screen name="MaterialTabNavi" component={MaterialTabNavi} />
      <Drawer.Screen
        name="MaterialTopTabNaviStackNavi"
        component={MaterialTopTabNaviStackNavi}
      />
    </Drawer.Navigator>
  );
};
...
{% endraw %}
```

ここでは`Logout`の機能を実装するためちょっと複雑になりました。Logoutの機能を抜いて見ると下記になります。

```js
{% raw %}
...
import {
  createDrawerNavigator,
} from '@react-navigation/drawer';
...
const Drawer = createDrawerNavigator();
...
const DrawNavi = () => {
  return (
    <Drawer.Navigator>
      <Drawer.Screen name="TabNavi" component={TabNavi} />
      <Drawer.Screen name="MaterialTabNavi" component={MaterialTabNavi} />
      <Drawer.Screen
        name="MaterialTopTabNaviStackNavi"
        component={MaterialTopTabNaviStackNavi}
      />
    </Drawer.Navigator>
  );
};
...
{% endraw %}
```

Stack Navigationとすごく似てます。上の例題ではこの状態で`Logout`と言う項目を出して、その項目を押すとログアウトされるようにしたので、少し複雑になりました。

### Bottom Tab Navigation 使い方

react-navigation V5ではBottom Tab Navigationは下記のように使います。

```js
{% raw %}
...
import {createBottomTabNavigator} from '@react-navigation/bottom-tabs';
import Icon from 'react-native-vector-icons/MaterialIcons';
...
const Tab = createBottomTabNavigator();
...
const TabNavi = () => {
  return (
    <Tab.Navigator>
      <Tab.Screen
        name="TabFirstStackNavi"
        component={TabFirstStackNavi}
        options={{
          tabBarLabel: 'Frist',
          tabBarIcon: ({color}) => <Icon name="home" color={color} size={26} />,
        }}
      />
      <Tab.Screen
        name="TabSecond"
        component={TabSecond}
        options={{
          tabBarLabel: 'Second',
          tabBarIcon: ({color}) => (
            <Icon name="people" color={color} size={26} />
          ),
        }}
      />
      <Tab.Screen
        name="TabThird"
        component={TabThird}
        options={{
          tabBarLabel: 'Third',
          tabBarIcon: ({color}) => (
            <Icon name="message" color={color} size={26} />
          ),
        }}
      />
      <Tab.Screen
        name="TabFourth"
        component={TabFourth}
        options={{
          tabBarLabel: 'Fourth',
          tabBarIcon: ({color}) => (
            <Icon name="settings" color={color} size={26} />
          ),
        }}
      />
    </Tab.Navigator>
  );
};
...
{% endraw %}
```

上の例題ではTabのLabelとIconを別に表示するために`Tab.Screen`の`options`を使いました。

```js
{% raw %}
<Tab.Screen
  ...
  options={{
    tabBarLabel: 'Fourth',
    tabBarIcon: ({color}) => (
      <Icon name="settings" color={color} size={26} />
    ),
  }}
/>
{% endraw %}
```

{% include in-feed-ads.html %}

### Material Bottom Tab Navigation 使い方

react-navigation V5ではMaterial Bottom Tab Navigationは下記のように使います。

```js
{% raw %}
...
import {createMaterialBottomTabNavigator} from '@react-navigation/material-bottom-tabs';
import Icon from 'react-native-vector-icons/MaterialIcons';
...
const MaterialTab = createMaterialBottomTabNavigator();
...
const MaterialTabNavi = () => {
  return (
    <MaterialTab.Navigator>
      <MaterialTab.Screen
        name="TabFirstStackNavi"
        component={TabFirstStackNavi}
        options={{
          tabBarColor: '#281b39',
          tabBarLabel: 'Frist',
          tabBarIcon: ({color}) => <Icon name="home" color={color} size={26} />,
        }}
      />
      <MaterialTab.Screen
        name="TabSecond"
        component={TabSecond}
        options={{
          tabBarColor: '#0e141d',
          tabBarLabel: 'Second',
          tabBarIcon: ({color}) => (
            <Icon name="people" color={color} size={26} />
          ),
        }}
      />
      <MaterialTab.Screen
        name="TabThird"
        component={TabThird}
        options={{
          tabBarColor: '#E64A19',
          tabBarLabel: 'Third',
          tabBarIcon: ({color}) => (
            <Icon name="message" color={color} size={26} />
          ),
        }}
      />
      <MaterialTab.Screen
        name="TabFourth"
        component={TabFourth}
        options={{
          tabBarColor: '#524365',
          tabBarLabel: 'Fourth',
          tabBarIcon: ({color}) => (
            <Icon name="settings" color={color} size={26} />
          ),
        }}
      />
    </MaterialTab.Navigator>
  );
};
{% endraw %}
```

Material Bottom Tab Navigationを使う時はTab BarでIconを設定する必要があります。

```js
{% raw %}
<MaterialTab.Screen
  ...
  options={{
    ...
    tabBarIcon: ({color}) => (
      <Icon name="settings" color={color} size={26} />
    ),
  }}
/>
{% endraw %}
```

また、各タブを選択した時、タブの色を変更したい場合、`tabBarColor`を設定します。

```js
{% raw %}
<MaterialTab.Screen
  ...
  options={{
    ...
    tabBarColor: '#524365',
    ...
  }}
/>
{% endraw %}
```

tabBarIconは必須的に追加する必要がありますが、tabBarColorは必要な時だけ追加して使えばいいと思います。

### Material Top Tab Navigation 使い方

react-navigation V5でMaterial Top Tab Navigationは下記のように使います。

```js
{% raw %}
...
import {createMaterialTopTabNavigator} from '@react-navigation/material-top-tabs';
...
const MaterailTopTab = createMaterialTopTabNavigator();
...
const MaterialTopTabNavi = () => {
  return (
    <MaterailTopTab.Navigator>
      <MaterailTopTab.Screen name="TabFirst" component={TabFirst} />
      <MaterailTopTab.Screen name="TabSecond" component={TabSecond} />
      <MaterailTopTab.Screen name="TabThird" component={TabThird} />
      <MaterailTopTab.Screen name="TabFourth" component={TabFourth} />
    </MaterailTopTab.Navigator>
  );
};
...
const MaterialTopTabNaviStackNavi = ({navigation}: DrawerProp) => {
  return (
    <Stack.Navigator
      screenOptions={{
        headerLeft: (props: StackHeaderLeftButtonProps) => (
          <IconButton
            iconName="menu"
            onPress={() => navigation.openDrawer()}
            color="black"
          />
        ),
      }}>
      <Stack.Screen name="MaterialTopTabNavi" component={MaterialTopTabNavi} />
    </Stack.Navigator>
  );
};
...
{% endraw %}
```

Material Top Tab Navigationは下記のように簡単に定義して使えます。

```js
{% raw %}
const MaterialTopTabNavi = () => {
  return (
    <MaterailTopTab.Navigator>
      <MaterailTopTab.Screen name="TabFirst" component={TabFirst} />
      <MaterailTopTab.Screen name="TabSecond" component={TabSecond} />
      <MaterailTopTab.Screen name="TabThird" component={TabThird} />
      <MaterailTopTab.Screen name="TabFourth" component={TabFourth} />
    </MaterailTopTab.Navigator>
  );
};
{% endraw %}
```

しかし、`Notch Design`ではNavigationが全部見えないです。

![notch designでmaterial top navigationの問題](/assets/images/category/react-native/2018/react-navigation-v5/notch-design-material-top-navigation-problem.jpg)

この問題を解決するため、Stack Navigationで庇って提供することをお勧めします。

```js
{% raw %}
...
const MaterialTopTabNavi = () => {
  return (
    <MaterailTopTab.Navigator>
      <MaterailTopTab.Screen name="TabFirst" component={TabFirst} />
      <MaterailTopTab.Screen name="TabSecond" component={TabSecond} />
      <MaterailTopTab.Screen name="TabThird" component={TabThird} />
      <MaterailTopTab.Screen name="TabFourth" component={TabFourth} />
    </MaterailTopTab.Navigator>
  );
};
...
const MaterialTopTabNaviStackNavi = ({navigation}: DrawerProp) => {
  return (
    <Stack.Navigator
      screenOptions={{
        headerLeft: (props: StackHeaderLeftButtonProps) => (
          <IconButton
            iconName="menu"
            onPress={() => navigation.openDrawer()}
            color="black"
          />
        ),
      }}>
      <Stack.Screen name="MaterialTopTabNavi" component={MaterialTopTabNavi} />
    </Stack.Navigator>
  );
};
...
{% endraw %}
```

Stack Navigationで庇って、提供すると、下記のような画面が見えます。

![notch designでmaterial top navigationの問題解決](/assets/images/category/react-native/2018/react-navigation-v5/solution-notch-design-material-top-navigation-problem.jpg)

{% include in-feed-ads.html %}

### Drawer Open

普通にDrawer Navigationだけで使うと、下記のような画面が見えます。

<div class="half_image_container">
  <img class="half_image" src="/assets/images/category/react-native/2018/react-navigation-v5/drawer.gif" alt="React Navigation V5 drawer Navigation">
</div>
[イメージ]: [reactnavigation.org 公式サイト](https://reactnavigation.org/docs/drawer-navigator){:rel="nofollow noreferrer" target="_blank" }]

上のように左からみぎにSwipeをしないとDrawer Navigationを確認することができないです。

しかし、普通はNavigationのHeaderへメニューアイコンがあって、そのアイコンを押すと、Drawer Navigationが表示されるように作ります。

このようにするため、Stack NavigationでNavigation Headerを表示させて、Headerの左にメニューアイコンを表示して、メニューアイコンを押すと`openDrawer`と言う関数を使ってDrawer Navigationを開けるように実装しました。

```js
{% raw %}
...
import {
  ...
  DrawerNavigationProp,
} from '@react-navigation/drawer';
...
type TypeDrawerProp = DrawerNavigationProp<
  {
    TabNavi: undefined;
    MaterialTabNavi: undefined;
    MaterialTopTabNaviStackNavi: undefined;
    Logout: undefined;
  },
  'TabNavi'
>;
interface DrawerProp {
  navigation: TypeDrawerProp;
}
...
const MaterialTopTabNaviStackNavi = ({navigation}: DrawerProp) => {
  return (
    <Stack.Navigator
      screenOptions={{
        headerLeft: (props: StackHeaderLeftButtonProps) => (
          <IconButton
            iconName="menu"
            onPress={() => navigation.openDrawer()}
            color="black"
          />
        ),
      }}>
      <Stack.Screen name="MaterialTopTabNavi" component={MaterialTopTabNavi} />
    </Stack.Navigator>
  );
};
{% endraw %}
```

### DrawerActions

上の例題ようにDrawer Navigationに直接連動された画面ではnavigationのPropsを使ってDrawerを開けることができます。
しかし、下記のようにDrawer Navigationへ直接連動されてない場合は、navigationのPropsを使ってDrawerを開けることができないです。

```js
{% raw %}
...
const MainTabs = () => {
  return (
    <BottomTab.Navigator tabBarOptions={{activeTintColor: 'black'}}>
      <BottomTab.Screen name="MyFeed" component={MyFeed}/>
      <BottomTab.Screen name="Feeds" component={Feeds}/>
      <BottomTab.Screen name="Upload" component={Upload}/>
      <BottomTab.Screen name="Notification" component={Notification}/>
      <BottomTab.Screen name="Profile" component={Profile}/>
    </BottomTab.Navigator>
  );
};
...
const MainNavigator = () => {
  return (
    <Drawer.Navigator
      drawerPosition="right"
      drawerType="slide"
      drawerContent={props => <CustomDrawer props={props} />}>
      <Drawer.Screen name="MainTabs" component={MainTabs} />
    </Drawer.Navigator>
  );
};
{% endraw %}
```

その理由はScreenで貰えるnavigationのPropsは直上のNavigationからPropsを貰うためです。上の例題では`MainTab`にある`Profile`画面のnavigation PropsはDrawer NavigationではなくBottom Tab NavigationのPropsになります。したがって、Profile画面は`navigation.openDrawer()`を使うことができないです。

この場合使う物が、`DrawerActions`になります。

Drawer Navigationの直下にはないけど、上のように上部にDrawer Navigationを使ってる場合、下記のようにDrawerを開くことができます。

```js
{% raw %}
...
import {DrawerActions} from '@react-navigation/native';
...
type NavigationProp = StackNavigationProp<ProfileTabParamList, 'Profile'>;
interface Props {
  navigation: NavigationProp;
}

const Profile = ({navigation}: Props) => {
  return (
    <ScrollView>
      ...
      <IconButton
        iconName="menu"
        onPress={() => navigation.dispatch(DrawerActions.openDrawer())}
      />
      ...
    </ScrollView>
  );
});

export default Profile;
{% endraw %}
```

上のように`navigation.dispatch(DrawerActions.openDrawer())`を使ってDrawer Navigationを開くことができます。これ以外にも下記の関数を使えます。

```js
navigation.dispatch(DrawerActions.openDrawer());
navigation.dispatch(DrawerActions.closeDrawer());
navigation.dispatch(DrawerActions.toggleDrawer());
```

{% include in-feed-ads.html %}

### setParams / getParams

react-navigation Vでは下記のように画面間データのやり取りをしました。

```js
...
navigation.setParams({
  showSearch: false,
});
...
const showSearch = navigation.getParam('showSearch');
```

react-navigation V5では`setParams`は使えますが、`getParams`は使えないです。

```js
navigation.setParams({
  showSearch: false,
});
```

react-navigation V5では`getParams`の変わりで`route.params`を使います。

```js
...
import { RouteProp } from '@react-navigation/native';
...

type ProfileScreenRouteProp = RouteProp<MovieNaviParamList, 'MovieDetail'>;
interface Props {
  route: ProfileScreenRouteProp;
}

const MovieDetail = ({ route }: Props) => {
  const { id } = route.params;
  ...
});

export default MovieDetail;
```

typescriptが適用されたからちょっと複雑に見えますが、

```js
const MovieDetail = ({ route, navigation }) => {
  const { id } = route.params;
  ...
});
```

上のようにnavigation Propsと一緒にくるroute Propsを使ってデーターを取得します。

## Typescript

react-navigation v5でtypescriptを使う方法について見てみます。

### navigation

画面を切り替える時、使うnavigation Propsは下記のように使えます。

```js
const Feeds = ({navigation}: Props) => {
  ...
  navigation.navigate('FeedListOnly');
  ...
});
```

この時、Propsは下記のように作成します。

```js
...
import {StackNavigationProp} from '@react-navigation/stack';
...
// Stack Navigation
type NavigationProp = StackNavigationProp<FeedsTabParamList, 'Feeds'>;
interface Props {
  navigation: NavigationProp;
}

const Feeds = ({navigation}: Props) => {
  ...
  navigation.navigate('FeedListOnly');
  ...
});
```

上の例題ではFeedsTabParamListは同じStack Navigationでも使うので、`@types/index.d.ts`ファイル生成して、下記のように修正します。

```js
type FeedsTabParamList = {
  Feeds: undefined;
  FeedListOnly: undefined;
};
```

このStack Navigationは`Feeds`と言う画面と`FeedListOnly`と言う画面を持ってます、画面を切り替える時、特に送るパラメータがないので、`undefined`を入れました。

もし画面を切り替える時、パラメータが必要な場合は、

```js
type FeedsTabParamList = {
  Feeds: undefined;
  FeedListOnly: {
    id: number;
  };
};
```

上のように必要なパラメータを定義して、

```js
const Feeds = ({navigation}: Props) => {
  ...
  navigation.navigate('FeedListOnly', {
    id: 1,
  });
  ...
});
```

上のようにパラメータを送ることができます。このように複雑にしてる理由は送るパラメータのタイプを正確にチェックするためです。

上では、Stack Navigationを紹介しましたが、下記のように各NavigationことにPropsがあります。

```js
import {BottomTabNavigationProp} from '@react-navigation/bottom-tabs';
import {DrawerNavigationProp} from '@react-navigation/drawer';
import {MaterialBottomTabNavigationProp} from '@react-navigation/material-bottom-tabs';
import {MaterialTopTabBarProps} from '@react-navigation/material-top-tabs';
```

使い方はStack Navigationと同じです。

```js
type NavigationProp = BottomTabNavigationProp<FeedsTabParamList, 'Feeds'>;
type NavigationProp = DrawerNavigationProp<FeedsTabParamList, 'Feeds'>;
type NavigationProp = MaterialBottomTabNavigationProp<FeedsTabParamList, 'Feeds'>;
type NavigationProp = MaterialTopTabBarProps<FeedsTabParamList, 'Feeds'>;
```

### route

上で説明しましたが、`navigation.setParams`を使って画面間データのやり取りそすることができます。この時、データを貰う方は`route.params`を使います。

この`route`パラメータを使うためには下記のようにtypescriptを使います。

```js
...
import { RouteProp } from '@react-navigation/native';
...
type ProfileScreenRouteProp = RouteProp<MovieNaviParamList, 'MovieDetail'>;
interface Props {
  route: ProfileScreenRouteProp;
}

const MovieDetail = ({ route }: Props) => {
  const { id } = route.params;
  ...
});

export default MovieDetail;
```

ここでは`MovieNaviParamList`も色んな画面で使うので、`@types/index.d.ts`ファイルを作ってその中に定義してください。

```js
type MovieNaviParamList = {
  MovieHome: undefined;
  MovieDetail: {
    id: number;
  };
};
```

## 完了

これでreact-navigation V5をインストールす方法と使う方法についてみてみました。V4だけずっと使って、V5を初めてみると、結構変わったことがあって、びくりしました。しかし、Reactコンポーネントを使う形になって、もっとReactに親和的な形で開発された感じがします。

既存で使ってる機能たちも全部実装できると思います。一旦react-navigation V4の例題で実装したものはreact-navigation V5の例題でも実装してみたので、react-navigation V5を使ってみようと思う方は下記の例題ソースを参考してください。

- react-navigation-exercise V5: [https://github.com/dev-yakuza/react-navigation-v5-exercise](https://github.com/dev-yakuza/react-navigation-v5-exercise){:rel="nofollow noreferrer" target="_blank" }

## 参考

- 公式サイト: [react-navigation](https://reactnavigation.org/docs){:rel="nofollow noreferrer" target="_blank" }
