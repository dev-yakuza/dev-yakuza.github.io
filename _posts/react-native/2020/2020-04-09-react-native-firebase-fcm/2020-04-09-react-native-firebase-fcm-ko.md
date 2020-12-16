---
layout: 'post'
permalink: '/react-native/react-native-firebase-fcm/'
paginate_path: '/react-native/:num/react-native-firebase-fcm/'
lang: 'ko'
categories: 'react-native'
comments: true

title: react-native-firebase(V5)를 이용한 Push message
description: React Native에서 푸시 메시지를 구현하기 위해, react-native-firebase(V5) 라이브러리를 사용하여 FCM(Firebase Cloud Messaging)을 사용해 봅시다.
image: '/assets/images/category/react-native/2020/react-native-firebase-fcm/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [라이브러리 설치](#라이브러리-설치)
- [라이브러리 링크](#라이브러리-링크)
  - [0.60 이상](#060-이상)
  - [0.59 이하](#059-이하)
- [Firebase 프로젝트 생성](#firebase-프로젝트-생성)
- [iOS 설정](#ios-설정)
- [Firbase iOS 프로젝트 설정](#firbase-ios-프로젝트-설정)
  - [권한 설정](#권한-설정)
  - [APNS 설정](#apns-설정)
- [안드로이드 설정](#안드로이드-설정)
  - [안드로이드 패키지명 수정](#안드로이드-패키지명-수정)
- [Firbase 안드로이드 프로젝트 설정](#firbase-안드로이드-프로젝트-설정)
- [테스트](#테스트)
- [Javascript 소스 코드 추가](#javascript-소스-코드-추가)
  - [iOS 테스트](#ios-테스트)
  - [안드로이드 테스트](#안드로이드-테스트)
- [완료](#완료)

</div>

## 개요

React Native로 개발한 앱도 보통의 앱이므로 푸시 메시지(Push Message)를 받을 수 있습니다. 이번 블로그 포스트에서는 React Native로 개발한 앱에서 푸시 메시지(Push Message)를 받기 위해 `react-native-firebase(V5)` 라이브러리로 `FCM(Firebase Cloud Messaging)`를 사용하는 방법에 대해서 공유합니다.

- react-native-firebase v5: [https://v5.rnfirebase.io/](https://v5.rnfirebase.io/){:rel="nofollow noreferrer" target="_blank"}
- FCM(Firebase Cloud Messaging): [https://firebase.google.com/docs/cloud-messaging](https://firebase.google.com/docs/cloud-messaging){:rel="nofollow noreferrer" target="_blank"}

## 라이브러리 설치

아래에 명령어를 사용하여 react-native-firebase 라이브러리를 설치합니다.

```bash
npm install --save react-native-firebase
```

## 라이브러리 링크

react-native-firebase 라이브러리를 사용하기 위해서는 라이브러리를 링크할 필요가 있습니다.

### 0.60 이상

아래에 명령어를 사용하여 react-native-firebase 라이브러리를 React Native 프로젝트에 연결합니다.

```bash
cd ios
pod install
cd ..
```

### 0.59 이하

아래에 명령어를 사용하여 react-native-firebase 라이브러리를 React Native 프로젝트에 연결합니다.

```bash
react-native link react-native-firebase
```

{% include in-feed-ads.html %}

## Firebase 프로젝트 생성

다음은 구글의 파이어베이스(Google Firebase)에서 프로젝트를 생성할 필요가 있습니다. 아래에 링크를 눌러 구글 파이어베이스(Google Firebase)로 이동합니다.

- 구글 파이어베이스(Google Firebase): [https://firebase.google.com](https://firebase.google.com){:rel="nofollow noreferrer" target="_blank"}

![google firebase](/assets/images/category/react-native/2020/react-native-firebase-fcm/google-firebase.jpg)

오른쪽 위에 `SIGN IN` 버튼을 눌러 로그인합니다.

![google firebase after login](/assets/images/category/react-native/2020/react-native-firebase-fcm/google-firebase-after-login.jpg)

로그인을 했다면 오른쪽 위에 `GO TO CONSOLE`을 눌러 구글 파이어베이스 콘솔(Google Firebase Console)로 이동합니다.

![google firebase console](/assets/images/category/react-native/2020/react-native-firebase-fcm/google-firebase-console.jpg)

구글 파이어베이스 콘솔(Google Firebase Console)에서 `+ Add project`를 눌러 프로젝트를 추가합니다.

![google firebase console add project](/assets/images/category/react-native/2020/react-native-firebase-fcm/google-firebase-console-add-project.jpg)

프로젝트 정보를 추가한 다음 `Create project` 버튼을 눌러 프로젝트를 생성합니다.

{% include in-feed-ads.html %}

## iOS 설정

react-native-firebase를 사용하기 위해 iOS를 설정하는 방법에 대해서 알아봅시다.

## Firbase iOS 프로젝트 설정

구글 파이어베이스 콘솔(Google Firebase Console)에서 프로젝트를 선택하면 다음과 같은 화면이 보입니다.

![google firebase console project](/assets/images/category/react-native/2020/react-native-firebase-fcm/google-firebase-console-project.jpg)

중앙에 `iOS` 버튼을 눌러 iOS 설정 화면으로 이동합니다.

![google firebase console project ios](/assets/images/category/react-native/2020/react-native-firebase-fcm/google-firebase-console-project-ios.jpg)

개발한 앱에 번들 ID(bundle ID)를 입력하고 `Register app` 버튼을 선택합니다.

![GoogleService-Info.plist download](/assets/images/category/react-native/2020/react-native-firebase-fcm/googleservice-info-plist-download.jpg)

구글 파이어베이스(Google Firebase)가 생성한 `GoogleService-Info.plist` 파일을 다운로드하여 `info.plist`와 동일한 위치에 추가합니다. `GoogleService-Info.plist` 파일 추가를 완료했다면 `Next` 버튼을 클릭합니다.

![add Firebase SDK](/assets/images/category/react-native/2020/react-native-firebase-fcm/add-firebase-sdk.jpg)

화면에 표시된 방식으로 구글 파이어베이스 SDK(Google Firebase SDK)를 React Native 프로젝트에 추가합니다.

React Native의 버전이 0.59 이하인 경우 아래에 명령어를 실행합니다.

```bash
pod init
```

구글 파이어베이스 SDK(Google Firebase SDK)를 `./ios/Podfile`에 추가합니다.

```ruby
target 'blaboo' do
  ...
  pod 'Firebase/Core'
  pod 'Firebase/Analytics' // if you use Analytics
  pod 'Firebase/Messaging'
  ...
end
```

구글 파이어베이스 SDK(Google Firebase SDK)를 설치합니다.

```bash
pod install
# pod update
```

![edit appdelegate.m for firebase](/assets/images/category/react-native/2020/react-native-firebase-fcm/edit-appdelegate.jpg)

React Native 프로젝트의 `AppDelegate.m` 파일에 아래와 같이 코드를 추가합니다.

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

구글 파이어베이스 SDK(Google Firebase SDK)를 초기화합니다.

![connect firebase to app](/assets/images/category/react-native/2020/react-native-firebase-fcm/connect-firebase-to-app.jpg)

저는 이 부분에서  `Skip this step`을 눌러 이 부분을 건너 뛰었습니다.

### 권한 설정

권한 설정을 하기 위해 `ios/[project name].xcworkspace` 파일을 선택하여 Xcode를 실행시킵니다.

Xcode가 실행되었다면 왼쪽 메뉴에서 프로젝트를 선택하고 `Signing & Capabilities` 탭으로 이동합니다.

![react native firebase analytics](/assets/images/category/react-native/2020/react-native-firebase-fcm/ios-fcm-capability.jpg)

상단에 `+Capabilty`를 선택하고 아래에 내용을 검색하여 추가합니다.

- Push Notifications
- Background modes

Background modes를 추가하면 Push Notifications과 달리 체크박스 리스트를 확인할 수 있습니다. 이중에서 `Remote notifications`을 선택합니다.

{% include in-feed-ads.html %}

### APNS 설정

iOS에서 푸시 메시지를 다루기 위해서는 `APNS(Apple Push Notification Service)`를 설정해야 합니다.

macOS에서 `Keychain Access`를 실행합니다. 그리고 `Keychain Access` > `Certificate Assistant` > `Request a Certificate From a Certificate Authority...` 메뉴를 선택합니다.

![APNS(Apple Push Notification Service) - request a certificate from a certicate authority](/assets/images/category/react-native/2020/react-native-firebase-fcm/request_a_certificate_from_a_certicate_authority.jpg)

아래와 같은 화면이 나오면 `User Email Address`와 `Common Name`을 입력한 후, `Saved to disk`를 선택하고 `Continue` 버튼을 선택합니다.

![APNS(Apple Push Notification Service) - request a certificate from a certicate authority insert information](/assets/images/category/react-native/2020/react-native-firebase-fcm/request_a_certificate_from_a_certicate_authority_insert_information.jpg)

아래와 같은 화면이 나오면, 원하는 폴더를 지정하고 `Save` 버튼을 눌러 저장합니다.

![APNS(Apple Push Notification Service) - request a certificate from a certicate authority save certification](/assets/images/category/react-native/2020/react-native-firebase-fcm/request_a_certificate_from_a_certicate_authority_save_certification.jpg)

그 다음 [https://developer.apple.com/](https://developer.apple.com/){:rel="nofollow noreferrer" target="_blank"} 사이트로 이동합니다.

![APNS(Apple Push Notification Service) - apple developer site](/assets/images/category/react-native/2020/react-native-firebase-fcm/apple_developer_site.jpg)

그런 다음 오른쪽 상단의 `Account` 메뉴를 선택하고 로그인합니다. 아래와 같은 화면이 보이면 왼쪽 메뉴에서 `Certificates, Identifiers & Profiles` 선택합니다.

![APNS(Apple Push Notification Service) - apple developer site Certificates, Identifiers & Profiles](/assets/images/category/react-native/2020/react-native-firebase-fcm/certificates_identifieers_profiles.jpg)

아래에 그림과 같은 화면이 보이면, `Certificates` 메뉴를 누르고, 상단에 있는 `+` 버튼을 선택합니다.

![APNS(Apple Push Notification Service) - Certificates, Identifiers & Profiles Add Certificates](/assets/images/category/react-native/2020/react-native-firebase-fcm/certificates_identifieers_profiles_add_certificates.jpg)

그 다음 `Create a New Certificate` 화면이 나오면, 스크롤하여 하단으로 이동합니다. 하단으로 이동하면 아래와 같이 `Service` 항목에서 `Apple Push Notification service SSL (Sandbox & Production)`을 찾을 수 있습니다. 해당 항목을 선택하고 오른쪽 상단의 `Continue` 버튼을 눌러 다음으로 이동합니다.

![APNS(Apple Push Notification Service) - Certificates, Identifiers & Profiles Apple push notification service](/assets/images/category/react-native/2020/react-native-firebase-fcm/apple_push_notification_service_ssl.jpg)

다음과 같은 화면이 나오면, FCM 메세지를 적용하고자 하는 앱을 선택하고, 오른쪽 상단의 `Continue` 버튼을 눌러 다음으로 진행합니다.

![APNS(Apple Push Notification Service) - Certificates, Identifiers & Profiles Apple push notification service](/assets/images/category/react-native/2020/react-native-firebase-fcm/select_app_id.jpg)

다음과 같이 파일을 선택하는 화면이 나오면 `Choose File`을 선택하고 Keychain을 통해 만든 파일을 선택합니다. 선택을 완료하였다면, 오른쪽 상단의 `Continue` 버튼을 선택합니다.

![APNS(Apple Push Notification Service) - Certificates, Identifiers & Profiles Apple push notification service](/assets/images/category/react-native/2020/react-native-firebase-fcm/select_app_id.jpg)

다음과 같은 화면이 나왔다면, 무사히 증명서가 생성이 되었습니다. 오른쪽 상단의 `Download` 버튼을 눌러, 생성한 증명서를 다운로드 합니다.

![APNS(Apple Push Notification Service) - Certificates, Identifiers & Profiles Apple push notification service](/assets/images/category/react-native/2020/react-native-firebase-fcm/download_your_certificate.jpg)

이렇게 다운로드한 증명서를 `.p12` 형식으로 변환할 필요가 있습니다. 다운로드 받은 증명서를 더블 클릭하여 Keychain에 등록합니다.

![APNS(Apple Push Notification Service) - generate .p12](/assets/images/category/react-native/2020/react-native-firebase-fcm/generate_p12_file.jpg)

등록된 증명서를 마우스 오른쪽 클릭을 한 다음 `Export "Apple Push Services: package name"...`을 선택합니다.

![APNS(Apple Push Notification Service) - generate .p12 export](/assets/images/category/react-native/2020/react-native-firebase-fcm/generate_p12_file_export.jpg)

위와 같이 파일 저장 화면이 나오면 `File Format`이 `Personal Information Exchange (.p12)`가 선택된 상태에서 `Save`를 눌러 파일을 저장합니다.

![APNS(Apple Push Notification Service) - generate .p12 insert password](/assets/images/category/react-native/2020/react-native-firebase-fcm/generate_p12_file_insert_password.jpg)

p12 파일을 저장하기 위해서는 위와 같이 암호를 입력할 필요가 있습니다. 암호를 입력하여 증명서를 .p12 파일 형식으로 저장합니다.

이제 다시 [Firebase Console](https://console.firebase.google.com/){:rel="nofollow noreferrer" target="_blank"}에 접속한 후, 위에서 만든 프로젝트를 선택합니다. 프로젝트를 선택하면 오른쪽에 앞에서 만든 `iOS` 프로젝트를 확인할 수 있습니다.

![APNS(Apple Push Notification Service) - Firebase Console select ios](/assets/images/category/react-native/2020/react-native-firebase-fcm/firebase_console_select_ios.jpg)

iOS 프로젝트를 선택하고 설정 아이콘을 눌러 iOS 프로젝트 설정 화면으로 이동합니다. iOS 설정화면 상단의 `Cloud Messaging` 메뉴를 선택합니다.

![APNS(Apple Push Notification Service) - Firebase Console cloud messaging](/assets/images/category/react-native/2020/react-native-firebase-fcm/firebase_console_cloud_messaging.jpg)

하단에 `iOS app configuration` 섹션의 `APNs certificates` 항목을 확인할 수 있습니다. `No development APNs certificate`와 `No production APNs certificate` 옆에 `Upload` 버튼을 눌러줍니다.

![APNS(Apple Push Notification Service) - Firebase Console upload p12 file](/assets/images/category/react-native/2020/react-native-firebase-fcm/firebase_console_upload_p12_file.jpg)

이 화면에서 위에서 만든 `.p12` 파일을 업로드하고, `.p12` 파일을 저장할 때 사용한 암호를 입력합니다.

![APNS(Apple Push Notification Service) - Firebase Console finish settings](/assets/images/category/react-native/2020/react-native-firebase-fcm/firebase_console_finish.jpg)

이제 APNS(Apple Push Notification Service) 설정을 모두 완료하였습니다.

{% include in-feed-ads.html %}

## 안드로이드 설정

이제 react-native-firebase를 사용하기 위해 안드로이드를 설정하는 방법에 대해서 알아봅시다.

### 안드로이드 패키지명 수정

- React Native 프로젝트 폴더에서 `android/app/BUCK` 파일 수정

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

- React Native 프로젝트 폴더에서 `android/app/src/main/AndroidManifest.xml` 파일 수정

  ```xml
  <manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="package_name">
  ...
  ```

- React Native 프로젝트 폴더에서 `android/app/src/main/java/com/ProjectName/MainActivity.java` 파일 수정

  ```java
  package package_name;
  ...
  ```

- React Native 프로젝트 폴더에서 `android/app/src/main/java/com/ProjectName/MainApplication.java` 파일 수정

  ```java
  package package_name;
  ...
  ```

- React Native 프로젝트 폴더에서 `android/app/build.gradle` 파일 수정

  ```java
  ...
  defaultConfig {
      applicationId package_name
      ...
  }
  ...
  ```

{% include in-feed-ads.html %}

## Firbase 안드로이드 프로젝트 설정

구글 파이어베이스 콘솔(Google Firebase Console)에서 왼쪽 상단의 `Project Overview`를 선택합니다.

![Google Firebase Console Project Overview](/assets/images/category/react-native/2020/react-native-firebase-fcm/firebase-project-overview.jpg)

상단에 `+ Add app` > `안드로이드(Android) 아이콘`을 눌러 안드로이드(Android) 프로젝트 설정으로 이동합니다.

![Google Firebase Android app register](/assets/images/category/react-native/2020/react-native-firebase-fcm/register-android.jpg)

안드로이드 패키지명(Android Package Name)을 입력하고 `Register app`을 선택합니다.

![Google Firebase google-services.json setting](/assets/images/category/react-native/2020/react-native-firebase-fcm/set-google-services-json.jpg)

구글 파이어베이스(Google Firebase)가 만든 `google-services.json` 파일을 React Native 프로젝트의 `android/app` 폴더에 복사합니다. 그리고 `Next`버튼을 눌러 다음 단계로 진행합니다.

![Google Firebase setting on android](/assets/images/category/react-native/2020/react-native-firebase-fcm/setting-android.jpg)

React Native 프로젝트가 있는 폴더에서 `android/build.gradle` 파일을 열고 아래에 코드를 추가합니다.

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

위와 같이 `repositories`에 `google()`이 포함되어 있어야 하며, `jcenter()`보다 위에 선언되어 있어야 됩니다.

React Native 프로젝트가 있는 폴더에서 `android/app/build.gradle` 파일을 열고 아래에 코드를 추가합니다.

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

그리고 동일한 파일 제일 하단에 아래에 코드를 추가합니다.

```js
...
apply plugin: 'com.google.gms.google-services'
```

다음은 `./android/build.gradle` 파일을 열고 아래와 같이 수정합니다.

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

- 0.60 이상

react-native-firebase를 적용하기 위해 `android/app/src/main/java/com/[app name]/MainApplication.java` 파일에 아래와 같이 소스를 추가합니다.

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

- 0.59 이하

react-native-firebase를 적용하기 위해 `android/app/src/main/java/com/[app name]/MainApplication.java` 파일에 아래와 같이 소스를 추가합니다.

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

안드로이드에서 메세지를 수신하기 위해 `android/app/src/main/AndroidManifest.xml` 파일을 열고 다음과 같이 수정합니다.

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

안드로이드 스튜디오(Android Studio)를 열면 `Gradle Sync`를 해줍니다.

{% include in-feed-ads.html %}

## 테스트

이제 FCM이 잘 설정되었는지 테스트해 봅시다.

## Javascript 소스 코드 추가

테스트를 위해서는 FCM Token이 필요합니다. 이 토큰을 얻기 위해서는 Javascript를 이용해야 합니다. 여기서 소개하는 소스코드는 실제 프로젝트에서도 사용이 가능합니다.

FCM을 사용하기 위해서 `./src/Components/FCMContainer/index.tsx` 파일을 열고 아래와 같이 수정합니다.

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

위에 소스코드에서 여러분의 `Channel ID`와 `App Name`, `Description`를 적용하시기 바랍니다.

```js
const CHANNEL_ID = 'io.github.dev.yakuza.poma';
const APP_NAME = 'POMA';
const DESCRIPTION = 'POMA channel';
```

또한, 테스트를 위해 FCM Token을 로그로 표시했지만,

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

실제 사용할 때는, 이 부분을 서버와 통신하여 FCM Token을 저장하도록 해야합니다.

위에 소스코드를 사용하기 위해서는 `App.tsx` 파일을 열고 아래와 같이 수정합니다.

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

### iOS 테스트

iOS에서 FCM을 테스트하기 위해서는 단말기가 필요합니다. 단말기를 연결하고 `Xcode`를 실행합니다.

![iOS FCM test - select device](/assets/images/category/react-native/2020/react-native-firebase-fcm/ios_fcm_test_select_device.jpg)

Xcode가 실행되면 왼쪽 상단에 연결된 단말기를 선택하고 `>` 버튼을 눌러 프로젝트를 실행합니다.

![iOS FCM test - permission](/assets/images/category/react-native/2020/react-native-firebase-fcm/ios_fcm_test_permission.jpg)

단말기에서 앱이 실행되면 위와 같이 Push Notification 권한을 허용할지 여부를 물어보는 화면이 나옵니다. `Allow` 버튼을 눌러 허용합니다.

![iOS FCM test - get token](/assets/images/category/react-native/2020/react-native-firebase-fcm/ios_fcm_test_get_token.jpg)

허용을 하고나면 콘솔에 위와 같이 FCM Token이 출력되는 것을 확인할 수 있습니다. 해당 Token 키를 복사합니다.

이제 [Firebase Console](https://console.firebase.google.com/){:rel="nofollow noreferrer" target="_blank"}을 접속한 후, 왼쪽 메뉴에서 `Cloud Messaging`을 선택하고 `Send your first message` 버튼을 선택합니다.

![ios FCM test - Firebase console](/assets/images/category/react-native/2020/react-native-firebase-fcm/android_fcm_test_firebase_console.jpg)

다음과 같은 화면이 나오면 `Notification title`과 `Notification text`에 테스트 메시지를 작성합니다. 작성을 완료하였다면, 오른쪽에 있는 `Send test message`를 선택합니다.

![ios FCM test - insert message](/assets/images/category/react-native/2020/react-native-firebase-fcm/android_fcm_test_insert_message.jpg)

다음과 같은 화면이 나오면 `Add an FCM registration token`에 위에서 복사한 FCM Token을 입력하고 `+` 버튼을 선택합니다.

![ios FCM test - insert token](/assets/images/category/react-native/2020/react-native-firebase-fcm/android_fcm_test_insert_token.jpg)

그런 다음 `Test` 버튼을 눌러 테스트 메시지를 발송해 봅니다.

![ios FCM test - send message](/assets/images/category/react-native/2020/react-native-firebase-fcm/android_fcm_test_send_message.jpg)

그러면 아래와 같이 단말기에서 메시지가 잘 수신 되는 것을 확인할 수 있습니다.

![ios FCM test - receive message](/assets/images/category/react-native/2020/react-native-firebase-fcm/ios_fcm_test_receive_message.jpg)

{% include in-feed-ads.html %}

### 안드로이드 테스트

안드로이드에서 FCM을 테스트하기 위해 아래에 명령어를 사용하여 안드로이드를 실행합니다.

```bash
npm run android
```

실행이 완료되면, 아래와 같이 콘솔에 FCM Token이 출력되는 것을 확인할 수 있습니다. 해당 키를 복사합니다.

![Android FCM test - FCM token](/assets/images/category/react-native/2020/react-native-firebase-fcm/android_fcm_test_fcm_token.jpg)

이제 [Firebase Console](https://console.firebase.google.com/){:rel="nofollow noreferrer" target="_blank"}을 접속한 후, 왼쪽 메뉴에서 `Cloud Messaging`을 선택하고 `Send your first message` 버튼을 선택합니다.

![Android FCM test - Firebase console](/assets/images/category/react-native/2020/react-native-firebase-fcm/android_fcm_test_firebase_console.jpg)

다음과 같은 화면이 나오면 `Notification title`과 `Notification text`에 테스트 메시지를 작성합니다. 작성을 완료하였다면, 오른쪽에 있는 `Send test message`를 선택합니다.

![Android FCM test - insert message](/assets/images/category/react-native/2020/react-native-firebase-fcm/android_fcm_test_insert_message.jpg)

다음과 같은 화면이 나오면 `Add an FCM registration token`에 위에서 복사한 FCM Token을 입력하고 `+` 버튼을 선택합니다.

![Android FCM test - insert token](/assets/images/category/react-native/2020/react-native-firebase-fcm/android_fcm_test_insert_token.jpg)

그런 다음 `Test` 버튼을 눌러 테스트 메시지를 발송해 봅니다.

![Android FCM test - send message](/assets/images/category/react-native/2020/react-native-firebase-fcm/android_fcm_test_send_message.jpg)

그러면 아래와 같이 메시지가 잘 수신 되는 것을 확인할 수 있습니다.

![Android FCM test - receive message](/assets/images/category/react-native/2020/react-native-firebase-fcm/android_fcm_test_receive_message.jpg)

## 완료

React Native 프로젝트에 react-native-firebase 라이브러리를 사용하여 FCM 메시지를 수신하는 방법에 대해서 알아보았습니다. Javascript에서 얻은 FCM Token을 서버에 저장하고, 해당 Token을 이용하여 메시지를 발송함으로써, Push notification을 구현할 수 있습니다.
