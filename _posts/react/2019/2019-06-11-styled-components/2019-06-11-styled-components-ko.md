---
layout: 'post'
permalink: '/react/styled-components/'
paginate_path: '/react/:num/styled-components/'
lang: 'ko'
categories: 'react'
comments: true

title: 'React에서 styled-components 사용하기'
description: 'React(리액트)에서 styled-components를 사용하기 위한 방법에 대해서 알아봅시다.'
image: '/assets/images/category/react/2019/styled-components/background.jpg'
---

## 개요
회사에서 React(리액트)로 새로운 프로젝트를 진행하게 되었습니다. 그래서 오랜만에 처음부터 세팅할 기회가 생겨 정리하게 되었습니다. 이번 블로그 포스트에서는 React(리액트)에서 styled-components를 사용하기 위한 방법에 대해서 살펴보고, React(리액트) 프로젝트에서 styled-components를 사용해 보겠습니다.

이 블로그에서 다루는 소스코드는 깃헙(Github)에서 확인할 수 있습니다.

- Github: [https://github.com/dev-yakuza/react_styled-components](https://github.com/dev-yakuza/react_styled-components){:target="_blank"}

이번 블로그 포스트에서 사용할 소스 코드는 이전 블로그에서 만든 프로젝트를 기반으로 합니다.

- 이전 블로그: [React에서 Typescript 사용하기]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}

## 프로젝트 준비
이 블로그 포스트에서 사용할 React(리액트) 프로젝트는 Webpack(웹팩)과 Typescript(타입스크립트)가 적용된 프로젝트를 기반으로 합니다. 자세한 내용은 이전 블로그 포스트를 확인해 주시기 바랍니다.

- [Webpack으로 React 시작하기]({{site.url}}/{{page.categories}}/start/){:target="_blank"}
- [React에서 Typescript 사용하기]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}

이전 블로그를 통해 프로젝트를 생성하면 아래와 같은 구조를 가지고 있습니다. 우리는 react_typescript라는 이름 대신 react_styled-components라는 이름으로 프로젝트를 생성했습니다.

```bash
|-- src
|   |-- index.html
|   |-- index.tsx
|-- .babelrc
|-- package.json
|-- webpack.config.js
```

## 설치
아래에 명령어로 React(리액트)에 styled-components를 사용하기 위해 필요한 라이브러리들을 설치합니다.

```bash
npm install --save-dev styled-components @types/styled-components babel-plugin-styled-components cross-env
```

- styled-components: styled-components를 사용합니다.
- @types/styled-components: styled-components를 사용할때 Typescript(타입스크립트)를 사용하기 위한 라이브러리.
- babel-plugin-styled-components: styled-components의 class명을 쉽게 알 수 있게 해주는 라이브러리.
- cross-env: Mac과 Windows에서 동일한 명령어로 환경 변수를 설정하기 위해 사용합니다.

{% include in-feed-ads.html %}

## package.json 수정
아래와 같이 `package.json`의 스크립트 부분을 수정합니다.

```js
"scripts": {
  "start": "cross-env NODE_ENV=development webpack-dev-server --open",
  "prebuild": "rimraf dist",
  "build": "cross-env NODE_ENV=production webpack --progress"
},
```

이전에는 Webpack(웹팩)의 모드를 설정하기 위해 `--mode development`와 `--mode production`을 사용하였지만 이 부분을 환경 변수로 설정하기 위해 변경하였습니다.

## Webpack 수정
아래와 같이 `webpack.config.js` 파일을 수정합니다.

```js
...
module.exports = {
  mode: process.env.NODE_ENV,
  ...
};
...
```

이전에는 명령어로 모드를 설정하였지만, 환경 변수를 통해 설정하기 위해 `mode`를 별도로 추가하였습니다.

## babel 설정
아래와 같이 `.babelrc` 파일을 수정합니다.

```json
{
  "presets": [
    ...
  ],
  "env": {
    "development": {
      "plugins": ["babel-plugin-styled-components"]
    }
  }
}
```

환경 변수가 development일 경우 class명을 구별하기 쉽도록 babel-plugin-styled-components를 설정하였습니다. 환경 변수가 production인 경우 class명을 hash화해서 사람이 인식하기 어렵게 만듭니다.

[환경 변수가 development인 경우]

![React에서 styled-components 사용하기 - 환경 변수 development일 때 class명](/assets/images/category/react/2019/styled-components/styled-components-in-development.jpg)

[환경 변수가 production인 경우]

![React에서 styled-components 사용하기 - 환경 변수 production일 때 class명](/assets/images/category/react/2019/styled-components/styled-components-in-production.jpg)

{% include in-feed-ads.html %}

## styled-components 스타일 코딩
React(리액트)에서 styled-components를 사용하기 위해 `./src/index.tsx`를 아래와 같이 수정합니다.

```js
import * as React from 'react';
import * as ReactDOM from 'react-dom';
import Styled from 'styled-components';

const Title = Styled.h1`
  color: red;
`;
interface Props {}

const App = ({  }: Props) => {
  return <Title>Hello World!</Title>;
};

ReactDOM.render(<App />, document.getElementById('app'));
```

## 확인
아래에 명령어로 우리가 생성하고 설정한 내용이 제대로 동작하는지 확인합니다.

```bash
npm start
```

그리고 브라우저를 열고 `http://localhost:8080/` 이동하면 `Hello World!`가 보이는 것을 확인할 수 있습니다. package.json의 스크립트인 `"start": "webpack-dev-server --mode development",`을 `"styled-components": "webpack-dev-server --mode development --open",`처럼 `--open` 옵션을 추가하면 `npm start`로 Webpack(웹팩)의 개발 서버를 실행시키면 자동적으로 브라우저가 열리고 `http://localhost:8080/`로 이동합니다.

이제 실행되고 있는 개발 서버를 죽이고, 아래에 명령어로 빌드해봅니다.

```bash
npm run build
```

문제없이 실행되면 `./dist/` 폴더가 생성되고 하위에 `index.html`과 `/js/app.js`가 생성된 것을 확인할 수 있습니다. 또한 `index.html`을 열어보면 우리가 만든 index.html과 다르게 `<script type="text/javascript" src="/js/app.js"></script>`이 추가된 것을 확인할 수 있습니다.

## 에러 대응
React(리액트) 프로젝트를 확인하기 위해 `npm start`를 사용할 때는 문제가 없었으나, `npm run build`를 통해 빌드를 할 경우 아래와 같은 에러가 발생하였습니다.

```bash
ERROR in /git_repository/react_styled-components/node_modules/@types/react-native/globals.d.ts
ERROR in /git_repository/react_styled-components/node_modules/@types/react-native/globals.d.ts(36,15):
TS2300: Duplicate identifier 'FormData'.

ERROR in /git_repository/react_styled-components/node_modules/@types/react-native/globals.d.ts
ERROR in /git_repository/react_styled-components/node_modules/@types/react-native/globals.d.ts(81,5):
TS2717: Subsequent property declarations must have the same type.  Property 'body' must be of type 'BodyInit', but here has type 'string | ArrayBuffer | DataView | Int8Array | Uint8Array | Uint8ClampedArray | Int16Array | Uint16Array | Int32Array | Uint32Array | Float32Array | Float64Array | Blob | FormData'.

ERROR in /git_repository/react_styled-components/node_modules/@types/react-native/globals.d.ts
ERROR in /git_repository/react_styled-components/node_modules/@types/react-native/globals.d.ts(107,14):
TS2300: Duplicate identifier 'RequestInfo'.

ERROR in /git_repository/react_styled-components/node_modules/@types/react-native/globals.d.ts
ERROR in /git_repository/react_styled-components/node_modules/@types/react-native/globals.d.ts(126,13):
TS2403: Subsequent variable declarations must have the same type.  Variable 'Response' must be of type '{ new (body?: BodyInit, init?: ResponseInit): Response; prototype: Response; error(): Response; redirect(url: string, status?: number): Response; }', but here has type '{ new (body?: string | ArrayBuffer | DataView | Int8Array | Uint8Array | Uint8ClampedArray | Int16Array | Uint16Array | Int32Array | Uint32Array | Float32Array | Float64Array | Blob | FormData, init?: ResponseInit): Response; prototype: Response; error: () => Response; redirect: (url: string, status?: number) => Res...'.

ERROR in /git_repository/react_styled-components/node_modules/@types/react-native/globals.d.ts
ERROR in /git_repository/react_styled-components/node_modules/@types/react-native/globals.d.ts(249,14):
TS2300: Duplicate identifier 'XMLHttpRequestResponseType'.

ERROR in /git_repository/react_styled-components/node_modules/@types/react-native/index.d.ts
ERROR in /git_repository/react_styled-components/node_modules/@types/react-native/index.d.ts(9418,18):
TS2717: Subsequent property declarations must have the same type.  Property 'geolocation' must be of type 'Geolocation', but here has type 'GeolocationStatic'.

ERROR in /git_repository/react_styled-components/node_modules/@types/react-native/index.d.ts
ERROR in /git_repository/react_styled-components/node_modules/@types/react-native/index.d.ts(9421,11):
TS2451: Cannot redeclare block-scoped variable 'navigator'.

ERROR in /git_repository/react_styled-components/node_modules/typescript/lib/lib.dom.d.ts
ERROR in /git_repository/react_styled-components/node_modules/typescript/lib/lib.dom.d.ts(5353,11):
TS2300: Duplicate identifier 'FormData'.

ERROR in /git_repository/react_styled-components/node_modules/typescript/lib/lib.dom.d.ts
ERROR in /git_repository/react_styled-components/node_modules/typescript/lib/lib.dom.d.ts(5363,13):
TS2300: Duplicate identifier 'FormData'.

ERROR in /git_repository/react_styled-components/node_modules/typescript/lib/lib.dom.d.ts
ERROR in /git_repository/react_styled-components/node_modules/typescript/lib/lib.dom.d.ts(17123,11):
TS2320: Interface 'Window' cannot simultaneously extend types 'GlobalFetch' and 'WindowOrWorkerGlobalScope'.
  Named property 'fetch' of types 'GlobalFetch' and 'WindowOrWorkerGlobalScope' are not identical.

ERROR in /git_repository/react_styled-components/node_modules/typescript/lib/lib.dom.d.ts
ERROR in /git_repository/react_styled-components/node_modules/typescript/lib/lib.dom.d.ts(18152,13):
TS2451: Cannot redeclare block-scoped variable 'navigator'.

ERROR in /git_repository/react_styled-components/node_modules/typescript/lib/lib.dom.d.ts
ERROR in /git_repository/react_styled-components/node_modules/typescript/lib/lib.dom.d.ts(18568,6):
TS2300: Duplicate identifier 'RequestInfo'.

ERROR in /git_repository/react_styled-components/node_modules/typescript/lib/lib.dom.d.ts
ERROR in /git_repository/react_styled-components/node_modules/typescript/lib/lib.dom.d.ts(18746,6):
TS2300: Duplicate identifier 'XMLHttpRequestResponseType'.

ERROR in /git_repository/react_styled-components/node_modules/typescript/lib/lib.dom.iterable.d.ts
ERROR in /git_repository/react_styled-components/node_modules/typescript/lib/lib.dom.iterable.d.ts(67,11):
```

이 문제를 해결하기 위해 `tsconfig.json`을 아래와 같이 수정하였습니다.

```json
{
  "compilerOptions": {
    ...
    "skipLibCheck": true
  },
  ...
}
```