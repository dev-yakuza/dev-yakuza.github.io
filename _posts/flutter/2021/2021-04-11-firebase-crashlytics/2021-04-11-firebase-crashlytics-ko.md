---
layout: 'post'
permalink: '/flutter/firebase/crashlytics/'
paginate_path: '/flutter/:num/firebase/crashlytics/'
lang: 'ko'
categories: 'flutter'
comments: true

title: '[Flutter] Firebase Crashlytics'
description: 이번 블로그 포스트에서는 Flutter에서 Firebase의 Crashlytics를 연동하고 사용하는 방법에 대해서 알아보겠습니다.
image: '/assets/images/category/flutter/background.png'
published: false
---

<div id="contents_list" markdown="1">

## 목차

</div>

## 개요

이번 블로그 포스트에서는 Flutter로 개발한 앱이 강제 종료되었을 때를 인지하기 위해 `Firebase`의 `Crashlytics`를 설정하는 방법에 대해서 소개합니다.

- [firebase_crashlytics](https://pub.dev/packages/firebase_crashlytics){:rel="nofollow noreferrer" target="_blank" }

`Firebase`의 `Crashlytics`를 사용하기 위해 Flutter 프로젝트에 `firebase_crashlytics`을 설정하고 사용하는 방법에 대해서 알아봅시다.

## 블로그 시리즈

이 블로그는 시리즈로 제작되었습니다. 다음 링크를 통해 다른 블로그 포스트도 확인해 보시기 바랍니다.

- [[Flutter] Firebase Core]({{site.url}}/{{page.categories}}/firebase/core/){:target="_blank"}
- [[Flutter] Firebase Analytics]({{site.url}}/{{page.categories}}/firebase/analytics/){:target="_blank"}
- [Flutter] Firebase Crashlytics

## Firebase 프로젝트 생성 및 설정

Flutter에서 Firebase를 사용하기 위해서는 Firebase 프로젝트를 생성하고, `firebase_core` 패키지를 설치할 필요가 있습니다. 아래의 링크를 통해 자세한 내용을 확인하시기 바랍니다.

- [[Flutter] Firebase Core]({{site.url}}/{{page.categories}}/firebase/core/){:target="_blank"}

{% include in-feed-ads.html %}

## Firebase 프로젝트 설정

다음은 구글의 파이어베이스(Google Firebase)에서 프로젝트에 Crashlytics를 설정할 필요가 있습니다. Firebase의 Console로 이동한 후, 왼쪽 메뉴에서 `Crashlytics`를 선택합니다.

![crashlytics add sdk](/assets/images/category/react-native/2020/react-native-firebase-v6-crashlytics/crashlytics-add-sdk.jpg)

상단에 있는 `Add SDK` 버튼을 눌러서 SDK를 추가합니다. 또한 상단에 `Crashlytics` 타이틀 옆에 있는 프로젝트를 선택하여 iOS/안드로이드로 변경한 후, `Add SDK`를 눌러 iOS, 안드로이드 모두 SDK를 추가해 줍니다.

## firebase_crashlytics 설치

Flutter 프로젝트에서 Firebase Crashlytics를 사용하기 위해서는 `firebase_crashlytics` 패키지를 설치할 필요가 있습니다. 다음 명령어를 실행하여 `firebase_crashlytics` 패키지를 설치합니다.

```dart
flutter pub pub add firebase_crashlytics
```

## Gradle 수정

Flutter 프로젝트의 안드로이드에서 Crashlytics를 사용하기 위해서는 `Gradle` 파일을 수정할 필요가 있습니다. 우선, `android/app/build.gradle` 파일을 열고 파일 하단을 다음과 같이 수정합니다.

```js
...
apply plugin: 'com.google.gms.google-services'
apply plugin: 'com.google.firebase.crashlytics' // <<<<<<<<<<<<< Add this
```

그런 다음, `android/build.gradle` 파일을 열고 다음과 같이 수정합니다.

```js
buildscript {
    ...
    dependencies {
        ...
        classpath "org.jetbrains.kotlin:kotlin-gradle-plugin:$kotlin_version"
        classpath 'com.google.gms:google-services:4.3.5'
        classpath 'com.google.firebase:firebase-crashlytics-gradle:2.5.1' // <<<<<<<<<<<<<<<< Add this
    }
}
```

이것으로 Flutter 프로젝트의 안드로이드에서 Crashlytics를 사용할 준비가 되었습니다.

## firebase_crashlytics 사용법

Flutter에서 다음과 같이 `firebase_crashlytics`를 사용하면, 앱이 강제 종료되었을 때, Firebase Crashlytics에 이를 보고할 수 있습니다.

```dart
import 'dart:async';
import 'package:firebase_crashlytics/firebase_crashlytics.dart';

Future<void> main() async {

  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();

  runZonedGuarded(() {
    runApp(MyApp());
  }, FirebaseCrashlytics.instance.recordError);
}
```

`runZonedCuarded`를 사용하여, 앱 실행중 강제 종료시 Firebase Crashlytics에 보고하도록 설정하였습니다.

{% include in-feed-ads.html %}

## 강제 종료 테스트

다음 코드를 사용하여 앱을 강제 종료 시킬 수 있습니다.

```dart
FirebaseCrashlytics.instance.crash();
```

해당 코드를 버튼, 화면 이동 등과 같은 이벤트에 연결을 하고, 앱을 강제 종료 시킵니다. 앱이 강제 종료되었다면, 다시 앱을 실행시켜 Firebase Crashlytics에 보고하도록 합니다.

앱 강제 종료 테스트는 단말기에서 실행해야 하며, 강제 종료후, Firebase Crashlytics에 보고할 수 있도록 꼭 다시 앱을 실행해야 합니다.

이렇게 강제 종료를 통해 Firebase Crashlytics에 보고하였다면, Firebase의 Crashlytics 화면이 다음과 같이 변경된 것을 확인할 수 있습니다.

![crashlytics integration](/assets/images/category/react-native/2020/react-native-firebase-v6-crashlytics/crashlytics-integration.jpg)

## 안드로이드 multiDexEnabled

`firebase_crashlytics`를 설치하고 Flutter 프로젝트를 안드로이드에서 실행했을 때, `Debug Console`에 다음과 같은 에러가 발생하였습니다.

```bash
Note: .pub-cache/hosted/pub.dartlang.org/firebase_core-1.0.4/android/src/main/java/io/flutter/plugins/firebase/core/FlutterFirebaseCorePlugin.java uses or overrides a deprecated API.
Note: Recompile with -Xlint:deprecation for details.
Note: Some input files use or override a deprecated API.
Note: Recompile with -Xlint:deprecation for details.
Note: .pub-cache/hosted/pub.dartlang.org/flutter_tts-3.0.0/android/src/main/java/com/tundralabs/fluttertts/FlutterTtsPlugin.java uses or overrides a deprecated API.
Note: Recompile with -Xlint:deprecation for details.

Note: .pub-cache/hosted/pub.dartlang.org/firebase_crashlytics-2.0.1/android/src/main/java/io/flutter/plugins/firebase/crashlytics/FlutterFirebaseCrashlyticsPlugin.java uses or overrides a deprecated API.
Note: Recompile with -Xlint:deprecation for details.
Note: .pub-cache/hosted/pub.dartlang.org/firebase_analytics-8.0.1/android/src/main/java/io/flutter/plugins/firebaseanalytics/FirebaseAnalyticsPlugin.java uses or overrides a deprecated API.
Note: Recompile with -Xlint:deprecation for details.
Note: .pub-cache/hosted/pub.dartlang.org/firebase_analytics-8.0.1/android/src/main/java/io/flutter/plugins/firebaseanalytics/FirebaseAnalyticsPlugin.java uses unchecked or unsafe operations.
Note: Recompile with -Xlint:unchecked for details.
```

이를 해결하기 위해서는 `multiDexEnabled`을 활성화할 필요가 있습니다. `android/app/build.gradle` 파일을 열고 다음과 같이 수정합니다.

```js
defaultConfig {
    ...
    minSdkVersion 21
    targetSdkVersion 30
    versionCode flutterVersionCode.toInteger()
    versionName flutterVersionName
    multiDexEnabled true // <<<<<<<<<< Add this
}
```

## 완료

이것으로 Flutter에서 Firebase Crashlytics를 사용하기 위해 Flutter 프로젝트에 `firebase_crashlytics`를 설정하는 방법에 대해서 알아보았습니다. 이제 Firebase Crashlytics를 사용하여 개발한 앱의 강제 종료를 분석해 보시기 바랍니다.
