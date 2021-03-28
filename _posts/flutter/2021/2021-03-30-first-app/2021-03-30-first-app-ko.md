---
layout: 'post'
permalink: '/flutter/first-app/'
paginate_path: '/flutter/:num/first-app/'
lang: 'ko'
categories: 'flutter'
comments: true

title: '[Flutter] Dart에서 클래스'
description: Flutter로 앱을 개발하기 위해서 Flutter의 개발 언어인 Dart에 대해서 알아봅시다. 이번 블로그 포스트에서는 Dart에서 클래스를 사용하는 방법에 대해서 알아봅니다.
image: '/assets/images/category/flutter/background.jpg'
published: false
---

<div id="contents_list" markdown="1">

## 목차

</div>


## 개요

## 폴더 구조

- pubspec.yaml
  : 프로젝트의 메타 데이터를 정의하고 관리하는 파일
  : 프로젝트의 버전 또는 환경 서드파티 라이브러리나 디펜던시를 관리

- iOS/Android 폴더: 플러터로 개발된 앱을 각 플랫폼에 배포할 때, 필요한 정보들을 가지고 있음
- test 폴더: 테스트 코드를 보관하는 폴더
- lib 폴더: 앱을 개발하기 위해 실제 코딩하는 파일들

## 코딩

- import 'package:flutter/material.dart';

플러터에서 머테리얼 UI로 앱을 개발하기 위한 위젯
무조건 임포트해야한다.
모든 위젯은 이 위젯 위에서 동작한다.

- void main

프로그램의 시작 위치
플러터에서는 runApp을 실행시켜야함.

- runApp
위젯을 파라메터로 전달받아야함.
이 때 커스텀 위젯을 전달해야함.
여기서 전달하는 위젯이 위젯 트리의 최상단에 위치함.
이 위젯은 스크린 레이아웃을 최초로 빌드하는 역할을 함.

- MyFirstWidget()
앱의 레이아웃을 빌드하는 역할을 함. 따라서 Stateless 위젯임
모든 위젯은 또 다른 위젯을 반환하는 build라는 함수를 가지고 있음.
import 'package:flutter/material.dart'의 MaterialApp을 반환하도록 함

- MaterialApp
MaterialApp을 호출할 때에는 특정 파라메터를 지정해야함.
  - title: 앱의 제목
  - theme: 앱의 기본 테마를 지정
    primarySwatch: 앱에서 사용할 색상 견본. 특정 색을 지정하고 해당 색상을 응용해서 앱의 색상을 구성하는 것을 의미
  - home: 앱이 정상적으로 실행되었을 때, 가장 먼저 보여지는 경로, 특정 위젯을 지정해야 함.

## Closing label

여러 위젯들을 나열하면서 코딩을 하는데, 위젯들의 구분을 좀 더 편하게 하기 위해 플러터가 자동으로 위젯의 끝에 생성하는 라벨

{% include in-feed-ads.html %}

## 완료
