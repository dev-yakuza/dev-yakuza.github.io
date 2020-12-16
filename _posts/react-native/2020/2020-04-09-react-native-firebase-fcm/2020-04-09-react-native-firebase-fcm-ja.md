---
layout: 'post'
permalink: '/react-native/react-native-firebase-fcm/'
paginate_path: '/react-native/:num/react-native-firebase-fcm/'
lang: 'ja'
categories: 'react-native'
comments: true

title: react-native-firebase(V5)を使ってPush Message
description: React Nativeでプッシュメッセージを使うため、react-native-firebase(V5)のライブラリを使ってFCM(Firebase Cloud Messaging)を使う方法について説明します。
image: '/assets/images/category/react-native/2020/react-native-firebase-fcm/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [ライブラリインストール](#ライブラリインストール)
- [ライブラリリンク](#ライブラリリンク)
  - [0.60以上](#060以上)
  - [0.59以下](#059以下)
- [Firebaseプロジェクト生成](#firebaseプロジェクト生成)
- [iOS設定](#ios設定)
- [Firbase iOSプロジェクトの設定](#firbase-iosプロジェクトの設定)
  - [権限の設定](#権限の設定)
  - [APNS設定](#apns設定)
- [アンドロイド設定](#アンドロイド設定)
  - [アンドロイドパッケージ名修正](#アンドロイドパッケージ名修正)
- [Firbase アンドロイドプロジェクト設定](#firbase-アンドロイドプロジェクト設定)
- [テスト](#テスト)
- [Javascriptソースコード追加](#javascriptソースコード追加)
  - [iOSテスト](#iosテスト)
  - [アンドロイドテスト](#アンドロイドテスト)
- [完了](#完了)

</div>

## 概要

React Nativeで開発したアプリも普通のアプリなのでプッシュメッセージ(Push Message)を受けることができます。このブログポストではReact Nativeで開発したアプリへプッシュメッセージ(Push Message)を受けるため`react-native-firebase(V5)`ライブラリで`FCM(Firebase Cloud Messaging)`を使う方法について説明します。

- react-native-firebase v5: [https://v5.rnfirebase.io/](https://v5.rnfirebase.io/){:rel="nofollow noreferrer" target="_blank"}
- FCM(Firebase Cloud Messaging): [https://firebase.google.com/docs/cloud-messaging](https://firebase.google.com/docs/cloud-messaging){:rel="nofollow noreferrer" target="_blank"}

## ライブラリインストール

下記のコマンドを使ってreact-native-firebaseのライブラリをインストールします。

```bash
npm install --save react-native-firebase
```

## ライブラリリンク

react-native-firebaseライブラリを使うためにはライブラリをリンクする必要があります。

### 0.60以上

下記のコマンドを使ってreact-native-firebaseライブラリをReact Nativeプロジェクトへ連結します。

```bash
cd ios
pod install
cd ..
```

### 0.59以下

下記のコマンドを使ってreact-native-firebaseライブラリをReact Nativeプロジェクトへ連結します。

```bash
react-native link react-native-firebase
```

{% include in-feed-ads.html %}

## Firebaseプロジェクト生成

次はGoogleのファイアベース(Google Firebase)でプロジェクトを生成する必要があります。下記のリンクを押してGoogleのファイアベース(Google Firebase)へ移動します。

- Googleのファイアベース(Google Firebase): [https://firebase.google.com](https://firebase.google.com){:rel="nofollow noreferrer" target="_blank"}

![google firebase](/assets/images/category/react-native/2020/react-native-firebase-fcm/google-firebase.jpg)

右上の`SIGN IN`ボタンを押してログインします。

![google firebase after login](/assets/images/category/react-native/2020/react-native-firebase-fcm/google-firebase-after-login.jpg)

ログインをしたら、右上の`GO TO CONSOLE`を押してGoogleのファイアベースコンソール(Google Firebase Console)へ移動します。

![google firebase console](/assets/images/category/react-native/2020/react-native-firebase-fcm/google-firebase-console.jpg)

Googleのファイアベースコンソール(Google Firebase Console)で`+ Add project`を押してプロジェクトを追加します。

![google firebase console add project](/assets/images/category/react-native/2020/react-native-firebase-fcm/google-firebase-console-add-project.jpg)

プロジェクトの情報を追加した後、`Create project`ボタンを押してプロジェクトを生成します。

{% include in-feed-ads.html %}

## iOS設定

react-native-firebaseを使うためiOSを設定する方法について説明します。

## Firbase iOSプロジェクトの設定

Googleのファイアベースコンソール(Google Firebase Console)でプロジェクトを選択したら下記のような画面が確認できます。

![google firebase console project](/assets/images/category/react-native/2020/react-native-firebase-fcm/google-firebase-console-project.jpg)

真ん中にある`iOS`ボランを押してiOS設定画面へ移動します。

![google firebase console project ios](/assets/images/category/react-native/2020/react-native-firebase-fcm/google-firebase-console-project-ios.jpg)

開発したアプリのBundle IDを入力して`Register app`ボタンを押します。

![GoogleService-Info.plist download](/assets/images/category/react-native/2020/react-native-firebase-fcm/googleservice-info-plist-download.jpg)

Googleのファイアベース(Google Firebase)が生成した`GoogleService-Info.plist`ファイルをダウンロードして、`info.plist`と同じ位置へ追加します。`GoogleService-Info.plist`ファイル追加が終わったら、`Next`ボタンを押します。

![add Firebase SDK](/assets/images/category/react-native/2020/react-native-firebase-fcm/add-firebase-sdk.jpg)

画面へ表示された形でGoogleファイアベースSDK(Google Firebase SDK)をReact Nativeプロジェクトへ追加します。

React Nativeのバージョンが0.59以下の場合、下記のコマンドを実行します。

```bash
pod init
```

GoogleのファイアベースSDK(Google Firebase SDK)を`./ios/Podfile`へ追加します。

```ruby
target 'blaboo' do
  ...
  pod 'Firebase/Core'
  pod 'Firebase/Analytics' // if you use Analytics
  pod 'Firebase/Messaging'
  ...
end
```

GoogleのファイアベースSDK(Google Firebase SDK)をインストールします。

```bash
pod install
# pod update
```

![edit appdelegate.m for firebase](/assets/images/category/react-native/2020/react-native-firebase-fcm/edit-appdelegate.jpg)

React Nativeプロジェクトの`AppDelegate.m`ファイルへ下記のようにソースコードを追加します。

```js
...
@import Firebase;
#import "RNFirebaseNotifications.h"
...
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
  [FIRApp configure];
  [RNFirebaseNotifications configure];
  ...
  return YES;
}
...
```

GoogleのファイアベースSDK(Google Firebase SDK)を初期化します。

![connect firebase to app](/assets/images/category/react-native/2020/react-native-firebase-fcm/connect-firebase-to-app.jpg)

私はこの部分は`Skip this step`を押してスキップしました。

### 権限の設定

権限の設定をするため`ios/[project name].xcworkspace`ファイルを選択してXcodeを実行します。

![react native firebase analytics](/assets/images/category/react-native/2020/react-native-firebase-fcm/ios-fcm-capability.jpg)

上にある`+Capabilty`を選択して下記の内容を検索して追加します。

- Push Notifications
- Background modes

Background modesを追加するとPush Notificationsと違ってチェックボックスのリストが確認できます。その中で`Remote notifications`を選択します。

{% include in-feed-ads.html %}

### APNS設定

iOSでプッシュメッセージを使うためには`APNS(Apple Push Notification Service)`を設定する必要があります。

macOSで`Keychain Access`を実行します。そして`Keychain Access` > `Certificate Assistant` > `Request a Certificate From a Certificate Authority...`のメニューを選択します。

![APNS(Apple Push Notification Service) - request a certificate from a certicate authority](/assets/images/category/react-native/2020/react-native-firebase-fcm/request_a_certificate_from_a_certicate_authority.jpg)

下記のような画面が出ると`User Email Address`と`Common Name`を入力した後、`Saved to disk`を選択して`Continue`ボタンを選択します。

![APNS(Apple Push Notification Service) - request a certificate from a certicate authority insert information](/assets/images/category/react-native/2020/react-native-firebase-fcm/request_a_certificate_from_a_certicate_authority_insert_information.jpg)

下記のような画面が出ると、保存したいフォルダを指定して`Save`ボタンを押して保存します。

![APNS(Apple Push Notification Service) - request a certificate from a certicate authority save certification](/assets/images/category/react-native/2020/react-native-firebase-fcm/request_a_certificate_from_a_certicate_authority_save_certification.jpg)

その後、[https://developer.apple.com/](https://developer.apple.com/){:rel="nofollow noreferrer" target="_blank"}サイトへ移動します。

![APNS(Apple Push Notification Service) - apple developer site](/assets/images/category/react-native/2020/react-native-firebase-fcm/apple_developer_site.jpg)

その後、右上の`Account`メニューを選択してログインします。下記のような画面が出ると左メニューにある`Certificates, Identifiers & Profiles`を選択します。

![APNS(Apple Push Notification Service) - apple developer site Certificates, Identifiers & Profiles](/assets/images/category/react-native/2020/react-native-firebase-fcm/certificates_identifieers_profiles.jpg)

下記のような画面が見えると`Certificates`メニューを押して、上にある`+`ボタンを押します。

![APNS(Apple Push Notification Service) - Certificates, Identifiers & Profiles Add Certificates](/assets/images/category/react-native/2020/react-native-firebase-fcm/certificates_identifieers_profiles_add_certificates.jpg)

その後、`Create a New Certificate`の画面が出ると、スクロールして下に移動します。下に移動すると下記のように`Service`のセクションにある`Apple Push Notification service SSL (Sandbox & Production)`を見つけれます。その項目を選択して右上の`Continue`ボタンを押して次へ移動します。

![APNS(Apple Push Notification Service) - Certificates, Identifiers & Profiles Apple push notification service](/assets/images/category/react-native/2020/react-native-firebase-fcm/apple_push_notification_service_ssl.jpg)

次と同じ画面が出ると、FCMメッセージを使いたいアプリを選択して、右上の`Continue`ボタンを押して次へ進めます。

![APNS(Apple Push Notification Service) - Certificates, Identifiers & Profiles Apple push notification service](/assets/images/category/react-native/2020/react-native-firebase-fcm/select_app_id.jpg)

次のようにファイルを選択する画面が出ると`Choose File`を選択してKeychainで作ったファイルを選択します。選択したら、右上の`Continue`ボタンを選択します。

![APNS(Apple Push Notification Service) - Certificates, Identifiers & Profiles Apple push notification service](/assets/images/category/react-native/2020/react-native-firebase-fcm/select_app_id.jpg)

次のような画面が出ると、無事に証明書が生成されました。右上の`Download`ボタンを押して、生成した証明書をダウンロードします。

![APNS(Apple Push Notification Service) - Certificates, Identifiers & Profiles Apple push notification service](/assets/images/category/react-native/2020/react-native-firebase-fcm/download_your_certificate.jpg)

このようにダウンロードした証明書を`.p12`の形式で変換する必要があります。ダウンロードした証明書をダブルクリックしてKeychainへ登録します。

![APNS(Apple Push Notification Service) - generate .p12](/assets/images/category/react-native/2020/react-native-firebase-fcm/generate_p12_file.jpg)

登録された証明書をマウスの右クリックした後、`Export "Apple Push Services: package name"...`を選択します。

![APNS(Apple Push Notification Service) - generate .p12 export](/assets/images/category/react-native/2020/react-native-firebase-fcm/generate_p12_file_export.jpg)

上のようにファイルを保存する画面が出ると`File Format`へ`Personal Information Exchange (.p12)`が選択された状態で`Save`を押してファイルを保存します。

![APNS(Apple Push Notification Service) - generate .p12 insert password](/assets/images/category/react-native/2020/react-native-firebase-fcm/generate_p12_file_insert_password.jpg)

p12ファイルを保存するため、上のようにパスワードを入力する必要があります。パスワードを入力したら.p12ファイル形式で保存します。

また、[Firebase Console](https://console.firebase.google.com/){:rel="nofollow noreferrer" target="_blank"}へ移動して、上で作ったプロジェクトを選択します。プロジェクトを選択したら右へ上で作った`iOS`のプロジェクトが確認できます。

![APNS(Apple Push Notification Service) - Firebase Console select ios](/assets/images/category/react-native/2020/react-native-firebase-fcm/firebase_console_select_ios.jpg)

iOSプロジェクトを選択して設定アイコンを押してiOSプロジェクトの設定画面へ移動します。iOSの設定画面の上にある`Cloud Messaging`のメニューを押します。

![APNS(Apple Push Notification Service) - Firebase Console cloud messaging](/assets/images/category/react-native/2020/react-native-firebase-fcm/firebase_console_cloud_messaging.jpg)

下へ`iOS app configuration`のセクションの`APNs certificates`の項目が確認できます。`No development APNs certificate`と`No production APNs certificate`の横にある`Upload`ボタンを押します。

![APNS(Apple Push Notification Service) - Firebase Console upload p12 file](/assets/images/category/react-native/2020/react-native-firebase-fcm/firebase_console_upload_p12_file.jpg)

この画面で上で作った`.p12`ファイルをアップロードして、`.p12`を保存する時使ったパスワードを入力します。

![APNS(Apple Push Notification Service) - Firebase Console finish settings](/assets/images/category/react-native/2020/react-native-firebase-fcm/firebase_console_finish.jpg)

これでAPNS(Apple Push Notification Service)の設定は完了しました。

{% include in-feed-ads.html %}

## アンドロイド設定

今からreact-native-firebaseを使うためアンドロイドを設定する方法について説明します。

### アンドロイドパッケージ名修正

- React Nativeプロジェクトのフォルダで`android/app/BUCK`ファイルを修正

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

- React Nativeプロジェクトフォルダにある`android/app/src/main/AndroidManifest.xml`ファイルを修正

  ```xml
  <manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="package_name">
  ...
  ```

- React Nativeプロジェクトフォルダにある`android/app/src/main/java/com/ProjectName/MainActivity.java`ファイルを修正

  ```java
  package package_name;
  ...
  ```

- React Nativeプロジェクトフォルダにある`android/app/src/main/java/com/ProjectName/MainApplication.java`ファイル修正

  ```java
  package package_name;
  ...
  ```

- React Nativeプロジェクトフォルダにある`android/app/build.gradle`ファイル修正

  ```java
  ...
  defaultConfig {
      applicationId package_name
      ...
  }
  ...
  ```

{% include in-feed-ads.html %}

## Firbase アンドロイドプロジェクト設定

Googleのファイアベースコンソール(Google Firebase Console)の左上の`Project Overview`を選択します。

![Google Firebase Console Project Overview](/assets/images/category/react-native/2020/react-native-firebase-fcm/firebase-project-overview.jpg)

上にある`+ Add app` > `アンドロイドアイコン`を押してアンドロイド(Android)プロジェクト設定へ移動します。

![Google Firebase Android app register](/assets/images/category/react-native/2020/react-native-firebase-fcm/register-android.jpg)

アンドロイドパッケージ名(Android Package Name)を入力して`Register app`を選択します。

![Google Firebase google-services.json setting](/assets/images/category/react-native/2020/react-native-firebase-fcm/set-google-services-json.jpg)

Googleのファイアベース(Google Firebase)が作った`google-services.json`ファイルをReact Nativeプロジェクトの`android/app`フォルダへコピーします。そして、`Next`ボタンを押して次へ進めます。

![Google Firebase setting on android](/assets/images/category/react-native/2020/react-native-firebase-fcm/setting-android.jpg)

React Nativeプロジェクトがあるフォルダへ`android/build.gradle`ファイルを開いて下記のようにコードを追加します。

```js
buildscript {
  repositories {
    google()
    jcenter()
  }
  dependencies {
    classpath("com.android.tools.build:gradle:3.4.2")
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

上のように`repositories`へ`google()`があるか確認して、`jcenter()`より上に宣言されてるか確認します。

React Nativeプロジェクトがあるフォルダで`android/app/build.gradle`ファイルを開いて下記のようにコードを追加します。

```js
dependencies {
    // under 59 version
    // implementation project(':react-native-firebase')
    ...
    implementation 'com.google.android.gms:play-services-base:17.2.1'
    implementation 'com.google.firebase:firebase-core:17.0.0'
    implementation "com.google.firebase:firebase-messaging:20.0.0"
    implementation 'me.leolin:ShortcutBadger:1.1.21@aar'
}
```

そして同じファイルの一番下へ下記のようにコードを追加します。

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

- 0.60以上

react-native-firebaseを使うため`android/app/src/main/java/com/[app name]/MainApplication.java`ファイルを開いて下記のように修正します。

```java
import io.invertase.firebase.RNFirebasePackage;
import io.invertase.firebase.analytics.RNFirebaseAnalyticsPackage;
import io.invertase.firebase.messaging.RNFirebaseMessagingPackage;
import io.invertase.firebase.notifications.RNFirebaseNotificationsPackage;
...
@Override
protected List<ReactPackage> getPackages() {
  @SuppressWarnings("UnnecessaryLocalVariable")
  List<ReactPackage> packages = new PackageList(this).getPackages();
  // Packages that cannot be autolinked yet can be added manually here, for example:
  // packages.add(new MyReactNativePackage());
  packages.add(new RNFirebaseAnalyticsPackage());
  packages.add(new RNFirebaseMessagingPackage());
  packages.add(new RNFirebaseNotificationsPackage());
  return packages;
}
...
```

- 0.59以下

react-native-firebaseを使うため`android/app/src/main/java/com/[app name]/MainApplication.java`ファイルを開いて下記のように修正します。

```java
import io.invertase.firebase.RNFirebasePackage;
import io.invertase.firebase.analytics.RNFirebaseAnalyticsPackage;
import io.invertase.firebase.messaging.RNFirebaseMessagingPackage;
...

@Override
protected List<ReactPackage> getPackages() {
  return Arrays.<ReactPackage>asList(
    ...
    new RNFirebasePackage(),
    new RNFirebaseAnalyticsPackage(),
    new RNFirebaseMessagingPackage()
    ...
  );
}
```

アンドロイドでメッセージを受けるため`android/app/src/main/AndroidManifest.xml`ファイルを開いて下記のように修正します。

```xml
<application ...>
...
<service android:name="io.invertase.firebase.messaging.RNFirebaseMessagingService">
  <intent-filter>
    <action android:name="com.google.firebase.MESSAGING_EVENT" />
  </intent-filter>
</service>
<service android:name="io.invertase.firebase.messaging.RNFirebaseBackgroundMessagingService" />
...
</application>
```

アンドロイドスタジオ(Android Studio)を開いて`Gradle Sync`をします。

{% include in-feed-ads.html %}

## テスト

FCMの設定が上手くできたかテストしてみましょう。

## Javascriptソースコード追加

テストをするためにはFCM Tokenが必要です。このトークンを取得するためにはJavascriptを利用しなきゃならないです。ここで紹介してるソースコードは実際プロジェクトでも使えます。

FCMを使うため`./src/Components/FCMContainer/index.tsx`ファイルを開いて下記のように修正します。

```js
import React, { useEffect } from 'react';
import { Platform, Alert } from 'react-native';
import firebase from 'react-native-firebase';
import DeviceInfo from 'react-native-device-info';
import AsyncStorage from '@react-native-community/async-storage';
import Axios from 'axios';

import Config from '~/Config';

interface Props {
  children: JSX.Element;
  onNotificationOpened?: (data: { [key: string]: string }) => any;
}

const FCMContainer = ({ children, onNotificationOpened }: Props): JSX.Element => {
  const CHANNEL_ID = 'io.github.dev.yakuza.poma';
  const APP_NAME = 'POMA';
  const DESCRIPTION = 'POMA channel';

  let _onTokenRefreshListener: any = undefined;
  let _notificationDisplayedListener: any = undefined;
  let _notificationListener: any = undefined;
  let _notificationOpenedListener: any = undefined;

  const _registerMessageListener = (): void => {
    firebase
      .notifications()
      .getInitialNotification()
      .then((notificationOpen) => {
        if (
          onNotificationOpened &&
          typeof onNotificationOpened === 'function' &&
          notificationOpen &&
          notificationOpen.notification &&
          notificationOpen.notification.data &&
          notificationOpen.notification.data.notifications_id
        ) {
          onNotificationOpened(notificationOpen.notification.data);
        }
      });

    const channel = new firebase.notifications.Android.Channel(
      CHANNEL_ID,
      APP_NAME,
      firebase.notifications.Android.Importance.Max,
    ).setDescription(DESCRIPTION);
    firebase.notifications().android.createChannel(channel);

    _notificationListener = firebase.notifications().onNotification((notification) => {
      // Process your notification as required
      notification.android.setPriority(firebase.notifications.Android.Priority.Max);
      notification.android.setChannelId(CHANNEL_ID);

      firebase.notifications().displayNotification(notification);
    });
    _notificationDisplayedListener = firebase.notifications().onNotificationDisplayed(() => {});
    _notificationOpenedListener = firebase
      .notifications()
      .onNotificationOpened((notificationOpen) => {
        if (onNotificationOpened && typeof onNotificationOpened === 'function') {
          onNotificationOpened(notificationOpen.notification.data);
        }
      });
  };

  const _registerToken = async (fcmToken: string): Promise<void> => {
    console.log(fcmToken);
    // try {
    //   const deviceUniqueId = DeviceInfo.getUniqueId();
    //   const token = await AsyncStorage.getItem('token');
    //   await Axios.post(
    //     `URL`,
    //     {
    //       token: fcmToken,
    //       device_unique_id,
    //     },
    //     {
    //       headers: { Authorization: 'Bearer ' + token },
    //     },
    //   );
    // } catch (error) {
    //   console.log('ERROR: _registerToken');
    //   console.log(error.response.data);
    // }
  };

  const _registerTokenRefreshListener = (): void => {
    if (_onTokenRefreshListener) {
      _onTokenRefreshListener();
      _onTokenRefreshListener = undefined;
    }

    _onTokenRefreshListener = firebase.messaging().onTokenRefresh((fcmToken) => {
      // Process your token as required
      _registerToken(fcmToken);
    });
  };
  const _updateTokenToServer = async (): Promise<void> => {
    try {
      const fcmToken = await firebase.messaging().getToken();
      _registerMessageListener();
      _registerToken(fcmToken);
    } catch (error) {
      console.log('ERROR: _updateTokenToServer');
      console.log(error);
    }
  };

  const _requestPermission = async (): Promise<void> => {
    try {
      // User has authorised
      await firebase.messaging().requestPermission();
      await _updateTokenToServer();
    } catch (error) {
      // User has rejected permissions
      Alert.alert("you can't handle push notification");
    }
  };

  const _checkPermission = async (): Promise<void> => {
    try {
      const enabled = await firebase.messaging().hasPermission();
      if (enabled) {
        // user has permissions
        _updateTokenToServer();
        _registerTokenRefreshListener();
      } else {
        // user doesn't have permission
        _requestPermission();
      }
    } catch (error) {
      console.log('ERROR: _checkPermission', error);
      console.log(error);
    }
  };

  useEffect(() => {
    _checkPermission();
    return (): void => {
      if (_onTokenRefreshListener) {
        _onTokenRefreshListener();
        _onTokenRefreshListener = undefined;
      }
      if (_notificationDisplayedListener) {
        _notificationDisplayedListener();
        _notificationDisplayedListener = undefined;
      }
      if (_notificationListener) {
        _notificationListener();
        _notificationListener = undefined;
      }
      if (_notificationOpenedListener) {
        _notificationOpenedListener();
        _notificationOpenedListener = undefined;
      }
    };
  }, []);

  if (Platform.OS === 'ios') {
    firebase.notifications().setBadge(0);
  }

  return children;
};

export default FCMContainer;
```

上のソースコードで皆さんの`Channel ID`と`App Name`、`Description`で修正します。

```js
const CHANNEL_ID = 'io.github.dev.yakuza.poma';
const APP_NAME = 'POMA';
const DESCRIPTION = 'POMA channel';
```

また、テストのためFCM Tokenをローグで表示しますが、

```js
const _registerToken = async (fcmToken: string): Promise<void> => {
  console.log(fcmToken);
  // try {
  //   const deviceUniqueId = DeviceInfo.getUniqueId();
  //   const token = await AsyncStorage.getItem('token');
  //   await Axios.post(
  //     `URL`,
  //     {
  //       token: fcmToken,
  //       device_unique_id,
  //     },
  //     {
  //       headers: { Authorization: 'Bearer ' + token },
  //     },
  //   );
  // } catch (error) {
  //   console.log('ERROR: _registerToken');
  //   console.log(error.response.data);
  // }
};
```

実際使うときは、この部分でサーバと通信してFCM Tokenを保存します。

上のソースコードを使うためには`App.tsx`ファイルを開いて下記のように修正します。

```js
import React from 'react';
import FCMContainer from '~/Component/FCMContainer';

const App = (): JSX.Element => {
  return (
    <FCMContainer>
      ...
    </FCMContainer>
  );
};

export default App;
```

{% include in-feed-ads.html %}

### iOSテスト

iOSでFCMをテストするためには端末が必要です。端末を連結して`Xcode`を実行します。

![iOS FCM test - select device](/assets/images/category/react-native/2020/react-native-firebase-fcm/ios_fcm_test_select_device.jpg)

Xcodeが実行されると左上のメニューで端末を選択して`>`ボタンを押してプロジェクトを実行します。

![iOS FCM test - permission](/assets/images/category/react-native/2020/react-native-firebase-fcm/ios_fcm_test_permission.jpg)

端末でアプリが実行されると下記のようにPush Notificationの権限を許可するか聞いてくれる画面がでます。`Allow`ボタンを押して許可します。

![iOS FCM test - get token](/assets/images/category/react-native/2020/react-native-firebase-fcm/ios_fcm_test_get_token.jpg)

許可するとコンソールへ上のようにFCM Tokenが出力されます。そのTokenをコピーします。

次は[Firebase Console](https://console.firebase.google.com/){:rel="nofollow noreferrer" target="_blank"}を接続した後、左メニュで`Cloud Messaging`を選択して`Send your first message`ボタンを押します。

![ios FCM test - Firebase console](/assets/images/category/react-native/2020/react-native-firebase-fcm/android_fcm_test_firebase_console.jpg)

次のような画面が出ると`Notification title`と`Notification text`へテストメッセージを作成します。作成が完了されたら、右にある`Send test message`を選択します。

![ios FCM test - insert message](/assets/images/category/react-native/2020/react-native-firebase-fcm/android_fcm_test_insert_message.jpg)

次のような画面が出ると`Add an FCM registration token`に上でコピーしたFCM Tokenを入力して`+`ボタンを選択します。

![ios FCM test - insert token](/assets/images/category/react-native/2020/react-native-firebase-fcm/android_fcm_test_insert_token.jpg)

その後、`Test`ボタンを押してテストメッセージを送信してみます。

![ios FCM test - send message](/assets/images/category/react-native/2020/react-native-firebase-fcm/android_fcm_test_send_message.jpg)

そしたら下記のように端末へメッセージがうまく受信されることが確認できます。

![ios FCM test - receive message](/assets/images/category/react-native/2020/react-native-firebase-fcm/ios_fcm_test_receive_message.jpg)

{% include in-feed-ads.html %}

### アンドロイドテスト

アンドロイドでFCMをテストするため下記のコマンドを使ってアンドロイド実行します。

```bash
npm run android
```

実行が完了されたら、下記のようにコンソールへFCM Tokenに出力されることが確認できます。そのキーをコピーします。

![Android FCM test - FCM token](/assets/images/category/react-native/2020/react-native-firebase-fcm/android_fcm_test_fcm_token.jpg)

次は[Firebase Console](https://console.firebase.google.com/){:rel="nofollow noreferrer" target="_blank"}へ移動して、左メニューで`Cloud Messaging`を選択して`Send your first message`ボタンを押します。

![Android FCM test - Firebase console](/assets/images/category/react-native/2020/react-native-firebase-fcm/android_fcm_test_firebase_console.jpg)

次のような画面が出ると`Notification title`と`Notification text`にテストメッセージを作成します。作成が終わったら、右にある`Send test message`ボタンを押します。

![Android FCM test - insert message](/assets/images/category/react-native/2020/react-native-firebase-fcm/android_fcm_test_insert_message.jpg)

次のような画面が出ると`Add an FCM registration token`へ上でコピーしたFCM Tokenを入力して、`+` ボタンを押します。

![Android FCM test - insert token](/assets/images/category/react-native/2020/react-native-firebase-fcm/android_fcm_test_insert_token.jpg)

その後、`Test`ボタンを押してテストメッセージを送信します。

![Android FCM test - send message](/assets/images/category/react-native/2020/react-native-firebase-fcm/android_fcm_test_send_message.jpg)

そしたら下記のようにメッセージが受信できることが確認できます。

![Android FCM test - receive message](/assets/images/category/react-native/2020/react-native-firebase-fcm/android_fcm_test_receive_message.jpg)

## 完了

React Nativeプロジェクトでreact-native-firebaseライブラリを使ってFCMメッセージを受ける方法について見てみました。Javascriptから取得したFCM Tokenをサーバに保存して、そのTokenを使ってメッセージを送信することでPush notificationを実装することができます。
