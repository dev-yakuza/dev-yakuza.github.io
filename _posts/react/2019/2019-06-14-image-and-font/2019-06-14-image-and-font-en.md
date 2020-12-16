---
layout: 'post'
permalink: '/react/image-and-font/'
paginate_path: '/react/:num/image-and-font/'
lang: 'en'
categories: 'react'
comments: true

title: 'Images And Web Font in React'
description: let's see how to use Images and Web Font in React project based on Webpack.
image: '/assets/images/category/react/2019/image-and-font/background.jpg'
---

## Outline
my company starts a new React project. so I try to configure React based on Webpack. in this blog post, we'll see how to use Resources(Images and Web font) in React project based on Webpack.

on Github, you can see full source code that I use in this blog post.

- Github: [https://github.com/dev-yakuza/react_image_font](https://github.com/dev-yakuza/react_image_font){:rel="noopener" target="_blank"}

## Prepare Project
React project introduced in here was applied the contents below. you can see more details on each link.

- [Start React With Webpack]({{site.url}}/{{page.categories}}/start/){:target="_blank"}
- [Use Typescript In React]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}
- [Use styled-components in React]({{site.url}}/{{page.categories}}/styled-components/){:target="_blank"}
- [Make Import path based on Root in React]({{site.url}}/{{page.categories}}/root-import/){:target="_blank"}
- [React Router]({{site.url}}/{{page.categories}}/react-router/){:target="_blank"}

if you make React project by following the previous blog posts, you can get the folder structure like below. I've created namded react_image_font instead of react_router.

```bash
|-- src
|   |-- Components
|   |   |-- Title
|   |   |   |-- index.tsx
|   |-- Features
|   |   |-- Page1
|   |   |   |-- index.tsx
|   |   |-- Page2
|   |   |   |-- index.tsx
|   |   |-- Top
|   |   |   |-- index.tsx
|   |-- index.html
|   |-- App.tsx
|-- .babelrc
|-- package.json
|-- webpack.config.js
```

## Install Moduels
we need Webpack `file-loader` and `url-loader` to use images and web font in React project based on Webpack. execute the command below to install `file-loader` and `url-loader`.

```bash
npm install --save-dev file-loader, url-loader
```

- file-loader: this module will copy the file used in the project by Webpack.
- url-loader: this moduel makes bundle file with small size file in Webpack.

{% include in-feed-ads.html %}

## Modify Webpack
open `webpack.config.js` and modify it like below to use installed modules(file-loader, url-loader).

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
    rules: [
      ...
      {
        // write image files under 10k to inline or copy image files over 10k
        test: /\.(jpg|jpeg|gif|png|svg|ico)?$/,
        use: [
          {
            loader: 'url-loader',
            options: {
              limit: 10000,
              fallback: 'file-loader',
              name: 'images/[name].[ext]',
            },
          },
        ],
      },
      {
        // write files under 10k to inline or copy files over 10k
        test: /\.(woff|woff2|eot|ttf|otf)$/,
        use: [
          {
            loader: 'url-loader',
            options: {
              limit: 10000,
              fallback: 'file-loader',
              name: 'fonts/[name].[ext]',
            },
          },
        ],
      },
    ],
  },
  resolve: {
    ...
  },
  plugins: [
    ...
  ],
  devServer: {
    ...
  },
};
```

two configurations are almost same, so let's see one configuration more deeply.

```js
{
  // write image files under 10k to inline or copy image files over 10k
  test: /\.(jpg|jpeg|gif|png|svg|ico)?$/,
  use: [
    {
      loader: 'url-loader',
      options: {
        limit: 10000,
        fallback: 'file-loader',
        name: 'images/[name].[ext]',
      },
    },
  ],
},
```

- `test: /\.(jpg|jpeg|gif|png|svg|ico)?$/,`: these files will be used by this setting.
- `loader: 'url-loader',`: use url-loader
- `limit: 10000,`: if file size is less than 10k, the file will be inserted into the location that the file is used on(make bundle).
- `fallback: 'file-loader',`: if file size is bigger than 10k, the file is copied by file-loader.
- `name: 'images/[name].[ext]',`: when the file is copied, the file will be `[name].[ext]` in `image` folder.

## Apply Web Font
in here, we use and Google Font([Aguafina Script](https://fonts.google.com/specimen/Aguafina+Script){:rel="nofollow noreferrer" target="_blank"}) to see web font applied surely. first, click the link below and download web font.

- Aguafina Script Font: [https://fonts.google.com/specimen/Aguafina+Script](https://fonts.google.com/specimen/Aguafina+Script){:rel="nofollow noreferrer" target="_blank"}

after downloading, create `src/Assets/Fonts` folder and copy web font file to it. and open `src/App.tsx` and modify it like below.

```js
import * as React from 'react';
import * as ReactDOM from 'react-dom';
import { createGlobalStyle } from 'styled-components';

import Router from './Router';

const GlobalStyles = createGlobalStyle`
  @font-face {
    font-family:'AguafinaScript';
    src: url(${require('~/Assets/Fonts/AguafinaScript-Regular.ttf')});
  }
  body {
    font-family: 'AguafinaScript', sans-serif;
  }
`;

interface Props {}
const App = ({  }: Props) => {
  return (
    <>
      <GlobalStyles />
      <Router />
    </>
  );
};

ReactDOM.render(<App />, document.getElementById('app'));
```

our React project is basedo on [styled-components]({{site.url}}/{{page.categories}}/styled-components/){:target="_blank"}. so we use `createGlobalStyle` in styled-components for global style like below.

```js
const GlobalStyles = createGlobalStyle`
  @font-face {
    font-family:'AguafinaScript';
    src: url(${require('~/Assets/Fonts/AguafinaScript-Regular.ttf')});
  }
  body {
    font-family: 'AguafinaScript', sans-serif;
  }
`;
```

- `src: url(${require('~/Assets/Fonts/AguafinaScript-Regular.ttf')});`: we've used url-loader and file-loader, so we need to use `require` to load the files.

and apply this global style like below.

```js
const App = ({  }: Props) => {
  return (
    <>
      <GlobalStyles />
      <Router />
    </>
  );
};
```

{% include in-feed-ads.html %}

## Use Images
create `src/Assets/images` folder and copy image files to it. I added 2 files(one is bigger than 10k and another is smaller than 10k) to see difference. and then, open the file that you want to use images(`src/Features/Top/index.tsx`) and modify it like below.

```js
...
const Top = ({ match, history, location }: Props) => {
  ...
  return (
    <div>
      ...
      <img src={require('~/Assets/Images/logo.jpg')} />
      <img src={require('~/Assets/Images/ic_account.jpg')} />
      <img src={require('~/Assets/Images/ic_account.svg')} />
    </div>
  );
};

export default Top;
```

we've used `require` to load files like when we've loaded Web font.

## Check
execute the command below to start Webpack dev server.

```bash
npm start
```

and, you can see Web font applied and Images loaded on the screen well.

![use web font and images in React based on Webpack](/assets/images/category/react/2019/image-and-font/check-with-webpack-dev-server.jpg)

as you can see the source code on the right side, files that file size is less than 10k are bundled.

execute the command below to build.

```bash
npm run build
```

and you can see the image file and font file in `dist` folder because that file size is bigger than 10k.

![copy images and web font in React project based on Webpack](/assets/images/category/react/2019/image-and-font/copy-image-font-file-with-webpack.jpg)

