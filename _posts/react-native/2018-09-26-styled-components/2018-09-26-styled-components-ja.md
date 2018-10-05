---
layout: 'post'
permalink: '/react-native/styled-components/'
paginate_path: '/react-native/:num/styled-components/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'styled-components'
description: 'react-nativeスタイリングのためstyled-componentsライブラリを活用する方法について説明します。'
image: '/assets/images/category/react-native/typescript.jpg'
---


## react-nativeプロジェクト生成
typescriptを適用したプロジェクトで進めます。RNへtypescriptを適用する方法は以前のブログをご参考してください。
- [typescript]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}

## styled-componentsライブラリをインストール
styled-componentsライブラリとtypescriptを連動するためのライブラリをインストールします。

{% include_relative common/installation.md %}

- styled-components: styled-componentsライブラリです。
- @types/styled-components: typescriptへ必要なstyled-componentsのタイプです。
- babel-plugin-styled-components: 必須ではないけど、デバッグする時、class名を分かりやすくしてくれます。```.babelrc```へ下記のように設定します。

{% include_relative common/babel-plugin-styled-components.md %}

## 使い方
styled-componentsは全般的なスタイルを管理するため```theme```の機能を提供してます。```theme```を使う方法と基本的使い方を説明します。

### 基本的使い方
- 基本的なスタイル適用する方法

{% include_relative common/basic_usage.md %}

- propsを使って動的にスタイルを適用する方法

{% include_relative common/dynamic_styling.md %}

### Themeを使う方法
公式サイトにはtypescriptを使ってthemeを使う方法が詳しく書いております。
- 公式サイト: [styled-components#typescript](https://www.styled-components.com/docs/api#typescript){:rel="nofollow noreferrer" target="_blank"}
- 参考サイト: [Styled-Components-Typescript-Example](https://github.com/patrick91/Styled-Components-Typescript-Example){:rel="nofollow noreferrer" target="_blank"}

公式サイトと参考サイトを見たらstyled-componentsを使うためには相対パスを使う問題点があります。

それで私たちは公式サイトの方式ではなく、”propsを使って動的にスタイルを適用する方法”を応用して使ってます。

{% include_relative common/theme_usage.md %}

## 参考
- styled-components公式サイト: [styled-components](https://www.styled-components.com/docs){:rel="nofollow noreferrer" target="_blank"}
- 参考サイト: [Styled-Components-Typescript-Example](https://github.com/patrick91/Styled-Components-Typescript-Example){:rel="nofollow noreferrer" target="_blank"}