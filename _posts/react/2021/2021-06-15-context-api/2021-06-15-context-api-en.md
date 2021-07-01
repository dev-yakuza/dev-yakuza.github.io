---
layout: 'post'
permalink: '/react/context-api/'
paginate_path: '/react/:num/context-api/'
lang: 'en'
categories: 'react'
comments: true

title: '[React] Context API'
description: Let's see how to use Context API to manage the global data in React.
image: '/assets/images/category/react/background.jpg'
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [Context](#context)
- [How to use Context](#how-to-use-context)
  - [Prepare project](#prepare-project)
  - [Create Context](#create-context)
  - [Provider](#provider)
  - [Consumer](#consumer)
  - [Check](#check)
- [Completed](#completed)

</div>

## Outline

To manage the data in React, you can use `Props`, `State` and `Context`. In this blog post, I will introduce what Context is and How to use it.

If you want to know details about Props and State, see the link below.

- [[React] Props와 State]({{site.url}}/{{page.categories}}/props-state/){:target="_blank"}

You can see full source code of the blog post on the link below.

- GitHub: [context_example](https://github.com/dev-yakuza/study-create-react-app/tree/main/example/context_exmaple){:rel="noopener" target="_blank"}

## Context

In React, Props and State are used for managing the data from the parent component to the child component. When you use the Props and State, the data flows from the parent component and the child component, that is, from top to bottom and to one way.

![React data flow with Props](/assets/images/category/react/2021/context-api/react-data-flow.png)

What should you do if you want to use data flowing one direction or insert data that is used by another component into the current data flow?

![React need data in another data flow](/assets/images/category/react/2021/context-api/react-data-flow-another-component.png)

In React, the data flows from top to bottom, so to solve this problem, you can create State for data in the common parent component and pass the data via Props to the child component.

![React global data with props and state](/assets/images/category/react/2021/context-api/global-data-use-props.png)

However, It's very inefficient to create State and pass it by Props for every time when we need to share the data between components. To solve this issue, React introduces `Flux` concept and provide `Context API` for Flux.

- React official site: [Context](https://reactjs.org/docs/context.html#consuming-multiple-contexts){:rel="noopener" target="_blank"}

Context is used to handle global data regardless of the data flow passed from the parent component to the child component. We can store global data to Context, and get the data on the component that needs it.

![React context](/assets/images/category/react/2021/context-api/context.png)

To use Context in React, you need to use Context API, especially you need to use `Provider` and `Consumer` of Context API.

![React context with Provider and Consumer](/assets/images/category/react/2021/context-api/context.png)

To use the data stored in Context, we need to provide Context Provider to the common parent component, and we need to use Context consumer to consume the data in the component that needs it.

{% include in-feed-ads.html %}

## How to use Context

Now, let's see how to use Context API to handle global data in React.

### Prepare project

Execute the command below to create a new React project for Context.

```bash
npx create-react-app context_example --template=typescript
```

### Create Context

Next, let's create a Context to store global data. Create`./src/Contexts/Count/index.tsx` file and modify it like the below.

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

To create Context in React, we need to use `createContext`. Also, Context is also a React component, so we need to use State to handle the mutable data in the component.

```js
import { createContext, useState } from 'react';
```

Next, create Context by createContext. At this time, we need to pass the initial value of the global data.

```js
const CountContext = createContext({
  count: 0,
  plusCount: () => {},
});
```

Context is also one of the React component, so the structure of Context is basically same with the component. At this time, we need to wrap the content to be displayed on the screen with Context Provider.

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

Context is also the React component. So, when we use the changeable data in Context, we need to use useState to create State.

```js
const CountProvider = ({ children }: Props): JSX.Element => {
  const [count, setCount] = useState(0);

  const plusCount = (): void => {
    setCount(count + 1);
  };
  ...
};
```

And then, we need to provide State to Context Provider.

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

Lastly, export Context created by createContext and the React component created by Context Provider. the React component created by Context Provider will be used on the common parent component, and Context created by createContext will be used to consume data.

```js
export { CountContext, CountProvider };
```

Done! we've created Context for global data. Next, let's see how to use Context.

{% include in-feed-ads.html %}

### Provider

To use Context, we need to provide Context Provider to the common parent component. In here, we'll provide it to the `App` component. To provide Context Provider, open the `./src/App.tsx` file and modify it like the below.

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

To use global data with Context, we need to provide Context Provider to the common parent component. Providing Context Provider means to wrap the component with it.

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

Now, we can access global data in Context on any component under `CountProvider`.

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

We didn't create the components that use Context, so errors occur. Next, let's create the `CountLabel` component and `PlusButton` component to use Context data.

### Consumer

Let's make components to use global data in Context. First, create `./src/Components/CountLabel/index.tsx` file and modify it like the below.

```js
import { useContext } from 'react';
import { CountContext } from '../../Contexts/Count';

export const CountLabel = () => {
  const { count } = useContext(CountContext);
  return <div>{count}</div>;
};
```

The CountLabel component is a simple component to show the count on the screen. we'll use the global data in Context for the count value in here. When you use the value in Context, you should use `Consumer` in the React class component and `useContext` hook in the function component.

We need to pass CountContext that is our Context to the parameter, and then we can access the variables that we've created them by createContext.

```js
const CountContext = createContext({
  count: 0,
  plusCount: () => {},
});
```

CountLabel only needs the count variable in Context.

```js
...
export const CountLabel = () => {
  const { count } = useContext(CountContext);
  return <div>{count}</div>;
};
```

{% include in-feed-ads.html %}

Next, let's create the `PlusButton` component to increase the count value in Context. Create the `./src/Components/PlusButton/index.tsx` file and modify it like the below.

```js
import { useContext } from 'react';
import { CountContext } from '../../Contexts/Count';

export const PlusButton = () => {
  const { plusCount } = useContext(CountContext);

  return <button onClick={plusCount}>+ 1</button>;
};
```

The PlusButton component is a simple component to show the `+ 1` label button and when the button is clicked, call the `plusCount` fucntion to increase the count value in Context.

Like CountLabel, we use useContext hook to get the `plusCount` function to increase the count value in Context, and then, we bound the function to the `onClick` event.

### Check

We've made the example to use global data with Context. To check the React project we've created, execute the command below to start the React project.

```bash
npm start
```

When the React project is started, you can see the `0` lable and `+ 1` button on the screen like the below.

![React Context example: Count](/assets/images/category/react/2021/context-api/count.npg)

When you click the `+ 1` button, you can see the count value is increased like the below.

![React Context example: Count increased](/assets/images/category/react/2021/context-api/count_increased.jpg)

## Completed

Done! we've seen how to handle global data in the React component with Context. The example in the blog post is very small, so actually, we don't need to use Context. However, if the project has many components, you can see Context to share the data, so someday this blog post about how to use Context is helpful for you.
