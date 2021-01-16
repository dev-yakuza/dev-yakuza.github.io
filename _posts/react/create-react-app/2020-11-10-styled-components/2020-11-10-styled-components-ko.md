---
layout: 'post'
permalink: '/react/create-react-app/styled-components/'
paginate_path: '/react/:num/create-react-app/styled-components/'
lang: 'ko'
categories: 'react'
comments: true

title: 'create-react-app에서 styled-components'
description: 'create-react-app으로 생성한 React 프로젝트에 styled-components를 적용하는 방법에 대해서 알아봅시다.'
image: '/assets/images/category/react/create-react-app/styled-components/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [프로젝트 생성](#프로젝트-생성)
- [styled-components 설치](#styled-components-설치)
- [사용법](#사용법)
- [완료](#완료)

</div>

## create-react-app 시리즈

이 블로그 포스트는 시리즈로 제작되었습니다. 다음은 `create-react-app`의 시리즈 리스트입니다.

- [create-react-app]({{site.url}}/{{page.categories}}/create-react-app/start/){:target="_blank"}
- [create-react-app에서 TypeScript]({{site.url}}/{{page.categories}}/create-react-app/typescript/){:target="_blank"}
- create-react-app에서 styled-components

## 개요

이번 블로그 포스트에서는 React 프로젝트에 `styled-components`를 적용하는 방법에 대해서 알아봅시다.

- styled-components: [https://styled-components.com/](https://styled-components.com/){:rel="noopener" target="_blank"}

이 블로그 포스트에서 사용하는 소스코드는 TypeScript가 적용된 소스 코드를 사용할 예정입니다.

여기서 소개한 소스코드는 아래에 링크를 통해 확인할 수 있습니다.

- GitHub: [https://github.com/dev-yakuza/study-create-react-app/tree/main/3.styled-components](https://github.com/dev-yakuza/study-create-react-app/tree/main/3.styled-components){:rel="noopener" target="_blank"}

## 프로젝트 생성

다음 명령어를 사용하여 React 프로젝트를 생성합니다.

```bash
npx create-react-app my-app --template=typescript
```

그리고 다음 명령어를 사용하여 React 프로젝트를 실행해 봅니다.

```bash
# cd my-app
npm start
```

문제없이 React 프로젝트가 실행되면 아래와 같은 화면을 브라우저에서 확인할 수 있습니다.

![create-react-app with styled-components](/assets/images/category/react/create-react-app/styled-components/project.jpg)

{% include in-feed-ads.html %}

## styled-components 설치

`create-react-app`으로 생성한 React 프로젝트에 `styled-components`를 적용하기 위해 필요한 라이브러리를 설치할 필요가 있습니다. 다음 명령어를 통해 `styled-components`에 필요한 라이브러리를 설치합니다.

```bash
npm install --save styled-components
```

그리고 저는 React 프로젝트에 TypeScript를 사용함으로, 다음 명령어를 통해 `styled-components`의 타입과 테스트에 필요한 라이브러리를 설치하였습니다.

```bash
npm install --save-dev @types/styled-components jest-styled-components
```

## 사용법

이제 `styled-components`를 사용하여 간단한 컴포넌트를 만들어 보겠습니다. `./src/App.tsx` 파일을 열고 다음과 같이 수정합니다.

```jsx
import React from 'react';
import Styled from 'styled-components';

const Container = Styled.div`
  background: red;
  width: 100%;
`;
const Label = Styled.div`
  color: white;
  padding: 20px;
`;

const App = () => {
  return (
    <Container>
      <Label>Hello World</Label>
    </Container>
  );
}

export default App;
```

위와 같이 `styled-components`를 사용하여 `JSX`에서 바로 스타일을 작성할 수 있습니다.

그리고 더이상 사용하지 않는 다음 파일들을 삭제합니다.

- App.css
- logo.svg

더 많은 사용법에 관해서는 공식 홈페이지를 참고하시기 바랍니다.

- styled-components basics: [https://styled-components.com/docs/basics](https://styled-components.com/docs/basics){:rel="noopener" target="_blank"}

## 완료

이번 블로그 포스트에서는 `create-react-app`으로 생성한 React 프로젝트에 `styled-components`를 적용하는 방법에 대해 알아보았습니다. 그리고 간단하게 JSX 파일에서 styled-components를 사용하는 방법에 대해서도 알아보았습니다.

이제 여러분도 JSX 파일에서 styled-components를 사용하여 스타일링 해 보시기 바랍니다.
