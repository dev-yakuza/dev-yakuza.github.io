---
layout: 'post'
permalink: '/react/create-react-app/react-router/'
paginate_path: '/react/:num/create-react-app/react-router/'
lang: 'ja'
categories: 'react'
comments: true

title: 'create-react-appでReact Routerを使う方法'
description: 'create-react-appで生成したReactでページ移動機能を実装するためreact-routerを使う方法について説明します。'
image: '/assets/images/category/react/background.jpg'
published: false
---

<div id="contents_list" markdown="1">

## 目次

</div>

## 概要

ReactはUIのJavaScriptライブラリでシングルページアプリケーションのUI(User Interface)を生成することに集中したライブラリです。したがって、UIと関係ないページ移動機能は基本的提供してないです。そのため、Reactでページ移動機能を実装するためには外部のライブラリを使う必要があります。今回のブログポストではReactでページ移動機能を主に使えてる`react-router`について説明します。

- React Routerの公式サイト: [react-router](https://reactrouter.com/){:rel="noopener" target="_blank"}

もし、Reactについてよく知らない方は、下記のリンクを確認してください。

- [Reactとは]({{site.url}}/{{page.categories}}/create-react-app/react/){:target="_blank"}

ここで紹介するコードは下記のリンクで確認できます。

- GitHub: [react_router_example](https://github.com/dev-yakuza/study-create-react-app/tree/main/example/react_router_example){:rel="noopener" target="_blank"}

## プロジェクトの準備

Reactでreact-routerを使ってページ移動機能を実装するためには、Reactプロジェクトを生成する予定です。このブログではCRA(create-react-app)とTypeScriptを使ってReactプロジェクトを生成する予定です。

- [create-react-app]({{site.url}}/{{page.categories}}/create-react-app/start/){:target="_blank"}
- [create-react-app에서 TypeScript]({{site.url}}/{{page.categories}}/create-react-app/typescript/){:target="_blank"}

そしたら次のコマンドを実行してTypeScriptベースのReactプロジェクトを生成します。

```bash
npx create-react-app react_router_example --template=typescript
```

{% include in-feed-ads.html %}

## react-routerのインストール

Reactでreact-routerを使うためにはreact-routerをインストールする必要があります。次のコマンドを実行してreact-routerをインストールします。

```bash
npm install --save react-router-dom
npm install --save-dev @types/react-router-dom
```

## react-routerの使い方

それじゃ、今からreact-routerを使ってReactプロジェクトにページ移動機能を追加してみます。

### Router

Reactプロジェクトでreact-routerを使うためには、まず、`Router`を提供する必要があります。`./src/index.tsx`ファイルを開いて下記のように修正します。

```js
import { BrowserRouter as Router } from 'react-router-dom';

ReactDOM.render(
  <React.StrictMode>
    <Router>
      <App />
    </Router>
  </React.StrictMode>,
  document.getElementById('root')
);
```

react-routerの機能を使うコンポーネントは必ず`Router`の中で宣言する必要があります。react-routerの機能を`Route`の外で使う場合エラーが発生します。

### Switch-Route

react-routerを使ってページ移動をするためには`Switch`と`Route`を使ってページを定義する必要があります。`Switch`と`Route`の使い方を確認するため`./src/App.tsx`ファイルを開いて下記のように修正します。

```js
import { Switch, Route } from 'react-router-dom';
import { Home } from './Pages/Home';
import { Detail } from './Pages/Detail';

function App() {
  return (
    <div>
      <header>This is header</header>
      <Switch>
        <Route exact path="/">
          <Home />
        </Route>
        <Route path="/detail/:id">
          <Detail />
        </Route>
      </Switch>
    </div>
  );
}
```

react-routerでSwitchとRouteを追加しました。また、作ってはないですが、画面に表示する2つのページコンポーネントも追加しました。

```js
import { Switch, Route } from 'react-router-dom';
import { Home } from './Pages/Home';
import { Detail } from './Pages/Detail';
```

このように持ってきたSwitchとRouter、各ページコンポーネントを次のように使います。

```js
<div>
  <header>This is header</header>
  <Switch>
    <Route exact path="/">
      <Home />
    </Route>
    <Route path="/detail/:id">
      <Detail />
    </Route>
  </Switch>
</div>
```

基本的にはRouteはSwitch中で使います。そして`path`のPropsを使って、当該ページのURLを宣言します。最後に子コンポーネントで当該URLのページコンポーネントを追加します。

このように使うと、各URLに合うページが表示されます。もし、ページのURLに動的なデータが含まれたら、`/detail/:id`のように宣言して使うことができます。

```js
<div>
  <header>This is header</header>
  <Switch>
    ...
  </Switch>
</div>
```

URLによって変わる部分はSwitchの中で宣言します。Switchの外で宣言した`<header/>`はURLと関係なくいつも表示されます。

### Link

そしたらHomeページコンポーネントを生成してみて、react-routerのリンクを使う方法を確認してみましょう。`./src/Pages/Home/index.tsx`ファイルを生成して次のように修正します。

```js
import { Link } from 'react-router-dom';

export const Home = () => {
  return (
    <div>
      <div>
        <Link to="/detail/1">Detail 1</Link>
      </div>
      <div>
        <Link to="/detail/2">Detail 2</Link>
      </div>
    </div>
  );
};
```

react-routerでページ移動をするためには`<a/>`タグの代わりreact-routerが提供する`<Link/>`コンポーネントを使います。このLinkコンポーネントは`to`と言うPropsを持っていて、当該Propsに移動先のURLを設定します。

{% include in-feed-ads.html %}

### useHistoryとuseParams

次のようにDetailページコンポーネントを作って`useHistory`と`useParams`フックを使う方法についてみてみましょう。`./src/Pages/Detail/index.tsx`ファイルを生成して下記のように修正します。

```js
import { useHistory, useParams } from 'react-router-dom';

export const Detail = () => {
  const { goBack } = useHistory();
  const params: { id: string } = useParams();

  return (
    <div>
      <div>Detail {params.id}</div>
      <button onClick={goBack}>GoBack</button>
    </div>
  );
};
```

react-routerの`useHistory`フックを使うと、プログラミングでページを移動させることができます。`useHistory`は`replace`, `push`そして`goBack`を提供しております。

- replace: 現在のページを指定されたURLページに置き換え。ブラウザの戻るボタンを使って以前のページに戻ることができない。
- push: 指定されたURLページに移動。ブラウザの戻るボタンで以前のページに戻ることができる。
- goBack: ブラウザの戻るボタン後同じ役割。

react-routerの`useParams`はURLを使って渡した動的なデータを受ける時使います。私たちはDetailページコンポーネントを次のようにURLと連結しました。

```js
<Route path="/detail/:id">
  <Detail />
</Route>
```

そしてHomeページコンポーネントで次のようにURLにデータを設定しました。

```js
<div>
  <Link to="/detail/1">Detail 1</Link>
</div>
<div>
  <Link to="/detail/2">Detail 2</Link>
</div>
```

この時、`1`, `2`は`:id`に割り当てられます。`useParams`を使うと`:id`に割り当てた値を使うことができます。

```js
const params: { id: string } = useParams();
...
<div>Detail {params.id}</div>
```

## 完了

これでReactでページ移動をするためreact-routerをインストールして使う方法についてみてみました。react-routerはこのブログで紹介した機能以外にもたくさんの機能があります。このブログで紹介した機能以外の機能について知りたい方はぜひ公式サイトを参考してみてください。

- React Routerの公式サイト: [Quick Start](https://reactrouter.com/web/guides/quick-start){:rel="noopener" target="_blank"}
