---
layout: 'post'
permalink: '/react/prettier/'
paginate_path: '/react/:num/prettier/'
lang: 'ko'
categories: 'react'
comments: true

title: '[React] Prettier'
description: 'React에서 Prettier를 사용하여 코드의 포맷을 일정하게 유지시켜 보자.'
image: '/assets/images/category/react/2021/prettier/background.png'
published: false
---

<div id="contents_list" markdown="1">

## 목차

</div>

## 블로그 시리즈

이 블로그 포스트는 시리즈로 제작되었습니다. 다음은 블로그 시리즈 리스트입니다.

- [React] Prettier
- [[React] ESLint]({{site.url}}/{{page.categories}}/eslint/){:target="_blank"}
- [[React] Husky, lint-staged]({{site.url}}/{{page.categories}}/husky-lint-staged/){:target="_blank"}
- [[React] GitHub Actions]({{site.url}}/{{page.categories}}/github-actions/){:target="_blank"}

## 개요

혼자서 서비스를 개발할 때는 코드 포맷(스페이스, 탭, 쿼테이션 등)은 큰 문제가 되지 않습니다. 하지만, 여러 사람들과 함께 협업하여 서비스를 개발할 때, 각 개발자가 사용하는 코드 포맷이 다를 수 있습니다. 이렇게 코드 포맷이 다르면 코드가 읽기 어려워지며, 예상치 못한 버그등이 발생할 수 있습니다.

Prettier는 코드 포맷터(Code formatter)로써 미리 코드 포맷을 정의하고, 해당 포맷에 맞게 코드를 수정해 주는 역할을 합니다.

이번 블로그 포스트에서 React에서 Prettier를 사용하여 코드 포맷을 통일 시키는 방법에 대해서 알아보겠습니다.

## 프로젝트 준비

React에서 Prettier를 사용하기 위해, `create-react-app`으로 간단하게 프로젝트를 생성하겠습니다. `create-react-app`에 관해 잘 모르시는 분들은 아래의 링크를 참고하시기 바랍니다.

- [create-react-app]({{site.url}}/{{page.categories}}/create-react-app/start/){:target="_blank"}

그럼 다음 명령어를 사용하여 Prettier를 사용할 React 프로젝트를 생성합니다.

```bash
npx create-react-app prettier_example
```

{% include in-feed-ads.html %}

## Prettier 설치

React에서 Prettier를 사용하기 위해서는 Prettier 라이브러리를 설치할 필요가 있습니다. 다음 명령어를 사용하여 Prettier 라이브러리를 설치합니다.

```bash
# cd prettier_example
npm install --save-dev prettier
```

## Prettier 설정

React에서 Prettier를 사용하기 위해서는 사용할 코드 포맷을 미리 정의할 필요가 있습니다. 코드 포맷을 미리 정의하기 위해, `.prettierrc.js` 파일을 생성하고 다음과 같이 수정합니다.

```js
module.exports = {
  jsxBracketSameLine: true,
  singleQuote: true,
  trailingComma: 'all',
  printWidth: 100,
};
```

Prettier의 공식 사이트에 설정 가능한 다른 옵션들을 확인할 수 있습니다.

- Prettier 공식 사이트: [Options](https://prettier.io/docs/en/options.html){:rel="noopener" target="_blank"}

위에서 옵션들을 확인하고, 각 프로젝트에 맞게 옵션을 설정하시기 바랍니다.

## 포맷 체크

다음 명령어를 사용하면 우리가 정의한 Prettier의 옵션들을 지키고 있지 않은 파일들을 찾을 수 있습니다.

```bash
npx prettier --check ./src
```

명령어를 실행하면 다음과 같이 정의된 옵션들을 지키고 있지 않는 파일 리스트를 확인할 수 있습니다.

```bash
[warn] public/index.html
[warn] src/App.js
[warn] src/index.css
[warn] src/index.js
[warn] src/reportWebVitals.js
[warn] Code style issues found in the above file(s). Forgot to run Prettier?
```

## 포맷팅

다음 명령어를 사용하면 우리가 정의한 Prettier의 옵션을 사용하여 코드 포맷팅을 할 수 있습니다.

```bash
prettier --write ./src
```

명령어를 실행하면 다음과 같이 포맷팅이 진행된 파일 리스트를 확인할 수 있습니다.

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

이렇게 파일 포맷팅이 완료된 후, 다시 다음 명령어를 실행하여 코드 포맷을 확인해 보면

```bash
npx prettier --check ./src
```

다음과 같이 모든 파일들이 잘 포맷팅된 것을 확인할 수 있습니다.

```bash
Checking formatting...
All matched files use Prettier code style!
```

## package.json 설정

앞에서 살펴본 `check` 명령어와 `write` 명령어를 점 더 쉽게 사용하기 위해 `package.json` 파일을 열고 다음과 같이 수정합니다.

```json
"scripts": {
  ...
  "format": "prettier --check ./src",
  "format:fix": "prettier --write ./src"
},
```

이렇게 `package.json` 파일을 수정하였다면, 이제 다음 명령어를 사용하여 Prettier를 사용할 수 있습니다

```bash
npm run format
npm run format:fix
```

{% include in-feed-ads.html %}

## 에디터 설정

Prettier는 다양한 에디터에서 사용할 수 있습니다. Prettier의 공식 사이트에서 Prettier가 사용 가능한 에디터를 확인할 수 있습니다.

- Prettier 공식 사이트: [Editor Integration](https://prettier.io/docs/en/editors.html){:rel="noopener" target="_blank"}

여기서는 `VSCode`에 설정하는 방법을 간단히 설명하겠습니다. 다음 링크를 통해 VSCode의 Prettier 플러그인을 설치합니다.

- VSCode 플러그인: [Prettier - Code formatter](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode){:rel="noopener" target="_blank"}

설치가 완료되었다면, VSCode를 열고 `(macOS) cmd + shift + p` 또는 `(windows) ctrl + shift + p` 키를 눌른 후, `open settings`를 검색합니다.

![vscode command palette](/assets/images/category/react/2021/prettier/vscode-command-palette.jpg)

`Preference: Open Setting(JSON)`을 선택하고 해당 파일을 다음과 같이 수정합니다.

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

또는 간단히 다음과 같이 설정할 수 있습니다.

```json
{
  ...
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode"
}
```

이렇게 설정하였다면, VSCode에서 파일을 수정하고 저장하면, 자동으로 코드가 포맷팅되는 것을 확인할 수 있습니다.

## 완료

이것으로 React 프로젝트에서 Prettier를 설정하는 방법에 대해서 알아보았습니다. Prettier를 통해 잘 포맷팅된 코드를 관리해 보시기 바랍니다.
