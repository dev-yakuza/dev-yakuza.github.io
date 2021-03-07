---
layout: 'post'
permalink: '/react-native/eslint-prettier-husky-lint-staged/'
paginate_path: '/react-native/:num/eslint-prettier-husky-lint-staged/'
lang: 'ko'
categories: 'react-native'
comments: true

title: 'React Native에서 ESLint, Prettier를 프로처럼 사용하기'
description: 'React Native 프로젝트에 ESLint와 Prettier를 적용하는 방법과 Husky, lint-staged로 프로처럼 사용하는 방법에 대해서 알아봅니다.'
image: '/assets/images/category/react-native/2018/eslint-prettier-husky-lint-staged/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [React Native 프로젝트 준비](#react-native-프로젝트-준비)
- [ESLint](#eslint)
  - [ESLint 설치하기](#eslint-설치하기)
  - [ESLint 설정하기](#eslint-설정하기)
  - [ESLint 상세 설정](#eslint-상세-설정)
  - [ESLint 실행 준비](#eslint-실행-준비)
  - [ESLint 실행](#eslint-실행)
  - [eslint --fix](#eslint---fix)
  - [VSCode에서 ESLint 사용하기](#vscode에서-eslint-사용하기)
- [Prettier](#prettier)
  - [Prettier 설치하기](#prettier-설치하기)
  - [Prettier 설정하기](#prettier-설정하기)
  - [ESLint에 Prettier 설정하기](#eslint에-prettier-설정하기)
  - [Prettier 실행 준비](#prettier-실행-준비)
  - [Prettier 실행](#prettier-실행)
  - [prettier --write](#prettier---write)
  - [VSCode에서 Prettier 사용하기](#vscode에서-prettier-사용하기)
- [ESLint와 Prettier를 프로처럼 사용하기](#eslint와-prettier를-프로처럼-사용하기)
  - [Husky](#husky)
  - [lint-staged](#lint-staged)
  - [Husky와 lint-staged를 사용하기](#husky와-lint-staged를-사용하기)
- [문제 해결](#문제-해결)
- [완료](#완료)

</div>

## 개요

이번 블로그 포스트에서 ESLint와 Prettier가 무엇인지 알아보고, React Native에서 ESLint와 Prettier를 사용하는 방법에 대해서 알아보려고 합니다.

또한 Husky와 lint-staged를 알아보고, 프로처럼 사용하기 위한 설정을 살펴보도록 하겠습니다.

여기서 사용한 ESLint와 Prettier는 아래에 Github 저장소에서 확인하실 수 있습니다.

- Github: [react-native-eslintrc-prettier](https://github.com/dev-yakuza/react-native-eslintrc-prettier){:rel="nofollow noreferrer" target="_blank"}

## React Native 프로젝트 준비

이번 블로그 포스트에서 소개하는 내용은, React Native에 Typescript가 적용된 상태에서 ESLint를 적용하는 방법에 대해서 설명합니다.

React Native에 Typescript를 적용하는 방법에 대해서는 아래에 링크를 확인하시기 바랍니다.

- [React Native에 Typescript를 적용하는 방법]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}

## ESLint

ESLint란 ES(EcmaScript) + Lint(에러 코드 표식) 합성어로 `Javascript` 코드를 분석하고, 코드의 스타일을 통일하도록 도와주는 툴입니다.

### ESLint 설치하기

아래에 명령어를 사용하여 ESLint를 React Native 프로젝트에 설치합니다. (React Native에는 기본적으로 ESLint가 설치되어있으므로 이 명령어는 스킵하셔도 됩니다.)

```bash
# cd SampleApp
npm install --save-dev eslint
```

{% include in-feed-ads.html %}

### ESLint 설정하기

이제 React Native 프로젝트에 ESLint를 설정하는 방법에 대해서 알아봅시다.

아래에 명령어를 사용하여 ESLint를 초기화합니다.

```bash
# cd SampleApp
npx eslint --init
```

위에 명령어를 실행하면, 아래와 같은 화면을 확인할 수 있습니다.

```bash
? How would you like to use ESLint? (Use arrow keys)
  To check syntax only
  To check syntax and find problems
❯ To check syntax, find problems, and enforce code style
```

여기서는 문법 체크뿐만 아니라, 자동으로 수정까지 하게 하기 위해 `To check syntax, find problems, and enforce code style`를 선택합니다.

```bash
? What type of modules does your project use? (Use arrow keys)
❯ JavaScript modules (import/export)
  CommonJS (require/exports)
  None of these
```

React Native에서는 주로 `import/export`을 사용하므로 `JavaScript modules (import/export)`을 선택하고 다음으로 진행합니다.

```bash
? Which framework does your project use? (Use arrow keys)
❯ React
  Vue.js
  None of these
```

React Native는 React를 기반으로 하기 때문에 `React`를 선택하고 진행합니다.

```bash
? Does your project use TypeScript? (y/N)
```

이 블로그 포스트에서는 `Typescript`가 적용된 React Native 프로젝트에 ESLint를 설정하고 있는 중이기 때문에, `y`를 눌러 진행합니다.

```bash
? Where does your code run? (Press <space> to select, <a> to toggle all, <i> to invert selection)
 ◯ Browser
❯◉ Node
```

ESLint를 적용하려는 소스코드가 브라우저에서 실행이 되는지 여부를 물어보는 화면입니다. React Native는 브라우저에서 실행하지 않으므로 `Node`을 선택하고 진행합니다.

다른 선택지와는 다르게 Browser에서 스페이스바를 한번 누르고 Node에서 한번 더 눌러서 선택합니다.

```bash
? How would you like to define a style for your project? (Use arrow keys)
  Use a popular style guide
❯ Answer questions about your style
  Inspect your JavaScript file(s)
```

어떤 스타일 가이드를 따를지 선택하는 화면입니다. 저는 `Answer questions about your style`을 선택하여 제가 사용하고 싶은 스타일을 적용하도록 선택하였습니다.

```bash
? What format do you want your config file to be in? (Use arrow keys)
❯ JavaScript
  YAML
  JSON
```

ESLint에 설정 내용을 저장할 파일 형식을 선택하는 화면입니다. React Native에는 이미 `.eslintrc.js` 파일이 존재합니다. 이 파일을 덮어쓰기 위해 `Javascript`를 선택하고 진행합니다.

```bash
? What style of indentation do you use? (Use arrow keys)
  Tabs
❯ Spaces
```

Indentation에 Tab을 사용할지 Space를 사용할지 여부를 물어봅니다. 저는 Space를 선호함으로 `Spaces`를 선택하고 진행하였습니다.

```bash
? What quotes do you use for strings? (Use arrow keys)
  Double
❯ Single
```

문자열에 Double Quotes(`"`)를 사용할지 Single Quote(`'`)를 사용할지 물어봅니다. 저는 Single Quote를 선호함으로 `Single`을 선택하고 진행합니다.

```bash
? What line endings do you use? (Use arrow keys)
❯ Unix
  Windows
```

Line ending에 사용되는 형식을 선택하는 질문이 나옵니다. 저는 Mac 유저이므로 `Unix`를 선택하고 진행합니다.

```bash
? Do you require semicolons? (Y/n)
```

마지막으로 Semicolon(`;`) 사용여부를 물어봅니다. 저는 Semicolon 사용을 선호하므로 `Y`를 눌러 진행하였습니다.

```bash
The config that you've selected requires the following dependencies:

eslint-plugin-react@latest @typescript-eslint/eslint-plugin@latest @typescript-eslint/parser@latest
Warning: React version not specified in eslint-plugin-react settings. See https://github.com/yannickcr/eslint-plugin-react#configuration .
Successfully created .eslintrc.js file in /Users/jeonghean_kim/projects/poma_app
```

모든 설정이 완료되면 위와 같은 화면을 볼 수 있습니다. 위에 메세지에서도 알수 있지만 Warning이 표시되고 있습니다. 이런 문제들을 해결하기위해 상세 설정을 진행해야합니다.

{% include in-feed-ads.html %}

### ESLint 상세 설정

저는 `Answer questions about your style`을 선택해서 ESLint를 설정하였습니다. 기본적인 설정만 되었기 때문에 `React`와 `Typescript`를 사용하기 위한 상세 설정을 해야합니다.

아래에 명령어로 설정에 필요한 추가 플러그인을 설치합니다.

```bash
npm install --save-dev eslint-plugin-react @typescript-eslint/eslint-plugin @typescript-eslint/parser eslint-plugin-react-hooks
```

상세 설정을 하기 위해, `.eslintrc.js` 파일을 열고 아래와 같이 수정합니다.

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

### ESLint 실행 준비

이제 ESLint로 React Native 프로젝트를 검사하기 위해 아래와 같이 `package.json` 파일을 수정합니다.

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

저는 모든 소스코드를 `src` 폴더에 넣고 관리하기 때문에 위와 같이 특정 폴더를 지정하였습니다. 만약 root 폴더에서 파일을 관리한다면 아래와 같이 기본 설정을 그대로 사용하시면 됩니다.

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

### ESLint 실행

이제 아래에 명령어를 통해 ESLint를 실행해 봅니다.

```bash
npm run lint
```

그러면 아래와 같은 결과를 얻을 수 있습니다.

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

위와 같이 우리가 설정한 ESLint 설정에 따른 소스코드의 문제점들을 확인할 수 있습니다.

### eslint --fix

위에 표시된 에러는 ESLint의 설정을 지키지 않았기 때문에 발생하였습니다. 물론 소스코드를 열고 하나씩 수정해도 되지만, 아래에 명령어를 사용하여 모든 에러를 빠르게 고칠 수 있습니다.

```bash
# npx eslint . --fix
npx eslint ./src/**/*.tsx --fix
```

많은 에러가 나오겠지만, 자동으로 수정해줍니다. 정말로 수정이 되었는지 확인하기 위해 아래에 명령어를 실행해 봅니다.

```bash
npm run lint
```

그럼 이전과는 다르게 아무 메세지도 표시되지 않는 것을 확인할 수 있습니다.

만약, 아직도 에러메세지가 나온다면, 해당 소스코드를 열고 수정하시기 바랍니다!

### VSCode에서 ESLint 사용하기

만약, 여러분이 VSCode를 사용하신다면 `ESLint` Extension을 사용하시길 권장합니다. ESLint Extension을 설치하면 파일을 저장할 때, `eslint --fix`와 동일하게 ESLint에 규칙에 맞게 자동으로 수정할 수 있습니다.

![VSCode ESLint Extension](/assets/images/category/react-native/2018/eslint-prettier-husky-lint-staged/vscode-eslint-extension.jpg)

설치가 완료되었다면 VSCode의 설정파일을 열고 아래와 같이 수정합니다.

```json
{
  ...
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": true
  },
  ...
}
```

이렇게 수정하면 파일을 저장할 때, ESLint의 설정에 맞게 자동으로 수정해 줍니다.

{% include in-feed-ads.html %}

## Prettier

Prettier란 Code Formatter로써, 정해진 규칙에 따라 코드 스타일을 통일 시켜줍니다. ESLint가 Javascript에 한정된 Code Formatter였다면, Prettier는 전체 코드 스타일을 다루는 Code Formatter입니다.

### Prettier 설치하기

아래에 명령어로 Prettier를 사용하기 위한 라이브러리를 설치합니다.

```bash
npm install --save-dev prettier eslint-plugin-prettier
```

### Prettier 설정하기

React Native로 프로젝트를 생성하면 기본적으로 `.prettierrc.js` 파일이 생성됩니다. 해당 파일을 열어보면 다음과 같습니다.

```js
module.exports = {
  bracketSpacing: false,
  jsxBracketSameLine: true,
  singleQuote: true,
  trailingComma: 'all',
};
```

이 파일을 `ESLint`와 함께 사용하기 위해 다음과 같이 수정합니다.

```js
module.exports = {
  jsxBracketSameLine: true,
  singleQuote: true,
  trailingComma: 'all',
  printWidth: 100,
};
```

{% include in-feed-ads.html %}

### ESLint에 Prettier 설정하기

Prettier를 ESLint와 함께 사용하기 위해서는 ESLint 설정에 Prettier를 설정할 필요가 있습니다. `.eslintrc.js` 파일을 열고 아래와 같이 수정합니다.

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

### Prettier 실행 준비

이제 Prettier로 소스코드를 Formatting하기 위해 아래와 같이 `package.json` 파일을 수정합니다.

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

### Prettier 실행

이제 아래에 명령어를 통해 Prettier를 실행해 봅니다.

```bash
npm run format
```

그러면 아래와 같은 결과를 얻을 수 있습니다.

```bash
...
src/Screen/ResetPassword/index.tsx
src/Screen/SignUp/index.tsx
src/Screen/SiteViewer/index.tsx
src/Util/Validation/index.tsx
Code style issues found in the above file(s). Forgot to run Prettier?
```

Prettier는 위와 같이 Formatting이 잘못된 파일 리스트들을 찾아줍니다.

### prettier --write

위에 표시된 파일 리스트는 Prettier의 설정을 지키지 않았기 때문에 발생하였습니다. 이렇게 문제가 있는 파일들은 아래에 명령어를 사용하여 고칠 수 있습니다.

```bash
npx prettier --write ./src
```

수정이 완료되면 아래와 같은 결과 화면을 볼 수 있습니다.

```bash
...
src/Screen/RequestSite/index.tsx 235ms
src/Screen/ResetPassword/index.tsx 92ms
src/Screen/SignUp/index.tsx 174ms
src/Screen/SiteViewer/index.tsx 124ms
src/Theme.tsx 12ms
src/Util/Validation/index.tsx 11ms
```

다시 아래에 명령어를 사용하여 코드를 검사해 봅니다.

```bash
npm run format
```

이전과는 다르게 아래와 같은 메세지를 확인할 수 있습니다.

```bash
...
Checking formatting...
All matched files use Prettier code style!
```

### VSCode에서 Prettier 사용하기

만약, 여러분이 VSCode를 사용하신다면 `Prettier` Extension을 사용하시길 권장합니다. Prettier Extension을 설치하면 파일을 저장할 때, `prettier --write`와 동일하게 Prettier에 규칙에 맞게 자동으로 수정할 수 있습니다.

![VSCode Prettier Extension](/assets/images/category/react-native/2018/eslint-prettier-husky-lint-staged/vscode-prettier-extension.jpg)

설치가 완료되었다면 VSCode의 설정파일을 열고 아래와 같이 수정합니다.

```json
{
  ...
  "editor.formatOnSave": true,
  ...
}
```

이렇게 수정하면 파일을 저장할 때, Prettier의 설정에 맞게 자동으로 수정해 줍니다.

{% include in-feed-ads.html %}

## ESLint와 Prettier를 프로처럼 사용하기

지금까지 ESLint와 Prettier가 무엇인지, 그리고 어떻게 사용하는지에 대해서 알아보았습니다. 이제 실전에서 프로처럼 사용하기 위해 `Husky`와 `lint-staged`를 활용하는 방법에 대해서 알아보도록 하겠습니다.

### Husky

Git는 Hook이라는 기능을 가지고 있습니다. Git에서 특정 이벤트(커밋, 푸쉬 등)를 실행할 때, 그 이벤트에 Hook을 설정하여 Hook에 설정된 스크립트를 실행할 수 있습니다.

Husky란 Git Hook을 간편하게 사용할 수 있도록 도와주는 툴입니다.

그럼 Husky를 사용하기 위해 아래에 명령어로 Husky를 설치합니다.

```bash
npm install --save-dev husky
```

### lint-staged

Husky와 함께 자주 사용되는 `lint-staged`는 Git의 Staged된 상태에 파일들에 특정 명령어를 실행할 수 있도록 해주는 툴입니다.

Git의 Staged된 상태란 `git add` 명령어로 수정된 파일을 커밋하기 위해 추가한 상태를 말합니다. 이렇게 Staged 상태에 파일들은 다시 수정하게 되면 `git add`로 다시 추가해 주어야 합니다.

lint-staged는 Staged된 파일을 수정한 후 다시 git add를 하지 않아도 문제가 없도록 도와주는 툴입니다.

그럼 Husky와 함께 `lint-staged`를 사용하기 위해 아래에 명령어로 lint-staged를 설치합니다.

```bash
npm install --save-dev lint-staged
```

{% include in-feed-ads.html %}

### Husky와 lint-staged를 사용하기

이제 Husky와 lint-staged를 사용하여 Git의 Commit을 사용할 때, ESLint와 Prettier를 실행하도록 설정해 보도록 하겠습니다.

Husky와 lint-staged를 설정하기 위해 `package.json` 파일을 열고 아래와 같이 수정합니다.

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

Husky를 사용하여 Git의 Commit을 실행하기 전(`pre-commit`)에 lint-staged를 실행하도록 하였습니다. lint-staged 설정에는 소스코드(`src/**/*.{ts,tsx}`, `*`)가 추가/변경된 경우, `eslint --fix`와 `prettier --write`를 실행하도록 하였습니다.

이제 Git의 Commit을 사용하여 소스코드를 저장소(Repository)에 올리기 전에 ESLint와 Prettier를 실행하여 소스코드를 항상 잘 정리된 상태로 관리할 수 있게 되었습니다.

## 문제 해결

위에 설정을 사용하는 React Native에서 아래와 같은 에러가 발생하였습니다.

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

이렇게 `Prettier`가 분석을 할 수 없는 파일이거나, 체크를 할 필요가 없는 파일들 때문에 문제가 발생할 경우가 있습니다.
이런 경우 `.prettierignore` 파일을 생성하고 아래와 같이 수정해 줍니다.

```bash
*.jpg
```

저는 우선 `.prettierignore` 파일을 만들고 `.gitignore` 파일의 내용을 복사하였습니다. 그리고 하단에 추가로 에러가 발생하는 파일을 추가하였습니다.

## 완료

이것으로 React Native 프로젝트에 ESLint와 Prettier를 설정하고 Husky와 lint-staged를 통해 자동화하는 방법에 대해서 알아보았습니다.

위에서 설명한 ESLint 설정과 Prettier 설정은 아래에 Github 저장소에서 확인이 가능합니다. 혹시 궁금하신 분들은 아래에 링크를 참고하시기 바랍니다.

- Github: [react-native-eslintrc-prettier](https://github.com/dev-yakuza/react-native-eslintrc-prettier){:rel="nofollow noreferrer" target="_blank"}