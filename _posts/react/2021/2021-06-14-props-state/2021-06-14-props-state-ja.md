---
layout: 'post'
permalink: '/react/props-state/'
paginate_path: '/react/:num/props-state/'
lang: 'ja'
categories: 'react'
comments: true

title: '[React] PropsとState'
description: 'Reactでデータを扱う重要な概念であるPropsとStateが何なのか説明して、使う方法について説明します。'
image: '/assets/images/category/react/background.jpg'
published: false
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [Props](#props)
- [State](#state)
- [完了](#完了)

</div>

## 概要

Reactでコンポーネントがデータを扱う方法には`Props`、`State`そして`Context`があります。今回のブログポストではPropsとStateに浮いて概念を説明します。

ReactでContextを扱うためContext APIを使う方法については下記のリンクを確認してください。

- [[React] Context API]({{site.url}}/{{page.categories}}/context-api/){:target="_blank"}

## Props

Props(Properties)は親コンポーネントから子コンポーネントに渡すデータを意味します。親コンポーネントから受けたデータなので、子コンポーネントで編集はできません。これはコンポーネントの属性(Properties)と言われます。

- Reactの公式サイト: [Components and Props](https://reactjs.org/docs/components-and-props.html){:rel="noopener" target="_blank"}

私たちは既にHTMLを使う時属性について概念を使ってました。

```html
<div id="name" class="label" onclick="alert('Hello World!');">
  Hello world!
</div>
```

上のコードはHTMLのdivタグにidとclassの属性を設定してonclickの属性に直接JavaScriptのalertのコードを使ってます。このように私たちは既にHTMLの属性と言う概念を使ってました。Reactではこの属性と言う概念にデータを渡す概念を追加して拡張したことです。

```js
const Text = ({text}) => {
  return <div>{text}</div>
}

const App = () => {
  return <Text text='Hello world!'/>
}
```

上のように親コンポーネント(App)から子コンポーネント(Text)に属性(Props)を使って`Hello world!`と言う文字列のデータを渡してるところが確認できます。

{% include in-feed-ads.html %}

## State

Stateは1つのコンポーネント中で流動できなデータを扱う時使うし、コンポーネント中でデータを変更することができます。つまり、Stateは1つのコンポーネントの状態(State)を意味します。

- Reactの公式サイト: [State and Lifecycle](https://reactjs.org/docs/state-and-lifecycle.html){:rel="noopener" target="_blank"}

次の例題は`+`ボタンを押すと、画面に表示された値が1上がるコードです。

```js
import React, { useState } from 'react';

const Text = ({text}) => {
  return <div>{text}</div>
}

const App = () => {
  const [count, setCount] = useState(0);

  return <div>
    <Text text={count} />
    <div onClick={() => setCount(count + 1)}>+</div>
  </div>
}
```

Reactの関数コンポーネントではStateを使うためuseStateと言うフック(Hook)を使います。useStateはState変数の初期値をパラメータで渡してコールして、結果値として配列をリターンします。リターンされた配列にはuseState関数をコールする時設定した初期値が入った変数と当該変数を修正できるSet関数が含まれております。

```js
const 配列 = useState (データの初期値);
```

- 配列[0]: データの初期値が入ってる変数
- 配列[1]: データを修正できるSet関数

普通はリターンされた結果値をJavaScriptの構造分解割り当て(Destructuring assignment)を使って変数とSet関数を割り当てって使います。

```js
const [変数名, Set関数名] = useState (データの初期値);
```

useStateを使って割り当てた変数はImmutableです。したがって、当該値は直接修正が不可能で、当該値を変更するためには必ずSet関数を使う必要があります。

```js
const App = () => {
  const [count, setCount] = useState(0);

  return <div>
    <Text text={count} />
    <div onClick={() => setCount(count + 1)}>+</div>
  </div>
}
```

## 完了

これでReactでコンポーネントがデータを扱う方法であるPropsとStateについて簡単に説明しました。Reactで1つのコンポーネントはコンポーネントの属性を意味して、修正できないデータであるPropsとコンポーネント中でコンポーネントの状態を意味して、変更可能なデータであるStateが存在してることを確認しました。今から皆さんもPropsとStateを使って素敵なReactコンポーネントを作成してみてください。
