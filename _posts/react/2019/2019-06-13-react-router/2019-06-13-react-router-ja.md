---
layout: 'post'
permalink: '/react/react-router/'
paginate_path: '/react/:num/react-router/'
lang: 'ja'
categories: 'react'
comments: true

title: 'React Router'
description: 'react-routerを使ってReact(リアクト)でページ遷移して見ましょう。'
image: '/assets/images/category/react/2019/react-router/background.jpg'
---

## 概要
React(リアクト)はSPA(Single Page Applicatoin)です。言葉とおりページ(Page)が1つ(Single)のアプリケーション(Application)です。このようにページが1つの場合はページ遷移がそもそも不可能です。しかし、このようにページが1つの場合も一般ウェブサイトみたいにURLでページを遷移できるようにしてくれる機能が`React Router`です。

- React Router: [https://github.com/ReactTraining/react-router](https://github.com/ReactTraining/react-router){:rel="nofollow noreferrer" target="_blank"}
- React Router Training: [https://reacttraining.com/react-router/](https://reacttraining.com/react-router/){:rel="nofollow noreferrer" target="_blank"}

React Routerはウェブ(react-router-dom)もネイティブ(react-router-native)でも使えます。このブログポストではReact(リアクト)プロジェクトでReact Router(react-router-dom)を適用してページ遷移を実装してみます。

このブログで紹介してるソースコードはギットバう(Github)で確認できます。

- Github: [https://github.com/dev-yakuza/react_router](https://github.com/dev-yakuza/react_router){:target="_blank"}

## プロジェクトの準備
ここで使うReact(リアクト)プロジェクトは下記のような内容が適用されたプロジェクトです。詳しく内容は各ブログポストを確認してください。

- [WebpackでReactを始める]({{site.url}}/{{page.categories}}/start/){:target="_blank"}
- [ReactでTypescriptを使う方法]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}
- [Reactでstyled-componentsを使う方法]({{site.url}}/{{page.categories}}/styled-components/){:target="_blank"}
- [Reactでroot importする方法]({{site.url}}/{{page.categories}}/root-import/){:target="_blank"}

以前のブログポストでプロジェクトを生成したら下記のようなフォルダ構造が出来上がります。私たちはreact_root_import라는の名前ではなくreact_routerの名前でプロジェクトを生成しました。

```bash
|-- src
|   |-- Components
|   |   |-- Title
|   |   |   |-- index.tsx
|   |-- Features
|   |   |-- Top
|   |   |   |-- index.tsx
|   |-- index.html
|   |-- App.tsx
|-- .babelrc
|-- package.json
|-- webpack.config.js
```

{% include in-feed-ads.html %}

## react-router-domインストール
下記のコマンドで`react-router-dom`をインストールします。

```bash
npm install --save react-router-dom
npm install --save-dev @types/react-router-dom
```

- react-router-dom: React Routerのためのライブラリです。
- @types/react-router-dom: Typescript(タイプスクリプト)を使うためのreact-router-domのタイプ(Type)を定義したライブラリです。


## ページ追加
ページ遷移をテストするためテストページを作ってみます。`src/Features/Page1.tsx`を開いて下記のように修正します。

```js
import * as React from 'react';
import { Link, RouteComponentProps } from 'react-router-dom';

import Title from '~/Components/Title';

interface Props extends RouteComponentProps {}

const Page1 = ({ history }: Props) => {
  return (
    <div>
      <a onClick={history.goBack}>Previous Page</a>
      <Link to="/">Top</Link>
      <Link to="/page2">Page 2</Link>
      <Title label="Page 1" />
    </div>
  );
};

export default Page1;
```

- react-routerでページ遷移で表示されるコンポーネント(Component)は`history`, `location`, `match`のPropsを持っています。このPropsを定義してる`RouteComponentProps`を相続してPropsを処理しました。
- {% raw %}`<a onClick={history.goBack}>Previous Page</a>`{% endraw %}: 以前のページに戻るためreact-routerで貰ったProps(`history`)を使って戻る機能を実装してみました。
- {% raw %}`<Link to="/">Top</Link>`{% endraw %}: React中でreact-routerを使ってページ遷移をするときはreact-router-domの`Link`コンポーネントを使う必要があります。

上と同じテストページをもう1つ作ります。`src/Features/Page2.tsx`を作って下記のように修正します。

```js
import * as React from 'react';
import { Link, RouteComponentProps } from 'react-router-dom';

import Title from '~/Components/Title';

interface Props extends RouteComponentProps {}

const Page2 = ({ history }: Props) => {
  return (
    <div>
      <a onClick={history.goBack}>Previous Page</a>
      <Link to="/">Top</Link>
      <Link to="/page1">Page 1</Link>
      <Title label="Page 2" />
    </div>
  );
};

export default Page2;
```

最後に以前作った`Top`ページを会のように修正してリンクを追加します。

```js
import * as React from 'react';
import { Link, RouteComponentProps } from 'react-router-dom';

import Title from '~/Components/Title';

interface Props extends RouteComponentProps {}
const Top = ({ match, history, location }: Props) => {
  console.log(match);
  console.log(history);
  console.log(location);
  return (
    <div>
      <Link to="/page1">Page 1</Link>
      <Link to="/page2">Page 2</Link>
      <Title label="Hello World!" />
    </div>
  );
};

export default Top;
```

{% include in-feed-ads.html %}

## Routerを作る
私は全般的なルーティング(Routing)を1つのファイルを作ってそこで全てのRouteを管理しています。この部分は必ずこのように管理する必要はないです。皆さんの状況に合わせて使ってくださ氏。私の場合は`src/Router.tsx`を作って下記のように修正しました。

```js
import * as React from 'react';
import { BrowserRouter, Route, Switch, Redirect } from 'react-router-dom';

import Top from './Features/Top';
import Page1 from './Features/Page1';
import Page2 from './Features/Page2';

const Router = () => {
  return (
    <BrowserRouter>
      <Switch>
        <Route exact={true} path="/" component={Top} />
        <Route path="/page1" component={Page1} />
        <Route path="/page2" component={Page2} />
        {/* Not Found */}
        <Route component={() => <Redirect to="/" />} />
      </Switch>
    </BrowserRouter>
  );
};

export default Router;
```

- BrowserRouter: react-routerをウェブ(Browser)上で使うためのコンポーネント(Component)です。
- Switch: 当該Routeの一番上のコンポーネント(Component)を表示します。
- Route: 当該URL(path)に合うコンポーネント(component)を表示します。

ここでSwitchの役割について説明が足りないと思ってもうちょっと詳しくみてみます。現在の設定を下記のように修正してみます。

```js
<BrowserRouter>
    <Switch>
        <Route exact={true} path="/" component={Top} />
        <Route path="/page1" component={Page1} />
        <Route path="/page1" component={Page2} />
        <Route path="/page2" component={Page2} />
        {/* Not Found */}
        <Route component={() => <Redirect to="/" />} />
    </Switch>
</BrowserRouter>
```

上のように設定して下記のコマンドでWebpack(ウェブパック)の開発サーバーを起動します。

```bash
npm start
```

そして、ブラウザで`page1`に移動して確認したら`Page1`だけ表示されることが確認できます。しかし、下記のように`Switch`を消して

```js
<BrowserRouter>
    <Route exact={true} path="/" component={Top} />
    <Route path="/page1" component={Page1} />
    <Route path="/page1" component={Page2} />
    <Route path="/page2" component={Page2} />
    {/* Not Found */}
    <Route component={() => <Redirect to="/" />} />
</BrowserRouter>
```

ブラウザで`page1`に移動して確認すると`Page1`と`Page2`が表示されることが確認できます。このように同じURLが存在する場合、`Switch`は上部に宣言されたコンポーネント(Component)だけ表示します。


## App.tsx修正
最後は私たちが作ったRouterが動作できるように`src/App.tsx`を下記のように修正します。

```js
import * as React from 'react';
import * as ReactDOM from 'react-dom';

import Router from './Router';

interface Props {}
const App = ({  }: Props) => {
  return <Router />;
};

ReactDOM.render(<App />, document.getElementById('app'));
```

## Webpack修正
現在の状態で`npm start`を実行したら画面にTopページが表示されてリンクを使ってページ遷移がうまくできることが確認できます。しかし`http://localhost:8080/page1`や`http://localhost:8080/page2`を直接入力したら404エラーが出ます。上でも説明しましたが、SPA(Single Page Applicatoin)なので実際は1つのページだけ存在するのでこのような問題が発生します。私たちはWebpack(ウェブパック)の設定でこの部分を解決します。`webpack.config.js`を開いて下記のように修正します。

```js
...
module.exports = {
  mode: process.env.NODE_ENV,
  entry: {
   ...
  },
  output: {
    ...
  },
  module: {
    ...
  },
  resolve: {
    extensions: ['.ts', '.tsx', '.js', '.jsx'],
  },
  plugins: [
    ...
  ],
  devServer: {
    contentBase: './dist',
    port: 3000,
    historyApiFallback: true,
  },
};
```

上のように`devServer`オプションを使って`webpack-dev-server`を設定しました。`historyApiFallback`を使って存在しないURLの場合、404レスポンス(Response)ではなく`index.html`をレスポンス(Response)するように設定しました。もう一回`http://localhost:3000/page1`や`http://localhost:3000/page2`を直接入力してページを移動すると当該ページが表示されることが確認できます。

## 確認
下記のコマンドでWebpack(ウェブパック)開発サーバーを起動してみます。

```bash
npm start
```

そしてブラウザを開いて`http://localhost:3000/`に移動します。(Gitソースは`--open`オプションがあるので児童にブラウザが開いて当該ページに移動します。)

画面に表示されるリンクを押してページを移動してみます。そしたら、問題なくページ遷移ができることが確認できます。また、直接`http://localhost:3000/page1`や`http://localhost:3000/page2`を入力しても問題なくページが表示されることが確認できます。

最後に下記のコマンドでビルド(Build)ができるか確認してみます。

```bash
npm run build
```

ビルド(Build)が終わったら`dist/`にファイルやフォルダが生成されたことが確認出来ます。
