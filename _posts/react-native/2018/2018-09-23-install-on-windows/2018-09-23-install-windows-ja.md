---
layout: 'post'
permalink: '/react-native/install-on-windows/'
paginate_path: '/react-native/:num/install-on-windows/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'ウィンドウ(Windows)にreact nativeの開発環境を構築する方法'
description: 'react-nativeでアプリを開発するためウィンドウ(Windows)に開発環境を構築して見て、react-nativeのプロジェクトがうまく起動できるか確認して見ます。'
image: '/assets/images/category/react-native/2018/install-on-windows/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

1. [概要](#概要)
1. [Chocolateyインストール](#chocolateyインストール)
1. [Nodejsインストール](#nodejsインストール)
1. [Pythonインストール](#pythonインストール)
1. [React Native CLIインストール](#react-native-cliインストール)
1. [JDKインストール](#jdkインストール)
1. [アンドロイドスタジオインストール](#アンドロイドスタジオインストール)
    - [アンドロイドスタジオ設定](#アンドロイドスタジオ設定)
    - [アンドロイドスタジオSDK設定](#アンドロイドスタジオsdk設定)
    - [アンドロイドスタジオ環境変数設定](#アンドロイドスタジオ環境変数設定)
1. [react-nativeプロジェクト生成や確認](#react-nativeプロジェクト生成や確認)
    - [アンドロイドで確認](#アンドロイドで確認)
1. [完了](#完了)

</div>

## 概要

react-nativeでアプリを開発するため、ウィンドウ(Windows)に開発環境を設定する方法について説明します。ウマック(Mac)に開発環境を設定する方法については下記のブログを参考してください。

- [マック(mac)にreact nativeの開発環境を構築する方法]({{site.url}}/react-native/install-on-mac/){:target="_blank"}

ウィンドウ(Windows)でreact-nativeアプリを開発する方法は`Expo CLI`と`React Native CLI`があります。

Expo CLIはreact-nativeでアプリを開発する時よく使うネイティブ機能(位置情報、カメラなど)をパッケージで提供してます。初めてreact-nativeで開発する時は楽かもしれないですが、使ってないネイティブ機能のモジュールのせいでファイルサイズが大きくなる問題とExpoが提供してないネイティブ機能を入れる時不便さなのがあって、このブログではExpoを使うことはお勧めしません。

このブログポストではReact Native CLIを使ってアプリを開発するため開発環境を設定する方法を説明します。また、インストールしたReact Native CLIを使ってプロジェクトを生成して見て、うまく起動するかも確認して見ます。

react-nativeでアプリを開発するためにはnodejs, Watchman, Xcodeなどをインストールする必要があります。各段階を一つ一つ詳しく見て見ます。

## Chocolateyインストール

Chocolateyはウィンドウ(Windows)に必要なパッケージをインストールや管理をする時使うパッケージ管理者です。Chocolateyを使うとウィンドウ(Windows)に簡単に必要なパッケージをインストールすることが出来ます。

- Chocolatey: [https://chocolatey.org/](https://chocolatey.org/){:rel="nofollow noreferrer" target="_blank"}

Chocolateyをインストールするため、コマンドプロンプト(cmd)を管理者権限で実行して、下記のコマンドを実行します。

```bash
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
```

インストールが終わったら、コマンドプロンプト(cmd)を再起動して、下記のコマンドを実行してインストールがうまく出来たか確認します。

```bash
choco –version
```

インストールがうまく出来たら、下記のようにChocolateyのバージョンの確認が出来ます。

```bash
0.10.15
```

{% include in-feed-ads.html %}

## Nodejsインストール

react-nativeはJavascriptなのでJavascriptのRuntimeであるNodejsが必要です。

- Nodejs: [https://nodejs.org/](https://nodejs.org/){:rel="nofollow noreferrer" target="_blank"}

コマンドプロンプト(cmd)を管理者権限で実行して、下記のChocolateyのコマンドを使ってNodejsをインストールします。

```bash
choco install -y nodejs.install
```

インストールが終わったら、コマンドプロンプト(cmd)を再起動して、下記のコマンドでNodejsが正しくインストールされたか確認します。

```bash
node -–version
```

Nodejsが正しくインストールされたら、下記のようにNodejsのバージョンが確認出来ます。

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

## Pythonインストール

React NativeのビルドシステムはPythonを使ってます。マック(Mac)は基本的Pythonがインストールされてるので、Pythonをインストールする必要がないですが、ウィンドウ(Windows)はPythonをインストールする必要があります。

コマンドプロンプト(cmd)を管理者権限で実行して、下記のChocolateyコマンドを実行してPythonをインストールします。

```bash
choco install -y python2
```

インストールが終わったら、Pythonを使うためにはパソコンを再起動する必要があります。パソコンを再起動したら、コマンドプロンプト(cmd)で下記のコマンドを実行してPythonが問題なくインストールされたか確認します。

```bash
python --version
```

Pythonがうまくインストールされたら、下記のようにPythonのバージョンが確認出来ます。

```bash
2.7.16
```

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

{% include in-feed-ads.html %}

## JDKインストール

react-nativeでアンドロイドアプリを開発するためにはJDK(Java Development Kit)をインストールする必要があります。コマンドプロンプト(cmd)を管理者権限で実行して、下記のChocolateyコマンドを実行してJDKをインストールします。

```bash
choco install -y jdk8
```

インストールが終わったら、コマンドプロンプト(cmd)を再起動して、下記のコマンドでJavaがインストールされたか確認します。

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

ダウンロードが終わったら、インストールファイルを実行してアンドロイドスタジオのインストールを進めます。

### アンドロイドスタジオ設定

アンドロイドスタジオを実行したら下記のような画面が確認できます。

![react-native開発環境設定 - アンドロイドスタジオインストール](/assets/images/category/react-native/2018/install-on-windows/install_android_studio.jpg)

Nextボタンを押して次の画面に移動します。次の画面に移動したら下記のようにChoose Components画面が表示します。Android Virtual Deviceを選択してNextボタンを押して次の画面に移動します。

![react-native開発環境設定 - アンドロイドスタジオコンポーネント設定](/assets/images/category/react-native/2018/install-on-windows/android_studio_choose_components.jpg)

次の画面に移動したら、下記のようにアンドロイドスタジオのインストールパスを設定する画面が出ます。日本語のフォルダ名が入らないように注意してインストールパスを設定します。インストールパスに特に問題ない時はNextボタンを押して次の画面に移動します。

![react-native開発環境設定 - アンドロイドスタジオインストールパス設定](/assets/images/category/react-native/2018/install-on-windows/android_studio_install_path.jpg)

次の画面に移動したら、下記のようにスタートメニューを設定する画面が出ます。特に修正することなく、Installボタンを押してインストールを進めます。

![react-native開発環境設定 - アンドロイドスタジオスタートメニュー設定](/assets/images/category/react-native/2018/install-on-windows/android_studio_start_menu_configuration.jpg)

インストールが終わったら、下記のような画面が見えます。Nextボタンを押してインストールを完了します。

![react-native開発環境設定 - アンドロイドスタジオインストール完了](/assets/images/category/react-native/2018/install-on-windows/android_studio_install_completed.jpg)

Nextボタンを押してインストールを完了させたら、下記のような画面が出ます。Start Android Studioがチェックされた状態でFinishボタンを押してアンドロイドスタジオのインストールを完了します。

![react-native開発環境設定 - アンドロイドスタジオインストールや設定完了](/assets/images/category/react-native/2018/install-on-windows/android_studio_install_configure_completed.jpg)

Finishボタンを押してアンドロイドスタジオのインストールを完了したら、下記のようにアンドロイドスタジオが実行されます。Do not import settingsを選択して、OKボタンを押してアンドロイドスタジオを実行します。

![react-native開発環境設定 - アンドロイドスタジオ実行](/assets/images/category/react-native/2018/install-on-windows/android_studio_start.jpg)

OKボタンを押してアンドロイドスタジオを実行したら、下記のようにアンドロイドスタジオ設定ウィザードの画面が出ます。Nextボタンを押して次の画面に移動します。

![react-native開発環境設定 - アンドロイドスタジオ設定ウィザード](/assets/images/category/react-native/2018/install-on-windows/android_studio_setup_wizard.jpg)

次の画面に移動したら下記のようにInstall Typeを設定する画面が出ます。Customを洗濯してNextボタンを押して次の画面に移動します。

![react-native開発環境設定 - アンドロイドスタジオInstall Type設定](/assets/images/category/react-native/2018/install-on-windows/configure_android_studio_install_type.jpg)

次の画面に移動したら、下記のようにSelect UI Theme画面が出ます。自分が好きなテーマを選択してNextボタンを押して次に進めます。

![react-native開発環境設定 - アンドロイドスタジオテーマ設定](/assets/images/category/react-native/2018/install-on-windows/configure_android_studio_select_ui_theme.jpg)

次の画面に移動したら、下記のようにSDK Components Setup画面が出ます。`Performance (Intel ® HAXM)`と`Android Virtual Device`を選択してNextボタンを押してインストールを進めます。

![react-native開発環境設定 - アンドロイドスタジオsdk設定](/assets/images/category/react-native/2018/install-on-windows/configure_android_studio_sdk_components_setup.jpg)

次に移動したら下記のようにEmulator Settings画面が出ます。特に修正することなく、Nextボタンを押して次の画面に移動します。

![react-native開発環境設定 - アンドロイドスタジオエミュレーター設定](/assets/images/category/react-native/2018/install-on-windows/configure_android_studio_emulator_settings.jpg)

次の画面からは一般的なプログラムをインストールする方法と同じなので説明を省略します。Finishボタンを押して進めるとアンドロイドスタジオの設定が終わります。

アンドロイドスタジオのインストールが終わったら下記のようにアンドロイドスタジオが実行されることが確認できます。

![react-native開発環境設定 - アンドロイドスタジオ実行](/assets/images/category/react-native/2018/install-on-windows/android_studio.jpg)

{% include in-feed-ads.html %}

### アンドロイドスタジオSDK設定

右下の`Configure > SDK Manger`を選択してアンドロイドSDK設定画面に移動します。

![react-native開発環境設定 - アンドロイドスタジオSDK設定](/assets/images/category/react-native/2018/install-on-windows/android_studio_configure_sdk.jpg)

上のような画面が見えたら、右下の`Show Pacakge Details`を選択します。そしてリストで下記の内容を探して選択します。

- Android SDK Platform 29
- Intel x86 Atom System Image
- Google APIs Intel x86 Atom System Image
- Google APIs Intel x86 Atom_64 System Image

全て選択したら右下のOKボタンを押して選択した内容をインストールします。

### アンドロイドスタジオ環境変数設定

これでアンドロイドスタジオのインストールや設定は終わりました。次はアンドロイドスタジオを環境変数に登録します。マイコンピュータ＞右クリック＞プロパティメニューを選択してプロパティメニューを移動します。

プロパティメニューを選択すると、下記のようにシステム設定画面が表示されます。左にあるシステムの詳細設定メニューを押します。

![react-native開発環境設定 - アンドロイドスタジオ環境変数設定：システム設定](/assets/images/category/react-native/2018/install-on-windows/android_studio_configure_environment_variable_system_setting_ja.jpg)

システムの詳細設定メニューを押すと、下記のようにシステムのプロパティ画面が確認出来ます。上部にある詳細設定を押して、詳細設定タブの下にある環境変数ボタンを押します。

![react-native開発環境設定 - アンドロイドスタジオ環境変数設定：システムの詳細設定ダイアログ](/assets/images/category/react-native/2018/install-on-windows/android_studio_configure_environment_variable_system_setting_dialog_ja.jpg)

環境変数ボタンを選択したら下記のように環境変数を設定する画面が確認出来ます。上部にあるユーザー環境変数の新規ボタンを押します。

![react-native開発環境設定 - アンドロイドスタジオ環境変数設定：環境変数新規登録](/assets/images/category/react-native/2018/install-on-windows/android_studio_configure_environment_variable_add_new_ja.jpg)

上のように新し環境追加画面が出たら変数名には`ANDROID_HOME`を入力して、変数値には自分のアンドロイドスタジオのSDKのパスを入力します。自分のアンドロイドスタジオのSDKのパスが分からない場合、下記のようにアンドロイドスタジオSDK設定画面に移動します。アンドロイドスタジオSDK設定画面の一番上にあるAndroid SDK Locationの項目で自分のアンドロイドSDKのパスを確認することが出来ます。

![react-native開発環境設定 - アンドロイドスタジオSDK設定](/assets/images/category/react-native/2018/install-on-windows/android_studio_configure_sdk.jpg)

ANDROID_HOME環境変数を追加したら、アンドロイドスタジオのplatform-toolsを設定する必要があります。ユーザー環境変数リストで`Path`を選択して環境変数を編集する画面に移動します。

![react-native開発環境設定 - アンドロイドスタジオ環境変数設定：platform-tools追加](/assets/images/category/react-native/2018/install-on-windows/android_studio_configure_environment_variable_edit_path_ja.jpg)

上のように編集画面が見えたら、リストの一番下に`C:\Users\[ユーザー名]\AppData\Local\Android\Sdk\platform-tools`見たいにSDKがインストールされたフォルダ下にあるplatform-toolsフォルダを入力して確認ボタンを押して環境変数を編集します。

このように全ての修正が終わったら、コマンドプロンプト(cmd)を実行して下記のコマンドを実行します。

```bash
adb
```

環境変数設定がうまく出来たら、下記のような結果を見ることが出来ます。

```bash
Android Debug Bridge version 1.0.41
Version 29.0.1-5644136
Installed as /Users/jeonghean_kim/Library/Android/sdk/platform-tools/adb
```

{% include in-feed-ads.html %}

## react-nativeプロジェクト生成や確認

次は下記のReact Native CLIコマンドでreact-nativeプロジェクトを生成します。

```bash
npx react-native init SampleApp SampleApp
```

### アンドロイドで確認

アンドロイドの場合、開発モードがアクティブされたデバイスをUSBで繋げた状態または、アンドロイドスタジオを実行してエミュレータを実行した状態で下記のコマンドを実行します。

```bash
cd SampleApp
# react-native run-android
npm run android
```

問題なく実行されたら、下記のような画面が確認出来ます。

![react-nativeの開発環境設定 - アンドロイドで実行](/assets/images/category/react-native/2018/install-on-windows/react_native_on_android.jpg)

## 完了

これでウィンドウ(Windows)でreact-nativeでアプリを開発するため開発環境を設定する方法を見て見ました。また、開発環境の設定がうまく出来たか確認するため、React Native CLIを使ってアプリを生成して実行して見ました。

react-nativeでアプリを開発する準備が終わりました。react-nativeでアプリを開発する世界にどっぷり浸かってみましょう！
