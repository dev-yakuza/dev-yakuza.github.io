---
layout: 'post'
permalink: '/flutter/widget/snackbar/'
paginate_path: '/flutter/:num/widget/snackbar/'
lang: 'ja'
categories: 'flutter'
comments: true

title: '[Flutter] Snackbarウィジェット'
description: Flutterを使ってアプリを開発してみようかと思います。今回のブログポストではFlutterでスナックバーを表示するためSnackbarウィジェットを使う方法について説明します。
image: '/assets/images/category/flutter/background.png'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [プロジェクト生成](#プロジェクト生成)
- [スナックバー](#スナックバー)
- [完了](#完了)

</div>

## 概要

Flutterを使ってアプリを開発してみようかと思います。今回のブログポストではFlutterで簡単にメッセージを表示するためスナックバーを使う方法について説明します。

![Flutter - snackbar](/assets/images/category/flutter/2021/snackbar/snackbar.jpg)

このブログポストで紹介するソースコードは下記のリンクで確認できます。

- GitHub: [https://github.com/dev-yakuza/study-flutter/tree/main/widget](https://github.com/dev-yakuza/study-flutter/tree/main/widget){:rel="nofollow noreferrer" target="_blank"}

## プロジェクト生成

Flutterでスナックバーを表示する方法を調べるため、下記のコマンドを使って新しいプロジェクトを生成します。

```bash
flutter create my_app
cd my_app
```

{% include in-feed-ads.html %}

## スナックバー

そしたら生成されたプロジェクトでスナックバーを表示してみましょう。`main.dart`ファイルを開いて下記のように修正します。

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
      debugShowCheckedModeBanner: false,
      home: Home(),
    );
  }
}

class Home extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Snack bar'),
      ),
      body: Center(
        child: ElevatedButton(
          child: Text('Show Snackbar'),
          onPressed: () {
            ScaffoldMessenger.of(context).showSnackBar(
              SnackBar(
                content: Text('Hello world'),
              ),
            );
          },
        ),
      ),
    );
  }
}
```

上のコードは画面の真ん中にボタンを表示して、そのボタンを押した時、スナックバーが表示される例題です。

```dart
Center(
  child: ElevatedButton(
    child: Text('Show Snackbar'),
    onPressed: () {
      ...
    },
  ),
),
```

スナックバーを表示するためには`ScaffoldMessenger`を使う必要があります。

```dart
ScaffoldMessenger.of(context).showSnackBar(
  SnackBar(
    content: Text('Hello world'),
  ),
);
```

この時、`showSnackBar`に`SnackBar`ウィジェットを渡して、画面に表示される内容を作成します。

{% include in-feed-ads.html %}

`SnackBar`ウィジェットは下記のように色んなオプションがあります。

```dart
ScaffoldMessenger.of(context).showSnackBar(
  SnackBar(
    content: Text('Hello world'),
    backgroundColor: Colors.teal,
    duration: Duration(milliseconds: 1000),
    behavior: SnackBarBehavior.floating,
    action: SnackBarAction(
      label: 'Undo',
      textColor: Colors.white,
      onPressed: () => print('Pressed'),
    ),
  ),
);
```

このようにオプションを指定したら、次と同じようにスナックバーを表示することができます。

![Flutter - snackbar with options](/assets/images/category/flutter/2021/snackbar/snackbar_with_options.jpg)

## 完了

これでFlutterでスナックバーを表示する方法についてみてみました。また、スナックバーの色んなオプションもみてみました。今からFlutterで簡単なメッセージを表示すると時はスナックバーを使ってみてください。
