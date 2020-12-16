---
layout: 'post'
permalink: '/react-native/react-native-firebase-v6-installation/'
paginate_path: '/react-native/:num/react-native-firebase-v6-installation/'
lang: 'ja'
categories: 'react-native'
comments: true

title: react-native-firebase V6インストール
description: React NativeでFirebaseを使うため、react-native-firebase(V6)をインストールする方法について説明します。
image: '/assets/images/category/react-native/2020/react-native-firebase-v6-installation/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [ライブラリインストール](#ライブラリインストール)
- [Firebaseプロジェクト生成](#firebaseプロジェクト生成)
- [iOS設定](#ios設定)
  - [Bundle ID変更](#bundle-id変更)
  - [Firbase iOSプロジェクト設定](#firbase-iosプロジェクト設定)
- [アンドロイド設定](#アンドロイド設定)
  - [アンドロイドパッケージ名修正](#アンドロイドパッケージ名修正)
  - [Firbaseアンドロイドプロジェクト設定](#firbaseアンドロイドプロジェクト設定)
- [完了](#完了)

</div>

## 概要

React Nativeプロジェクトで[Firebase](https://firebase.google.com/){:rel="nofollow noreferrer" target="_blank"}を使うため`react-native-firebase`をインストールする方法について説明します。

- react-native-firebase(V6): [https://rnfirebase.io/](https://rnfirebase.io/){:rel="nofollow noreferrer" target="_blank"}

react-native-firebaseの以前のバージョン(V5)を使う方法については下記のブログリストを参考してください。

- [Firebase Analytics]({{site.url}}/{{page.categories}}/react-native-firebase-analytics/){:target="_blank"}
- [Firebase Crashlytics]({{site.url}}/{{page.categories}}/firebase-crashlytics/){:target="_blank"}
- [Firebase Admob]({{site.url}}/{{page.categories}}/react-native-firebase-admob/){:target="_blank"}
- [react-native-firebase(V5)を使ってPush Message]({{site.url}}/{{page.categories}}/react-native-firebase-fcm/){:target="_blank"}

このブログポストはシリーズで作成されております。他の内容を確認したい方は下記のブログリストを参考してください。

- react-native-firebase V6 インストール
- [react-native-firebase V6 Crashlytics]({{site.url}}/{{page.categories}}/react-native-firebase-v6-crashlytics/){:target="_blank"}
- [react-native-firebase V6 Admob]({{site.url}}/{{page.categories}}/react-native-firebase-v6-admob/){:target="_blank"}

## ライブラリインストール

下記のコマンドを使って`react-native-firebase`をインストールします。

```bash
npm install --save @react-native-firebase/app
```

下記のコマンドを使ってiOSプロジェクトへreact-native-firebaseを連結します。

```bash
cd ios
pod install
```

{% include in-feed-ads.html %}

## Firebaseプロジェクト生成

次はグーグルファイアベース(Google Firebase)でプロジェクトを生成する必要があります。下記のリンクを押してグーグルファイアベース(Google Firebase)へ移動します。

- グーグルファイアベース(Google Firebase): [https://firebase.google.com](https://firebase.google.com){:rel="nofollow noreferrer" target="_blank"}

![google firebase](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/google-firebase.jpg)

右上の`SIGN IN`ボタンを押してログインします。

![google firebase after login](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/google-firebase-after-login.jpg)

ログインしたら、右上の`GO TO CONSOLE`ボタンを押してグーグルファイアベースコンソール(Google Firebase Console)へ移動します。

![google firebase console](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/google-firebase-console.jpg)

グーグルファイアベースコンソール(Google Firebase Console)で`+ Add project`を押してプロジェクトを追加します。

![google firebase console add project](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/google-firebase-console-add-project.jpg)

上のような画面で`Enter your project name`へ作りたいFirebaseプロジェクトの名前を入力します。入力が終わったら、下記にある`Continue`ボタンを押して次へ進めます。

![google firebase console add google analytics](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/google-firebase-console-add-google-analytics.jpg)

プロジェクト名を入力したら、上のように`Google Analytics`を連動する画面が表示されます。Google Analyticsと連動したくない場合、左下にあるボタンを押して`Disable`で変更してFirebaseプロジェクトを生成します。

Google Analyticsと連動したい方は`Continue`を押して進めます。

![google firebase console add integrate google analytics](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/google-firebase-console-integrate-google-analytics.jpg)

Google Analyticsのアカウントを選択して、`Create project`ボタンを押してFirebaseプロジェクトを生成します。

{% include in-feed-ads.html %}

## iOS設定

react-native-firebaseを使うためiOSを設定する方法について説明します。

### Bundle ID変更

FirebaseへiOSプロジェクトを生成する前にiOSの`Bundle ID`を変更する必要があります。`ios/[project name].xcworkspace`を選択してXcodeを実行します。

![change ios bundle id](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/ios-change-bundle-id.jpg)

左上のプロジェクト名を選択して`General`タブへ移動したら、上に`Bundle Identifier`があることが確認できます。このBundle IDを自分のプロジェクトへ合わせて変更します。

### Firbase iOSプロジェクト設定

グーグルファイアベースコンソール(Google Firebase Console)でプロジェクトを選択したら下記のような画面が見えます。

![google firebase console project](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/google-firebase-console-project.jpg)

真ん中へ`iOS`ボタンを押してiOSの設定画面へ移動します。

![google firebase console project ios](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/google-firebase-console-project-ios.jpg)

開発したアプリのID(bundle ID)を入力して`Register app`ボタンを選択します。

![GoogleService-Info.plist download](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/googleservice-info-plist-download.jpg)

グーグルファイアベース(Google Firebase)が生成した`GoogleService-Info.plist`ファイルをダウンロードして`info.plist`同じ位置へ追加します。`GoogleService-Info.plist`ファイルを追加したら、`Next`ボタンを押します。

![add Firebase SDK](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/add-firebase-sdk-google-analytics.jpg)

画面へ表示された方法でグーグルファイアベースSDK(Google Firebase SDK)をReact Nativeプロジェクトへ追加する必要があります。`./ios/Podfile`ファイルを開いて下記のように修正します。

```ruby
target 'blaboo' do
  ...
  pod 'Firebase/Analytics'
  ...
end
```

Google Analyticsを使ってない方は上のようにコードを修正する必要がないです。

下記のコマンドでグーグルファイアベースSDK(Google Firebase SDK)をインストールします。

```bash
pod install
# pod update
```

![edit appdelegate.m for firebase](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/edit-appdelegate.jpg)

React Nativeプロジェクトの`AppDelegate.m`ファイルへ下記のようにコードを追加します。

```js
...
@import Firebase;

@implementation AppDelegate
...
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
  [FIRApp configure];
  ...
  return YES;
}
...
```

グーグルファイアベースSDK(Google Firebase SDK)を初期化します。

![connect firebase to app](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/connect-firebase-to-app.jpg)

私はこの部分で`Skip this step`を押してスキップしました。

{% include in-feed-ads.html %}

## アンドロイド設定

次は、react-native-firebaseを使うためアンドロイドを設定する方法について説明します。

### アンドロイドパッケージ名修正

- React Nativeプロジェクトフォルダへ`android/app/BUCK`ファイルを修正

  ```xml
  ...
  android_build_config(
      ...
      package = "package_name",
  )
  ...
  android_resource(
      ...
      package = "package_name",
      ...
  )
  ...
  ```

- React Nativeプロジェクトフォルダで`android/app/src/main/AndroidManifest.xml`ファイル修正

  ```xml
  <manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="package_name">
  ...
  ```

- React Nativeプロジェクトフォルダで`android/app/src/main/java/com/ProjectName/MainActivity.java`ファイル修正

  ```java
  package package_name;
  ...
  ```

- React Nativeプロジェクトフォルダで`android/app/src/main/java/com/ProjectName/MainApplication.java`ファイル修正

  ```java
  package package_name;
  ...
  ```

- React Nativeプロジェクトフォルダで`android/app/build.gradle`ファイル修正

  ```java
  ...
  defaultConfig {
      applicationId package_name
      ...
  }
  ...
  ```

このようにパッケージ名を変更したら、`android/app/src/main/java/com/[App Name]/MainActivity.java`でできてるフォルダ構造を`android/app/src/main/java/[Package Name Folder]/MainActivity.java`ように変更する必要があります。

{% include in-feed-ads.html %}

### Firbaseアンドロイドプロジェクト設定

グーグルファイアベースコンソール(Google Firebase Console)で左上の`Project Overview`を選択します。

![Google Firebase Console Project Overview](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/firebase-project-overview.jpg)

上にある`+ Add app` > `アンドロイド(Android)アイコン`を押してアンドロイド(Android)プロジェクトの設定へ移動します。

![Google Firebase Android app register](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/register-android.jpg)

アンドロイドパッケージ名(Android Package Name)を入力して`Register app`を選択します。

![Google Firebase google-services.json setting](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/set-google-services-json.jpg)

グーグルファイアベース(Google Firebase)が作った`google-services.json`ファイルをReact Nativeプロジェクトの`android/app`フォルダへコピーします。そして`Next`ボタンを押して次へ進めます。

![Google Firebase setting on android](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/setting-android.jpg)

React Nativeプロジェクトがあるフォルダへ`android/build.gradle`ファイルを開いて下記のように修正します。

```js
buildscript {
  repositories {
    google()
    jcenter()
  }
  dependencies {
    classpath("com.android.tools.build:gradle:3.5.2")
    classpath 'com.google.gms:google-services:4.3.3'
  }
}
...
allprojects {
  repositories {
    mavenLocal()
    google()
    jcenter()
    ...
  }
}
```

上のように`repositories`へ`google()`が含めてあるか、`jcenter()`より上に宣言されたか確認します。

React Nativeプロジェクトがあるフォルダで`android/app/build.gradle`ファイルを開いて下記のようにコードを追加します。

```js
dependencies {
    // under 59 version
    // implementation project(':react-native-firebase')
    ...
    implementation 'com.google.firebase:firebase-analytics:17.2.2'
}
```

Google Analyticsを使ってない場合は上の内容は追加しなくて大丈夫です。そして、同じファイルを一番したへ下記のコードを追加します。

```js
...
apply plugin: 'com.google.gms.google-services'
```

次は`./android/build.gradle`ファイルを開いて下記のように修正します。

```js
buildscript {
    ext {
        ...
    }
    repositories {
        ...
    }
    dependencies {
        classpath("com.android.tools.build:gradle:3.4.2")
        classpath 'com.google.gms:google-services:4.3.3'
    }
}
```

## 完了

これでReact NativeでFirebaseを使うため`react-native-firebae`をインストールする方法について説明しました。他の機能を追加する方法については下記のリンクを参考してください。

- [react-native-firebase V6 Crashlytics]({{site.url}}/{{page.categories}}/react-native-firebase-v6-crashlytics/){:target="_blank"}
- [react-native-firebase V6 Admob]({{site.url}}/{{page.categories}}/react-native-firebase-v6-admob/){:target="_blank"}