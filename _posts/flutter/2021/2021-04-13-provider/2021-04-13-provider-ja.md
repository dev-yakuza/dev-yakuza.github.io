---
layout: 'post'
permalink: '/flutter/provider/'
paginate_path: '/flutter/:num/provider/'
lang: 'ja'
categories: 'flutter'
comments: true

title: '[Flutter] Provider'
description: 今回のブログポストではFlutterでグローバル状態（State）、またはウィジェットたちの間で状態（State）を共有するためProviderを使う方法について説明します。
image: '/assets/images/category/flutter/background.png'
published: false
---

<div id="contents_list" markdown="1">

## 目次

</div>

## 概要

今回ブログポストではFlutterでグローバル状態(State)を管理するため、またはウィジェットたちの間で状態(State)を共有するため使える`Provider`について説明します。

- [flutter_provider](https://pub.dev/packages/flutter_provider){:rel="nofollow noreferrer" target="_blank" }

このブログポストで紹介するソースコードはGitHubで確認できます。

- GitHub: [https://github.com/dev-yakuza/study-flutter/tree/main/packages/provider_example](https://github.com/dev-yakuza/study-flutter/tree/main/packages/provider_example){:rel="nofollow noreferrer" target="_blank"}

それじゃ、FlutterでProviderを使ってグローバル状態管理やウィジェットたちの間で状態を共有する方法についてみてみましょう。

## Flutterプロジェクト生成

次のコマンドを実行して`flutter_provider`パッケージを使うFlutterプロジェクトを生成します。

```bash
flutter create provider_example
```

`Null safety`を適用するため次のコマンドを実行します。

```bash
cd provider_example
dart migrate --apply-changes
```

{% include in-feed-ads.html %}

## flutter_providerパッケージのインストール

Flutterでグローバル状態管理やウィジェットたちの間で状態を共有するため、次のコマンドを実行して`flutter_provider`パッケージをインストールします。

```bash
flutter pub add flutter_provider
```

## Providerとは

Flutterでは大きく2種類のウィジェットが存在します。1は状態を持ってない`Stateless Widget`と状態(State)を持ってる`Stateful Widget`です。

`Statefule Widget`は1つのウィジェット中で状態(データ)を持ってその状態の変化によって画面に表示されたUIを変更します。

![flutter state](/assets/images/category/flutter/2021/provider/state.jpg)

もし、他のウィジェットで同じ状態（データ）が必要な場合はどうすれば良いでしょうか？

![flutter state required](/assets/images/category/flutter/2021/provider/need_state.jpg)

状態をシェアする2つの共通親ウィジェットを`Stateful Widget`を作って、チャイルドウィジェットを生成する時、パラメータでその状態を渡して、2つのウィジェットの間で同じ状態を使うことができます。

![flutter state required](/assets/images/category/flutter/2021/provider/pass_state.jpg)

しかし、状態を表示するため要らないウィジェットたちが`Re-build`され性能的な問題が出る可能性があります。`Provider`はこの問題を解決するため登場しました。このように同じ状態（データ）をグローバル的他のウィジェットと共有する時、`Provider`を使います。

![flutter provider](/assets/images/category/flutter/2021/provider/provider.jpg)

Providerを使う時には、ウィジェットツリーと関係なく状態（データ）を保存するクラスを生成して、当該状態をシェアする共通親ウィジェットに`Provider`を提供(Provide)して、状態を使うところで`Cosumer`を提供してその状態を消費(Consume)します。

{% include in-feed-ads.html %}

## 使い方

次は`flutter_provider`を使って実際グローバルの状態を管理してみましょう。今回のブログポストでは`flutter_provider`パッケージを使って、次のような簡単なカウンターアプリを開発する予定です。

![flutter provider](/assets/images/category/flutter/2021/provider/counter_app.jpg)

`+`ボタンを押すと、画面に表示される数字が上がって、`-`ボタンを押すと数字が下がる単純なアプリです。このアプリでFlutterでProviderを使う方法について説明します。

### Provider

まず、グローバルデータを管理するためProviderを作ってみましょう。`lib/providers/counts.dart`ファイルを生成して次のように修正します。

```dart
import 'package:flutter/material.dart';

class Counts with ChangeNotifier {
  int _count = 0;
  int get count => _count;

  void add() {
    _count++;
    notifyListeners();
  }

  void remove() {
    _count--;
    notifyListeners();
  }
}
```

Providerを使うためには`ChangeNotifier`を使ってクラスを生成する必要があります。

```dart
import 'package:flutter/material.dart';

class Counts with ChangeNotifier {
  ...
}
```

そしてアプリ内で共有する状態変数を宣言します。また、その変数を外部からアクセスできるように`getter`も生成します。

```dart
import 'package:flutter/material.dart';

class Counts with ChangeNotifier {
  int _count = 0;
  int get count => _count;
  ...
}
```

その後、その状態変数を変更する関数を生成します。ここでは値を上げる`add`関数と値を下げる`remove`関数を生成しました。

```dart
class Counts with ChangeNotifier {
  ...
  void add() {
    _count++;
    notifyListeners();
  }

  void remove() {
    _count--;
    notifyListeners();
  }
}
```

ここで重要なものは変数を修正したら、`notifyListeners()`を実行して、データが更新されたことを知らせます。`Stateful Widget`で値が変わったことを知らせるために`setState`関数を使うことと同じです。`notifyListeners`関数を実行しないと、他のウィジェットで値が変更されたことが認識できないです。

これでProviderを使ってアプリ全体で使うグローバル状態を生成しました。

{% include in-feed-ads.html %}

### Main

次は生成したグローバル状態を使うウィジェットたちの共通親ウィジェットに`Provider`を提供してみましょう。`lib/main.dart`ファイルを開いて下記のように修正します。

```dart
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:provider_example/providers/counts.dart';
import 'package:provider_example/widgets/buttons.dart';
import 'package:provider_example/widgets/counter.dart';

void main() {
  runApp(
    MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (_) => Counts()),
      ],
      child: MyApp(),
    ),
  );
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: Home(),
    );
  }
}

class Home extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Provider'),
      ),
      body: ChangeNotifierProvider(
        create: (BuildContext context) => Counts(),
        child: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Counter(),
              Buttons(),
            ],
          ),
        ),
      ),
    );
  }
}
```

上で生成したグローバル状態を使うため`flutter_proivder`パッケージと状態クラスをインポートしました。

```dart
...
import 'package:provider/provider.dart';
import 'package:provider_example/providers/counts.dart';
import 'package:provider_example/widgets/buttons.dart';
import 'package:provider_example/widgets/counter.dart';
```

まだ、作ってはないですが、Providerを使うウィジェットも追加しました。

```dart
...
void main() {
  runApp(
    MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (_) => Counts()),
      ],
      child: MyApp(),
    ),
  );
}
...
```

今回の例題では一番上のウィジェットに`Provider`を提供しました。普通は1つのアプリを開発する時、1つ以上のProviderを使うので、この例題では`MultiProvider`を使って複数のProviderを提供できるようにしました。

```dart
...
class Home extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Provider'),
      ),
      body: ChangeNotifierProvider(
        create: (BuildContext context) => Counts(),
        child: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Counter(),
              Buttons(),
            ],
          ),
        ),
      ),
    );
  }
}
...
```

後は、普通のアプリを開発する方法で画面を構成しました。次はProviderを使うウィジェットである`Counter`と`Buttons`を開発してみましょう。

{% include in-feed-ads.html %}

### Counter

そしたら、Providerを使うウィジェットを作ってみましょう。`lib/widgets/counter.dart`ファイルを生成して次のように修正します。

```dart
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:provider_example/providers/counts.dart';

class Counter extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    print('Counter');

    return Text(
      context.watch<Counts>().count.toString(),
      style: TextStyle(
        fontSize: 20,
      ),
    );
  }
}
```

`Counter`ウィジェットは`Text`ウィジェットを使って、画面に数字を表示する単純なウィジェットです。この時、`context.watch<Counts>().count`を使って私たちが作ったProviderの`count`の値が変更されることを監視して、変更がある場合その変更された値を表示するようにしました。

### Buttons

次は、私たちが作ったProviderの値を変更するため、`Buttons`ウィジェットを作ってみましょう。`lib/widgets/buttons.dart`ファイルを生成して次のように修正します。

```dart
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:provider_example/providers/counts.dart';

class Buttons extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        ElevatedButton(
            onPressed: () {
              context.read<Counts>().add();
            },
            child: Icon(Icons.add)),
        SizedBox(
          width: 40,
        ),
        ElevatedButton(
            onPressed: () {
              context.read<Counts>().remove();
            },
            child: Icon(Icons.remove))
      ],
    );
  }
}
```

`Counter`ウィジェットとは違って`Buttons`ウィジェットではProviderの`count`を変更するため`context.read<Counts>()`を使って`add`と`remove`関数をコールしました。

`Buttons`ウィジェットでは`add`または`remove`関数がコールされると、Providerで当該変数を変更した後、`notifyListeners()`関数をコールして値が変更されたことを知らせます。このように値が変更されたら、Providerの`context.watch`または`context.select`で当該値を使うウィジェットたちは値が変更で`re-build`が反省してウィジェットが新しい値と一緒に再表示されます。

{% include in-feed-ads.html %}

## watch, read, select

Providerは`watch`, `read`, `select`の機能を提供しております。

- read: 当該ウィジェットは状態の値を読み込みます。しかし、変更を監視しません。
- watch: 当該ウィジェットが状態の値の変更を監視します。
- select: 当該ウィジェットは状態の値の特定な部分だけ監視します。

普通Providerの値を変更するための関数は`read`を使ってアクセスするし、状態の値を使う時には`watch`を使います。変更された状態の値を表示するためには`re-build`が発生しますが、この`re-build`は費用が高いです。したがって、次のように`select`を使って特定な値の変更だけ監視して`re-build`を最適化することができます。

```dart
Widget build(BuildContext context) {
  final name = context.select((Person p) => p.name);
  return Text(name);
}
```

## 実行

今まで開発したFlutterアプリを次のコマンドで実行します。

```bash
flutter run
```

または使っているエディターのデバッグ機能を使って実行すると、次のような画面が見えます。

![flutter provider](/assets/images/category/flutter/2021/provider/counter_app.jpg)

そして画面に見える`+`ボタンを押したら表示された数字が上がることが確認できます。また、`-`ボタンを押すと表示された数字が下がることが確認できます。

## 完了

これでFlutterでProviderを使って色んなウィジェットで使えるグローバル状態を管理する方法についてみてみました。また、簡単な例題を使ってProviderを使う方法についてもみてみました。
