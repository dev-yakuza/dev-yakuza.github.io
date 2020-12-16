---
layout: 'post'
permalink: '/react-native/styled-components/'
paginate_path: '/react-native/:num/styled-components/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'styled-components'
description: 'react-nativeスタイリングのためstyled-componentsライブラリを活用する方法について説明します。'
image: '/assets/images/category/react-native/styled-components.jpg'
---

<div id="contents_list" markdown="1">

## 目次

1. [リアクトネイティブ(React Native)プロジェクト生成](#リアクトネイティブreact-nativeプロジェクト生成)
1. [styled-componentsライブラリをインストール](#styled-componentsライブラリをインストール)
1. [使い方](#使い方)
    - [Class Componentで基本的使い方](#class-componentで基本的使い方)
    - [Class ComponentでThemeを使う方法](#class-componentでthemeを使う方法)
    - [Functional Componentsで基本的使い方](#functional-componentsで基本的使い方)
   - [Functional ComponentsでThemeを使う方法](#functional-componentsでthemeを使う方法)
1. [参考](#参考)

</div>

## リアクトネイティブ(React Native)プロジェクト生成

typescriptを適用したプロジェクトで進めます。RNへtypescriptを適用する方法は以前のブログをご参考してください。

- [typescript]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}

## styled-componentsライブラリをインストール

styled-componentsライブラリとtypescriptを連動するためのライブラリをインストールします。

{% include_relative common/installation.md %}

- styled-components: styled-componentsライブラリです。
- @types/styled-components: typescriptへ必要なstyled-componentsのタイプです。
- babel-plugin-styled-components: 必須ではないけど、デバッグする時、class名を分かりやすくしてくれます。```babel.config.js```へ下記のように設定します。

```js
module.exports = {
  ...
  plugins: ['babel-plugin-styled-components'],
};
```

{% include in-feed-ads.html %}

## 使い方

styled-componentsは全般的なスタイルを管理するため```theme```の機能を提供してます。```theme```を使う方法と基本的使い方を説明します。

### Class Componentで基本的使い方

- 基本的なスタイル適用する方法

{% include_relative common/basic_usage.md %}

- propsを使って動的にスタイルを適用する方法

{% include_relative common/dynamic_styling.md %}

### Class ComponentでThemeを使う方法

公式サイトにはtypescriptを使ってthemeを使う方法が詳しく書いております。

- 公式サイト: [styled-components#typescript](https://www.styled-components.com/docs/api#typescript){:rel="nofollow noreferrer" target="_blank"}
- 参考サイト: [Styled-Components-Typescript-Example](https://github.com/patrick91/Styled-Components-Typescript-Example){:rel="nofollow noreferrer" target="_blank"}

公式サイトと参考サイトを見たらstyled-componentsを使うためには相対パスを使う問題点があります。

それで私たちは公式サイトの方式ではなく、”propsを使って動的にスタイルを適用する方法”を応用して使ってます。

{% include_relative common/theme_usage.md %}

{% include in-feed-ads.html %}

### Functional Componentsで基本的使い方

```js
import React from 'react';
import styled from 'styled-components/native';

const Container = styled.View`
  flex: 1;
  justify-content: center;
  align-items: center;
  background-color: #f5fcff;
`;
const MainText = styled.Text`
  font-size: 20;
  text-align: center;
  margin: 10px;
  color: red;
`;

interface Props {}
const App = ({}: Props) => {
  return (
    <Container>
      <MainText>Hello world</MainText>
    </Container>
  );
};

export default App;
```

### Functional ComponentsでThemeを使う方法

```js
import React from 'react';
import styled from 'styled-components/native';
import {ThemeProvider} from 'styled-components';
import Theme from './Theme';

interface StyledProps {
  theme: ITheme;
}
const Container = styled.View`
  flex: 1;
  justify-content: center;
  align-items: center;
  background-color: ${(props: StyledProps) =>
    props.theme && props.theme.color.black};
`;
const MainText = styled.Text`
  font-size: 20;
  text-align: center;
  margin: 10px;
  color: red;
`;

interface Props {}
const App = ({}: Props) => {
  return (
    <ThemeProvider theme={Theme}>
      <Container>
        <MainText>Hello world</MainText>
      </Container>
    </ThemeProvider>
  );
};

export default App;
```

## 参考

- styled-components公式サイト: [styled-components](https://www.styled-components.com/docs){:rel="nofollow noreferrer" target="_blank"}
- 参考サイト: [Styled-Components-Typescript-Example](https://github.com/patrick91/Styled-Components-Typescript-Example){:rel="nofollow noreferrer" target="_blank"}
