---
layout: 'post'
permalink: '/flutter/app-name/'
paginate_path: '/flutter/:num/app-name/'
lang: 'ko'
categories: 'flutter'
comments: true

title: '[Flutter] 앱 이름 변경'
description: 이번 블로그 포스트에서는 Flutter로 생성한 앱의 이름을 변경하는 방법에 대해서 살펴보겠습니다.
image: '/assets/images/category/flutter/background.png'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [iOS](#ios)
- [Android](#android)
- [완료](#완료)

</div>

## 개요

Flutter에서는 다음 명령어를 사용하여 프로젝트를 생성합니다.

```bash
flutter create project_name
```

이렇게 생성한 앱은 기본적으로 프로젝트 이름을 앱 이름으로 가지게 됩니다. 이번 블로그 포스트에서는 Flutter로 생성한 앱의 이름을 변경하는 방법에 대해서 살펴보도록 하겠습니다.

## iOS

Flutter로 생성한 프로젝트에서 iOS 앱의 이름을 변경하기 위해 `ios/Runner/Info.plist` 파일을 열고 다음과 같이 수정합니다.

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

`CFBundleName`하단의 `<string/>`안에 이름을 프로젝트명에서 앱의 이름으로 변경합니다.

## Android

Flutter로 생성한 프로젝트에서 안드로이드 앱의 이름을 변경하기 위해 `android/app/src/main/AndroidManifest.xml` 파일을 열고 다음과 같이 수정합니다.

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

`android:label`의 값을 프로젝트명에서 앱의 이름으로 변경합니다.

## 완료

이렇게 iOS와 안드로이드에서 프로젝트명을 앱의 이름으로 변경하면, 앱의 이름이 잘 표시되는 것을 확인할 수 있습니다.
