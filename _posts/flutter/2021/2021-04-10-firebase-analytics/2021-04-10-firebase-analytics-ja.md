---
layout: 'post'
permalink: '/flutter/firebase/analytics/'
paginate_path: '/flutter/:num/firebase/analytics/'
lang: 'ja'
categories: 'flutter'
comments: true

title: '[Flutter] Firebase Analytics'
description: 今回のブログポストではFlutterでFirebaseのAnalyticsを連動する方法について説明します。
image: '/assets/images/category/flutter/background.png'
published: false
---

<div id="contents_list" markdown="1">

## 目次

</div>

## 概要

今回のブログポストではFlutterでユーザの動きを分析するため`Firebase`の`Analytics`を設定する方法について説明します。

- [firebase_analytics](https://pub.dev/packages/firebase_analytics){:rel="nofollow noreferrer" target="_blank" }

`Firebase`の`Analytics`を使うためFlutterで`firebase_analytics`を使う必要があります。今回のブログポストでは`firebase_analytics`を設定して、使う方法について説明します。

## ブログシリーズ

このブログはシリーズで作成されております。次のリンクを使って他のブログポストは下記のリンクで確認できます。

- [[Flutter] Firebase Core]({{site.url}}/{{page.categories}}/firebase/core/){:target="_blank"}
- [Flutter] Firebase Analytics
- [[Flutter] Firebase Crashlytics]({{site.url}}/{{page.categories}}/firebase/crashlytics/){:target="_blank"}

## Firebaseプロジェクト生成や設定

FlutterでFirebaseを使うためにはFirebaseプロジェクトを生成して、`firebase_core`パッケージをインストールする必要があります。下記のリンクで詳しい内容を確認してください。

- [[Flutter] Firebase Core]({{site.url}}/{{page.categories}}/firebase/core/){:target="_blank"}

## firebase_analyticsインストール

FlutterプロジェクトでFirebase Analyticsを使うためには`firebase_analytics`パッケージをインストールする必要があります。次のコマンドを実行して`firebase_analytics`パッケージをインストールします。

```dart
flutter pub pub add firebase_analytics
```

{% include in-feed-ads.html %}

## firebase_analyticsの使い方

Flutterで次のように`firebase_analytics`を使うと、画面が変更された時、Firebase Analyticsへこれを記録することができます。

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

次のようにカスタムユーザイベントを作って使うこともできます。

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

## 完了

これでFlutterでFirebase Analyticsを使うためFlutterプロジェクトで`firebase_analytics`を設定する方法について説明しました。これからFirebase Analyticsを使ってユーザのアプリ内行動パターンを分析してみてください。
