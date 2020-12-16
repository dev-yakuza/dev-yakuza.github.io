---
layout: 'post'
permalink: '/react-native/splash-image/'
paginate_path: '/react-native/:num/splash-image/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'Splashイメージ'
description: 'generator-rn-toolboxを使ってSplashイメージを設定して見ましょう。'
image: '/assets/images/category/react-native/splash-image.jpg'
---

<div id="contents_list" markdown="1">

## 目次

1. [Deprecated](#deprecated)
1. [概要](#概要)
1. [ライブラリインストール](#ライブラリインストール)
1. [イメージ準備](#イメージ準備)
    - [sketchappからpsdファイル生成](#sketchappからpsdファイル生成)
1. [splashイメージ設定](#splashイメージ設定)
1. [確認](#確認)
1. [エラー対応](#エラー対応)
    - [イメージ生成ができない](#イメージ生成ができない)
1. [Splashイメージコントロール](#splashイメージコントロール)
1. [参考](#参考)

</div>

## Deprecated

このブログポストはgenerator-rn-toolboxが`Deprecated`されたのでもう管理しません。generator-rn-toolboxの新しいライブラリである`react-native-make`を使うことをおすすめします。

react-native-makeに関しては下記のブログをご参考してください。

- [react-native-make]({{site.url}}/{{page.categories}}/react-native-make/){:target="_blank"}

## 概要

mac osxで [generator-rn-toolbox](https://github.com/bamlab/generator-rn-toolbox){:rel="nofollow noreferrer" target="_blank" }を使ってsplashイメージを作る方法を説明します。

## ライブラリインストール

generator-rn-toolbox ライブラリインストールは前回のブログ[App icon]({{site.url}}/{{page.categories}}/app-icon/){:target="_blank"}をご参考してください。

## イメージ準備

splashイメージで使う2208x2208pxサイズのpsdファイルを準備します。

### sketchappからpsdファイル生成

私たちはデザインでsketchappを使ってます。sketchappをpsdファイルのエクスポートができないのでイメージ準備ができませんでしけど、下記のういすればpsdファイルを作ることができます。

1. sketchappでsplashイメージをデザインする。
1. デザインしたsplashイメージをpngでエクスポートする。
1. ネットでpng to psd converterを検索してオンライン変換ツールを探す。(私たちが使った[サイト](https://www.photopea.com/){:rel="nofollow noreferrer" target="_blank" })

{% include in-feed-ads.html %}

## splashイメージ設定

下記のコマンドで角osに合うsplashイメージを生成します。

{% include_relative common/usage.md %}

## 確認

splashイメージが生成されてプロジェクトへ反映されました。プロジェクトを実行してsplashイメージが反映されたかを確認します。

{% include_relative common/start_project.md %}

splashイメージがちゃんと表示されない時はシミュレーター/端末でアプリを削除してもう一度実行してください。

## エラー対応

アンドロイド(Android)でsplashイメージがフルサイズ表示できない問題が発生しました。それで```android/app/src/main/res/drawable/launch_screen_bitmap.xml```を下記のように修正して解決しました。

```xml
<bitmap
    android:src="@drawable/launch_screen"
    android:gravity="fill_horizontal|fill_vertical"/>
```

### イメージ生成ができない

下記のようにエラーがでってイメージが生成されない問題が発生しました。

```bash
Error: Command failed: identify: FailedToExecuteCommand `'gs'
```

下記のコマンドで```ghostscript```をインストールします。

```bash
brew install ghostscript
```

また、下記のコマンドを実行したら、正常に動作することを確認することができます。
다시 아래에 명령어를 실행할 경우, 정상 동작하는 것을 확인하실 수 있습니다.

{% include_relative common/usage.md %}

{% include in-feed-ads.html %}

## Splashイメージコントロール

アプリでSplashイメージをコントロールする場合があります。Splashイメージを画面に表示してその間ログイン処理をしたり、データを取ってくる時があります。このようにSplashイメージをコントロールする必要がある方は下記のブログを参考してください。

- [App Splash スクリーン]({{site.url}}/{{page.categories}}/react-native-splash-screen/){:target="_blank"}

## 参考

- 公式サイト: [generator-rn-toolbox](https://github.com/bamlab/generator-rn-toolbox){:rel="nofollow noreferrer" target="_blank" }
