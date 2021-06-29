---
layout: 'post'
permalink: '/react/props-state/'
paginate_path: '/react/:num/props-state/'
lang: 'en'
categories: 'react'
comments: true

title: '[React] Props and State'
description: Let's see what Props and State are and how to use Props and State to manage the data in React.
image: '/assets/images/category/react/background.jpg'
published: false
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [Props](#props)
- [State](#state)
- [Completed](#completed)

</div>

## Outline

To manage the data in React, you can use `Props`, `State` and `Context`. In this blog post, I will introduce what Props and State are and how to use them.

To manage Context in React, there is a blog post about how to use Context API. See the link below.

- [[React] Context API]({{site.url}}/{{page.categories}}/context-api/){:target="_blank"}

## Props

Props(Properties) is a data from the parent component to the child component. The data is from the parent, so it can't be modified in the child component. This means the Props is the property of the component.

- React official site: [Components and Props](https://reactjs.org/docs/components-and-props.html){:rel="noopener" target="_blank"}

We already use the properties with HTML.

```html
<div id="name" class="label" onclick="alert('Hello World!');">
  Hello world!
</div>
```

The code above configures the id and class properties to the HTML div tag and use the alert code of the JavaScript in the onclick property. Like this, we already use the property concept in HTML. React extends this property concept by passing the data.

```js
const Text = ({text}) => {
  return <div>{text}</div>
}

const App = () => {
  return <Text text='Hello world!'/>
}
```

Like the above, we can pass te strig data(`Hello world!`) to the Props of the child component(Text) in the parent component(App).

{% include in-feed-ads.html %}

## State

State is used to handle fluid data within a component, and the data can be changed in a component. in other words, State means the state of the component.

- React offical site: [State and Lifecycle](https://reactjs.org/docs/state-and-lifecycle.html){:rel="noopener" target="_blank"}

The example below is the code when you click the `+` button, the value on the screen is increased 1.

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

To use State in React function componet, we should use the Hook called `useState`. useState is called with the initial value of the variable, and returns an array. The returned array has a variable set the initial value and a Set function to update the variable.

```js
const Array = useState (Initial value);
```

- Array[0]: the variable initialized with the initial value.
- Array[1]: Set function can update the variable(Array[0]).

Noramlly, we use Destructuring assignment of JavaScript to allocate the variable and Set function.

```js
const [Variable name, Set fucntion name] = useState (initial value);
```

the variable from useState is the `Immutable`, so we can't update the variable directly. If you want to update the variable, you should use the Set function.

```js
const App = () => {
  const [count, setCount] = useState(0);

  return <div>
    <Text text={count} />
    <div onClick={() => setCount(count + 1)}>+</div>
  </div>
}
```

## Completed

Done! We've seen how to use Props and State to manage the data in the React component. Now, we know the Props, that is the immutable data and means the property of the component, and State that is updatable in a component and means the state of the component. From now, try to make great React components with Props and State.
