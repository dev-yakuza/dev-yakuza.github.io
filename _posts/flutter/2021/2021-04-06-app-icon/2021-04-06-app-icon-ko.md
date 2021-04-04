---
layout: 'post'
permalink: '/flutter/app-icon/'
paginate_path: '/flutter/:num/app-icon/'
lang: 'ko'
categories: 'flutter'
comments: true

title: '[Flutter] 앱 아이콘 변경'
description: Flutter를 이용하여 앱을 개발해 봅시다. 이번 블로그 포스트에서는 Flutter에서 앱 아이콘을 변경하는 방법에 대해서 알아봅시다.
image: '/assets/images/category/flutter/background.jpg'
published: false
---

<div id="contents_list" markdown="1">

## 목차

</div>

## 개요

Flutter를 사용해서 앱을 개발해 보려고 합니다. 이번 블로그 포스트에서는 Flutter에서 앱 아이콘을 변경하는 방법에 대해서 알아봅니다.

앱 아이콘을 변경하기 위해서는 안드로이드와 iOS에 맞게 이미지를 생성하고, 각각의 플랫폼에 맞게 앱 아이콘을 설정해야 합니다. 하지만 `flutter_launcher_icons` 패키지를 사용하면, 앱 아이콘을 좀 더 쉽게 변경할 수 있습니다.

- [flutter_launcher_icons](https://pub.dev/packages/flutter_launcher_icons){:rel="nofollow noreferrer" target="_blank"}

## 이미지 파일 준비

우선 앱 아이콘에 사용할 이미지 파일이 필요합니다. 이미지 파일은 다음의 조건을 만족해야 합니다.

- PNG 파일
- 1024px x 1024px 이상의 크기
- 파일 사이즈는 최대 1024KB

준비한 파일을 `assets/app-icon.png`로 저장합니다.

## flutter_launcher_icons 설치

flutter_launcher_icons 패키지를 사용하기 위해서는 flutter_launcher_icons 패키지를 설치할 필요가 있습니다.

flutter_launcher_icons 패키지를 설치하기 위해 `pubspec.yaml` 파일을 열고 다음과 같이 수정합니다.

```yaml
...
dev_dependencies:
  flutter_launcher_icons: "^0.8.0"
...
```

이렇게 수정하였다면, 다음 명령어를 통해 flutter_launcher_icons 패키지를 설치합니다.

```bash
flutter pub get
```

{% include in-feed-ads.html %}

## 앱 아이콘 설정

이제 앱 아이콘으로 생성할 이미지 파일을 설정할 필요가 있습니다. `pubspec.yaml` 파일을 열고 다음과 같이 수정합니다.

```yaml
...
flutter_icons:
  android: "launcher_icon"
  ios: true
  image_path: "assets/app-icon.png"
```

## 앱 아이콘 생성

flutter_launcher_icons 패키지를 사용하여 앱 이미지 아이콘을 생성하기 위해서는 다음 명령어를 실행할 필요가 있습니다.

```bash
flutter pub run flutter_launcher_icons:main
```

## 확인

이제 Flutter 프로젝트를 재실행하면 다음과 같이 앱 아이콘이 잘 변경된 것을 확인할 수 있습니다.

![Flutter - App icon](/assets/images/category/flutter/2021/app-icon/app-icon.jpg)

## 완료

이것으로 Flutter에서 앱 아이콘을 변경하는 방법에 대해서 살펴보았습니다. `flutter_launcher_icons` 패키지를 사용하면 이처럼 간단하게 Flutter 앱의 아이콘을 변경할 수 있습니다.
