---
layout: 'post'
permalink: '/react/root-import/'
paginate_path: '/react/:num/root-import/'
lang: 'en'
categories: 'react'
comments: true

title: 'Make Import path based on Root in React'
description: when import Component in React, let's make import path based on Root.
image: '/assets/images/category/react/2019/root-import/background.jpg'
---

## Outline
I already introduced to make import path based on Root in React Native(RN) blog post. if you want to know why I use and what the problem is, see React Native(RN) blog post.

- [Make Import path based on Root in RN(React Native)]({{site.url}}/react-native/root-import/){:target="_blank"}

on Github, you can see full source code that I use in this blog post.

- Github: [https://github.com/dev-yakuza/react_root_import](https://github.com/dev-yakuza/react_root_import){:target="_blank"}

## Prepare Project
React project in this blog post is based on Webpack, Typescript and styled-components. if you want to know more details, see the previous blog post.

- [Start React With Webpack]({{site.url}}/{{page.categories}}/start/){:target="_blank"}
- [Use Typescript In React]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}
- [Use styled-components in React]({{site.url}}/{{page.categories}}/styled-components/){:target="_blank"}

if you make React project by following the previous blog posts, you can get the folder structure like below. I've created namded react_root_import instead of react_styled-components.

```bash
|-- src
|   |-- index.html
|   |-- App.tsx
|-- .babelrc
|-- package.json
|-- webpack.config.js
```

{% include in-feed-ads.html %}

## babel-plugin-root-import
execute the command below to install `babel-plugin-root-import` to make import path based on Root.

```bash
npm install babel-plugin-root-import --save-dev
```

open and modify `.babelrc` in React project like below.

```json
{
  "presets": [
    ...
  ],
  "plugins": [
    [
      "babel-plugin-root-import",
      {
        "rootPathPrefix": "~",
        "rootPathSuffix": "src"
      }
    ]
  ],
  "env": {
    ...
  }
}
```

as you can see my folder structure, all source code is in `src` folder. so I made import path based on `src` instead of `root`.

## Webpack Setting
open `webpack.config.js` file and modify it like below to make import path based on root.

```js
...
module.exports = {
  mode: process.env.NODE_ENV,
  entry: {
    ...
  },
  output: {
    ...
  },
  module: {
    ...
  },
  resolve: {
    extensions: ['.ts', '.tsx', '.js', '.jsx'],
  },
  plugins: [
    ...
  ],
};
```

## Typescript
if you don't use Typescript in React, you don't need to do below. I use Typescript in React, so I need to make Typescript recognize root path.

open and modify `tsconfig.json` in React like below.

```json
{
  "compilerOptions": {
    ...
    "baseUrl": "./src", // all paths are relative to the baseUrl
    "paths": {
      "~/*": ["*"] // resolve any `~/foo/bar` to `<baseUrl>/foo/bar`
    }
  },
  ...
}
```

{% include in-feed-ads.html %}

## Modify Source Code
create and modify source code to check the configuration above. create `src/Components/Title/index.tsx` file and modify it like below.

```js
import * as React from 'react';
import Styled from 'styled-components';

const Label = Styled.h1`
  color: red;
`;
interface Props {
  label: string;
}

const Title = ({ label }: Props) => {
  return <Label>{label}</Label>;
};

export default Title;
```

and then, create and modify `src/Features/Top/index.tsx` file like below.

```js
import * as React from 'react';

import Title from '~/Components/Title';

interface Props {}

const Top = ({  }: Props) => {
  return <Title label="Hello World!" />;
};

export default Top;
```

lastly, open and modify `src/App.tsx` like below.

```js
import * as React from 'react';
import * as ReactDOM from 'react-dom';

import Top from './Features/Top';

interface Props {}

const App = ({  }: Props) => {
  return <Top />;
};

ReactDOM.render(<App />, document.getElementById('app'));
```

{% include in-feed-ads.html %}

## Check
execute the command below to execute Webpack test server for checking our setting working well.

```bash
npm start
```

when you open `http://localhost:8080/` on the browser, you can see `Hello World!` on the screen.
execute the command below to build React project by Webpack.

```bash
npm run build
```

and then, you can see the folder and file is created in `dist` folder.

## Completed
now, we can also refer the components with `~/` instead of `../../../../` when we `import` it. as you can see my source code, I refer the component in the folder with `./`, and I refer the component out of the folder with `~/`.
