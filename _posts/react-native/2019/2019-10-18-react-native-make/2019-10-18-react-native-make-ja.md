---
layout: 'post'
permalink: '/react-native/react-native-make/'
paginate_path: '/react-native/:num/react-native-make/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'React NaitveでAppアイコン & Splashイメージを作る方法'
description: 'react-native-makeライブラリを使ってAppアイコンやSplashイメージを生成する方法について説明します。'
image: '/assets/images/category/react-native/2019/react-native-make/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [react-native-makeインストール](#react-native-makeインストール)
- [Appアイコン](#appアイコン)
- [Splashイメージ](#splashイメージ)
  - [Splashイメージ生成](#splashイメージ生成)
  - [iOS](#ios)
  - [react-native-splash-screen](#react-native-splash-screen)
- [完了](#完了)

</div>

## 概要

React NativeでAppアイコンとSplashイメージを作るため, 今まで[generator-rn-toolbox](https://github.com/bamlab/generator-rn-toolbox){:rel="nofollow noreferrer" target="_blank" }を使っていました。これに関しては下記のブログを確認してください。

- [App icon]({{site.url}}/{{page.categories}}/app-icon/){:target="_blank"}
- [Splashイメージ]({{site.url}}/{{page.categories}}/splash-image/){:target="_blank"}

今までgenerator-rn-toolboxを良く使ってましたが、generator-rn-toolboxを開発した方が、親切に私のブログまで来て新しライブラリを作ったと教えてくれました。

![react-native-makeを使ってAppアイコンやSplashイメージを生成 - 開発者のコメント](/assets/images/category/react-native/2019/react-native-make/comment.jpg)

確認して見たらgenerator-rn-toolboxは`Deprecated`されて、新しく[react-native-make](https://github.com/bamlab/react-native-make){:rel="nofollow noreferrer" target="_blank" }を開発して提供しておりました。

今回のブログではreact-native-makeを使ってアプリアイコンやSplashイメージを生成する方法について調べるし、既存のライブラリより良くなった部分も調べてみます。

## react-native-makeインストール

下記のコマンドを使ってreact-native-makeをインストールします。

```bash
npm install --save-dev @bam.tech/react-native-make
```

これでreact-native-makeを使う準備が終わりました。以前のgenerator-rn-toolboxと少し比べると下記のようです。

generator-rn-toolboxをインストールするときは下記のようにグローバルでインストールしましたし、

```bash
npm install -g yo generator-rn-toolbox
```

下記のようにimagemagickと言うライブラリをインストールする必要がありました。

```bash
brew install imagemagick
```

これと比べて今回のreact-native-makeはローカルでインストールするし、追加で他のライブラリをインストールする必要もありません。

## Appアイコン

react-native-makeを使ってアプリアイコンを生成する時は`1024x1024 px`サイズの`png`ファイルが必要です。

アイコンファイルが準備できたら下記のコマンドを使ってAppアイコンを生成します。

```bash
# react-native set-icon --path [path-to-image]
react-native set-icon --path [path-to-image] --background ["color"]
```

例えば下記のようです。

```bash
# react-native set-icon --path ./src/Assets/images/app_icon.jpg
react-native set-icon --path ./src/Assets/images/app_icon.jpg --background "#FFFFFF"
```

{% include in-feed-ads.html %}

## Splashイメージ

### Splashイメージ生成

react-native-makeを使ってSplashイメージを生成するためには最小`3000x3000px`サイズの`png`ファイルが必要です。

Splashイメージファイルが準備できたら、下記のコマンドを使ってSplashイメージを生成します。

```bash
# react-native set-splash --path [path-to-image]
# react-native set-splash --path [path-to-image] --resize [contain|cover|center]
react-native set-splash --path [path-to-image] --resize [contain|cover|center] --background ["background-color"]
```

例えば下記のようです。

```bash
# react-native set-splash --path ./src/Assets/images/splash.jpg
# react-native set-splash --path ./src/Assets/images/splash.jpg --resize cover
react-native set-splash --path ./src/Assets/images/splash.jpg --resize center --background "#FFFFFF"
```

ここではresizeオプションがありますがデフォルトは`contain`です。また、Coverオプションを使う場合は、重要なイメージが切れないようするため、Splashイメージを作る時重要イメージがバックグラウンドイメージの1/3 paddingところに位置するようにします。

オプションによるイメージの状態は下記のリンクで確認することができます。

- [resize-modes](https://github.com/bamlab/react-native-make/blob/master/docs/set-splash.md#resize-modes){:rel="nofollow noreferrer" target="_blank" }

私は主に単色じゃない背景があるSplashイメージを使っております。この時は`cover`オプションを使って生成すると綺麗なSplashイメージを生成することができました。

### iOS

iOSでSplashイメージを使うためにはSplashイメージ用のStoryboardを設定する必要があります。Storyboardを設定するため`./ios/[Project Name].xcworkspace`ファイルを選択してXcodeを実行します。

![React NaitveでAppアイコン & Splashイメージを作る方法 - add storyboard on iOS ](/assets/images/category/react-native/2019/react-native-make/add_files.jpg)


Xcodeが実行されたら左上のプロジェクトでプロジェクト名を右クリックして`Add Files to "Project Name"`のメニューを選択します。

そして`ios/SplashScreen.storyboard`ファイルを選択して追加します。

![React NaitveでAppアイコン & Splashイメージを作る方法 - setting launch_screen_file](/assets/images/category/react-native/2019/react-native-make/create-splash-screen.jpg)


ファイルを追加したら`General`タブの`Launch Screen File`で`SplashScreen`を入力します。

### react-native-splash-screen

このようにSplashイメージを作ってアプリに適用する理由はこのSplashイメージを使ってSplashイメージを表示してその裏でログイン処理をしたり、データー送受信処理をしたりするためですよね？

このためreact-native-makeは[react-native-splash-screen](https://github.com/crazycodeboy/react-native-splash-screen){:rel="nofollow noreferrer" target="_blank"}を使うようにしております。

react-native-makeだけではなくReact NativeでSplashイメージをコントロールする時には、`react-native-splash-screen`を使ったら結構便利です。これに関して作成したブログがありますので、下記のリンクをご確認してください。

- [App Splashスクリーン]({{site.url}}/{{page.categories}}/react-native-splash-screen/){:target="_blank"}

## 完了

一人でデザインするし、開発する私にはAppアイコンとSplashイメージを作る時、generator-rn-toolboxを良く使いました。今回、新しくできたreact-native-makeも本当に助かると思います。

皆さんもreact-native-makeを使ってもっと簡単にアプリアイコンやSplashイメージを生成してみてください。
