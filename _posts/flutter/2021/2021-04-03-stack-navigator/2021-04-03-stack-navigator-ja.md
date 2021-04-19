---
layout: 'post'
permalink: '/flutter/navigator/stack/'
paginate_path: '/flutter/:num/navigator/stack/'
lang: 'ja'
categories: 'flutter'
comments: true

title: '[Flutter] スタックナビゲーション'
description: Flutterを使ってアプリを開発しています。このブログポストではFlutterで生成したプロジェクトにスタックナビゲーションを使う方法について説明します。
image: '/assets/images/category/flutter/background.png'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [Stack](#stack)
- [Named routes](#named-routes)
- [popUntil](#popuntil)
- [完了](#完了)

</div>

## 概要

Flutterを使ってアプリを開発しています。アプリ開発で画面の移動にはナビゲーションを使います。今回のブログポストではFlutterでスタックナビゲーションを使って画面を移動する方法について説明します。

このブログポストで紹介するソースコードは下記のリンクで確認できます。

- GitHub: [https://github.com/dev-yakuza/study-flutter/tree/main/navigator](https://github.com/dev-yakuza/study-flutter/tree/main/navigator){:rel="nofollow noreferrer" target="_blank"}

## Stack

スタックナビゲーションは画面の上に画面を表示する方式で画面を移動します。画面の上に画面を表示する時は`push`を、上に表示された画面を削除する時には`pop`を使います。

それでは例題を見てスタックナビゲーションを理解してみましょう。次のコマンドを使ってスタックナビゲーションのためプロジェクトを生成します。

```bash
flutter create my_app
cd stack
```

{% include in-feed-ads.html %}

次は`main.dart`ファイルを開いて下記のように修正してスタックナビゲーションを使ってみます。

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
        title: Text('Navigator'),
      ),
      body: Center(
        child: ElevatedButton(
          child: Text('Second Screen'),
          onPressed: () {
            Navigator.push(
              context,
              MaterialPageRoute(
                builder: (_) => SecondScreen(),
              ),
            );
          },
        ),
      ),
    );
  }
}

class SecondScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
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
      ),
    );
  }
}
```

{% include in-feed-ads.html %}

そしたらソースコードを一つづつ詳しくみてみましょう。

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
```

ここまでは基本的アプリを生成することと同じです。`MaterialApp`を使うと、アプリが実行された時、一番最初表示される画面を`home`パラメータに設定することができます。ここに私は`Home`ウィジェットを設定しました。

次はスタックナビゲーションを使うため二つの`StatelessWidget`を生成しました。一つは`MaterialApp`の`home`に設定した`Home`ウィジェットとスタックナビゲーションを使ってHomeウィジェット上に表示する`SecondScreen`ウィジェットを生成しました。

```dart
class Home extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: ...,
      body: Center(
        child: ElevatedButton(
          child: Text('Second Screen'),
          onPressed: () {...},
        ),
      ),
    );
  }
}

class SecondScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar:...,
      body: Center(
        child: ElevatedButton(
          child: Text('Home Screen'),
          onPressed: () {...},
        ),
      ),
    );
  }
}
```

二つのウィジェットは`Scaffold`を使って基本的同じ構造を持っています。画面の真ん中に`ElevatedButton`ウィジェットを使ってボタンを表示しました。そして、各ボタンを押した時、スタックナビゲーションを使って画面の移動を実装しました。

次は各ボタンを押した時、スタックナビゲーションを呼び出す部分をみてみましょう。一旦`Home`画面から`SecondScreen`に移動するコードをみてみましょう。

```dart
onPressed: () {
  Navigator.push(
    context,
    MaterialPageRoute(
      builder: (context) => SecondScreen(),
    ),
  );
},
```

スタックナビゲーションで、新しい画面を画面の上に表示するためには`Navigator`ウィジェットの`push`関数を使う必要があります。`push`関数をコールする時、ウィジェットツーリの位置情報を持ってる`context`と`MaterialPageRoute`のbuilderを使って画面の上に表示するウィジェットをパラメータで設定します。

このようにコードを作成すると`Home`ウィジェットに表示されたボタンを押すと、Home画面の上に、`SecondScreen`ウィジェットが表示されます。

次は`SecondScreen`で`Home`画面に戻るため、`SecondScreen`を削除するコードを確認してみましょう。

```dart
onPressed: () {
  Navigator.pop(context);
},
```

`Navigator`ウィジェットの`pop`をコールすると、現在表示された画面が削除されるし、現在表示された画面の下にあった画面が表示されます。`pop`関数をコールする時には現在位置情報を持ってる`context`を渡さなきゃならないです。

{% include in-feed-ads.html %}

## Named routes

Flutterで複数画面を管理する時、`Named routes`を使います。

次は`Named routes`を使ってスタックナビゲーションを使ってみましょう。まず、`main.dart`ファイルを次のように修正します。

```dart
import 'package:flutter/material.dart';
import 'ScreenA.dart';
import 'ScreenB.dart';
import 'ScreenC.dart';

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
      initialRoute: 'ScreenA',
      routes: {
        'ScreenA': (context) => ScreenA(),
        'ScreenB': (context) => ScreenB(),
        'ScreenC': (context) => ScreenC(),
      },
    );
  }
}
```

`Named routes`を使うためには`MaterialApp`で`routes`に画面の名前と名前に合う画面のウィジェットを宣言します。また、`home`パラメータの代わりで`initialRoute`を使ってアプリが実行された後最初表示されるウィジェットを定義します。

今回の例題では各画面ウィジェットを`lib/ScreenA.dart`、`lib/ScreenB.dart`、`lib/ScreenC.dart`ファイルを生成した後、そのファイルにコードを作成しました。

このように生成したウィジェットを`main.dart`ファイルに次のようにインポートしました。

```dart
import 'ScreenA.dart';
import 'ScreenB.dart';
import 'ScreenC.dart';
```

各ファイルのコードをもっと詳しくみてみましょう。`ScreenA.dart`ファイルを内容は次のようです。

```dart
import 'package:flutter/material.dart';

class ScreenA extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Screen A'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            ElevatedButton(
              child: Text('Screen B'),
              onPressed: () {
                Navigator.pushNamed(context, 'ScreenB');
              },
            ),
            ElevatedButton(
              child: Text('Second C'),
              onPressed: () {
                Navigator.pushNamed(context, 'ScreenC');
              },
            ),
          ],
        ),
      ),
    );
  }
}
```

`StatelessWidget`を継承して、`Scafford`ウィジェットを使った簡単な画面のウィジェットです。上で説明したソースコードと同じ構造なので説明は省略します。ここでは`Named routes`を使ったスタックナビゲーションを使う部分だけ説明します。

```dart
onPressed: () {
  Navigator.pushNamed(context, 'ScreenB');
},
```

`Named routes`を使ってスタックナビゲーションを使うためには`Navigator`ウィジェットの`pushNamed`関数を使います。この時ウィジェットツーリの情報を持ってる`contenxt`と移動したい画面の名前をパラメータで渡します。

{% include in-feed-ads.html %}

`ScreenB.dart`と`ScreenC.dart`は同じ構造を持ってますので、コードだけ共有します。

- ScreenB.dart

```dart
import 'package:flutter/material.dart';

class ScreenB extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Screen B'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            ElevatedButton(
              child: Text('Back'),
              onPressed: () {
                Navigator.pop(context);
              },
            ),
            ElevatedButton(
              child: Text('Second A'),
              onPressed: () {
                Navigator.pushNamed(context, 'ScreenA');
              },
            ),
            ElevatedButton(
              child: Text('Second C'),
              onPressed: () {
                Navigator.pushNamed(context, 'ScreenC');
              },
            ),
          ],
        ),
      ),
    );
  }
}
```

- ScreenC.dart

```dart
import 'package:flutter/material.dart';

class ScreenC extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Screen C'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            ElevatedButton(
              child: Text('Back'),
              onPressed: () {
                Navigator.pop(context);
              },
            ),
            ElevatedButton(
              child: Text('Second A'),
              onPressed: () {
                Navigator.pushNamed(context, 'ScreenA');
              },
            ),
            ElevatedButton(
              child: Text('Second B'),
              onPressed: () {
                Navigator.pushNamed(context, 'ScreenB');
              },
            ),
          ],
        ),
      ),
    );
  }
}
```

Named routesを使うともっと簡単に画面の移動することができるし、色んな画面を管理するのに適しています。

{% include in-feed-ads.html %}

## popUntil

スタックナビゲーションを使うと、たくさんの画面がたまることがあります。このように溜まった画面を一回で戻るためには`popUntil`を使います。

`popUntil`の使い方を確認するため、`ScreenC.dart`ファイルを次のように修正します。

```dart
import 'package:flutter/material.dart';

class ScreenC extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Screen C'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            ElevatedButton(
              child: Text('Home'),
              onPressed: () {
                Navigator.popUntil(context, (route) => route.isFirst);
              },
            ),
          ],
        ),
      ),
    );
  }
}
```

画面を最初の画面である`ScreenA`まで戻るため、`ScreenC`では次のようなコードを使いました。

```dart
onPressed: () {
  Navigator.popUntil(context, (route) => route.isFirst);
},
```

最初の画面に戻るため`Navigator`の`popUntil`を使いましたし、`route.isFirst`を設定しました。このように`popUntil`を使うと最初の画面に戻ることができます。または、下記のように使うと特定した画面まで戻ることもできます。

```dart
onPressed: () {
  Navigator.popUntil(context, ModalRoute.withName('ScreenA'));
},
```

上のように使うと、`Named routes`に定義した名前を使ってその画面まで戻ることができます。

## 完了

これでFlutterでスタックナビゲーションを使う方法についてみてみました。スタックナビゲーションはアプリの画面の移動に一番多く使えるので、今回よく覚えておきましょう。
