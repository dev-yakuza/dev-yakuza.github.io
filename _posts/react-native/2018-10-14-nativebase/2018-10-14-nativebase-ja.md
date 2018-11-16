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


## 概要
RNプロジェクトへmaterial ui componentsである[NativeBase](https://nativebase.io/){:rel="nofollow noreferrer" target="_blank" }を適用して見ましょう。

## ライブラリインストール
下記のコマンドでNativeBaseをインストールします。

{% include_relative common/installation.md %}

インストールが終わったら、下記のコマンドで、ライブラいとプロジェクトをリンクします。

{% include_relative common/link.md %}

## 使い方
私たちは基本的使ったことがある場合、ブログを作成します。したがってここには私たちが実際使って分かった内容を追加する予定です。

使い方を詳しく知りたい方は公式サイトを見てください。
- 公式サイト: [NativeBase](https://nativebase.io/){:rel="nofollow noreferrer" target="_blank" }

## ActionSheet
ActionSheetを使うためにはプロジェクト全体をNativeBaseの```<Root>``` component中に入れる必要があります。

{% include_relative common/action_sheet-1.md %}

ActionSheetを表示する部分へ下記のようにコーディングします。

{% include_relative common/action_sheet-2.md %}

- options: stringタイプのリスト(string[])やアイコンが含まれたリスト(Array<{ text: string, icon?: string, iconColor?: string }>)の形式を対応します。
- cancelButtonIndex: キャンセルボタンの位置です。
- destructiveButtonIndex: 削除ボタンの位置です。(赤文字ボタンを表示するための部分の位置です。)
- title: ActionSheetのタイトルです。
- (buttonIndex: number) => { alert(buttonIndex); }: 選択されたボタンのindexを貰えます。

## 参考
- 公式サイト: [NativeBase](https://nativebase.io/){:rel="nofollow noreferrer" target="_blank" }