---
layout: 'post'
permalink: '/flutter/firebase/crashlytics/'
paginate_path: '/flutter/:num/firebase/crashlytics/'
lang: 'en'
categories: 'flutter'
comments: true

title: '[Flutter] Firebase Crashlytics'
description: Let's see how to use Firebase Crashlytics in Flutter.
image: '/assets/images/category/flutter/background.png'
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [Blog series](#blog-series)
- [Create and configure Firebase project](#create-and-configure-firebase-project)
- [Configure Firebase project](#configure-firebase-project)
- [Install firebase_crashlytics](#install-firebase_crashlytics)
- [Edit Gradle](#edit-gradle)
- [How to use firebase_crashlytics](#how-to-use-firebase_crashlytics)
- [App crash test](#app-crash-test)
- [Android multiDexEnabled](#android-multidexenabled)
- [Completed](#completed)

</div>

## Outline

In this blog post, I will show you how to configure `Firebase Crashlytics` to detect the app crash in Flutter.

- [firebase_crashlytics](https://pub.dev/packages/firebase_crashlytics){:rel="nofollow noreferrer" target="_blank" }

To use `Firebase Crashlytics`, I will introduce how to configure and use `firebase_crashlytics` in Flutter.

## Blog series

This blog post is a series. You can see the other posts on the link below.

- [[Flutter] Firebase Core]({{site.url}}/{{page.categories}}/firebase/core/){:target="_blank"}
- [[Flutter] Firebase Analytics]({{site.url}}/{{page.categories}}/firebase/analytics/){:target="_blank"}
- [Flutter] Firebase Crashlytics

## Create and configure Firebase project

To use Firebase in Flutter, we need to create Firebase project, and install the `firebase_core` package. See the details on the link below.

- [[Flutter] Firebase Core]({{site.url}}/{{page.categories}}/firebase/core/){:target="_blank"}

{% include in-feed-ads.html %}

## Configure Firebase project

Next, we need to configure Crashlytics in Google Firebase project. After going to the Firebase Console, click the `Crashlytics` menu on the left menu list.

![crashlytics add sdk](/assets/images/category/react-native/2020/react-native-firebase-v6-crashlytics/crashlytics-add-sdk.jpg)

Clic the `Add SDK` button on the top to add SDK. Also, change the iOS/Android project on the side of `Crashlytics` title, and click the `Add SDK` button to add SDK to iOS and Android.

## Install firebase_crashlytics

To use Firebase Crashlytics in Flutter project, we need to install the `firebase_crashlytics` package. Execute the command below to install the `firebase_crashlytics` package.

```dart
flutter pub pub add firebase_crashlytics
```

## Edit Gradle for Android

To use Crashlytics in Android of the Flutter project, we need to modify the `Gradle` file. First, open the `android/app/build.gradle` file and add the code below to the bottom of the file.

```js
...
apply plugin: 'com.google.gms.google-services'
apply plugin: 'com.google.firebase.crashlytics' // <<<<<<<<<<<<< Add this
```

Next, open the `android/build.gradle` file and modify it like below.

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

Done! we're ready to use Crathlytics in Android of the Flutte project.

## Add script on iOS

To use Crashlytics on iOS, we need to add the start script of Crashlytics. To add the Crashlytics script, execute the `./ios/Runner.xcworkspace` file.

![Add crashlytics script to ios](/assets/images/category/flutter/2021/crashlytics/configure_crashlytics_ios.jpg)

After opening Xcode, click the `Runners` on the left top, and click the `Build Phases` tab on the right side. And then, click the `+` button and select the `New Run Script Phase` menu to add `Run Script`.

Lastly, click the added `Run Script`, and add the code below.

```bash
${PODS_ROOT}/FirebaseCrashlytics/run
```

{% include in-feed-ads.html %}

## How to use firebase_crashlytics

If you use the code below to use the `firebase_crashlytics` package in Flutter, when the app is crashed, you can report it to Firebase Crashlytics.

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

We can report the app crash to Firebase Crashlytics by using `runZonedCuarded`.

## App crash test

You can make the app crash forcely by using the code below.

```dart
FirebaseCrashlytics.instance.crash();
```

Add the code to the button tap event, or the screen changed event, and then trigger the event(tap the button) to make the app crashed. After the App crash, open the app again to report the crash to Firebase Crashlytics.

You should test it on the real device, and after the crash, you should open the app again to report it to Firebase Crashlytics.

If you report the app crash via this way to Firebase Crashlytics, you can see the screen like below on Firebase Crashlytics.

![crashlytics error message list](/assets/images/category/flutter/2021/crashlytics/message_list.jpg)

Also, when you click the error message, you can see the test message(`This is a test crash caused by calling .crash() in Dart`) like the below.

![crashlytics error message list](/assets/images/category/flutter/2021/crashlytics/result_test.jpg)

## Android multiDexEnabled

After installing the `firebase_crashlytics` package, when I open the app on Android, I got the error like below on `Debug Console`.

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

To solve this issue, we need to configure `multiDexEnabled`. open the `android/app/build.gradle` file and modify it like below.

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

## Completed

Done! we've seen how to configure the `firebase_crashlytics` package to use Firebase Crashlytics in Flutter project. Now, you can analyze the app crash via Firebase Crashlytics!
