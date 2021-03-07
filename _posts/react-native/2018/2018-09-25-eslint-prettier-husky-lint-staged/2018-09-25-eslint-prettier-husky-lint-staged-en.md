---
layout: 'post'
permalink: '/react-native/eslint-prettier-husky-lint-staged/'
paginate_path: '/react-native/:num/eslint-prettier-husky-lint-staged/'
lang: 'en'
categories: 'react-native'
comments: true

title: Use ESLint, Prettier like Pro on React Native
description: Let's see how to use ESLint and Prettier on React Native project, and Let's see how to use Husky and lint-staged to use ESLint and Prettier like Pro.
image: '/assets/images/category/react-native/2018/eslint-prettier-husky-lint-staged/background.jpg'
---

<div id="contents_list" markdown="1">

## Content

- [Outline](#outline)
- [Prepare React Native project](#prepare-react-native-project)
- [ESLint](#eslint)
  - [Install ESLint](#install-eslint)
  - [Configure ESLint](#configure-eslint)
  - [ESLint detail configurations](#eslint-detail-configurations)
  - [Prepare to execute ESLint](#prepare-to-execute-eslint)
  - [Execute ESLint](#execute-eslint)
  - [eslint --fix](#eslint---fix)
  - [Use ESLint on VSCode](#use-eslint-on-vscode)
- [Prettier](#prettier)
  - [Install Prettier](#install-prettier)
  - [Configure Prettier](#configure-prettier)
  - [Configure Prettier on ESLint](#configure-prettier-on-eslint)
  - [Prepare to execute Prettier](#prepare-to-execute-prettier)
  - [Execute Prettier](#execute-prettier)
  - [prettier --write](#prettier---write)
  - [Use Prettier on VSCode](#use-prettier-on-vscode)
- [Use ESLint and Prettier like Pro](#use-eslint-and-prettier-like-pro)
  - [Husky](#husky)
  - [lint-staged](#lint-staged)
  - [How to use Husky and lint-staged](#how-to-use-husky-and-lint-staged)
- [Solve problems](#solve-problems)
- [Completed](#completed)

</div>

## Outline

In this blog post, I will introduce what ESLint is and What Prettier is, and how to use ESLint and Prettier on React Native.

Also, I will introduce Husky and lint-staged, and how to use them like Pro.

You can see ESLint and Prettier settings, that introduced in here, on Github below.

- Github: [react-native-eslintrc-prettier](https://github.com/dev-yakuza/react-native-eslintrc-prettier){:rel="nofollow noreferrer" target="_blank"}

## Prepare React Native project

In this blog post, we will use the React Native based on Typescript.

If you want to know how to integrate Typescript to React Native, see the link below.

- [How to integrate Typescript to React Native]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}

## ESLint

ESLint is the compound language of ES(EcmaScript) + Lint(show error code), and analyzes the source code, and the tool that helps to make them the same style.

### Install ESLint

Execute the command below to install ESLint on React Native. (ESLint is basically installed on React Native, so you can skip this command)

```bash
# cd SampleApp
npm install --save-dev eslint
```

{% include in-feed-ads.html %}

### Configure ESLint

Next, let's see how to configure ESLint for React Native.

Execute the command below to initialize ESLint.

```bash
# cd SampleApp
npx eslint --init
```

After executing the command above, you can see the screen like below.

```bash
? How would you like to use ESLint? (Use arrow keys)
  To check syntax only
  To check syntax and find problems
❯ To check syntax, find problems, and enforce code style
```

In here, I selected `To check syntax, find problems, and enforce code style` to check style and fix it automatically.

```bash
? What type of modules does your project use? (Use arrow keys)
❯ JavaScript modules (import/export)
  CommonJS (require/exports)
  None of these
```

On React Native, `import/export` is mainly used, so select `JavaScript modules (import/export)` to go next.

```bash
? Which framework does your project use? (Use arrow keys)
❯ React
  Vue.js
  None of these
```

React Native is based on React, so select `React`.

```bash
? Does your project use TypeScript? (y/N)
```

In this blog post, we will use `Typescript` is integrated on React Native, so select `y` to configure ESLint.

```bash
? Where does your code run? (Press <space> to select, <a> to toggle all, <i> to invert selection)
 ◯ Browser
❯◉ Node
```

React Native is not run on the browser, so select only `Node`.

Unlike other options, press the space bar on the Browser option and press the space bar on Node.

```bash
? How would you like to define a style for your project? (Use arrow keys)
  Use a popular style guide
❯ Answer questions about your style
  Inspect your JavaScript file(s)
```

This question is what style you want to implement via ESLint. I selected `Answer questions about your style` option to make own my style.

```bash
? What format do you want your config file to be in? (Use arrow keys)
❯ JavaScript
  YAML
  JSON
```

This question is about what file you want to save ESLint settings. `.eslintrc.js` file exists already in React Native, so select `Javascript` to overwrite it.

```bash
? What style of indentation do you use? (Use arrow keys)
  Tabs
❯ Spaces
```

This question is about what style you want to use Tab or Space for Indentation. I prefer the Sapce, so I selected `Spaces`.

```bash
? What quotes do you use for strings? (Use arrow keys)
  Double
❯ Single
```

In this question, I selected `Single` because I prefer Single Quote.

```bash
? What line endings do you use? (Use arrow keys)
❯ Unix
  Windows
```

In this question, I am a Mac user, so I selected `Unix`.

```bash
? Do you require semicolons? (Y/n)
```

I prefer to use Semicolon(`;`), so I selected `Y` in here.

```bash
The config that you've selected requires the following dependencies:

eslint-plugin-react@latest @typescript-eslint/eslint-plugin@latest @typescript-eslint/parser@latest
Warning: React version not specified in eslint-plugin-react settings. See https://github.com/yannickcr/eslint-plugin-react#configuration .
Successfully created .eslintrc.js file in /Users/jeonghean_kim/projects/poma_app
```

After all settings, you can see the screen like above. As you can see above, Warning is shown up, so we need to set detail configurations.

{% include in-feed-ads.html %}

### ESLint detail configurations

I selected `Answer questions about your style` to set ESLint. If you select it like me, it configures basic settings, so we need to configure detail settings about `React` and `Typescript`.

Execute the command below to install additional plugins.

```bash
npm install --save-dev eslint-plugin-react @typescript-eslint/eslint-plugin @typescript-eslint/parser eslint-plugin-react-hooks
```

For detail configurations, open `.eslintrc.js` file and modify it like me.

```js
module.exports = {
  env: {
    es6: true,
    node: true,
    jest: true,
  },
  extends: [
    'eslint:recommended',
    'plugin:react/recommended',
    'plugin:@typescript-eslint/eslint-recommended',
    'plugin:@typescript-eslint/recommended',
    'plugin:@typescript-eslint/recommended-requiring-type-checking',
  ],
  ...
  parserOptions: {
    project: './tsconfig.json',
    ...
  },
  plugins: ['react', 'react-hooks', '@typescript-eslint'],
  ...
  rules: {
    indent: ['error', 2, { SwitchCase: 1 }],
    quotes: ['error', 'single', { avoidEscape: true }],
    ...,
    'no-empty-function': 'off',
    '@typescript-eslint/no-empty-function': 'off',
    'react/display-name': 'off',
    'react/prop-types': 'off',
  },
  settings: {
    react: {
      version: 'detect',
    },
  },
};
```

### Prepare to execute ESLint

To prepare to execute ESLint, modify `package.json` to prepare inspecting React Native project.

```json
{
  ...
  "scripts": {
    ...
    "lint": "eslint --ext .tsx --ext .ts src/",
    ...
  },
  ...
}
```

I put all source code on `src` folder, so I configure the specific folder. If you use Root folder to manage files, you can use the basic configuration like below.

```json
{
  ...
  "scripts": {
    ...
    "lint": "eslint .",
    ...
  },
  ...
}
```

{% include in-feed-ads.html %}

### Execute ESLint

Now, let's execute ESLint by using the command below.

```bash
npm run lint
```

And then you can get the result like below.

```bash
   1:8   error  A space is required after '{'                             object-curly-spacing
   1:50  error  A space is required before '}'                            object-curly-spacing
   2:8   error  A space is required after '{'                             object-curly-spacing
   2:29  error  A space is required before '}'                            object-curly-spacing
   ...
  11:25  error  Unable to resolve path to module './RequestSite'          import/no-unresolved
  11:25  error  Missing file extension for "./RequestSite"                import/extensions
  12:25  error  Unable to resolve path to module './CheckServer'          import/no-unresolved
  12:25  error  Missing file extension for "./CheckServer"                import/extensions

✖ 22 problems (22 errors, 0 warnings)
  4 errors and 0 warnings potentially fixable with the `--fix` option.
```

As above, you can get the problems of the source code according to the ESLint setting we set.

### eslint --fix

The above error occurred because ESLint setting was not observed. Of course, you can open the source code and modify it one by one, you can also execute the command below to fix the problems fastly.

```bash
# npx eslint . --fix
npx eslint ./src/**/*.tsx --fix
```

You can get many errors, but ESLint fixes them automatically. To check them really fixed, execute the command below.

```bash
npm run lint
```

You can see no messages unlike before.

If the error messages are still shown up, open the source code and modify it to fix it!

### Use ESLint on VSCode

If you use VSCode, I recommend you to use `ESLint` Extension. If you install ESLint Extension, when you save files, files are automatically fixed by ESLint rules like you execute `eslint --fix`.

![VSCode ESLint Extension](/assets/images/category/react-native/2018/eslint-prettier-husky-lint-staged/vscode-eslint-extension.jpg)

After installing, open VSCode configuration file and modify it like below.

```json
{
  ...
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": true
  },
  ...
}
```

After this, when you save files, ESLint fixes automatically them.

{% include in-feed-ads.html %}

## Prettier

Prettier is a Code Formatter, makes the same code style by rules. ESLint is a kind of Code Formatter for Javascript, Prettier is the Code Formatter for all source code.

### Install Prettier

Execute the command below to install Prettier.

```bash
npm install --save-dev prettier eslint-plugin-prettier
```

### Configure Prettier

React Native project has basically `.prettierrc.js` file. As you open the file, you can see the contents below.

```js
module.exports = {
  bracketSpacing: false,
  jsxBracketSameLine: true,
  singleQuote: true,
  trailingComma: 'all',
};
```

Modify it like below to use it with `ESLint`.

```js
module.exports = {
  jsxBracketSameLine: true,
  singleQuote: true,
  trailingComma: 'all',
  printWidth: 100,
};
```

{% include in-feed-ads.html %}

### Configure Prettier on ESLint

To use Prettier with ESLint, we need to configure Prettier on ESLint. open `.eslintrc.js` file and modify it like below.

```js
module.exports = {
  ...
  plugins: ['react', 'react-hooks', '@typescript-eslint', 'prettier'],
  rules: {
    ...
    'prettier/prettier': 'error',
  },
  ...
};
```

### Prepare to execute Prettier

To prepare to execute Prettier, open `package.json` file and modify it like below.

```json
{
  ...
  "scripts": {
    ...
    "format": "prettier --check ./src",
    ...
  },
  ...
}
```

{% include in-feed-ads.html %}

### Execute Prettier

Execute the command below to execute Prettier.

```bash
npm run format
```

And then, you can get the result like below.

```bash
...
src/Screen/ResetPassword/index.tsx
src/Screen/SignUp/index.tsx
src/Screen/SiteViewer/index.tsx
src/Util/Validation/index.tsx
Code style issues found in the above file(s). Forgot to run Prettier?
```

Prettier finds the wrong formatting file list like above.

### prettier --write

To solve it, you can execute the command below.

```bash
npx prettier --write ./src
```

After fixing, you can see the result like below.

```bash
...
src/Screen/RequestSite/index.tsx 235ms
src/Screen/ResetPassword/index.tsx 92ms
src/Screen/SignUp/index.tsx 174ms
src/Screen/SiteViewer/index.tsx 124ms
src/Theme.tsx 12ms
src/Util/Validation/index.tsx 11ms
```

And then, execute the command below to check the source code again.

```bash
npm run format
```

Unlike below, you can see the message like below.

```bash
...
Checking formatting...
All matched files use Prettier code style!
```

### Use Prettier on VSCode

If you are VSCode user, you can use `Prettier` Extension. When you save the file, Prettier Extension fixes it by rules like `prettier --write` command.

![VSCode Prettier Extension](/assets/images/category/react-native/2018/eslint-prettier-husky-lint-staged/vscode-prettier-extension.jpg)

After installing, open VSCode settings file and modify it like below.

```json
{
  ...
  "editor.formatOnSave": true,
  ...
}
```

After it, when you save the file, Prettier formats automatically it.

{% include in-feed-ads.html %}

## Use ESLint and Prettier like Pro

Until now, we've seen what ESLint and Prettier are, and how to use them. In this part, we'll see what `Husky` and `lint-staged` is and how to use them like Pro.

### Husky

Git has the Hook feature. When some events(commit, push, etc) are triggered on Git, you can use the Hook feature to execute scripts that are configured on the Hook.

Husky makes you use Git Hook more simply.

Let's install Husky by executing the command below.

```bash
npm install --save-dev husky
```

### lint-staged

To be with Husky, `lint-staged` is normally used. lint-staged makes you execute scripts to files that are staged on Git.

Staged on Git means the files are added by `git add` command for committing. If you modify files staged on Git, you should execute `git add` command again to add them.

lint-staged makes you modify staged files and not execute `git add` for them.

Execute the command below to install `lint-staged` to use it with Husky.

```bash
npm install --save-dev lint-staged
```

{% include in-feed-ads.html %}

### How to use Husky and lint-staged

Let's make ESLint and Prettier run when you commit on Git by using Husky and lint-staged.

Open `package.json` and modify it like below to configure Husky and lint-staged.

```json
{
  ...
  "lint-staged": {
    "src/**/*.{ts,tsx}": [
      "eslint --ext .tsx --ext .ts src/ --fix"
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

We've made Husky runs lint-staged before Git commit(`pre-commit`), and lintlint-staged runs `eslint --fix` and `prettier --write` if the source code(`src/**/*.{ts,tsx}`, `*`) is modified.

Now, you can see ESLint and Prettier run and fix the source code, when you commit on Git.

## Solve problems

I got the error message like below after using above configuration on React Native.

```bash
husky > pre-commit (node v13.8.0)
  ✔ Preparing...
  ❯ Running tasks...
    ↓ Running tasks for src/**/*.{ts,tsx} [skipped]
      → No staged files match src/**/*.{ts,tsx}
    ❯ Running tasks for *
      ✖ prettier --write .
  ↓ Applying modifications... [skipped]
    → Skipped because of errors from tasks.
  ✔ Reverting to original state...
  ✔ Cleaning up...
...
src/Theme.tsx 4ms
tsconfig.json 5ms
[error] No parser could be inferred for file: src/image.jpg
```

In this case, the error is occurred because `Prettier` can't analyze the file, or the files are not needed to be analyzed.
For this error, create `.prettierignore` file and modify it like below.

```bash
*.jpg
```

First, I copied the contents of `.gitignore` to `.prettierignore` file. And added the files that occur the error on the bottom.

## Completed

We've seen how to configure ESLint and Prettier, and how to execute them by Husky and lint-staged automaticaaly.

You can see configurations of ESLint and Prettier above on Github repository. If you want it, see the link below.

- Github: [react-native-eslintrc-prettier](https://github.com/dev-yakuza/react-native-eslintrc-prettier){:rel="nofollow noreferrer" target="_blank"}