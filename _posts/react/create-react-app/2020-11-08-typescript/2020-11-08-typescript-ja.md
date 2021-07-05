---
layout: 'post'
permalink: '/react/create-react-app/typescript/'
paginate_path: '/react/:num/create-react-app/typescript/'
lang: 'ja'
categories: 'react'
comments: true

title: 'create-react-appでTypeScriptを使う方法'
description: 'create-react-appで生成したReactプロジェクトでTypeScriptを使う方法について説明します。'
image: '/assets/images/category/react/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [プロジェクト生成](#プロジェクト生成)
- [TypeScript適用](#typescript適用)
  - [インストール](#インストール)
  - [設定](#設定)
  - [ファイル拡張子修正](#ファイル拡張子修正)
  - [TypeScriptエラー修正](#typescriptエラー修正)
  - [実行](#実行)
- [Template](#template)
- [完了](#完了)

</div>

## create-react-appシリーズ

このブログポストはシリーズで作成しております。次は`create-react-app`のシリーズのリストです。

- [Reactとは]({{site.url}}/{{page.categories}}/create-react-app/react/){:target="_blank"}
- [create-react-app]({{site.url}}/{{page.categories}}/create-react-app/start/){:target="_blank"}
- create-react-appでTypeScriptを使う方法
- [[TypeScript] create-react-appで絶対パスのimport]({{site.url}}/{{page.categories}}/create-react-app/root-import/){:target="_blank"}
- [create-react-appでstyled-componentsの使い方]({{site.url}}/{{page.categories}}/create-react-app/styled-components/){:target="_blank"}
- [Jest]({{site.url}}/{{page.categories}}/create-react-app/jest/){:target="_blank"}
- [create-react-appでreact-testing-libraryを使ってテストする]({{site.url}}/{{page.categories}}/create-react-app/react-testing-library/){:target="_blank"}

## 概要

以前ブログで`create-react-app`を使ってReactプロジェクトを始める方法について説明しました。今回のブログポストでは`create-react-app`で生成したReactプロジェクトで`TypeScript`を使う方法について説明します。

ここで紹介するソースコードは下記のリンクで確認できます。

- GitHub: [https://github.com/dev-yakuza/study-create-react-app/tree/main/2.typescript](https://github.com/dev-yakuza/study-create-react-app/tree/main/2.typescript){:rel="noopener" target="_blank"}

## プロジェクト生成

次のコマンドを使ってReactプロジェクトを生成します。

```bash
npx create-react-app my-app
```

そして次のコマンドを使ってReactプロジェクトを実行します。

```bash
# cd my-app
npm start
```

問題なくReactプロジェクトが実行されたら下記のような画面をブラウザで確認することができます。

![create-react-app with typescript](/assets/images/category/react/create-react-app/typescript/project.jpg)

{% include in-feed-ads.html %}

## TypeScript適用

次は`create-react-app`で生成したReactプロジェクトへTypeScriptを適用する方法について説明します。

### インストール

`create-react-app`で生成したReactプロジェクトへ`TypeScript`を適用するため必要なライブラリをインストールする必要があります。次のコマンドを使って`TypeScript`へ必要なライブラリをインストールします。

```bash
npm install --save typescript @types/node @types/react @types/react-dom @types/jest
```

### 設定

TypeScriptを使うため`tsconfig.json`を使ってTypeScriptに関する設定をする必要があります。

- [TypeScript Handbook](https://www.typescriptlang.org/){:rel="noopener" target="_blank"}
- [TypeScript Example on React](https://www.typescriptlang.org/play?jsx=2&esModuleInterop=true&e=196#example/typescript-with-react){:rel="noopener" target="_blank"}
- [TypeScript Handbook](https://github.com/typescript-cheatsheets/react#reacttypescript-cheatsheets){:rel="noopener" target="_blank"}

TypeScriptのため`tsconfig.json`ファイルを生成して下記のように修正します。

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

### ファイル拡張子修正

次はTypeScriptがソースコードを認識できるようにファイルの拡張子を修正する必要があります。`src`フォルダの`.js`ファイル拡張子を`.tsx`または`.ts`の拡張子で変更します。

- App`.js` > App`.tsx`
- App.test`.js` > App.test`.tsx`
- index`.js` > index`.tsx`
- reportWebVitals`.js` > reportWebVitals`.ts`
- setupTests`.js` > setupTests`.ts`

### TypeScriptエラー修正

このように`.js`ファイル拡張子を`.tsx`または`.ts`で修正したらTypeScriptがエラーを表示します。このエラーを修正するため`App.test.tsx`と`App.tsx`ファイルを開いて最上段へ下記の内容を追加します。

```ts
import React from 'react';
```

そして`reportWebVitals.ts`ファイルを開いて下記のように修正します。

```ts
import { ReportHandler } from 'web-vitals';

const reportWebVitals = (onPerfEntry?: ReportHandler) => {
...
```

そして`./src/custom.d.ts`ファイルを作って下記のように修正します。

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

### 実行

このように修正したReactプロジェクトがうまく起動するか確認するため下記のコマンドを実行してReactプロジェクトを実行します。

```bash
npm start
```

問題なくTypeScriptを設定したら下記のようにReactプロジェクトがブラウザで実行されることが確認できます。

![create-react-app with TypeScript](/assets/images/category/react/create-react-app/typescript/project.jpg)

{% include in-feed-ads.html %}

## Template

create-react-appを使う理由はReactプロジェクトでプロジェクトを生成する時、たくさんの設定をしないためですが、TypeScriptのためたくさんの設定をしました。しかし、TypeScriptは最近のJavaScriptでは重要な役割をしてるのでReactでもTypeScriptを使わなきゃならないです。

create-react-appもこのようなTypeScriptの重要性を認識してるので、TypeScriptをもっと簡単に提供するため`Template`オプションを提供してます。そしたら、create-react-appの`Tempate`オプションを使ってReactのTypeScriptプロジェクトを生成してみましょう。

次のコマンドを実行してReactでTypeScriptが適用されたプロジェクトを生成します。

```bash
npx create-react-app my-app --template=typescript
```

その後、当該フォルダを開いて見ると私たちが上で頑張って設定した内容と同じことが確認できます。

## 完了

今回のブログポストでは`create-react-app`で生成したReactプロジェクトで`TypeScript`を適用する方法についてみてみました。また、create-react-appを使って新しいReactプロジェクトを生成する時、`Template`オプションを使ってもっと簡単にTypeScriptが適用されたReactプロジェクトを生成する方法もみてみました。

今度は皆さんのReactプロジェクトへTypeScriptを適用してみて下さい。
