---
layout: 'post'
permalink: '/react-native/typescript/'
paginate_path: '/react-native/:num/typescript/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'How to use TypeScript in React Native'
description: Let's see how to configure TypeScript and how to use TypeScript in React Native.
image: '/assets/images/category/react-native/typescript.jpg'
---

<div id="contents_list" markdown="1">

## Contents

- [create react-native project](#create-react-native-project)
- [install required libraries for TypeScript](#install-required-libraries-for-typescript)
  - [TypeScript libraries](#typescript-libraries)
- [TypeScript configuration](#typescript-configuration)
  - [create tsconfig.json](#create-tsconfigjson)
- [Make TypeScript project via React Native CLI](#make-typescript-project-via-react-native-cli)
- [code with TypeScript](#code-with-typescript)
- [Completed](#completed)

</div>

## create react-native project

create React Native project with below command.

```bash
npm install typescript @types/react @types/react-native --save-dev
```

## install required libraries for TypeScript

install required libraries for applying TypeScript to the project.

```bash
react-native init proejct-name
```

### TypeScript libraries

- typescript: intsall TypeScript.
- @types/react: intsll react types for TypeScript.
- @types/react-native: intall RN type for TypeScript.

## TypeScript configuration

configure TypeScript to make react-native work.

### create tsconfig.json

create ```tsconfig.json``` in the project root folder and copy-paste below contents.

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

if you want more detail, see official website.

- [TypeScript - tsconfig.json](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html){:rel="nofollow noreferrer" target="_blank"}
- [TypeScript - compile options](https://www.typescriptlang.org/docs/handbook/compiler-options.html){:rel="nofollow noreferrer" target="_blank"}

{% include in-feed-ads.html %}

## Make TypeScript project via React Native CLI

If you feel bothered to configure these all settings, you can use React Native CLI to make React Native project based on TypeScript to use the command below.

```bash
npx react-native init SampleProject --template react-native-template-typescript
```

## code with TypeScript

change App.js filename to App.tsx and code with TypeScript style.

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

## Completed

Done! we've seen how to apply TypeScript to React Native, and how to use TypeScript in React Native. Form now, let's use TypeScript in React Native to check the types!
