---
layout: 'post'
permalink: '/react-native/react-native-tts/'
paginate_path: '/react-native/:num/react-native-tts/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'react-native-tts'
description: 'react-native-ttsを使ってtext-to-speech機能を作って見ましょう。'
image: '/assets/images/category/react-native/react-native-tts.jpg'
---


## 概要
[react-native-tts](https://github.com/ak1394/react-native-tts){:rel="nofollow noreferrer" :target="_blank" }を使ってRNプロジェクトでtext-to-speech機能を作って見ます。

## react-native-ttsライブラリインストール
下記のコマンドでreact-native-ttsをインストールします。

{% include_relative common/installation.md %}

インストールが終わったら下記のコマンドでreact-native-ttsライブラリとRNプロジェクトをリンクします。

{% include_relative common/link.md %}

## 使い方
私たちは基本的使ったことがある場合、ブログを作成します。したがってここには私たちが実際使って分かった内容を追加する予定です。

使い方を詳しく知りたい方は公式サイトを見てください。
- 公式サイト: [react-native-tts](https://github.com/ak1394/react-native-tts){:rel="nofollow noreferrer" :target="_blank" }

## text-to-speech.
下記の方法でtext-to-speechを実行します。

{% include_relative common/usage.md %}

- setDefaultLanguage: Default言語を設定します。言語コードは[Language codes](https://docs.fedoraproject.org/en-US/Fedora_Contributor_Documentation/1/html/Users_Guide/appe-Users_Guide-Language_codes.html){:rel="nofollow noreferrer" :target="_blank" }を参考してください。
- speak: この単語を読みます。

## 参考
- 公式サイト: [react-native-tts](https://github.com/ak1394/react-native-tts){:rel="nofollow noreferrer" :target="_blank" }
- Language codes: [Language codes](https://docs.fedoraproject.org/en-US/Fedora_Contributor_Documentation/1/html/Users_Guide/appe-Users_Guide-Language_codes.html){:rel="nofollow noreferrer" :target="_blank" }