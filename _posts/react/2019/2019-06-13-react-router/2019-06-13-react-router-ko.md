---
layout: 'post'
permalink: '/react/react-router/'
paginate_path: '/react/:num/react-router/'
lang: 'ko'
categories: 'react'
comments: true

title: 'React Router'
description: 'react-router을 사용하여 React(리액트)에서 페이지 전환을 사용해 봅시다.'
image: '/assets/images/category/react/2019/react-router/background.jpg'
---

## 개요
React(리액트)는 SPA(Single Page Applicatoin)입니다. 말그대로 페이지(Page)가 하나(Single)인 어플리케이션(Application)입니다. 이렇게 페이지가 하나이기 때문에 페이지 이동이 불가능합니다. 하지만 이렇게 페이지가 하나인 경우에도 일반 웹 사이트처럼 URL에 따른 페이지 이동을 할 수 있게 해주는 기능이 `React Router`입니다.

- React Router: [https://github.com/ReactTraining/react-router](https://github.com/ReactTraining/react-router){:rel="nofollow noreferrer" target="_blank"}
- React Router Training: [https://reacttraining.com/react-router/](https://reacttraining.com/react-router/){:rel="nofollow noreferrer" target="_blank"}

React Router는 웹(react-router-dom)에서도 네이티브(react-router-native)에서도 사용할 수 있습니다. 이 블로그 포스트에서는 React(리액트) 프로젝트에 React Router(react-router-dom)을 적용하여 페이지 전환을 구현해 보도록 하겠습니다.

이 블로그에서 다루는 소스코드는 깃헙(Github)에서 확인할 수 있습니다.

- Github: [https://github.com/dev-yakuza/react_router](https://github.com/dev-yakuza/react_router){:target="_blank"}

## 프로젝트 준비
여기서 사용하는 React(리액트) 프로젝트는 아래에 내용들이 적용된 프로젝트입니다. 자세한 내용은 각 블로그 포스트를 참고하시기 바랍니다.

- [Webpack으로 React 시작하기]({{site.url}}/{{page.categories}}/start/){:target="_blank"}
- [React에서 Typescript 사용하기]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}
- [React에서 styled-components 사용하기]({{site.url}}/{{page.categories}}/styled-components/){:target="_blank"}
- [React에서 root import하기]({{site.url}}/{{page.categories}}/root-import/){:target="_blank"}

이전 블로그를 통해 프로젝트를 생성하면 아래와 같은 구조를 가지고 있습니다. 우리는 react_root_import라는 이름 대신 react_router라는 이름으로 프로젝트를 생성했습니다.

```bash
|-- src
|   |-- Components
|   |   |-- Title
|   |   |   |-- index.tsx
|   |-- Features
|   |   |-- Top
|   |   |   |-- index.tsx
|   |-- index.html
|   |-- App.tsx
|-- .babelrc
|-- package.json
|-- webpack.config.js
```

{% include in-feed-ads.html %}

## react-router-dom 설치
아래에 명령어로 `react-router-dom`을 설치합니다.

```bash
npm install --save react-router-dom
npm install --save-dev @types/react-router-dom
```

- react-router-dom: React Router를 위한 라이브러리입니다.
- @types/react-router-dom: Typescript(타입스크립트)를 사용하기 위한 react-router-dom의 타입(Type) 정의 라이브러리입니다.

## 페이지 추가
페이지 전환을 위해 테스트 페이지를 만들어 봅시다. `src/Features/Page1.tsx`를 만들고 아래와 같이 수정합니다.

```js
import * as React from 'react';
import { Link, RouteComponentProps } from 'react-router-dom';

import Title from '~/Components/Title';

interface Props extends RouteComponentProps {}

const Page1 = ({ history }: Props) => {
  return (
    <div>
      <a onClick={history.goBack}>Previous Page</a>
      <Link to="/">Top</Link>
      <Link to="/page2">Page 2</Link>
      <Title label="Page 1" />
    </div>
  );
};

export default Page1;
```

- react-router에서 페이지 전환으로 불러온 컴포넌트(Component)는 `history`, `location`, `match`의 Props를 가지고 있습니다. 이 Props를 정의하고 있는 `RouteComponentProps`을 상속받아 Props를 처리하였습니다.
- {% raw %}`<a onClick={history.goBack}>Previous Page</a>`{% endraw %}: 이전 페이지로 돌아가기 위해 react-router로부터 받은 Props(`history`)를 이용하여 뒤로 가기 기능을 구현하였습니다.
- {% raw %}`<Link to="/">Top</Link>`{% endraw %}: React안에서 react-router를 이용해 페이지 전환을 할때는 react-router-dom의 `Link` 컴포넌트를 이용해야 합니다.

위와 동일하게 테스트 페이지를 하나 더 만들어 봅니다. `src/Features/Page2.tsx`를 만들고 아래와 같이 수정합니다.

```js
import * as React from 'react';
import { Link, RouteComponentProps } from 'react-router-dom';

import Title from '~/Components/Title';

interface Props extends RouteComponentProps {}

const Page2 = ({ history }: Props) => {
  return (
    <div>
      <a onClick={history.goBack}>Previous Page</a>
      <Link to="/">Top</Link>
      <Link to="/page1">Page 1</Link>
      <Title label="Page 2" />
    </div>
  );
};

export default Page2;
```

마지막으로 이전에 만든 `Top` 페이지를 아래와 같이 수정하여 링크를 추가합니다.

```js
import * as React from 'react';
import { Link, RouteComponentProps } from 'react-router-dom';

import Title from '~/Components/Title';

interface Props extends RouteComponentProps {}
const Top = ({ match, history, location }: Props) => {
  console.log(match);
  console.log(history);
  console.log(location);
  return (
    <div>
      <Link to="/page1">Page 1</Link>
      <Link to="/page2">Page 2</Link>
      <Title label="Hello World!" />
    </div>
  );
};

export default Top;
```

{% include in-feed-ads.html %}

## Router 만들기
저는 전반적인 라우팅(Routing)을 관리하는 파일을 하나 만들고 그 곳에서 전체적인 Route를 관리하고 있습니다. 이 부분은 꼭 한 파일로 관리할 필요는 없습니다. 여러분의 상황에 맞게 활용하면 됩니다. 저의 경우는 `src/Router.tsx`를 만들고 아래와 같이 수정하였습니다.

```js
import * as React from 'react';
import { BrowserRouter, Route, Switch, Redirect } from 'react-router-dom';

import Top from './Features/Top';
import Page1 from './Features/Page1';
import Page2 from './Features/Page2';

const Router = () => {
  return (
    <BrowserRouter>
      <Switch>
        <Route exact={true} path="/" component={Top} />
        <Route path="/page1" component={Page1} />
        <Route path="/page2" component={Page2} />
        {/* Not Found */}
        <Route component={() => <Redirect to="/" />} />
      </Switch>
    </BrowserRouter>
  );
};

export default Router;
```

- BrowserRouter: react-router를 웹(Browser)상에서 사용하기 위한 컴포넌트(Component)입니다.
- Switch: 해당 Route에 맞는 최상단에 컴포넌트(Component)를 표시합니다.
- Route: 해당 URL(path)에 맞는 컴포넌트(component)를 표시합니다.

여기서 Switch에 역할에 대한 설명이 부족한거 같아 좀 더 자세히 설명하겠습니다. 현재 설정을 아래와 같이 수정해 보겠습니다.

```js
<BrowserRouter>
    <Switch>
        <Route exact={true} path="/" component={Top} />
        <Route path="/page1" component={Page1} />
        <Route path="/page1" component={Page2} />
        <Route path="/page2" component={Page2} />
        {/* Not Found */}
        <Route component={() => <Redirect to="/" />} />
    </Switch>
</BrowserRouter>
```

위와 같이 설정하고 아래에 명령어를 실행하여 Wepack(웹팩) 개발 서버를 실행시킵니다.

```bash
npm start
```

그리고 브라우저로 `page1`에 이동하여 확인하면 `Page1`만 표시되는 것을 확인할 수 있습니다. 하지만 아래와 같이 `Switch`를 제거하고

```js
<BrowserRouter>
    <Route exact={true} path="/" component={Top} />
    <Route path="/page1" component={Page1} />
    <Route path="/page1" component={Page2} />
    <Route path="/page2" component={Page2} />
    {/* Not Found */}
    <Route component={() => <Redirect to="/" />} />
</BrowserRouter>
```

브라우저에서 `page1`에 이동하여 확인하면 `Page1`과 `Page2`가 모두 화면에 표시되는 것을 알 수 있습니다. 이처럼 동일한 URL이 존재하는 경우 `Switch`는 상단에 선언된 컴포넌트(Component)만 표시합니다.


## App.tsx 수정
마지막으로 우리가 만든 Router가 동작하도록 `src/App.tsx`를 아래와 같이 수정합니다.

```js
import * as React from 'react';
import * as ReactDOM from 'react-dom';

import Router from './Router';

interface Props {}
const App = ({  }: Props) => {
  return <Router />;
};

ReactDOM.render(<App />, document.getElementById('app'));
```

## Webpack 수정
현재 상태에서 `npm start`를 실행하면 화면에 Top 페이지가 표시되고 링크를 통해 페이지 전환이 잘 되는 것을 확인할 수 있습니다. 하지만 `http://localhost:8080/page1` 또는 `http://localhost:8080/page2`와 같이 링크를 직접 입력하면 Page를 찾을 수 없다고 표시됩니다. 위에서도 설명했지만 SPA(Single Page Applicatoin)이므로 실제로는 페이지가 하나만 존재하기 때문에 이와 같은 문제가 발생합니다. 우리는 Webpack(웹팩) 설정을 통해 이 부분을 해결할 수 있습니다. `webpack.config.js`를 열고 아래와 같이 수정합니다.

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
  devServer: {
    contentBase: './dist',
    port: 3000,
    historyApiFallback: true,
  },
};
```

위와 같이 `devServer` 옵션을 사용하여 `webpack-dev-server`를 설정하였습니다. `historyApiFallback`을 사용하여 존재하지 않는 URL인 경우 404 응답(Response)을 내보내는 것이 아니라 `index.html`을 응답(Response)하도록 설정하였습니다. 이제 다시 `http://localhost:3000/page1` 또는 `http://localhost:3000/page2`을 직접 입력하여 페이지를 열어도 해당 페이지가 잘 보이는 것을 확인할 수 있습니다.

## 확인
아래에 명령어로 Webpack(웹팩) 개발 서버를 기동합니다.

```bash
npm start
```

그리고 브라우저를 열고 `http://localhost:3000/`으로 이동합니다.(Git 소스는 `--open` 옵션을 사용하고 있어 자동으로 브라우저가 열리고 해당 페이지로 이동합니다.)

화면에 보이는 링크들을 눌러 페이지를 이동해 봅니다. 그럼 문제없이 페이지를 이동할 수 있음을 확인할 수 있습니다. 또한, 직접 `http://localhost:3000/page1` 또는 `http://localhost:3000/page2`을 입력해도 페이지가 문제없이 화면에 표시되는 것을 확인할 수 있습니다.

마지막으로, 아래에 명령어로 빌드(Build)가 잘되는지 확인합니다.

```bash
npm run build
```

빌드(Build)가 완료되면 `dist/`에 파일과 폴더가 생성된 것을 확인할 수 있습니다.