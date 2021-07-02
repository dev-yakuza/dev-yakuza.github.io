---
layout: 'post'
permalink: '/react/create-react-app/react-router/'
paginate_path: '/react/:num/create-react-app/react-router/'
lang: 'ko'
categories: 'react'
comments: true

title: 'create-react-app에서 React Router 사용하기'
description: 'create-react-app로 생성한 React에서 페이지 전환 기능을 구현하기 위해 react-router를 사용하는 방법에 대해서 알아봅시다.'
image: '/assets/images/category/react/background.jpg'
published: false
---

<div id="contents_list" markdown="1">

## 목차

</div>

## 개요

React는 UI 자바스크립트 라이브러리로써 싱글 페이지 애플리케이션의 UI(User Interface)를 생성하는데 집중한 라이브러리입니다. 따라서, UI와 관련이 없는 페이지 전환 기능은 기본적으로 제공하고 있지 않습니다. 그래서 React에서 페이지 전환 기능을 구현하기 위해서는 외부 라이브러리에 의존해야 합니다. 이번 블로그 포스트에서는 React에서 페이지 전환을 위해 주로 사용되는 `react-router`에 대해서 알아보도록 하겠습니다.

- React Router 공식 사이트: [react-router](https://reactrouter.com/){:rel="noopener" target="_blank"}

혹시 React에 관해 궁금하신 분들은, 아래 링크를 확인해 보시기 바랍니다.

- [React란]({{site.url}}/{{page.categories}}/create-react-app/react/){:target="_blank"}

여기서 소개하는 코드는 아래의 링크에서 확인하실 수 있습니다.

- GitHub: [react_router_example](https://github.com/dev-yakuza/study-create-react-app/tree/main/example/react_router_example){:rel="noopener" target="_blank"}

## 프로젝트 준비

React에서 react-router를 사용하여 페이지 전환 기능을 구현해 보기 위해, React 프로젝트를 생성할 예정입니다. 이 블로그에서는 CRA(create-react-app)과 TypeScript를 사용하여 React 프로젝트를 생성합니다.

- [create-react-app]({{site.url}}/{{page.categories}}/create-react-app/start/){:target="_blank"}
- [create-react-app에서 TypeScript]({{site.url}}/{{page.categories}}/create-react-app/typescript/){:target="_blank"}

그럼 다음 명령어를 실행하여 TypeScript 기반 React 프로젝트를 생성합니다.

```bash
npx create-react-app react_router_example --template=typescript
```

{% include in-feed-ads.html %}

## react-router 설치

React에서 react-router를 사용하기 위해서는 react-router를 설치할 필요가 있습니다. 다음 명령어를 사용해서 react-router를 설치합니다.

```bash
npm install --save react-router-dom
npm install --save-dev @types/react-router-dom
```

## react-router 사용법

그럼 이제 react-router를 사용하여 React 프로젝트에 페이지 전환 기능을 추가해 봅시다.

### Router

React 프로젝트에서 react-router를 사용하려면, 우선 `Router`를 제공해야 합니다. `./src/index.tsx` 파일을 열고 다음과 같이 수정합니다.

```js
import { BrowserRouter as Router } from 'react-router-dom';

ReactDOM.render(
  <React.StrictMode>
    <Router>
      <App />
    </Router>
  </React.StrictMode>,
  document.getElementById('root')
);
```

react-router의 기능을 사용하는 컴포넌트는 항상 `Router`안에 선언이 되어야 합니다. react-router의 기능을 `Route` 밖에서 사용할 경우 에러가 발생합니다.

### Switch-Route

react-router를 사용하여 페이지 전환을 하기 위해서는 `Switch`와 `Route`를 사용해서 페이지를 정의할 필요가 있습니다. 그럼 `Switch`와 `Route`의 사용 방법을 확인하기 위해 `./src/App.tsx` 파일을 열고 다음과 같이 수정합니다.

```js
import { Switch, Route } from 'react-router-dom';
import { Home } from './Pages/Home';
import { Detail } from './Pages/Detail';

function App() {
  return (
    <div>
      <header>This is header</header>
      <Switch>
        <Route exact path="/">
          <Home />
        </Route>
        <Route path="/detail/:id">
          <Detail />
        </Route>
      </Switch>
    </div>
  );
}
```

react-router에서 Switch와 Route를 추가하였습니다. 또한 아직 만들지 않았지만, 화면에 표시할 두 페이지 컴포넌트도 가져왔습니다.

```js
import { Switch, Route } from 'react-router-dom';
import { Home } from './Pages/Home';
import { Detail } from './Pages/Detail';
```

이렇게 가져온 Switch와 Route, 각각의 페이지 컴포넌트를 다음과 같이 사용하였습니다.

```js
<div>
  <header>This is header</header>
  <Switch>
    <Route exact path="/">
      <Home />
    </Route>
    <Route path="/detail/:id">
      <Detail />
    </Route>
  </Switch>
</div>
```

기본적으로 Route는 Switch 안에서 사용되어야 합니다. 그리고 `path` Props를 사용하여, 해당 페이지의 URL을 선언합니다. 마지막으로 자식 컴포넌트로 해당 URL의 페이지 컴포넌트를 추가합니다.

이렇게 사용하면, 각각의 URL에 맞는 페이지를 표시할 수 있습니다. 만약, 페이지 URL에 동적인 데이터가 포함되어 있다면, `/detail/:id`와 같이 선언하여 사용해야 합니다.

```js
<div>
  <header>This is header</header>
  <Switch>
    ...
  </Switch>
</div>
```

URL에 따라 변경되는 부분은 Switch의 하위입니다. Switch에 밖에서 사용된 `<header/>`는 URL과 관계없이 항상 표시되게 됩니다.

### Link

그럼 Home 페이지 컴포넌트를 생성하면서 react-router의 링크 사용법을 확인해 봅시다. `./src/Pages/Home/index.tsx` 파일을 생성하고 다음과 같이 수정합니다.

```js
import { Link } from 'react-router-dom';

export const Home = () => {
  return (
    <div>
      <div>
        <Link to="/detail/1">Detail 1</Link>
      </div>
      <div>
        <Link to="/detail/2">Detail 2</Link>
      </div>
    </div>
  );
};
```

react-router에서 페이지 이동을 위한 링크는 `<a/>` 태그 대신 react-router가 제공하는 `<Link/>` 컴포넌트를 사용해야 합니다. 이 Link 컴포넌트는 `to`라는 Props를 가지고 있으며, 해당 Props에 이동하고자 하는 URL을 추가합니다.

{% include in-feed-ads.html %}

### useHistory와 useParams

다음으로 Detail 페이지 컴포넌트를 만들면서 `useHistory`와 `useParams` 훅을 사용하는 방법에 대해서 알아봅시다. `./src/Pages/Detail/index.tsx` 파일을 생성하고 다음과 같이 수정합니다.

```js
import { useHistory, useParams } from 'react-router-dom';

export const Detail = () => {
  const { goBack } = useHistory();
  const params: { id: string } = useParams();

  return (
    <div>
      <div>Detail {params.id}</div>
      <button onClick={goBack}>GoBack</button>
    </div>
  );
};
```

react-router의 `useHistory` 훅을 사용하면, 프로그래밍으로 페이지를 이동할 수 있습니다. `useHistory`는 `replace`, `push` 그리고 `goBack`을 제공하고 있습니다.

- replace: 현재 페이지를 주어진 URL 페이지로 교체. 브라우저의 돌아가기 버튼을 사용하여 이전 페이지로 돌아갈 수 없음.
- push: 주어진 URL 페이지로 이동. 브라우저의 돌아가기 버튼을 통해 이전 페이지로 돌아갈 수 있음.
- goBack: 브라우저의 돌아가기 버튼과 동일한 기능을 수행함

react-router의 `useParams`는 URL을 통해 전달한 동적 데이터를 받아서 사용할 수 있도록 도와줍니다. 우리는 Detail 페이지 컴포넌트를 다음과 같이 URL과 연결하였습니다.

```js
<Route path="/detail/:id">
  <Detail />
</Route>
```

그리고 Home 페이지 컴포넌트에서 다음과 같이 URL에 데이터를 할당하였습니다.

```js
<div>
  <Link to="/detail/1">Detail 1</Link>
</div>
<div>
  <Link to="/detail/2">Detail 2</Link>
</div>
```

이때, `1`, `2`는 `:id`에 할당이 됩니다. `useParams`를 사용하면 `:id`에 할당된 값을 사용할 수 있습니다.

```js
const params: { id: string } = useParams();
...
<div>Detail {params.id}</div>
```

## 완료

이것으로 React에서 페이지 전환을 하기 위해 react-router를 설치하고 사용하는 방법에 대해서 살펴보았습니다. react-router는 이 블로그에서 소개한 기능 이외에도 많은 기능을 가지고 있습니다. 이 블로그에서 소개한 기능 이외에 기능에 대해 궁금하신 분들은 꼭 공식 홈페이지를 참고해 보시기 바랍니다.

- React Router 공식 사이트: [Quick Start](https://reactrouter.com/web/guides/quick-start){:rel="noopener" target="_blank"}
