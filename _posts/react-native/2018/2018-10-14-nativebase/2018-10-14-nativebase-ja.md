---
layout: 'post'
permalink: '/react-native/nativebase/'
paginate_path: '/react-native/:num/nativebase/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'NativeBase'
description: '基本Component UIでNativeBaseライブラリを使って見ましょう。'
image: '/assets/images/category/react-native/nativebase.jpg'
---

<div id="contents_list" markdown="1">

## 目次

1. [概要](#概要)
1. [ライブラリインストール](#ライブラリインストール)
    - [0.60 以上](#060-以上)
    - [0.59 以下](#059-以下)
1. [使い方](#使い方)
1. [ActionSheet](#actionsheet)
    - [Functional Components - Root](#functional-components---root)
    - [Class Components - Root](#class-components---root)
    - [Functional Components - ActionSheet](#functional-components---actionsheet)
    - [Class Components - ActionSheet](#class-components---actionsheet)
1. [参考](#参考)

</div>

## 概要

リアクトネイティブ(React Native)プロジェクトへmaterial ui componentsである[NativeBase](https://nativebase.io/){:rel="nofollow noreferrer" target="_blank" }を適用して見ましょう。

## ライブラリインストール

下記のコマンドでNativeBaseをインストールします。

{% include_relative common/installation.md %}

インストールが終わったら、下記のコマンドで、ライブラいとプロジェクトをリンクします。

### 0.60 以上

```bash
cd ios
pod install
cd ..
```

### 0.59 以下

{% include_relative common/link.md %}

## 使い方

私たちは基本的使ったことがある場合、ブログを作成します。したがってここには私たちが実際使って分かった内容を追加する予定です。

使い方を詳しく知りたい方は公式サイトを見てください。

- 公式サイト: [NativeBase](https://nativebase.io/){:rel="nofollow noreferrer" target="_blank" }

{% include in-feed-ads.html %}

## ActionSheet

ActionSheetを使うためにはプロジェクト全体をNativeBaseの```<Root>``` component中に入れる必要があります。

### Functional Components - Root

```js
import React from 'react';
import { Root } from 'native-base';
import { ThemeProvider } from 'styled-components';

import Theme from './Theme';

import Navigator from './Screen/Navigator';

interface Props {}
interface State {}

const App = ({}: Props) => {
  return (
    <Root>
    <ThemeProvider theme={Theme}>
        <Navigator />
    </ThemeProvider>
    </Root>
  );
};

export default App;
```

### Class Components - Root

{% include_relative common/action_sheet-1.md %}

ActionSheetを表示する部分へ下記のようにコーディングします。

### Functional Components - ActionSheet

```js
...
import { ActionSheet } from 'native-base';
...
    const ActionButtons = ['English', '日本語', '한국어', 'Cancel'];

    const cancelButtonIndex = ActionButtons.length - 1;

    return (
      <Container>
          <Button
            onPress={() =>
              ActionSheet.show(
                {
                  options: ActionButtons,
                  cancelButtonIndex: cancelButtonIndex,
                  destructiveButtonIndex: cancelButtonIndex,
                },
                (buttonIndex: number) => {
                  alert(buttonIndex);
                }
              )
            }>
            Test
          </Button>
      </Container>
    );
};
```

### Class Components - ActionSheet

{% include_relative common/action_sheet-2.md %}

- options: stringタイプのリスト(string[])やアイコンが含まれたリスト(Array<{ text: string, icon?: string, iconColor?: string }>)の形式を対応します。
- cancelButtonIndex: キャンセルボタンの位置です。
- destructiveButtonIndex: 削除ボタンの位置です。(赤文字ボタンを表示するための部分の位置です。)
- title: ActionSheetのタイトルです。
- (buttonIndex: number) => { alert(buttonIndex); }: 選択されたボタンのindexを貰えます。

## 参考

- 公式サイト: [NativeBase](https://nativebase.io/){:rel="nofollow noreferrer" target="_blank" }