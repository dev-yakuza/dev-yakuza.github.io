---
layout: 'post'
permalink: '/react/create-react-app/root-import/'
paginate_path: '/react/:num/create-react-app/root-import/'
lang: 'ja'
categories: 'react'
comments: true

title: '[TypeScript] create-react-appで絶対パスのimport'
description: 'create-react-appのタイプスクリプトで作ったReactプロジェクトで絶対パスを使ってコンポーネントを追加する方法について説明します。'
image: '/assets/images/category/react/create-react-app/typescript/background.jpg'
published: false
---

<div id="contents_list" markdown="1">

## 目次

</div>

## create-react-appシリーズ

このブログポストはシリーズで作成しております。次は`create-react-app`のシリーズのリストです。

- [Reactとは]({{site.url}}/{{page.categories}}/create-react-app/react/){:target="_blank"}
- [create-react-app]({{site.url}}/{{page.categories}}/create-react-app/start/){:target="_blank"}
- [create-react-appでTypeScriptを使う方法]({{site.url}}/{{page.categories}}/create-react-app/typescript/){:target="_blank"}
- [TypeScript] create-react-appで絶対パスのimport
- [Jest]({{site.url}}/{{page.categories}}/create-react-app/jest/){:target="_blank"}

## 概要

以前のブログでは`create-react-app`を使ってReactプロジェクトにタイプスクリプトを適用する方法について説明しました。今回のブログポストではタイプスクリプトが適用されたReactプロジェクトでコンポーネントを追加する時、相対パスではなく絶対パスを使ってコンポーネントを追加する方法について説明します。

ここで紹介するソースコードは下記のリンクで確認できます。

- GitHub: [https://github.com/dev-yakuza/study-create-react-app/tree/main/3.root-import](https://github.com/dev-yakuza/study-create-react-app/tree/main/3.root-import){:rel="noopener" target="_blank"}

## 相対パスと絶対パス

Reactを使ってプロジェクトを開発すると、私たちはコンポーネントを中心にアプリを開発します。Reactでプロジェクトを開発する時、まず必要なコンポーネントを開発してそのコンポーネントを組み込んでページを作成します。。

このようにReactコンポーネントを組み込んでページを作成する時、普通は早退パス(`import Button from '../../Buttton'`)を使ってコンポーネントを追加します。

コンポーネントがたくさんではない場合、特に問題ないですが、プロジェクトが大きくなってコンポーネントがたくさんになると、プロジェクトのフォルダ構造がどんどん複雑になって、この相対パスでの追加方式はどのパスを指定するかどのコンポーネントを追加してるのか把握することが難しくなります。

このような問題を解決するため、今回のブログポストでは絶対パス(`import Button from 'Buttton'`)でコンポーネントを追加する方法について説明します。

{% include in-feed-ads.html %}

## プロジェクト生成

次のコマンドを使ってタイプスクリプトが適用されたReactプロジェクトを生成します。

```bash
npx create-react-app root-import --template=typescript
```

そして次のコマンドを使ってReactプロジェクトを実行します。

```bash
# cd root-import
npm start
```

問題なくReactプロジェクトが実行されたら下記のような画面がブラウザで確認できます。

![create-react-app with typescript](/assets/images/category/react/create-react-app/root-imprt/project.jpg)

## 絶対パウの設定

타입스크립트가 적용된 React 프로젝트에 절대 경로를 설정하는 방법은 간단하다. 타입스크립트의 설정만 수정하면 바로 컴포넌트를 절대 경로를 사용하여 추가할 수 있다.

그럼 절대 경로로 컴포넌트를 추가하기 위해 `tsconfig.json` 파일을 열고 다음과 같이 수정한다.

```json
{
  "compilerOptions": {
    ...
    "jsx": "react-jsx",
    "baseUrl": "src"
  },
  ...
}
```

이것으로 모든 설정이 끝났다. 정말 간단하다.

## 사용법

그럼 실제로 절대 경로로 컴포넌트를 추가해 보자. 우선, `./src/Components` 폴더를 만들고 `App.js`, `App.css`, `App.test.tsx`, `logo.svg` 파일을 `./src/Components` 폴더 로 이동시킨다.

그리고 `./src/index.js` 파일을 열고 다음과 같이 수정한다.

```js
...
import App from 'Components/App';
...
```

그리고 다음 명령어를 사용하여 React 프로젝트를 실행한다.

```bash
npm start
```

문제없이 설정하였다면, 다음과 같은 화면을 브라우저에서 확인할 수 있다.

![create-react-app with typescript](/assets/images/category/react/create-react-app/root-imprt/project.jpg)

현재는 React 프로젝트가 간단하기 때문에 절대 경로로 컴포넌트를 추가하는 것에 큰 장점이 없어보이지만, 앞으로 React로 프로젝트를 진행하다보면, 이 절대 경로 컴포넌트 추가가 빛을 발하는 것을 목격할 수 있을 것이다.

## 완료

이것으로 create-react-app으로 타입스크립트가 적용된 React 프로젝트에 절대 경로로 컴포넌트를 추가하는 방법에 대해서 알아보았다. 프로젝트 초반에는 큰 장점을 느끼지 못하지만, 프로젝트가 점점 커지면, 정말 편리하다고 느끼게 될 것이다.
