---
layout: 'post'
permalink: '/flutter/app-name/'
paginate_path: '/flutter/:num/app-name/'
lang: 'ja'
categories: 'flutter'
comments: true

title: '[Flutter] アプリの名前変更'
description: 今回のブログポストではFlutterで生成したアプリの名前を変更する方法について説明します。
image: '/assets/images/category/flutter/background.png'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [iOS](#ios)
- [Android](#android)
- [完了](#完了)

</div>

## 概要

Flutterでは次のコマンドを使ってプロジェクトを生成します。

```bash
flutter create project_name
```

このように生成したアプリは基本的プロジェクト名がアプリの名前になります。今回のブログポストではFlutterで生成したアプリの名前を変更する方法について説明します。

## iOS

Flutterで生成したプロジェクトでiOSアプリの名前を変更するためには`ios/Runner/Info.plist`ファイルを開いて下記のように修正します。

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

`CFBundleName`下にある`<string/>`中のプロジェクト名をアプリの名前に変更します。

## Android

Flutterで生成したプロジェクトでアンドロイドのアプリの名前を変更するため、`android/app/src/main/AndroidManifest.xml`ファイルを開いて下記のように修正します。

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

`android:label`の値をプロジェクト名からアプリの名前に変更します。

## 完了

これでiOSとアンドロイドでプロジェクト名をアプリの名前に変更すると、アプリの名前がうまく表示されることが確認できます。
