---
layout: 'post'
permalink: '/react-native/android-google-play/'
paginate_path: '/react-native/:num/android-google-play/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'アンドロイドアプリストア登録'
description: 'RN(React Native)で開発したアンドロイドアプリ(Android App)をアンドロイドアプリストア(Google Play)に登録して見ましょう。'
image: '/assets/images/category/react-native/android-google-play.jpg'
---


## 概要
RN(React Native)で開発したアンドロイドアプリ(Android App)をアンドロイドアプリストア(Google Play)に登録してみようかと思います。アンドロイドアプリ(Android App)をアンドロイドアプリストア(Google Play)に登録するためにはアンドロイド開発者登録(グーグルプレイ開発者登録)が必要です。アンドロイド開発者登録(グーグルプレイ開発者登録)をしてない方は以前のブログを参考して登録してください。

- [アンドロイド開発者登録]({{site.url}}/{{page.categories}}/android-enroll-google-play-developer/){:target="_blank"}

## 準備
RN(React Native)で開発したアンドロイドアプリ(Android App)をアンドロイドアプリストア(Google Play)に灯篭するためRN(React Native)をアンドロイド用にビルドする必要があります。RN(React Native)にアンドロイド署名キー(Android Signing Key)を登録してアンドロイド用にビルドする方法については以前のブログを参考してください。

- [アンドロイドビルドやテスト]({{site.url}}/{{page.categories}}/android-running-on-device/){:target="_blank"}

## ビルドファイルサイズ最適化
以前のブログである[アンドロイドビルドやテスト]({{site.url}}/{{page.categories}}/android-running-on-device/){:target="_blank"}でアンドロイド用にビルドされたファイルはファイルサイズの最適化がされてないです。RN(React Native)で開発したアンドロイドアプリ(Android App)をアンドロイドアプリストア(Google Play)にアップロードするためにはビルドファイルサイズを最適化する必要があります。

RN(React Native)プロジェクトフォルダで```android/app/build.gradle```を開いて下記のように修正します。

```
...
defaultConfig {
    ...
    // ndk {
    //     abiFilters "armeabi-v7a", "x86"
    // }
}
...
def enableSeparateBuildPerCPUArchitecture = true
```

そして下記のコマンドを使ってRN(React Native)をアンドロイド用にビルドします。

```bash
# react-native bundle --platform android --dev false --entry-file index.js --bundle-output android/app/src/main/assets/index.android.bundle
# cd android
./gradlew assembleRelease
```

ビルドされたファイルは下記の位置で確認できます。

```bash
android/app/build/outputs/apk/release/app-armeabi-v7a-release.apk
android/app/build/outputs/apk/release/app-x86-release.apk
```

## アプリ登録
下記のリンクを押してグーグルプレイコンソル(Google Play Console)に移動します。

- グーグルプレイコンソル(Google Play Console): [https://play.google.com/apps/publish/](https://play.google.com/apps/publish/){:rel="nofollow noreferrer" target="_blank"}

グーグルプレイコンソル(Google Play Console)に移動したら下記の画面が見えます。

![グーグルプレイコンソルホーム](/assets/images/category/react-native/android-google-play/google-play-console-home.png)

画面の上にある```PUBLISH AN ANDROID APP ON GOOGLE PLAY```ボタンを押します。

![グーグルプレイコンソルアプリタイトル](/assets/images/category/react-native/android-google-play/app-title.png)

アンドロイドアプリストア(Google Play)に表示される名前と基本言語を選択します。

![グーグルプレイコンソルアプリ情報](/assets/images/category/react-native/android-google-play/app-info.png)

アンドロイドアプリストア(Google Play)に表示される情報を入力します。

- タイトル(title): 50文字
- 要約説明(short description): 80文字
- 全体説明(full description): 4000文字
- アプリイメージ(Screenshots)
- アプリアイコン(App icon): 512x512(32-bit PNG, alpha), 1024x500(JPG or 24-bit PNG), 180x120(JPG or 24-bit PNG), 1280x720(JPG or 24-bit PNG), 4096x4096(JPG or 24-bit PNG)
- プロモーションビデオ(Promo Video)
- アプリカテゴリ(Category)
- 開発者連絡先(Contact details)
- 個人情報ポリシー(Privacy Policy)

全ての情報を入力したらapkファイルを登録する方法について説明します。

左上にある```App release```メニューを押したら下記の画面が見えます。

![グーグルプレイアプリ登録](/assets/images/category/react-native/android-google-play/app-register.png)

画面に見える```Production track```の```Production```項目の```MANAGE```を押します。

![グーグルプレイアプリproduction生成](/assets/images/category/react-native/android-google-play/app-production.png)

上のような画面が見えたら下の```CREATE RELEASE```を押します。

![グーグルプレイアプリ署名キー登録](/assets/images/category/react-native/android-google-play/register-signing-key.png)

グーグルプレイ(Google Play)を使ってアプリ署名(App Signing)をするため```FINISH```ボタンを押します。

![グーグルプレイ利用規約同意](/assets/images/category/react-native/android-google-play/accept-agreement.png)

上のような利用規約が表示されたら下にある```ACCEPT```ボタンを押して同意します。

![グーグルプレイapkアップロード](/assets/images/category/react-native/android-google-play/app_apk.png)

上でビルド下RN(React Native)の```apk```ファイルをアップロードします。

![グーグルプレイapkリリースノート](/assets/images/category/react-native/android-google-play/app_release_note.png)

アプリの配布名前(Release Name)と配布ノート(Release Note)を作成して右下の```SAVE```ボタンを押します。そしたら右の```REVIEW```ボタンがアクティブになります。アクティブになった```REVIEW```ボタンを押します。

![グーグルプレイ登録不可](/assets/images/category/react-native/android-google-play/not_yet.png)

アプリの登録手続きが終わってないので右下の```START ROLLOUT TO PRODUCTION```ボタンがアクティブになりません。左メニューの```Content rating```を押します。

![グーグルプレイコンテンツ評価](/assets/images/category/react-native/android-google-play/app_content_rating.png)

コンテンツ評価(Content Rating)を設定する画面です。```CONTINUE```を押します。

![グーグルプレイコンテンツ評価情報入力](/assets/images/category/react-native/android-google-play/app_content_rating_insert_info.png)

メール情報やアプリのカテゴリを選択します。

![グーグルプレイコンテンツ評価情報同意](/assets/images/category/react-native/android-google-play/app_content_rating_agreement.png)

アプリのコンテンツ評価を決めるための情報を選択します。全て選択したら下の```SAVE QUESTIONNAIRE```ボタンを押してアクティブされた```CALCULATE RATING```を押します。

![グーグルプレイコンテンツ評価情報選択完了](/assets/images/category/react-native/android-google-play/app_content_rating_completed.png)

入力した情報をベースでコンテンツ評価が計算されて出ます。内容を確認して下の```APPLYING RATING```を押します。

![グーグルプレイコンテンツ評価完了](/assets/images/category/react-native/android-google-play/calculated_content_rating.png)

コンテンツ評価の入力を完了しました。コンテンツ評価に影響があるアップデートがあったら、コンテンツ評価を再計算する必要がありますので、上の手続きをまたしてください。

![グーグルプレイコンテンツ評価](/assets/images/category/react-native/android-google-play/content_rating.png)

最後の手続きである料金の設定をするため左メニューの```Pricing & distribution```を押します。

![グーグルプレイアプリ料金情報](/assets/images/category/react-native/android-google-play/app_price_info.png)

アプリの料金を設定する画面です。私たちは無料でアプリを提供する予定なので、```FREE```を設定して進めます。また、子供向け、アプリに広告が含まれてあるかなど情報を入力します。必須項目を全て入力したら下の```SAVE DRAFT```ボタンを押します。

## アプリ審査申請
アプリ審査(App Review)のための準備が終わりました。メニューの```App release```を押します。

![グーグルプレイアプリ審査](/assets/images/category/react-native/android-google-play/app_review.png)

上で作成した```Production```項目の横にある```EDIT RELEASE```ボタンを押します。

![グーグルプレイアプリ審査情報](/assets/images/category/react-native/android-google-play/app_review_info.png)

上で作成した情報が見えます。スクロールして下に移動して、```REVIEW```ボタンを選択します。

![グーグルプレイアプリ審査申請](/assets/images/category/react-native/android-google-play/apply_app_review_info.png)

上のような画面が見えたらスクロールして下に移動して```START ROLLOUT TO PRODUCTION```を押します。

![グーグルプレイアプリ登録](/assets/images/category/react-native/android-google-play/register_app.png)

アプリ審査の準備が終わったら```CONFIRM```ボタンを押してアプリ審査を申請します。

## エラー対応
下記のコマンドでアンドロイドをビルドする時、

```bash
./gradlew assembleRelease
```

下記のようなエラーメッセージが出ってビルドが失敗される時があります。

```bash
Execution failed for task ':app:transformDexArchiveWithExternalLibsDexMergerForRelease'.
```

下記の内容を`android/app/build.gradle`に追加してもう一回ビルドします。

```js
defaultConfig {
    ...
    multiDexEnabled true
}
```

### ビルドエラー対応
RN(React Native)のバージョン0.58で下記のコマンドを実行したら

```bash
./gradlew assembleRelease
```

下記のエラーが出ます。

```bash
  --auto-add-overlay\
          --non-final-ids\
          -0\
          apk\
          --no-version-vectors
  Daemon:  AAPT2 aapt2-3.2.1-4818971-osx Daemon #0
```

下記のコマンドで実行したらビルドができます。

```bash
./gradlew app:assembleRelease
```

### 権限エラー
RN(React Native)のバージョン0.58でビルドしたファイルをグーグルプレイへアップロードする時```android.permission.READ_PHONE_STATE```権限が含めてるのでダメですのエラーが出ます。

公式サイトに解決方法があります。

[https://facebook.github.io/react-native/docs/removing-default-permissions](https://facebook.github.io/react-native/docs/removing-default-permissions){:rel="nofollow noreferrer" target="_blank"}

それを見ながらやってみます。

RN(React Native)プロジェクトの```android/app/src/main/AndroidManifest.xml```のファイルを開いて下記のように修正します。

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="XXXXXXXX"
+   xmlns:tools="http://schemas.android.com/tools"
    >

    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.SYSTEM_ALERT_WINDOW" />
+   <uses-permission tools:node="remove" android:name="android.permission.READ_PHONE_STATE" />
+   <uses-permission tools:node="remove" android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
+   <uses-permission tools:node="remove" android:name="android.permission.READ_EXTERNAL_STORAGE" />
...
```

そして```android/app/src/release/AndroidManifest.xml```ファイルを生成して下記の内容をコピペします。(パッケージ名は自分のパッケージ名を入れてください。)

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="XXXXXXX"
    xmlns:tools="http://schemas.android.com/tools">

    <uses-permission tools:node="remove" android:name="android.permission.SYSTEM_ALERT_WINDOW" />

</manifest>
```

これでビルドしてアップロードしたら問題なくアップロードできることを確認できます。



### Android 4.4.2 Kitkat
RN(React Native) 0.58でビルドしたファイルをアンドロイド4.4.2(Kitkat)の端末でテストする時、アプリがCrashが発生して起動出来ない問題が発生しました。問題を調査した結果、`multiDexEnabled`の問題で下記の内容を追加して解決しました。

RN(React Native)プロジェクトの`android/app/build.gradle`を開いて下記の内容を追加してください。

```bash
dependencies {
    implementation project(':react-native-firebase')
    ...
    implementation 'com.android.support:multidex:1.0.1'
}
```

また、`MainApplication.java`を開いて下記のように修正してください。

```java
import android.app.Application;
import android.content.Context;
import android.support.multidex.MultiDex;
...
public class MainApplication extends Application implements ReactApplication {
  @Override
  protected void attachBaseContext(Context base) {
      super.attachBaseContext(base);
      MultiDex.install(this);
  }
  ...
}
```

このように修正してアンドロイド4.4.2(Kitkat)でテストしたら無事に動作することを確認出来ます。


## 完了
アンドロイドアプリストア(Google Play)にアプリを登録するための手続きが終わりました。アプリ審査は2~3時間くらいかかります。アプリの審査が終わったら登録申請したアプリをアンドロイドアプリストア(Google Play)で検索やダウンロードができます。