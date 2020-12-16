---
layout: 'post'
permalink: '/react-native/react-navigation/'
paginate_path: '/react-native/:num/react-navigation/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'react-navigation'
description: 'use react-navigation for developing an application.'
image: '/assets/images/category/react-native/react-navigation.jpg'
---

<div id="contents_list" markdown="1">

## Contents

1. [react-navigation V5](#react-native-v5)
1. [create react-native project](#create-react-native-project)
1. [react-navigation installation](#react-navigation-installation)
    - [react-navigation V4](#react-navigation-v4)
        - [react-navigation-stack](#react-navigation-stack)
        - [react-navigation-tabs](#react-navigation-tabs)
        - [react-navigation-drawer](#react-navigation-drawer)
    - [react-navigation v3](#react-navigation-v3)
    - [link react-native-gesture-handler library](#link-react-native-gesture-handler-library)
1. [how to use](#how-to-use)
    - [Navigation to use](#navigation-to-use)
        - [V4](#v4)
        - [V3](#v3)
    - [createAppContainer](#createappcontainer)
    - [createSwitchNavigator](#createswitchnavigator)
    - [createStackNavigator](#createstacknavigator)
    - [createBottomTabNavigator](#createbottomtabnavigator)
    - [switch navigation](#switch-navigation)
1. [hide Navigation bar](#hide-navigation-bar)
1. [reference](#reference)

</div>

## react-navigation V5

I've written a blog post about react-navigation version 5. If you want to know how to use it, see the link below.

- [react-navigation-v5]({{site.url}}/{{page.categories}}/react-navigation-v5/){:target="_blank"}

## create react-native project

this blog uses react-native project which composed typescript and styled-components. if you want to know how to apply typescript and styled-components to RN, see previous blogs.

- [typescript]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}
- [styled-components]({{site.url}}/{{page.categories}}/styled-components/){:target="_blank"}

## react-navigation installation

### react-navigation V4

install react-navigation library via below commands.

```bash
npm install --save react-navigation react-native-gesture-handler react-native-reanimated react-native-screens
```

from react-navigation V4, each navigation is separated other libraries. you need to install the library which you want to use the navigation like below.

#### react-navigation-stack

you can use the navigations via this library.

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

Installation command.

```bash
npm install --save react-navigation-stack
```

#### react-navigation-tabs

you can use the navigations via this library.

- createBottomTabNavigator
- createMaterialTopTabNavigator
- BottomTabBar
- MaterialTopTabBar

Installation command.

```bash
npm install --save react-navigation-tabs
```

#### react-navigation-drawer

you can use the navigations via this library.

- createDrawerNavigator
- DrawerGestureContext
- DrawerRouter
- DrawerActions
- DrawerView
- DrawerNavigatorItems
- DrawerSidebar

Installation command.

```bash
npm install --save react-navigation-drawer
```

after installation, you should connect native modules to execute the command below.

```bash
cd ios
pod install
cd ...
```

{% include in-feed-ads.html %}

### react-navigation v3

install react-navigation library via below commands.

```bash
npm install --save react-navigation react-native-gesture-handler
npm install --save-dev @types/react-navigation
```

### link react-native-gesture-handler library

execute below command to link ```react-native-gesture-handler``` library to RN(react-native) project.

```bash
react-native link react-native-gesture-handler
```

## how to use

there are many ways to use react-navigation at the official site. if you want to know details, please check below link.

- official site: [https://reactnavigation.org/docs](https://reactnavigation.org/docs){:rel="nofollow noreferrer" target="_blank" }

we've made the repository about basic usage by following official site. before using ```react-navigation```, if you see this repository, it will help when you get the basic structure.

- react-navigation-exercise V4: [https://github.com/dev-yakuza/react-navigation-v4-exercise](https://github.com/dev-yakuza/react-navigation-v4-exercise){:rel="nofollow noreferrer" target="_blank" }
- react-navigation-exercise V3: [https://github.com/dev-yakuza/react-navigation-exercise](https://github.com/dev-yakuza/react-navigation-exercise){:rel="nofollow noreferrer" target="_blank" }

{% include in-feed-ads.html %}

### Navigation to use

import Navigation to use.

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

to use ```react-navigation``` in App, we should use ```createAppContainer``` to Top navigation.

### createSwitchNavigator

if App has Login feature, we recommend to use ```createSwitchNavigator```.  our Repository uses Switch Navigation to basic navigation.

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

this ```createStackNavigator``` is the navigator to stack a view to another view. we use this navigation to show full screen view on tab navigation and display another view in tab nabigation.

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

we use this ```createBottomTabNavigator``` to show tab navigation on the bottom of the screen.

```js
const MainTab = createBottomTabNavigator({
  FirstTabStack,
  SecondTab,
  ThirdTab,
});
```

### switch navigation

we use below code to switch a view to another view.

```js
this.props.navigation.navigate('MainTab');
```

## hide Navigation bar

you can hide navigation bar with below code

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

- static navigationOptions: you can set navigation options via this variable.
- { header: null }: hide navigation header bar.

## reference

- official site: [react-navigation](https://reactnavigation.org/docs){:rel="nofollow noreferrer" target="_blank" }
