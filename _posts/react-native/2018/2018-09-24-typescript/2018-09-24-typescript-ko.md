---
layout: 'post'
permalink: '/react-native/typescript/'
paginate_path: '/react-native/:num/typescript/'
lang: 'ko'
categories: 'react-native'
comments: true

title: 'React Native에서 TypeScript 사용하기'
description: 'react-native 프로젝트에 TypeScript를 적용하여 개발해 보자.'
image: '/assets/images/category/react-native/typescript.jpg'
---

<div id="contents_list" markdown="1">

## 목차

- [react-native 프로젝트 생성](#react-native-프로젝트-생성)
- [TypeScript에 필요한 라이브러리 설치](#typescript에-필요한-라이브러리-설치)
  - [TypeScript 라이브러리](#typescript-라이브러리)
- [TypeScript 설정](#typescript-설정)
  - [tsconfig.json 만들기](#tsconfigjson-만들기)
- [React Native CLI로 TypeScript 시작하기](#react-native-cli로-typescript-시작하기)
- [TypeScript로 코딩하기](#typescript로-코딩하기)
- [완료](#완료)

</div>

## react-native 프로젝트 생성

아래에 명령어를 이용하여 RN 프로젝트를 생성합니다.

```bash
react-native init proejct-name
```

## TypeScript에 필요한 라이브러리 설치

TypeScript가 동작할 수 있도록 필요한 라이브러리을 설치합니다.

```bash
npm install typescript @types/react @types/react-native --save-dev
```

### TypeScript 라이브러리

- typescript: TypeScript를 설치한다.
- @types/react: TypeScript에 필요한 react의 type을 설치한다.
- @types/react-native: TypeScript에 필요한 react-native의 type을 설치한다.

{% include in-feed-ads.html %}

## TypeScript 설정

TypeScript를 설정하여 react-native가 동작하도록 만듭니다.

### tsconfig.json 만들기

프로젝트 root 폴더에 ```tsconfig.json```파일을 생성하고 아래에 내용을 복사합니다.

```json
{
  "compilerOptions": {
    "allowJs": true,
    "allowSyntheticDefaultImports": true,
    "esModuleInterop": true,
    "isolatedModules": true,
    "jsx": "react",
    "lib": ["es6", "es2017"],
    "moduleResolution": "node",
    "noEmit": true,
    "strict": true,
    "target": "esnext",
    "skipLibCheck": true
  },
  "exclude": ["node_modules", "babel.config.js", "metro.config.js", "jest.config.js"]
}
```

자세한 내용은 공식 홈페이지를 참조하세요.

- [TypeScript - tsconfig.json](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html){:rel="nofollow noreferrer" target="_blank"}
- [TypeScript - compile options](https://www.typescriptlang.org/docs/handbook/compiler-options.html){:rel="nofollow noreferrer" target="_blank"}

## React Native CLI로 TypeScript 시작하기

이렇게 모든 설정이 귀찮은 경우, 아래에 React Native CLI 명령어를 사용하여 TypeScript를 기반으로하는 React Native 프로젝트를 생성할 수 있습니다.

```bash
npx react-native init SampleProject --template react-native-template-typescript
```

## TypeScript로 코딩하기

App.js를 App.tsx로 파일명을 수정하고 TypeScript 형식으로 코딩합니다.

- Class Component

```js
import React from 'react';
...
interface Props {}
interface State {}
...
export default class App extends React.Component<Props, State> {
```

- Function Component

```js
import React from 'react';
...
interface Props {}
...
const App = ({  }: Props) => {
...
```

## 완료

이것으로 React Native에서 TypeScript를 적용하고 TypeScript를 사용하는 방법에 대해서 알아보았습니다. 이제 React Native 프로젝트에서도 TypeScript를 사용하여 타입 체크를 해 보시기 바랍니다.
