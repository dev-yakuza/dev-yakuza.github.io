---
layout: 'post'
permalink: '/react-native/android-running-on-device/'
paginate_path: '/react-native/:num/android-running-on-device/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'アンドロイドビルドやテスト'
description: 'RN(react native)で開発したプロジェクトをアンドロイド(Android)用でビルドしてデバイスでテストしてみましょう。'
image: '/assets/images/category/react-native/android-running-on-device.jpg'
---


## 概要
今まで開発したRN(react native)をアンドロイド(Android)用でビルドしてデバイスへ上げてテストする方法を紹介します。ここにはMac(マック)でアンドロイド(Android)署名キー(Signing Key)を生成してビルドする要諦です。このブログはRN(react native)公式サイトを参考しましたので詳しく内容は公式サイトを参考してください。

- 公式サイト: [https://facebook.github.io/react-native/docs/signed-apk-android](https://facebook.github.io/react-native/docs/signed-apk-android){:rel="nofollow noreferrer" target="_blank"}

## アンドロイド署名キー生成
Macで```ターミナル```プログラムを開いてRN(react native)プロジェクトフォルダの```android/app```フォルダへ移動します。

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

全てを入力したらRN(react native)プロジェクトフォルダ下ある```android/app```フォルダへ```my-release-key.keystore```ファイルが生成されたことが確認できます。

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
RN(react native)があるプロジェクトフォルダの```android```フォルダへ移動した後、下のコマンドでビルドします。

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