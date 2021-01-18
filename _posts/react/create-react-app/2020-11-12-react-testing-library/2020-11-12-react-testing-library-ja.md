---
layout: 'post'
permalink: '/react/create-react-app/react-testing-library/'
paginate_path: '/react/:num/create-react-app/react-testing-library/'
lang: 'ja'
categories: 'react'
comments: true

title: 'create-react-appでreact-testing-libraryを使ってテストする'
description: 'create-react-appで生成したReactプロジェクトでreact-testing-libraryを使ってテストをする方法について説明します。'
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
- [[TypeScript] create-react-appで絶対パスのimport]({{site.url}}/{{page.categories}}/create-react-app/root-import/){:target="_blank"}
- [Jest]({{site.url}}/{{page.categories}}/create-react-app/jest/){:target="_blank"}
- create-react-appでreact-testing-libraryを使ってテストする

## 概要

以前のブログポストではJavaScriptテストフレームワークである`Jest`を使ってテストの基礎とJavaScriptのテストについて確認しました。今回のブログポストでは`create-react-app`で生成したReactプロジェクトで`react-testing-library`を使ってテストする方法について説明します。

このブログポストで紹介するソースコードは下記のリンクで確認できます。

- GitHub: [https://github.com/dev-yakuza/study-create-react-app/tree/main/6.react-test](https://github.com/dev-yakuza/study-create-react-app/tree/main/6.react-test){:rel="noopener" target="_blank"}

## react-testing-library

以前ブログで紹介した`Jest`はJavaScriptテストフレームワークとして、JavaScriptの全般的なテストに使います。今回紹介する`react-testing-library`はReactをテストするため最適化されたライブラリです。

- react-testing-library: [https://testing-library.com/docs/react-testing-library/intro/](https://testing-library.com/docs/react-testing-library/intro/){:rel="noopener" target="_blank"}

create-react-appでReactプロジェクトを生成すると、`Jest`と同じように`react-testing-library`と一緒にインストールされます。したがって、特にインストールする必要なく、すぐに`react-testing-library`を使うことができます。

今回のブログぷそつでは例題を使ってreact-testing-libraryを使う方法について説明します。

{% include in-feed-ads.html %}

## カウントアプリ開発

簡単な例題を使ってreact-testing-libraryを使う方法を確認するためReactプロジェクトを準備してみましょう。今回のブログポストでは下記のようなカウントアプリを作る要諦です。

![Counter app](/assets/images/category/react/create-react-app/react-testing-library/counter.jpg)

次のコマンドを使ってタイプスクリプトが適用されたReactプロジェクトを生成します。

```bash
npx create-react-app react-test --template=typescript
```

そして絶対パスでコンポーネントを追加するため、`tsconfig.json`ファイルを開いて下記のように修正します。

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

最後にReactプロジェクトで`styled-components`を使うため、下記のコマンドを使って`styled-components`をインストールします。

```bash
npm install --save styled-components
npm install --save-dev @types/styled-components jest-styled-components
```

### Buttonコンポーネント

次はカウントアプリで値を加算したり減算するため使うボタンコンポーネントを作ってみましょう。ボタンコンポーネントを作るため`./src/Components/Button/index.tsx`ファイルを生成して次のように修正します。

```js
import React from "react";
import Styled from "styled-components";

interface ContainerProps {
  readonly backgroundColor?: string;
}

const Container = Styled.div<ContainerProps>`
  padding: 10px 15px;
  border-radius: 5px;
  background-color: ${(props) => props.backgroundColor};
  color: white;
  font-weight: bold;
  cursor: pointer;
`;

interface Props {
  readonly label: string;
  readonly backgroundColor?: string;
  readonly onClick?: () => void;
}
export const Button = ({ label, backgroundColor, onClick }: Props) => {
  return (
    <Container backgroundColor={backgroundColor} onClick={onClick}>
      {label}
    </Container>
  );
};
```

今回のブログではreact-testing-libraryを使ってテストする方法を説明するので、Reactのコンポーネントを作る方法についての説明は省略します。

{% include in-feed-ads.html %}

### Appコンポーネント

次は上で生成したButtonコンポーネントを使ってカウントアプリを生成してみましょう。`./src/App.tsx`ファイルを開いて下記のように修正します。

```js
import React, { useState } from "react";
import Styled from "styled-components";

import { Button } from "Components/Button";

const Container = Styled.div`
  display: flex;
  min-height: 100vh;
  align-items: center;
  justify-content: center;
  background-color: #F5F5F5;
`;

const Label = Styled.div`
  margin: 10px;
  width: 40px;
  text-align: center;
`;

function App() {
  const [count, setCount] = useState(0);
  return (
    <Container>
      <Button
        label="-"
        backgroundColor="#FF1744"
        onClick={() => setCount(count - 1)}
      />
      <Label>{count}</Label>
      <Button
        label="+"
        backgroundColor="#304FFE"
        onClick={() => setCount(count + 1)}
      />
    </Container>
  );
}

export default App;
```

このように作ったカウントアプリがうまく動いてるか確認してみましょう。次のコマンドを実行してカウントアプリを実行します。

```bash
npm start
```

問題なく実行されたら、ブラウザで次のような画面が確認されます。

![create-react-app with typescript](/assets/images/category/react/create-react-app/root-import/project.jpg)

{% include in-feed-ads.html %}

## テスト

次はこのように開発されたカウントアプリをJestとreact-testing-libraryを使ってテストをしてみましょう。まず、既存の`./src/App.test.tsx`ファイルを削除します。そして下記のコマンドを実行してJestを実行します。

```bash
npm run test
```

### Buttonコンポーネントのテスト

まず、Buttonコンポーネントをテストしてみましょう。Buttonコンポーネントをテストするため`./src/Components/Button/index.tsx`ファイルを作って次のように修正します。

```js
import React from 'react';
import { render, screen } from '@testing-library/react';
import 'jest-styled-components';

import { Button } from './index';

describe('<Button />', () => {
  it('renders component correctly', () => {
    const { container } = render(<Button label="button" />);

    const button = screen.getByText('button');
    expect(button).toBeInTheDocument();

    expect(container).toMatchSnapshot();
  });
});
```

一旦ReactをテストするのでReactライブラリを読み込む必要があります。

```js
import React from 'react';
```

私たちはreact-testing-libraryの`render`と`screen`を使ってテストを進める予定です。

```js
import { render, screen } from '@testing-library/react';
```

私たちはコンポーネントをデザインする時`styled-components`を使ってます。そのテストをするためのライブラリを追加します。

```js
import 'jest-styled-components';
```

次は私たちがテストしたいButtonコンポーネントを読み込んで、Jestの`describe`と`it`を使ってテストコードを作成する準備をします。

```js
import { Button } from './index';

describe('<Button />', () => {
  it('renders component correctly', () => {
    ...
  });
});
```

まず、私たちが作ったButtonコンポーネントが画面へうまく表示されるかを確認するため、react-testing-libraryを使ってレンダリングします。

```js
const { container } = render(<Button label="button" />);
```

このようにreact-testing-libraryのrenderを使ってテストしたいコンポーネントをレンダリングしたら、その結果でテストで使えるオブジェクトを返します。ここではスナップショットテストをするため`container`を割り当てました。

Buttonコンポーネントを画面へ表示するためには必須Propsである`label`を設定する必要があります。このように設定した`label`はボタンと一緒に画面へ表示されるので、私たちはこの`label`のテキストを画面から探して、画面に存在するかどうかを確認します。

```js
const button = screen.getByText('button');
expect(button).toBeInTheDocument();
```

そのためreact-testing-libraryの`screen.getByText`を使って画面から、私たちが`label`を使って設定したテキストでコンポーネントを探して、当該コンポーネントが画面に表示されたか`toBeInTheDocument`で確認します。

最後には`toMatchSnapshot`を使ってスナップショットを保存します。

```js
expect(container).toMatchSnapshot();
```

このように保存されたスナップショットはコードの変更から影響を受けたかどうかを知らせる役割をします。

このようにファイルを修正して保存したら、上で実行した`npm run test`のコマンドによって自動でテストコードが実行されて、次のような結果が確認できます。

```bash
 PASS  src/Components/Button/index.test.tsx
  <Button />
    ✓ renders component correctly (27 ms)

Test Suites: 1 passed, 1 total
Tests:       1 passed, 1 total
Snapshots:   1 passed, 1 total
Time:        2.46 s
```

{% include in-feed-ads.html %}

次はButtonコンポーネントの他のPropsをテストしてみましょう。Buttonコンポーネントの必須ではないPropsである`backgroundColor`をテストするため次のような内容を追加します。

```js
it('renders component with backgroundColor', () => {
  render(<Button label="button" backgroundColor="#FF1744" />);

  const button = screen.getByText('button');
  expect(button).toHaveStyleRule('background-color', '#FF1744');
});
```

まず、`backgroundColor`を設定したButtonコンポーネントを画面へ表示します。

```js
render(<Button label="button" backgroundColor="#FF1744" />);
```

その後Buttonコンポーネントの`label`で画面へ表示されたButtonコンポーネントを探して`jest-styled-components`が提供してる`toHaveStyleRule`を使って当該スタイルを持ってるかどうかを確認します。

```js
const button = screen.getByText('button');
expect(button).toHaveStyleRule('background-color', '#FF1744');
```

このようにファイルを修正して保存したら、上で実行した`npm run test`のコマンドによって自動でテストコードが実行されて、次のような結果が確認できます。

```bash
 PASS  src/Components/Button/index.test.tsx
  <Button />
    ✓ renders component correctly (33 ms)
    ✓ renders component with backgroundColor (6 ms)

Test Suites: 1 passed, 1 total
Tests:       2 passed, 2 total
Snapshots:   1 passed, 1 total
Time:        3.669 s
Ran all test suites.
```

{% include in-feed-ads.html %}

最後に、Buttonコンポーネントのクリックイベントをテストしてみましょう。Buttonコンポーネントのクリックイベントをテストするため次のような内容を追加します。

```js
import { render, screen, fireEvent } from '@testing-library/react';
...
it('clicks', () => {
  const onClick = jest.fn();
  render(<Button label="button" onClick={onClick} />);

  expect(onClick).toHaveBeenCalledTimes(0);
  const button = screen.getByText('button');
  fireEvent.click(button);
  expect(onClick).toHaveBeenCalledTimes(1);
});
```

ユーザのイベントをテストするためには、react-testing-libraryが提供する`fireEvent`を使う必要があります。

```js
import { render, screen, fireEvent } from '@testing-library/react';
```

そして実際イベントが発生した時、そのイベントを処理する関数へJestの`Mock Function`を適用します。

```js
const onClick = jest.fn();
render(<Button label="button" onClick={onClick} />);
```

このように適用された`Mock Function`はユーザのクリックイベントが発生した時、コールのカウントをチェックすることで実際クリックイベントが発生したかどうかを確認することができます。最初はクリックイベントが発生してないので当該関数のコールカウントは`0`になります。

```js
expect(onClick).toHaveBeenCalledTimes(0);
```

次は実際react-testing-libraryの`fireEvent`を使ってButtonコンポーネントをクリックしてみて、当該関数のコールカウントが増加したか確認します。

```js
const button = screen.getByText('button');
fireEvent.click(button);
expect(onClick).toHaveBeenCalledTimes(1);
```

このようにファイルを修正して保存したら、上で実行した`npm run test`のコマンドによって自動でテストコードが実行されて、次のような結果が確認できます。

```bash
 PASS  src/Components/Button/index.test.tsx
  <Button />
    ✓ renders component correctly (27 ms)
    ✓ renders component with backgroundColor (4 ms)
    ✓ clicks (7 ms)

Test Suites: 1 passed, 1 total
Tests:       3 passed, 3 total
Snapshots:   1 passed, 1 total
Time:        3.634 s
Ran all test suites.
```

これで私たちが作ったButtonコンポーネントについて全てのテストコードを作成してみました。

{% include in-feed-ads.html %}

### Appコンポーネントのテスト

次はAppコンポーネントをテストしてみましょう。AppコンポーネントはButtonコンポーネントとは違ってPropsがない代わり、Stateを使って動的なデータを管理しています。

Appコンポーネントをテストするため`./src/App.test.tsx`ファイルを生成して次のように修正します。

```js

import React from 'react';
import { render, screen } from '@testing-library/react';
import 'jest-styled-components';

import App from './App';

describe('<App />', () => {
  it('renders component correctly', () => {
    const { container } = render(<App />);

    const minusButton = screen.getByText('-');
    expect(minusButton).toBeInTheDocument();
    expect(minusButton).toHaveStyleRule('background-color', '#FF1744');
    const plusButton = screen.getByText('+');
    expect(plusButton).toBeInTheDocument();
    expect(plusButton).toHaveStyleRule('background-color', '#304FFE');
    const label = screen.getByText('0');
    expect(label).toBeInTheDocument();

    expect(container).toMatchSnapshot();
  });
});
```

Buttonコンポーネントで説明した内容は省略して進めます。まず、Buttonコンポーネントと同じようにAppコンポーネントが画面にうまく表示されたか確認するテストコードを作成してみました。Appコンポーネントは`label`と`backgroundColor`が違う二つのButtonコンポーネントとカウントを表示するコンポーネントを持っています。カウントの初期値は`0`なので画面から`0`が表示されたか確認することでカウントを表示するコンポーネントが画面に表示されたか確認しました。

```js
const minusButton = screen.getByText('-');
expect(minusButton).toBeInTheDocument();
expect(minusButton).toHaveStyleRule('background-color', '#FF1744');

const plusButton = screen.getByText('+');
expect(plusButton).toBeInTheDocument();
expect(plusButton).toHaveStyleRule('background-color', '#304FFE');

const label = screen.getByText('0');
expect(label).toBeInTheDocument();
```

このようにファイルを修正して保存したら、上で実行した`npm run test`のコマンドによって自動でテストコードが実行されて、次のような結果が確認できます。

```bash
 PASS  src/App.test.tsx
  <App />
    ✓ renders component correctly (34 ms)

 › 1 snapshot written.
Snapshot Summary
 › 1 snapshot written from 1 test suite.

Test Suites: 1 passed, 1 total
Tests:       1 passed, 1 total
Snapshots:   1 written, 1 total
Time:        3.316 s
```

次は画面でマイナスボタンをクリックしてStateを使って画面へ表示されたカウントが変わるか確認してみましょう。マイナスボタンをクリックするために次のような内容を追加します。

```js
import { render, screen, fireEvent } from '@testing-library/react';
...
it('clicks minus button', () => {
  render(<App />);

  const minusButton = screen.getByText('-');
  const label = screen.getByText('0');
  expect(label).toBeInTheDocument();

  fireEvent.click(minusButton);
  expect(label.textContent).toBe("-1");
  fireEvent.click(minusButton);
  expect(label.textContent).toBe("-2");
});
```

上でButtonコンポーネントをテストした方法と同じように`fireEvent`を使ってボタンをクリックして画面へ表示されあた値がうまく変更されたかテストしました。

このようにファイルを修正して保存したら、上で実行した`npm run test`のコマンドによって自動でテストコードが実行されて、次のような結果が確認できます。

```bash
 PASS  src/App.test.tsx
  <App />
    ✓ renders component correctly (43 ms)
    ✓ clicks minus button (17 ms)

Test Suites: 1 passed, 1 total
Tests:       2 passed, 2 total
Snapshots:   1 passed, 1 total
Time:        3.82 s
```

{% include in-feed-ads.html %}

マイナスボタンと同じようにプラスボタンもテストしてみましょう。プラスボタンをテストするため次のような内容を追加します。

```js
it('clicks plus button', () => {
  render(<App />);

  const plusButton = screen.getByText('+');
  const label = screen.getByText('0');
  expect(label).toBeInTheDocument();

  fireEvent.click(plusButton);
  expect(label.textContent).toBe("1");
  fireEvent.click(plusButton);
  expect(label.textContent).toBe("2");
});
```

プラスボタンのテストもマイナスボタンのテストと同じように画面へ表示されたプラスボタンをクリックして、画面に表示された値がうまく変更されたか確認しました。

このようにファイルを修正して保存したら、上で実行した`npm run test`のコマンドによって自動でテストコードが実行されて、次のような結果が確認できます。

```bash
 PASS  src/App.test.tsx
  <App />
    ✓ renders component correctly (36 ms)
    ✓ clicks minus button (14 ms)
    ✓ clicks plus button (8 ms)

Test Suites: 1 passed, 1 total
Tests:       3 passed, 3 total
Snapshots:   1 passed, 1 total
Time:        3.705 s
```

これで私たちが開発したカウントアプリを全てテストしてみました。また、全てのテストがうまく動いてることを確認しました。

## コードカバレッジ

そしたら、現在実行中のコマンドをキャンセルして、次のコマンドを実行してコードカバレッジを確認してみましょう。

```bash
npm run test -- --coverage
```

このようにコマンドを実行したら次のように全てのコードについてテストコードがうまく作成されたことが確認できます。

```bash
 PASS  src/Components/Button/index.test.tsx
 PASS  src/App.test.tsx
----------|---------|----------|---------|---------|-------------------
File      | % Stmts | % Branch | % Funcs | % Lines | Uncovered Line #s
----------|---------|----------|---------|---------|-------------------
All files |     100 |      100 |     100 |     100 |
 App.tsx  |     100 |      100 |     100 |     100 |
----------|---------|----------|---------|---------|-------------------

Test Suites: 2 passed, 2 total
Tests:       6 passed, 6 total
Snapshots:   2 passed, 2 total
Time:        2.752 s, estimated 3 s
```

## 完了

これでcreate-react-appで生成したReactプロジェクトをJestとcreate-react-appでテストする方法についてみてみました。ここで作成したテストコードが正解ではなく、色んな方法で同じテストコードを作成することができます。

また、テストカバレッジを使って私たちが作成したテストコードが全てのテストをカバーすることを確認しました。しかし、コードカバレッジをあくまでも確認用なので、100%で信頼しないように注意する必要があります。テストカバレッジが100%が出たことで現在作ったアプリへバグがなくて、私が作ったテストコードが全てのテストケースをテストしてると菅自害しないように注意しましょう。
