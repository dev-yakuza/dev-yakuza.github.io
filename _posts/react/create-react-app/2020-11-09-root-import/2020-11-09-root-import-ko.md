---
layout: 'post'
permalink: '/react/create-react-app/root-import/'
paginate_path: '/react/:num/create-react-app/root-import/'
lang: 'ko'
categories: 'react'
comments: true

title: '[타입스크립트] create-react-app에서 절대 경로 import'
description: 'create-react-app의 타입스크립트로 생성한 React 프로젝트에 절대 경로를 사용하여 컴포넌트를 추가하는 방법에 대해서 알아본다.'
image: '/assets/images/category/react/create-react-app/typescript/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [상대 경로와 절대 경로](#상대-경로와-절대-경로)
- [프로젝트 생성](#프로젝트-생성)
- [절대 경로 설정](#절대-경로-설정)
- [사용법](#사용법)
- [완료](#완료)

</div>

## create-react-app 시리즈

이 블로그 포스트는 시리즈로 제작되었습니다. 다음은 `create-react-app`의 시리즈 리스트입니다.

- [React란]({{site.url}}/{{page.categories}}/create-react-app/react/){:target="_blank"}
- [create-react-app]({{site.url}}/{{page.categories}}/create-react-app/start/){:target="_blank"}
- [create-react-app에서 TypeScript]({{site.url}}/{{page.categories}}/create-react-app/typescript/){:target="_blank"}
- [타입스크립트] create-react-app에서 절대 경로 import
- [create-react-app에서 styled-components]({{site.url}}/{{page.categories}}/create-react-app/styled-components/){:target="_blank"}

## 개요

이전 블로그에서 `create-react-app`을 사용하여 React 프로젝트에 타입스크립트를 적용하는 방법에 대해서 알아보았습니다. 이번 블로그 포스트에서는 타입스크립트가 적용된 React 프로젝트에서 컴포넌트를 추가할 때, 상대 경로가 아닌 절대 경로를 사용하여 컴포넌트를 추가하는 방법에 대해서 알아봅시다.

여기서 소개한 소스코드는 아래에 링크를 통해 확인할 수 있습니다.

- GitHub: [https://github.com/dev-yakuza/study-create-react-app/tree/main/3.root-import](https://github.com/dev-yakuza/study-create-react-app/tree/main/3.root-import){:rel="noopener" target="_blank"}

## 상대 경로와 절대 경로

React를 사용하여 프로젝트를 개발하면, 우리는 컴포넌트를 중심으로 앱을 개발하게 된다. React로 프로젝트를 개발하면, 우선 필요한 수많은 컴포넌트를 제작하고, 그 컴포넌트를 조합하여 페이지를 제작하게 된다.

이렇게 리액트 컴포넌트를 조합하여 페이지를 제작할 때, 보통은 상대 경로(`import Button from '../../Button'`)를 사용하여 컴포넌트를 불러오게 된다.

컴포넌트가 많지 않은 경우는 큰 불편함을 느끼지 못하지만, 프로젝트가 커지고 컴포넌트가 많아지고, 프로젝트의 폴더 구조가 점점 복잡해지면, 이 상대 경로 추가 방식은 어떤 경로로 컴포넌트를 지정해야하는지, 어떤 컴포넌트를 불러오는지 파악하기 어려운 단점이 있다.

이런 문제를 해결하고자, 이번 블로그 포스트에서는 절대 경로(`import Button from 'Button'`)로 컴포넌트를 추가하는 방법에 대해서 설명합니다.

{% include in-feed-ads.html %}

## 프로젝트 생성

다음 명령어를 사용하여 타입스크립트가 적용된 React 프로젝트를 생성합니다.

```bash
npx create-react-app root-import --template=typescript
```

그리고 다음 명령어를 사용하여 React 프로젝트를 실행해 봅니다.

```bash
# cd root-import
npm start
```

문제없이 React 프로젝트가 실행되면 아래와 같은 화면을 브라우저에서 확인할 수 있습니다.

![create-react-app with typescript](/assets/images/category/react/create-react-app/root-import/project.jpg)

## 절대 경로 설정

타입스크립트가 적용된 React 프로젝트에 절대 경로를 설정하는 방법은 간단하다. 타입스크립트의 설정만 수정하면 바로 컴포넌트를 절대 경로를 사용하여 추가할 수 있다.

그럼 절대 경로로 컴포넌트를 추가하기 위해 `tsconfig.json` 파일을 열고 다음과 같이 수정한다.

```json
{
  "compilerOptions": {
    ...
    "jsx": "react-jsx",
    "baseUrl": "src"
  },
  ...
}
```

이것으로 모든 설정이 끝났다. 정말 간단하다.

## 사용법

그럼 실제로 절대 경로로 컴포넌트를 추가해 보자. 우선, `./src/Components` 폴더를 만들고 `App.js`, `App.css`, `App.test.tsx`, `logo.svg` 파일을 `./src/Components` 폴더 로 이동시킨다.

그리고 `./src/index.js` 파일을 열고 다음과 같이 수정한다.

```js
...
import App from 'Components/App';
...
```

그리고 다음 명령어를 사용하여 React 프로젝트를 실행한다.

```bash
npm start
```

문제없이 설정하였다면, 다음과 같은 화면을 브라우저에서 확인할 수 있다.

![create-react-app with typescript](/assets/images/category/react/create-react-app/root-import/project.jpg)

현재는 React 프로젝트가 간단하기 때문에 절대 경로로 컴포넌트를 추가하는 것에 큰 장점이 없어보이지만, 앞으로 React로 프로젝트를 진행하다보면, 이 절대 경로 컴포넌트 추가가 빛을 발하는 것을 목격할 수 있을 것이다.

## 완료

이것으로 create-react-app으로 타입스크립트가 적용된 React 프로젝트에 절대 경로로 컴포넌트를 추가하는 방법에 대해서 알아보았다. 프로젝트 초반에는 큰 장점을 느끼지 못하지만, 프로젝트가 점점 커지면, 정말 편리하다고 느끼게 될 것이다.
