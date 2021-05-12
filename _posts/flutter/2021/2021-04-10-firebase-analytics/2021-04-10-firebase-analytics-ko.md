---
layout: 'post'
permalink: '/flutter/firebase/analytics/'
paginate_path: '/flutter/:num/firebase/analytics/'
lang: 'ko'
categories: 'flutter'
comments: true

title: '[Flutter] Firebase Analytics'
description: 이번 블로그 포스트에서는 Flutter에서 Firebase의 Analytics를 연동하고 사용하는 방법에 대해서 알아보겠습니다.
image: '/assets/images/category/flutter/background.png'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [블로그 시리즈](#블로그-시리즈)
- [Firebase 프로젝트 생성 및 설정](#firebase-프로젝트-생성-및-설정)
- [firebase_analytics 설치](#firebase_analytics-설치)
- [firebase_analytics 사용법](#firebase_analytics-사용법)
- [커스텀 이벤트](#커스텀-이벤트)
- [완료](#완료)

</div>

## 개요

이번 블로그 포스트에서는 Flutter에서 사용자의 행동을 분석하기 위해 `Firebase`의 `Analytics`를 설정하는 방법에 대해서 소개합니다.

- [firebase_analytics](https://pub.dev/packages/firebase_analytics){:rel="nofollow noreferrer" target="_blank" }

`Firebase`의 `Analytics`를 사용하기 위해 Flutter에 `firebase_analytics`을 사용할 필요가 있습니다. 이번 블로그 포스트에서는 `firebase_analytics`을 설정하고 사용하는 방법에 대해서 알아봅시다.

## 블로그 시리즈

이 블로그는 시리즈로 제작되었습니다. 다음 링크를 통해 다른 블로그 포스트도 확인해 보시기 바랍니다.

- [[Flutter] Firebase Core]({{site.url}}/{{page.categories}}/firebase/core/){:target="_blank"}
- [Flutter] Firebase Analytics
- [[Flutter] Firebase Crashlytics]({{site.url}}/{{page.categories}}/firebase/crashlytics/){:target="_blank"}

## Firebase 프로젝트 생성 및 설정

Flutter에서 Firebase를 사용하기 위해서는 Firebase 프로젝트를 생성하고, `firebase_core` 패키지를 설치할 필요가 있습니다. 아래의 링크를 통해 자세한 내용을 확인하시기 바랍니다.

- [[Flutter] Firebase Core]({{site.url}}/{{page.categories}}/firebase/core/){:target="_blank"}

## firebase_analytics 설치

Flutter 프로젝트에서 Firebase Analytics를 사용하기 위해서는 `firebase_analytics` 패키지를 설치할 필요가 있습니다. 다음 명령어를 실행하여 `firebase_analytics` 패키지를 설치합니다.

```dart
flutter pub pub add firebase_analytics
```

{% include in-feed-ads.html %}

## firebase_analytics 사용법

Flutter에서 다음과 같이 `firebase_analytics`를 사용하면, 화면이 변경되었을 때, Firebase Analytics에 이를 기록할 수 있습니다.

```dart
import 'package:firebase_analytics/firebase_analytics.dart';
import 'package:firebase_analytics/observer.dart';

class MyApp extends StatelessWidget {
  static FirebaseAnalytics analytics = FirebaseAnalytics();

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      navigatorObservers: [
        FirebaseAnalyticsObserver(analytics: analytics),
      ],
      initialRoute: 'Category',
      routes: {'Category': (context) => Categories()},
    );
  }
}
```

## 커스텀 이벤트

다음과 같이 사용자 정의 이벤트를 만들어서 사용할 수도 있습니다.

```dart
class MyApp extends StatelessWidget {
  const MyApp({Key key}) : super(key: key);

  static FirebaseAnalytics analytics = FirebaseAnalytics();
  static FirebaseAnalyticsObserver observer =
      FirebaseAnalyticsObserver(analytics: analytics);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Firebase Analytics Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      navigatorObservers: [observer],
      home: Home(
        analytics: analytics,
      ),
    );
  }
}

class Home extends StatefulWidget {
  Home({this.analytics})
      : super();

  final FirebaseAnalytics analytics;

  @override
  _HomeState createState() => _HomeState();
}

class _MyHomePageState extends State<MyHomePage> {
  String _message = '';

  void setMessage(String message) {
    setState(() {
      _message = message;
    });
  }

  Future<void> _sendAnalyticsEvent() async {
    await widget.analytics.logEvent(
      name: 'test_event',
      parameters: <String, dynamic>{
        'string': 'string',
        'int': 42,
        'long': 12345678910,
        'double': 42.0,
        'bool': true,
      },
    );
    setMessage('logEvent succeeded');
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Column(
        children: <Widget>[
          MaterialButton(
            onPressed: _sendAnalyticsEvent,
            child: const Text('Test logEvent'),
          ),
          Text(_message,
              style: const TextStyle(color: Color.fromARGB(255, 0, 155, 0))),
        ],
      ),
    );
  }
}
```

## 완료

이것으로 Flutter에서 Firebase Analytics를 사용하기 위해 Flutter 프로젝트에 `firebase_analytics`를 설정하는 방법에 대해서 알아보았습니다. 이제 Firebase Analytics를 사용하여 사용자의 앱 행동 패턴을 분석해 보시기 바랍니다.
