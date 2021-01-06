---
layout: 'post'
permalink: '/react/create-react-app/react-testing-library/'
paginate_path: '/react/:num/create-react-app/react-testing-library/'
lang: 'ko'
categories: 'react'
comments: true

title: 'create-react-app에서 react-testing-library로 테스트하기'
description: 'create-react-app로 생성한 React 프로젝트에서 react-testing-library를 사용하여 테스트하는 방법에 대해서 알아봅시다.'
image: '/assets/images/category/react/create-react-app/typescript/background.jpg'
published: false
---

<div id="contents_list" markdown="1">

## 목차

</div>

## create-react-app 시리즈

이 블로그 포스트는 시리즈로 제작되었습니다. 다음은 `create-react-app`의 시리즈 리스트입니다.

- [React란]({{site.url}}/{{page.categories}}/create-react-app/react/){:target="_blank"}
- [create-react-app]({{site.url}}/{{page.categories}}/create-react-app/start/){:target="_blank"}
- [create-react-app에서 TypeScript]({{site.url}}/{{page.categories}}/create-react-app/typescript/){:target="_blank"}
- [Jest]({{site.url}}/{{page.categories}}/create-react-app/jest/){:target="_blank"}
- create-react-app에서 react-testing-library로 테스트하기

## 개요

이전 블로그에서 자바스크립트 테스트 프레임워크인 `Jest`를 사용하여 테스트의 기초와 자바스크립트에 대한 테스트에 대해서 알아보았습니다. 이번 블로그 포스트에서는 `create-react-app`으로 생성한 React 프로젝트를 테스트하기 위한 `react-testing-library`에 대해서 알아보겠습니다.

여기서 소개한 소스코드는 아래에 링크를 통해 확인할 수 있습니다.

- GitHub: [https://github.com/dev-yakuza/study-create-react-app/tree/main/6.react-test](https://github.com/dev-yakuza/study-create-react-app/tree/main/6.react-test){:rel="noopener" target="_blank"}

## react-testing-library

이전 블로그에서 소개한 `Jest`는 자바스크립트 테스트 프레임워크로써, 자바스크립트의 전반적인 테스트에 사용됩니다. 이번에 소개해 드릴 `react-testing-library`는 React를 테스트하기 위해 최적화된 라이브러리입니다.

- react-testing-library: [https://testing-library.com/docs/react-testing-library/intro/](https://testing-library.com/docs/react-testing-library/intro/){:rel="noopener" target="_blank"}

create-reate-app으로 React 프로젝트를 생성하면, `Jest`와 마찬가지로 `react-testing-library`도 함께 설치됩니다. 그러므로 특별한 설치없이 바로 `react-testing-library`를 사용할 수 있습니다.

이번 블로그 포스트에서는 예제를 통해 react-testing-library를 사용하는 방법에 대해서 알아보겠습니다.

{% include in-feed-ads.html %}

![create-react-app with typescript](/assets/images/category/react/create-react-app/root-imprt/project.jpg)

## 카운터 앱 개발

간단한 예제를 통해 react-testing-library를 사용법을 알아보기 위해 React 프로젝트를 준비해 봅시다. 이번 블로그에서는 아래와 같은 카운터 앱을 만들 예정입니다.

![Counter app](/assets/images/category/react/create-react-app/react-testing-library/counter.jpg)

다음 명령어를 통해 타입스크립트가 적용된 React 프로젝트를 생성합니다.

```bash
npx create-react-app react-test --template=typescript
```

그리고 절대 경로로 컴포넌트를 추가할 수 있게 하기 위해 `tsconfig.json` 파일을 열고 다음과 같이 수정합니다.

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

그리고 React 프로젝트에서 `styled-components`를 사용하기 위해, 다음 명령어를 통해 `styled-components`을 설치합니다.

```bash
npm install --save styled-components
npm install --save-dev @types/styled-components jest-styled-components
```

### Button 컴포넌트

이제 카운터 앱에서 값을 더하거나 빼기 위해 사용되는 버튼 컴포넌트를 만들어 봅시다. 버튼 컴포넌트를 만들기 위해 `./src/Components/Button/index.tsx` 파일을 생성하고 다음과 같이 수정합니다.

```js
import React from "react";
import Styled from "styled-components";

interface ContainerProps {
  readonly backgroundColor?: string;
}

const Container = Styled.div<ContainerProps>`
  padding: 10px 15px;
  border-radius: 5px;
  background-color: ${(props) => props.backgroundColor};
  color: white;
  font-weight: bold;
  cursor: pointer;
`;

interface Props {
  readonly label: string;
  readonly backgroundColor?: string;
  readonly onClick?: () => void;
}
export const Button = ({ label, backgroundColor, onClick }: Props) => {
  return (
    <Container backgroundColor={backgroundColor} onClick={onClick}>
      {label}
    </Container>
  );
};
```

이번 블로그에서는 react-testing-library를 사용하는 방법에 대한 블로그이기 때문에, React 컴포넌트를 제작하는 방법에 대해서는 설명을 생략하도록 하겠습니다.

### App 컴포넌트

그럼 위에서 생성한 Button 컴포넌트를 사용하여 카운터 앱을 생성해 봅시다.

## 테스트

### Button 컴포넌트의 테스트

### App 컴포넌트의 테스트


## 완료

이것으로 create-react-app으로 타입스크립트가 적용된 React 프로젝트에 절대 경로로 컴포넌트를 추가하는 방법에 대해서 알아보았다. 프로젝트 초반에는 큰 장점을 느끼지 못하지만, 프로젝트가 점점 커지면, 정말 편리하다고 느끼게 될 것이다.
