---
layout: 'post'
permalink: '/react/husky-lint-staged/'
paginate_path: '/react/:num/husky-lint-staged/'
lang: 'ko'
categories: 'react'
comments: true

title: '[React] husky, lint-staged'
description: 'React에서 husky와 lint-staged를 사용하여 Git에 커밋할 때, ESLint와 Prettier를 실행하도록 설정해 봅시다.'
image: '/assets/images/category/react/2021/husky-lint-staged/background.jpg'
published: false
---

<div id="contents_list" markdown="1">

## 목차

</div>

## 블로그 시리즈

이 블로그 포스트는 시리즈로 제작되었습니다. 다음은 블로그 시리즈 리스트입니다.

- [Prettier]({{site.url}}/{{page.categories}}/prettier/){:target="_blank"}
- [ESLint]({{site.url}}/{{page.categories}}/eslint/){:target="_blank"}
- Husky, lint-staged

## 개요

이전 블로그 시리즈에서 create-react-app으로 생성한 React 프로젝트에 Prettier와 ESLint를 설치하고 설정하는 방법에 대해서 알아보았습니다.

이번 블로그 포스트에서는 `husky`와 `lint-staged`를 사용하여 Prettier와 ESlint를 활용하는 방법에 대해서 알아봅시다.

## 프로젝트 준비

React의 husky와 lint-staged를 사용하기 위해, `create-react-app`으로 간단하게 프로젝트를 생성하겠습니다. `create-react-app`에 관해 잘 모르시는 분들은 아래의 링크를 참고하시기 바랍니다.

- [create-react-app]({{site.url}}/{{page.categories}}/create-react-app/start/){:target="_blank"}

그럼 다음 명령어를 사용하여 Prettier를 사용할 React 프로젝트를 생성합니다.

```bash
npx create-react-app husky_lint_example --template=typescript
```

저는 주로 `TypeScript`를 사용하여 React를 개발하므로 `--template=typescript` 옵션을 사용하여 React 프로젝트를 생성하였습니다. 이렇게 생성된 React 프로젝트에 Prettier와 ESLint를 설정해 줍니다. Prettier와 ESLint를 설정하는 방법에 대해서는 아래에 링크를 참고하시기 바랍니다.

- [Prettier]({{site.url}}/{{page.categories}}/prettier/){:target="_blank"}
- [ESLint]({{site.url}}/{{page.categories}}/eslint/){:target="_blank"}

{% include in-feed-ads.html %}

## husky

Git는 Hook이라는 기능을 가지고 있습니다. Git에서 특정 이벤트(커밋, 푸쉬 등)를 실행할 때, 그 이벤트에 Hook을 설정하여 Hook에 설정된 스크립트를 실행할 수 있습니다.

husky란 Git Hook을 간편하게 사용할 수 있도록 도와주는 툴입니다.

- husky 공식 사이트: [https://typicode.github.io/husky/](https://typicode.github.io/husky/){:rel="noopener" target="_blank"}

그럼 husky를 사용하기 위해 아래에 명령어로 Husky를 설치합니다.

```bash
npm install --save-dev husky
```

## lint-staged

husky와 함께 자주 사용되는 lint-staged는 Git의 Staged된 상태에 파일들에 특정 명령어를 실행할 수 있도록 해주는 툴입니다.

- lint-staged 공식 페이지: [https://github.com/okonet/lint-staged](https://github.com/okonet/lint-staged){:rel="noopener" target="_blank"}

Git의 Staged된 상태란 git add 명령어로 수정된 파일을 커밋하기 위해 추가한 상태를 말합니다. 이렇게 Staged 상태에 파일들은 다시 수정하게 되면 git add로 다시 추가해 주어야 합니다.

lint-staged는 Staged된 파일을 수정한 후 다시 git add를 하지 않아도 문제가 없도록 도와주는 툴입니다.

그럼 husky와 함께 lint-staged를 사용하기 위해 아래에 명령어로 lint-staged를 설치합니다.

```bash
npm install --save-dev lint-staged
```

{% include in-feed-ads.html %}

## husky와 lint-staged 설정

이제 husky와 lint-staged를 사용하여 Git의 Commit을 사용할 때, ESLint와 Prettier를 실행하도록 설정해 보도록 하겠습니다.

husky와 lint-staged를 설정하기 위해 `package.json` 파일을 열고 아래와 같이 수정합니다.

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

이렇게 수정하면 Git를 사용하여 Commit을 할 때, husky의 pre-commit에 등록된 lint-staged가 실행되며, lint-staged에 등록된 ESLint와 Prettier 명령어가 실행되게 됩니다.

## 완료

이것으로 React 프로젝트에서 husky와 lint-staged를 사용하여 ESLint와 Prettier를 실행하는 방법에 대해서 알아보았습니다. 지금부터 husky와 lint-staged로 자동화 된 ESLint와 Prettier를 사용해 보시기 바랍니다.
