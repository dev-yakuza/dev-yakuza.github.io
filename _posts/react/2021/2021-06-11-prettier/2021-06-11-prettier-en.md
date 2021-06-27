---
layout: 'post'
permalink: '/react/prettier/'
paginate_path: '/react/:num/prettier/'
lang: 'en'
categories: 'react'
comments: true

title: '[React] Prettier'
description: Let's see how to keep the same code format by Prettier in React.
image: '/assets/images/category/react/2021/prettier/background.png'
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [Prepare project](#prepare-project)
- [Prettier Installation](#prettier-installation)
- [Prettier configuration](#prettier-configuration)
- [Check format](#check-format)
- [Formatting](#formatting)
- [Configure package.json](#configure-packagejson)
- [Configure Editor](#configure-editor)
- [Completed](#completed)

</div>

## Blog series

This blog post is a series. You can see the other posts on the link below.

- [React] Prettier
- [[React] ESLint]({{site.url}}/{{page.categories}}/eslint/){:target="_blank"}
- [[React] Husky, lint-staged]({{site.url}}/{{page.categories}}/husky-lint-staged/){:target="_blank"}
- [[React] GitHub Actions]({{site.url}}/{{page.categories}}/github-actions/prettier-eslint/){:target="_blank"}

## Outline

When you develop alone, the code format(space, tab, quotation, etc) is not a big problem. However, when you work with other programmers, each programmer can use a different code format. If the code format is different, it's hard to read and understand the code and it's possible to make bugs.

Prettier is a code formatter to make the same style of the code by predefined the code format.

- [Prettier](https://prettier.io/){:rel="noopener" target="_blank"}

In this blog post, I will introduce how to configure the Prettier and how to use Prettier to make the same style of the code in React.

## Prepare project

In this blog post, to use Prettier, we'll create the React project by `create-react-app`. If you want to know more details about `create-react-app`, see the link below.

- [create-react-app]({{site.url}}/{{page.categories}}/create-react-app/start/){:target="_blank"}

Execute the command below to create a new React project for Prettier.

```bash
npx create-react-app prettier_example
```

{% include in-feed-ads.html %}

## Prettier Installation

To use Prettier in React, we need to install the Prettier library. Execute the command below to install Prettier library.

```bash
# cd prettier_example
npm install --save-dev prettier
```

## Prettier configuration

To use Prettier in React, we need to define the code format. Create the `.prettierrc.js` file and modify it like below to define the code format.

```js
module.exports = {
  jsxBracketSameLine: true,
  singleQuote: true,
  trailingComma: 'all',
  printWidth: 100,
};
```

You can see the other options on the Prettier official site.

- Prettier official site: [Options](https://prettier.io/docs/en/options.html){:rel="noopener" target="_blank"}

Check the options and configure them for your project.

## Check format

You can find the files are not following the format that we've defined by executing the command below.

```bash
npx prettier --check ./src
```

After executing the command, you can see the file list not following the code format.

```bash
[warn] public/index.html
[warn] src/App.js
[warn] src/index.css
[warn] src/index.js
[warn] src/reportWebVitals.js
[warn] Code style issues found in the above file(s). Forgot to run Prettier?
```

## Formatting

You can automatically fix the file follows the code format that we've defined by executing the command below.

```bash
prettier --write ./src
```

After executing the command below, you can see the file list fixed with the format.

```bash
.prettierrc.js 40ms
package-lock.json 441ms
package.json 25ms
public/index.html 55ms
public/manifest.json 4ms
README.md 49ms
src/App.css 44ms
src/App.js 17ms
src/App.test.js 10ms
src/index.css 7ms
src/index.js 6ms
src/reportWebVitals.js 8ms
src/setupTests.js 3ms
```

After that, execute the command below to check the files formatted well.

```bash
npx prettier --check ./src
```

You can see all files formatted well.

```bash
Checking formatting...
All matched files use Prettier code style!
```

## Configure package.json

When we use the `package.json` file, we can use the `check` and `write` commands simpler. Open the `package.json` file and modify it like the below.

```json
"scripts": {
  ...
  "format": "prettier --check ./src",
  "format:fix": "prettier --write ./src"
},
```

If you modify the `package.json` file, you can use the commands below to use Prettier.

```bash
npm run format
npm run format:fix
```

{% include in-feed-ads.html %}

## Configure Editor

Prettier supports various editors. You can see the editor list that you can use Prettier on the link below.

- Prettier official site: [Editor Integration](https://prettier.io/docs/en/editors.html){:rel="noopener" target="_blank"}

In this blog post, I will show you how to configure Prettier in `VSCode`. Install VSCode Prettier plugin by clicking the link below.

- VSCode Plugin: [Prettier - Code formatter](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode){:rel="noopener" target="_blank"}

After installing, open VSCode, and press `(macOS) cmd + shift + p` or `(windows) ctrl + shift + p` and search `open settings`.

![vscode command palette](/assets/images/category/react/2021/prettier/vscode-command-palette.jpg)

Select `Preference: Open Setting(JSON)` and modify the file like the below.

```json
{
  ...
  "editor.formatOnSave": true,
  "[typescriptreact]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[typescript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[javascript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[javascriptreact]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[json]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  }
}
```

Or you can simply modify it like the below.

```json
{
  ...
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode"
}
```

After modifying, when you modify a file and save it, you can see the code of the file is fomatted automatically.

## Completed

Done! we've seen how to use Prettier in the React project. Please configure Prettier and use it to make the same style of the code!
