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

그럼 이제, 생성한 전역 상태를 사용할 위젯들의 공통 부모 위젯에 `Provider`를 제공해 봅시다. `lib/main.dart` 파일을 열고 다음과 같이 수정합니다.

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

앞에서 생성한 전역 상태를 사용하기 위해 `flutter_proivder` 패키지와 상태 클래스를 가져왔습니다.

```dart
...
import 'package:provider/provider.dart';
import 'package:provider_example/providers/counts.dart';
...
```

아직 만들지 않았지만, Provider를 사용할 위젯을 추가하였습니다.

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

이번 예제에서는 최상단 위젯에 `Provider`를 제공하였습니다. 보통 하나의 앱을 개발할 때, 하나 이상의 Provider를 사용하므로, 이 번 예제에서도 `MultiProvider`를 사용하여 여러 Provider를 제공할 수 있도록 하였습니다.

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

이후, 보통의 앱을 개발하는 방식으로 화면을 구성하였습니다. 그럼 이제 Provider를 사용할 위젯인 `Counter`와 `Buttons`를 개발해 보도록 합시다.

{% include in-feed-ads.html %}

### Counter

그럼 이제, Provider를 사용하는 위젯을 만들어 봅시다. `lib/widgets/counter.dart` 파일을 생성하고 다음과 같이 수정합니다.

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

`Counter`위젯은 `Text` 위젯을 사용하여, 화면에 숫자를 표시하는 단순한 위젯입니다. 이때, `context.watch<Counts>().count`를 사용하여 우리가 만든 Provider의 `count` 값이 변경되는지를 감시하고, 변경이 발생하면 화면에 변경된 값을 표시하도록 하였습니다.

### Buttons

다음은, 우리가 만든 Provider의 값을 변경하기 위해, `Buttons` 위젯을 만들어 봅시다. `lib/widgets/buttons.dart` 파일을 생성하고 다음과 같이 수정합니다.

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

`Counter` 위젯과는 다르게 `Buttons` 위젯에서는 Provider의 `count`를 변경하기 위해 `context.read<Counts>()`을 사용해서 `add`와 `remove` 함수를 호출하였습니다.

`Buttons` 위젯에서 `add` 또는 `remove` 함수가 호출되면, Provider에서 해당 변수를 변경한 후, `notifyListeners()` 함수를 호출하여 값이 변경되었음을 알립니다. 이렇게 값이 변경되면, Provider의 `context.watch` 또는 `context.select`로 해당 값을 사용하는 위젯들은 값의 변경에 따라 `re-build`가 발생하고 위젯이 새로운 값과 함께 다시 표시되게 욉니다.

{% include in-feed-ads.html %}

## watch, read, select

Provider에는 `watch`, `read`, `select` 기능을 제공하고 있습니다.

- read: 해당 위젯은 상태값을 읽습니다. 하지만 변경을 감시하지 않습니다.
- watch: 해당 위젯이 상태값의 변경을 감시합니다.
- select: 해당 위젯은 상태값의 특정 부분만을 감시합니다.

보통 Provider의 값을 변경하기 위한 함수는 `read`를 통해 접근하며, 상태값을 사용할 때에는 `watch`를 사용합니다. 변경된 상태값을 표시하기 위해 `re-build`가 발생하는데, 이 `re-build`는 많은 비용을 사용합니다. 따라서, 다음과 같이 `select`를 통해 특정 값의 변경만을 감시하여 `re-build`를 최적화 할 수 있습니다.

```dart
Widget build(BuildContext context) {
  final name = context.select((Person p) => p.name);
  return Text(name);
}
```

## 실행

지금까지 개발한 Flutter 앱을 다음 명령어로 실행해 봅니다.

```bash
flutter run
```

또는 사용하고 있는 에디터의 디버깅 기능으로 실행하면, 다음과 같은 화면을 볼 수 있습니다.

![flutter provider](/assets/images/category/flutter/2021/provider/counter_app.jpg)

그리고 화면에 보이는 `+` 버튼을 누르면 표시된 숫자가 증가하는 것을 확인할 수 있습니다. 또 `-` 버튼을 누르면 표시된 숫자가 감소하는 것을 확인할 수 있습니다.

## 완료

이것으로 Flutter에서 Provider를 사용여 여러 위젯에서 사용되는 전역 상태를 관리하는 방법에 대해서 알아보았습니다. 또한 간단한 예제를 통해 Provider를 사용하는 방법에 대해서도 알아보았습니다.
