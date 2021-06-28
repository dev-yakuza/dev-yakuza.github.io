---
layout: 'post'
permalink: '/react/props-state/'
paginate_path: '/react/:num/props-state/'
lang: 'ko'
categories: 'react'
comments: true

title: '[React] Props와 State'
description: 'React에서 데이터를 다루는 주요 개념인 Props와 State가 무엇인지 알아보고, 사용하는 방법에 대해서 살펴봅시다.'
image: '/assets/images/category/react/background.jpg'
published: false
---

<div id="contents_list" markdown="1">

## 목차

</div>

## 개요

React에서 컴포넌트가 데이터를 다루는 방법으로 `Props`, `State` 그리고 `Context`가 있습니다. 이번 블로그 포스트에서는 Porps와 State에 관한 개념을 정리해 보도록 하겠습니다.

React에서 Context를 다루기 위해 Context API를 사용하는 방법에 대해서는 아래에 링크를 참고하시기 바랍니다.

- [[React] Context API]({{site.url}}/{{page.categories}}/context-api/){:target="_blank"}

## Props

Props(Properties)는 부모 컴포넌트에서 자식 컴포넌트로 전달되는 데이터를 말합니다. 부모 컴포넌트로부터 받는 데이터이므로 자식 컴포넌트에서는 변경할 수 없습니다. 이는 한 컴포넌트의 속성(Properties)과 같음을 의미합니다.

- React 공식 사이트: [Components and Props](https://reactjs.org/docs/components-and-props.html){:rel="noopener" target="_blank"}

이미 우리는 HTML을 다루면서 속성에 대한 개념을 사용하고 있습니다.

```html
<div id="name" class="label" onclick="alert('Hello World!');">
  Hello world!
</div>
```

위의 코드는 HTML의 div 태그에 id와 class 속성을 설정하고 onclick 속성에 직접 자바스크립트의 alert 코드를 사용하였습니다. 이처럼 우리는 이미 HTML의 속성이라는 개념을 사용 해 왔습니다. React에서는 이 속성 개념에 데이터를 전달한다는 개념을 추가 확장한 것입니다.

```js
const Text = ({text}) => {
  return <div>{text}</div>
}

const App = () => {
  return <Text text='Hello world!'/>
}
```

위와 같이 부모 컴포넌트(App)에서 자식 컴포넌트(Text)에 속성(Props)을 이용하여 `Hello world!`라는 문자열 데이터를 전달하는 것을 확인할 수 있습니다.

{% include in-feed-ads.html %}

## State

State는 한 컴포넌트 안에서 유동적인 데이터를 다룰 때 사용되며, 컴포넌트 안에서 데이터를 변경할 수 있습니다. 즉, State는 한 컴포넌트의 상태(State)를 나타냅니다.

- React 공식 사이트: [State and Lifecycle](https://reactjs.org/docs/state-and-lifecycle.html){:rel="noopener" target="_blank"}

다음 예제는 `+` 버튼을 누르면, 화면에 표시된 값을 1 증가 시키는 코드입니다.

```js
import React, { useState } from 'react';

const Text = ({text}) => {
  return <div>{text}</div>
}

const App = () => {
  const [count, setCount] = useState(0);

  return <div>
    <Text text={count} />
    <div onClick={() => setCount(count + 1)}>+</div>
  </div>
}
```

React의 함수 컴포넌트에서는 State를 사용하기 위해 useState라는 훅(Hook)을 사용해야 합니다. useState는 State 변수의 초기값을 매개변수로 전달 하여 호출하며, 결과값으로는 배열을 반환하게 됩니다. 반환된 배열에서는 useState 함수를 호출할 때 설정한 초기값이 할당된 변수와 해당 변수를 수정하기 위한 Set 함수가 포함되어 있습니다.

```js
const 배열 = useState (데이터 초기값);
```

- 배열[0]: 데이터 초기값이 들어간 변수
- 배열[1]: 데이터를 수정할 수 있는 Set 함수

보통은 반환된 결과값을 자바스크립트의 구조 분해 할당(Destructuring assignment)을 통해 변수와 Set 함수를 할당하여 사용하게 됩니다.

```js
const [변수명, Set함수명] = useState (데이터 초기값);
```

useState를 사용하여 할당받은 변수는 불변값(Immutable)입니다. 따라서 해당 값은 직접 수정이 불가능하며 해당 값을 변경하기 위해서는 반드시 Set 함수를 사용해야 합니다.

```js
const App = () => {
  const [count, setCount] = useState(0);

  return <div>
    <Text text={count} />
    <div onClick={() => setCount(count + 1)}>+</div>
  </div>
}
```

## 완료

이것으로 React에서 컴포넌트가 데이터를 다루는 방법인 Props와 State에 대해 간단히 살펴보았습니다. React에서 하나의 컴포넌트는 컴포넌트의 속성을 나타내며, 변경이 불가능한 데이터인 Props와 컴포넌트 안에서 컴포넌트의 상태를 나타내며, 변경이 가능한 데이터인 State가 존재하는 것을 배웠습니다. 이제 여러분도 Props와 State를 사용하여 멋진 React 컴포넌트를 제작해 보시기 바랍니다.
