---
layout: 'post'
permalink: '/react/context-api/'
paginate_path: '/react/:num/context-api/'
lang: 'ko'
categories: 'react'
comments: true

title: '[React] Context API'
description: 'React에서 데이터를 다루는 개념중 하나인 Context API를 사용하는 방법에 대해서 알아봅시다..'
image: '/assets/images/category/react/background.jpg'
published: false
---

<div id="contents_list" markdown="1">

## 목차

</div>

## 개요

React에서 컴포넌트가 데이터를 다루는 방법으로 `Props`, `State` 그리고 `Context`  있습니다. 이번 블로그 포스트에서는 Context에 관한 개념을 정리해 보도록 하겠습니다.

React에서 Props와 State 개념과 사용 방법에 대해서는 아래에 링크를 참고하시기 바랍니다.

- [[React] Props와 State]({{site.url}}/{{page.categories}}/props-state/){:target="_blank"}

## Context

React에서 Props와 State는 부모 컴포넌트와 자식 컴포넌트 또는 한 컴포넌트 안에서 데 이터를 다루기 위해 사용됩니다. 이 Props와 State를 사용하게 되면 부모 컴포넌트에서 자식 컴포넌트, 즉, 위에서 아래, 한쪽으로 데이터가 흐르게 됩니다.

![React data flow with Props](/assets/images/category/react/2021/context-api/react-data-flow.png)

만약 다른 컴포넌트에서 한쪽으로 흐르고 있는 데이터를 사용하고 싶은 경우 또는 다른 컴포넌트에서 사용하고 있는 데이터를 현재의 데이터 흐름에 넣고 싶은 경우가 발생한다면 어떻게 해야할까요?

![React need data in another data flow](/assets/images/category/react/2021/context-api/react-data-flow-another-component.png)

React에서 데이터는 위에서 아래로 흐르게 되므로 사용하고 싶은 데이터와 이 데이터를 사용할 컴포넌트의 공통 부모 컴포넌트에 State를 만들고 사용하고자 하는 데이터를 Props를 전달하면 이 문제를 해결할 수 있습니다.

![React global data with props and state](/assets/images/category/react/2021/context-api/global-data-use-props.png)

하지만 이처럼 컴포넌트 사이에 공유되는 데이터를 위해 매번 공통 부모 컴포넌트를 수정하고 하위 모든 컴포넌트에 데이터를 Props로 전달하는 것은 매우 비효율적입니다. 이와 같은 문제를 해결하기 위해 React에서는 `Flux`라는 개념을 도입하였고 그에 걸맞은 `Context API`를 제공하기 시작했습니다.

- React 공식 사이트: [Context](https://reactjs.org/docs/context.html#consuming-multiple-contexts){:rel="noopener" target="_blank"}

Context는 부모 컴포넌트로부터 자식 컴포넌트로 전달되는 데이터의 흐름과는 상관없이 전역적인 데이터를 다룰 때 사용합니다. 전역 데이터를 Context에 저장한 후 필요한 컴포넌트에서 해당 데이터를 불러와 사용할 수 있습니다.

![React context](/assets/images/category/react/2021/context-api/context.png)

React에서 Context를 사용하기 위해서는 Context API를 사용해야 하며, Context의 `Provider`와 `Consumer`를 사용해야 합니다.

![React context with Provider and Consumer](/assets/images/category/react/2021/context-api/context.png)

Context에 저장된 데이터를 사용하기 위해서는 공통 부모 컴포넌트에 Context의 Provider를 사용하여 데이터를 제공해야 하며, 데이터를 사용하려는 컴포넌트에서 Context의 Consumer를 사용하여 실제로 데이터를 사용합니다.

{% include in-feed-ads.html %}

## Context 사용법

그럼 이제 Context API를 사용하여 React에서 전역적인 데이터를 다루는 방법에 대해서 알아봅시다.

### 프로젝트 준비

다음 명령어를 사용하여 Context를 사용하기 위한 React 프로젝트를 생성합니다.

```bash
npx create-react-app context_example --template=typescript
```

### Context 생성

그럼 전역 데이터를 저장하기 위한 Context를 생성해 보도록 합시다. `./src/Contexts/Count/index.tsx` 파일을 열고 다음과 같이 수정합니다.

```js
import { createContext, useState } from 'react';

const CountContext = createContext({
  count: 0,
  plusCount: () => {},
});

interface Props {
  children: JSX.Element | JSX.Element[];
}

const CountProvider = ({ children }: Props): JSX.Element => {
  const [count, setCount] = useState(0);

  const plusCount = (): void => {
    setCount(count + 1);
  };

  return (
    <CountContext.Provider
      value={{
        count,
        plusCount,
      }}>
      {children}
    </CountContext.Provider>
  );
};

export { CountContext, CountProvider };
```

함수 컴포넌트에서 Context를 생성하기 위해서는 createContext 훅(Hook)을 사용해야 합니다. 또한 Context도 하나의 React 컴포넌트이므로, 컴포넌트안에서 변경 가능한 데이터를 다루기 위해 State를 사용해야 합니다.

```js
import { createContext, useState } from 'react';
```

이렇게 추가한 createContext를 사용하여 Context를 생성합니다.

```js
const CountContext = createContext({
  count: 0,
  plusCount: () => {},
});
```

Context도 하나의 React 컴포넌트이므로, 기본적으로 컴포넌트의 형태를 가지고 있습니다. 이때 화면에 표시될 내용에 Context의 Provider를 감싸서 제공합니다.

```js
...
const CountProvider = ({ children }: Props): JSX.Element => {
  ...
  return (
    <CountContext.Provider>
      {children}
    </CountContext.Provider>
  );
};

export { CountContext, CountProvider };
```

Context는 하나의 React 컴포넌트입니다. 따라서 내부적으로 변경 가능한 데이터를 사용하려면 useState를 사용하여 State를 사용해야 합니다.

```js
const CountProvider = ({ children }: Props): JSX.Element => {
  const [count, setCount] = useState(0);

  const plusCount = (): void => {
    setCount(count + 1);
  };
  ...
};
```

이렇게 만든 State를 Context의 Provider에 제공합니다.

```js
const CountProvider = ({ children }: Props): JSX.Element => {
  ...
  return (
    <CountContext.Provider
      value={{
        count,
        plusCount,
      }}>
      {children}
    </CountContext.Provider>
  );
};
```

마지막으로 createContext를 사용하여 생성한 Context와 Context의 Provider를 사용하여 만든 React 컴포넌트를 내보냅니다. Context의 Provider를 사용하여 만든 React 컴포넌트는 공통 부모 컴포넌트에 제공할 예정이며, createContext로 생성한 Context는 데이터를 소비할 때, 사용할 예정입니다.

```js
export { CountContext, CountProvider };
```

이것으로 전역 데이터를 다룰 Context를 생성하였습니다. 이제 이 Context를 사용하는 방법에 대해서 알아봅시다.

{% include in-feed-ads.html %}

### Provider

앞에서 만든 Context를 사용하기 위해, 공통 부모 컴포넌트인 `App` 컴포넌트에 Context의 Provider를 제공해 봅시다. Context의 Provider를 제공하기 위해, `./src/App.tsx` 파일을 열고 다음과 같이 수정합니다.

```js
import { CountProvider } from './Contexts/Count';

import { CountLabel } from './Components/CountLabel';
import { PlusButton } from './Components/PlusButton';

function App() {
  return (
    <CountProvider>
      <CountLabel />
      <PlusButton />
    </CountProvider>
  );
}

export default App;
```

Context를 사용하여 전역 데이터를 사용하려면 공통 부모 컴포넌트에 Context의 Provider를 사용해야 합니다. 여기서 사용한다는 의미는 Context의 Provider로 감싼다는 의미 입니다.

```js
import { CountProvider } from './Contexts/Count';
...
function App() {
  return (
    <CountProvider>
      ...
    </CountProvider>
  );
}

export default App;
```

이제 `CountProvider`로 감싼 부분에서는 Context 내부에 생성한 전역 데이터를 자유롭게 접근할 수 있게 됩니다.

```js
...
import { CountLabel } from './Components/CountLabel';
import { PlusButton } from './Components/PlusButton';

function App() {
  return (
    <CountProvider>
      <CountLabel />
      <PlusButton />
    </CountProvider>
  );
}
```

아직 Context를 사용하는 컴포넌트를 만들지 않아 에러가 발생합니다. 그럼 이제 Context를 사용하는 `CountLabel` 컴포넌트와 `PlusButton` 컴포넌트를 만들어 봅시다.

### Consumer

Context를 사용하여 전역 데이터를 사용할 컴포넌트를 제작해 봅시다. 우선 `./src/Components/CountLabel/index.tsx` 파일을 생성하고 다음과 같이 수정합니다.

```js
import { useContext } from 'react';
import { CountContext } from '../../Contexts/Count';

export const CountLabel = () => {
  const { count } = useContext(CountContext);
  return <div>{count}</div>;
};
```

CountLabel은 단순히 카운트를 화면에 표시하는 컴포넌트입니다. 여기서 표시할 카운트는 전역 변수로써, Context에 선언된 값을 사용할 예정입니다. 이렇게 Context에 선언된 값을 사용할 때, React의 클래스 컴포넌트에서 `Consumer`를 사용하였지만, 함수 컴포넌트에서는 `useContext` 훅을 사용하게 됩니다.

useContext 훅에 우리가 만든 Context인 CountContext를 파라메터로 전달하면, createContext로 생성한 값들에 접근이 가능합니다.

```js
const CountContext = createContext({
  count: 0,
  plusCount: () => {},
});
```

CountLabel에서는 Context의 count 변수만을 사용하였습니다.

{% include in-feed-ads.html %}

다음으로 Context의 count 변수값을 올리기 위해 `PlusButton` 컴포넌트를 생성해 봅시다. `./src/Components/PlusButton/index.tsx` 파일을 생성하고 다음과 같이 수정합니다.

```js
import { useContext } from 'react';
import { CountContext } from '../../Contexts/Count';

export const PlusButton = () => {
  const { plusCount } = useContext(CountContext);

  return <button onClick={plusCount}>+ 1</button>;
};
```

PlusButton은 화면에 단순히 `+ 1`이라는 버튼을 표시하고, 해당 버튼을 눌렀을 때, Context의 count값을 증가시키는 함수인 `plusCount` 함수를 호출하는 컴포넌트입니다.

CountLabel과 마찬가지로 useContext 훅과 우리가 만든 Context를 사용하여, 전역 데이터인 count를 증가시키는 `plusCount` 함수를 가져왔으며, 이렇게 가져온 함수를 버튼의 `onClick` 이벤트에 연결하였습니다.

### 확인

Context를 활용하여 전역 데이터를 다루는 예제를 모두 만들어 보았습니다. 이제 이렇게 생성한 React 프로젝트를 확인하기 위해, 다음 명령어를 사용하여 React 프로젝트를 실행합니다.

```bash
npm start
```

React 프로젝트가 실행되면 다음과 같이 `0`과 `+ 1` 버튼을 확인할 수 있습니다.

![React Context example: Count](/assets/images/category/react/2021/context-api/count.npg)

`+ 1` 버튼을 누르면, 다음과 같이 카운트가 증가되는 것을 확인할 수 있습니다.

![React Context example: Count increased](/assets/images/category/react/2021/context-api/count_increased.jpg)

## 완료

이것으로 React에서 컴포넌트가 전역 데이터를 다루는 방법인 Context에 대해 간단히 살펴보았습니다. 이제 컴포넌트 사이의 데이터를 공유할 때, Context를 사용하여 좀 더 효율적으로 공유해 보시기 바랍니다.
