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

{% include_relative common/installation.md %}

- react-navigation: this is react-navigation library.
- @types/react-navigation: this is react-navigation type for typescript.

## how to use
there are many ways to use react-navigation at the official site. we will add how to use react-navigation which we really apply our project.

- official site: [react-navigation](https://reactnavigation.org/docs){:rel="nofollow noreferrer" target="_blank" }

### stack navigation
this is how to use basic stack navigation.

{% include_relative common/stack-navigation.md %}

- set screens which you want to use and default screen in ```Navigator.tsx```
- screens created by ```createStackNavigator``` basically have navigation variable in props.
- use ```this.props.navigation.navigate``` for switching screens.
- use ```this.props.navigation.goBack``` for going to the previous screen.

## hide Navigation bar
you can hide navigation bar with below code

{% include_relative common/hide-navigation-bar.md %}

- static navigationOptions: you can set navigation options via this variable.
- { header: null }: hide navigation header bar.

## reference
- official site: [react-navigation](https://reactnavigation.org/docs){:rel="nofollow noreferrer" target="_blank" }