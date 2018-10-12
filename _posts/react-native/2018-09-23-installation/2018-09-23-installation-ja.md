---
layout: 'post'
permalink: '/react-native/installation/'
paginate_path: '/react-native/:num/installation/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'RNインストール'
description: 'react-nativeをインストールしてプロジェクトが起動するか確認しましょう。'
image: '/assets/images/category/react-native/installation.jpg'
---


## インストール
react-native（RN）をインストールしてプロジェクトが起動するか確認します。

[create-react-native-app](https://github.com/react-community/create-react-native-app){:rel="nofollow noreferrer" :target="_blank"}使ってプロジェクトを作れますが、ここでは [react-native-cli](https://github.com/facebook/react-native#readme){:rel="nofollow noreferrer" :target="_blank"}を使って作ります。

[react-native](https://facebook.github.io/react-native/docs/getting-started){:rel="nofollow noreferrer" :target="_blank"}の公式サイトへインストール方法が詳しく載せてるのでご参考してください。

## react-nativeインストールする前
react-nativeインストールする前(Mac)Node, Watchman / (Windows)Node, python2 jdk8をインストールする必要があります。また、iOSの開発のため、xcodeをAndroidを開発するためにはAndroid studioをインストールする必要があります。

ここではMacはxcodeでWindowsはAndroid studioで作って見ます。

### Mac
- Macは[Homebrew](https://brew.sh/){:rel="nofollow noreferrer" :target="_blank"}を使ってインストールします。

{% include_relative common/install_node_watchman_mac.md %}

- xcodeダウンロードやインストール: [App store](https://itunes.apple.com/us/app/xcode/id497799835?mt=12){:rel="nofollow noreferrer" :target="_blank"}

### Windows
- Windowsは[Chocolatey](https://chocolatey.org/){:rel="nofollow noreferrer" :target="_blank"}を使ってインストールします。

{% include_relative common/install_node_watchman_windows.md %}

- Android studioダウンロードやインストール: [Download](https://developer.android.com/studio/){:rel="nofollow noreferrer" :target="_blank"}
- インストールする時Customオプションを選択して下記の項目をチェックしてインストールしてください。

{% include_relative common/install_custom_android.md %}

- Android SDK ```Android 8.0 (Oreo)```バージョンをインストールしてください。

{% include_relative common/install_android_sdk.md %}

- ANDROID_HOMEを環境変数へ追加

{% include_relative common/android_enviroment_valiable.md %}

- Android仮想デバイス生成: [managing-avds](https://developer.android.com/studio/run/managing-avds){:rel="nofollow noreferrer" :target="_blank"}参考

{% include_relative common/android_avd.md %}

## react-nativeインストール
npmを使ってreact-native-cliをインストールします。

{% include_relative common/install_react_native_cli.md %}

## プロジェクト生成

{% include react-native/create_new_project.md %}

## プロジェクト確認

{% include_relative common/check_project.md %}
