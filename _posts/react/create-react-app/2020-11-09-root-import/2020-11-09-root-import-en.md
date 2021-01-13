---
layout: 'post'
permalink: '/react/create-react-app/root-import/'
paginate_path: '/react/:num/create-react-app/root-import/'
lang: 'en'
categories: 'react'
comments: true

title: '[TypeScript] Make Import path based on Root in create-react-app'
description: Let's see how to use the absolute path for importing components in the create-react-app project with TypeScript.
image: '/assets/images/category/react/create-react-app/typescript/background.jpg'
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [Absolute path and relative path](#absolute-path-and-relative-path)
- [Create a project](#create-a-project)
- [Configure the absolute path](#configure-the-absolute-path)
- [How to use](#how-to-use)
- [Completed](#completed)

</div>

## create-react-app series

This blog post is a series. You can see other blog posts of the series on the list.

- [What is React]({{site.url}}/{{page.categories}}/create-react-app/react/){:target="_blank"}
- [create-react-app]({{site.url}}/{{page.categories}}/create-react-app/start/){:target="_blank"}
- [TypeScript in create-react-app]({{site.url}}/{{page.categories}}/create-react-app/typescript/){:target="_blank"}
- [TypeScript] Make Import path based on Root in create-react-app
- [Jest]({{site.url}}/{{page.categories}}/create-react-app/jest/){:target="_blank"}

## Outline

In the previous blog post, I introduced how to apply Typescript to the React project created by `create-react-app`. In this blog post, I will show you how to configure the React TypeScript project to import components by the absolute path instead of the relative path.

You can see the source code of the blog post on the link below.

- GitHub: [https://github.com/dev-yakuza/study-create-react-app/tree/main/3.root-import](https://github.com/dev-yakuza/study-create-react-app/tree/main/3.root-import){:rel="noopener" target="_blank"}

## Absolute path and relative path

When we develop the project with React, we develop the app based on components. When we develop the React project, first, we develop many components, and we combine them to make pages.

When we combine the components to create the pages, normally we use the relative path(`import Button from '../../Button'`) to import the components.

If you have not too many components, you don't feel any inconvenience to use the relative path, but if your project is bigger and the folder structures are complicated, you'll confuse which components you want to import and where the components are from.

To solve this problem, I will introduce how to use the absolute path (`import Button from 'Button'`) to import the components in this blog post.

{% include in-feed-ads.html %}

## Create a project

Execute the command below to create the React project with TypeScript.

```bash
npx create-react-app root-import --template=typescript
```

And then, execute the command below to start the React project.

```bash
# cd root-import
npm start
```

If you don't have any problem to execute the React project, you can see the screen below on your browser.

![create-react-app with typescript](/assets/images/category/react/create-react-app/root-import/project.jpg)

## Configure the absolute path

If you use the React project with TypeScript, it's very simple to configure to use the absolute path. You can use the absolute path by modifying the TypeScript configuration.

Open the `tsconfig.json` file and modify it like below.

```json
{
  "compilerOptions": {
    ...
    "jsx": "react-jsx",
    "baseUrl": "src"
  },
  ...
}
```

Done! it's pretty simple.

## How to use

Let's see how to use the absolute path to import the components. First, create `./src/Components` folder and move `App.js`, `App.css`, `App.test.tsx`, `logo.svg` files to the folder.

And then, open `./src/index.js` file and modify it like below.

```js
...
import App from 'Components/App';
...
```

After it, execute the command below to start the React project.

```bash
npm start
```

If you configure well, you can see the screen below on your browser.

![create-react-app with typescript](/assets/images/category/react/create-react-app/root-import/project.jpg)

Currently, the absolute path looks like no merit, but if your React project becomes bigger and bigger, definitely, you can see the benefit of the absolute path.

## Completed

We've seen how to use the absolute path to import the components in the TypeScript React project created by create-react-app. At the beginning of the project, you don't feel any merit, but when the project becomes, you really see the benefit of the absolute path.
