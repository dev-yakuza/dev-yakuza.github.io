---
layout: 'post'
permalink: '/react/styled-components/'
paginate_path: '/react/:num/styled-components/'
lang: 'en'
categories: 'react'
comments: true

title: 'Use styled-components in React'
description: let's see how to use styled-components in React.
image: '/assets/images/category/react/2019/styled-components/background.jpg'
---

## Outline
my company starts a new React project. so I got a chance to configure it from the beginning. in this blog, I will introduce how to set styled-components and how to use styled-components in React.

on Github, you can see full source code that I use in this blog post.

- Github: [https://github.com/dev-yakuza/react_styled-components](https://github.com/dev-yakuza/react_styled-components){:target="_blank"}

the source code is based on the project created by the previous blog post.

- previous blog: [Use Typescript In React]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}

## Prepare Project.
React project in this blog post is based on Webpack and Typescript. if you want to know more details, see the previous blog posts.

- [Start React With Webpack]({{site.url}}/{{page.categories}}/start/){:target="_blank"}
- [Use Typescript In React]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}

if you make React project by following the previous blog posts, you can get the folder structure like below. I've created namded react_styled-components instead of react_typescript.

```bash
|-- src
|   |-- index.html
|   |-- App.tsx
|-- .babelrc
|-- package.json
|-- webpack.config.js
```

## Installation
execute the command below to install libraries for using styled-components in React.

```bash
npm install --save-dev styled-components @types/styled-components babel-plugin-styled-components cross-env
```

- styled-components: for using styled-components
- @types/styled-components: for using Typesciption when use styled-components
- babel-plugin-styled-components: for making class name recognizable in styled-components
- cross-env: for setting the environment variable with same command in Mac and Windows both.

{% include in-feed-ads.html %}

## Modify package.json
modify script part in `package.json` like below.

```js
"scripts": {
  "start": "cross-env NODE_ENV=development webpack-dev-server --open",
  "prebuild": "rimraf dist",
  "build": "cross-env NODE_ENV=production webpack --progress"
},
```

before, we've used `--mode development` and `--mode production` to configure Webpack mode. now, we'll use the environment variable to set the mode.

## Webpack 수정
modify `webpack.config.js` like below.

```js
...
module.exports = {
  mode: process.env.NODE_ENV,
  ...
};
...
```

before, we've set the mode by executing the command with option, but now, we set the environment variable to `mode`.

## Configure babel
modify `.babelrc` file like below.

```json
{
  "presets": [
    ...
  ],
  "env": {
    "development": {
      "plugins": ["babel-plugin-styled-components"]
    }
  }
}
```

if the enviroment variable is development, babel-plugin-styled-components is set to make class name recognizable. if the environment variable is production, styled-components makes hash class name so people can't understand it easily.

[if the environment variable is development]

![use styled-components in React - class name when the environment variable is development](/assets/images/category/react/2019/styled-components/styled-components-in-development.jpg)

[if the environment variabel is production]

![use styled-components in React - class name when the environment variable is production](/assets/images/category/react/2019/styled-components/styled-components-in-production.jpg)

{% include in-feed-ads.html %}

## styled-components Style Coding
open `./src/App.tsx` file and modify it like below to use styled-components in React.

```js
import * as React from 'react';
import * as ReactDOM from 'react-dom';
import Styled from 'styled-components';

const Title = Styled.h1`
  color: red;
`;
interface Props {}

const App = ({  }: Props) => {
  return <Title>Hello World!</Title>;
};

ReactDOM.render(<App />, document.getElementById('app'));
```

## Check
execute the command below to check our configuration and React worked well.

```bash
npm start
```

and open the browser and go to `http://localhost:8080/`. you can see `Hello World!` on the screen. we can add `--open` option like `"start": "webpack-dev-server --mode development --open",` instated of `"start": "webpack-dev-server --mode development",` in package.json script to open the browser and move `http://localhost:8080/` automatically when `npm start` is executed.

kill the test server process, and execute the command below to build.

```bash
npm run build
```

we can see `./dist/` folder created, and `index.html`, `js/app.js` created in there. also when you open `index.html` file, you can see `<script type="text/javascript" src="/js/app.js"></script>` is added automatically instead of index.html created by us.

## Fix Error
when I executed `npm start` to check React project, it was fine, but when I executed `npm run build` to build the proejct, I got errors like below.

```bash
ERROR in /git_repository/react_styled-components/node_modules/@types/react-native/globals.d.ts
ERROR in /git_repository/react_styled-components/node_modules/@types/react-native/globals.d.ts(36,15):
TS2300: Duplicate identifier 'FormData'.

ERROR in /git_repository/react_styled-components/node_modules/@types/react-native/globals.d.ts
ERROR in /git_repository/react_styled-components/node_modules/@types/react-native/globals.d.ts(81,5):
TS2717: Subsequent property declarations must have the same type.  Property 'body' must be of type 'BodyInit', but here has type 'string | ArrayBuffer | DataView | Int8Array | Uint8Array | Uint8ClampedArray | Int16Array | Uint16Array | Int32Array | Uint32Array | Float32Array | Float64Array | Blob | FormData'.

ERROR in /git_repository/react_styled-components/node_modules/@types/react-native/globals.d.ts
ERROR in /git_repository/react_styled-components/node_modules/@types/react-native/globals.d.ts(107,14):
TS2300: Duplicate identifier 'RequestInfo'.

ERROR in /git_repository/react_styled-components/node_modules/@types/react-native/globals.d.ts
ERROR in /git_repository/react_styled-components/node_modules/@types/react-native/globals.d.ts(126,13):
TS2403: Subsequent variable declarations must have the same type.  Variable 'Response' must be of type '{ new (body?: BodyInit, init?: ResponseInit): Response; prototype: Response; error(): Response; redirect(url: string, status?: number): Response; }', but here has type '{ new (body?: string | ArrayBuffer | DataView | Int8Array | Uint8Array | Uint8ClampedArray | Int16Array | Uint16Array | Int32Array | Uint32Array | Float32Array | Float64Array | Blob | FormData, init?: ResponseInit): Response; prototype: Response; error: () => Response; redirect: (url: string, status?: number) => Res...'.

ERROR in /git_repository/react_styled-components/node_modules/@types/react-native/globals.d.ts
ERROR in /git_repository/react_styled-components/node_modules/@types/react-native/globals.d.ts(249,14):
TS2300: Duplicate identifier 'XMLHttpRequestResponseType'.

ERROR in /git_repository/react_styled-components/node_modules/@types/react-native/index.d.ts
ERROR in /git_repository/react_styled-components/node_modules/@types/react-native/index.d.ts(9418,18):
TS2717: Subsequent property declarations must have the same type.  Property 'geolocation' must be of type 'Geolocation', but here has type 'GeolocationStatic'.

ERROR in /git_repository/react_styled-components/node_modules/@types/react-native/index.d.ts
ERROR in /git_repository/react_styled-components/node_modules/@types/react-native/index.d.ts(9421,11):
TS2451: Cannot redeclare block-scoped variable 'navigator'.

ERROR in /git_repository/react_styled-components/node_modules/typescript/lib/lib.dom.d.ts
ERROR in /git_repository/react_styled-components/node_modules/typescript/lib/lib.dom.d.ts(5353,11):
TS2300: Duplicate identifier 'FormData'.

ERROR in /git_repository/react_styled-components/node_modules/typescript/lib/lib.dom.d.ts
ERROR in /git_repository/react_styled-components/node_modules/typescript/lib/lib.dom.d.ts(5363,13):
TS2300: Duplicate identifier 'FormData'.

ERROR in /git_repository/react_styled-components/node_modules/typescript/lib/lib.dom.d.ts
ERROR in /git_repository/react_styled-components/node_modules/typescript/lib/lib.dom.d.ts(17123,11):
TS2320: Interface 'Window' cannot simultaneously extend types 'GlobalFetch' and 'WindowOrWorkerGlobalScope'.
  Named property 'fetch' of types 'GlobalFetch' and 'WindowOrWorkerGlobalScope' are not identical.

ERROR in /git_repository/react_styled-components/node_modules/typescript/lib/lib.dom.d.ts
ERROR in /git_repository/react_styled-components/node_modules/typescript/lib/lib.dom.d.ts(18152,13):
TS2451: Cannot redeclare block-scoped variable 'navigator'.

ERROR in /git_repository/react_styled-components/node_modules/typescript/lib/lib.dom.d.ts
ERROR in /git_repository/react_styled-components/node_modules/typescript/lib/lib.dom.d.ts(18568,6):
TS2300: Duplicate identifier 'RequestInfo'.

ERROR in /git_repository/react_styled-components/node_modules/typescript/lib/lib.dom.d.ts
ERROR in /git_repository/react_styled-components/node_modules/typescript/lib/lib.dom.d.ts(18746,6):
TS2300: Duplicate identifier 'XMLHttpRequestResponseType'.

ERROR in /git_repository/react_styled-components/node_modules/typescript/lib/lib.dom.iterable.d.ts
ERROR in /git_repository/react_styled-components/node_modules/typescript/lib/lib.dom.iterable.d.ts(67,11):
```

I've modified `tsconfig.json` like below to solve this problem.

```json
{
  "compilerOptions": {
    ...
    "skipLibCheck": true
  },
  ...
}
```