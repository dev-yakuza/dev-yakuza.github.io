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


## create react-native project
this blog uses react-native project which composed typescript and styled-components. if you want to know how to apply typescript and styled-components to RN, see previous blogs.

- [typescript]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}
- [styled-components]({{site.url}}/{{page.categories}}/styled-components/){:target="_blank"}

## react-navigation installation
install react-navigation library via below commands.

```bash
npm install --save react-navigation
npm install --save react-native-gesture-handler
```

## link react-native-gesture-handler library
execute below command to link ```react-native-gesture-handler``` library to RN(react-native) project.

```bash
react-native link react-native-gesture-handler
```

## how to use
there are many ways to use react-navigation at the official site. if you want to know details, please check below link.

- official site: [https://reactnavigation.org/docs](https://reactnavigation.org/docs){:rel="nofollow noreferrer" target="_blank" }

we've made the repository about basic usage by following official site. before using ```react-navigation```, if you see this repository, it will help when you get the basic structure.

- react-navigation-exercise: [https://github.com/dev-yakuza/react-navigation-exercise](https://github.com/dev-yakuza/react-navigation-exercise){:rel="nofollow noreferrer" target="_blank" }

### Navigation to use
import Navigation to use.

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