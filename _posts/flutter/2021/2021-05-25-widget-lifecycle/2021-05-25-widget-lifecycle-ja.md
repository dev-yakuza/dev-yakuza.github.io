---
layout: 'post'
permalink: '/flutter/widget/lifecycle/'
paginate_path: '/flutter/:num/widget/lifecycle/'
lang: 'ja'
categories: 'flutter'
comments: true

title: '[Flutter] ライフサイクル'
description: 今回のブログポストではFlutterのウィジェットのライフサイクル(lifecycle)について説明します。
image: '/assets/images/category/flutter/background.png'
published: false
---

<div id="contents_list" markdown="1">

## 目次

</div>

## 概要

Flutterでは単純に画面を構成するStatelessウィジェットは違って、Statefulウィジェットは`ライフサイクル(lifecycle`を持っています。今回のブログポストではStatefulウィジェットのライフサイクについて説明します。

Flutterのライフサイクル関数の理解を助けるため例題を作りました。下記のリンクでソースコードを確認することができます。

- GitHub: [AnimatedContainer](https://github.com/dev-yakuza/study-flutter/tree/main/widget/lifecycle){:rel="nofollow noreferrer" target="_blank"}

## Statelessウィジェット

Statelessウィジェットは単純に画面を構成するウィジェットなので、複雑なライフサイクルを持ってないです。それではStatelessウィジェットのライフサイクル関数についてみてみましょう。

### StatelessウィジェットのConstructor

Flutterでウィジェットは基本的クラスを使って生成します。ウィジェットは基本的クラスで構成されるので、同然ながらクラスの`コンストラクタ(Constructor)`を使うことができます。

ウィジェットのコンストラクタはクラスのコンストラクタと同じ役割をして、ウィジェット（クラス）中の使う変数を初期化する時使います。

```dart
import 'package:flutter/material.dart';

class Home extends StatelessWidget {
  final String title;

  Home({required this.title});

  ...
}
```

### Statelessウィジェットのbuild

ウィジェットの`build`関数は画面に表示される内容を作成します。これは`React`の`render`関数と同じ役割をして、画面に表示されるウィジェットをリターンします。

```dart
import 'package:flutter/material.dart';

class Home extends StatelessWidget {
  ...
  @override
  Widget build(BuildContext context) {
    return Center(
      child: Text('Setting Screen'),
    );
  }
}
```

Statelessウィジェットはステート（State）を持ってません。したがって、親ウィジェットから渡してもらった値が変更されるとウィジェットが`rebuild`され、画面を更新することになります。この時`Constructor`と`build`が再実行されます。

{% include in-feed-ads.html %}

## Statefulウィジェット

StatefulウィジェットはStatelessウィジェットとは違ってウィジェットがステート（State）を持ってるので、ウィジェットのライフサイクルが複雑です。それではStatefulウィジェットのライフサイクル関数を見てみましょう。

### StatefulウィジェットのConstructor

Statefulウィジェットのコンストラクト(Constructor)もStatelessウィジェットのコンストラクトと同じ役割をします。ウィジェットクラスでインスタンスを作る時、コンストラクトが一番最初コールされて、親ウィジェットからパラメータを貰う時使います。

```dart
class CounterContainer extends StatefulWidget {
  final int count;

  CounterContainer({required this.count})

  @override
  _CounterContainerState createState() => _CounterContainerState(count: count);
}

class _CounterContainerState extends State<CounterContainer> {
  int count;
  _CounterContainerState({required this.count})
  ...
}
```

### initState

Statefulウィジェットが生成される時、`一回`だけコールされる関数で、ステート(State)の値を初期化する時使います。

```dart
class _CounterContainerState extends State<CounterContainer> {
  late int count;

  @override
  void initState() {
    super.initState();
    count = 0;
  }
  ...
}
```

### didChangeDependencies

この関数はウィジェットが生成される時、`initState`関数がコールされた直後、一回コールされます。また、[InheritedWidget](https://api.flutter.dev/flutter/widgets/InheritedWidget-class.html){:rel="nofollow noreferrer" target="_blank"}や[Provider]({{site.url}}/{{page.categories}}/provider/){:target="_blank"}を使う場合、InheritedWidgetやProviderの内容が変わると、コールされます。

つまり、親ウィジェットや自分のステートが変更される時はコールされないですが、当該ウィジェットが参照(Depedency)するウィジェット(InheritedWidgetまたはProvider)が変更されると`didChangeDependencies`関数がコールされます。

### didUpdateWidget

この関数は親ウィジェットによって`rebuild`が必要な時、`build`関数がコールされる直前にコールされます。普通、親ウィジェットの変更によって、アニメーションを再実行する必要がある時、良く使います。

```dart
@override
void didUpdateWidget(MyWidget oldWidget) {
  super.didUpdateWidget(oldWidget);
  if (widget.value != oldWidget.value) {
    // TODO: start a transition between the previous and new value
  }
}
```

また、親ウィジェットの変更しによってステートを初期化する必要がある場合、この関数で`setState`を使ってステートを再初期化することができます。

### Statefulウィジェットのbuild

Statelessウィジェットのbuildと同じ役割をします。画面に表示されるウィジェットをリターンする時使います。`setState`を使ってStatefulウィジェットのステート(State)が変わるとき、再びコールされ画面を更新します。

{% include in-feed-ads.html %}

### deactivate

StatefulウィジェットはStatelessウィジェットは違ってステート(State)オブジェクトを持っています。このステートオブジェクトが変更(dirty)されると、変更されたステートオブジェクトを使ってStatefulウィジェットを`rebuild`します。

`deactivate`関数はステート(State)オブジェクトがツーリで削除される時、コールされます。Flutterは時々ステータオブジェクトでけ消して、また追加する場合があります。例えば`GlobalKey`を使って現在のウィジェットをウィジェットツーリの特定な位置に移動させると、当該ウィジェットのステータオブジェクトが変更され`deactivate`が実行されます。

詳しい内容は公式ドキュメントを参考してください。

- 公式ドキュメント: [deactivate](https://api.flutter.dev/flutter/widgets/State/deactivate.html){:rel="nofollow noreferrer" target="_blank"}

### dispose

ウィジェットオブジェクトがウィジェットツーリから永遠に削除される時、コールされます。ウィジェットツーリから完全に削除されるので、ステートオブジェクトも一緒に削除されます。ステータオブジェクトが削除されるので、`deactivate`が先コールされ、ステータオブジェクトが削除された後、`dispose`がコールされウィジェットが削除されたことを教えてくれます。

`dispose`関数のコールはウィジェットが永遠に削除されたことを意味するので、`setState`を使って当該ウィジェットの`rebuild`をすることができません。

### コールの順番

- Statefulウィジェットが生成される時: `Constructor` > `initState` > `didChangeDependencies` > `build`
- setStateがコールされる時: `build`
- InheritedWidgetまたはProviderの値が変更された時: `didChangeDependencies` > `build`
- 親ウィジェットから渡して貰った値が変更される時: `didUpdateWidget` > `build`
- ステータオブジェクトが削除される時: `deactivate` > `build`
- ウィジェットオブジェクトが削除される時: `deactivate` > `dispose`

## 完了

これでFlutterのウィジェットのライフサイクル(lifecycle)についてみてみました。間違ってライフサイクル関数を使うと、アプリの性能が悪くなったり、無限ループになったりするので注意して使わなきゃならないです。また、ウィジェットのライフサイクルは`setState`や特定な関数のコールタイミングを決定したり、アニメーションの実行時点に重要な役割をするので今回ちゃんと勉強しておきましょう。
