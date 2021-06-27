---
layout: 'post'
permalink: '/react/github-actions/prettier-eslint/'
paginate_path: '/react/:num/github-actions/prettier-eslint/'
lang: 'en'
categories: 'react'
comments: true

title: '[React] GitHub Actions for Prettier and ESLint'
description: Let's see how to execute Prettier and ESLint by GitHub Actions in React.
image: '/assets/images/category/react/background.jpg'
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [GitHub Actions](#github-actions)
- [Check](#check)
- [Complated](#complated)

</div>

## Blog series

This blog post is a series. You can see the other posts on the link below.

- [[React] Prettier]({{site.url}}/{{page.categories}}/prettier/){:target="_blank"}
- [[React] ESLint]({{site.url}}/{{page.categories}}/eslint/){:target="_blank"}
- [[React] Husky, lint-staged]({{site.url}}/{{page.categories}}/husky-lint-staged/){:target="_blank"}
- [React] GitHub Actions

## Outline

Until now, we've configured Prettier and ESLit to the React project with create-react-app, and we've used husky and lint-staged to execute Prettier and ESLint automatically. In this blog post, I will show you how to use GitHub Actions to execute Prettier and ESlint when Pull request is created.

- GitHub official site: [Actions](https://github.com/features/actions){:rel="noopener" target="_blank"}

You can see the full source code of the blog post on the link below.

- GitHub: [Todo](https://github.com/dev-yakuza-example/todo){:rel="noopener" target="_blank"}

## GitHub Actions

To use GitHub Actions, let's make GitHub Actions configuration file. Create the `./.github/workflows/main.yml` file and modify it like the below.

```yaml
name: Check the source code
on:
  pull_request:
    branches:
      - main
jobs:
  test:
    name: Check the source code
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Install packages
        run: npm ci
      - name: Prettier
        run: npm run format
      - name: Lint
        run: npm run lint
```

Let's see the code one by one.

{% include in-feed-ads.html %}

This GitHub Actions name is `Check the source code`.

```yaml
name: Check the source code
...
```

This GitHub Actions is executed when the `main` branch gets `Pull Request`.

```yaml
...
on:
  pull_request:
    branches:
      - main
...
```

This GitHub Actions has a Flow named `Check the source code`, and is executed on `ubuntu`.

```yaml
...
jobs:
  test:
    name: Check the source code
    runs-on: ubuntu-latest
...
```

First, get the source code from Repositoy.

```yaml
...
jobs:
  test:
    ...
    steps:
      - uses: actions/checkout@v2
...
```

And then, install the Node packages on the source code, and execute the `npm` scripts of Prettier and ESLint that we've defined before.

```yaml
...
jobs:
  test:
    ...
    steps:
      ...
      - name: Install packages
        run: npm ci
      - name: Prettier
        run: npm run format
      - name: Lint
        run: npm run lint
```

After modifying the file, execute the commands below to upload it to GitHub.

```bash
git add .
git commit -m 'Add GitHub Actions'
git push origin main
```

{% include in-feed-ads.html %}

## Check

Let's check GitHub Actions working well. Execute the command below to make a new branch.

```bash
git checkout -b test-pr
```

And the, open the `./src/App.tsx` file and modify it like the below.

```js
const App = (): JSX.Element => {
  console.log('test!');
  return (
    ...
  );
};
```

And then, execute the commands below to upload it to GitHub.

```bash
git add .
git commit -m 'Add test code'
git push origin test-pr
```

If you can't `commit` because of husky and lint-staged that we've defined, open the `./package.json` file and delete the code like below.

```json
{
  ...
  "husky": {
    "hooks": {
      "pre-commit": "lint-staged"
    }
  },
  "lint-staged": {
    "src/**/*.{ts,tsx}": [
      "eslint --ext .tsx --ext .ts ./src"
    ],
    "./src/**": [
      "prettier --check ./src"
    ]
  },
  ...
}
```

And then, execute the commands below again to upload the modified contents to GitHub.

```bash
git commit -m 'Add test code'
git push origin test-pr
```

After uploading to GitHub, go to the GitHub site, and click the `Pull requests` tab, and the click `New pull request` to create a new Pull Request.

![GitHub create pull request](/assets/images/category/react/2021/github-actions/create-pull-request.jpg)

If you configure GitHub Actions well, you can seel the error of GitHub Actions on the bottom of `Pull request` you've created.

![GitHub actions error](/assets/images/category/react/2021/github-actions/github-actions-error.jpg)

When you click the `Details` on the right side, you can see the details of the GitHub Actions error.

![GitHub actions error details](/assets/images/category/react/2021/github-actions/github-actions-error-details.jpg)

You can see the details about that one file doesn't follow the ESLint rules we've set. Through this, we can know the GitHub Actions that we've set is working well.

## Complated

Done! we've seen how to execute Prettier and ESLint by GitHub Actions. We can know the problems by husky and lint-staged, but all developers are not in same developmenet environment. Now, we can execute the Prettier and ESlint on the same environment created by GitHub actions to check the source code!

You can implement various features with GitHub Actions in addition to Prettier and ESLint. Please try to implement `CI/CD` with GitHub Actions!
