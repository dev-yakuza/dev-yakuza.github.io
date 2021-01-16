---
layout: 'post'
permalink: '/react/create-react-app/styled-components/'
paginate_path: '/react/:num/create-react-app/styled-components/'
lang: 'en'
categories: 'react'
comments: true

title: 'styled-components in create-react-app'
description: Let's see how to apply and use styled-components to the React project created by create-react-app.
image: '/assets/images/category/react/create-react-app/styled-components/background.jpg'
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [Create project](#create-project)
- [Install styled-components](#install-styled-components)
- [How to use](#how-to-use)
- [Completed](#completed)

</div>

## create-react-app series

This blog post is a series. You can see other blog posts of the series on the list.

- [What is React]({{site.url}}/{{page.categories}}/create-react-app/react/){:target="_blank"}
- [create-react-app]({{site.url}}/{{page.categories}}/create-react-app/start/){:target="_blank"}
- [TypeScript in create-react-app]({{site.url}}/{{page.categories}}/create-react-app/typescript/){:target="_blank"}
- [[TypeScript] Make Import path based on Root in create-react-app]({{site.url}}/{{page.categories}}/create-react-app/root-import/){:target="_blank"}
- styled-components in create-react-app
- [Jest]({{site.url}}/{{page.categories}}/create-react-app/jest/){:target="_blank"}

## Outline

In this blog post, I'll show how to apply `styled-components` to the React project.

- styled-components: [https://styled-components.com/](https://styled-components.com/){:rel="noopener" target="_blank"}

This blog post will use the React project with TypeScript, and you can see the source code on the link below.

- GitHub: [https://github.com/dev-yakuza/study-create-react-app/tree/main/3.styled-components](https://github.com/dev-yakuza/study-create-react-app/tree/main/3.styled-components){:rel="noopener" target="_blank"}

## Create project

Execute the command below to create a React project.

```bash
npx create-react-app my-app --template=typescript
```

And then, execute the command below to start the React project.

```bash
# cd my-app
npm start
```

If you don't have any problem, you can see the screen below on the browser.

![create-react-app with styled-components](/assets/images/category/react/create-react-app/styled-components/project.jpg)

{% include in-feed-ads.html %}

## Install styled-components

We need to install the `styled-components` library to apply it to the React project created by `create-react-app`. Execute the command below to install the `styled-components` library.

```bash
npm install --save styled-components
```

And then, we use TypeScript on the React project, so execute the command below to install `styled-components` types and test library.

```bash
npm install --save-dev @types/styled-components jest-styled-components
```

## How to use

Let's make a simple component with `styled-components`. Open `./src/App.tsx` file and modify it like below.

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

We can write the style in `JSX` with `styled-components` like above.

And then, delete the unused files below.

- App.css
- logo.svg

You can see more usages on the official homepage.

- styled-components basics: [https://styled-components.com/docs/basics](https://styled-components.com/docs/basics){:rel="noopener" target="_blank"}

## Completed

We've seen how to apply `styled-components` to the React project created by `create-react-app` in this blog post. And the, we've seen simple usage of `styled-components`.

From now on, let's make styles in JSX file with styled-components.
