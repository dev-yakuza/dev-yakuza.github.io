---
layout: 'post'
permalink: '/react-native/install-on-mac/'
paginate_path: '/react-native/:num/install-on-mac/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'マック(Mac)にreact nativeの開発環境を構築する方法'
description: 'react-nativeでアプリを開発するためマック(Mac)に開発環境を構築して見て、react-nativeのプロジェクトがうまく起動できるか確認して見ます。'
image: '/assets/images/category/react-native/2018/install-on-mac/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

1. [概要](#概要)
1. [Homebrewインストール](#homebrewインストール)
1. [Nodejsインストール](#nodejsインストール)
1. [Watchmanインストール](#watchmanインストール)
1. [React Native CLIインストール](#react-native-cliインストール)
1. [Xcodeインストール](#xcodeインストール)
    - [Cocoapodsインストール](#cocoapodsインストール)
1. [JDKインストール](#jdkインストール)
1. [アンドロイドスタジオインストール](#アンドロイドスタジオインストール)
    - [アンドロイドスタジオ設定](#アンドロイドスタジオ設定)
    - [アンドロイドスタジオSDK設定](#アンドロイドスタジオsdk設定)
    - [アンドロイドスタジオ環境変数設定](#アンドロイドスタジオ環境変数設定)
1. [react-nativeプロジェクト生成や確認](#react-nativeプロジェクト生成や確認)
    - [iOSで確認](#iosで確認)
    - [アンドロイドで確認](#アンドロイドで確認)
1. [完了](#完了)

</div>

## 概要

react-nativeでアプリを開発するため、マック(Mac)に開発環境を設定する方法について説明します。ウィンドウ（Windows)に開発環境を設定する方法については下記のブログを参考してください。

- [ウィンドウ(Windows)にreact nativeの開発環境を構築する方法]({{site.url}}/react-native/install-on-windows/){:target="_blank"}

マック(Mac)でreact-nativeアプリを開発する方法は`Expo CLI`と`React Native CLI`があります。

Expo CLIはreact-nativeでアプリを開発する時よく使うネイティブ機能(位置情報、カメラなど)をパッケージで提供してます。初めてreact-nativeで開発する時は楽かもしれないですが、使ってないネイティブ機能のモジュールのせいでファイルサイズが大きくなる問題とExpoが提供してないネイティブ機能を入れる時不便さなのがあって、このブログではExpoを使うことはお勧めしません。

このブログポストではReact Native CLIを使ってアプリを開発するため開発環境を設定する方法を説明します。また、インストールしたReact Native CLIを使ってプロジェクトを生成して見て、うまく起動するかも確認して見ます。

react-nativeでアプリを開発するためにはnodejs, Watchman, Xcodeなどをインストールする必要があります。各段階を一つ一つ詳しく見て見ます。

## Homebrewインストール

Homebrewはマック(Mac)に必要なパッケージをインストールや管理をする時使うパッケージ管理者です。Homebrewを使うとマック(Mac)に簡単に必要なパッケージをインストールすることが出来ます。

- Homebrew: [https://brew.sh/](https://brew.sh/){:rel="nofollow noreferrer" target="_blank"}

まず、下記のコマンドを使ってマック(Mac)にHomebrewがインストールされたか確認します。

```bash
brew --version
```

もし、Homebrewがインストールされたら下記のようにHomebrewのバージョンが確認出来ます。

```bash
homebrew 2.1.7
homebrew/homebrew-core (git revision f487; last commit 2019-07-20)
```

Homebrewのバージョンが表示されない時は、下記のコマンドを実行してHomebrewをインストールします。

```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

インストールが終わったら、下記のコマンドを実行してインストールが出来たか確認します。

```bash
brew --version
```

インストールが出来たら、下記のようにHomebrewのバージョンが確認出来ます。

```bash
homebrew 2.1.7
homebrew/homebrew-core (git revision f487; last commit 2019-07-20)
```

{% include in-feed-ads.html %}

## Nodejsインストール

react-nativeはJavascriptなのでJavascriptのRuntimeであるNodejsが必要です。

- Nodejs: [https://nodejs.org/](https://nodejs.org/){:rel="nofollow noreferrer" target="_blank"}

下記のHomebrewコマンドでNodejsをインストールします。

```bash
brew install node
```

インストールが終わったら、下記のコマンドでNodejsがうまくインストールされたか確認します。

```bash
node -–version
```

Nodejsが問題なくインストールされたら、下記のようにNodejsバージョンが確認できます。

```bash
v12.6.0
```

Nodejsをインストールすると、基本的Nodejsのパッケージマネージャーであるnpm(Node Package Manater)も一緒にインストールされます。npmもインストールされたか確認するため下記のコマンドを実行して見ます。

```bash
npm --version
```

npmも問題なくインストールされたら、下記のようにnpmのバージョンが確認できます。

```bash
6.9.0
```

## Watchmanインストール

Watchmanは特定フォルダやファイルを監視して変化があったら、特定なアクションを実行するように設定する役割をします。react-nativeはソースコードの追加、変更が発生したら、再ビルドするためWatchmanを使っています。

- Watchman: [https://facebook.github.io/watchman/](https://facebook.github.io/watchman/){:rel="nofollow noreferrer" target="_blank"}

Watchmanをインストールするため下記のHomebrewコマンドを実行します。

```bash
brew install watchman
```

インストールが完了されたら、下記のコマンドを実行してWatchmanがうあくインストールされたか確認します。

```bash
watchman –version
```

Watchmanが問題なくインストールされたら、下記のようにWatchmanのバージョンを確認することできます。

```bash
4.9.0
```

{% include in-feed-ads.html %}

## React Native CLIインストール

react-nativeでアプリを開発するため必要なReact Native CLIをインストールして見ましょう。下記のnpmのコマンドを使ってReact Native CLIをインストールします。

```bash
npm install -g react-native-cli
```

インストールが終わったら、下記のコマンドを実行してReact Native CLIがうまくインストールされたか確認します。

```bash
npx react-native --version
```

問題なくインストールしたら、下記のようにReact Native CLIのバージョンが確認できます。

```bash
react-native-cli: 2.0.1
react-native: n/a - not inside a React Native project
```

## Xcodeインストール

react-nativeでiOSアプリを開発するためにはiOSの開発ツールであるXcodeをインストールする必要があります。下記のリンクを押してアプリストアでXcodeをダウンロードします。

- Xcodeのダウンロードリンク: [https://apps.apple.com/us/app/xcode/id497799835?mt=12](https://apps.apple.com/us/app/xcode/id497799835?mt=12){:rel="nofollow noreferrer" target="_blank"}

Xcodeをインストールしたら、Command Line Toolsを設定する必要があります。Xcodeを実行して上部のメニューで`Xcode > Preferences... > Locations`を押してCommand Line Toolsが設定されたか確認します。

![react-nativeの開発環境設定 - Command Line Tools設定](/assets/images/category/react-native/2018/install-on-mac/configure_command_line_tools.jpg)

もし上のように設定されてないときは、dropdownメニューを選択して一番最新のCommand Line Toolを選択して設定します。

### Cocoapodsインストール

CocoapodsはiOSの開発で使える依存性管理者です。

- Cocoapods: [https://cocoapods.org/](https://cocoapods.org/){:rel="nofollow noreferrer" target="_blank"}

react-nativeでiOSアプリを開発する時、必ず必要なので下記のコマンドでCocoapodsをインストールします。

```bash
sudo gem install cocoapods
```

インストールが終わったら、下記のコマンドでCocoapodsがうまくインストールされたか確認します。

```bash
pod --version
```

問題なくインストールされたら、下記のようにCocoapodsのバージョンが確認できます。

```bash
1.7.5
```

{% include in-feed-ads.html %}

## JDKインストール

react-nativeでアンドロイドアプリを開発するためにはJDK(Java Development Kit)をインストールする必要があります。下記のHomebrewコマンドを実行してJDKをインストールします。

```bash
brew tap AdoptOpenJDK/openjdk
brew cask install adoptopenjdk8
```

インストールが完了されたら、下記のコマンドでJavaがインストールされたか確認します。

```bash
java -version
```

JDKでJavaがインストールされたら、下記のようにJavaのバージョンが確認できます。

```bash
openjdk version "1.8.0_222"
OpenJDK Runtime Environment (AdoptOpenJDK)(build 1.8.0_222-b10)
OpenJDK 64-Bit Server VM (AdoptOpenJDK)(build 25.222-b10, mixed mode)
```

JDKをインストールするとJavaのコンパイラーもインストールされます。下記のコマンドでJavaのコンパイラーもインストールされたか確認します。

```bash
javac -version
```

JDKのインストールでJavaのコンパイラーもインストールされたら、下記のようにJavaのコンパイラーのバージョンが確認されます。

```bash
javac 1.8.0_222
```

## アンドロイドスタジオインストール

react-nativeでアンドロイドアプリを開発するため、アンドロイドスタジオをインストールする必要があります。下記のリンクを押してアンドロイドスタジオのサイトに移動して、インストールファイルをダウンロードします。

- アンドロイドスタジオ: [https://developer.android.com/studio](https://developer.android.com/studio){:rel="nofollow noreferrer" target="_blank"}

ダウンロードが完了されたら、インストールファイルを実行してアンドロイドスタジオを実行します。

### アンドロイドスタジオ設定

アンドロイドスタジオを実行したら下記のような画面が確認できます。

![react-nativeの開発環境設定 - アンドロイドスタジオ設定](/assets/images/category/react-native/2018/install-on-mac/configure_android_studio.jpg)

Nextボタンを押して次の画面に移動します。次の画面に移動したら下記のようにInstall Typeを設定する画面が出ます。Customを洗濯してNextボタンを押して次の画面に移動します。

![react-nativeの開発環境設定 - アンドロイドスタジオインストールタイプ設定](/assets/images/category/react-native/2018/install-on-mac/configure_android_studio_install_type.jpg)

次の画面に移動したら、下記のようにSelect UI Theme画面が確認できます。自分が好きなテーマを選択してNextボタンを押して次に進めます。

![react-nativeの開発環境設定 - アンドロイドスタジオテーマ設定](/assets/images/category/react-native/2018/install-on-mac/configure_android_studio_select_ui_theme.jpg)

次の画面に移動したら、下記のようにSDK Components Setup画面が表示されます。`Performance (Intel ® HAXM)`と`Android Virtual Device`を選択してNextボタンを押してインストールを進めます。

![react-nativeの開発環境設定 - アンドロイドスタジオSDK設定](/assets/images/category/react-native/2018/install-on-mac/configure_android_studio_sdk_components_setup.jpg)

次の画面に移動したら、下記のようにEmulator Settings画面が見えます。特に修正することなくNextボタンを押して次の画面に進めます。

![react-nativeの開発環境設定 - アンドロイドスタジオエミュレータ設定](/assets/images/category/react-native/2018/install-on-mac/configure_android_studio_emulator_settings.jpg)

次の画面からは一般的なプログラムをインストールする方法と同じなので説明を省略します。Finishボタンを押して進めるとアンドロイドスタジオの設定が終わります。

アンドロイドスタジオのインストールが終わったら下記のようにアンドロイドスタジオが実行されることが確認できます。

![react-nativeの開発環境設定 - アンドロイドスタジオの実行](/assets/images/category/react-native/2018/install-on-mac/android_studio.jpg)

{% include in-feed-ads.html %}

### アンドロイドスタジオSDK設定

右下の`Configure > SDK Manger`を選択してアンドロイドSDK設定画面に移動します。

![react-nativeの開発環境設定 - アンドロイドスタジオSDK設定](/assets/images/category/react-native/2018/install-on-mac/android_studio_configure_sdk.jpg)

上のような画面が見えたら、右下の`Show Pacakge Details`を選択します。そしてリストで下記の内容を探して選択します。

- Android SDK Platform 29
- Intel x86 Atom System Image
- Google APIs Intel x86 Atom System Image
- Google APIs Intel x86 Atom_64 System Image

全て選択したら右下のOKボタンを押して選択した内容をインストールします。

### アンドロイドスタジオ環境変数設定

これでアンドロイドスタジオのインストールと設定が終わりました。次はアンドロイドスタジオを環境変数に登録します。環境変数を追加するため`~/.bash_profile`ファイルまたは、`~/.zshrc`ファイルを開いて下記の内容を追加します。

```bash
# export ANDROID_HOME=$HOME/Library/Android/sdk
export ANDROID_HOME=自分のアンドロイドSDKのディレクトリ/Android/sdk
export PATH=$PATH:$ANDROID_HOME/emulator
export PATH=$PATH:$ANDROID_HOME/tools
export PATH=$PATH:$ANDROID_HOME/tools/bin
export PATH=$PATH:$ANDROID_HOME/platform-tools
```

もし`.bash_profile`を使う場合、下記のコマンドを実行してください。

```bash
source ~/.bash_profile
# or
source ~/.zshrc
```

上のコードで自分のアンドロイドSDKのディレクトリを自分の環境に合わせて修正します。自分のアンドロイドSDKのディレクトリが分からない場合、アンドロイドスタジオSDKを設定する画面に移動します。

![react-nativeの開発環境設定 - アンドロイドスタジオSDK設定](/assets/images/category/react-native/2018/install-on-mac/android_studio_configure_sdk.jpg)

アンドロイドスタジオSDKを設定する画面の一番上部を見るとAndroid SDK Locationの項目で自分のアンドロイドSDKのディレクトリが確認できます。

このように環境変数を設定したら、ターミナルを再起動して下記のコマンドを実行して見ます。

```bash
adb
```

環境変数にアンドロイドSDKがうまく設定されたら、下記のような結果が確認できます。

```bash
Android Debug Bridge version 1.0.41
Version 29.0.1-5644136
Installed as /自分のアンドロイドSDKのディレクトリ/platform-tools/adb
```

{% include in-feed-ads.html %}

## react-nativeプロジェクト生成や確認

次は下記のReact Native CLIコマンドでreact-nativeプロジェクトを生成します。

```bash
npx react-native init SampleApp
```

### iOSで確認

生成が完了されたら、下記のコマンドでreact-nativeアプリをiOSで起動させて見ます。

```bash
cd SampleApp
# react-native run-ios
npm run ios
```

うまく実行出来ない場合、`ios/SampleApp.xcworkspace`ファイルを実行して左上のシミュレータを設定するメニューでシミュレータを設定して矢印ボタンを押してシミュレータを実行します。

うまく実行されたら、下記のような画面が見えます。

![react-nativeの開発環境設定 - iOSで実行](/assets/images/category/react-native/2018/install-on-mac/react_native_on_ios.jpg)

### アンドロイドで確認

アンドロイドの場合、開発モードがアクティブされたデバイスをUSBで繋げた状態または、アンドロイドスタジオを実行してエミュレータを実行した状態で下記のコマンドを実行します。

```bash
cd SampleApp
# react-native run-android
npm run android
```

問題なく実行されたら、下記のような画面が確認出来ます。

![react-nativeの開発環境設定 - アンドロイドで実行](/assets/images/category/react-native/2018/install-on-mac/react_native_on_android.jpg)

## 完了

これでマック(Mac)でreact-nativeでアプリを開発するため開発環境を設定する方法を見て見ました。また、開発環境の設定がうまく出来たか確認するため、React Native CLIを使ってアプリを生成して実行して見ました。

react-nativeでアプリを開発する準備が終わりました。react-nativeでアプリを開発する世界にどっぷり浸かってみましょう！
