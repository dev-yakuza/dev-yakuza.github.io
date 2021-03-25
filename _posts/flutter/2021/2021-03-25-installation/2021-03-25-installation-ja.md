---
layout: 'post'
permalink: '/flutter/installation/'
paginate_path: '/flutter/:num/installation/'
lang: 'ja'
categories: 'flutter'
comments: true

title: '[MacOS] Flutterのインストール'
description: MacOSへFlutterをインストールする方法を説明します。
image: '/assets/images/category/flutter/background.png'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [Xcode](#xcode)
- [Android Studio](#android-studio)
- [Flutter SDK インストール](#flutter-sdk-インストール)
- [パスの設定](#パスの設定)
- [依存性のインストール](#依存性のインストール)
- [確認](#確認)
- [完了](#完了)

</div>

## 概要

FlutterはReact Nativeと同じように一つの言語でiOSとアンドロイドアプリ、両方を開発することができるクロスプラットフォームモバイルアプリ開発プラットフォームです。最近ウェブまで拡張してどんどん対応OSを拡大しております。

- Flutter: [公式サイト](https://flutter.dev/){:rel="nofollow noreferrer" target="_blank"}

今回のブログポストではマックへFlutterでアプリを開発するため、Flutterをマックへインストールする方法について調べます。他のOSへFlutterをインストールする方法は公式サイトを参考してください。

- 公式サイト: [https://flutter.dev/docs/get-started/install](https://flutter.dev/docs/get-started/install){:rel="nofollow noreferrer" target="_blank"}

## Xcode

Flutterはクロスプラットフォームアプリ開発プラットフォームなのでiOSのアプリを開発することができます。iOSアプリを開発する時にはiOSのシミュレーターを使いますし、リリースするときはXcodeを使います。したがって、Flutterでアプリを開発する場合もXcodeはインストールする必要があります。

- Xcode: [Web](https://developer.apple.com/xcode/){:rel="nofollow noreferrer" target="_blank"}
- Xcode: [Mac App Store](https://itunes.apple.com/us/app/xcode/id497799835){:rel="nofollow noreferrer" target="_blank"}

上のリンクを使ってXcodeをインストールした後、下記のコマンドを実行してXcodeを設定します。

```bash
sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer
sudo xcodebuild -runFirstLaunch
sudo xcodebuild -license
sudo gem install cocoapods
```

## Android Studio

iOSと同じようにFlutterではアンドロイドのアプリを開発することができます。しかし、アンドロイドのエミュレーターを使う時、アプリをデプロイするためにはAndroid Studioが必要です。

次のリンクを使ってAndroid Studioをダンロードして、インストールします。

- [Android Studio](https://developer.android.com/studio){:rel="nofollow noreferrer" target="_blank"}

{% include in-feed-ads.html %}

## Flutter SDK インストール

Flutterでアプリを開発するため、FlutterのSDKをインストールする必要があります。まず、下記のコマンドを使ってFlutter SDKをダウンロードするフォルダを生成します。

```bash
mkdir ~/development
cd ~/development
```

このようにFlutter SDKをダウンロードするフォルダを生成したら、下記のコマンドを使ってFlutter SDKをCloneします。

```bash
git clone https://github.com/flutter/flutter.git -b stable
```

また、次のコマンドを使ってウェブを通じてデプロイされたFlutter SDKをダウンロードができます。

```bash
curl -O https://storage.googleapis.com/flutter_infra/releases/stable/macos/flutter_macos_2.0.3-stable.zip
unzip flutter_macos_2.0.3-stable.zip
```

## パスの設定

Flutter SDKを使うためにはFlutter SDKのパスを設定する必要があります。次のコマンドを使ってパスを追加するためファイルを修正します。

```bash
code ~/.zshrc
```

そして当該ファイルの一番下に次の内容を追加します。

```bash
...
export PATH=$HOME/development/flutter/bin:$PATH
```

{% include in-feed-ads.html %}

## 依存性のインストール

まずFlutterでアプリを開発するため、必要なSDKやToolをインストールする必要があります。次のコマンドを実行してFlutterでアプリを開発するため必要なものをインストールします。

```bash
flutter doctor
```

Flutter SDKを`git clone`でコピーした場合はSDKをビルドするので、結構時間がかかります。SDKをウェブでダウンロードした場合はビルドの内容も含まれてるので、少し早く進めます。

実行が終わったら下記のような結果がみれます。

```bash
[✓] Flutter (Channel stable, 2.0.3, on macOS 11.2.3 20D91 darwin-x64, locale en)
[!] Android toolchain - develop for Android devices (Android SDK version 29.0.3)
    ! Some Android licenses not accepted.  To resolve this, run: flutter doctor --android-licenses
[✓] Xcode - develop for iOS and macOS
[✓] Chrome - develop for the web
[✓] Android Studio (version 3.6)
[✓] VS Code (version 1.54.2)
[✓] Connected device (1 available)
```

私は`Android toolchain`が失敗しました。失敗メッセージで表示されたコマンドを実行して`Android toolchain`を設定します。

```bash
flutter doctor --android-licenses
```

そして、また`flutter doctor`を実行すると下記のように全てのものがうまくインストールされたことが確認できます。

```bash
Doctor summary (to see all details, run flutter doctor -v):
[✓] Flutter (Channel stable, 2.0.3, on macOS 11.2.3 20D91 darwin-x64, locale en)
[✓] Android toolchain - develop for Android devices (Android SDK version 29.0.3)
[✓] Xcode - develop for iOS and macOS
[✓] Chrome - develop for the web
[✓] Android Studio (version 3.6)
[✓] VS Code (version 1.54.2)
[✓] Connected device (1 available)
```

このように`flutter doctor`はFlutterでアプリ開発に必要なSDKやツールをインストールしてくれます。

## 確認

このように全てのもののインストールが終わったら、Flutterアプリを生成してみて、アプリがうまく実行されるか確認してみましょう。次のコマンドを実行してFlutterで開発するアプリを生成します。

```bash
flutter create my_app
```

そしてアンドロイドのエミュレーターまたはiOSのシミュレーターを実行して次のコマンドを使って生成したアプリを実行します。

```bash
cd my_app
flutter run
```

iOSのシミュレーターは下記のコマンドで実行できます。

```bash
open -a Simulator
```

下記のコマンドでアンドロイドエミュレーターを実行することができます。

```bash
emulator -list-avds
emulator -avd @name-of-your-emulator
```

## 完了

これでFlutterでアプリを開発する準備ができました。次はDartを勉強してFlutterのアプリを開発してみましょう。
