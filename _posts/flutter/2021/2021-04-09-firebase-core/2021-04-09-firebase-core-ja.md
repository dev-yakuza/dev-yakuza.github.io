---
layout: 'post'
permalink: '/flutter/firebase/core/'
paginate_path: '/flutter/:num/firebase/core/'
lang: 'ja'
categories: 'flutter'
comments: true

title: '[Flutter] Firebase core'
description: 今回ブログポストではFlutterでFirebaseを連動する方法について説明します。
image: '/assets/images/category/flutter/background.png'
published: false
---

<div id="contents_list" markdown="1">

## 目次

</div>

## 概要

今回のブログポストではFlutterで`firebase_core`を使って`Firebase`を連動するつ方法について説明します。

- [firebase_core](https://pub.dev/packages/firebase_core){:rel="nofollow noreferrer" target="_blank" }

## ブログシリーズ

このブログはシリーズで作成されております。次のリンクを使って他のブログポストは下記のリンクで確認できます。

- [Flutter] Firebase Core
- [[Flutter] Firebase Analytics]({{site.url}}/{{page.categories}}/firebase/analytics/){:target="_blank"}
- [[Flutter] Firebase Crashlytics]({{site.url}}/{{page.categories}}/firebase/crashlytics/){:target="_blank"}

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

`firebase_core`を使ってFlutterでFirebaseを使うためiOSを設定する方法について説明します。

### Bundle identifier変更

FirebaseでiOSプロジェクトを生成する前、iOSの`Bundle identifier`を変更する必要があります。`ios/Runner.xcworkspace`ファイルを実行してXcodeを実行します。

![change ios bundle id](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/ios-change-bundle-id.jpg)

左上のプロジェクト名を選択して`General`タブに移動すると、上にある`Bundle Identifier`を確認することができます。このBundle IDを自分のプロジェクトに合わせて変更します。

### Firbase iOSプロジェクト設定

グーグルファイアベースコンソール(Google Firebase Console)でプロジェクトを選択すると次のような画面が見えます。

![google firebase console project](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/google-firebase-console-project.jpg)

真ん中へ`iOS`ボタンを押してiOSの設定画面へ移動します。

![google firebase console project ios](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/google-firebase-console-project-ios.jpg)

開発したアプリのID(bundle ID)を入力して`Register app`ボタンを選択します。

![GoogleService-Info.plist download](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/googleservice-info-plist-download.jpg)

グーグルファイアベース(Google Firebase)が生成した`GoogleService-Info.plist`ファイルをダウンロードしてXcodeを使って`Runner/Runner`フォルダへドラッグして当該ファイルを追加します。`GoogleService-Info.plist`ファイルを追加したら、`Next`ボタンを押します。

![add Firebase SDK](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/add-firebase-sdk-google-analytics.jpg)

이 화면이 표시되면, `Next` 버튼을 클릭하여 다음 화면으로 이동합니다.

![edit appdelegate.m for firebase](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/edit-appdelegate.jpg)

上のような画面でも`Next`ボタンをクリックして次の画面へ移動します。

![connect firebase to app](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/connect-firebase-to-app.jpg)

私はこの部分で`Skip this step`を押してスキップしました。

{% include in-feed-ads.html %}

## アンドロイド設定

`firebase_core`を使ってFlutterでFirebaseを使うためアンドロイドを設定する方法について説明します。

### Gradle修正

FlutterでFirebaseを使うためには`Gradle`ファイルを修正する必要があります。まず、`android/app/build.gradle`ファイルを開いてファイルの下へ下記のような内容を追加します。

```js
...
apply plugin: 'com.google.gms.google-services' // <<<<<<<<<<<<< Add this
```

そして`applicationId`を当該プロジェクトに合わせて修正します。

```js
// applicationId "com.example.blaboo_app"
applicationId "io.github.dev.yakuza.blaboo"
```

その後、`android/build.gradle`ファイルを開いて下記のように修正します。

```js
buildscript {
    ...
    dependencies {
        ...
        classpath "org.jetbrains.kotlin:kotlin-gradle-plugin:$kotlin_version"
        classpath 'com.google.gms:google-services:4.3.5' // <<<<<<<<<<<<<<<< Add this
    }
}
```

これでアンドロイドでFirebaseを使う準備ができました。

### Firbaseのアンドロイドプロジェクト設定

グーグルファイアベースコンソール(Google Firebase Console)で左上の`Project Overview`を選択します。

![Google Firebase Console Project Overview](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/firebase-project-overview.jpg)

상단에 `+ Add app` > `안드로이드(Android) 아이콘`을 눌러 안드로이드(Android) 프로젝트 설정으로 이동합니다.

![Google Firebase Android app register](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/register-android.jpg)

上にある`+ Add app` > `アンドロイド(Android)アイコン`を押してアンドロイド(Android)プロジェクトの設定へ移動します。

![Google Firebase google-services.json setting](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/set-google-services-json.jpg)

グーグルファイアベース(Google Firebase)が作った`google-services.json`ファイルをFlutterプロジェクトの`android/app`フォルダへコピーします。そして`Next`ボタンを押して次へ進めます。

![Google Firebase setting on android](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/setting-android.jpg)

{% include in-feed-ads.html %}

## firebase_coreインストール

FlutterでFirebaseを使うためには、`firebase_core`パッケージをインストールする必要があります。次のコマンドを実行して`firebase_core`をインストールします。

```bash
flutter pub pub add firebase_core
```

## Firebase初期化

このように`firebase_core`パッケージをインストールしたら、次は当該パッケージを使ってFirebaseを初期化する必要があります。`main.dart`ファイルを開いて下記のように修正してFirebaseを初期化します。

```dart
import 'package:firebase_core/firebase_core.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();

  runApp(MyApp());
}
```

## 完了

これでFlutterでFirebaseを使うためFlutterプロジェクトとFirebaseプロジェクトを準備して、`firebase_core`を設定する方法についてみてみました。次はFirebaseの他の機能を使うため、他のブログポストも確認してみてください。

- [[Flutter] Firebase Analytics]({{site.url}}/{{page.categories}}/firebase/analytics/){:target="_blank"}
- [[Flutter] Firebase Crashlytics]({{site.url}}/{{page.categories}}/firebase/crashlytics/){:target="_blank"}
