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
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [相対パスと絶対パス](#相対パスと絶対パス)
- [プロジェクト生成](#プロジェクト生成)
- [絶対パウの設定](#絶対パウの設定)
- [使い方](#使い方)
- [完了](#完了)

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

このようにReactコンポーネントを組み込んでページを作成する時、普通は早退パス(`import Button from '../../Button'`)を使ってコンポーネントを追加します。

コンポーネントがたくさんではない場合、特に問題ないですが、プロジェクトが大きくなってコンポーネントがたくさんになると、プロジェクトのフォルダ構造がどんどん複雑になって、この相対パスでの追加方式はどのパスを指定するかどのコンポーネントを追加してるのか把握することが難しくなります。

このような問題を解決するため、今回のブログポストでは絶対パス(`import Button from 'Button'`)でコンポーネントを追加する方法について説明します。

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

![create-react-app with typescript](/assets/images/category/react/create-react-app/root-import/project.jpg)

## 絶対パウの設定

タイプスクリプトが適用されたReactプロジェクトへ絶対ぱあすを設定する方法は簡単です。タイプスクリプトの設定だけ修正すれば、すぐにコンポーネントを絶対パスで追加することができます。

絶対パスでコンポーネントを追加できるようにするため`tsconfig.json`ファイルを下記のように修正します。

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

これで終わりです。本当に簡単ですね。

## 使い方

そしたら実際、絶対パスでコンポーネントを追加してみましょう。まず、`./src/Components`フォルダを作って`App.js`, `App.css`, `App.test.tsx`, `logo.svg`ファイルを`./src/Components`へ移動させます。

そして`./src/index.js`ファイルを開いて下記のように修正します。

```js
...
import App from 'Components/App';
...
```

そして次のコマンドを使ってReactプロジェクトを実行します。

```bash
npm start
```

問題なく設定したら、下記のような画面をブラウザで確認することができます。

![create-react-app with typescript](/assets/images/category/react/create-react-app/root-import/project.jpg)

現在はReactプロジェクトが簡単なので、絶対パスをコンポーネントへ追加することがメリットないように見えますが、Reactプロジェクトを進めると、この絶対パスでコンポーネント追加することが必ず役に立てます。

## 完了

これでcreate-react-appでタイプスクリプトが適用されたReactプロジェクトへ絶対パスでコンポーネントを追加する方法についてみてみました。プロジェクトの始まりではメリットを感じないですが、プロジェクトがどんどん大きくなると本当に便利だと感じると思います。
