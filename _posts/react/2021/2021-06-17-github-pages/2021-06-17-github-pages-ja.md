---
layout: 'post'
permalink: '/react/github-pages/'
paginate_path: '/react/:num/github-pages/'
lang: 'ja'
categories: 'react'
comments: true

title: '[React] GitHub Pagesにデプロイ'
description: 'create-react-appで作ったReactプロジェクトをGitHub Pagesにデプロイしてみましょう。'
image: '/assets/images/category/react/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [プロジェクト準備](#プロジェクト準備)
- [Build](#build)
- [アップロード](#アップロード)
  - [Public repository](#public-repository)
  - [Private Repository](#private-repository)
- [GitHub Pagesの設定](#github-pagesの設定)
- [問題解決](#問題解決)
  - [PUBLIC_URL](#public_url)
  - [404ページ](#404ページ)
- [完了](#完了)

</div>

## 概要

GitHub PagesはGitHubが提供してる機能中で1つで、無料で静的なファイルでWebページを作れるようにしてくれるサービスです。今回のブログポストでは`create-react-app`で開発したReactプロジェクトを`GitHub Pages`にデプロイする方法について説明します。

- Reactの公式サイト: [Deployment](https://create-react-app.dev/docs/deployment/){:rel="noopener" target="_blank"}

ここで紹介するコードは下記のリンクで確認できます。

- GitHub: [Todo](https://github.com/dev-yakuza-example/todo){:rel="noopener" target="_blank"}

## プロジェクト準備

今回のブログポストでGitHub PagesにデプロイするReactプロジェクトは`create-react-app`と`react-router`が提供されております。`create-react-app`と`react-router`については下記のブログを参考してください。

- [create-react-app]({{site.url}}/{{page.categories}}/create-react-app/start/){:target="_blank"}
- [[React] React Router]({{site.url}}/{{page.categories}}/react-router/){:target="_blank"}

GitHub Pagesを使ってReactプロジェクトをデプロイするためにはGitHubに`Public`リポジトリが必要です。既存のPrivate Repositoryを持ってる方は新しくPublicリポジトリを生成してください。GitHub PagesでデプロイしたいReactプロジェクトがPublicリポジトリの場合、そのプロジェクトをそのまま使ってください。

## Build

create-react-appで生成したReactプロジェクトをデプロイするためにはReactプロジェクトを`build`する必要があります。次のコマンドを実行してReactプロジェクトを`build`します。

```bash
npm run build
```

{% include in-feed-ads.html %}

## アップロード

このようにビルドしたReactプロジェクトをGitHubにアップロードする必要があります。

### Public repository

すでにReactプロジェクトがPublicリポジトリの場合、buildコマンドで生成された`build`フォルダをGitHubにアップロードする必要があります。`.gitignore`ファイルを開いて下記のように修正します。

```bash
# production
# /build
```

`.gitignore`ファイルを修正したら、次のコマンドを実行して`build`フォルダをGitHubにアップロードします。

```bash
git commit -am 'Add build folder'
git push origin main
```

GitHub Pagesは特定なBranchを使って静的なファイルをサービスします。したがってbuildフォルダのためだけのBranchを作る必要があります。次のコマンドを実行してbuildフォルダだけ新しいBranchにアップロードします。

```bash
git subtree push --prefix build/ origin gh-pages
```

### Private Repository

GitHub PagesはPublicリポジトリの特定Branchを使って静的なファイルをサービスします。したがって、GitHub PagesにデプロイするためにはReactプロジェクトがPrivateリポジトリの場合、buildフォルダの内容をPublicリポジトリにアップロードする必要があります。

次のコマンドを実行してbuildフォルダをPublicリポジトリにアップロードします。

```bash
cd build
git init
git remote add origin GITHUB_PUBLIC_REPOSITORY_URL
git commit -am 'Add build folder'
git push origin main
```

## GitHub Pagesの設定

GitHub Pagesの機能を使って静的なファイルを使ってウェブサービスをするため、GitHubでGitHub Pagesの機能を活性かする必要があります。`build`フォルダをアップロードしたGitHubのページに移動します。

![GitHub pages configuration](/assets/images/category/react/2021/github-pages/settings.jpg)

GitHubページに移動したら、`Settings` > `Pages`を選択してGitHub Pagesの設定画面に移動します。そして、GitHub PagesでサービスするBranchiを設定して保存します。

GitHubは基本的に`gh-pages`の名前のBranchをGitHub Pages用で認識します。したがって、`gh-pages`のBranchでbuildフォルダをアップロードしたら、特に設定することがありません。

このように設定した後、表示されたURLを開くと、またReactプロジェクトが画面に表示されないことが確認できます。

{% include in-feed-ads.html %}

## 問題解決

create-react-appとreact-routerで作成したReactプロジェクトをGitHub Pagesでサービスするためにはいくつかの問題を解決する必要があります。

### PUBLIC_URL

create-react-appで開発したReactプロジェクトは基本的ルート(`/`)URLを基準にしてプロジェクトを生成します。しかし、私たちがアップロードしたGitHub PagesはURLにリポジトリの名前を持ってます。したがって、ReactプロジェクトにルートのURLではなくリポジトリの名前を持つURLを使えるように修正する必要があります。

まず、`./package.json`ファイルを開いて下記のように`homepage`を追加します。

```json
{
  ...,
  "homepage": "https://dev-yakuza-org.github.io/todo"
}
```

`homepage`に追加したURLはGitHub PagesのフールURLで最後の`/`を消したURLを入力します。

そしてreact-routerの`BrowserRouter`を使う部分を探して下記のように修正します。私は`./src/index.tsx`ファイルで`BrowserRouter`を使ってます。

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

`BrowserRouter`の`basename`に`PUBLIC_URL`を設定します。ここで設定した`PUBLIC_URL`は`package.json`に設定したURLが適用されます。

このように全て修正したら、次のコマンドを実行してReactプロジェクトをデプロイします。

```bash
npm run build
git commit -am 'Add hompage'
git push origin main
git subtree push --prefix build/ origin gh-pages
```

Privateのリポジトリの場合、

```bash
npm run build
cd build
git init
git remote add origin GITHUB_PUBLIC_REPOSITORY_URL
git commit -am 'Add hompage'
git push origin main
```

そしてGitHub PagesのURLに再び接続してみると、以前と違ってReactプロジェクトがうまく表示されることが確認できます。

### 404ページ

ReactはSPA(Single Page Application)で、1つのページ(index.html)を使って全てのページをサービスします。したがって、Reactプロジェクトをデプロイしたら、全てのURLがindex.htmlページに移動するようにする必要があります。しかし、GitHub Pagesにはそのような機能がありません。

この問題を解決するためには少しトリックを使う必要があります。GitHub Pagesで間違ったURLを入力する場合、全て404ページが表示されます。GitHub Pagesではこの404ページをカスタム化することができます。これを使うと1つのページを使えるようにすることができます。

そしたら、この問題を解決するため`./build/index.html`ファイルをコピーして`./build/404.html`ファイルを生成します。そしてこのようにコピーしたファイルをGitHub Pagesにデプロイします。

このようにGitHub Pagesにデプロイにデプロイすると、GitHub PagesのルートURLにアクセスすると、`./build/index.html`ファイルが開くようになって、私たちが期待する動きをしてくれます。もし、ルートURLではなく他のURLに接続すると、ページが存在しないので`./build/404.html`ファイルが開きます。しかし、`404.html`のページ内容は`index.html`と同じなので、私たちが設定した動きを実行するようになります。

これを自動化するため、`./package.json`ファイルを開いて下記のように修正します。

```json
...
"scripts": {
  ...
  "build": "react-scripts build",
  "postbuild": "cp build/index.html build/404.html",
  ...
},
...
```

このようにスクリプトを修正すると、ビルドが終わった後、`index.html`ファイルをコピーして`404.html`ページを生成するようになります。

## 完了

今回のブログポストではcreate-react-appとreact-routerで作られたReactプロジェクトをGItHub Pagesにデプロイする方法について説明しました。これで皆さんはReactプロジェクトで作られたポートフォリオを無料でサービスすることができます。

このように無料でポートフォリオをサービスできるようにするGitHub Pagesを提供してるGitHubとMicrosoftに感謝します。
