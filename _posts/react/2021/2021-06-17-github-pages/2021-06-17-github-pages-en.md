---
layout: 'post'
permalink: '/react/github-pages/'
paginate_path: '/react/:num/github-pages/'
lang: 'en'
categories: 'react'
comments: true

title: '[React] Deploy to GitHub Pages'
description: Let's deploy the React project created by create-react-app to GitHub Pages.
image: '/assets/images/category/react/background.jpg'
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [Prepare project](#prepare-project)
- [Build](#build)
- [Upload](#upload)
  - [Public repository](#public-repository)
  - [Private Repository](#private-repository)
- [Configue GitHub Pages](#configue-github-pages)
- [Solve issues](#solve-issues)
  - [PUBLIC_URL](#public_url)
  - [404 page](#404-page)
- [Completed](#completed)

</div>

## Outline

GitHub Pages is one of the GitHub features that you can serve the static files for the web pages. In this blog post, I will show you how to deploy the React project created by `create-react-app` to `GitHub Pages`.

- React official site: [Deployment](https://create-react-app.dev/docs/deployment/){:rel="noopener" target="_blank"}

You can see full source code of the blog post in the link below.

- GitHub: [Todo](https://github.com/dev-yakuza-example/todo){:rel="noopener" target="_blank"}

## Prepare project

In this blog post, I will use the React project created by `create-react-app` with `react-router` to deploy to GitHub Pages. If you want to know how to use `create-react-app` and how to apply `react-router`, please see the following links.

- [create-react-app]({{site.url}}/{{page.categories}}/create-react-app/start/){:target="_blank"}
- [[React] React Router]({{site.url}}/{{page.categories}}/react-router/){:target="_blank"}

To depoly the React project to GitHub Pages, you need a `Public` repository. If the project is in the Private repository, create a new Public repository. If the project is in the Public repository, you can use the same repository to deploy to GitHub Pages.

## Build

To deploy the React project created by create-react-app, we need to `build` the React project. Execute the following command to `build` the React project.

```bash
npm run build
```

{% include in-feed-ads.html %}

## Upload

Now, we need to upload this build files to GitHub.

### Public repository

If the React project is already under the Public repository, you just need to upload the `build` folder created by the build command. Open the `.gitignore` file and modify it like the below.

```bash
# production
# /build
```

After modifying the `.gitignore` file, execute the following command to upload the build folder.

```bash
git commit -am 'Add build folder'
git push origin main
```

GitHub Pages serves the static files on the specific Branch. So, you need to create a new Branch for the build folder. Execute the following command to upload the build folder to a new Branch.

```bash
git subtree push --prefix build/ origin gh-pages
```

### Private Repository

GitHub Pages does not support the Private repository. So, if your project that you want to deploy is in the Private repository, you need to create a new Public repository and upload the build folder to it.

Execute the following command to upload the build folder to the new Public repository.

```bash
cd build
git init
git remote add origin GITHUB_PUBLIC_REPOSITORY_URL
git commit -am 'Add build folder'
git push origin main
```

## Configue GitHub Pages

To serve the static files for the web page by GitHub Pages, you need to activate the GitHub Pages feature on the project. Go to GitHub site that you uploaded the `build` folder.

![GitHub pages configuration](/assets/images/category/react/2021/github-pages/settings.jpg)

When you go to GitHub, click `Settings` > `Pages` to go to the GitHub Pages configuration page. And then, select the branch that you want to serve via GitHub Pages and click the `Save` button.

GitHub recognizes the `gh-pages` branch as GitHub Pages branch. So, if you upload the build folder to the `gh-pages` branch, you don't need to do anything. Just, GitHub Pages will serve the static files.

After configuration, you can see the URL of your GitHub Pages. When you click it, you can see the project is not served yet.

{% include in-feed-ads.html %}

## Solve issues

There are some issues that the React project created by `create-react-app` with `react-router` to serve on the GitHub Pages.

### PUBLIC_URL

The React project that is created by create-react-app is based on the root(`/`) URL for the project. However, GitHub Pages is based on the URL with the repository name. So, we need to change base URL from the root to the repository name.

First, open `./package.json` file and add the `homepage` field like the below.

```json
{
  ...,
  "homepage": "https://dev-yakuza-org.github.io/todo"
}
```

The URL of the `homepage` field is the full URL of the GitHub Pages without `/` at the end.

And the find the source code that uses `BrowserRouter` of react-router and modify it like the below. I used `BrowserRouter` in `./src/index.tsx`.

```js
...
import { BrowserRouter as Router } from 'react-router-dom';

ReactDOM.render(
  <React.StrictMode>
    <Router basename={process.env.PUBLIC_URL}>
      <App />
    </Router>
  </React.StrictMode>,
  document.getElementById('root'),
);
...
```

Set `PUBLIC_URL` to `basename` of `BrowserRouter`. In here, `PUBLIC_URL` is the URL that we've configured on the `package.json` file.

After all modificatons, execute the following command to deploy the React project.

```bash
npm run build
git commit -am 'Add hompage'
git push origin main
git subtree push --prefix build/ origin gh-pages
```

If the project is under Private repository,

```bash
npm run build
cd build
git init
git remote add origin GITHUB_PUBLIC_REPOSITORY_URL
git commit -am 'Add hompage'
git push origin main
```

And then, when you open the GitHub Pages URL, you can see the project shown up well unlike before.

### 404 page

React is SPA(Single Page Application), so it serves the service with one single page(index.html). So, When you deploy the React project, you need to make all URL point to the index.html. However, GitHub Pages does not support that feature.

To solve this issue, we need to use a trick. When the user access wrong URL of the GitHub pages, the GitHub Pages will show the 404 page. And we can customize the 404 page in GitHub Pages. By using this, we can make all URL shows a single page.

So, to solve this issue, copy the `./build/index.html` file to the `./build/404.html` file. And the upload the copied file to GitHub Pages.

After deploying, when the user access the root URL of the GitHub Pages, the `./build/index.html` file will be opened and the React project will work well. If the user access not root URL, the page does not exist, the `./build/404.html` file will be served. However, the `404.html` page is same with the `index.html`. So, the React project will work well.

To automate this process, open the `./package.json` file and modify it like the below.

```json
...
"scripts": {
  ...
  "build": "react-scripts build",
  "postbuild": "cp build/index.html build/404.html",
  ...
},
...
```

After modifying, when you build the project, the `./build/index.html` file will be copied to the `./build/404.html` file.

## Completed

Done! we've seen how to deploy the React project that is created by create-react-app with react-router to GitHub Pages. Now, you can serve your React portfolio projects on GitHub Pages for free.

Thanks to GitHub and Microsoft for providing GitHub Pages to serve the portfolio for free like this.
