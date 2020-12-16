---
layout: 'post'
permalink: '/react-native/react-navigation-v5/'
paginate_path: '/react-native/:num/react-navigation-v5/'
lang: 'ko'
categories: 'react-native'
comments: true

title: 'react-navigation V5'
description: 'react-navigation V5를 설치하고 사용하는 방법에 대해서 공유합니다.'
image: '/assets/images/category/react-native/2018/react-navigation-v5/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [react-native 프로젝트 생성](#react-native-프로젝트-생성)
- [react-navigation V5 설치](#react-navigation-v5-설치)
- [추가로 필요한 Navigation 설치](#추가로-필요한-navigation-설치)
  - [Stack Navigation](#stack-navigation)
  - [Drawer Navigation](#drawer-navigation)
  - [Bottom Tab Navigation](#bottom-tab-navigation)
  - [Material Bottom Tab Navigation](#material-bottom-tab-navigation)
  - [Material Top Tab Navigation](#material-top-tab-navigation)
- [사용법](#사용법)
  - [react-native-gesture-handler](#react-native-gesture-handler)
  - [NavigationContainer](#navigationcontainer)
  - [Auth 처리](#auth-처리)
  - [Stack Navigation 사용법](#stack-navigation-사용법)
  - [Drawer Navigation 사용법](#drawer-navigation-사용법)
  - [Bottom Tab Navigation 사용법](#bottom-tab-navigation-사용법)
  - [Material Bottom Tab Navigation 사용법](#material-bottom-tab-navigation-사용법)
  - [Material Top Tab Navigation 사용법](#material-top-tab-navigation-사용법)
  - [Drawer Open](#drawer-open)
  - [DrawerActions](#draweractions)
  - [setParams / getParams](#setparams--getparams)
- [Typescript](#typescript)
  - [navigation](#navigation)
  - [route](#route)
- [완료](#완료)
- [참고](#참고)

</div>

## 개요

react-navigation의 버전 V5는 정말 많은 것이 바뀌었네요. V3과 V4는 그래도 조금 비슷한 느낌이 있었는데, V5는 전혀 다른 Navigation이라는 느낌입니다. 그래서 이렇게 react-navigation V5에 관한 블로그 포스트를 작성하게 되었네요.

이전 버전(V3, V4)에 관해서 궁금하신 분들은 이전 블로그 포스트를 참고하시기 바랍니다.

- [react-navigation]({{site.url}}/{{page.categories}}/react-navigation/){:target="_blank"}

react-navigation의 V5에 관한 공식 사이트는 아래와 같습니다.

- 공식 홈페이지: [https://reactnavigation.org](https://reactnavigation.org){:rel="nofollow noreferrer" target="_blank" }

이번 블로그 포스트에서는 react-navigation V5를 사용하는 방법에 대해서 알아봅니다.

## react-native 프로젝트 생성

여기서 소개하는 소스코드는 typescript와 styled-components가 적용되었습니다. React Native에 typescript와 styled-components를 적용하는 방법은 이전 블로그를 참고하세요.

- [typescript]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}
- [styled-components]({{site.url}}/{{page.categories}}/styled-components/){:target="_blank"}
- [root-import]({{site.url}}/{{page.categories}}/root-import/){:target="_blank"}

{% include in-feed-ads.html %}

## react-navigation V5 설치

react-navigation v5 라이브러리를 아래에 명령어를 통해 설치합니다.

```bash
npm install --save @react-navigation/native
```

또한 react-navigation v5를 사용하기 위한 라이브러리들을 아래에 명령어로 설치합니다.

```bash
npm install --save react-native-reanimated react-native-gesture-handler react-native-screens react-native-safe-area-context @react-native-community/masked-view
```

설치가 완료되면 iOS 폴더에 가서 아래에 명령어를 실행합니다.

```bash
# cd ios
pod install
```

## 추가로 필요한 Navigation 설치

react-navigation V4부터 Navigation을 사용하기 위해서는, 필요한 Navigation을 따로따로 설치해야합니다. V5도 역시 필요한 Navigation을 사용하기 위해서는 추가적으로 Navigation 라이브러리를 설치해야 합니다.

### Stack Navigation

한 화면 위에, 다른 화면을 쌓아 올리듯 화면 전환을 하는 Navigation을 Stack Navigation이라고 합니다.

<div class="half_image_container">
  <img class="half_image" src="/assets/images/category/react-native/2018/react-navigation-v5/stack.gif" alt="React Navigation V5 Stack Navigation">
</div>
[그림: [reactnavigation.org 공식 홈페이지](https://reactnavigation.org/docs/stack-navigator){:rel="nofollow noreferrer" target="_blank" }]

Stack Navigation을 사용하기 위해서는 아래와 같은 명령어로 추가 라이브러리를 설치해야 합니다.

```bash
npm install --save @react-navigation/stack
```

### Drawer Navigation

주로 메뉴에 사용되는 Navigation으로 사용자의 Swipe 액션에 반응하여 화면에 표시되는 Navigation입니다.

<div class="half_image_container">
  <img class="half_image" src="/assets/images/category/react-native/2018/react-navigation-v5/drawer.gif" alt="React Navigation V5 drawer Navigation">
</div>
[그림: [reactnavigation.org 공식 홈페이지](https://reactnavigation.org/docs/drawer-navigator){:rel="nofollow noreferrer" target="_blank" }]

Drawer Navigation을 사용하기 위해서는 아래와 같은 명령어로 추가 라이브러리를 설치해야 합니다.

```bash
npm install --save @react-navigation/drawer
```

### Bottom Tab Navigation

화면 하단에서 Tab으로 화면을 전환하는 Navigation입니다.

<div class="half_image_container">
  <img class="half_image" src="/assets/images/category/react-native/2018/react-navigation-v5/bottom-tabs-demo.gif" alt="React Navigation V5 bottom-tabs-demo Navigation">
</div>
[그림: [reactnavigation.org 공식 홈페이지](https://reactnavigation.org/docs/bottom-tab-navigator){:rel="nofollow noreferrer" target="_blank" }]

Bottom Tab Navigation을 사용하기 위해서는 아래와 같은 명령어로 추가 라이브러리를 설치해야 합니다.

```bash
npm install --save @react-navigation/bottom-tabs
```

{% include in-feed-ads.html %}

### Material Bottom Tab Navigation

Bottom Tab Navigation과 동일하게 화면 하단에서 Tab으로 화면을 전환하는 Navigation입니다. 여기에 Google의 Material 디자인이 적용된 Navigation 입니다.

<div class="half_image_container">
  <img class="half_image" src="/assets/images/category/react-native/2018/react-navigation-v5/material-bottom-tabs.gif" alt="React Navigation V5 Material Bottom Tab Navigation">
</div>
[그림: [reactnavigation.org 공식 홈페이지](https://reactnavigation.org/docs/material-bottom-tab-navigator){:rel="nofollow noreferrer" target="_blank" }]

Material Bottom Tab Navigation을 사용하기 위해서는 아래와 같은 명령어로 추가 라이브러리를 설치해야 합니다.

```bash
npm install --save @react-navigation/material-bottom-tabs react-native-paper
```

이 Navigation은 `react-native-vector-icons`라는 라이브러리가 추가적으로 필요합니다. react-native-vector-icons를 설치하는 방법에 대해서는 아래에 링크를 참고하시기 바랍니다.

- [react-native-vector-icons]({{site.url}}/{{page.categories}}/react-native-vector-icons/){:target="_blank"}

### Material Top Tab Navigation

Google의 Material 디자인이 적용된 Navigation으로써, 화면 상단에서 Tab으로 화면을 전환하는 Navigation입니다.

<div class="half_image_container">
  <img class="half_image" src="/assets/images/category/react-native/2018/react-navigation-v5/material-top-tabs.gif" alt="React Navigation V5 material-top-tabs Navigation">
</div>
[그림: [reactnavigation.org 공식 홈페이지](https://reactnavigation.org/docs/material-top-tab-navigator){:rel="nofollow noreferrer" target="_blank" }]

Material Top Tab Navigation을 사용하기 위해서는 아래와 같은 명령어로 추가 라이브러리를 설치해야 합니다.

```bash
npm install --save @react-navigation/material-top-tabs react-native-tab-view
```

## 사용법

react-navigation를 사용하는 여러가지 방법들이 공식 홈페이지에 자세히 나와있습니다. 자세한 내용은 링크를 참고해주세요.

- 공식 홈페이지: [https://reactnavigation.org/docs](https://reactnavigation.org/docs){:rel="nofollow noreferrer" target="_blank" }

이 블로그에서는 공식 홈페이지를 참고하여 기본적인 사용법을 정리한 저장소(Repository)를 만들었습니다. `react-navigation`을 사용하기 전에 이 저장소(Repository)를 확인한다면 기본적인 구조를 잡을 때, 도움이 될거 같습니다.

- react-navigation-exercise V5: [https://github.com/dev-yakuza/react-navigation-v5-exercise](https://github.com/dev-yakuza/react-navigation-v5-exercise){:rel="nofollow noreferrer" target="_blank" }

이 저장소(Repository)에 구현된 내용을 설명하도록 하겠습니다.

{% include in-feed-ads.html %}

### react-native-gesture-handler

react-navigation을 사용하기 위해서는 `react-native-gesture-handler`를 import할 필요가 있습니다. `index.js` 파일 또는 `App.js` 파일(react-navigation을 사용하는 컴포넌트의 최상위 컴포넌트)을 아래와 같이 수정합니다.

```js
import 'react-native-gesture-handler';
...
```

### NavigationContainer

V4에서 Navigation을 사용하기 위해서는 `createAppContainer`을 마지막에 사용해야 했습니다.

```js
{% raw %}
import {createAppContainer} from 'react-navigation';
...
export default createAppContainer(
  ...
);
{% endraw %}
```

V5에서는 V4와 비슷하게 마지막에는 `NavigationContainer`라는 컴포넌트를 제공할 필요가 있습니다.

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

벌써부터 차이점이 느껴지시나요? 기존의 react-navigation은 설정을 하는 느낌이였다면, V5는 React의 컴포넌트를 사용하는 느낌입니다.

### Auth 처리

V4에서는 Auth 부분을 처리하기 위해 `createSwitchNavigator`라는 Navigation을 별도로 제공하였습니다.

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

createSwitchNavigator는 위와 같이 사용이 가능한데, AuthLoading이라는 React 컴포넌트에서 로그인 여부를 확인하고, 로그인이 되지 않은 경우 Auth 화면으로, 로그인을 했다면, MainNavi로 화면을 전환하였습니다.

V5에서는 `createSwitchNavigator`가 없어졌습니다. 위와 같은 Auth 처리를 구현하기 위해서는 아래와 같이 react-navigation을 사용할 필요가 있습니다.

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

V5에서는 createSwitchNavigator가 없습니다. 그대신 V4와 다르게 React 컴포넌트 형식이므로, Navigation안에서 직접 로그인 여부를 판단하고 화면에 표시할 Navigation을 결정하게 됩니다.
공식 홈페이지에서도 위와 같은 방법을 안내하고 있으니 참고해 보시기 바랍니다.

- 공식 홈페이지: [react-navigation - Auth flow](https://reactnavigation.org/docs/auth-flow){:rel="nofollow noreferrer" target="_blank" }

### Stack Navigation 사용법

react-navigation V4에서는 아래와 같이 Stack Navigation을 사용하였습니다.

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

react-navigation V5에서는 아래와 같이 Stack Navigation을 사용합니다.

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

react-navigation V5에서 Stack Navigation 전체에 공통적으로 속성을 적용하고 싶으면 `Stack.Navigator`의 `screenOptions`을 사용합니다.

반대로, 각 화면에만 속성을 적용하고 싶으면 `Stack.Screen`의 `options`를 사용합니다.

위에 예제에서는 자주 사용하는 Header Bar를 숨기기 위해 `options`의 `headerShown`을 사용하였습니다.

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

또한 뒤로 돌아가는 버튼의 타이틀을 숨기기 위해 `options`의 `headerBackTitleVisible`도 사용해 보았습니다.

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

### Drawer Navigation 사용법

react-navigation V5에서는 아래와 같이 Drawer Navigation을 사용합니다.

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

여기에서는 `Logout` 기능을 구현하기 위해 조금 복잡해졌습니다. Logout 기능을 빼고 보면 아래와 같습니다.

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

Stack Navigation과 굉장히 비슷합니다. 위에 예제에서는 여기에 `Logout`이라는 항목을 추가로 표시하고 Logout 항목을 선택하면 Logout되도록 추가하면서 좀 복잡한 형태를 가지게 되었습니다.

### Bottom Tab Navigation 사용법

react-navigation V5에서는 Bottom Tab Navigation은 아래와 같이 사용합니다.

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

위에 예제에서는 Tab의 Label과 Icon을 각각 표시하기 위해 `Tab.Screen`의 `options`를 사용하였습니다.

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

### Material Bottom Tab Navigation 사용법

react-navigation V5에서 Material Bottom Tab Navigation은 아래와 같이 사용합니다.

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

Material Bottom Tab Navigation를 사용할 때는 Tab Bar에 Icon을 설정해야 합니다.

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

또한 각 탭을 선택할 때마다, 색상을 변경하고 싶다면, `tabBarColor`를 설정하면 됩니다.

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

tabBarIcon은 필수적으로 추가해야하지만, tabBarColor는 필요한 상황에서만 사용하시면 됩니다.

### Material Top Tab Navigation 사용법

react-navigation V5에서 Material Top Tab Navigation은 아래와 같이 사용합니다.

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

Material Top Tab Navigation은 아래와 같이 간단하게 선언하여 사용할 수 있습니다.

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

하지만, `Notch Design`에서는 Navigation이 제대로 보이지 않습니다.

![notch design에서 material top navigation의 문제점](/assets/images/category/react-native/2018/react-navigation-v5/notch-design-material-top-navigation-problem.jpg)

이 문제를 해결하기 위해, Stack Navigation으로 감싸서 제공하기를 권장합니다.

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

Stack Navigation으로 감싸서 제공하면 아래와 같은 화면을 볼 수 있습니다.

![notch design에서 material top navigation의 문제점 해결](/assets/images/category/react-native/2018/react-navigation-v5/solution-notch-design-material-top-navigation-problem.jpg)

{% include in-feed-ads.html %}

### Drawer Open

보통 Drawer Navigation만 사용하면 아래와 같은 화면을 볼 수 있습니다.

<div class="half_image_container">
  <img class="half_image" src="/assets/images/category/react-native/2018/react-navigation-v5/drawer.gif" alt="React Navigation V5 drawer Navigation">
</div>
[그림: [reactnavigation.org 공식 홈페이지](https://reactnavigation.org/docs/drawer-navigator){:rel="nofollow noreferrer" target="_blank" }]

위와 같이 왼쪽에서 오른쪽으로 Swipe를 해야 Drawer Navigation을 확인할 수 있습니다.

하지만 보통, Navigation의 Header에 메뉴 아이콘을 표시하고, 메뉴를 선택하면 Drawer Navigation을 표시하도록 만듭니다.

이렇게 하기 위해서는 Stack Navigation으로 Navigation Header를 표시하고, Header의 왼쪽에 메뉴 아이콘을 표시한 후, 메뉴 아이콘을 선택하면 `openDrawer`라는 함수를 사용하여 Drawer Navigation을 열도록 구현해야 합니다.

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

위에 예제처럼 Drawer Navigation에 직접 연결된 화면에서는 navigation의 Props를 사용하여 Drawer를 열고 닫을 수 있습니다.
하지만 아래와 같이 Drawer Navigation에 직접 연결되지 않은 경우에는 navigation의 Props를 사용하여 Drawer를 열고 닫을 수 없습니다.

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

그 이유는 Screen에서 받는 navigation의 Props는 바로 상위에 있는 Navigation에서 Props를 전달 받기 때문입니다. 위에 예제에서 `MainTab`에 있는 `Profile` 화면의 navigation Props는 Drawer Navigation이 아닌 Bottom Tab Navigation의 Props가 됩니다. 따라서 Profile 화면에서는 `navigation.openDrawer()`를 사용할 수 없습니다.

이와 같은 경우 사용하는 것이 `DrawerActions`입니다.

Drawer Navigation의 바로 하단에 있지는 않지만, 위와 같이 상단에 Drawer Navigation을 사용할 때, 아래와 같이 Drawer를 열고 닫을 수 있습니다.

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

위와 같이 `navigation.dispatch(DrawerActions.openDrawer())`을 사용하여 Drawer Navigation을 열 수 있습니다. 그 외에도 아래와 같은 함수를 지원합니다.

```js
navigation.dispatch(DrawerActions.openDrawer());
navigation.dispatch(DrawerActions.closeDrawer());
navigation.dispatch(DrawerActions.toggleDrawer());
```

{% include in-feed-ads.html %}

### setParams / getParams

react-navigation V4에서는 아래와 같이 화면간 데이터를 주고 받을 수 있었습니다.

```js
...
navigation.setParams({
  showSearch: false,
});
...
const showSearch = navigation.getParam('showSearch');
```

react-navigation V5에서는 `setParams`는 사용할 수 있지만, `getParams`는 사용할 수 없습니다.

```js
navigation.setParams({
  showSearch: false,
});
```

react-navigation V5에서는 `getParams` 대신 `route.params`을 사용하게 됩니다.

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

typescript가 적용이 되어 조금 복잡해 보이지만,

```js
const MovieDetail = ({ route, navigation }) => {
  const { id } = route.params;
  ...
});
```

위와 같이 navigation Props와 함께 오는 route Props를 사용하여 데이터를 습득하게 됩니다.

## Typescript

react-navigation v5에서 typescript를 사용하는 방법에 대해서 알아봅니다.

### navigation

화면을 전환하기 위해서는 navigation Props를 아래와 같이 사용하게 됩니다.

```js
const Feeds = ({navigation}: Props) => {
  ...
  navigation.navigate('FeedListOnly');
  ...
});
```

이 때, Props는 아래와 같이 작성합니다.

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

위에 예제에서 FeedsTabParamList는 같은 Stack Navigation에서도 사용하게 되므로 `@types/index.d.ts` 파일을 생성하고 아래와 같이 선언합니다.

```js
type FeedsTabParamList = {
  Feeds: undefined;
  FeedListOnly: undefined;
};
```

이 Stack Navigation은 `Feeds`라는 화면과 `FeedListOnly`라는 화면을 가지고 있으며, 화면을 전환할 때, 특별히 전달할 파라메터가 없으므로 `undefined`를 대입하였습니다.

만약 화면 전환시 파라메터가 필요한 경우,

```js
type FeedsTabParamList = {
  Feeds: undefined;
  FeedListOnly: {
    id: number;
  };
};
```

위와 같이 필요한 파라메터를 정의한 후,

```js
const Feeds = ({navigation}: Props) => {
  ...
  navigation.navigate('FeedListOnly', {
    id: 1,
  });
  ...
});
```

위와 같이 파라메터를 전달할 수 있습니다. 이렇게 복잡하게 하는 이유는 전달하는 파라메터의 타입을 정확하게 체크하기 위해서입니다.

위에서는 Stack Navigation을 소개하였지만 아래와 같이 각 Navigation별로 Props를 사용할 수 있습니다.

```js
import {BottomTabNavigationProp} from '@react-navigation/bottom-tabs';
import {DrawerNavigationProp} from '@react-navigation/drawer';
import {MaterialBottomTabNavigationProp} from '@react-navigation/material-bottom-tabs';
import {MaterialTopTabBarProps} from '@react-navigation/material-top-tabs';
```

사용법은 Stack Navigation과 동일합니다.

```js
type NavigationProp = BottomTabNavigationProp<FeedsTabParamList, 'Feeds'>;
type NavigationProp = DrawerNavigationProp<FeedsTabParamList, 'Feeds'>;
type NavigationProp = MaterialBottomTabNavigationProp<FeedsTabParamList, 'Feeds'>;
type NavigationProp = MaterialTopTabBarProps<FeedsTabParamList, 'Feeds'>;
```

### route

위에서 설명하였지만 `navigation.setParams`를 활용하여 화면간 데이터를 주고 받을 수 있습니다. 이때, 데이터를 받는 쪽에서는 `route.params`를 사용하게 됩니다.

이 `route` 파라메터를 사용하기 위해서는 아래와 같이 typescript를 사용합니다.

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

여기서 `MovieNaviParamList`도 여러 화면에서 사용되기 때문에 별도의 `@types/index.d.ts` 파일을 만들고 작성합니다.

```js
type MovieNaviParamList = {
  MovieHome: undefined;
  MovieDetail: {
    id: number;
  };
};
```

## 완료

이것으로 react-navigation V5를 설치하는 방법과 사용하는 방법에 대해서 알아보았습니다. V4만 사용하다가 V5를 보니, 많이 달라진 점때문에 놀랐습니다. 하지만 React 컴포넌트를 사용하는 형태로 변경되면서, 좀 더 React에 친화적인 형태로 개발이 된거 같다고 느꼈습니다.

기존에 사용하던 기능들이 모두 구현 가능하다고 생각합니다. 일단 react-navigation V4 예제에서 구현한 모든 내용을 react-navigation V5에서도 구현해 보았습니다. react-navigation V5를 사용하고자 하시는 분들은 아래에 예제 소스를 꼭 참고해 보시기 바랍니다.

- react-navigation-exercise V5: [https://github.com/dev-yakuza/react-navigation-v5-exercise](https://github.com/dev-yakuza/react-navigation-v5-exercise){:rel="nofollow noreferrer" target="_blank" }

## 참고

- 공식 홈페이지: [react-navigation](https://reactnavigation.org/docs){:rel="nofollow noreferrer" target="_blank" }
