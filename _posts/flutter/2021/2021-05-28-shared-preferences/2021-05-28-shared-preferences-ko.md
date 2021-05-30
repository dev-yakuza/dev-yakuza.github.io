---
layout: 'post'
permalink: '/flutter/widget/shared-preferences/'
paginate_path: '/flutter/:num/widget/shared-preferences/'
lang: 'ko'
categories: 'flutter'
comments: true

title: '[Flutter] Shared preferences'
description: 이번 블로그 포스트에서는 Flutter에서 로컬에 간단한 데이터를 저장하기 위해 Shared preferences 패키지를 사용하는 방법에 대해서 알아봅시다.
image: '/assets/images/category/flutter/background.png'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [Shared preferences 패키지 설치](#shared-preferences-패키지-설치)
- [Shared preferences의 사용법](#shared-preferences의-사용법)
  - [데이터 저장](#데이터-저장)
  - [데이터 읽기](#데이터-읽기)
  - [데이터 삭제](#데이터-삭제)
- [유닛 테스트](#유닛-테스트)
- [완료](#완료)

</div>

## 개요

Flutter로 앱을 개발하다보면, 웹의 localStorage나 리액트 네이티브의 AsyncStorage처럼, 사용자의 단말기에 간단하게 데이터를 저장하고 싶을 경우가 생깁니다. 이때, Flutter에서 사용할 수 있는 패키지가 `Shared preferences`입니다.

- [shared_preferences](https://pub.dev/packages/shared_preferences){:rel="nofollow noreferrer" target="_blank"}

Flutter의 공식문서에서도 사용법이 자세히 나와 있으니 참고하시기 바랍니다.

- 공식 문서: [Store key-value data on disk](https://flutter.dev/docs/cookbook/persistence/key-value){:rel="nofollow noreferrer" target="_blank"}

## Shared preferences 패키지 설치

`Shared preferences`는 사용자의 단말기에 `key-value` 형태로 간단하게 데이터를 저장할 수 있도록 도와줍니다. 그럼 Shared preferences를 사용하기 위해, 다음 명령어를 실행하여 패키지를 설치합니다.

```dart
flutter pub add shared_preferences
```

## Shared preferences의 사용법

`Shared preferences`에는 `int`, `double`, `bool`, `string`, 그리고 `List<String>` 데이터를 저장할 수 있습니다. 그럼, `Shared preferences`을 사용해서 데이터의 읽기/쓰기/삭제에 대해서 알아봅시다.

### 데이터 저장

`Shared preferences`를 사용하여 다음과 같이 데이터를 저장할 수 있습니다.

```dart
...
import 'package:shared_preferences/shared_preferences.dart';
...
final prefs = await SharedPreferences.getInstance();
prefs.setInt('counter', 0);
prefs.setDouble('width', 20.5);
prefs.setBool('isAdmin', true);
prefs.setString('userName', 'dev-yakuza');
prefs.setStringList('alphabet', ['a', 'b', 'c', 'd']);
```

### 데이터 읽기

`Shared preferences`를 사용하여 다음과 같이 데이터를 읽을 수 있습니다.

```dart
...
import 'package:shared_preferences/shared_preferences.dart';
...
final prefs = await SharedPreferences.getInstance();
final counter = prefs.getInt('counter') ?? 0;
final width = prefs.getDouble('width') ?? 10.5;
final isAdmin = prefs.getBool('isAdmin') ?? false;
final userName = prefs.getString('userName') ?? '';
final alphabet = prefs.getStringList('alphabet') ?? [];
final data = prefs.get('userInfo') : {};
```

### 데이터 삭제

다음과 같이 `Shared preferences`을 사용하여 저장한 데이터를 삭제할 수 있습니다.

```dart
...
import 'package:shared_preferences/shared_preferences.dart';
...
final prefs = await SharedPreferences.getInstance();
prefs.remove('counter');
```

또는 다음과 같이 모든 데이터를 삭제할 수 있습니다.

```dart
prefs.clear();
```

## 유닛 테스트

`Shared preferences` 패키지를 사용하는 코드를 유닛 테스트(Unit Test)할 때, 다음과 같이 `Shared preferences`가 제공하는 `setMockInitialValues`을 사용하여 데이터를 초기화 할 수 있습니다.

```dart
...
import 'package:shared_preferences/shared_preferences.dart';
...
setUp(() {
  SharedPreferences.setMockInitialValues({});
});
```

## 완료

이것으로 Flutter에서 간단한 데이터를 사용자 단말기에 저장하기 위해 `Shared preferences`를 사용하는 방법에 대해서 알아보았습니다. `Shared preferences` 패키지는 기본적으로 간단한 데이터를 저장하기 위해 설계되었습니다. 따라서 큰 데이터를 저장하기에는 적합하지 않습니다. 단순히 사용자가 선택한 설정 옵션 등을 저장할 때, 사용하시는 것을 추천드립니다.
