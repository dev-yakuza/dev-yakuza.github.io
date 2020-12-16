---
layout: 'post'
permalink: '/react-native/react-native-firebase-v6-installation/'
paginate_path: '/react-native/:num/react-native-firebase-v6-installation/'
lang: 'en'
categories: 'react-native'
comments: true

title: react-native-firebase V6 installation
description: To use Firebase on React Native, Let's see how to install react-native-firebase(V6).
image: '/assets/images/category/react-native/2020/react-native-firebase-v6-installation/background.jpg'
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [Install library](#install-library)
- [Create Firebase project](#create-firebase-project)
- [iOS configuration](#ios-configuration)
  - [Change Bundle ID](#change-bundle-id)
  - [Configure iOS project on Firbase](#configure-ios-project-on-firbase)
- [Android Configuration](#android-configuration)
  - [Change Android package name](#change-android-package-name)
  - [Configure Android project on Firbase](#configure-android-project-on-firbase)
- [Completed](#completed)

</div>

## Outline

In this blog, we'll see how to install `react-native-firebase` to use [Firebase](https://firebase.google.com/){:rel="nofollow noreferrer" target="_blank"} on React Native project.

- react-native-firebase(V6): [https://rnfirebase.io/](https://rnfirebase.io/){:rel="nofollow noreferrer" target="_blank"}

If you want to know how to use react-native-firebase previous version(V5), see the blog post list below.

- [Firebase Analytics]({{site.url}}/{{page.categories}}/react-native-firebase-analytics/){:target="_blank"}
- [Firebase Crashlytics]({{site.url}}/{{page.categories}}/firebase-crashlytics/){:target="_blank"}
- [Firebase Admob]({{site.url}}/{{page.categories}}/react-native-firebase-admob/){:target="_blank"}
- [Push message via react-native-firebase(V5)]({{site.url}}/{{page.categories}}/react-native-firebase-fcm/){:target="_blank"}

This blog post is a series. If you want to know more, see the blog posts below.

- react-native-firebase V6 installation
- [react-native-firebase V6 Crashlytics]({{site.url}}/{{page.categories}}/react-native-firebase-v6-crashlytics/){:target="_blank"}
- [react-native-firebase V6 Admob]({{site.url}}/{{page.categories}}/react-native-firebase-v6-admob/){:target="_blank"}

## Install library

Execute the command below to install `react-native-firebase`.

```bash
npm install --save @react-native-firebase/app
```

Execute the command below to bind react-native-firebase to iOS.

```bash
cd ios
pod install
```

{% include in-feed-ads.html %}

## Create Firebase project

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

Let's see how to configure iOS to use react-native-firebase.

### Change Bundle ID

Before creating iOS project on Fireabse, we need to change iOS `Bundle ID`. click `ios/[project name].xcworkspace` to execute Xcode.

![change ios bundle id](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/ios-change-bundle-id.jpg)

Select the project name on the left top, and click `General` tab, you can see `Bundle Identifier` on the top of it. Change this Bundle ID to fit your project.

### Configure iOS project on Firbase

When you select the project on Google Fireabse Console, you can see the screen like below.

![google firebase console project](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/google-firebase-console-project.jpg)

Click `iOS` button on the center of the screen to go iOS configuraion.

![google firebase console project ios](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/google-firebase-console-project-ios.jpg)

Insert iOS Bundle ID, and click `Register app` button.

![GoogleService-Info.plist download](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/googleservice-info-plist-download.jpg)

Download `GoogleService-Info.plist` file created by Google Firebase, and add it to the same directory of `info.plist` file. After adding `GoogleService-Info.plist` file, click `Next` button.

![add Firebase SDK](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/add-firebase-sdk-google-analytics.jpg)

We need to add Google Firebase SDK to React Native project like the screen. open `./ios/Podfile` file and modify it like below.

```ruby
target 'blaboo' do
  ...
  pod 'Firebase/Analytics'
  ...
end
```

If you don't use Googe Analytics, yo don't need to modify it like above.

Execute the command below to install Google Firebase SDK.

```bash
pod install
# pod update
```

![edit appdelegate.m for firebase](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/edit-appdelegate.jpg)

Open `AppDelegate.m` file on React Native project, and modify it like below.

```js
...
@import Firebase;

@implementation AppDelegate
...
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
  [FIRApp configure];
  ...
  return YES;
}
...
```

This initializes Google Firebase SDK.

![connect firebase to app](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/connect-firebase-to-app.jpg)

I've skipped this section to click `Skip this step` link.

{% include in-feed-ads.html %}

## Android Configuration

Next, let's see how to configure Android to use react-native-fireabse.

### Change Android package name

- Open `android/app/BUCK` file and moodify Android package name to fit your project.

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

- Open `android/app/src/main/AndroidManifest.xml` file and moodify Android package name.

  ```xml
  <manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="package_name">
  ...
  ```

- Open `android/app/src/main/java/com/ProjectName/MainActivity.java` file and moodify Android package name.

  ```java
  package package_name;
  ...
  ```

- Open `android/app/src/main/java/com/ProjectName/MainApplication.java` file and moodify Android package name.

  ```java
  package package_name;
  ...
  ```

- Open `android/app/build.gradle` file and moodify Android package name.

  ```java
  ...
  defaultConfig {
      applicationId package_name
      ...
  }
  ...
  ```

After chaning the package name like above, we need to change folder structure from `android/app/src/main/java/com/[App Name]/MainActivity.java` to `android/app/src/main/java/[Package Name Folder]/MainActivity.java`.

{% include in-feed-ads.html %}

### Configure Android project on Firbase

Click `Project Overview` on the top of Google Firebase Console.

![Google Firebase Console Project Overview](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/firebase-project-overview.jpg)

Click `+ Add app` > `Android icon` to go Android project settings.

![Google Firebase Android app register](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/register-android.jpg)

Insert Android Package Name and click `Register app` button.

![Google Firebase google-services.json setting](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/set-google-services-json.jpg)

Copy and paste `google-services.json` to `android/app` folder and click `Next` button.

![Google Firebase setting on android](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/setting-android.jpg)

Open `android/build.gradle` file on React Native project and modify it like below.

```js
buildscript {
  repositories {
    google()
    jcenter()
  }
  dependencies {
    classpath("com.android.tools.build:gradle:3.5.2")
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

As above, `google()` should be in `repositories` and above `jcenter()`.

Open `android/app/build.gradle` file on React Native folder, and modify it like below.

```js
dependencies {
    // under 59 version
    // implementation project(':react-native-firebase')
    ...
    implementation 'com.google.firebase:firebase-analytics:17.2.2'
}
```

If you don't use Google Analytics, you don't nedd to modify the file like above. And then, add the source code below on the bottom of the same file.

```js
...
apply plugin: 'com.google.gms.google-services'
```

Next, open `./android/build.gradle` file and modify it like below.

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

## Completed

Done! we've seen how to install `react-native-firebae` to use Firebase on React Native. You can see other features on the links below.

- [react-native-firebase V6 Crashlytics]({{site.url}}/{{page.categories}}/react-native-firebase-v6-crashlytics/){:target="_blank"}
- [react-native-firebase V6 Admob]({{site.url}}/{{page.categories}}/react-native-firebase-v6-admob/){:target="_blank"}
