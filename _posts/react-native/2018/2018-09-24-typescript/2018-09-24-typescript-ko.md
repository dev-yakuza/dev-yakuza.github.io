---
layout: 'post'
permalink: '/react-native/typescript/'
paginate_path: '/react-native/:num/typescript/'
lang: 'ko'
categories: 'react-native'
comments: true

title: 'typescript'
description: 'react-native 프로젝트에 typescript를 적용하여 개발해 보자.'
image: '/assets/images/category/react-native/typescript.jpg'
---

<div id="contents_list" markdown="1">

## 목차

1. [react-native 프로젝트 생성](#react-native-프로젝트-생성)
1. [typescript에 필요한 라이브러리 설치](#typescript에-필요한-라이브러리-설치)
    - [typescript 라이브러리](#typescript-라이브러리)
1. [typescript 설정](#typescript-설정)
    - [tsconfig.json 만들기](#tsconfigjson-만들기)
1. [React Native CLI로 Typescript 시작하기](#react-native-cli로-typescript-시작하기)
1. [typescript로 코딩하기](#typescript로-코딩하기)

</div>


## react-native 프로젝트 생성

아래에 명령어를 이용하여 RN 프로젝트를 생성합니다.

{% include_cached react-native/create_new_project.md %}

## typescript에 필요한 라이브러리 설치

typescript가 동작할 수 있도록 필요한 라이브러리을 설치합니다.

{% include_relative common/install_modules.md %}

### typescript 라이브러리

- typescript: typescript를 설치한다.
- @types/react: typescript에 필요한 react의 type을 설치한다.
- @types/react-native: typescript에 필요한 react-native의 type을 설치한다.

{% include in-feed-ads.html %}

## typescript 설정

typescript를 설정하여 react-native가 동작하도록 만듭니다.

### tsconfig.json 만들기

프로젝트 root 폴더에 ```tsconfig.json```파일을 생성하고 아래에 내용을 복사합니다.

{% include_relative common/tsconfig_json.md %}

자세한 내용은 공식 홈페이지를 참조하세요.

- [typescript - tsconfig.json](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html){:rel="nofollow noreferrer" target="_blank"}
- [typescript - compile options](https://www.typescriptlang.org/docs/handbook/compiler-options.html){:rel="nofollow noreferrer" target="_blank"}

## React Native CLI로 Typescript 시작하기

(0.60.2에 버그가 있는거 같습니다.)
이렇 모든 설정이 귀찮은 경우, 아래에 React Native CLI 명령어를 사용하여 Typescript를 기반으로하는 React Native 프로젝트를 생성할 수 있습니다.

```bash
react-native init SampleProject --template typescript
```

## typescript로 코딩하기

App.js를 App.tsx로 파일명을 수정하고 typescript 형식으로 코딩합니다.

- Class Component

```js
import React from 'react';
...
interface Props {}
interface State {}
...
export default class App extends React.Component<Props, State> {
```

- Functional Component

```js
import React from 'react';
...
interface Props {}
...
const App = ({  }: Props) => {
...
```
