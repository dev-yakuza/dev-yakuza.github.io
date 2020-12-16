---
layout: 'post'
permalink: '/react/root-import/'
paginate_path: '/react/:num/root-import/'
lang: 'ko'
categories: 'react'
comments: true

title: 'React에서 root import하기'
description: 'React(리액트)에서 컴포넌트(Component)를 불러올때(import), root 폴더를 기준으로 불러오도록 설정해 봅시다.'
image: '/assets/images/category/react/2019/root-import/background.jpg'
---

## 개요
React Native(RN 리액트네이티브)에서도 소개한 root import를 React(리액트)에도 적용하려고 합니다. 왜 root import를 사용하려고 하는지, 문제점은 무엇인지는 React Native(RN 리액트네이티브)의 블로그를 참고하시기 바랍니다.

- [RN(React Native)에서 root import하기]({{site.url}}/react-native/root-import/){:target="_blank"}

이 블로그에서 다루는 소스코드는 깃헙(Github)에서 확인할 수 있습니다.

- Github: [https://github.com/dev-yakuza/react_root_import](https://github.com/dev-yakuza/react_root_import){:target="_blank"}

## 프로젝트 준비
이 블로그 포스트에서 사용할 React(리액트) 프로젝트는 Webpack(웹팩)과 Typescript(타입스크립트), styled-components가 적용된 프로젝트를 기반으로 합니다. 자세한 내용은 이전 블로그 포스트를 확인해 주시기 바랍니다.

- [Webpack으로 React 시작하기]({{site.url}}/{{page.categories}}/start/){:target="_blank"}
- [React에서 Typescript 사용하기]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}
- [React에서 styled-components 사용하기]({{site.url}}/{{page.categories}}/styled-components/){:target="_blank"}

이전 블로그를 통해 프로젝트를 생성하면 아래와 같은 구조를 가지고 있습니다. 우리는 react_styled-components라는 이름 대신 react_root_import라는 이름으로 프로젝트를 생성했습니다.

```bash
|-- src
|   |-- index.html
|   |-- App.tsx
|-- .babelrc
|-- package.json
|-- webpack.config.js
```

{% include in-feed-ads.html %}

## babel-plugin-root-import
root 폴더부터 참조할 수 있게 하기 위해 `babel-plugin-root-import`를 아래에 명령어로 설치합니다.

```bash
npm install babel-plugin-root-import --save-dev
```

React(리액트) 프로젝트의 `.babelrc`를 열고 아래와 같이 수정합니다.

```json
{
  "presets": [
    ...
  ],
  "plugins": [
    [
      "babel-plugin-root-import",
      {
        "rootPathPrefix": "~",
        "rootPathSuffix": "src"
      }
    ]
  ],
  "env": {
    ...
  }
}
```

제 폴더 구조를 보면 알수 있지만 `src` 폴더에 모든 소스를 넣고 관리하고 있습니다. 따라서 저는 `root` 폴더가 아닌 `src` 폴더를 기준으로 동작하도록 설정하였습니다.

## Webpack 설정
root 폴더부터 참조할 수 있게 하기 위해 `webpack.config.js`을 열고 아래와 같이 수정합니다.

```js
...
module.exports = {
  mode: process.env.NODE_ENV,
  entry: {
    ...
  },
  output: {
    ...
  },
  module: {
    ...
  },
  resolve: {
    extensions: ['.ts', '.tsx', '.js', '.jsx'],
  },
  plugins: [
    ...
  ],
};
```

## Typescript
Typescript(타입스크립트)를 사용하지 않는다면 위에 설정만으로 해결됩니다. 저는 React(리액트) 프로젝트에서 Typescript(타입스크립트)를 사용하므로 Typescript(타입스크립트)도 root 폴더를 인식하도록 설정해주어야 합니다.

React(리액트) 프로젝트의 `tsconfig.json` 파일을 열고 아래와 같이 수정합니다.

```json
{
  "compilerOptions": {
    ...
    "baseUrl": "./src", // all paths are relative to the baseUrl
    "paths": {
      "~/*": ["*"] // resolve any `~/foo/bar` to `<baseUrl>/foo/bar`
    }
  },
  ...
}
```

{% include in-feed-ads.html %}

## 소스 수정
위에 설정을 확인하기 위해 소스 코드를 수정해보겠습니다. `src/Components/Title/index.tsx`를 생성하고 아래와 같이 수정합니다.

```js
import * as React from 'react';
import Styled from 'styled-components';

const Label = Styled.h1`
  color: red;
`;
interface Props {
  label: string;
}

const Title = ({ label }: Props) => {
  return <Label>{label}</Label>;
};

export default Title;
```

그리고 `src/Features/Top/index.tsx`를 생성하고 아래와 같이 수정합니다.

```js
import * as React from 'react';

import Title from '~/Components/Title';

interface Props {}

const Top = ({  }: Props) => {
  return <Title label="Hello World!" />;
};

export default Top;
```

마지막으로, `src/App.tsx`를 열고 아래와 같이 수정합니다.

```js
import * as React from 'react';
import * as ReactDOM from 'react-dom';

import Top from './Features/Top';

interface Props {}

const App = ({  }: Props) => {
  return <Top />;
};

ReactDOM.render(<App />, document.getElementById('app'));
```

{% include in-feed-ads.html %}

## 확인
위에서 설정한 내용이 제대로 동작하는지 확인하기 위해 아래에 명령어로 Webpack(웹팩) 테스트 서버를 실행시킵니다.

```bash
npm start
```

브라우저에서 `http://localhost:8080/`를 열면 `Hello World!`가 표시되는 것을 확인할 수 있습니다.
아래에 명령어로 Webpack(웹팩)을 이용하여 React(리액트) 프로젝트를 빌드(build)해 봅시다.

```bash
npm run build
```

그러면 `dist` 폴더에 파일들이 생성되는 것을 확인할 수 있습니다.

## 완료
이로써 React(리액트) 프로젝트에서도 `import`할 때, `../../../../` 대신 `~/`을 사용할 수 있게 되었습니다. 이번 소스에서도 알수 있듯이 저는 참조하는 컴포넌트(Component)가 폴더안에 있는 경우 `./`를 사용하여 참조하고, 폴더밖에 있는 경우 `~/`을 이용하여 참조하고 있습니다.
