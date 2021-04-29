---
layout: 'post'
permalink: '/flutter/splash-screen/'
paginate_path: '/flutter/:num/splash-screen/'
lang: 'en'
categories: 'flutter'
comments: true

title: '[Flutter] 스플래시 스크린 변경'
description: 이번 블로그 포스트에서는 Flutter에서 스플래시 스크린을 변경하는 방법에 대해서 알아봅시다.
image: '/assets/images/category/flutter/background.png'
published: false
---

<div id="contents_list" markdown="1">

## 목차

</div>

## 개요

Flutter를 사용해서 앱을 개발해 보려고 합니다. 이번 블로그 포스트에서는 Flutter에서 스플래시 스크린을 변경하는 방법에 대해서 알아봅니다.

스플래시 스크린을 변경하기 위해서는 안드로이드와 iOS에 맞게 이미지를 생성하고, 각각의 플랫폼에 맞게 스플래시 스크린을 설정해야 합니다.

- [Adding a splash screen to your mobile app](https://flutter.dev/docs/development/ui/advanced/splash-screen){:rel="nofollow noreferrer" target="_blank"}

하지만 `flutter_native_splash` 패키지를 사용하면, 스플래시 스크린을 좀 더 쉽게 변경할 수 있습니다.

- [flutter_native_splash](https://pub.dev/packages/flutter_native_splash){:rel="nofollow noreferrer" target="_blank"}

## 이미지 파일 준비

공식 문서에 이미지 파일에 대한 특별한 조건이 명시되어 있지 않습니다. 저는 다음과 같은 이미지를 사용하였습니다.

- PNG 파일
- 3000px X 3000px 사이즈 이상의 이미지

준비한 파일을 `assets/splash.png`로 저장합니다.

## flutter_native_splash 설치

flutter_native_splash 패키지를 사용하기 위해서는 flutter_native_splash 패키지를 설치할 필요가 있습니다. 다음 명령어를 실행하여 flutter_native_splash 패키지를 설치합니다.

```bash
flutter pub add flutter_native_splash
```

## 스플래시 이미지 설정

이제 스플래시 스크린으로 사용할 이미지 파일을 설정할 필요가 있습니다. `pubspec.yaml` 파일을 열고 다음과 같은 내용을 파일 하단에 추가합니다.

```yaml
...
flutter_native_splash:
  color: "#FFFFFF"
  image: assets/splash.png
  fullscreen: true
```

## flutter_native_splash 패키지 옵션

flutter_native_splash 패키지는 다양한 옵션을 가지고 있습니다

- color: 스플래시 스크린의 배경색
- background_image: 스플래시 스크린의 배경 이미지
- image: 스플래시 스크린의 이미지
- color_dark: 디바이스 설정이 다크 모드일 경우의 배경색
- background_image_dark: 디바이스 설정이 다크 모드일 경우의 배경 이미지
- image_dark: 디바이스 설정이 다크 모드일 경우의 스플래시 스크린 이미지
- android_gravity: 안드로이드에서 스플래시 이미지의 위치를 설정합니다. (bottom, center, center_horizontal, center_vertical, clip_horizontal, clip_vertical, end, fill, fill_horizontal, fill_vertical, left, right, start, top)
- ios_content_mode: iOS에서 스플래시 이미지의 위치를 설정합니다. (scaleToFill, scaleAspectFit, scaleAspectFill, center, top, bottom, left, right, topLeft, topRight, bottomLeft, bottomRight)
- web_image_mode: 웹에서 스플래시 이미지의 위치를 설정합니다. (center, contain, stretch, cover)
- fullscreen: 스플래시 스크린을 전체 화면으로 표시할지 여부(true, false)
- info_plist_files: info.plist 이름을 변경한 경우, 해당 파일을 설정하기 위한 옵션

## 스플래시 이미지 생성

flutter_native_splash 패키지의 옵션을 설정하였다면, 다음 명령어를 실행하여 스플래시 이미지를 생성합니다.

```bash
flutter pub run flutter_native_splash:create
```

{% include in-feed-ads.html %}

## 팁

flutter_native_splash 패키지를 사용하여 스플래시 이미지를 생성하였다면, 더이상 특별한 수정이 스플래시 스크린을 표시할 수 있습니다.

스플래시 스크린을 다음의 팁들과 함께 사용하면 좀 더 유용합니다.

### 초기 데이터

보통 스플래시 스크린을 화면에 표시한 후, 초기 데이터를 가져오곤 합니다. 이때는 다음과 같이 `Future`와 `async-await`를 사용하여 스플래시 스크린이 표시된 상태에서 데이터를 가져올 수 있습니다.

```dart
import 'package:flutter/material.dart';

Future<void> main() async {
  bool data = await fetchData();
  print(data);

  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Home(),
    );
  }
}

Future<bool> fetchData() async {
  bool data = false;

  // Change to API call
  await Future.delayed(Duration(seconds: 3), () {
    data = true;
  });

  return data;
}
...
```

`main` 함수를 `async-await`로 변경한 후, `runApp`을 통해, 앱을 실행하기 전에 데이터를 가져옵니다. 이런 구조를 가지게 되면, 스플래시 스크린이 화면에 표시된 상태에서 데이터를 가져올 수 있습니다.

### 상태바

이 블로그 포스트에서는 `pubspec.yaml`에 `fullscreen: true`을 설정하여 스플래시 스크린을 생성하였습니다. flutter_native_splash의 버그인건지 모르겠지만, iOS에서 앱이 실행된 후, 상태바(Status Bar)가 표시되지 않습니다. 그래서 다음과 같이 코드를 수정하여 상태바를 표시하였습니다.

```dart
...
import 'package:flutter/services.dart';
...
class Home extends StatelessWidget {
  Home() {
    SystemChrome.setEnabledSystemUIOverlays(SystemUiOverlay.values);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Home'),
      ),
      body: Center(
        child: Text('Hello world!'),
      ),
    );
  }
}
```

## 완료

이것으로 Flutter에서 스플래시 스크린을 변경하는 방법에 대해서 살펴보았습니다. `flutter_native_splash` 패키지를 사용하면 이처럼 간단하게 Flutter 앱의 스플래시 스크린을 변경할 수 있습니다.
