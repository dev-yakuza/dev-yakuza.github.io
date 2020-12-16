---
layout: 'post'
permalink: '/react/image-and-font/'
paginate_path: '/react/:num/image-and-font/'
lang: 'ko'
categories: 'react'
comments: true

title: 'React에서 이미지와 웹 폰트 다루기'
description: 'Webpack(폰팩)을 기반으로 만든 React(리액트) 프로젝트에서 이미지(image)와 웹 폰트(font)를 사용하는 방법에 대해서 알아봅니다.'
image: '/assets/images/category/react/2019/image-and-font/background.jpg'
---

## 개요
회사에서 React(리액트)로 새로운 프로젝트를 진행하게 되었습니다. 그래서 Wepack(웹팩)을 사용하여 React(리액트) 프로젝트를 설정하려고 합니다. 이번 블로그 포스트에서는 Webpack(웹팩)을 기반으로 만든 React(리액트) 프로젝트에서 리소스(Resource)인, 이미지(image)와 웹 폰트(Font)를 다루는 방법에 대해서 설명합니다.

이 블로그에서 다루는 소스코드는 깃헙(Github)에서 확인할 수 있습니다.

- Github: [https://github.com/dev-yakuza/react_image_font](https://github.com/dev-yakuza/react_image_font){:rel="noopener" target="_blank"}

## 프로젝트 준비
여기서 사용하는 React(리액트) 프로젝트는 아래에 내용들이 적용된 프로젝트입니다. 자세한 내용은 각 블로그 포스트를 참고하시기 바랍니다.

- [Webpack으로 React 시작하기]({{site.url}}/{{page.categories}}/start/){:target="_blank"}
- [React에서 Typescript 사용하기]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}
- [React에서 styled-components 사용하기]({{site.url}}/{{page.categories}}/styled-components/){:target="_blank"}
- [React에서 root import하기]({{site.url}}/{{page.categories}}/root-import/){:target="_blank"}
- [React Router]({{site.url}}/{{page.categories}}/react-router/){:target="_blank"}

이전 블로그를 통해 프로젝트를 생성하면 아래와 같은 구조를 가지고 있습니다. 우리는 react_router라는 이름 대신 react_image_font라는 이름으로 프로젝트를 생성했습니다.

```bash
|-- src
|   |-- Components
|   |   |-- Title
|   |   |   |-- index.tsx
|   |-- Features
|   |   |-- Page1
|   |   |   |-- index.tsx
|   |   |-- Page2
|   |   |   |-- index.tsx
|   |   |-- Top
|   |   |   |-- index.tsx
|   |-- index.html
|   |-- App.tsx
|-- .babelrc
|-- package.json
|-- webpack.config.js
```

## 모듈 설치
Webpack(웹팩) 기반 React(리액트) 프로젝트에서 이미지, 웹 폰트를 다루기 위해서는 Webpack(웹팩)의 `file-loader`, `url-loader`가 필요합니다. 아래에 명령어로 `file-loader`, `url-loader`를 설치합니다.

```bash
npm install --save-dev file-loader, url-loader
```

- file-loader: Webpack(웹팩)에서 실제 사용하는 파일을 복사하는데 사용됩니다.
- url-loader: Webpack(웹팩)에서 파일 사이즈가 작은 파일을 번들 파일로 만드는데 사용합니다.

{% include in-feed-ads.html %}

## Webpack 수정
설치한 모듈(file-loader, url-loader)를 사용하기 위해 `webpack.config.js`를 열고 아래와 같이 수정합니다.

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
    rules: [
      ...
      {
        // write image files under 10k to inline or copy image files over 10k
        test: /\.(jpg|jpeg|gif|png|svg|ico)?$/,
        use: [
          {
            loader: 'url-loader',
            options: {
              limit: 10000,
              fallback: 'file-loader',
              name: 'images/[name].[ext]',
            },
          },
        ],
      },
      {
        // write files under 10k to inline or copy files over 10k
        test: /\.(woff|woff2|eot|ttf|otf)$/,
        use: [
          {
            loader: 'url-loader',
            options: {
              limit: 10000,
              fallback: 'file-loader',
              name: 'fonts/[name].[ext]',
            },
          },
        ],
      },
    ],
  },
  resolve: {
    ...
  },
  plugins: [
    ...
  ],
  devServer: {
    ...
  },
};
```

두 설정이 비슷하므로 하나에 설정에 대해서만 자세히 살펴보도록 하겠습니다.

```js
{
  // write image files under 10k to inline or copy image files over 10k
  test: /\.(jpg|jpeg|gif|png|svg|ico)?$/,
  use: [
    {
      loader: 'url-loader',
      options: {
        limit: 10000,
        fallback: 'file-loader',
        name: 'images/[name].[ext]',
      },
    },
  ],
},
```

- `test: /\.(jpg|jpeg|gif|png|svg|ico)?$/,`: 해당 파일들을 다룹니다.
- `loader: 'url-loader',`: url-loader를 사용합니다.
- `limit: 10000,`: 파일 사이즈가 10k보다 작은 경우 문자열로 만들어 사용하는 부분에 직접 삽입합니다.(번들로 만든다.)
- `fallback: 'file-loader',`: 파일 사이즈가 10k보다 큰 경우, file-loader를 이용하여 파일을 복사합니다.
- `name: 'images/[name].[ext]',`: 복사할때 파일을 이미지(image) 폴더에 파일명(name)과 확장자(ext) 형태로 복사합니다.

## 웹 폰트 적용
명확하게 웹 폰트(Font)가 적용되었는지 확인하기 위해 Google Font의 [Aguafina Script](https://fonts.google.com/specimen/Aguafina+Script){:rel="nofollow noreferrer" target="_blank"}를 사용하여 테스트해보겠습니다. 우선 아래에 링크를 통해 Google Font로 이동하여 웹 폰트(Font)를 다운로드 합니다.

- Aguafina Script Font: [https://fonts.google.com/specimen/Aguafina+Script](https://fonts.google.com/specimen/Aguafina+Script){:rel="nofollow noreferrer" target="_blank"}

웹 폰트(Font)를 다운로드하였다면 `src/Assets/Fonts` 폴더를 만들고 해당 파일을 복사합니다. 그리고 `src/App.tsx`를 열고 아래와 같이 수정합니다.

```js
import * as React from 'react';
import * as ReactDOM from 'react-dom';
import { createGlobalStyle } from 'styled-components';

import Router from './Router';

const GlobalStyles = createGlobalStyle`
  @font-face {
    font-family:'AguafinaScript';
    src: url(${require('~/Assets/Fonts/AguafinaScript-Regular.ttf')});
  }
  body {
    font-family: 'AguafinaScript', sans-serif;
  }
`;

interface Props {}
const App = ({  }: Props) => {
  return (
    <>
      <GlobalStyles />
      <Router />
    </>
  );
};

ReactDOM.render(<App />, document.getElementById('app'));
```

우리가 사용하는 React(리액트) 프로젝트는 [styled-components]({{site.url}}/{{page.categories}}/styled-components/){:target="_blank"}가 적용되있습니다. styled-components의 `createGlobalStyle`을 이용하여 전역 스타일(Global Style)을 아래와 같이 만들었습니다.

```js
const GlobalStyles = createGlobalStyle`
  @font-face {
    font-family:'AguafinaScript';
    src: url(${require('~/Assets/Fonts/AguafinaScript-Regular.ttf')});
  }
  body {
    font-family: 'AguafinaScript', sans-serif;
  }
`;
```

- `src: url(${require('~/Assets/Fonts/AguafinaScript-Regular.ttf')});`: 우리는 url-loader와 file-loader를 사용하므로 `require`를 이용하여 해당 파일을 불러오도록 하였습니다.

이렇게 만든 전역 스타일(Global Style)을 아래와 같이 적용하였습니다.

```js
const App = ({  }: Props) => {
  return (
    <>
      <GlobalStyles />
      <Router />
    </>
  );
};
```

{% include in-feed-ads.html %}

## 이미지 사용하기
이미지를 사용하기 위해 `src/Assets/images` 폴더를 만들고 이미지 파일을 복사하였습니다. 여기에서는 10k보다 큰 png파일과, 10k보다 작은 파일을 비교하기 위해 추가하였습니다. 그리고 이미지를 사용할 부분(`src/Features/Top/index.tsx`)을 열고 아래와 같이 수정합니다.

```js
...
const Top = ({ match, history, location }: Props) => {
  ...
  return (
    <div>
      ...
      <img src={require('~/Assets/Images/logo.jpg')} />
      <img src={require('~/Assets/Images/ic_account.jpg')} />
      <img src={require('~/Assets/Images/ic_account.svg')} />
    </div>
  );
};

export default Top;
```

웹 폰트(Font)를 불러올때처럼, `require`를 이용하여 파일들을 불러왔습니다.

## 확인
지금까지 작업한 내용을 확인하기 위해 아래에 명령어로 Webpack(웹팩) 개발 서버를 실행시킵니다.

```bash
npm start
```

그러면 아래와 같이 웹 폰트(Font)가 적용된 화면과 이미지(image)가 로딩된 화면을 볼 수 있습니다.

![Webpack 기반 React 프로젝트에서 웹 폰트, 이미지 사용](/assets/images/category/react/2019/image-and-font/check-with-webpack-dev-server.jpg)

오른쪽 소스코드를 보면 알 수 있듯이, 10k보다 작은 파일들은 하나에 파일로 번들링(Bundle)된 것을 확인할 수 있습니다.

아래에 명령어로 빌드(Build)해 봅시다.

```bash
npm run build
```

그러면 아래와 같이 `dist` 폴더에 10k 보다 큰 이미지 파일과 웹 폰트(Font) 파일이 복사된 것을 확인할 수 있습니다.

![Webpack 기반 React 프로젝트에서 웹 폰트, 이미지 복사](/assets/images/category/react/2019/image-and-font/copy-image-font-file-with-webpack.jpg)

