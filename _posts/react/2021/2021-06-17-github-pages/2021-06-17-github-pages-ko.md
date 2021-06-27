---
layout: 'post'
permalink: '/react/github-pages/'
paginate_path: '/react/:num/github-pages/'
lang: 'ko'
categories: 'react'
comments: true

title: '[React] GitHub Pages에 배포'
description: 'React로 만든 프로젝트를 GitHub Pages에 배포해 보도록 합시다.'
image: '/assets/images/category/react/background.jpg'
published: false
---

<div id="contents_list" markdown="1">

## 목차

</div>

## 개요

GitHub Pages는 GitHub이 제공하는 기능중에 하나로, 무료로 정적인 파일들로 웹 페이지를 만들 수 있도록 해줍니다. 이번 블로그 포스트에서는 `create-react-app`으로 개발한 React 프로젝트를 `GitHub Pages`에 배포하는 방법에 대해서 알아봅니다.

- React 공식 사이트: [Deployment](https://create-react-app.dev/docs/deployment/){:rel="noopener" target="_blank"}

여기서 소개하는 코드는 아래의 링크에서 확인하실 수 있습니다.

- GitHub: [Todo](https://github.com/dev-yakuza-example/todo){:rel="noopener" target="_blank"}

## 프로젝트 준비

이번 블로그 포스트에서 GitHub Pages로 배포할 React 프로젝트는 `create-react-app`과 `react-router`가 적용되었습니다. `create-react-app`과 `react-router`에 관해서는 다음 블로그를 참고하시기 바랍니다.

- [create-react-app]({{site.url}}/{{page.categories}}/create-react-app/start/){:target="_blank"}
- [[React] React Router]({{site.url}}/{{page.categories}}/react-router/){:target="_blank"}

GitHub Pages를 사용하여 React 프로젝트를 배포하기 위해서는 GitHub에 `Public` Repository가 필요합니다. 기존의 Private Repository를 가지고 계신 분들은 새롭게 Public Repository를 만드시기 바랍니다. GitHub Pages로 배포하기를 원하는 React 프로젝트가 Public Repository에 있으시다면, 해당 프로젝트를 그대로 이용하시면 됩니다.

## Build

create-react-app으로 생성된 React 프로젝트를 배포하기 위해서는 React 프로젝트를 `build` 할 필요가 있습니다. 다음 명령어를 실행하여 React 프로젝트를 `build` 합니다.

```bash
npm run build
```

{% include in-feed-ads.html %}

## 업로드

이제 이렇게 빌드된 React 프로젝트를 GitHub에 업로드해야 합니다.

### Public repository

이미 React 프로젝트가 Public Repository인 경우, build 명령어로 생성된 `build` 폴더를 GitHub에 업로드할 필요가 있습니다. `.gitignore` 파일을 열고 다음과 같이 수정합니다.

```bash
# production
# /build
```

`.gitignore` 파일을 수정하였다면, 다음 명령어를 실행하여 `build` 폴더를 GitHub에 업로드합니다.

```bash
git commit -am 'Add build folder'
git push origin main
```

GitHub Pages는 특정 Branch를 사용하여 정적 파일들을 서비스합니다. 따라서 build 폴더만을 위한 Branch를 만들 필요가 있습니다. 다음 명령어를 사용하여 build 폴더만 새로운 Branch에 업로드합니다.

```bash
git subtree push --prefix build/ origin gh-pages
```

### Private Repository

GitHub Pages는 Public Repository의 특정 Branch를 사용하여 정적 파일들을 서비스합니다. 따라서, GitHub pages에 배포하려는 React 프로젝트가 Private Repository인 경우, build 폴더의 내용을 Public Repository로 업로드할 필요가 있습니다.

다음 명령어를 실행하여 build 폴더를 Public Repository에 업로드 합니다.

```bash
cd build
git init
git remote add origin GITHUB_PUBLIC_REPOSITORY_URL
git commit -am 'Add build folder'
git push origin main
```

## GitHub Pages 설정

GitHub Pages 기능을 사용하여 정적 파일들을 사용하여 웹 서비스를 하기 위해서는, GitHub에서 GitHub Pages 기능을 활성화 시킬 필요가 있습니다. `build` 폴더를 업로드한 GitHub 페이지로 이동합니다.

![GitHub pages configuration](/assets/images/category/react/2021/github-pages/settings.jpg)

GitHub 페이지로 이동하였다면, `Settings` > `Pages`를 선택하여 GitHub Pages 설정 화면으로 이동합니다. 그리고 GitHub Pages로 서비스하고자 하는 브랜치를 설정하고 저장합니다.

GitHub는 기본적으로 `gh-pages` 이름으로 된 Branch를 GitHub Pages용으로 인식합니다. 따라서 `gh-pages` Branch로 build 폴더를 올렸다면, 특별히 설정을 할 필요가 없습니다.

이렇게 설정한 후 상단에 표시된 URL을 방문하면, 아직 React 프로젝트가 화면에 표시되지 않는 것을 확인할 수 있습니다.

{% include in-feed-ads.html %}

## 문제 해결

create-react-app과 react-router로 제작한 React 프로젝트를 GitHub Pages에서 서비스하기 위해서는 몇가지 문제들을 해결해야 합니다.

### PUBLIC_URL

create-react-app으로 개발한 React 프로젝트는 기본적으로 루트(`/`) URL을 기준으로 프로젝트가 생성됩니다. 하지만 우리가 업로드한 GitHub Pasges는 URL에 Repository 이름을 가지고 있습니다. 따라서 React 프로젝트에서 루트 URL이 아닌 Repository 이름을 가진 URL을 사용하도록 수정할 필요가 있습니다.

우선 `./package.json` 파일을 열고 다음과 같이 `homepage`를 추가합니다.

```json
{
  ...,
  "homepage": "https://dev-yakuza-org.github.io/todo"
}
```

`homepage`에 추가하는 URL은 GitHub Pages의 전체 URL에서 마지막 `/`를 제거한 URL을 넣어줍니다.

그리고 react-router의 `BrowserRouter`를 사용하는 부분을 찾아 다음과 같이 수정합니다. 저는 `./src/index.tsx` 파일에서 `BrowserRouter`를 사용하고 있습니다.

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

`BrowserRouter`의 `basename`에 `PUBLIC_URL`을 설정해 줍니다. 여기서 설정한 `PUBLIC_URL`은 `package.json`에 설정한 URL이 적용되게 됩니다.

이렇게 모두 수정하였다면, 다음 명령어를 사용하여 React 프로젝트를 배포합니다.

```bash
npm run build
git commit -am 'Add hompage'
git push origin main
git subtree push --prefix build/ origin gh-pages
```

Private Repository를 사용하는 경우,

```bash
npm run build
cd build
git init
git remote add origin GITHUB_PUBLIC_REPOSITORY_URL
git commit -am 'Add hompage'
git push origin main
```

그리고 GitHub Pages의 URL에 다시 접속해보면, 이전과는 다르게 React 프로젝트가 잘 표시되는 것을 확인할 수 있습니다.

### 404 페이지

React는 SPA(Single Page Application)으로써, 하나의 페이지(index.html)를 가지고 모든 페이지를 서비스하게 됩니다. 따라서, React 프로젝트를 배포하였다면, 모든 URL이 index.html 페이지로 이동하게 만들어야 합니다. 하지만, 안타깝게도 GitHub Pages에서는 그런 기능을 제공하지 않습니다.

이 문제를 해결하기 위해서는 조금 트릭을 사용할 필요가 있습니다. GitHub Pages에서 알 수 없는 URL을 입력한 경우 404 페이지를 표시합니다. GitHub Pages에서 잘못된 URL을 입력한 경우, 모두 404 페이지를 표시하게 됩니다. GitHub Pages에서는 이 404 페이지 커스텀화 할 수 있습니다. 이를 통해 모든 페이지가 한 페이지를 사용하게 만들 수 있습니다.

그럼 문제를 해결하기 위해 `./build/index.html` 파일을 `./build/404.html` 파일로 복사합니다. 그리고 이렇게 복사한 파일을 GitHub Pages에 배포합니다.

이렇게 GitHub Pages를 배포하면, GitHub Pages의 루트 URL로 접근하면 `./build/index.html` 파일이 열리게 되고, 우리가 원하는 동작을 하게 됩니다. 만약 루트 URL이 아닌 다른 URL을 접근하게 되면, 페이지가 존재하지 않기 때문에 `./build/404.html` 파일이 열리게 됩니다. 하지만, `404.html` 페이지 내용이 `index.html`과 동일하기 때문에, 우리가 원하는 동작을 수행하게 됩니다.

이를 자동화 시키기 위해, `./package.json` 파일을 열고 다음과 같이 수정합니다.

```json
...
"scripts": {
  ...
  "build": "react-scripts build && cp build/index.html build/404.html",
  ...
},
...
```

이렇게 `build` 명령어를 수정하면, 빌드가 완료된 후, `index.html` 파일을 복사하여 `404.html` 페이지를 생성하게 됩니다.

## 완료

이번 블로그 포스트에서는 create-react-app과 react-router로 만들어진 React 프로젝트를 GitHub Pages에 배포하는 방법에 대해서 알아보았습니다. 이것으로 여러분은 React 프로젝트로 만든 포트폴리오를 무료로 서비스할 수 있게 되었습니다.

이렇게 무료로 포트폴리오를 서비스할 수 있도록 GitHub Pages를 제공하는 GitHub과 Microsoft에게 감사를 표합니다.
