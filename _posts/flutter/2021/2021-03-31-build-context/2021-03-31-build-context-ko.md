---
layout: 'post'
permalink: '/flutter/build-context/'
paginate_path: '/flutter/:num/build-context/'
lang: 'ko'
categories: 'flutter'
comments: true

title: '[Flutter] BuildContext'
description: Flutter를 이용하여 앱을 개발해 봅시다. 이번 블로그 포스트에서는 Flutter로 생성한 프로젝트를 살펴보고, Flutter의 위젯에 관해 배워보겠습니다.
image: '/assets/images/category/flutter/background.jpg'
published: false
---

<div id="contents_list" markdown="1">

## 목차

</div>

## 개요

BuildContext: Widget Tree에서 현재 Widget의 위치를 알 수 있는 정보

build 함수: 위젯을 반환. 이때 현재 위젯의 위치를 알 수 있는 Context를 파라메터로 전달 받음

```dart
@override
Widget build(BuildContext context) {
}
```

이 BuildContext는 Stateless 위젯이나 state 빌드 메서드에 의해서 반환된 위젯의 부모가 된다.

Scaffold.of(context): 현재 주어진 context에서 위로 올라가면서 가장 가까운 Scaffold를 찾아 반환하라.

Something.of(context): 위로 거술러 올라가면서 가장 가까운 Something을 반환하라.
Theme.of(context): 위로 거슬러 올라가면서 가장 가까운 Theme을 반환하라.

{% include in-feed-ads.html %}
