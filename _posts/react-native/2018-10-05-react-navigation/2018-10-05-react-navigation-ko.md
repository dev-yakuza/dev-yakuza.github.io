---
layout: 'post'
permalink: '/react-native/react-navigation/'
paginate_path: '/react-native/:num/react-navigation/'
lang: 'ko'
categories: 'react-native'
comments: true

title: 'react-navigation'
description: 'react-navigation을 활용하여 어플을 개발해 보자.'
image: '/assets/images/category/react-native/react-navigation.jpg'
---


## react-native 프로젝트 생성
typescript와 styled-components를 적용한 프로젝트에서 진행합니다. RN에 typescript와 styled-components를 적용하는 방법은 이전 블로그를 참고하세요.
- [typescript]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}
- [styled-components]({{site.url}}/{{page.categories}}/styled-components/){:target="_blank"}

## react-navigation 설치
react-navigation 라이브러리를 아래에 명령어를 통해 설치합니다.

{% include_relative common/installation.md %}

- react-navigation: react-navigation 라이브러리입니다.
- @types/react-navigation: typescript에 필요한 react-navigation의 타입입니다.

## 사용법
react-navigation를 사용하는 여러가지 방법들이 공식 홈페이지에 자세히 나와있습니다. 우리는 실제로 프로젝트를 진행하면서 사용한 내용을 조금씩 추가해 나갈 예정입니다.
- 공식 홈페이지: [react-navigation](https://reactnavigation.org/docs){:rel="nofollow noreferrer" target="_blank" }

### stack navigation
기본적인 스택 네비게이션을 사용하는 방법입니다.

{% include_relative common/stack-navigation.md %}

- ```Navigator.tsx```에 사용할 화면과 기본 화면을 설정합니다.
- ```createStackNavigator```으로 생성된 화면은 기본적으로 props에 navigation을 가지고 있습니다.
- ```this.props.navigation.navigate```를 사용하여 화면 전환을 합니다.
- ```this.props.navigation.goBack```을 이용하여 이전 페이지로 돌아갑니다.

## Navigation bar 숨기기
아래에 코드로 navigation bar를 숨길 수 있습니다.

{% include_relative common/hide-navigation-bar.md %}

- static navigationOptions: 네비게이션의 옵션을 설정합니다.
- { header: null }: navigation header bar를 비활성화합니다.

## 참고
- 공식 홈페이지: [react-navigation](https://reactnavigation.org/docs){:rel="nofollow noreferrer" target="_blank" }