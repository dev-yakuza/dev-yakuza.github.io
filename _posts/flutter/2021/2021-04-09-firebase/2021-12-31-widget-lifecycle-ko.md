---
layout: 'post'
permalink: '/flutter/firebase/basic/'
paginate_path: '/flutter/:num/firebase/basic/'
lang: 'ko'
categories: 'flutter'
comments: true

title: '[Flutter] Firebase'
description: Flutter를 이용하여 앱을 개발해 봅시다. 이번 블로그 포스트에서는 Flutter로 생성한 프로젝트를 살펴보고, Flutter의 위젯에 관해 배워보겠습니다.
image: '/assets/images/category/flutter/background.png'
published: false
---

<div id="contents_list" markdown="1">

## 목차

</div>

## 개요

stateless widget
- build

stateful widget
- initState: State가 최초로 초기화될 때 호출. 위젯이 생성되서 위젯 트리에 추가되면, 호출됨.
- build
- dispose: 위젯이 위젯 트리에서 완전히 제거되고 난 후, 호출.
- deactivate