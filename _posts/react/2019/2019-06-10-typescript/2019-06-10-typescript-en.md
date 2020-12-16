---
layout: 'post'
permalink: '/react/typescript/'
paginate_path: '/react/:num/typescript/'
lang: 'en'
categories: 'react'
comments: true

title: 'Use Typescript In React'
description: let's see how to set Typescript in React, and how to use Typescript in Recat simply
image: '/assets/images/category/react/2019/typescript/background.jpg'
---

## Outline
my company starts a new React project. so I got a chance to configure it from the beginning. in this blog post, we will see how to set Typescript in React and how to use Typesscript in React.

on Github, you can see full source code that I use in this blog post.

- Github: [https://github.com/dev-yakuza/react_typescript](https://github.com/dev-yakuza/react_typescript){:target="_blank"}

if you want to know how to configure Webpack for React project, see the previous blog post.

- Previous blog: [Start React With Webpack]({{site.url}}/{{page.categories}}/start/){:target="_blank"}

## Prepare Proejct
the React source code in this blog post is based on Webpack that I've introduced on the previous blog post. if you want to know more details, see the previous blog post.

- Previous blog: [Start React With Webpack]({{site.url}}/{{page.categories}}/start/){:target="_blank"}

if you make React project by following the previous blog post, you can get the folder structure like below. I've created namded react_typescript instead of react_start.

```bash
|-- src
|   |-- index.html
|   |-- App.jsx
|-- .babelrc
|-- package.json
|-- webpack.config.js
```

## Installation
execute the command below to install libraries for using Typescript in React.

```bash
npm install --save-dev typescript @babel/preset-typescript ts-loader fork-ts-checker-webpack-plugin tslint tslint-react
```

- typescript: for using Typescript.
- @babel/preset-typescript: for building Typescript by using babel.
- ts-loader: for compiling Typescript in Webpack.
- fork-ts-checker-webpack-plugin: for making ts-loader faster
- tslint, tslint-react: for checking code conventions.

{% include in-feed-ads.html %}

## Configure Webpack
open `webpack.config.js` and modify it like below for using Typescript in React.

```js
const path = require('path');

const HtmlWebpackPlugin = require('html-webpack-plugin');

// For Typescript
const ForkTsCheckerWebpackPlugin = require('fork-ts-checker-webpack-plugin');

module.exports = {
  entry: {
    // For Typescript
    'js/app': ['./src/App.tsx'],
  },
  output: {
    path: path.resolve(__dirname, 'dist/'),
    publicPath: '/',
  },
  module: {
    rules: [
      // For Typescript
      {
        test: /\.(ts|tsx)$/,
        use: [
          'babel-loader',
          {
            loader: 'ts-loader',
            options: {
              transpileOnly: true,
            },
          },
        ],
        exclude: /node_modules/,
      },
    ],
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: './src/index.html',
      filename: 'index.html',
    }),
    // For typescript
    new ForkTsCheckerWebpackPlugin({ silent: true }),
  ],
};
```

let's see details.

```js
// For Typescript
const ForkTsCheckerWebpackPlugin = require('fork-ts-checker-webpack-plugin');
```

load(import) the plugin for making Typescript build faster.

```js
entry: {
  // For Typescript
  'js/app': ['./src/App.tsx'],
},
```

change `jsx` to `tsx` in entry file of the bundle file.

```js
{
  test: /\.(ts|tsx)$/,
  use: [
    'babel-loader',
    {
      loader: 'ts-loader',
      options: {
        transpileOnly: true,
      },
    },
  ],
  exclude: /node_modules/,
},
```

change `js|jsx` to `ts|tsx` and add `ts-loader` to use Typescript in Webpack. ts-loader option is for making faster.

```js
plugins: [
  ...
  // For typescript
  new ForkTsCheckerWebpackPlugin({ silent: true }),
],
```

lastly, use the plugin for making Typescript build faster.

{% include in-feed-ads.html %}

## tsconfig.json
create and modify `tsconfig.json` like below to use Typescript.

```json
{
  "compilerOptions": {
    "target": "es6",
    "module": "esnext",
    "moduleResolution": "node",
    "noResolve": false,
    "noImplicitAny": false,
    "removeComments": false,
    "sourceMap": true,
    "allowJs": true,
    "jsx": "react",
    "allowSyntheticDefaultImports": true,
    "keyofStringsOnly": true
  },
  "typeRoots": ["node_modules/@types", "src/@type"],
  "exclude": [
    "node_modules",
    "build",
    "scripts",
    "acceptance-tests",
    "webpack",
    "jest",
    "src/setupTests.ts",
    "./node_modules/**/*"
  ],
  "include": ["./src/**/*", "@type"]
}
```

if you want to know details about options, see the links below.

- [https://www.typescriptlang.org/docs/handbook/tsconfig-json.html](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html){:rel="nofollow noreferrer" target="_blank"}
- [https://www.typescriptlang.org/docs/handbook/compiler-options.html](https://www.typescriptlang.org/docs/handbook/compiler-options.html){:rel="nofollow noreferrer" target="_blank"}

## tslint.json
create `tslint.json` and modify it like below to use Typescript.

```json
{
  "extends": ["tslint", "tslint-react"],
  "rules": {
    "align": [true, "parameters", "statements"],
    "jsx-alignment": false,
    "ban": false,
    "class-name": true,
    "comment-format": [true, "check-space"],
    "curly": true,
    "eofline": false,
    "forin": true,
    "indent": [true, "spaces"],
    "interface-name": [false],
    "jsdoc-format": true,
    "jsx-no-lambda": false,
    "jsx-no-multiline-js": false,
    "label-position": true,
    "max-line-length": [true, 120],
    "member-ordering": [
      true,
      "public-before-private",
      "static-before-instance",
      "variables-before-functions"
    ],
    "no-any": false,
    "no-arg": true,
    "no-bitwise": true,
    "no-console": [
      true,
      "log",
      "error",
      "debug",
      "info",
      "time",
      "timeEnd",
      "trace"
    ],
    "no-consecutive-blank-lines": true,
    "no-construct": true,
    "no-debugger": true,
    "no-duplicate-variable": true,
    "no-empty": false,
    "no-eval": true,
    "no-shadowed-variable": true,
    "no-string-literal": true,
    "no-switch-case-fall-through": true,
    "no-trailing-whitespace": false,
    "no-unused-expression": true,
    "no-use-before-declare": true,
    "one-line": [
      true,
      "check-catch",
      "check-else",
      "check-open-brace",
      "check-whitespace"
    ],
    "quotemark": [true, "single", "jsx-double"],
    "radix": true,
    "semicolon": [false],
    "switch-default": true,

    "trailing-comma": [false],

    "triple-equals": [true, "allow-null-check"],
    "typedef": [true, "parameter", "property-declaration"],
    "typedef-whitespace": [
      true,
      {
        "call-signature": "nospace",
        "index-signature": "nospace",
        "parameter": "nospace",
        "property-declaration": "nospace",
        "variable-declaration": "nospace"
      }
    ],
    "variable-name": [
      true,
      "ban-keywords",
      "check-format",
      "allow-leading-underscore",
      "allow-pascal-case"
    ],
    "whitespace": [
      true,
      "check-branch",
      "check-decl",
      "check-module",
      "check-operator",
      "check-separator",
      "check-type",
      "check-typecast"
    ]
  }
}
```

if you want to know details about options, see the links below.

- [https://github.com/Microsoft/TypeScript-React-Starter#overriding-defaults](https://github.com/Microsoft/TypeScript-React-Starter#overriding-defaults){:rel="nofollow noreferrer" target="_blank"}
- [https://palantir.github.io/tslint/usage/configuration/](https://palantir.github.io/tslint/usage/configuration/){:rel="nofollow noreferrer" target="_blank"}

{% include in-feed-ads.html %}

## Configure babel
open and modify `.babelrc` like below for setting babel.

```json
{
  "presets": [
    [
      "@babel/preset-env",
      { "targets": { "browsers": ["last 2 versions", ">= 5% in KR"] } }
    ],
    "@babel/react",
    "@babel/typescript"
  ]
}
```

add `"@babel/typescript"` to compile Typescript in babel.

## Coding Typescript style
change file name from `./src/App.jsx` to `./src/App.tsx` to use Typescript in React and modify it like below.

```js
import * as React from 'react';
import * as ReactDOM from 'react-dom';

interface Props {}

const App = ({  }: Props) => {
  return <h1>Hello World!</h1>;
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

## Reference
- [https://github.com/TypeStrong/ts-loader](https://github.com/TypeStrong/ts-loader){:rel="nofollow noreferrer" target="_blank"}
- [https://github.com/Realytics/fork-ts-checker-webpack-plugin](https://github.com/Realytics/fork-ts-checker-webpack-plugin){:rel="nofollow noreferrer" target="_blank"}
- [https://github.com/palantir/tslint-react](https://github.com/palantir/tslint-react){:rel="nofollow noreferrer" target="_blank"}