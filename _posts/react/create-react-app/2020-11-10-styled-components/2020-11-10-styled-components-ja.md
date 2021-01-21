---
layout: 'post'
permalink: '/react/create-react-app/styled-components/'
paginate_path: '/react/:num/create-react-app/styled-components/'
lang: 'ja'
categories: 'react'
comments: true

title: 'create-react-appへstyled-componentsの提供'
description: 'create-react-appで生成したReactプロジェクトでstyled-componentsを適用する方法について説明します。'
image: '/assets/images/category/react/create-react-app/styled-components/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [プロジェクト生成](#プロジェクト生成)
- [styled-componentsのインストール](#styled-componentsのインストール)
- [使い方](#使い方)
- [完了](#完了)

</div>

## create-react-appシリーズ

このブログポストはシリーズで作成しております。次は`create-react-app`のシリーズのリストです。

- [Reactとは]({{site.url}}/{{page.categories}}/create-react-app/react/){:target="_blank"}
- [create-react-app]({{site.url}}/{{page.categories}}/create-react-app/start/){:target="_blank"}
- [create-react-appでTypeScriptを使う方法]({{site.url}}/{{page.categories}}/create-react-app/typescript/){:target="_blank"}
- [[TypeScript] create-react-appで絶対パスのimport]({{site.url}}/{{page.categories}}/create-react-app/root-import/){:target="_blank"}
- create-react-appでstyled-componentsの使い方
- [Jest]({{site.url}}/{{page.categories}}/create-react-app/jest/){:target="_blank"}
- [create-react-appでreact-testing-libraryを使ってテストする]({{site.url}}/{{page.categories}}/create-react-app/react-testing-library/){:target="_blank"}

## 概要

このブログポストではReactプロジェクトへ`styled-components`を適用する方法について説明します。

- styled-components: [https://styled-components.com/](https://styled-components.com/){:rel="noopener" target="_blank"}

このブログポストで使ってソースコードはTypeScriptが適用されたソースコードを使う予定です。

ここで紹介するソースコードは下記のリンクで確認できます。

- GitHub: [https://github.com/dev-yakuza/study-create-react-app/tree/main/3.styled-components](https://github.com/dev-yakuza/study-create-react-app/tree/main/3.styled-components){:rel="noopener" target="_blank"}

## プロジェクト生成

次のコマンドを使ってReactプロジェクトを生成します。

```bash
npx create-react-app my-app --template=typescript
```

そして次のコマンドを使ってReactプロジェクトを実行します。

```bash
# cd my-app
npm start
```

問題なくReactプロジェクトが実行されたら下記の画面をブラウザで確認できます。

![create-react-app with styled-components](/assets/images/category/react/create-react-app/styled-components/project.jpg)

{% include in-feed-ads.html %}

## styled-componentsのインストール

`create-react-app`で生成したReactプロジェクトへ`styled-components`を適用するため必要なライブラリをインストールする必要があります。下記のコマンドを使って`styled-components`へ必要なライブラリをインストールします。

```bash
npm install --save styled-components
```

そして私はReactプロジェクトへTypeScriptを使っているので、下記のコマンドを使って`styled-components`のタイプやテストの必要なライブラリをインストールします。

```bash
npm install --save-dev @types/styled-components jest-styled-components
```

## 使い方

次は`styled-components`を使って簡単なコンポーネントを作ってみます。`./src/App.tsx`ファイルを開いて下記のように修正します。

```jsx
import React from 'react';
import Styled from 'styled-components';

const Container = Styled.div`
  background: red;
  width: 100%;
`;
const Label = Styled.div`
  color: white;
  padding: 20px;
`;

const App = () => {
  return (
    <Container>
      <Label>Hello World</Label>
    </Container>
  );
}

export default App;
```

上のように`styled-components`を使って`JSX`ファイルで直接スタイルを作成することができます。

そしてもう使わないファイルは削除します。

- App.css
- logo.svg

他の使い方は公式サイトを参考して下さい。

- styled-components basics: [https://styled-components.com/docs/basics](https://styled-components.com/docs/basics){:rel="noopener" target="_blank"}

## 完了

このブログポストでは`create-react-app`を使って生成したReactプロジェクトへ`styled-components`を適用する方法についてみてみました。そして簡単にJSXファイルでstyled-componentsを使う方法についてもみてみました。

皆さんも今度JSXファイルを使ってstyled-componentsを使ってスタイリングをやてみて下さい。
