---
layout: 'post'
permalink: '/react/create-react-app/typescript/'
paginate_path: '/react/:num/create-react-app/typescript/'
lang: 'en'
categories: 'react'
comments: true

title: 'TypeScript in create-react-app'
description: Let's see how to apply TypeScript to the React project created by create-react-app.
image: '/assets/images/category/react/create-react-app/typescript/background.jpg'
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [Create a project](#create-a-project)
- [Apply TypeScript](#apply-typescript)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Modify file extension](#modify-file-extension)
  - [Fix TypeScript error](#fix-typescript-error)
  - [Execution](#execution)
- [Template](#template)
- [Completed](#completed)

</div>

## create-react-app series

This blog post is a series. You can see other blog posts of the series on the list.

- [What is React]({{site.url}}/{{page.categories}}/create-react-app/react/){:target="_blank"}
- [create-react-app]({{site.url}}/{{page.categories}}/create-react-app/start/){:target="_blank"}
- TypeScript in create-react-app
- [Jest]({{site.url}}/{{page.categories}}/create-react-app/jest/){:target="_blank"}

## Outline

In the previous blog post, we've seen how to create the React project with `create-react-app`. In this blog post, I will show how to apply `TypeScript` to the React project created by `create-react-app`.

You can see the source code on the GitHub link below.

- GitHub: [https://github.com/dev-yakuza/study-create-react-app/tree/main/2.typescript](https://github.com/dev-yakuza/study-create-react-app/tree/main/2.typescript){:rel="noopener" target="_blank"}

## Create a project

Execute the command below to create a React project.

```bash
npx create-react-app my-app
```

And then, execute the command below to execute the project.

```bash
# cd my-app
npm start
```

If you don't have any problem, you can see the screen below on your browser.

![create-react-app with TypeScript](/assets/images/category/react/create-react-app/typescript/project.jpg)

{% include in-feed-ads.html %}

## Apply TypeScript

Now, let's see how to apply TypeScript to the React project created `create-react-app`.

### Installation

We need to install libraries to apply `TypeScript` to the React project created by `create-react-app`. Execute the command below to install libraries for `TypeScript`.

```bash
npm install --save typescript @types/node @types/react @types/react-dom @types/jest
```

### Configuration

We need to configure `tsconfig.json` to configure TypeScript.

- [TypeScript Handbook](https://www.typescriptlang.org/){:rel="noopener" target="_blank"}
- [TypeScript Example on React](https://www.typescriptlang.org/play?jsx=2&esModuleInterop=true&e=196#example/typescript-with-react){:rel="noopener" target="_blank"}
- [TypeScript Handbook](https://github.com/typescript-cheatsheets/react#reacttypescript-cheatsheets){:rel="noopener" target="_blank"}

Create `tsconfig.json` and modify it like below.

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

### Modify file extension

We need to modify files extension to make TypeScript recognizes files. modify `.js` to `.tsx` or `.ts` of files in `src` folder.

- App`.js` > App`.tsx`
- App.test`.js` > App.test`.tsx`
- index`.js` > index`.tsx`
- reportWebVitals`.js` > reportWebVitals`.ts`
- setupTests`.js` > setupTests`.ts`

### Fix TypeScript error

After modifying file extensions, TypeScript shows the errors. To fix the errors, add the code below on the top of `App.test.tsx` and `App.tsx` files

```ts
import React from 'react';
```

And then, open `reportWebVitals.ts` file and modify it like below.

```ts
import { ReportHandler } from 'web-vitals';

const reportWebVitals = (onPerfEntry?: ReportHandler) => {
...
```

And, create `./src/custom.d.ts` file and modify it like below.

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

### Execution

After modification, execute the command below to check the project work well.

```bash
npm start
```

If you don't have any problem, you can see the screen like below on your browser.

![create-react-app with TypeScript](/assets/images/category/react/create-react-app/typescript/project.jpg)

{% include in-feed-ads.html %}

## Template

We use create-react-app not to set many configurations to start the React project. However, there are too many settings to use TypeScript. TypeScript becomes an important part of JavaScript, so it's better to use TypeScript for React.

The create-react-app team also known TypeScript's importance, so they provide the `Template` option to set TypeScript simpler. Let's see how to use the `Template` option to configure TypeScript on React.

Execute the command below to create a React project applied TypeScript.

```bash
npx create-react-app my-app --template=typescript
```

After creating, when you open the folder of the project, you can see all configurations that we've done above.

## Completed

In this blog post, we've seen how to configure `TypeScript` to the React project which is created by `create-react-app`. Also, we've seen when we create a new React project with create-react-app, using the `Template` option makes simpler to configure TypeScript to the React project.

Now, you can apply TypeScript to your React project!
