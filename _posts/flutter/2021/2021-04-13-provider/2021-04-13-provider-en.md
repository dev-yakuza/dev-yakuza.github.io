---
layout: 'post'
permalink: '/flutter/provider/'
paginate_path: '/flutter/:num/provider/'
lang: 'en'
categories: 'flutter'
comments: true

title: '[Flutter] Provider'
description: In this blog post, I will show you how to use Provider to use a global state or share the state between widgets in Flutter.
image: '/assets/images/category/flutter/background.png'
published: false
---

<div id="contents_list" markdown="1">

## Contents

</div>

## Outline

Int this blog post, I will introduce how to use `Provider` to manage the global state or share the state between widgets in Flutter.

- [flutter_provider](https://pub.dev/packages/flutter_provider){:rel="nofollow noreferrer" target="_blank" }

You can see the full source code of the blog post on GitHub.

- GitHub: [https://github.com/dev-yakuza/study-flutter/tree/main/packages/provider_example](https://github.com/dev-yakuza/study-flutter/tree/main/packages/provider_example){:rel="nofollow noreferrer" target="_blank"}

So, let's see how to use Provider in Flutter to manage the global state and share the state between widgets.

## Create Flutter project

To use the `flutter_provider` package, execute the command below to create new Flutter project.

```bash
flutter create provider_example
```

To apply `Null safety`, execute the command below.

```bash
cd provider_example
dart migrate --apply-changes
```

{% include in-feed-ads.html %}

## Install flutter_provider package

To share the global state and share the state between widgets, execute the command below to install the `flutter_provider` package.

```bash
flutter pub add flutter_provider
```

## What is Provider

There are two types of the widgets. One is the `Stateless Widget` which has no state, and another is the `Stateful Widget` which has the state.

The `Statefule Widget` has the state(data) and when the state is changed, the UI is changed by the state.

![flutter state](/assets/images/category/flutter/2021/provider/state.jpg)

If the other widgets need the same state(data), what can we do?

![flutter state required](/assets/images/category/flutter/2021/provider/need_state.jpg)

Change the two widgets' shared parent widget to the `Stateful Widget`, and by passing the state to the child widget when you create the child widget, you can share the state between two widgets.

![flutter state required](/assets/images/category/flutter/2021/provider/pass_state.jpg)

However, to show the state, many widgets do `re-build` unnecessarily, so the performance issue may occur. To solve this issue, `Provider` is created. When we want to share the state between wigets globally, we use `Provider`.

![flutter provider](/assets/images/category/flutter/2021/provider/provider.jpg)

When we use Provider, we create a class to store the state(data) regardless of the widget tree, and provider `Provder` to the shared parent widget, and read `Provider` data in the widget which needs to consume the state.

{% include in-feed-ads.html %}

## How to use

Now, let's see how to use the `flutter_provider` package to manage the global state. In this blog post, we will make a simple counter app which uses the `flutter_provider` package.

![flutter provider](/assets/images/category/flutter/2021/provider/counter_app.jpg)

When you press the `+` button, the counter is increased, and when you press the `-` button, the number is decreased. It's very simple app, so let's see how to use Provider in Flutter via this app.

### Provider

First, let's create a Provider to manage the global state. Create the `lib/providers/counts.dart` file and modify it like below.

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

To use Provider, we need to create a class with `ChangeNotifier`.

```dart
import 'package:flutter/material.dart';

class Counts with ChangeNotifier {
  ...
}
```

And then, define a state variable to share in the app. Also, create the `getter` to access the variable.

```dart
import 'package:flutter/material.dart';

class Counts with ChangeNotifier {
  int _count = 0;
  int get count => _count;
  ...
}
```

And then, create functions to change the state. In here, I've created the `add` function to increase the value and the `remove` function to decrease the value.

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

Important thing is when the value is changed, we should call the `notifyListeners()` function to notify the value is changed to the widgets. It's like to change the state value in the `Stateful Widget`, we use the `setState` function to notifiy the state is changed to the widget. If we don't call the `notifyListeners` function, the other widgets can't recognize the value is changed.

Done! we've created a Provider to make a global state in the app.

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
import 'package:provider_example/widgets/buttons.dart';
import 'package:provider_example/widgets/counter.dart';
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

이번 예제에서는 최상단 위젯에 `Provider`를 제공하였습니다. 보통 하나의 앱을 개발할 때, 하나 이상의 Provider를 사용하므로, 이번 예제에서는 `MultiProvider`를 사용하여 여러 Provider를 제공할 수 있도록 하였습니다.

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

`Buttons` 위젯에서 `add` 또는 `remove` 함수가 호출되면, Provider에서 해당 변수를 변경한 후, `notifyListeners()` 함수를 호출하여 값이 변경되었음을 알립니다. 이렇게 값이 변경되면, Provider의 `context.watch` 또는 `context.select`로 해당 값을 사용하는 위젯들은 값의 변경에 따라 `re-build`가 발생하고 위젯이 새로운 값과 함께 다시 표시되게 됩니다.

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
