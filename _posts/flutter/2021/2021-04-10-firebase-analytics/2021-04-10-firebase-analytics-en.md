---
layout: 'post'
permalink: '/flutter/firebase/analytics/'
paginate_path: '/flutter/:num/firebase/analytics/'
lang: 'en'
categories: 'flutter'
comments: true

title: '[Flutter] Firebase Analytics'
description: In this blog post, I will show you how to use Filebase Analytics in Flutter.
image: '/assets/images/category/flutter/background.png'
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [Blog series](#blog-series)
- [Create and configure Firebase project](#create-and-configure-firebase-project)
- [Install firebase_analytics](#install-firebase_analytics)
- [How to use firebase_analytics](#how-to-use-firebase_analytics)
- [Custom Event](#custom-event)
- [Complete](#complete)

</div>

## Outline

In this blog post, I will introduce how to configure `Firebase Analytics` to analyze the user behavior patterns in Flutter.

- [firebase_analytics](https://pub.dev/packages/firebase_analytics){:rel="nofollow noreferrer" target="_blank" }

To use `Firebase Analytics` in Flutter, we need to install the `firebase_analytics` package. In this blog post, I will show you how to configure the `firebase_analytics` package and how to use it.

## Blog series

This blog post is a series. You can see the other posts on the link below.

- [[Flutter] Firebase Core]({{site.url}}/{{page.categories}}/firebase/core/){:target="_blank"}
- [Flutter] Firebase Analytics
- [[Flutter] Firebase Crashlytics]({{site.url}}/{{page.categories}}/firebase/crashlytics/){:target="_blank"}

## Create and configure Firebase project

To use Firebase in Flutter, we need to create Firebase project, and install the `firebase_core` package. See the details on the link below.

- [[Flutter] Firebase Core]({{site.url}}/{{page.categories}}/firebase/core/){:target="_blank"}

## Install firebase_analytics

To use Firebase Analytics in Flutter, we need to install the `firebase_analytics` package. Execute the command below to install the `firebase_analytics` package.

```dart
flutter pub pub add firebase_analytics
```

{% include in-feed-ads.html %}

## How to use firebase_analytics

If you use the `firebase_analytics` package like below in Flutter, when the screen is changed, you can write the event to Firebase Analytics.

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

## Custom Event

You can make a custom event and use it like below.

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

## Complete

Done! we've seen how to configure and use the `firebase_analytics` package to use Firebase Analytics in Flutter. Now, you can analyze the user behavior patterns via Firebase Analytics!
