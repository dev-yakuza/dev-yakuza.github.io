---
layout: 'post'
permalink: '/react-native/react-native-multidex/'
paginate_path: '/react-native/:num/react-native-multidex/'
lang: 'ja'
categories: 'react-native'
comments: true

title: React NativeでMultidexの設定
description: React NaitveのプロジェクトのアンドロイドへMultidexを設定する方法について説明します。
image: '/assets/images/category/react-native/2020/react-native-multidex/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [Gradle修正](#gradle修正)
- [Javaファイル修正](#javaファイル修正)
- [完了](#完了)

</div>

## 概要

React Nativeでアプリを開発する時、下記のようなエラーが発生する場合があります。

```bash
Cannot fit requested classes in single dex file
```

この問題を解決するためReact NativeプロジェクトへMultidexを設定する必要があります。このブログポストで、React NativeプロジェクトへMultidexを設定する方法について説明します。

## Gradle修正

React NativeプロジェクトのアンドロイドへMultidexを設定するため、`android/app/build.gradle`ファイルを開いて下記のように修正します。

```js
android {
    defaultConfig {
        ...
        versionName "1.0"
        multiDexEnabled true
    }
    ...
}

dependencies {
  def multidex_version = "2.0.1"
  implementation 'androidx.multidex:multidex:$multidex_version'
}
```

## Javaファイル修正

上のようにGradleファイルを修正したら、`MainApplication.java`ファイルを開いて下記のように修正します。

```java
import androidx.multidex.MultiDexApplication;

public class MainApplication extends MultiDexApplication implements ReactApplication {
  ...
}
```

## 完了

これでReact NativeへMultidexを設定する方法について確認しました。このように設定をした後、下記のコマンドでアンドロイドを実行すると問題なく実行されることが確認できます。

```bash
npm run android
```

このブログポストがReact Nativeでアンドロイドプロジェクトを進めている方へ少しでも役に立ったら嬉しいです。
