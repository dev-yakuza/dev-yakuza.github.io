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
published: false
---

<div id="contents_list" markdown="1">

## 目次

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

各ファイルのコードをもっと詳しくみてみましょう。`ScreenA.dart`ファイルを
그럼 이제 각 화면에 대한 코드를 살펴보도록 하겠습니다. `ScreenA.dart` 파일 내용은 다음과 같습니다.

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

`StatelessWidget`을 상속 받고, `Scafford` 위젯을 사용한 간단한 화면 위젯입니다. 앞에서 설명한 소스 코드와 동일한 구조이므로 자세한 설명은 생략하도록 하겠습니다. 여기서는 `Named routes`를 사용하여 스택 내비게이션을 사용하는 부분만 살펴보도록 하겠습니다.

```dart
onPressed: () {
  Navigator.pushNamed(context, 'ScreenB');
},
```

`Named routes`를 사용하여 스택 내비게이션을 사용하기 위해서는 `Navigator` 위젯의 `pushNamed` 함수를 사용하면 됩니다. 이때, 위젯 트리의 위치 정보를 가지고 있는 `contenxt`와 이동하고 싶은 화면의 이름을 파라메터로 전달하면 됩니다.

{% include in-feed-ads.html %}

`ScreenB.dart`와 `ScreenC.dart`는 동일한 구조를 가지고 있으므로, 소스 코드만 공유하도록 하겠습니다.

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

Named routes를 사용하면 좀 더 간단하게 화면 이동을 할 수 있으며, 여러 화면을 관리하기에 더 적합합니다.

{% include in-feed-ads.html %}

## popUntil

스택 내비게이션을 사용하다보면, 많은 화면들이 쌓이게 됩니다. 이렇게 쌓인 화면을 한번에 되돌아 가기 위해서는 `popUntil`을 사용합니다.

`popUntil`의 사용 방법을 확인하기 위해서 `ScreenC.dart` 파일을 열고 다음과 같이 수정합니다.

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

화면을 첫 화면인 `ScreenA`까지 되돌아 가기 위해서 `ScreenC`에서는 다음과 같은 코드를 사용하였습니다.

```dart
onPressed: () {
  Navigator.popUntil(context, (route) => route.isFirst);
},
```

첫 화면으로 돌아가기 위해 `Navigator`의 `popUntil`을 사용하였으며, `route.isFirst`을 설정하였습니다. 이렇게 `popUntil`을 사용하면 첫 화면으로 돌아갈 수도 있지만, 다음과 같이 사용하면 특정 화면까지 되돌아 갈 수 있습니다.

```dart
onPressed: () {
  Navigator.popUntil(context, ModalRoute.withName('ScreenA'));
},
```

위와 같이 사용하면, `Named routes`에 정의된 이름을 사용하여 해당 화면까지 되돌아 갈 수 있습니다.

## 완료

이것으로 Flutter에서 스택 내비게이션을 사용하는 방법에 대해서 살펴보았습니다. 스택 내비게이션은 앱의 화면 전환에 가장 많이 사용되는 내비게이션이므로 사용법을 잘 익혀둡시다.
