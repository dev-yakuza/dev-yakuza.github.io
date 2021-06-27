---
layout: 'post'
permalink: '/react/github-actions/prettier-eslint/'
paginate_path: '/react/:num/github-actions/prettier-eslint/'
lang: 'ko'
categories: 'react'
comments: true

title: '[React] GitHub Actions으로 Prettier와 ESLint 사용하기'
description: 'React 프로젝트에 설정한 Prettier와 ESLint를 GitHub Actions를 사용하여 실행해 봅시다.'
image: '/assets/images/category/react/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [GitHub Actions](#github-actions)
- [확인](#확인)
- [완료](#완료)

</div>

## 블로그 시리즈

이 블로그 포스트는 시리즈로 제작되었습니다. 다음은 블로그 시리즈 리스트입니다.

- [[React] Prettier]({{site.url}}/{{page.categories}}/prettier/){:target="_blank"}
- [[React] ESLint]({{site.url}}/{{page.categories}}/eslint/){:target="_blank"}
- [[React] Husky, lint-staged]({{site.url}}/{{page.categories}}/husky-lint-staged/){:target="_blank"}
- [React] GitHub Actions

## 개요

지금까지 create-react-app으로 생성한 React 프로젝트에 Prettier와 ESLint를 설정하고, husky와 lint-staged를 사용하여 Prettier와 ESLint를 자동으로 실행하도록 만들어 보았습니다. 이번 블로그 포스트에서는 GitHub Actions를 사용하여, Pull Request가 만들어졌을 때, Prettier와 ESLint를 실행하도록 해볼 예정입니다.

- GitHub 공식 사이트: [Actions](https://github.com/features/actions){:rel="noopener" target="_blank"}

여기서 소개하는 코드는 아래의 링크에서 확인하실 수 있습니다.

- GitHub: [Todo](https://github.com/dev-yakuza-example/todo){:rel="noopener" target="_blank"}

## GitHub Actions

그럼 GitHub Actions를 사용하기 위해, GitHub Actions의 설정 파일을 만들어 봅시다. `./.github/workflows/main.yml` 파일을 생성하고 다음과 같이 수정합니다.

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

그럼 코드를 좀 더 상세하게 살펴 봅시다.

{% include in-feed-ads.html %}

이 GitHub Actions의 이름은 `Check the source code`입니다.

```yaml
name: Check the source code
...
```

이 GitHub Actions는 `main` 브랜치에 `Pull Request`가 생성되면 실행됩니다.

```yaml
...
on:
  pull_request:
    branches:
      - main
...
```

이 GitHub Actions는 `Check the source code`라는 Flow를 가지고 있으며, `ubuntu`에서 실행됩니다.

```yaml
...
jobs:
  test:
    name: Check the source code
    runs-on: ubuntu-latest
...
```

우선 현재 Repository의 소스 코드를 가져옵니다.

```yaml
...
jobs:
  test:
    ...
    steps:
      - uses: actions/checkout@v2
...
```

이렇게 가져온 소스코드에서 Node 패키지를 설치하고, 미리 정의된 Prettier와 ESLint의 `npm` 스크립트를 실행합니다.

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

이렇게 모든 내용을 수정하였다면, 다음 명령어를 실행하여 해당 내용을 GitHub에 업로드합니다.

```bash
git add .
git commit -m 'Add GitHub Actions'
git push origin main
```

{% include in-feed-ads.html %}

## 확인

이제 이렇게 만든 GitHub Actions를 확인해 봅시다. 다음 명령어를 실행하여 새로운 브랜치를 만듭니다.

```bash
git checkout -b test-pr
```

그리고 `./src/App.tsx` 파일을 열고 다음과 같이 수정합니다.

```js
const App = (): JSX.Element => {
  console.log('test!');
  return (
    ...
  );
};
```

그런 다음, 다음 명령어를 실행하여 해당 내용을 GitHub에 올립니다

```bash
git add .
git commit -m 'Add test code'
git push origin test-pr
```

만약 앞에서 설정한 husky와 lint-staged때문에 `Commit`이 안되는 경우, `./package.json` 파일에서 아래 내용을 찾아 삭제합니다.

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

그리고 다시 아래 명령어를 사용하여 수정한 내용을 GitHub에 업로드합니다.

```bash
git commit -m 'Add test code'
git push origin test-pr
```

이렇게 GitHub에 수정한 내용을 업로드 하였다면, GitHub 사이트로 이동한 후, `Pull requests` 탭을 선택한 후, `New pull request`를 눌러 새로운 Pull Request를 생성합니다.

![GitHub create pull request](/assets/images/category/react/2021/github-actions/create-pull-request.jpg)

GitHub Actions를 잘 설정하였다면, 방금 만든 `Pull request` 하단에 다음과 같이 GitHub Actions에서 에러가 나는 것을 확인할 수 있습니다.

![GitHub actions error](/assets/images/category/react/2021/github-actions/github-actions-error.jpg)

오른쪽에 `Details`를 선택하면, GitHub Actions에서 발생한 에러의 자세한 내용을 확인할 수 있습니다.

![GitHub actions error details](/assets/images/category/react/2021/github-actions/github-actions-error-details.jpg)

우리가 설정한 ESLint의 룰을 지키지 않는 부분이 있어서 에러가 발생한 것을 확인할 수 있습니다. 이것으로 우리가 설정한 GitHub Actions가 제대로 동작하는 것을 확인할 수 있습니다.

## 완료

이것으로 GitHub Actions를 사용하여 Prettier와 ESLint를 실행하는 방법에 대해서 알아보았습니다. husky와 lint-staged를 설정하였기 때문에, 미리 문제를 알 수 있지만, 모든 개발자가 개발 환경이 같지 않을 수 있으므로, 이렇게 GitHub Actions를 생성해 동일한 환경에서 Prettier와 ESLint로 소스코드를 검증할 수 있습니다.

Prettierr와 ESLint이외에도 GitHub Actions로 다양한 기능을 구현할 수 있습니다. 여러분도 GitHub Actions를 사용하여 `CI/CD`를 구현해 보시기 바랍니다.
