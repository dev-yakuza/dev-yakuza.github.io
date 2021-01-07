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

{% include in-feed-ads.html %}

### App 컴포넌트

그럼 위에서 생성한 Button 컴포넌트를 사용하여 카운터 앱을 생성해 봅시다. `./src/App.tsx` 파일을 열고 다음과 같이 수정한다.

```js
import React, { useState } from "react";
import Styled from "styled-components";

import { Button } from "Components/Button";

const Container = Styled.div`
  display: flex;
  min-height: 100vh;
  align-items: center;
  justify-content: center;
  background-color: #F5F5F5;
`;

const Label = Styled.div`
  margin: 10px;
  width: 40px;
  text-align: center;
`;

function App() {
  const [count, setCount] = useState(0);
  return (
    <Container>
      <Button
        label="-"
        backgroundColor="#FF1744"
        onClick={() => setCount(count - 1)}
      />
      <Label>{count}</Label>
      <Button
        label="+"
        backgroundColor="#304FFE"
        onClick={() => setCount(count + 1)}
      />
    </Container>
  );
}

export default App;
```

이렇게 만든 카운터 앱이 잘 동작하는지 확인해 보자. 다음 명령어를 실행하여 카운터 앱을 실행한다.

```bash
npm start
```

문제없이 실행되었다면, 브라우저에서 다음과 같은 화면을 확인할 수 있다.

![create-react-app with typescript](/assets/images/category/react/create-react-app/root-imprt/project.jpg)

{% include in-feed-ads.html %}

## 테스트

이제 이렇게 개발한 카운터 앱을 Jest와 react-testing-library를 사용하여 테스트 해보자. 우선 기존의 `./src/App.test.tsx` 파일을 삭제하도록 한다. 그리고 다음 명령어를 실행하여 Jest를 실행한다.

```bash
npm run test
```

### Button 컴포넌트의 테스트

우선 Button 컴포넌트를 테스트해 보자. Button 컴포넌트를 테스트하기 위해 `./src/Components/Button/index.tsx` 파일을 만들고 다음과 같이 수정한다.

```js
import React from 'react';
import { render, screen } from '@testing-library/react';
import 'jest-styled-components';

import { Button } from './index';

describe('<Button />', () => {
  it('renders component correctly', () => {
    const { container } = render(<Button label="button" />);

    const button = screen.getByText('button');
    expect(button).toBeInTheDocument();

    expect(container).toMatchSnapshot();
  });
});
```

일단 리액트를 테스트 하므로 리액트 라이브러리를 불러올 필요가 있다.

```js
import React from 'react';
```

우리는 react-testing-library의 `render`와 `screen`을 사용하여 테스트를 진행할 예정이다.

```js
import { render, screen } from '@testing-library/react';
```

우리는 컴포넌트를 디자인할 때 `styled-compontents`를 사용하고 있다. 이를 테스트하기 위한 라이브러리를 추가했다.

```js
import 'jest-styled-components';
```

다음으로 우리가 테스트하려는 Button 컴포넌트를 불러왔으며, Jest의 `describe`와 `it`을 사용하여 테스트 코드를 작성을 준비했다.

```js
import { Button } from './index';

describe('<Button />', () => {
  it('renders component correctly', () => {
    ...
  });
});
```

우선, 우리가 만든 Button 컴포넌트가 화면에 잘 표시되는지 확인하기 위해, react-testing-library를 사용하여 렌더링하였다.

```js
const { container } = render(<Button label="button" />);
```

이렇게 react-testing-library의 render를 사용하여 테스트하고자 하는 컴포넌트를 렌더링하면, 그 결과값으로 테스트에 도움을 주는 오브젝트를 반환한다. 우리는 여기서 스냅샷 테스트를 위해 `container`를 할당 받았다.

Button 컴포넌트를 화면에 표시하기 위해서는 필수 Props인 `label`을 설정할 필요가 있다. 이렇게 설정한 `label`은 버튼과 함께 화면에 표시되므로, 우리는 이 `label`의 텍스트를 화면에서 찾고, 화면에 존재하는지 확인해야 한다.

```js
const button = screen.getByText('button');
expect(button).toBeInTheDocument();
```

이를 위해서 react-testing-library의 `screen.getByText`를 사용하여 화면에서, 우리가 `label`를 통해 전달한 텍스트로 컴포넌트를 찾고, 해당 컴포넌트가 화면에 표시되었는지 `toBeInTheDocument`으로 확인하였다.

마지막으로 `toMatchSnapshot`을 통해 스냅샷을 저장하였다.

```js
expect(container).toMatchSnapshot();
```

이렇게 저장한 스냅샷은 어떤 변경이 화면에 영향이 있는지 알려주는 역할을 할 것이다.

이렇게 파일을 수정하고 저장하면, 앞에서 실행한 `npm run test`에 의해, 자동으로 테스트 코드가 실행되며, 다음과 같은 결과를 확인할 수 있다.

```bash
 PASS  src/Components/Button/index.test.tsx
  <Button />
    ✓ renders component correctly (27 ms)

Test Suites: 1 passed, 1 total
Tests:       1 passed, 1 total
Snapshots:   1 passed, 1 total
Time:        2.46 s
```

{% include in-feed-ads.html %}

그럼 이제 Button 컴포넌트의 다른 Props들을 테스트해 보자. Button 컴포넌트의 필수가 아닌 Props인 `backgroundColor`를 테스트하기 위해 다음과 같은 내용을 추가한다.

```js
it('renders component with backgroundColor', () => {
  render(<Button label="button" backgroundColor="#FF1744" />);

  const button = screen.getByText('button');
  expect(button).toHaveStyleRule('background-color', '#FF1744');
});
```

우선 `backgroundColor`를 설정한 Button 컴포넌트를 화면에 표시하였다.

```js
render(<Button label="button" backgroundColor="#FF1744" />);
```

이후 Button 컴포넌트의 `label`로 화면에 표시된 Button 컴포넌트를 찾고 `jest-styled-components`에서 제공하는 `toHaveStyleRule`을 사용하여 해당 스타일을 잘 가지고 있는지 확인하였다.

```js
const button = screen.getByText('button');
expect(button).toHaveStyleRule('background-color', '#FF1744');
```

이렇게 파일을 수정하고 저장하면, 앞에서 실행한 `npm run test`에 의해, 자동으로 테스트 코드가 실행되며, 다음과 같은 결과를 확인할 수 있다.

```bash
 PASS  src/Components/Button/index.test.tsx
  <Button />
    ✓ renders component correctly (33 ms)
    ✓ renders component with backgroundColor (6 ms)

Test Suites: 1 passed, 1 total
Tests:       2 passed, 2 total
Snapshots:   1 passed, 1 total
Time:        3.669 s
Ran all test suites.
```

{% include in-feed-ads.html %}

마지막으로, Button 컴포넌트의 클릭 이벤트를 테스트해 보자. Button 컴포넌트의 클릭 이벤트를 테스트하기 위해 다음과 같은 내용을 추가한다.

```js
import { render, screen, fireEvent } from '@testing-library/react';
...
it('clicks', () => {
  const onClick = jest.fn();
  render(<Button label="button" onClick={onClick} />);

  expect(onClick).toHaveBeenCalledTimes(0);
  const button = screen.getByText('button');
  fireEvent.click(button);
  expect(onClick).toHaveBeenCalledTimes(1);
});
```

사용자의 이벤트를 테스트하기 위해서는, react-testing-library가 제공하는 `fireEvent`를 사용할 필요가 있다.

```js
import { render, screen, fireEvent } from '@testing-library/react';
```

그리고 실제 이벤트가 발생하였을 때, 그 이벤트를 처리하는 함수에 Jest의 `Mock Function`을 적용한다.

```js
const onClick = jest.fn();
render(<Button label="button" onClick={onClick} />);
```

이렇게 적용된 `Mock Function`은 사용자의 클릭 이벤트가 발생할 시, 호출되는 카운트를 체크함으로써 실제 클릭이 발생되었는지 알 수 있다. 처음에는 클릭 이벤트가 발생하지 않은 상태이므로 해당 함수의 호출 카운트는 `0`이 된다.

```js
expect(onClick).toHaveBeenCalledTimes(0);
```

이제 실제로 react-testing-library의 `fireEvent`를 사용하여 Button 컴포넌트를 클릭해 보고, 해당 함수의 호출 카운트가 증가했는지 확인해 본다.

```js
const button = screen.getByText('button');
fireEvent.click(button);
expect(onClick).toHaveBeenCalledTimes(1);
```

이렇게 파일을 수정하고 저장하면, 앞에서 실행한 `npm run test`에 의해, 자동으로 테스트 코드가 실행되며, 다음과 같은 결과를 확인할 수 있다.

```bash
 PASS  src/Components/Button/index.test.tsx
  <Button />
    ✓ renders component correctly (27 ms)
    ✓ renders component with backgroundColor (4 ms)
    ✓ clicks (7 ms)

Test Suites: 1 passed, 1 total
Tests:       3 passed, 3 total
Snapshots:   1 passed, 1 total
Time:        3.634 s
Ran all test suites.
```

이것으로 우리가 만든 Button 컴포넌트에 관한 모든 테스트 코드를 작성하였다.

{% include in-feed-ads.html %}

### App 컴포넌트의 테스트

이제 App 컴포넌트를 테스트해 보자. App 컴포넌트는 Button 컴포넌트와 다르게 Props가 없으며, 대신 State를 사용하여 동적 데이터를 관리하고 있다.

그럼 App 컴포넌트를 테스트하기 위해 `./src/App.test.tsx` 파일을 생성하고 다음과 같이 수정한다.

```js

import React from 'react';
import { render, screen } from '@testing-library/react';
import 'jest-styled-components';

import App from './App';

describe('<App />', () => {
  it('renders component correctly', () => {
    const { container } = render(<App />);

    const minusButton = screen.getByText('-');
    expect(minusButton).toBeInTheDocument();
    expect(minusButton).toHaveStyleRule('background-color', '#FF1744');
    const plusButton = screen.getByText('+');
    expect(plusButton).toBeInTheDocument();
    expect(plusButton).toHaveStyleRule('background-color', '#304FFE');
    const label = screen.getByText('0');
    expect(label).toBeInTheDocument();

    expect(container).toMatchSnapshot();
  });
});
```

Button 컴포넌트에서 설명한 내용은 생략하고 진행하도록 하겠다. 우선 Button 컴포넌트와 동일하게 우선 App 컴포넌트가 화면에 잘 표시되는지 확인하는 테스트 코드를 작성하였다. App 컴포넌트는 `label`과 `backgroundColor`가 다른 두 개의 Button 컴포넌트와 카운트를 표시하는 컴포넌트를 가지고 있다. 카운트는 초기값이 `0`이므로 화면에 `0`이 표시되어있는지를 통해 카운트를 표시하는 컴포넌트가 표시되었는지 확인하였다.

```js
const minusButton = screen.getByText('-');
expect(minusButton).toBeInTheDocument();
expect(minusButton).toHaveStyleRule('background-color', '#FF1744');

const plusButton = screen.getByText('+');
expect(plusButton).toBeInTheDocument();
expect(plusButton).toHaveStyleRule('background-color', '#304FFE');

const label = screen.getByText('0');
expect(label).toBeInTheDocument();
```

이렇게 파일을 수정하고 저장하면, 앞에서 실행한 `npm run test`에 의해, 자동으로 테스트 코드가 실행되며, 다음과 같은 결과를 확인할 수 있다.

```bash
 PASS  src/App.test.tsx
  <App />
    ✓ renders component correctly (34 ms)

 › 1 snapshot written.
Snapshot Summary
 › 1 snapshot written from 1 test suite.

Test Suites: 1 passed, 1 total
Tests:       1 passed, 1 total
Snapshots:   1 written, 1 total
Time:        3.316 s
```

그럼 이제, 화면에 마이너스 버튼을 클릭하여 State를 통해 화면에 표시된 카운트 값을 변경해 보자. 마이너스 버튼을 클릭하는 테스트를 하기 위해 다음과 같은 내용을 추가한다.

```js
import { render, screen, fireEvent } from '@testing-library/react';
...
it('clicks minus button', () => {
  render(<App />);

  const minusButton = screen.getByText('-');
  const label = screen.getByText('0');
  expect(label).toBeInTheDocument();

  fireEvent.click(minusButton);
  expect(label.textContent).toBe("-1");
  fireEvent.click(minusButton);
  expect(label.textContent).toBe("-2");
});
```

앞에서 Button 컴포넌트를 테스트하는 방법과 동일하게 `fireEvent`를 사용하여 버튼을 클릭하였고, 화면에 표시된 값이 제대로 변경되는지 테스트하였다.

이렇게 파일을 수정하고 저장하면, 앞에서 실행한 `npm run test`에 의해, 자동으로 테스트 코드가 실행되며, 다음과 같은 결과를 확인할 수 있다.

```bash
 PASS  src/App.test.tsx
  <App />
    ✓ renders component correctly (43 ms)
    ✓ clicks minus button (17 ms)

Test Suites: 1 passed, 1 total
Tests:       2 passed, 2 total
Snapshots:   1 passed, 1 total
Time:        3.82 s
```

{% include in-feed-ads.html %}

마이너스 버튼과 동일하게 플러스 버튼도 테스트해 보자. 플러스 버튼을 테스트하기 위해 다음과 같은 내용을 추가한다.

```js
it('clicks plus button', () => {
  render(<App />);

  const plusButton = screen.getByText('+');
  const label = screen.getByText('0');
  expect(label).toBeInTheDocument();

  fireEvent.click(plusButton);
  expect(label.textContent).toBe("1");
  fireEvent.click(plusButton);
  expect(label.textContent).toBe("2");
});
```

플러스 버튼 테스트도 마이너스 버튼 테스트와 동일하게, 화면에 표시된 플러스 버튼을 클릭해 보고, 화면에 표시된 값이 제대로 변경되는지 테스트해보았다.

이렇게 파일을 수정하고 저장하면, 앞에서 실행한 `npm run test`에 의해, 자동으로 테스트 코드가 실행되며, 다음과 같은 결과를 확인할 수 있다.

```bash
 PASS  src/App.test.tsx
  <App />
    ✓ renders component correctly (36 ms)
    ✓ clicks minus button (14 ms)
    ✓ clicks plus button (8 ms)

Test Suites: 1 passed, 1 total
Tests:       3 passed, 3 total
Snapshots:   1 passed, 1 total
Time:        3.705 s
```

이것으로 우리가 개발한 카운터 앱을 모두 테스트해보았다. 또한 모든 테스트가 정상 동작하는 것을 확인할 수 있었다.

## 코드 커버리지

그럼 현재 실행중인 명령어를 취소하고, 다음 명령어를 실행하여 코드 커버리지를 확인해 보자

```bash
npm run test -- --coverage
```

이렇게 명령어를 실행하며 다음과 같이 모든 코드에 대한 테스트 코드가 잘 작성된 것을 확인할 수 있다.

```bash
 PASS  src/Components/Button/index.test.tsx
 PASS  src/App.test.tsx
----------|---------|----------|---------|---------|-------------------
File      | % Stmts | % Branch | % Funcs | % Lines | Uncovered Line #s
----------|---------|----------|---------|---------|-------------------
All files |     100 |      100 |     100 |     100 |
 App.tsx  |     100 |      100 |     100 |     100 |
----------|---------|----------|---------|---------|-------------------

Test Suites: 2 passed, 2 total
Tests:       6 passed, 6 total
Snapshots:   2 passed, 2 total
Time:        2.752 s, estimated 3 s
```

## 완료

이것으로 create-react-app으로 생성한 리액트 프로젝트를 Jest와 create-react-app으로 테스트하는 방법에 대해서 알아보았다. 여기서 작성한 테스트 코드가 정답은 아니며, 여러 방법으로 같은 동일한 테스트 코드를 작성할 수 있다.

또한, 테스트 커버리지를 통해 우리가 작성한 테스트 코드가 모든 테스트를 커버하는 것을 확인할 수 있었다. 하지만 코드 커버리지는 어디까지나 확인용이므로, 100%로 신뢰하지 않도록 주의하자. 테스트 커버리지가 100%라고 해서 현재 만든 앱에 버그가 없고, 내가 만든 테스트 코드가 모든 테스트 케이스를 테스트하고 있다고 착각하지 않도록 주의하자.
