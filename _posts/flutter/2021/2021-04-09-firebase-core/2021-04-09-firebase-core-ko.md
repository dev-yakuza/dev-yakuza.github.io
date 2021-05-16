---
layout: 'post'
permalink: '/flutter/firebase/core/'
paginate_path: '/flutter/:num/firebase/core/'
lang: 'ko'
categories: 'flutter'
comments: true

title: '[Flutter] Firebase core'
description: 이번 블로그 포스트에서는 Flutter에서 Firebase를 연동하는 방법에 대해서 알아보겠습니다.
image: '/assets/images/category/flutter/background.png'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [블로그 시리즈](#블로그-시리즈)
- [Firebase 프로젝트 생성](#firebase-프로젝트-생성)
- [iOS 설정](#ios-설정)
  - [Bundle identifier 변경](#bundle-identifier-변경)
  - [타겟 SDK 버전 변경](#타겟-sdk-버전-변경)
  - [Firbase iOS 프로젝트 설정](#firbase-ios-프로젝트-설정)
- [안드로이드 설정](#안드로이드-설정)
  - [Gradle 수정](#gradle-수정)
  - [Firbase 안드로이드 프로젝트 설정](#firbase-안드로이드-프로젝트-설정)
- [firebase_core 설치](#firebase_core-설치)
- [Firebase 초기화](#firebase-초기화)
- [완료](#완료)

</div>

## 개요

이번 블로그 포스트에서는 Flutter에서 `firebase_core`을 사용하여 `Firebase`를 연동하는 방법에 대해서 소개합니다.

- [firebase_core](https://pub.dev/packages/firebase_core){:rel="nofollow noreferrer" target="_blank" }

## 블로그 시리즈

이 블로그는 시리즈로 제작되었습니다. 다음 링크를 통해 다른 블로그 포스트도 확인해 보시기 바랍니다.

- [Flutter] Firebase Core
- [[Flutter] Firebase Analytics]({{site.url}}/{{page.categories}}/firebase/analytics/){:target="_blank"}
- [[Flutter] Firebase Crashlytics]({{site.url}}/{{page.categories}}/firebase/crashlytics/){:target="_blank"}

## Firebase 프로젝트 생성

다음은 구글의 파이어베이스(Google Firebase)에서 프로젝트를 생성할 필요가 있습니다. 아래에 링크를 눌러 구글 파이어베이스(Google Firebase)로 이동합니다.

- 구글 파이어베이스(Google Firebase): [https://firebase.google.com](https://firebase.google.com){:rel="nofollow noreferrer" target="_blank"}

![google firebase](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/google-firebase.jpg)

오른쪽 위에 `SIGN IN` 버튼을 눌러 로그인합니다.

![google firebase after login](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/google-firebase-after-login.jpg)

로그인을 했다면 오른쪽 위에 `GO TO CONSOLE`을 눌러 구글 파이어베이스 콘솔(Google Firebase Console)로 이동합니다.

![google firebase console](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/google-firebase-console.jpg)

구글 파이어베이스 콘솔(Google Firebase Console)에서 `+ Add project`를 눌러 프로젝트를 추가합니다.

![google firebase console add project](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/google-firebase-console-add-project.jpg)

위와 같은 화면에서 `Enter your project name`에 만들고자하는 Firebase 프로젝트 이름을 입력합니다. 입력을 하였다면 하단에 있는 `Continue` 버튼을 눌러 다음으로 진행합니다.

![google firebase console add google analytics](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/google-firebase-console-add-google-analytics.jpg)

프로젝트 명을 입력하였다면, 위와 같이 `Google Analytics`을 연동하는 화면을 볼 수 있습니다. Google Analytics와 연동을 원하지 않는 경우, 왼쪽 하단의 스위치를 선택하여 `Disable`로 변경하고 Firebase 프로젝트를 생성합니다.

Google Analytics와 연동을 원하는 분들은 `Continue`를 눌러 진행합니다.

![google firebase console add integrate google analytics](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/google-firebase-console-integrate-google-analytics.jpg)

Google Analytics 계정을 선택하고, `Create project` 버튼을 눌러 Firebase 프로젝트를 생성합니다.

{% include in-feed-ads.html %}

## iOS 설정

`firebase_core`을 사용해서 Flutter에서 Firebase를 사용하기 위해 iOS를 설정하는 방법에 대해서 알아봅시다.

### Bundle identifier 변경

Firebase에 iOS 프로젝트를 생성하기 전에, iOS의 `Bundle identifier`를 변경할 필요가 있습니다. `ios/Runner.xcworkspace` 파일을 실행하여 Xcode를 실행합니다.

![change ios bundle id](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/ios-change-bundle-id.jpg)

왼쪽 상단의 프로젝트 명을 선택하고 `General` 탭으로 이동하면, 상단에 `Bundle Identifier`를 확인할 수 있습니다. 이 Bundle ID를 자신의 프로젝트에 맞게 변경해 줍니다.

### 타겟 SDK 버전 변경

`firebase_core`을 사용하기 위해서는 iOS의 타겟 SDK 버전을 변경할 필요가 있습니다. `ios/Podfile` 파일을 열고 다음과 같이 수정합니다.

```ruby
# Uncomment this line to define a global platform for your project
platform :ios, '10.0'
```

### Firbase iOS 프로젝트 설정

구글 파이어베이스 콘솔(Google Firebase Console)에서 프로젝트를 선택하면 다음과 같은 화면이 보입니다.

![google firebase console project](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/google-firebase-console-project.jpg)

중앙에 `iOS` 버튼을 눌러 iOS 설정 화면으로 이동합니다.

![google firebase console project ios](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/google-firebase-console-project-ios.jpg)

개발한 앱에 번들 ID(bundle ID)를 입력하고 `Register app` 버튼을 선택합니다.

![GoogleService-Info.plist download](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/googleservice-info-plist-download.jpg)

구글 파이어베이스(Google Firebase)가 생성한 `GoogleService-Info.plist` 파일을 다운로드하여, Xcode를 통해 `Runner/Runner` 폴더에 드래그하여 해당 파일을 추가합니다. `GoogleService-Info.plist` 파일 추가를 완료했다면 `Next` 버튼을 클릭합니다.

![add Firebase SDK](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/add-firebase-sdk-google-analytics.jpg)

이 화면이 표시되면, `Next` 버튼을 클릭하여 다음 화면으로 이동합니다.

![edit appdelegate.m for firebase](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/edit-appdelegate.jpg)

위와 같은 화면에서도 `Next` 버튼을 클릭하여 다음 화면으로 이동합니다.

![connect firebase to app](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/connect-firebase-to-app.jpg)

저는 이 부분에서 `Skip this step`을 눌러 이 부분을 건너 뛰었습니다.

{% include in-feed-ads.html %}

## 안드로이드 설정

`firebase_core`을 사용해서 Flutter에서 Firebase를 사용하기 위해 안드로이드를 설정하는 방법에 대해서 알아봅시다.

### Gradle 수정

Flutter에서 Firebase를 사용하기 위해서는 `Gradle` 파일을 수정할 필요가 있습니다. 우선, `android/app/build.gradle` 파일을 열고 파일 하단을 다음과 같이 수정합니다.

```js
...
apply plugin: 'com.google.gms.google-services' // <<<<<<<<<<<<< Add this
```

그리고 `applicationId`를 해당 프로젝트에 맞게 수정합니다.

```js
// applicationId "com.example.blaboo_app"
applicationId "io.github.dev.yakuza.blaboo"
```

그런 다음, `android/build.gradle` 파일을 열고 다음과 같이 수정합니다.

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

이것으로 안드로이드에 Firebase를 사용할 준비가 되었습니다.

### Firbase 안드로이드 프로젝트 설정

구글 파이어베이스 콘솔(Google Firebase Console)에서 왼쪽 상단의 `Project Overview`를 선택합니다.

![Google Firebase Console Project Overview](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/firebase-project-overview.jpg)

상단에 `+ Add app` > `안드로이드(Android) 아이콘`을 눌러 안드로이드(Android) 프로젝트 설정으로 이동합니다.

![Google Firebase Android app register](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/register-android.jpg)

안드로이드 패키지명(Android Package Name)에 위에서 설정한 `applicationId`을 입력하고 `Register app`을 선택합니다.

![Google Firebase google-services.json setting](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/set-google-services-json.jpg)

구글 파이어베이스(Google Firebase)가 만든 `google-services.json` 파일을 Flutter 프로젝트의 `android/app` 폴더에 복사합니다. 이것으로 안드로이드에서 Firebase를 사용할 준비가 끝났습니다. 이후에 나오는 화면들에서 `Next` 버튼을 눌러 진행합니다.

![Google Firebase setting on android](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/setting-android.jpg)

{% include in-feed-ads.html %}

## firebase_core 설치

Flutter에서 Firebase를 사용하기 위해, `firebase_core` 패키지를 설치할 필요가 있습니다. 다음 명령어를 사용하여 `firebase_core`를 설치합니다.

```bash
flutter pub pub add firebase_core
```

## Firebase 초기화

이렇게 `firebase_core` 패키지를 설치하였다면, 이제 해당 패키지를 사용하여 Firebase를 초기화할 필요가 있습니다. `main.dart` 파일을 열고 다음과 같이 수정하여 Firebase를 초기화해 줍니다.

```dart
import 'package:firebase_core/firebase_core.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();

  runApp(MyApp());
}
```

## 완료

이것으로 Flutter에서 Firebase를 사용하기 위해 Flutter 프로젝트와 Firebase 프로젝트를 준비하고, `firebase_core`를 설정하는 방법에 대해서 알아보았습니다. 이제 Firebase의 다른 기능들을 사용하기 위해, 다른 블로그 포스트를 확인해 주시기 바랍니다.

- [[Flutter] Firebase Analytics]({{site.url}}/{{page.categories}}/firebase/analytics/){:target="_blank"}
- [[Flutter] Firebase Crashlytics]({{site.url}}/{{page.categories}}/firebase/crashlytics/){:target="_blank"}
