---
layout: 'post'
permalink: '/flutter/widget/animated/'
paginate_path: '/flutter/:num/widget/animated/'
lang: 'ja'
categories: 'flutter'
comments: true

title: '[Flutter] アニメーション'
description: 今回のブログポストではFlutterで簡単なアニメーションを使うためAnimatedContainerとAnimatedOpacityを使う方法について説明します。
image: '/assets/images/category/flutter/background.png'
published: false
---

<div id="contents_list" markdown="1">

## 目次

</div>

## 概要

Flutterで簡単なアニメーションを使うため`AnimatedContainer`ウィジェットと`AnimatedOpacity`ウィジェットを使う方法について説明します。

このブログポストで紹介するソースコードは下記のリンクで確認できます。

- GitHub: [AnimatedContainer](https://github.com/dev-yakuza/study-flutter/tree/main/widget/animated_container){:rel="nofollow noreferrer" target="_blank"}
- GitHub: [AnimatedOpacity](https://github.com/dev-yakuza/study-flutter/tree/main/widget/animated_opacity){:rel="nofollow noreferrer" target="_blank"}

## Flutterプロジェクト生成

Flutterで簡単なアニメーションを使う方法を練習するため、次のコマンドを使って新しFlutterプロジェクトを生成します。

```bash
flutter create my_app
cd my_app
```

{% include in-feed-ads.html %}

## AnimatedContainer

プロジェクトを生成したら、`main.dart`ファイルを次のように修正して`AnimatedContainer`ウィジェットを表示します。

```dart
import 'dart:math';

import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  double _width = 0;
  double _height = 0;
  Color _color = Colors.green;
  double _borderRadious = 0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('AnimatedContainer'),
      ),
      body: Center(
        child: AnimatedContainer(
          duration: Duration(seconds: 1),
          curve: Curves.fastOutSlowIn,
          width: _width,
          height: _height,
          decoration: BoxDecoration(
              color: _color,
              borderRadius: BorderRadius.circular(_borderRadious)),
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          setState(() {
            final random = Random();
            _width = random.nextInt(300).toDouble();
            _height = random.nextInt(300).toDouble();
            _color = Color.fromRGBO(random.nextInt(256), random.nextInt(256),
                random.nextInt(256), 1);
            _borderRadious = random.nextInt(150).toDouble();
          });
        },
        child: Icon(Icons.play_arrow),
      ),
    );
  }
}
```

上のとうにコードを作成したら次のような画面が確認できます。

![Flutter - AnimatedContainer](/assets/images/category/flutter/2021/animated/animated_container.jpg)

{% include in-feed-ads.html %}

そしたら`AnimatedContainer`ウィジェットを使う部分を詳しくみてみましょう。

```dart
class _MyHomePageState extends State<MyHomePage> {
  double _width = 0;
  double _height = 0;
  Color _color = Colors.green;
  double _borderRadious = 0;
  ...
}
```

`Statefull widget`を使ってアニメーションに使える変数を定義しました。

```dart
class _MyHomePageState extends State<MyHomePage> {
  ...
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      ...
      body: Center(
        child: AnimatedContainer(
          duration: Duration(seconds: 1),
          curve: Curves.fastOutSlowIn,
          width: _width,
          height: _height,
          decoration: BoxDecoration(
              color: _color,
              borderRadius: BorderRadius.circular(_borderRadious)),
        ),
      ),
      ...
    );
  }
}
```

このように定義した変数を`AnimatedContainer`ウィジェットを生成する時、使いました。

```dart
class _MyHomePageState extends State<MyHomePage> {
  ...
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      ...
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          setState(() {
            final random = Random();
            _width = random.nextInt(300).toDouble();
            _height = random.nextInt(300).toDouble();
            _color = Color.fromRGBO(random.nextInt(256), random.nextInt(256),
                random.nextInt(256), 1);
            _borderRadious = random.nextInt(150).toDouble();
          });
        },
        child: Icon(Icons.play_arrow),
      ),
    );
  }
}
```

最後に`FloatingActionButton`を押した時、`setState`を使ってアニメーションに使えてる変数の値を変更しました。`FloatingActionButton`ボタンを押すと、色んな四角形が画面に表示されることが確認できます。

{% include in-feed-ads.html %}

## AnimatedOpacity

`AnimatedOpacity`ウィジェットは`AnimatedContainer`ウィジェットと違って、単純に透明度(Opacity)に関するアニメーションを適用する時使います。`main.dart`ファイルを開いて下記のように修正します。

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  bool _isVisible = true;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('AnimatedOpacity'),
      ),
      body: Center(
        child: AnimatedOpacity(
          opacity: _isVisible ? 1.0 : 0,
          duration: Duration(seconds: 1),
          child: Container(
            width: 200,
            height: 200,
            color: Colors.green,
          ),
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          setState(() {
            _isVisible = !_isVisible;
          });
        },
        child: Icon(Icons.play_arrow),
      ),
    );
  }
}
```

コードを上のように修正したら、次のような画面が確認できます。

![Flutter - AnimatedOpacity](/assets/images/category/flutter/2021/animated/animated_opacity.jpg)

{% include in-feed-ads.html %}

そしたら`AnimatedOpacity`ウィジェットを使う部分をもっと詳しくみてみましょう。

```dart
class _MyHomePageState extends State<MyHomePage> {
  bool _isVisible = true;
  ...
}
```

今回の例題では`_isVisible`変数を使って、`true`の場合は`AnimatedOpacity`ウィジェットを画面に表示して、`false`の場合はウィジェットを見えないようにする予定です。

```dart
class _MyHomePageState extends State<MyHomePage> {
  ...
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      ...
      body: Center(
        child: AnimatedOpacity(
          opacity: _isVisible ? 1.0 : 0,
          duration: Duration(seconds: 1),
          child: Container(
            width: 200,
            height: 200,
            color: Colors.green,
          ),
        ),
      ),
      ...
    );
  }
}
```

`AnimatedOpacity`ウィジェットは`child`でウィジェットを必須で貰います。この時、`opacity`をセットすることで透明度のアニメーションを適用することができます。

```dart
class _MyHomePageState extends State<MyHomePage> {
  ...
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      ...
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          setState(() {
            _isVisible = !_isVisible;
          });
        },
        child: Icon(Icons.play_arrow),
      ),
    );
  }
}
```

次は`FloatingActionButton`ウィジェットを使って`_isVisible`を変更して、`AnimatedOpacity`ウィジェットの透明度を変更しました。

## 完了

これでFlutterで`AnimatedContainer`ウィジェットと`AnimatedOpacity`ウィジェットを使って簡単なアニメーションを適用する方法についてみてみました。
