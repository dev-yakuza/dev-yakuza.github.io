---
layout: 'post'
permalink: '/react-native/styled-components/'
paginate_path: '/react-native/:num/styled-components/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'styled-components'
description: 'this blog is about how to use styled-component library for react-native styling.'
image: '/assets/images/category/react-native/styled-components.jpg'
---

<div id="contents_list" markdown="1">

## Contents

1. [create react-native project](#create-react-native-project)
1. [install styled-components library](#install-styled-components-library)
1. [how to use](#how-to-use)
    - [basic usages in Class Component](#basic-usages-in-class-component)
    - [Theme usage in Class Component](#theme-usage-in-class-component)
    - [Basic usage in Functional Components](#basic-usage-in-functional-components)
    - [Theme Usage in Functional Components](#theme-usage-in-functional-components)
1. [reference](#reference)

</div>

## create react-native project

this blog introduce how to use styled-component with RN project which is applied typescript. if you want to know how to apply typescript to RN, see previous blog.

- [typescript]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}

## install styled-components library

install styled-components library and other necessary libraries for integrating typescript.

{% include_relative common/installation.md %}

- styled-components: this is styled-components library.
- @types/styled-components: this is stypled-components types for typescript.
- babel-plugin-styled-components: this is not required but make class name easily understand. copy and paste below code to ```babel.config.js```.

```js
module.exports = {
  ...
  plugins: ['babel-plugin-styled-components'],
};
```

{% include in-feed-ads.html %}

## how to use

styled-components has theme function for maintaining site level styles. let's see ```theme``` feature and basic usages.

### basic usages in Class Component

- basic styling

{% include_relative common/basic_usage.md %}

- dynamic styling using props

{% include_relative common/dynamic_styling.md %}

### Theme usage in Class Component

there are details about how to use typescript for theme in official site.

- officail site: [styled-components#typescript](https://www.styled-components.com/docs/api#typescript){:rel="nofollow noreferrer" target="_blank"}
- reference site: [Styled-Components-Typescript-Example](https://github.com/patrick91/Styled-Components-Typescript-Example){:rel="nofollow noreferrer" target="_blank"}

if you see official site and reference site, you can catch we should use relative path for using styled-components.

so, we don't use official site way. we use "dynamic styling using props" way.

{% include_relative common/theme_usage.md %}

{% include in-feed-ads.html %}

### Basic usage in Functional Components

```js
import React from 'react';
import styled from 'styled-components/native';

const Container = styled.View`
  flex: 1;
  justify-content: center;
  align-items: center;
  background-color: #f5fcff;
`;
const MainText = styled.Text`
  font-size: 20;
  text-align: center;
  margin: 10px;
  color: red;
`;

interface Props {}
const App = ({}: Props) => {
  return (
    <Container>
      <MainText>Hello world</MainText>
    </Container>
  );
};

export default App;
```

### Theme Usage in Functional Components

```js
import React from 'react';
import styled from 'styled-components/native';
import {ThemeProvider} from 'styled-components';
import Theme from './Theme';

interface StyledProps {
  theme: ITheme;
}
const Container = styled.View`
  flex: 1;
  justify-content: center;
  align-items: center;
  background-color: ${(props: StyledProps) =>
    props.theme && props.theme.color.black};
`;
const MainText = styled.Text`
  font-size: 20;
  text-align: center;
  margin: 10px;
  color: red;
`;

interface Props {}
const App = ({}: Props) => {
  return (
    <ThemeProvider theme={Theme}>
      <Container>
        <MainText>Hello world</MainText>
      </Container>
    </ThemeProvider>
  );
};

export default App;
```

## reference

- styled-components official site: [styled-components](https://www.styled-components.com/docs){:rel="nofollow noreferrer" target="_blank"}
- reference site: [Styled-Components-Typescript-Example](https://github.com/patrick91/Styled-Components-Typescript-Example){:rel="nofollow noreferrer" target="_blank"}
