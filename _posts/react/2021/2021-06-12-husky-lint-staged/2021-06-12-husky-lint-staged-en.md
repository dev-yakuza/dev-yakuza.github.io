---
layout: 'post'
permalink: '/react/husky-lint-staged/'
paginate_path: '/react/:num/husky-lint-staged/'
lang: 'en'
categories: 'react'
comments: true

title: '[React] husky, lint-staged'
description: Let's see how to use husky and lint-staged to execute ESLint and Prettier automatically when you commit the code to Git.
image: '/assets/images/category/react/2021/husky-lint-staged/background.jpg'
published: false
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [Prepare project](#prepare-project)
- [husky](#husky)
- [lint-staged](#lint-staged)
- [configure husky and lint-staged](#configure-husky-and-lint-staged)
- [Completed](#completed)

</div>

## Blog series

This blog post is a series. You can see the other posts on the link below.

- [[React] Prettier]({{site.url}}/{{page.categories}}/prettier/){:target="_blank"}
- [[React] ESLint]({{site.url}}/{{page.categories}}/eslint/){:target="_blank"}
- [React] Husky, lint-staged
- [[React] GitHub Actions]({{site.url}}/{{page.categories}}/github-actions/){:target="_blank"}

## Outline

On the previous blog posts, we've seen how to configure Prettier and ESLint, and how to use them on the React project with create-react-app.

In this blog post, I will show you how to use `husky` and `lint-staged` to use Prettier and ESLint.

## Prepare project

To use husky and lint-staged on React, we'll create the simple project with `create-react-app`. If you want to know more details about `create-react-app`, see the link below.

- [create-react-app]({{site.url}}/{{page.categories}}/create-react-app/start/){:target="_blank"}

Execute the command below to create a new React project that we'll use for husky and lint-staged.

```bash
npx create-react-app husky_lint_example --template=typescript
```

I use `TypeScript` to develop React, so I use the `--template=typescript` option to create the React project. And then, you should configure Prettier and ESLint to this React project. If you don't know how to configure Prettier and ESLint, see the links below.

- [Prettier]({{site.url}}/{{page.categories}}/prettier/){:target="_blank"}
- [ESLint]({{site.url}}/{{page.categories}}/eslint/){:target="_blank"}

{% include in-feed-ads.html %}

## husky

Git has the `Hook` feature. You can configure the Hook to the event, and execute the script by Hook when Git gets specific events(like commit, push, etc).

husky helps you use Git Hook simply.

- husky official site: [https://typicode.github.io/husky/](https://typicode.github.io/husky/){:rel="noopener" target="_blank"}

Execute the command below to install husky.

```bash
npm install --save-dev husky
```

## lint-staged

lint-staged, is normally used with husky, helps you execute specific commands to Staged files on Git.

- lint-staged official page: [https://github.com/okonet/lint-staged](https://github.com/okonet/lint-staged){:rel="noopener" target="_blank"}

Staged files on Git means the files are modified and added by you execute the `git add` command. If you modify Staged files, you should execute `git add` again to add them.

lint-staged helps you not execute the `gid add` command when you modify Staged files.

Execute the command below to install lint-sgated to use it with husky.

```bash
npm install --save-dev lint-staged
```

{% include in-feed-ads.html %}

## configure husky and lint-staged

Next, let's configure husky and lint-staged to execute the ESLint and Prettier when you commit to Git.

Open the `package.json` file and modify it like the below to configure husky and lint-staged.

```json
{
  ...
  "scripts": {
    ...
  },
  "lint-staged": {
    "src/**/*.{ts,tsx}": [
      "eslint --ext .tsx --ext .ts ./src --fix"
    ],
    "./src/**": [
      "prettier --write ."
    ]
  },
  "husky": {
    "hooks": {
      "pre-commit": "lint-staged"
    }
  },
  ...
}
```

After modifying, when you commit to Git, lit staged is executed by pre-commit of husky, and ESLint and Prettier are executed by lint-staged.

## Completed

Done! we've seen how to configure husky and lint-staged to execute ESLint and Prettier on the React project. Please use husky and lint-staged to execute automatically ESLint and Prettier!
