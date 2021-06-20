---
layout: 'post'
permalink: '/flutter/app-icon/'
paginate_path: '/flutter/:num/app-icon/'
lang: 'ko'
categories: 'flutter'
comments: true

title: '[Flutter] 앱 아이콘 변경'
description: 이번 블로그 포스트에서는 Flutter에서 앱 아이콘을 변경하는 방법에 대해서 알아봅시다.
image: '/assets/images/category/flutter/background.png'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [이미지 파일 준비](#이미지-파일-준비)
- [flutter_launcher_icons 설치](#flutter_launcher_icons-설치)
- [앱 아이콘 설정](#앱-아이콘-설정)
- [앱 아이콘 생성](#앱-아이콘-생성)
- [확인](#확인)
- [완료](#완료)

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

다음 명령어를 실행하여, flutter_launcher_icons 패키지를 설치합니다.

```bash
flutter pub add flutter_launcher_icons --dev
```

## 앱 아이콘 설정

이제 앱 아이콘으로 생성할 이미지 파일을 설정할 필요가 있습니다. `pubspec.yaml` 파일을 열고 제일 하단에 다음과 같은 내용을 추가합니다.

```yaml
...
flutter_icons:
  android: "launcher_icon"
  ios: true
  image_path: "assets/app-icon.png"
```

## 앱 아이콘 생성

다음 명령어를 실행하여, flutter_launcher_icons 패키지를 사용하여 앱 이미지 아이콘을 생성합니다.

```bash
flutter pub run flutter_launcher_icons:main
```

## 확인

이제 Flutter 프로젝트를 재실행하면 다음과 같이 앱 아이콘이 잘 변경된 것을 확인할 수 있습니다.

![Flutter - App icon](/assets/images/category/flutter/2021/app-icon/app-icon.jpg)

## 완료

이것으로 Flutter에서 앱 아이콘을 변경하는 방법에 대해서 살펴보았습니다. `flutter_launcher_icons` 패키지를 사용하면 이처럼 간단하게 Flutter 앱의 아이콘을 변경할 수 있습니다.
