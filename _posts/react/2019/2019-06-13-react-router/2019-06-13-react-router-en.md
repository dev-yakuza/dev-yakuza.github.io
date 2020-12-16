---
layout: 'post'
permalink: '/react/react-router/'
paginate_path: '/react/:num/react-router/'
lang: 'en'
categories: 'react'
comments: true

title: 'React Router'
description: let's see how to use react-router to route the page in React.
image: '/assets/images/category/react/2019/react-router/background.jpg'
---

## Outline
React is SPA(Single Page Application). literally, React is one page application. so routing pages is impossible because it's single page. however, `React Router` makes React be able to route pages according to URL like normal websites.

- React Router: [https://github.com/ReactTraining/react-router](https://github.com/ReactTraining/react-router){:rel="nofollow noreferrer" target="_blank"}
- React Router Training: [https://reacttraining.com/react-router/](https://reacttraining.com/react-router/){:rel="nofollow noreferrer" target="_blank"}

we can use React Router for the web(react-router-dom) and for the native(react-router-native). in this blog post, we'll see how to use React Router(react-router-dom) to route pages in React project.

on Github, you can see full source code that I use in this blog post.

- Github: [https://github.com/dev-yakuza/react_router](https://github.com/dev-yakuza/react_router){:target="_blank"}

## Prepare Project
React project introduced in here was applied the contents below. you can see more details on each link.

- [Start React With Webpack]({{site.url}}/{{page.categories}}/start/){:target="_blank"}
- [Use Typescript In React]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}
- [Use styled-components in React]({{site.url}}/{{page.categories}}/styled-components/){:target="_blank"}
- [Make Import path based on Root in React]({{site.url}}/{{page.categories}}/root-import/){:target="_blank"}


if you make React project by following the previous blog posts, you can get the folder structure like below. I've created namded react_router instead of react_root_import.

```bash
|-- src
|   |-- Components
|   |   |-- Title
|   |   |   |-- index.tsx
|   |-- Features
|   |   |-- Top
|   |   |   |-- index.tsx
|   |-- index.html
|   |-- App.tsx
|-- .babelrc
|-- package.json
|-- webpack.config.js
```

{% include in-feed-ads.html %}

## Install react-router-dom
execute the command below to install `react-router-dom`.

```bash
npm install --save react-router-dom
npm install --save-dev @types/react-router-dom
```

- react-router-dom: this is React Router library.
- @types/react-router-dom: it's type definitions of react-router-dom for Typescript.

## Add Pages
we need to make test pages for routing pages. create `src/Features/Page1.tsx` and modify it like below.

```js
import * as React from 'react';
import { Link, RouteComponentProps } from 'react-router-dom';

import Title from '~/Components/Title';

interface Props extends RouteComponentProps {}

const Page1 = ({ history }: Props) => {
  return (
    <div>
      <a onClick={history.goBack}>Previous Page</a>
      <Link to="/">Top</Link>
      <Link to="/page2">Page 2</Link>
      <Title label="Page 1" />
    </div>
  );
};

export default Page1;
```

- if our components are called by react-router, the components have `hisotry`, `location`, `match` props. for this props, I defined the props extended `RouteComponentProps`.
- {% raw %}`<a onClick={history.goBack}>Previous Page</a>`{% endraw %}: I made a link to go back the page by using Props(`history`) from react-router.
- {% raw %}`<Link to="/">Top</Link>`{% endraw %}: we need to use `Link` component to make links in react-router-dom.

let's make same page like above. create and modify `src/Features/Page2.tsx` like below.

```js
import * as React from 'react';
import { Link, RouteComponentProps } from 'react-router-dom';

import Title from '~/Components/Title';

interface Props extends RouteComponentProps {}

const Page2 = ({ history }: Props) => {
  return (
    <div>
      <a onClick={history.goBack}>Previous Page</a>
      <Link to="/">Top</Link>
      <Link to="/page1">Page 1</Link>
      <Title label="Page 2" />
    </div>
  );
};

export default Page2;
```

lastly, modify `Top` page we've made before lik below.

```js
import * as React from 'react';
import { Link, RouteComponentProps } from 'react-router-dom';

import Title from '~/Components/Title';

interface Props extends RouteComponentProps {}
const Top = ({ match, history, location }: Props) => {
  console.log(match);
  console.log(history);
  console.log(location);
  return (
    <div>
      <Link to="/page1">Page 1</Link>
      <Link to="/page2">Page 2</Link>
      <Title label="Hello World!" />
    </div>
  );
};

export default Top;
```

{% include in-feed-ads.html %}

## Create Router
I make one file for managing Routing and add all routes in there. it's my rules, so you don't have to follow this style. you can make your style to manage routing. in my case, I've made `src/Router.tsx` and modify it like below.

```js
import * as React from 'react';
import { BrowserRouter, Route, Switch, Redirect } from 'react-router-dom';

import Top from './Features/Top';
import Page1 from './Features/Page1';
import Page2 from './Features/Page2';

const Router = () => {
  return (
    <BrowserRouter>
      <Switch>
        <Route exact={true} path="/" component={Top} />
        <Route path="/page1" component={Page1} />
        <Route path="/page2" component={Page2} />
        {/* Not Found */}
        <Route component={() => <Redirect to="/" />} />
      </Switch>
    </BrowserRouter>
  );
};

export default Router;
```

- BrowserRouter: this component is for using react-router on Web(Browser).
- Switch: show first component corresponding the route.
- Route: show the component depends on the URL.

I think we need to see more details about `Switch`. let's modify our settings like below.

```js
<BrowserRouter>
    <Switch>
        <Route exact={true} path="/" component={Top} />
        <Route path="/page1" component={Page1} />
        <Route path="/page1" component={Page2} />
        <Route path="/page2" component={Page2} />
        {/* Not Found */}
        <Route component={() => <Redirect to="/" />} />
    </Switch>
</BrowserRouter>
```


and then, execute the command below to execute Webpack dev server.

```bash
npm start
```

and then, go to `page1` via browser link. you can see only `Page1` in the screen. however, if you remove `Switch` like below,

```js
<BrowserRouter>
    <Route exact={true} path="/" component={Top} />
    <Route path="/page1" component={Page1} />
    <Route path="/page1" component={Page2} />
    <Route path="/page2" component={Page2} />
    {/* Not Found */}
    <Route component={() => <Redirect to="/" />} />
</BrowserRouter>
```

and go to the `page1` via browser link, you can see `Page1` and `Page2` both in the screen. like this case, `Switch` only shows first component if there are same URL.


## Modify App.tsx
lastly, we need to modify `src/App.tsx` to use Router like below.

```js
import * as React from 'react';
import * as ReactDOM from 'react-dom';

import Router from './Router';

interface Props {}
const App = ({  }: Props) => {
  return <Router />;
};

ReactDOM.render(<App />, document.getElementById('app'));
```

## Modify Webpack
in this status, when you execute `npm start`, you can see Top page and you can route other pages via links. however, if you browser `http://localhost:8080/page1` or `http://localhost:8080/page2` directly, you get 404 response. we've already talked about it above, React is SPA(Single Page Application), so we get this kind of problem because a real page is just one. we'll modify Webpack configuration to solve this proble. open `webpack.config.js` and modify it like below.

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
  devServer: {
    contentBase: './dist',
    port: 3000,
    historyApiFallback: true,
  },
};
```

we've set `devServer` option like above for `webpack-dev-server`. `historyApiFallback` option returns `index.html` response instead of 404 response if the page does not exist corresponding to the URL. now, when we browser directly `http://localhost:3000/page1` or `http://localhost:3000/page2` again, we can see the page shown well.

## Check
execute the command below to execute Webpack dev server.

```bash
npm start
```

and then, ope the browser and go to `http://localhost:3000/`.(at Git source code, we've used `--open` option, so the browser is opend and go to the page automatically.)

click the links to go to other pages. you can see the page and URL is changed. alos, browser `http://localhost:3000/page1` or `http://localhost:3000/page2` directly. you can see pages shown well.

lastly, execute the command below to build.

```bash
npm run build
```

after it, you can see files and folders created well in `dist/`.