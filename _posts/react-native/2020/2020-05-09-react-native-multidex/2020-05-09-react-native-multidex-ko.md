---
layout: 'post'
permalink: '/react-native/react-native-multidex/'
paginate_path: '/react-native/:num/react-native-multidex/'
lang: 'ko'
categories: 'react-native'
comments: true

title: React Native에 Multidex 설정하기
description: React Naitve 프로젝트에서 안드로이드에 Multidex를 설정하는 방법에 대해서 알아봅시다.
image: '/assets/images/category/react-native/2020/react-native-multidex/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [Gradle 설정](#gradle-설정)
- [Java 파일 수정](#java-파일-수정)
- [완료](#완료)

</div>

## 개요

React Native로 앱을 개발하다보면 아래와 같은 에러를 나올 때가 있습니다.

```bash
Cannot fit requested classes in single dex file
```

이 문제를 해결하기 위해 React Native 프로젝트에 Multidex를 설정할 필요가 있습니다. 그럼 React Native 프로젝트에 Multidex를 설정하는 방법에 대해서 알아봅시다.

## Gradle 설정

React Native 프로젝트의 안드로이드에 Multidex를 설정하기 위해서, `android/app/build.gradle` 파일을 열고 아래와 같이 수정합니다.

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

## Java 파일 수정

위와 같이 Gradle 파일을 수정하였다면, `MainApplication.java` 파일을 열고 아래와 같이 수정합니다.

```java
import androidx.multidex.MultiDexApplication;

public class MainApplication extends MultiDexApplication implements ReactApplication {
  ...
}
```

## 완료

이것으로 React Native에 Multidex를 설정하는 방법에 대해서 알아보았습니다. 이렇게 설정한 후, 아래에 명령어로 안드로이드를 실행하면 문제없이 실행되는 것을 확인할 수 있습니다.

```bash
npm run android
```

이 블로그 포스트가 React Native로 안드로이드 프로젝트를 진행하시는 분들께 조금이라도 도움이 되었으면 좋겠습니다.
