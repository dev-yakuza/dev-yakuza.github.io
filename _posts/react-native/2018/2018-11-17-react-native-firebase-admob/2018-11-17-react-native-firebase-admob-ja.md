---
layout: 'post'
permalink: '/react-native/react-native-firebase-admob/'
paginate_path: '/react-native/:num/react-native-firebase-admob/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'Firebase Admob'
description: 'react-native-firebaseライブラリを使ってグーグルアドモブ(Google Admob)を表示してみましょう。'
image: '/assets/images/category/react-native/react-native-firebase-admob.jpg'
---

<div id="contents_list" markdown="1">

## 目次

1. [概要](#概要)
1. [ライブラリインストール](#ライブラリインストール)
1. [ライブラリリンク](#ライブラリリンク)
    - [0.60以上](#060以上)
    - [0.59以下](#059以下)
1. [firebaseプロジェクト生成](#firebaseプロジェクト生成)
1. [グーグルアドモブ設定](#グーグルアドモブ設定)
1. [firebase iOS 設定](#firebase-ios-設定)
1. [firebaseアンドロイド(Android)設定](#firebaseアンドロイドandroid設定)
    - [アンドロイドパッケージ名修正](#アンドロイドパッケージ名修正)
1. [ソース追加](#ソース追加)
    - [バナー](#バナー)
    - [割込み広告](#割込み広告)
1. [エラー対応](#エラー対応)
    - [admob/error-code-no-fill](#admoberror-code-no-fill)
1. [完了](#完了)

</div>

## 概要

私はグーグルアドモブ(Google Admob)を使ってアプリへ広告を表示しています。以前にはreact-native-admobというライブラリを使いましたが、グーグルアドモブ(Google Admob)以外にもアナリティクス(Analytics)など、色んな機能を使うことのになって、統合的に使えるライブラリを探した結果react-native-firebaseというライブラリを見つけました。

ここにはグーグルファイアベース(Google Firebase)を使って無料でグーグルアドモブ(Google Admob), アナリティクス(Analytics)を使う方法を紹介します。

簡単にグーグルアドモブ(Google Admob)だけ使いたい方は以前のブログ[グーグルアドモブ(Google Admob)]({{site.url}}/{{page.categories}}/react-native-admob/){:target="_blank"}を参考してください。

下記のリンクはreact-native-firebaseの公式ページです。詳しく内容は公式サイトを確認してください。

- 公式サイト: [react-native-firebase](https://github.com/invertase/react-native-firebase){:rel="nofollow noreferrer" target="_blank"}

## ライブラリインストール

下のコマンドを使ってreact-native-firebaseライブラリをインストールします。

```bash
npm install --save react-native-firebase
```

{% include in-feed-ads.html %}

## ライブラリリンク

react-native-firebaseライブラリを使うためにはライブラリをリンクする必要があります。

### 0.60以上

下記のコマンドを使ってreact-native-firebaseライブラリをリアクトネイティブ(React Native)プロジェクトへ連携します。

```bash
cd ios
pod install
cd ..
```

### 0.59以下

下記のコマンドを使ってreact-native-firebaseライブラリをリアクトネイティブ(React Native)プロジェクトへ連携します。

```bash
react-native link react-native-firebase
```

## firebaseプロジェクト生成

次はグーグルのファイアベース(Google Firebase)へプロジェクトを生成する必要があります。下のリンクを押してグーグルファイアベース(Google Firebase)へ移動します。

- グーグルファイアベース(Google Firebase): [https://firebase.google.com](https://firebase.google.com){:rel="nofollow noreferrer" target="_blank"}

![google firebase](/assets/images/category/react-native/react-native-firebase-admob/google-firebase.jpg)

右上にある```SIGN IN```ボタンを押してログインします。

![google firebase after login](/assets/images/category/react-native/react-native-firebase-admob/google-firebase-after-login.jpg)

ログインしたら右上にある```GO TO CONSOLE```を押してグーグルファイアベースコンソル(Google Firebase Console)へ移動します。

![google firebase console](/assets/images/category/react-native/react-native-firebase-admob/google-firebase-console.jpg)

グーグルファイアベースコンソル(Google Firebase Console)で```+ Add project```を押してプロジェクトを追加します。

![google firebase console add project](/assets/images/category/react-native/react-native-firebase-admob/google-firebase-console-add-project.jpg)

プロジェクト情報を追加した後```Create project```ボタンを押してプロジェクトを生成します。

## グーグルアドモブ設定

グーグルアドモブ(Google Admob)へ広告を設定する必要があります。グーグルファイアベースコンソル(Google Firebase Console)の```Grow``` > ```Admob```を選択したら下記の画面が見えます。

![google firebase console admob](/assets/images/category/react-native/react-native-firebase-admob/google-firebase-console-admob.jpg)

画面の下へ```linking your apps in AdMob.```リンクを押してグーグルアドモブ(Google Admob)ページへ移動します。

グーグルアドモブ(Google Admob)へ広告を設定する方法は[グーグルアドモブ(Google Admob)]({{site.url}}/{{page.categories}}/react-native-admob/){:target="_blank"}ブログを参考してください。

{% include in-feed-ads.html %}

## firebase iOS 設定

グーグルファイアベースコンソル(Google Firebase Console)でプロジェクトを選択したら下の画面が見えます。

![google firebase console project](/assets/images/category/react-native/react-native-firebase-admob/google-firebase-console-project.jpg)

中央にある```iOS```ボタンを押してiOS設定画面へ移動します。

![google firebase console project ios](/assets/images/category/react-native/react-native-firebase-admob/google-firebase-console-project-ios.jpg)

開発したアプリのバンドルID(Bundle ID)を入力して```Register app```ボタンを押します。

![GoogleService-Info.plist download](/assets/images/category/react-native/react-native-firebase-admob/googleservice-info-plist-download.jpg)

グーグルファイアベース(Google Firebase)が生成した```GoogleService-Info.plist```ファイルをダウンロードして```info.plist```と同じ位置へコピーします。```GoogleService-Info.plist```ファイルの追加が終わったら```Next```ボタンを押します。

![add Firebase SDK](/assets/images/category/react-native/react-native-firebase-admob/add-firebase-sdk.jpg)

画面へ表示したようにグーグルファイアベースSDK(Google Firebase SDK)をリアクトネイティブ(React Native)プロジェクトへ追加します。

React Nativeのバージョンが0.59以下の場合、下記のコマンドを実行します。

```bash
pod init
```

グーグルファイアベースSDK(Google Firebase SDK)を```Podfile```に追加します。

```ruby
target 'blaboo' do
  ...
  pod 'Firebase/Core'
  pod 'Firebase/Analytics' // if you use Analytics
  pod 'Firebase/AdMob'
  ...
end
```

グーグルファイアベースSDK(Google Firebase SDK)をインストールします。

```bash
pod install
# pod update
```

![edit appdelegate.m for firebase](/assets/images/category/react-native/react-native-firebase-admob/edit-appdelegate.jpg)

リアクトネイティブ(React Native)プロジェクトの```AppDelete.m```ファイルを上のようにコードを追加します。

```js
...
@import Firebase;
...
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
  [FIRApp configure];
  ...
  return YES;
}
...
```

グーグルファイアベースSDK(Google Firebase SDK)を初期化します。そして、`Info.plist`ファイルを開いて下記のように修正しました。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	...
	<key>GADIsAdManagerApp</key>
	<true/>
	<key>GADApplicationIdentifier</key>
  <string>ca-app-pub-7987914246691031~8295071692</string>
</dict>
</plist>
```

グーグルアドモブ(Google Admob)のアプリID(App ID)を入力してグーグルアドモブ(Google Admob)を初期化します。グーグルアドモブのアプリID(App ID)を取得する方法は以前のブログ[グーグルアドモブ(Google Admob)]({{site.url}}/{{page.categories}}/react-native-admob/){:target="_blank"}を参考してください。

![connect firebase to app](/assets/images/category/react-native/react-native-firebase-admob/connect-firebase-to-app.jpg)

私はこの部分では```Skip this step```を押してスキップしました。

{% include in-feed-ads.html %}

## firebaseアンドロイド(Android)設定

グーグルファイアベースコンソル(Google Firebase Console)へ左上の```Project Overview```を選択します。

![Google Firebase Console Project Overview](/assets/images/category/react-native/react-native-firebase-admob/firebase-project-overview.jpg)

上部へ```+ Add app``` > ```アンドロイド(Android)アイコン```を押してアンドロイドプロジェクト設定へ移動します。

![Google Firebase Android app register](/assets/images/category/react-native/react-native-firebase-admob/register-android.jpg)

アンドロイドパッケージ名(Android Package Name)を入力して```Register app```を押します。

リアクトネイティブ(React Native)でアンドロイドパッケージ名を修正したい方は下の項目を進んでください。

### アンドロイドパッケージ名修正

- リアクトネイティブ(React Native)プロジェクトフォルダで```android/app/BUCK```ファイル修正

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

- リアクトネイティブ(React Native)プロジェクトフォルダで```android/app/src/main/AndroidManifest.xml```ファイル修正

  ```xml
  <manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="package_name">
  ...
  ```

- リアクトネイティブ(React Native)プロジェクトフォルダで```android/app/src/main/java/com/ProjectName/MainActivity.java```ファイル修正

  ```java
  package package_name;
  ...
  ```

- リアクトネイティブ(React Native)プロジェクトフォルダで```android/app/src/main/java/com/ProjectName/MainApplication.java```ファイル修正

  ```java
  package package_name;
  ...
  ```

- リアクトネイティブ(React Native)プロジェクトフォルダで```android/app/build.gradle```ファイル修正

  ```java
  ...
  defaultConfig {
      applicationId package_name
      ...
  }
  ...
  ```

![Google Firebase google-services.json setting](/assets/images/category/react-native/react-native-firebase-admob/set-google-services-json.jpg)

グーグルファイアベース(Google Firebase)が作った```google-services.json```ファイルをリアクトネイティブ(React Native)プロジェクトの```android/app```フォルダへコピーします。その後、```Next```ボタンを押して次へ移動します。

![Google Firebase setting on android](/assets/images/category/react-native/react-native-firebase-admob/setting-android.jpg)

リアクトネイティブ(React Native)プロジェクトがあるフォルダで```android/build.gradle```を開いて下記のコードを追加します。

```js
buildscript {
  repositories {
    google()
    jcenter()
  }
  dependencies {
    // Add this line
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

上記のように```repositories```へ```google()```が入ってるか```jcenter()```のより上にあるか確認します。

リアクトネイティブ(React Native)プロジェクトがあるフォルダで```android/app/build.gradle```ファイルを開いて下記のコードを追加します。

```js
dependencies {
    implementation project(':react-native-firebase') // under 59 version
    ...
    implementation "com.google.android.gms:play-services-base:16.1.0"
    implementation 'com.google.firebase:firebase-core:16.0.9'
    implementation 'com.google.firebase:firebase-analytics:17.2.2' // if you use analytics
    implementation "com.google.firebase:firebase-ads:17.2.1"
}
```

そして同じファイルの一番下へ下記のコードを追加します。

```js
...
apply plugin: 'com.google.gms.google-services'
```

- 0.60以上

Admobeを適用するため```android/app/src/main/java/com/[app name]/MainApplication.java```ファイルを開いて下記のように修正します。

```java
import io.invertase.firebase.RNFirebasePackage;
import io.invertase.firebase.admob.RNFirebaseAdMobPackage;
import io.invertase.firebase.analytics.RNFirebaseAnalyticsPackage;
...
@Override
protected List<ReactPackage> getPackages() {
  @SuppressWarnings("UnnecessaryLocalVariable")
  List<ReactPackage> packages = new PackageList(this).getPackages();
  // Packages that cannot be autolinked yet can be added manually here, for example:
  // packages.add(new MyReactNativePackage());
  packages.add(new RNFirebaseAnalyticsPackage());
  packages.add(new RNFirebaseAdMobPackage());
  packages.add(new RNFirebaseCrashlyticsPackage());
  return packages;
}
...
```

Admobを適用するため```android/app/src/AndroidManifest.xml```ファイルを開いて下記のように修正します。

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
  package="io.github.dev.yakuza.blaboo">
    ...
    <application
      android:name=".MainApplication"
      android:label="@string/app_name"
      android:icon="@mipmap/ic_launcher"
      android:allowBackup="false"
      android:theme="@style/AppTheme">
      <meta-data
        android:name="com.google.android.gms.ads.APPLICATION_ID"
        android:value="ca-app-pub-7987914246691031~9800293270"/>
      ...
    </application>

</manifest>
```

- 0.59以下

Admobeを適用するため```android/app/src/main/java/com/[app name]/MainApplication.java```ファイルを開いて下記のように修正します。

```java
import io.invertase.firebase.RNFirebasePackage;
import io.invertase.firebase.admob.RNFirebaseAdMobPackage;
import io.invertase.firebase.analytics.RNFirebaseAnalyticsPackage;
import com.google.android.gms.ads.MobileAds;
...

@Override
protected List<ReactPackage> getPackages() {
  return Arrays.<ReactPackage>asList(
    ...
    new RNFirebasePackage(),
    new RNFirebaseAdMobPackage(),
    new RNFirebaseAnalyticsPackage(),
    ...
  );
}

@Override
public void onCreate() {
  super.onCreate();
  MobileAds.initialize(this, "ca-app-pub-7987914246691031~9800293270");
  ...
}
```

上のソースで```MobileAds.initialize(this, "ad app id");```部分へグーグルアドモブ(Google Admob)で生成下アプリアイディ(App ID)を追加します。グーグルアドモブ(Google Admob)のアプリアイディ(App ID)を生成する方法は以前のブログ[グーグルアドモブ(Google Admob)]({{site.url}}/{{page.categories}}/react-native-admob/){:target="_blank"}を参考してください。

アンドロイドスタジオ(Android Studio)を開いて```Gradle```を同期化するか聞いてくれたら```Sync now```を押して同期化します。

{% include in-feed-ads.html %}

## ソース追加

react-native-firebaseの設定は完了しました。今からリアクトネイティブ(React Native)のソースコードを修正してグーグルアドモブ(Google Admob)が上手く表示されるようにします。

下のソースはreact-native-firebaseを使ってbannerを表示する例です。

```js
...
import firebase from 'react-native-firebase';
...
```

react-native-firebaseをローディングします。

### バナー

下記のソースコードは```react-native-firebase```のアドモブ(Admob)を使って広告タイプ(Ad Unit)がバナー(Banner)である広告を表示するれいたい例題です。

```js
import { Platform } from 'react-native';
...
render() {
    const Banner = firebase.admob.Banner;
    const AdRequest = firebase.admob.AdRequest;
    const request = new AdRequest();

    const unitId =
      Platform.OS === 'ios'
        ? 'ca-app-pub-7987914246691031/4248107679'
        : 'ca-app-pub-7987914246691031/5729668166';
    ...
    return (
        ...
        <Banner
          unitId={unitId}
          size={'SMART_BANNER'}
          request={request.build()}
          onAdLoaded={() => {
            console.log('Advert loaded');
          }}
        />
    );
```

上のようにソースコードを追加してリアクトネイティブ(React Native)プロジェクトを実行したらバナーが上手く表示されることを確認することができます。

### 割込み広告

下記のソースコードは```react-native-firebase```のアドモブ(Admob)を使って広告タイプ(AD Unit)が割込み広告(Interstitial)である広告を表示する方法です。

```js
import { Platform } from 'react-native';
...
componentDidMount() {
  ...
  const unitId =
    Platform.OS === 'ios'
      ? 'ca-app-pub-7987914246691031/4248107679'
      : 'ca-app-pub-7987914246691031/5729668166';
  const advert = firebase.admob().interstitial(unitId);
  const AdRequest = firebase.admob.AdRequest;
  const request = new AdRequest();
  advert.loadAd(request.build());

  advert.on('onAdLoaded', () => {
    console.log('Advert ready to show.');
    advert.show();
  });
  ...
}
...
```

上のソースでわかると思いますが、```react-native-firebase```のアドモブ(Admob)の割込み広告(Interstitial)を表示したい時、```advert.show()```を使って表示します。表示する前いつも```advert.isLoaded()```を使って広告が準備できたか確認してください。

```js
setTimeout(() => {
  if (advert.isLoaded()) {
    advert.show();
  } else {
    // Unable to show interstitial - not loaded yet.
  }
}, 1000);
```

{% include in-feed-ads.html %}

## エラー対応

react-native-firebaseでadmobを実装して問題があった内容をまとめます。

### admob/error-code-no-fill

私もいよいよ出ました。突然アプリの広告が表示されなくて調査してみたら`admob/error-code-no-fill`のエラーが出ました。

私は収入が4000円（8000円から入金可能）ぐらい時から`admob/error-code-no-fill`のエラーが出ました。その時私はまだPaymentの情報を入力してない状態でした。入金先の情報を入力した後から広告はまた良く表示されました。グーグルが入金が出来ないかもだから広告を表示してなかったかもしれないです。

結論的に、`admob/error-code-no-fill`のエラーが出て広告が表示されない方中Payment情報を入力してない方は、入金情報を入れてみてください。


## 完了

リアクトネイティブ(React Native)プロジェクトへreact-native-firebaseライブラリを使ってグーグルアドモブ(Google Admob)を適用する方法をみてみました。これでreact-native-firebaseを設定したらアナリティクス(Analytics)は自動に設定されて分析することができます。

グーグルファイアベースコンソル(Google Firebase Console)のメニューで```Analytics``` > ```Dashboard```を押してみたら、分析してることが確認できます。

![react native firebase analytics](/assets/images/category/react-native/react-native-firebase-admob/react-native-firebase-analytics.jpg)

