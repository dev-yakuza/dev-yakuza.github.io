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

```dart
Scaffold(
        appBar: AppBar(
          title: Text('Navigator'),
        ),
        body: Center(
          child: ElevatedButton(
            child: Text('Second Screen'),
            onPressed: () {
              Navigator.push(
                  context, MaterialPageRoute(builder: (_) => SecondScreen()));
            },
          ),
        ));
```

```dart
Scaffold(
        appBar: AppBar(
          title: Text('Second Screen'),
        ),
        body: Center(
          child: ElevatedButton(
            child: Text('Home Screen'),
            onPressed: () {
              Navigator.pop(context);
            },
          ),
        ));
```

`_` 변수 => 사용하지 않은 매개변수


{% include in-feed-ads.html %}
