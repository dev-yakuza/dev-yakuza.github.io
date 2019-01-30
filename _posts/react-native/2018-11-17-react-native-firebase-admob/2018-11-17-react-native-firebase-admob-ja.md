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


## 概要
私たちはグーグルアドモブ(Google Admob)を使ってアプリへ広告を表示しています。以前にはreact-native-admobというライブラリを使いましたが、グーグルアドモブ(Google Admob)以外にもアナリティクス(Analytics)など、色んな機能を使うことのになって、統合的に使えるライブラリを探した結果react-native-firebaseというライブラリを見つけました。

ここにはグーグルファイアベース(Google Firebase)を使って無料でグーグルアドモブ(Google Admob), アナリティクス(Analytics)を使う方法を紹介します。

簡単にグーグルアドモブ(Google Admob)だけ使いたい方は以前のブログ[グーグルアドモブ(Google Admob)]({{site.url}}/{{page.categories}}/react-native-admob/){:target="_blank"}を参考してください。

下記のリンクはreact-native-firebaseの公式ページです。詳しく内容は公式サイトを確認してください。

- 公式サイト: [react-native-firebase](https://github.com/invertase/react-native-firebase){:rel="nofollow noreferrer" target="_blank"}

## ライブラリインストール
下のコマンドを使ってreact-native-firebaseライブラリをインストールします。

```bash
npm install --save react-native-firebase
```

## ライブラリリンク
下記のコマンドを使ってreact-native-firebaseライブラリをRN(react native)プロジェクトへ連携します。

```bash
react-native link react-native-firebase
```

## firebaseプロジェクト生成
次はグーグルのファイアベース(Google Firebase)へプロジェクトを生成する必要があります。下のリンクを押してグーグルファイアベース(Google Firebase)へ移動します。

- グーグルファイアベース(Google Firebase): [https://firebase.google.com](https://firebase.google.com){:rel="nofollow noreferrer" target="_blank"}

![google firebase](/assets/images/category/react-native/react-native-firebase-admob/google-firebase.png)

右上にある```SIGN IN```ボタンを押してログインします。

![google firebase after login](/assets/images/category/react-native/react-native-firebase-admob/google-firebase-after-login.png)

ログインしたら右上にある```GO TO CONSOLE```を押してグーグルファイアベースコンソル(Google Firebase Console)へ移動します。

![google firebase console](/assets/images/category/react-native/react-native-firebase-admob/google-firebase-console.png)

グーグルファイアベースコンソル(Google Firebase Console)で```+ Add project```を押してプロジェクトを追加します。

![google firebase console add project](/assets/images/category/react-native/react-native-firebase-admob/google-firebase-console-add-project.png)

プロジェクト情報を追加した後```Create project```ボタンを押してプロジェクトを生成します。

## グーグルアドモブ設定
グーグルアドモブ(Google Admob)へ広告を設定する必要があります。グーグルファイアベースコンソル(Google Firebase Console)の```Grow``` > ```Admob```を選択したら下記の画面が見えます。

![google firebase console admob](/assets/images/category/react-native/react-native-firebase-admob/google-firebase-console-admob.png)

画面の下へ```linking your apps in AdMob.```リンクを押してグーグルアドモブ(Google Admob)ページへ移動します。

グーグルアドモブ(Google Admob)へ広告を設定する方法は[グーグルアドモブ(Google Admob)]({{site.url}}/{{page.categories}}/react-native-admob/){:target="_blank"}ブログを参考してください。

## firebase iOS 設定
グーグルファイアベースコンソル(Google Firebase Console)でプロジェクトを選択したら下の画面が見えます。

![google firebase console project](/assets/images/category/react-native/react-native-firebase-admob/google-firebase-console-project.png)

中央にある```iOS```ボタンを押してiOS設定画面へ移動します。

![google firebase console project ios](/assets/images/category/react-native/react-native-firebase-admob/google-firebase-console-project-ios.png)

開発したアプリのバンドルID(Bundle ID)を入力して```Register app```ボタンを押します。

![GoogleService-Info.plist download](/assets/images/category/react-native/react-native-firebase-admob/googleservice-info-plist-download.png)

グーグルファイアベース(Google Firebase)が生成した```GoogleService-Info.plist```ファイルをダウンロードして```info.plist```と同じ位置へコピーします。```GoogleService-Info.plist```ファイルの追加が終わったら```Next```ボタンを押します。

![add Firebase SDK](/assets/images/category/react-native/react-native-firebase-admob/add-firebase-sdk.png)

画面へ表示したようにグーグルファイアベースSDK(Google Firebase SDK)をRN(react native)プロジェクトへ追加します。

```bash
pod init
```

グーグルファイアベースSDK(Google Firebase SDK)を```Podfile```に追加します。

```ruby
target 'blaboo' do
  # Uncomment the next line if you're using Swift or would like to use dynamic frameworks
  # use_frameworks!

  # Pods for blaboo
  pod 'Firebase/Core'
  pod 'Firebase/AdMob'

#  target 'blaboo-tvOS' do
#    inherit! :search_paths
#    # Pods for testing
#  end

  target 'blabooTests' do
    inherit! :search_paths
    # Pods for testing
  end

end
```

グーグルファイアベースSDK(Google Firebase SDK)をインストールします。

```bash
pod install
# pod update
```

![edit appdelegate.m for firebase](/assets/images/category/react-native/react-native-firebase-admob/edit-appdelegate.png)

RN(react native)プロジェクトの```AppDelete.m```ファイルを上のようにコードを追加します。

```js
...
@import Firebase;
...
```

グーグルファイアベースSDK(Google Firebase SDK)をインポートします。

```js
...
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
...
[FIRApp configure];
[GADMobileAds configureWithApplicationID:@"ca-app-pub-7987914246691031~8295071692"];
return YES;
...
```

グーグルファイアベースSDK(Google Firebase SDK)を初期化します。その後グーグルアドモブ(Google Admob)のアプリID(App ID)を入力してグーグルアドモブ(Google Admob)を初期化します。グーグルアドモブのアプリID(App ID)を取得する方法は以前のブログ[グーグルアドモブ(Google Admob)]({{site.url}}/{{page.categories}}/react-native-admob/){:target="_blank"}を参考してください。

![connect firebase to app](/assets/images/category/react-native/react-native-firebase-admob/connect-firebase-to-app.png)

私たちはこの部分では```Skip this step```を押してスキップしました。

## firebaseアンドロイド(Android)設定
グーグルファイアベースコンソル(Google Firebase Console)へ左上の```Project Overview```を選択します。

![Google Firebase Console Project Overview](/assets/images/category/react-native/react-native-firebase-admob/firebase-project-overview.png)

上部へ```+ Add app``` > ```アンドロイド(Android)アイコン```を押してアンドロイドプロジェクト設定へ移動します。

![Google Firebase Android app register](/assets/images/category/react-native/react-native-firebase-admob/register-android.png)

アンドロイドパッケージ名(Android Package Name)を入力して```Register app```を押します。

RN(react native)でアンドロイドパッケージ名を修正したい方は下の項目を進んでください。

### アンドロイドパッケージ名修正
- RN(react native)プロジェクトフォルダで```android/app/BUCK```ファイル修正

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

- RN(react native)プロジェクトフォルダで```android/app/src/main/AndroindManifest.xml```ファイル修正

  ```xml
  <manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="package_name">
  ...
  ```

- RN(react native)プロジェクトフォルダで```android/app/src/main/java/com/ProjectName/MainActivity.java```ファイル修正

  ```java
  package package_name;
  ...
  ```

- RN(react native)プロジェクトフォルダで```android/app/src/main/java/com/ProjectName/MainApplication.java```ファイル修正

  ```java
  package package_name;
  ...
  ```
- RN(react native)プロジェクトフォルダで```android/app/src/bundle.gradle```ファイル修正

  ```java
  ...
  defaultConfig {
      applicationId package_name
      ...
  }
  ...
  ```
![Google Firebase google-services.json setting](/assets/images/category/react-native/react-native-firebase-admob/set-google-services-json.png)

グーグルファイアベース(Google Firebase)が作った```google-services.json```ファイルをRN(react native)プロジェクトの```android/app```フォルダへコピーします。その後、```Next```ボタンを押して次へ移動します。

![Google Firebase setting on android](/assets/images/category/react-native/react-native-firebase-admob/setting-android.png)

RN(react native)プロジェクトがあるフォルダで```android/build.gradle```を開いて下記のコードを追加します。

```js
buildscript {
  repositories {
    google()
    jcenter()
  }
  dependencies {
    // Add this line
    classpath 'com.google.gms:google-services:4.0.1'
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

RN(react native)プロジェクトがあるフォルダで```android/app/build.gradle```ファイルを開いて下記のコードを追加します。

```js
dependencies {
    implementation project(':react-native-firebase')
    ...
    implementation "com.google.android.gms:play-services-base:16.0.1"
    implementation 'com.google.firebase:firebase-core:16.0.4'
    implementation "com.google.firebase:firebase-ads:16.0.1"
}
```

そして同じファイルの一番下へ下記のコードを追加します。

```js
...
apply plugin: 'com.google.gms.google-services'
com.google.gms.googleservices.GoogleServicesPlugin.config.disableVersionCheck = true
```

最後に```android/app/src/main/java/com/[app name]/MainApplication.java```ファイルへ下のソースを追加します。

```java
import io.invertase.firebase.RNFirebasePackage;
import io.invertase.firebase.admob.RNFirebaseAdMobPackage;
import io.invertase.firebase.analytics.RNFirebaseAnalyticsPackage;
import com.google.android.gms.ads.MobileAds;

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

## ソース追加
react-native-firebaseの設定は完了しました。今からRN(react native)のソースコードを修正してグーグルアドモブ(Google Admob)が上手く表示されるようにします。

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

上のようにソースコードを追加してRN(react native)プロジェクトを実行したらバナーが上手く表示されることを確認することができます。

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

## 完了
RN(react native)プロジェクトへreact-native-firebaseライブラリを使ってグーグルアドモブ(Google Admob)を適用する方法をみてみました。これでreact-native-firebaseを設定したらアナリティクス(Analytics)は自動に設定されて分析することができます。

グーグルファイアベースコンソル(Google Firebase Console)のメニューで```Analytics``` > ```Dashboard```を押してみたら、分析してることが確認できます。

![react native firebase analytics](/assets/images/category/react-native/react-native-firebase-admob/react-native-firebase-analytics.png)