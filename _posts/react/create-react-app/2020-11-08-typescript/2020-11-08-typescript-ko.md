---
layout: 'post'
permalink: '/react/create-react-app/typescript/'
paginate_path: '/react/:num/create-react-app/typescript/'
lang: 'ko'
categories: 'react'
comments: true

title: 'create-react-app에서 TypeScript'
description: 'create-react-app으로 생성한 React 프로젝트에 Typescript를 적용하는 방법에 대해서 알아봅시다.'
image: '/assets/images/category/react/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [프로젝트 생성](#프로젝트-생성)
- [TypeScript 적용](#typescript-적용)
  - [설치](#설치)
  - [설정](#설정)
  - [파일 확장자 수정](#파일-확장자-수정)
  - [TypeScript 에러 수정](#typescript-에러-수정)
  - [실행](#실행)
- [Template](#template)
- [완료](#완료)

</div>

## create-react-app 시리즈

이 블로그 포스트는 시리즈로 제작되었습니다. 다음은 `create-react-app`의 시리즈 리스트입니다.

- [React란]({{site.url}}/{{page.categories}}/create-react-app/react/){:target="_blank"}
- [create-react-app]({{site.url}}/{{page.categories}}/create-react-app/start/){:target="_blank"}
- create-react-app에서 TypeScript
- [Jest]({{site.url}}/{{page.categories}}/create-react-app/jest/){:target="_blank"}

## 개요

이전 블로그에서 `create-react-app`을 사용하여 React 프로젝트를 시작하는 방법에 대해서 알아보았습니다. 이번 블로그 포스트에서는 `create-react-app`으로 생성한 React 프로젝트에 `TypeScript`를 적용하는 방법에 대해서 알아봅니다.

여기서 소개한 소스코드는 아래에 링크를 통해 확인할 수 있습니다.

- GitHub: [https://github.com/dev-yakuza/study-create-react-app/tree/main/2.typescript](https://github.com/dev-yakuza/study-create-react-app/tree/main/2.typescript){:rel="noopener" target="_blank"}

## 프로젝트 생성

다음 명령어를 사용하여 React 프로젝트를 생성합니다.

```bash
npx create-react-app my-app
```

그리고 다음 명령어를 사용하여 React 프로젝트를 실행해 봅니다.

```bash
# cd my-app
npm start
```

문제없이 React 프로젝트가 실행되면 아래와 같은 화면을 브라우저에서 확인할 수 있습니다.

![create-react-app with TypeScript](/assets/images/category/react/create-react-app/typescript/project.jpg)

{% include in-feed-ads.html %}

## TypeScript 적용

이제 `create-react-app`으로 생성한 React 프로젝트에 TypeScript를 적용하는 방법에 대해서 알아봅시다.

### 설치

`create-react-app`으로 생성한 React 프로젝트에 `TypeScript`를 적용하기 위해 필요한 라이브러리를 설치할 필요가 있습니다. 다음 명령어를 통해 `TypeScript`에 필요한 라이브러리를 설치합니다.

```bash
npm install --save typescript @types/node @types/react @types/react-dom @types/jest
```

### 설정

TypeScript를 사용하기 위해서는 `tsconfig.json`을 사용하여 TypeScript에 관한 설정을 할 필요가 있습니다.

- [TypeScript Handbook](https://www.typescriptlang.org/){:rel="noopener" target="_blank"}
- [TypeScript Example on React](https://www.typescriptlang.org/play?jsx=2&esModuleInterop=true&e=196#example/typescript-with-react){:rel="noopener" target="_blank"}
- [TypeScript Handbook](https://github.com/typescript-cheatsheets/react#reacttypescript-cheatsheets){:rel="noopener" target="_blank"}

그럼 `tsconfig.json` 파일을 생성하고 다음과 같이 수정합니다.

```json
{
  "compilerOptions": {
    "target": "es5",
    "lib": [
      "dom",
      "dom.iterable",
      "esnext"
    ],
    "allowJs": true,
    "skipLibCheck": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noFallthroughCasesInSwitch": true,
    "module": "esnext",
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react"
  },
  "include": [
    "src",
    "custom.d.ts"
  ]
}
```

### 파일 확장자 수정

이제 TypeScript가 소스코드를 인식할 수 있도록 파일의 확장자를 수정할 필요가 있습니다. `src` 폴더에 `.js` 파일 확장자를 `.tsx` 또는 `.ts` 파일 확장자로 변경합니다.

- App`.js` > App`.tsx`
- App.test`.js` > App.test`.tsx`
- index`.js` > index`.tsx`
- reportWebVitals`.js` > reportWebVitals`.ts`
- setupTests`.js` > setupTests`.ts`

### TypeScript 에러 수정

이렇게 `.js` 파일 확장자를 `.tsx` 또는 `.ts`로 수정하면 TypeScript가 에러를 출력합니다. 이 에러를 수정하기 위해 `App.test.tsx`와 `App.tsx` 파일을 열고 최상단에 다음을 추가합니다.

```ts
import React from 'react';
```

그리고 `reportWebVitals.ts` 파일을 열고 아래와 같이 수정합니다.

```ts
import { ReportHandler } from 'web-vitals';

const reportWebVitals = (onPerfEntry?: ReportHandler) => {
...
```

그리고 `./src/custom.d.ts` 파일을 만들고 아래와 같이 수정합니다.

```ts
declare module '*.svg' {
  import * as React from 'react';

  export const ReactComponent: React.FunctionComponent<React.SVGProps<
    SVGSVGElement
  > & { title?: string }>;

  const src: string;
  export default src;
}
```

### 실행

이렇게 수정한 React 프로젝트가 제대로 동작하는지 확인하기 위해서 다음 명령어를 실행하여 React 프로젝트를 실행합니다.

```bash
npm start
```

문제없이 TypeScript를 설정하였다면 다음과 같이 React 프로젝트가 브라우저에서 실행되는 것을 확인할 수 있습니다.

![create-react-app with TypeScript](/assets/images/category/react/create-react-app/typescript/project.jpg)

{% include in-feed-ads.html %}

## Template

create-react-app을 사용하는 이유는 React로 프로젝트를 만들때, 많은 설정들을 하지 않기 위함인데, TypeScript만을 위해 너무 많은 설정을 했습니다. 하지만 TypeScript는 이제 JavaScript에서 중요한 역할을 하고 있기 때문에 React에서도 TypeScript를 사용하지 않을 수 없습니다.

create-react-app도 이렇게 TypeScript에 중요성을 인지하고 있고, TypeScript를 더욱 간단하게 지원하기 위해 `Template` 옵션을 제공하고 있습니다. 그럼 create-react-app의 `Tempate` 옵션을 사용하여 React의 TypeScript 프로젝트를 생성해 보도록 합시다.

다음 명령어를 실행하여 React에 TypeScript가 적용된 프로젝트를 생성합니다.

```bash
npx create-react-app my-app --template=typescript
```

그리고 해당 폴더를 열어보면 우리가 위에서 열심히 설정한 내용과 동일한 것을 볼 수 있습니다.

## 완료

이번 블로그 포스트에서는 `create-react-app`으로 생성한 React 프로젝트에 `TypeScript`를 적용하는 방법에 대해 알아보았습니다. 또한 create-react-app을 사용하여 새로운 React 프로젝트를 생성할 때, `Template` 옵션을 활용하여 더욱 간단하게 TypeScript가 적용된 React 프로젝트를 생성하는 방법도 알아보았습니다.

이제 여러분도 React 프로젝트에 TypeScript를 적용하여 사용해 보시기 바랍니다.
