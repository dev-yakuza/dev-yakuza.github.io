---
layout: 'post'
permalink: '/react-native/react-native-firebase-v6-crashlytics/'
paginate_path: '/react-native/:num/react-native-firebase-v6-crashlytics/'
lang: 'ko'
categories: 'react-native'
comments: true

title: react-native-firebase V6 Crashlytics
description: react-native-firebase(V6)을 사용하여 Firebase의 Crashlytics를 사용하는 방법에 대해서 알아봅시다.
image: '/assets/images/category/react-native/2020/react-native-firebase-v6-crashlytics/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [react-natiev-firebase 설치 및 준비](#react-natiev-firebase-설치-및-준비)
- [라이브러리 설치](#라이브러리-설치)
- [Firebase 프로젝트 설정](#firebase-프로젝트-설정)
- [완료](#완료)

</div>

## 개요

React Native 프로젝트에서 [Firebase](https://firebase.google.com/){:rel="nofollow noreferrer" target="_blank"}의 [Crashlytics](https://firebase.google.com/docs/crashlytics){:rel="nofollow noreferrer" target="_blank"}를 사용하기 위해 `react-native-firebase`를 사용하는 방법에 대해서 알아보려고 합니다.

- react-native-firebase(V6): [https://rnfirebase.io/](https://rnfirebase.io/){:rel="nofollow noreferrer" target="_blank"}

이 블로그는 시리즈로 제작되어있습니다. 다른 내용을 확인하고 싶으신 분들은 아래에 블로그 리스트를 참고하시기 바랍니다.

- [react-native-firebase V6 설치]({{site.url}}/{{page.categories}}/react-native-firebase-v6-installation/){:target="_blank"}
- react-native-firebase V6 Crashlytics
- [react-native-firebase V6 Admob]({{site.url}}/{{page.categories}}/react-native-firebase-v6-admob/){:target="_blank"}

react-native-firebase의 이전 버전(V5)을 사용하는 방법에 대해서는 아래에 블로그 리스트를 참고하시기 바랍니다.

- [Firebase Analytics]({{site.url}}/{{page.categories}}/react-native-firebase-analytics/){:target="_blank"}
- [Firebase Crashlytics]({{site.url}}/{{page.categories}}/firebase-crashlytics/){:target="_blank"}
- [Firebase Admob]({{site.url}}/{{page.categories}}/react-native-firebase-admob/){:target="_blank"}
- [react-native-firebase(V5)를 이용한 Push message]({{site.url}}/{{page.categories}}/react-native-firebase-fcm/){:target="_blank"}

## react-natiev-firebase 설치 및 준비

아래에 블로그를 참고하여 react-native-firebase를 설치하고, Firebase 프로젝트를 생성합니다.

- [react-native-firebase V6 설치]({{site.url}}/{{page.categories}}/react-native-firebase-v6-installation/){:target="_blank"}

## 라이브러리 설치

아래에 명령어를 사용하여 `react-native-firebase`의 `Crashlytics`를 설치합니다.

```bash
npm install --save @react-native-firebase/crashlytics
```

아래에 명령어를 사용하여 iOS 프로젝트에 react-native-firebase의 Crashlytics를 연결합니다.

```bash
cd ios
pod install
```

## Firebase 프로젝트 설정

다음은 구글의 파이어베이스(Google Firebase)에서 프로젝트에 Crashlytics를 설정할 필요가 있습니다. Firebase의 Console로 이동한 후, 왼쪽 메뉴에서 `Crashlytics`를 선택합니다.

![crashlytics add sdk](/assets/images/category/react-native/2020/react-native-firebase-v6-crashlytics/crashlytics-add-sdk.jpg)

상단에 있는 `Add SDK` 버튼을 눌러서 SDK를 추가합니다. 또한 상단에 `Crashlytics` 타이틀 옆에 있는 프로젝트를 선택하여 iOS/안드로이드로 변경 한 후, `Add SDK`를 눌러 iOS, 안드로이드 모두 SDK를 추가해 줍니다.

## 완료

이것으로 Firebase의 Crashlytics를 사용하기 위해, react-native-firebase 라이브러리를 사용하는 방법에 대해서 알아보았습니다.

![crashlytics integration](/assets/images/category/react-native/2020/react-native-firebase-v6-crashlytics/crashlytics-integration.jpg)

react-native-firebase로 Crashlytics를 잘 설정하고, React Native 프로젝트를 잘 실행하였다면, 위와 같은 화면을 확인할 수 있습니다.