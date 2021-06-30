---
layout: 'post'
permalink: '/react/context-api/'
paginate_path: '/react/:num/context-api/'
lang: 'ja'
categories: 'react'
comments: true

title: '[React] Context API'
description: 'Reactでデータを扱う概念の1つであるContext APIを使う方法について説明します。
image: '/assets/images/category/react/background.jpg'
published: false
---

<div id="contents_list" markdown="1">

## 目次

</div>

## 概要

Reactでコンポーネントがデータを扱う方法には`Props`、`State`そして`Context`があります。今回のブログポストではContextに関する概念と使い方を説明します。

ReactでPropsとStateの概念と使い方については下記のリンクを確認してください。

- [[React] PropsとState]({{site.url}}/{{page.categories}}/props-state/){:target="_blank"}

ここで紹介するスースコードは下記のリンクで確認できます。

- GitHub: [context_example](https://github.com/dev-yakuza/study-create-react-app/tree/main/example/context_exmaple){:rel="noopener" target="_blank"}

## Context

ReactでPropsとStateは親コンポーネントと子コンポーネント、または1つのコンポーネント中でデータを扱う時使います。このPropsとStateを使う場合、親コンポーネントから子コンポーネント、つまり上から下、片側にデータが流れるようになります。

![React data flow with Props](/assets/images/category/react/2021/context-api/react-data-flow.png)

もし、他のコンポーネントで片側で流れてるデータを使いたい場合、または他のコンポーネントが使ってるデータを現在のデータ流れに入れたい場合はどうすればいいでしょうか？

![React need data in another data flow](/assets/images/category/react/2021/context-api/react-data-flow-another-component.png)

Reactではデータは上から下に流れるので、使いたいデータとこのデータを使うコンポーネントの共通親コンポーネントにStateを作って使いたいデータをPropsで子コンポーネントに渡せば問題を解決することができます。

![React global data with props and state](/assets/images/category/react/2021/context-api/global-data-use-props.png)

しかし、このようにコンポーネント中で共有されるデータのため毎回共通親コンポーネントを修正して全ての子コンポーネントにデータをPropsで渡すことは非常に非効率です。このような問題を解決するためReactでは`Flux`と言う概念を導入し、それに合う`Context API`を提供を始めました。

- Reactの公式サイト: [Context](https://reactjs.org/docs/context.html#consuming-multiple-contexts){:rel="noopener" target="_blank"}

Contextは親コンポーネントから子コンポーネントに渡されるデータの流れとは関係なくグローバル的なデータを扱う時使います。グローバルデータをContextに保存した後、データが必要なコンポーネントで当該データを取ってきて使います。

![React context](/assets/images/category/react/2021/context-api/context.png)

ReactでContextを使うためにはContext APIを使う必要があり、Contextの`Provider`と`Consumer`を使う必要があります。

![React context with Provider and Consumer](/assets/images/category/react/2021/context-api/context.png)

Contextで保存されたデータを使うためには共通親コンポーネントにContextのProviderを使ってデータを提供いて、データを使うコンポーネントではContextのConsumerを使って実際データを使います。

{% include in-feed-ads.html %}

## Contextの使い方

そしたら今からContext APIを使ってReactでグローバルデータを扱う方法について説明します。

### プロジェクト準備

次のコマンドを実行してContextを使うためReactプロジェクトを生成します。

```bash
npx create-react-app context_example --template=typescript
```

### Contextの生成

そして、グローバルデータを保存するためContextを生成してみましょう。`./src/Contexts/Count/index.tsx`ファイルを生成して下記のように修正します。

```js
import { createContext, useState } from 'react';

const CountContext = createContext({
  count: 0,
  plusCount: () => {},
});

interface Props {
  children: JSX.Element | JSX.Element[];
}

const CountProvider = ({ children }: Props): JSX.Element => {
  const [count, setCount] = useState(0);

  const plusCount = (): void => {
    setCount(count + 1);
  };

  return (
    <CountContext.Provider
      value={{
        count,
        plusCount,
      }}>
      {children}
    </CountContext.Provider>
  );
};

export { CountContext, CountProvider };
```

ReactでContextを生成するためにはcreateContextを使います。また、Contextも1つのReactコンポーネントなので、コンポーネント中で変更可能なデータを扱うためStateを使う必要があります。

```js
import { createContext, useState } from 'react';
```

このように追加したcreateContextを使ってContextを生成します。

```js
const CountContext = createContext({
  count: 0,
  plusCount: () => {},
});
```

Contextも1つのReactコンポーネントなので、基本的にはコンポーネントの形をしてます。この時、画面に表示される内容をContextのProviderを包んで提供します。

```js
...
const CountProvider = ({ children }: Props): JSX.Element => {
  ...
  return (
    <CountContext.Provider>
      {children}
    </CountContext.Provider>
  );
};

export { CountContext, CountProvider };
```

Contextは1つのReactコンポーネントです。したがって、内部的に変更可能なデータを使うためにはuseStateを使ってStateを使う必要があります。

```js
const CountProvider = ({ children }: Props): JSX.Element => {
  const [count, setCount] = useState(0);

  const plusCount = (): void => {
    setCount(count + 1);
  };
  ...
};
```

このように作ったStateをContextのProviderに提供します。

```js
const CountProvider = ({ children }: Props): JSX.Element => {
  ...
  return (
    <CountContext.Provider
      value={{
        count,
        plusCount,
      }}>
      {children}
    </CountContext.Provider>
  );
};
```

最後にcreateContextを使って生成したContextとContextのProviderを使って作ったReactコンポーネントをエクスポートします。ContextのProviderを使って作ったReactコンポーネントは共通親コンポーネントに提供する予定で、createContextで生成したContextはデータを消費する時、使う予定です。

```js
export { CountContext, CountProvider };
```

これでグローバルデータを扱うためContextを生成してみました。これからこのContextを使う方法について説明します。

{% include in-feed-ads.html %}

### Provider

上で作ったContextを使うため、共通親コンポーネントである`App`コンポーネントにContextのProviderを提供してみます。ContextのProviderを提供するため、`./src/App.tsx`ファイルを開いて下記のように修正します。

```js
import { CountProvider } from './Contexts/Count';

import { CountLabel } from './Components/CountLabel';
import { PlusButton } from './Components/PlusButton';

function App() {
  return (
    <CountProvider>
      <CountLabel />
      <PlusButton />
    </CountProvider>
  );
}

export default App;
```

Contextを使ってグローバルデータを使うためには共通親コンポーネントでContextのProviderを使う必要があります。ここで使うと言う意味はContextのProviderで包むことを意味します。

```js
import { CountProvider } from './Contexts/Count';
...
function App() {
  return (
    <CountProvider>
      ...
    </CountProvider>
  );
}

export default App;
```

このように`CountProvider`で包んだ部分ではContext内部で生成したグローバルデータを自由にアクセスすることができます。

```js
...
import { CountLabel } from './Components/CountLabel';
import { PlusButton } from './Components/PlusButton';

function App() {
  return (
    <CountProvider>
      <CountLabel />
      <PlusButton />
    </CountProvider>
  );
}
```

またContextを使うコンポーネントを作ってないのでエラーが発生してます。今からContextを使う`CountLabel`コンポーネントと`PlusButton`コンポーネントを作ってみましょう。

### Consumer

Contextを使ってグローバルデータを使うコンポーネントを作成してみましょう。まず、`./src/Components/CountLabel/index.tsx`ファイルを生成して次のように修正します。

```js
import { useContext } from 'react';
import { CountContext } from '../../Contexts/Count';

export const CountLabel = () => {
  const { count } = useContext(CountContext);
  return <div>{count}</div>;
};
```

CountLabelは単純にカウントを画面に表示するコンポーネントです。ここで表示するカウントはグローバル変数で、Contextに宣言した値を使う予定です。このようにContextに宣言された値を使う時、Reactのクラスコンポーネントでは`Consumer`を使いますが、関数コンポーネントでは`useContext`フック（Hook）を使います。

useContextフックを使って私たちが作ったContextであるCountContextをパラメーターで渡すと、createContextで生成した値にアクセスすることができます。

```js
const CountContext = createContext({
  count: 0,
  plusCount: () => {},
});
```

CountLabelではContextのcount変数だけ使います。

{% include in-feed-ads.html %}

次はContextのcount変数の値を上げる`PlusButton`コンポーネントを生成してみましょう。`./src/Components/PlusButton/index.tsx`ファイルを生成して次のように修正します。

```js
import { useContext } from 'react';
import { CountContext } from '../../Contexts/Count';

export const PlusButton = () => {
  const { plusCount } = useContext(CountContext);

  return <button onClick={plusCount}>+ 1</button>;
};
```

PlusButtonは画面に単純に`+ 1`と言うボタンを表示して、そのボタンを押した時、Contextのcount値を上げる関数である`plusCount`関数をコールするコンポーネントです。

CountLabelと同じようにuseContextフックと私たちが作ったContextを使って、グローバルデータであるcountの値を上げる`plusCount`関数を取ってきました。このように取ってきた関数をボタンの`onClick`に連結しました。

### 確認

Contextを使ってグローバルデータを扱う例題を作ってみました。このように作ったReactプロジェクトを確認するため、次のコマンドを使ってReactプロジェクトを実行します。

```bash
npm start
```

Reactプロジェクトが実行されたら次のように`0`と`+ 1`ボタンが表示されることが確認できます。

![React Context example: Count](/assets/images/category/react/2021/context-api/count.npg)

`+ 1`ボタンを押すと、次のようにカウントが上がることが確認できます。

![React Context example: Count increased](/assets/images/category/react/2021/context-api/count_increased.jpg)

## 完了

これでReactでコンポーネントがグローバルデータを扱う方法であるContextについて簡単に説明しました。今回のブログポストの例題ではContextを使わなくてもいいぐらいの小さいプロジェクトだったので、Contextを使う必要性を感じてなかったと思います。しかし、たくさんのコンポーネントを使ってるプロジェクトではContextを使ってデータを共有する場合がありますので、今回の機会でよく勉強して置くと役に立つと思います。
