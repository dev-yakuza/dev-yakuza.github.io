---
layout: 'post'
permalink: '/react/create-react-app/react-router/'
paginate_path: '/react/:num/create-react-app/react-router/'
lang: 'en'
categories: 'react'
comments: true

title: React Router in create-react-app
description: Let's see how to use react-router in the React project with create-react-app.
image: '/assets/images/category/react/background.jpg'
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [Prepare project](#prepare-project)
- [Install react-router](#install-react-router)
- [How to use react-router](#how-to-use-react-router)
  - [Router](#router)
  - [Switch-Route](#switch-route)
  - [Link](#link)
  - [useHistory and useParams](#usehistory-and-useparams)
- [Completed](#completed)

</div>

## Outline

React is an UI JavaScript library for the Single page application that focuses to create the UI(User Interface). So, React doesn't provide the features not related to the UI. So, we need to use another library to implement the page navigation feature in React. In this blog post, I will show you how to use react-router in the React project for the page navigation system.

- React Router officail site: [react-router](https://reactrouter.com/){:rel="noopener" target="_blank"}

If you want to know what React is, see the link below.

- [React란]({{site.url}}/{{page.categories}}/create-react-app/react/){:target="_blank"}

You can see full source code of this post on the link below.

- GitHub: [react_router_example](https://github.com/dev-yakuza/study-create-react-app/tree/main/example/react_router_example){:rel="noopener" target="_blank"}

## Prepare project

To implement the page navigation feature by react-router, we'll create a new React project. In this blog post, I'll use the create-react-app and TypeScript to create the project.

- [create-react-app]({{site.url}}/{{page.categories}}/create-react-app/start/){:target="_blank"}
- [TypeScript in create-react-app]({{site.url}}/{{page.categories}}/create-react-app/typescript/){:target="_blank"}

To create the React project based on TypeScript, execute the command below.

```bash
npx create-react-app react_router_example --template=typescript
```

{% include in-feed-ads.html %}

## Install react-router

To use react-router in React, we need to install the react-router package. Exeucte the command below to install react-router.

```bash
npm install --save react-router-dom
npm install --save-dev @types/react-router-dom
```

## How to use react-router

Next, let's see how to use react-router to add the page navigation feature to the React project.

### Router

To use react-router in the React project, we need to use `Router` component, first. Open `./src/index.tsx` file and modify it like the below.

```js
import { BrowserRouter as Router } from 'react-router-dom';

ReactDOM.render(
  <React.StrictMode>
    <Router>
      <App />
    </Router>
  </React.StrictMode>,
  document.getElementById('root')
);
```

When you use the react-router feature in React, you should use the `Router` component. If you use the react-router feature out side of the `Route` component, an error occurs.

### Switch-Route

To implement the page navigation feature by react-router,  we need to define pages with the `Swiech` and `Route` components. Open `./src/App.tsx` file and modify it like the below to check how to use the `Switch` and `Route` components.

```js
import { Switch, Route } from 'react-router-dom';
import { Home } from './Pages/Home';
import { Detail } from './Pages/Detail';

function App() {
  return (
    <div>
      <header>This is header</header>
      <Switch>
        <Route exact path="/">
          <Home />
        </Route>
        <Route path="/detail/:id">
          <Detail />
        </Route>
      </Switch>
    </div>
  );
}
```

we import `Switch` and `Route` components from `react-router-dom`. Also, we import two page components that are not created yet.

```js
import { Switch, Route } from 'react-router-dom';
import { Home } from './Pages/Home';
import { Detail } from './Pages/Detail';
```

And then, we use Switch and Route components like the below.

```js
<div>
  <header>This is header</header>
  <Switch>
    <Route exact path="/">
      <Home />
    </Route>
    <Route path="/detail/:id">
      <Detail />
    </Route>
  </Switch>
</div>
```

Basically, we should use Route component in Switch component. And we should use `path` props to define the target page URL. Lastly, we shouold add the child component for the page when the URL is changed.

As we write the code above, we can show the page that matches the URL, If the page URL has dynamic data parameter, you can define it like `/detail/:id`.

```js
<div>
  <header>This is header</header>
  <Switch>
    ...
  </Switch>
</div>
```

The part under the `Switch` component is the part that is changed by URL. So, the `<header/>` component out side of the `Switch` component is always shown regardless of the URL.

### Link

Next, let's create the Home page component to see how to use Link in react-router. Open the `./src/Pages/Home/index.tsx` file and modify it like the below.

```js
import { Link } from 'react-router-dom';

export const Home = () => {
  return (
    <div>
      <div>
        <Link to="/detail/1">Detail 1</Link>
      </div>
      <div>
        <Link to="/detail/2">Detail 2</Link>
      </div>
    </div>
  );
};
```

You should use the `<link/>` component instead of `<a/>` tag for the link for the page navigation in react-router. This Link component ahs the `to` Props, and you should add the target URL to this Props.

{% include in-feed-ads.html %}

### useHistory and useParams

Next, let's see how to use `useHistory` and `useParams` by creating the Detail page component. Open the `./src/Pages/Detail/index.tsx` file and modify it like the below.

```js
import { useHistory, useParams } from 'react-router-dom';

export const Detail = () => {
  const { goBack } = useHistory();
  const params: { id: string } = useParams();

  return (
    <div>
      <div>Detail {params.id}</div>
      <button onClick={goBack}>GoBack</button>
    </div>
  );
};
```

When you use the `useHistory` hook of react-router, you can move the page by progmramming. The `useHistory` hook provides `replace`, `push` and `goBack` functions.

- replace: replace the current page to the passed URL. We can go back the page with the browser back button.
- push: move the page to the passed URL. We can go back the page with the browser back button.
- goBack: this is a same feature of the browser back button.

We can use the `useParams` hook of react-rotuer to get the URL parameter. We've bound the Detail page component to the URL like the below.

```js
<Route path="/detail/:id">
  <Detail />
</Route>
```

And, we've assigned data to the URL parameter like the below in the Home page component.

```js
<div>
  <Link to="/detail/1">Detail 1</Link>
</div>
<div>
  <Link to="/detail/2">Detail 2</Link>
</div>
```

At this time, the `1`, `2` are assigned to `:id` parameter. When you use `useParams`, you can get teh value assigned `:id` like the below.

```js
const params: { id: string } = useParams();
...
<div>Detail {params.id}</div>
```

## Completed

Done! we've seen how to use react-router to chagne the pages in React. react-router has many features besides the features introduced in this blog. If you want to know more features, please check them on the official site.

- React Router official site: [Quick Start](https://reactrouter.com/web/guides/quick-start){:rel="noopener" target="_blank"}
