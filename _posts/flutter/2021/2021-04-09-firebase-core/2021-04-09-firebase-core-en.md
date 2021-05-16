---
layout: 'post'
permalink: '/flutter/firebase/core/'
paginate_path: '/flutter/:num/firebase/core/'
lang: 'en'
categories: 'flutter'
comments: true

title: '[Flutter] Firebase core'
description: Let's see how to use firebase_core to connect Firebase in Flutter
image: '/assets/images/category/flutter/background.png'
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [Blog series](#blog-series)
- [Create Firebase Project](#create-firebase-project)
- [iOS configuration](#ios-configuration)
  - [Change bundle identifier](#change-bundle-identifier)
  - [Configure Firbase iOS project](#configure-firbase-ios-project)
- [Android Configuration](#android-configuration)
  - [Modify Gradle](#modify-gradle)
  - [Firbase 안드로이드 프로젝트 설정](#firbase-안드로이드-프로젝트-설정)
- [Install firebase_core](#install-firebase_core)
- [Initialize Firebase](#initialize-firebase)
- [Completed](#completed)

</div>

## Outline

in this blog post, I will introduce how to use `firebase_core` to connect `Firebase` in Flutter.

- [firebase_core](https://pub.dev/packages/firebase_core){:rel="nofollow noreferrer" target="_blank" }

## Blog series

This blog post is a series. You can see the other posts on the link below.

- [Flutter] Firebase Core
- [[Flutter] Firebase Analytics]({{site.url}}/{{page.categories}}/firebase/analytics/){:target="_blank"}
- [[Flutter] Firebase Crashlytics]({{site.url}}/{{page.categories}}/firebase/crashlytics/){:target="_blank"}

## Create Firebase Project

Next, we need to create a Google Firebase project. Click the link below to go to Google Firebase.

- Google Firebase: [https://firebase.google.com](https://firebase.google.com){:rel="nofollow noreferrer" target="_blank"}

![google firebase](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/google-firebase.jpg)

Click `SIGN IN` button on the right top.

![google firebase after login](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/google-firebase-after-login.jpg)

After login, click `GO TO CONSOLE` to go to Google Firebase Console.

![google firebase console](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/google-firebase-console.jpg)

Click `+ Add project` button to create a new porject on Google Firebase Console.

![google firebase console add project](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/google-firebase-console-add-project.jpg)

On the screen above, insert a project name that you want to use to `Enter your project name`. After inserting, click `Continue` button on the bottom to go to the next step.

![google firebase console add google analytics](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/google-firebase-console-add-google-analytics.jpg)

After inserting the project name, you can see the screen that asks you want to integrate `Google Analytics`. If you don't want to integrate, click the switch to make `Disable` and create Fireabase project.

If you want to integreate Google Analytics, click `Continue` button.

![google firebase console add integrate google analytics](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/google-firebase-console-integrate-google-analytics.jpg)

Select Google Analytics account, and click `Create project` button to create Firebase project.

{% include in-feed-ads.html %}

## iOS configuration

Let's see how to configure `firebase_core` on iOS to use Firebase in Flutter.

### Change bundle identifier

Before creating iOS porject in Firebase, we need to change `Bundle identifier` on iOS. Execute `ios/Runner.xcworkspace` file to open Xcode.

![change ios bundle id](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/ios-change-bundle-id.jpg)

Select the project name on left top and go to the `General`, you can find `Bundle Identifier` on it. Change the Bundle ID for your project.

### Change target SDK version

To use the `firebase_core` package, we need to change the iOS target SDK version. Open the `ios/Podfile` file and modify it like below.

```ruby
# Uncomment this line to define a global platform for your project
platform :ios, '10.0'
```

### Configure Firbase iOS project

When you select the project on Google Fireabse Console, you can see the screen like below.

![google firebase console project](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/google-firebase-console-project.jpg)

Click `iOS` button on the center of the screen to go iOS configuraion.

![google firebase console project ios](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/google-firebase-console-project-ios.jpg)

Insert iOS Bundle ID, and click `Register app` button.

![GoogleService-Info.plist download](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/googleservice-info-plist-download.jpg)

Download `GoogleService-Info.plist` file created by Google Firebase, and drag it to the `Runner/Runner` folder to copy it on Xcode. After adding `GoogleService-Info.plist` file, click `Next` button.

![add Firebase SDK](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/add-firebase-sdk-google-analytics.jpg)

When you see the screen like below, click the `Next` button to go to the next page.

![edit appdelegate.m for firebase](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/edit-appdelegate.jpg)

When you see the screen like below, click the `Next` button to go to the next page.

![connect firebase to app](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/connect-firebase-to-app.jpg)

I juse clicked the `Skip this step` button to skip this part.

{% include in-feed-ads.html %}

## Android Configuration

Next, let's see how to configure Android to use react-native-fireabse.

### Modify Gradle

TO use Firebase in Flutter, we need to modify the `Gradle` file. First, open `android/app/build.gradle` file and add the code below to the bottom of the file.

```js
...
apply plugin: 'com.google.gms.google-services' // <<<<<<<<<<<<< Add this
```

And modify `applicationId` for your project.

```js
// applicationId "com.example.blaboo_app"
applicationId "io.github.dev.yakuza.blaboo"
```

And then, open `android/build.gradle` file and modify it like below.

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

Done! we've ready to use Firebase on Android.

### Firbase 안드로이드 프로젝트 설정

Click `Project Overview` on the top of Google Firebase Console.

![Google Firebase Console Project Overview](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/firebase-project-overview.jpg)

Click `+ Add app` > `Android icon` to go Android project settings.

![Google Firebase Android app register](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/register-android.jpg)

Insert Android Package Name and click `Register app` button.

![Google Firebase google-services.json setting](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/set-google-services-json.jpg)

Copy and paste `google-services.json` to `android/app` folder and click `Next` button. Done. we've ready to use Firebase on Android. Click the `Next` button on all screens after.

![Google Firebase setting on android](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/setting-android.jpg)

{% include in-feed-ads.html %}

## Install firebase_core

To use Firebase in Flutter, we need to install the `firebase_core` package. Execute the command below to install `firebase_core`.

```bash
flutter pub pub add firebase_core
```

## Initialize Firebase

After installing the `firebase_core` pacakge, we need to initialize Firebase by using this pacakge. Open the `main.dart` file and modify it like below to initialize Firebase.

```dart
import 'package:firebase_core/firebase_core.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();

  runApp(MyApp());
}
```

## Completed

Finished! we've prepared the Flutter and Firebase project to use Firebase in Flutter, and seen how to configure the `firebase_core` package. To use the Firebase features, see other blog posts on below.

- [[Flutter] Firebase Analytics]({{site.url}}/{{page.categories}}/firebase/analytics/){:target="_blank"}
- [[Flutter] Firebase Crashlytics]({{site.url}}/{{page.categories}}/firebase/crashlytics/){:target="_blank"}
