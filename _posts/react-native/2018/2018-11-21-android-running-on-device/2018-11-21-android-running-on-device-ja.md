---
layout: 'post'
permalink: '/react-native/android-running-on-device/'
paginate_path: '/react-native/:num/android-running-on-device/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'アンドロイドビルドやテスト'
description: 'リアクトネイティブ(React Native)で開発したプロジェクトをアンドロイド(Android)用でビルドしてデバイスでテストしてみましょう。'
image: '/assets/images/category/react-native/android-running-on-device.jpg'
---

<div id="contents_list" markdown="1">

## 目次

1. [概要](#概要)
1. [アンドロイド署名キー生成](#アンドロイド署名キー生成)
1. [署名キー設定](#署名キー設定)
1. [ビルド](#ビルド)
1. [ビルドされたファイルテスト](#ビルドされたファイルテスト)
1. [エラー対応](#エラー対応)

</div>

## 概要

今まで開発したリアクトネイティブ(React Native)をアンドロイド(Android)用でビルドしてデバイスへ上げてテストする方法を紹介します。ここにはMac(マック)でアンドロイド(Android)署名キー(Signing Key)を生成してビルドする要諦です。このブログはリアクトネイティブ(React Native)公式サイトを参考しましたので詳しく内容は公式サイトを参考してください。

- 公式サイト: [https://facebook.github.io/react-native/docs/signed-apk-android](https://facebook.github.io/react-native/docs/signed-apk-android){:rel="nofollow noreferrer" target="_blank"}

このブログはシリーズです。下記のブログも確認してください。

- [アンドロイドデバイステスト]({{site.url}}/{{page.categories}}/android-test-on-device/){:target="_blank"}
- [アンドロイド開発者登録]({{site.url}}/{{page.categories}}/android-enroll-google-play-developer/){:target="_blank"}
- [アンドロイドアプリストア登録]({{site.url}}/{{page.categories}}/android-google-play/){:target="_blank"}
- [Fastlaneを使ってアプリのデプロイを自動化する]({{site.url}}/{{page.categories}}/fastlane/){:target="_blank"}

## アンドロイド署名キー生成

Macで```ターミナル```プログラムを開いてリアクトネイティブ(React Native)プロジェクトフォルダの```android/app```フォルダへ移動します。

```bash
cd [your path]/android/app
```

下記のコマンドでアンドロイド(Android)用署名キー(Signing Key)を発行します。

```bash
# keytool -genkey -v -keystore my-release-key.keystore -alias my-key-alias -keyalg RSA -keysize 2048 -validity 10000

keytool -genkey -v -keystore [key-name].keystore -alias [key alias] -keyalg RSA -keysize 2048 -validity 10000

Enter keystore password:
Re-enter new password:
What is your first and last name?
  [Unknown]:
What is the name of your organizational unit?
  [Unknown]:
What is the name of your organization?
  [Unknown]:
What is the name of your City or Locality?
  [Unknown]:
What is the name of your State or Province?
  [Unknown]:
What is the two-letter country code for this unit?
  [Unknown]:
Is CN=*****, OU=Unknown, O=Unknown, L=*****, ST=*****, C=***** correct?
  [no]:

Enter key password for <my-key-alias>
    (RETURN if same as keystore password):
```

全てを入力したらリアクトネイティブ(React Native)プロジェクトフォルダ下ある```android/app```フォルダへ```my-release-key.keystore```ファイルが生成されたことが確認できます。

{% include in-feed-ads.html %}

## 署名キー設定

署名キー(Signing Key)が生成されたら```gradle```へキーを設定する必要があります。```android/gradle.properties```ファイルを開いて下記のコードを追加します。

```xml
MYAPP_RELEASE_STORE_FILE=my-release-key.keystore
MYAPP_RELEASE_KEY_ALIAS=my-key-alias
MYAPP_RELEASE_STORE_PASSWORD=*****
MYAPP_RELEASE_KEY_PASSWORD=*****
```

下のコードを```android/app/build.gradle```ファイルへ追加します。

```xml
...
android {
    ...
    defaultConfig { ... }
    signingConfigs {
        release {
            if (project.hasProperty('MYAPP_RELEASE_STORE_FILE')) {
                storeFile file(MYAPP_RELEASE_STORE_FILE)
                storePassword MYAPP_RELEASE_STORE_PASSWORD
                keyAlias MYAPP_RELEASE_KEY_ALIAS
                keyPassword MYAPP_RELEASE_KEY_PASSWORD
            }
        }
    }
    buildTypes {
        release {
            ...
            signingConfig signingConfigs.release
        }
    }
}
...
```

## ビルド

リアクトネイティブ(React Native)があるプロジェクトフォルダの```android```フォルダへ移動した後、下のコマンドでビルドします。

```bash
./gradlew assembleRelease
```

ビルドされたファイルは下記のパスが生成されます

```bash
android/app/build/outputs/apk/release/app-release.apk
```

私たちはこの部分で下記のようなエラーが発生しました。

```bash
...
Execution failed for task ':app:lintVitalRelease'.
> Lint found fatal errors while assembling a release target.
...
```

いい方法ではないですが、私たちは```android/app/build.gradle```ファイルへ下の内容を追加したこの部分を解決しました。

```xml
...
android {
  ...
  lintOptions {
      checkReleaseBuilds false
      // Or, if you prefer, you can continue to check for errors in release builds,
      // but continue the build even when errors are found:
      abortOnError false
  }
  ...
}
...
```

{% include in-feed-ads.html %}

## ビルドされたファイルテスト

アンドロイドデバイス(Android Device)でインストールされた既存のアプリを削除して下記のコマンドでビルドファイルのテストを進んでください。

```bash
react-native run-android --variant=release
```

## エラー対応

公式サイトの内容を見て上記のように進めましたが私たちは実際下のコマンドでビルドする時と

```bash
./gradlew assembleRelease
```

下のコマンドで直接デバイスでテストする時、

```bash
react-native run-android --variant=release
```

下記のようなエラーが発生しました。

```bash
java.lang.RuntimeException: Unable to load script from assets 'index.android.bundle'. Make sure your bundle is packaged correctly or you're running a packager server.
```

解決する方法で下のコマンドを先実行して```index.android.bundle```を生成した後

```bash
react-native bundle --platform android --dev false --entry-file index.js --bundle-output android/app/src/main/assets/index.android.bundle
```

ビルドをしたり

```bash
# cd android
./gradlew assembleRelease
```

直接デバイスでテストしたりしました。

```bash
react-native run-android --variant=release
```
