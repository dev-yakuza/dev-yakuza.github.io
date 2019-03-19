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

## how to use
styled-components has theme function for maintaining site level styles. let's see ```theme``` feature and basic usages.

### basic usages
- basic styling

{% include_relative common/basic_usage.md %}

- dynamic styling using props

{% include_relative common/dynamic_styling.md %}

### Theme usage
there are details about how to use typescript for theme in official site.
- officail site: [styled-components#typescript](https://www.styled-components.com/docs/api#typescript){:rel="nofollow noreferrer" target="_blank"}
- reference site: [Styled-Components-Typescript-Example](https://github.com/patrick91/Styled-Components-Typescript-Example){:rel="nofollow noreferrer" target="_blank"}

if you see official site and reference site, you can catch we should use relative path for using styled-components.

so, we don't use official site way. we use "dynamic styling using props" way.

{% include_relative common/theme_usage.md %}

## reference
- styled-components official site: [styled-components](https://www.styled-components.com/docs){:rel="nofollow noreferrer" target="_blank"}
- reference site: [Styled-Components-Typescript-Example](https://github.com/patrick91/Styled-Components-Typescript-Example){:rel="nofollow noreferrer" target="_blank"}