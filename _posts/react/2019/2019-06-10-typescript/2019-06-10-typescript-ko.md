---
layout: 'post'
permalink: '/react/typescript/'
paginate_path: '/react/:num/typescript/'
lang: 'ko'
categories: 'react'
comments: true

title: 'React에서 Typescript 사용하기'
description: 'React(리액트)에서 Typescript(타입스크립트)를 사용하기 위한 방법에 대해서 알아보고, 간단하게 React(리액트) 프로젝트에 Typescript(타입스크립트)를 적용해 보겠습니다.'
image: '/assets/images/category/react/2019/typescript/background.jpg'
---

## 개요
회사에서 React(리액트)로 새로운 프로젝트를 진행하게 되었습니다. 그래서 오랜만에 처음부터 세팅할 기회가 생겨 정리하게 되었습니다. 이번 블로그 포스트에서는 React(리액트)에서 Typescript(타입스크립트)를 사용하기 위한 방법에 대해서 살펴보고, React(리액트) 프로젝트에서 Typescript(타입스크립트)를 사용해 보겠습니다.

이 블로그에서 다루는 소스코드는 깃헙(Github)에서 확인할 수 있습니다.

- Github: [https://github.com/dev-yakuza/react_typescript](https://github.com/dev-yakuza/react_typescript){:target="_blank"}

React(리액트) 프로젝트를 시작하기 위한 Webpack(웹팩) 설정은 이전 블로그를 참고하시기 바랍니다.

- 이전 블로그: [Webpack으로 React 시작하기]({{site.url}}/{{page.categories}}/start/){:target="_blank"}

## 프로젝트 준비
이 블로그 포스트에서 사용할 기본 React(리액트) 프로젝트는 이전 블로그에서 소개한 Webpack(웹팩) 기반 프로젝트입니다. 자세한 내용은 이전 블로그 포스트를 확인해 주시기 바랍니다.

- 이전 블로그: [Webpack으로 React 시작하기]({{site.url}}/{{page.categories}}/start/){:target="_blank"}

이전 블로그를 통해 프로젝트를 생성하면 아래와 같은 구조를 가지고 있습니다. 우리는 react_start라는 이름 대신 react_typescript라는 이름으로 프로젝트를 생성했습니다.

```bash
|-- src
|   |-- index.html
|   |-- App.jsx
|-- .babelrc
|-- package.json
|-- webpack.config.js
```

## 설치
아래에 명령어로 React(리액트)에 Typescript(타입스크립트)를 적용하기 위해 필요한 라이브러리들을 설치합니다.

```bash
npm install --save-dev typescript @babel/preset-typescript ts-loader fork-ts-checker-webpack-plugin tslint tslint-react
```

- typescript: Typescript(타입스크립트)를 사용합니다.
- @babel/preset-typescript: babel(바벨)에서 Typescript(타입스크립트)를 빌드하기 위한 라이브러리입니다.
- ts-loader: Webpack(웹팩)에서 Typescript(타입스크립트)를 컴파일 하기 위해 필요한 라이브러리입니다.
- fork-ts-checker-webpack-plugin: ts-loader의 성능을 향상시키기 위한 라이브러리입니다.
- tslint, tslint-react: 코딩 컨벤션을 체크하기 위한 라이브러리입니다.

{% include in-feed-ads.html %}

## Webpack 설정
React(리액트)에서 Typescript(타입스크립트)를 사용하기 위해 `webpack.config.js`를 열고 아래와 같이 Webpack(웹팩)을 설정합니다.

```js
const path = require('path');

const HtmlWebpackPlugin = require('html-webpack-plugin');

// For Typescript
const ForkTsCheckerWebpackPlugin = require('fork-ts-checker-webpack-plugin');

module.exports = {
  entry: {
    // For Typescript
    'js/app': ['./src/App.tsx'],
  },
  output: {
    path: path.resolve(__dirname, 'dist/'),
    publicPath: '/',
  },
  module: {
    rules: [
      // For Typescript
      {
        test: /\.(ts|tsx)$/,
        use: [
          'babel-loader',
          {
            loader: 'ts-loader',
            options: {
              transpileOnly: true,
            },
          },
        ],
        exclude: /node_modules/,
      },
    ],
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: './src/index.html',
      filename: 'index.html',
    }),
    // For typescript
    new ForkTsCheckerWebpackPlugin({ silent: true }),
  ],
};
```

수정된 내용을 확인해 보도록 하겠습니다.

```js
// For Typescript
const ForkTsCheckerWebpackPlugin = require('fork-ts-checker-webpack-plugin');
```

Typescript(타입스크립트)를 빌드할 때 성능을 향상시키기 위한 플러그인를 불러왔습니다.

```js
entry: {
  // For Typescript
  'js/app': ['./src/App.tsx'],
},
```

번들 파일(bundle)의 시작 파일(Entry)을 `jsx`에서 `tsx`로 변경하였습니다.

```js
{
  test: /\.(ts|tsx)$/,
  use: [
    'babel-loader',
    {
      loader: 'ts-loader',
      options: {
        transpileOnly: true,
      },
    },
  ],
  exclude: /node_modules/,
},
```

Webpack(웹팩)에서 Typescript(타입스크립트)를 사용하기 위해 `js|jsx`를 `ts|tsx`로 수정하였고, `ts-loader`를 추가하였습니다. ts-loader의 옵션은 성능 향상을 위한 옵션입니다.

```js
plugins: [
  ...
  // For typescript
  new ForkTsCheckerWebpackPlugin({ silent: true }),
],
```

마지막으로 Typescript(타입스크립트)의 컴파일 속도 향상을 위한 플러그인을 설정하였습니다.

{% include in-feed-ads.html %}

## tsconfig.json
Typescript(타입스크립트)를 사용하기 위해 `tsconfig.json`을 만들고 아래와 같이 수정합니다.

```json
{
  "compilerOptions": {
    "target": "es6",
    "module": "esnext",
    "moduleResolution": "node",
    "noResolve": false,
    "noImplicitAny": false,
    "removeComments": false,
    "sourceMap": true,
    "allowJs": true,
    "jsx": "react",
    "allowSyntheticDefaultImports": true,
    "keyofStringsOnly": true
  },
  "typeRoots": ["node_modules/@types", "src/@type"],
  "exclude": [
    "node_modules",
    "build",
    "scripts",
    "acceptance-tests",
    "webpack",
    "jest",
    "src/setupTests.ts",
    "./node_modules/**/*"
  ],
  "include": ["./src/**/*", "@type"]
}
```

옵션에 대한 설명은 생략하도록 하겠습니다. 자세한 내용은 아래의 사이트를 참고하시기 바랍니다.

- [https://www.typescriptlang.org/docs/handbook/tsconfig-json.html](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html){:rel="nofollow noreferrer" target="_blank"}
- [https://www.typescriptlang.org/docs/handbook/compiler-options.html](https://www.typescriptlang.org/docs/handbook/compiler-options.html){:rel="nofollow noreferrer" target="_blank"}

## tslint.json
Typescript를 사용하기 위해 `tslint.json`을 생성하고 아래와 같이 수정합니다.

```json
{
  "extends": ["tslint", "tslint-react"],
  "rules": {
    "align": [true, "parameters", "statements"],
    "jsx-alignment": false,
    "ban": false,
    "class-name": true,
    "comment-format": [true, "check-space"],
    "curly": true,
    "eofline": false,
    "forin": true,
    "indent": [true, "spaces"],
    "interface-name": [false],
    "jsdoc-format": true,
    "jsx-no-lambda": false,
    "jsx-no-multiline-js": false,
    "label-position": true,
    "max-line-length": [true, 120],
    "member-ordering": [
      true,
      {
        "order": [
          "public-before-private",
          "static-before-instance",
          "variables-before-functions"
        ]
      }
    ],
    "no-any": false,
    "no-arg": true,
    "no-bitwise": true,
    "no-console": [
      true,
      "log",
      "error",
      "debug",
      "info",
      "time",
      "timeEnd",
      "trace"
    ],
    "no-consecutive-blank-lines": true,
    "no-construct": true,
    "no-debugger": true,
    "no-duplicate-variable": true,
    "no-empty": false,
    "no-eval": true,
    "no-shadowed-variable": true,
    "no-string-literal": true,
    "no-switch-case-fall-through": true,
    "no-trailing-whitespace": false,
    "no-unused-expression": true,
    "no-use-before-declare": true,
    "one-line": [
      true,
      "check-catch",
      "check-else",
      "check-open-brace",
      "check-whitespace"
    ],
    "quotemark": [true, "single", "jsx-double"],
    "radix": true,
    "semicolon": [false],
    "switch-default": true,

    "trailing-comma": [false],

    "triple-equals": [true, "allow-null-check"],
    "typedef": [true, "parameter", "property-declaration"],
    "typedef-whitespace": [
      true,
      {
        "call-signature": "nospace",
        "index-signature": "nospace",
        "parameter": "nospace",
        "property-declaration": "nospace",
        "variable-declaration": "nospace"
      }
    ],
    "variable-name": [
      true,
      "ban-keywords",
      "check-format",
      "allow-leading-underscore",
      "allow-pascal-case"
    ],
    "whitespace": [
      true,
      "check-branch",
      "check-decl",
      "check-module",
      "check-operator",
      "check-separator",
      "check-type",
      "check-typecast"
    ]
  }
}
```

옵션에 대한 설명은 아래에 사이트에서 확인하시기 바랍니다.

- [https://github.com/Microsoft/TypeScript-React-Starter#overriding-defaults](https://github.com/Microsoft/TypeScript-React-Starter#overriding-defaults){:rel="nofollow noreferrer" target="_blank"}
- [https://palantir.github.io/tslint/usage/configuration/](https://palantir.github.io/tslint/usage/configuration/){:rel="nofollow noreferrer" target="_blank"}

{% include in-feed-ads.html %}

## babel 설정
babel을 설정하기 위해 `.babelrc`를 생성하고 아래와 같이 수정합니다.

```json
{
  "presets": [
    [
      "@babel/preset-env",
      { "targets": { "browsers": ["last 2 versions", ">= 5% in KR"] } }
    ],
    "@babel/react",
    "@babel/typescript"
  ]
}
```

babel(바벨)에서 Typescript(타입스크립트)가 컴파일 가능하도록 `"@babel/typescript"`을 추가하였습니다.

## Typescript 스타일 코딩
React(리액트)에서 Typescript(타입스크립트)를 사용하기 위해 `./src/App.jsx`를 `./src/App.tsx`로 이름을 변경하고 아래와 같이 수정합니다.

```js
import * as React from 'react';
import * as ReactDOM from 'react-dom';

interface Props {}

const App = ({  }: Props) => {
  return <h1>Hello World!</h1>;
};

ReactDOM.render(<App />, document.getElementById('app'));
```

## 확인
아래에 명령어로 우리가 생성하고 설정한 내용이 제대로 동작하는지 확인합니다.

```bash
npm start
```

그리고 브라우저를 열고 `http://localhost:8080/` 이동하면 `Hello World!`가 보이는 것을 확인할 수 있습니다. package.json의 스크립트인 `"start": "webpack-dev-server --mode development",`을 `"typescript": "webpack-dev-server --mode development --open",`처럼 `--open` 옵션을 추가하면 `npm start`로 Webpack(웹팩)의 개발 서버를 실행시키면 자동적으로 브라우저가 열리고 `http://localhost:8080/`로 이동합니다.

이제 실행되고 있는 개발 서버를 죽이고, 아래에 명령어로 빌드해봅니다.

```bash
npm run build
```

문제없이 실행되면 `./dist/` 폴더가 생성되고 하위에 `index.html`과 `/js/app.js`가 생성된 것을 확인할 수 있습니다. 또한 `index.html`을 열어보면 우리가 만든 index.html과 다르게 `<script type="text/javascript" src="/js/app.js"></script>`이 추가된 것을 확인할 수 있습니다.

## 참고
- [https://github.com/TypeStrong/ts-loader](https://github.com/TypeStrong/ts-loader){:rel="nofollow noreferrer" target="_blank"}
- [https://github.com/Realytics/fork-ts-checker-webpack-plugin](https://github.com/Realytics/fork-ts-checker-webpack-plugin){:rel="nofollow noreferrer" target="_blank"}
- [https://github.com/palantir/tslint-react](https://github.com/palantir/tslint-react){:rel="nofollow noreferrer" target="_blank"}