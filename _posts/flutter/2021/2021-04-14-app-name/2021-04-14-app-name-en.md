---
layout: 'post'
permalink: '/flutter/app-name/'
paginate_path: '/flutter/:num/app-name/'
lang: 'en'
categories: 'flutter'
comments: true

title: '[Flutter] Change App Name'
description: In this blog post, I will show you how to change the App name in Flutter.
image: '/assets/images/category/flutter/background.png'
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [iOS](#ios)
- [Android](#android)
- [Completed](#completed)

</div>

## Outline

In Flutter, we create the porject with the command below.

```bash
flutter create project_name
```

When we create the project by the commad above, the project name will be the app name. In this blog post, I will introduce how to change the App name in Flutter.

## iOS

To change the app name on iOS in the Flutter project, open `ios/Runner/Info.plist` file and modify it like below.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
  <dict>
    ...
    <key>CFBundleName</key>
    <string>[APP NAME]</string>
    ...
  </dict>
</plist>
```

Change the project name to the app name in `<string/>` on the bottom of `CFBundleName`.

## Android

To change the project name to the app name on Android in Flutter, open `android/app/src/main/AndroidManifest.xml` file and modify it like below.

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.app">
    <application
        android:label="[APP NAME]"
        android:icon="@mipmap/launcher_icon">
    ...
    </application>
</manifest>
```

Change the project name to the app name in `android:label`.

## Completed

After change the project name to the app name in iOS and Android, you can see the app name is changed well when you execute the app.
