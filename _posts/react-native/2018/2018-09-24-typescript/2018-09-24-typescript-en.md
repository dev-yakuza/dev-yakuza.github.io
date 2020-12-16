---
layout: 'post'
permalink: '/react-native/typescript/'
paginate_path: '/react-native/:num/typescript/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'typescript'
description: 'create react-native project and  develop it by applying typescript.'
image: '/assets/images/category/react-native/typescript.jpg'
---

<div id="contents_list" markdown="1">

## Contents

1. [create react-native project](#create-react-native-project)
1. [install required libraries for typescript](#install-required-libraries-for-typescript)
    - [typescript libraries](#typescript-libraries)
1. [typescript configuration](#typescript-configuration)
    - [create tsconfig.json](#create-tsconfigjson)
1. [Make typescript project via React Native CLI](#make-typescript-project-via-react-native-cli)
1. [code with typescript](#code-with-typescript)

</div>

## create react-native project

create RN project with below command.

{% include_cached react-native/create_new_project.md %}

## install required libraries for typescript

install required libraries for applying typescript to the project.

{% include_relative common/install_modules.md %}

### typescript libraries

- typescript: intsall typescript.
- @types/react: intsll react types for typescript.
- @types/react-native: intall RN type for typescript.

## typescript configuration

configure typescript to make react-native work.

### create tsconfig.json

create ```tsconfig.json``` in the project root folder and copy-paste below contents.

{% include_relative common/tsconfig_json.md %}

if you want more detail, see official website.

- [typescript - tsconfig.json](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html){:rel="nofollow noreferrer" target="_blank"}
- [typescript - compile options](https://www.typescriptlang.org/docs/handbook/compiler-options.html){:rel="nofollow noreferrer" target="_blank"}

{% include in-feed-ads.html %}

## Make typescript project via React Native CLI

(0.60.2 version has some bugs.)
If you feel bothered to configure these all settings, you can use React Native CLI to make React Native project based on Typescript to use the command below.

```bash
react-native init SampleProject --template typescript
```

## code with typescript

change App.js filename to App.tsx and code with typescript style.

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
