---
layout: 'post'
permalink: '/react-native/firebase-crashlytics/'
paginate_path: '/react-native/:num/firebase-crashlytics/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'Firebase Crashlytics'
description: 'react-native-firebaseを使ってファイアベース(Firebase)のCrashlyticsでアプリのCrashが発生したらその情報を取得してみましょう。'
image: '/assets/images/category/react-native/firebase-crashlytics.jpg'
---


## 概要
以前のブログ([iOS App crash 分析]({{site.url}}/{{page.categories}}/ios-app-crash-debugging/){:target="_blank"})でアプリ審査の拒絶(reject)にあるApp crash logを分析してみました。しかし、審査中ではなくユーザーが使ってる環境でCrashが発生したら私たちは分からないです。それでファイアベース(Firebase)のCrashlyticsを使ってアプリのCrashを収集して分析してみます。このブログではreact-native-firebaseライブラリを使う予定です。react-native-firebaseライブラリのインストールや設定は以前のブログを確認してください。

- [Firebase Admob]({{site.url}}/{{page.categories}}/react-native-firebase-admob/){:target="_blank"}

## iOS設定
ファイアベース(Firebase)のCrashlyticsを使うためreact-native-firebaseを設定します。

### 必要なライブラリ設定やインストール
iOSへ必要なライブラリを下記のように```Podfile```に追加します。

```ruby
...
pod 'Firebase/Core'
pod 'Firebase/AdMob'
pod 'Fabric'
pod 'Crashlytics'
...
```

追加したライブラリを下の```pod```コマンドでインストールします。

```bash
# cd ios
pod update
```

### Crashlytics実行スクリプト追加
ファイアベース(Firebase)のCrashlyticsを使うためCrashlytics実効スクリプトを追加する必要があります。


RN(react native)プロジェクトフォルダにある```ios/[AppName].xcworkspace```を選択してXcodeを実効します。

![xcode 実効](/assets/images/category/react-native/firebase-crashlytics/execute_xcode.png)

左にあるファイルエクスプローラと```TARGETS```で自分のプロジェクトを選択します。そして上のメニューで```Build Phases```を選択します。

![xcode build phases](/assets/images/category/react-native/firebase-crashlytics/build_phases.png)

Build Phasesタブで左上の```+```ボタンを押して```New Run Script Phase```を選択します。

![new run script menu on build phases](/assets/images/category/react-native/firebase-crashlytics/new_run_script.png)

下記のコマンドを```Run Scrit```の```Shelll```下にある```# Type a script..```に入力します。

```bash
"${PODS_ROOT}/Fabric/run"
```

![add Run Script](/assets/images/category/react-native/firebase-crashlytics/add_run_script.png)

### テスト
今まで設定したファイアベース(Firebase)のCrashlyticsをテストするため下記のコードをテストしたい位置に入れます。

```js
firebase.crashlytics().crash();
```

この部分は強制的にアプリをCrashさせるコードです。アプリのCrashが発生して終了されたら、ファイアベース(Firebase)のCrashlyticsに報告できるようにアプリをもう一度起動します。

下記のコマンドまたはxcodeを使ってシミュレータを起動します。

```bash
react-native run-ios
```

xcodeを使ってシミュレータを起動した方はxcodeを終了してシミュレータでアプリを選択して再起動してください。xcodeが起動中にCrashが発生したらCrashlyticsまで報告が行かなく、xcodeがCrashを処理します。

Crashが発生してアプリをまた起動します。少し時間がたったらファイアベースコンソル(Firebase Console)のCrashlyticsに下のような内容が確認できます。

![Firebase Console Crashlytics](/assets/images/category/react-native/firebase-crashlytics/firebase_crashlytics.png)

注意：テストコード(```firebase.crashlytics().crash();```)は確認が終わったら必ず削除してください。

## アンドロイド設定
アンドロイド(Android)でファイアベース(Firebase)のCrashlyticsを使うためreact-native-firebaseを設定します。

### 必要なライブラリ設定やインストール
下記のように```android/app/build.gradle```ファイルを修正します。

```xml
apply plugin: "com.android.application"
apply plugin: 'io.fabric'
...
dependencies {
  ...
  implementation('com.crashlytics.sdk.android:crashlytics:2.9.5@aar') {
    transitive = true
  }
}
...
```

下記のように```android/build.gradle```ファイルを修正します。

```xml
...
buildscript {
  ...
  dependencies {
    ...
    classpath 'com.google.gms:google-services:4.0.1'
    classpath 'io.fabric.tools:gradle:1.25.4'
  }
  ...
  repositories {
    ...
    jcenter()
    maven {
        url 'https://maven.fabric.io/public'
    }
  }
  ...
}
...
```

下記のように```android/app/src/main/java/com/[app name]/MainApplication.java```ファイルを修正します。

```java
...
import io.invertase.firebase.RNFirebasePackage;
import io.invertase.firebase.fabric.crashlytics.RNFirebaseCrashlyticsPackage;
...
    @Override
    protected List<ReactPackage> getPackages() {
      return Arrays.<ReactPackage>asList(
          ...
          new RNFirebasePackage(),
          new RNFirebaseCrashlyticsPackage(),
          ...
      );
    }
...
```

### テスト
今まで設定したファイアベース(Firebase)のCrashlyticsをテストするため下記のコードをテストしたい位置へ追加します。

```js
firebase.crashlytics().crash();
```

アンドロイド(Android)ではエミュレータを起動して```react-native run-android```を実効してCrashを
発生させたら赤いエラー画面がでって実際Crashが報告されませんでした。それで私たちはエミュレータへビルドしたファイルをインストールしてテストしました。アンドロイド(Android)ビルドやテストに関しては[アンドロイドビルドやテスト]({{site.url}}/{{page.categories}}/android-running-on-device/){:target="_blank"}を参考してください。

```bash
react-native bundle --platform android --dev false --entry-file index.js --bundle-output android/app/src/main/assets/index.android.bundle
```

上のコマンドを使ってjavascriptをビルドした後、下記のコマンドでエミュレータにビルドされたファイルをインストールしました。

```bash
react-native run-android --variant=release
```

それでテストしたら下記のようにアンドロイド(Android)でもCrash報告を見ることができました。

![Firebase Console Crashlytics android](/assets/images/category/react-native/firebase-crashlytics/firebase_crashlytics_android.png)

注意: テストコード(```firebase.crashlytics().crash();```)は確認が完了したら必ず削除してください。

## 参考
- [https://firebase.google.com/docs/crashlytics/get-started](https://firebase.google.com/docs/crashlytics/get-started){:rel="nofollow noreferrer" target="_blank"}
- [https://rnfirebase.io/docs/v5.x.x/crashlytics/ios](https://rnfirebase.io/docs/v5.x.x/crashlytics/ios){:rel="nofollow noreferrer" target="_blank"}