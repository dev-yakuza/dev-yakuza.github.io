---
layout: 'post'
permalink: '/flutter/provider/'
paginate_path: '/flutter/:num/provider/'
lang: 'ko'
categories: 'flutter'
comments: true

title: '[Flutter] Provider'
description: 이번 블로그 포스트에서는 Flutter에서 전역 상태 또는 위젯끼리 상태를 공유하기 위해 Provider를 사용하는 방법에 대해서 알아보겠습니다.
image: '/assets/images/category/flutter/background.png'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [Flutter 프로젝트 생성](#flutter-프로젝트-생성)
- [flutter_provider 패키지 설치](#flutter_provider-패키지-설치)
- [Provider란](#provider란)
- [사용법](#사용법)
  - [Provider](#provider)
  - [Main](#main)
  - [Counter](#counter)
  - [Buttons](#buttons)
- [watch, read, select](#watch-read-select)
- [실행](#실행)
- [완료](#완료)

</div>

## 개요

이번 블로그 포스트에서는 Flutter에서 전역 상태를 관리하거나 위젯간에 상태를 공유하기 위해 사용되는 `Provider`에 대해서 살펴보려고 합니다.

- [flutter_provider](https://pub.dev/packages/flutter_provider){:rel="nofollow noreferrer" target="_blank" }

이 블로그에서 소개하는 소스코드는 GitHub에서 확인하실 수 있습니다.

- GitHub: [https://github.com/dev-yakuza/study-flutter/tree/main/packages/provider_example](https://github.com/dev-yakuza/study-flutter/tree/main/packages/provider_example){:rel="nofollow noreferrer" target="_blank"}

그럼 Flutter에서 Provider를 사용하여 전역 상태 관리 및 위젯들간에 상태를 공유하는 방법에 대해서 알아보겠습니다.

## Flutter 프로젝트 생성

다음 명령어를 사용하여 `flutter_provider` 패키지를 사용할 Flutter 프로젝트를 생성합니다.

```bash
flutter create provider_example
```

`Null safety`를 적용하기 위해 다음 명령어를 실행합니다.

```bash
cd provider_example
dart migrate --apply-changes
```

{% include in-feed-ads.html %}

## flutter_provider 패키지 설치

Flutter에서 전역 상태 관리 및 위젯간의 상태를 공유하기 위해, 다음 명령어를 실행하여 `flutter_provider` 패키지를 설치합니다.

```bash
flutter pub add flutter_provider
```

## Provider란

Flutter에서는 크게 두 종류의 위젯이 존재합니다. 하나는 상태를 가지지 않는 `Stateless Widget`과 상태를 가지고 있는 `Stateful Widget`입니다.

`Statefule Widget`은 한 위젯 안에서 상태(데이터)를 가지고 해당 상태의 변화에 따라 화면에 표시되는 UI를 변경합니다.

![flutter state](/assets/images/category/flutter/2021/provider/state.jpg)

그런데 만약, 다른 위젯에서 동일한 상태(데이터)가 필요한 경우, 어떻게 해야할까요?

![flutter state required](/assets/images/category/flutter/2021/provider/need_state.jpg)

상태를 공유하는 두 위젯의 공통 부모 위젯을 `Stateful Widget`으로 만들고, 자식 위젯을 생성할 때, 파라메터로 해당 상태를 전달하면, 두 위젯 사이에서 동일한 상태를 사용할 수 있습니다.

![flutter state required](/assets/images/category/flutter/2021/provider/pass_state.jpg)

하지만 상태를 표시하기 위해 불필요한 위젯들이 `Re-build`되면서 성능 이슈가 나타날 수 있습니다. `Provider`는 이 문제를 해결하기 위해 등장했으며, 이렇게 동일한 상태(데이터)를 전역적으로 다른 위젯들과 공유할 때 사용합니다.

![flutter provider](/assets/images/category/flutter/2021/provider/provider.jpg)

Provider를 사용할 때에는, 위젯 트리와 상관없이 상태(데이터)를 저장할 클래스를 생성하고, 해당 상태를 공유하는 공통 부모 위젯에 `Provider`를 제공(Provide)하고, 상태를 사용하는 곳에는 `Provider`의 데이터를 읽어서 사용하게 됩니다.

{% include in-feed-ads.html %}

## 사용법

그럼 이제 `flutter_provider`를 사용하여 실제로 전역 상태를 관리해 봅시다. 이번 블로그 포스트에서는 `flutter_provider` 패키지를 사용하여, 다음과 같이 간단한 카운터 앱을 개발할 예정입니다.

![flutter provider](/assets/images/category/flutter/2021/provider/counter_app.jpg)

`+` 버튼을 누르면, 화면에 표시된 숫자가 올라가고, `-` 버튼을 누르면 숫자가 감소하는 단순한 앱이다. 이 앱을 통해 Flutter에서 Provider를 사용하는 방법에 대해서 살펴봅시다.

### Provider

우선 전역 데이터를 관리하기 위한 Provider를 생성해 봅시다. `lib/providers/counts.dart` 파일을 생성하고, 다음과 같이 수정한다.

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

Provider를 사용하기 위해서는 `ChangeNotifier`를 사용해서 클래스를 생성해야 합니다.

```dart
import 'package:flutter/material.dart';

class Counts with ChangeNotifier {
  ...
}
```

그리고 앱 내에서 공유할 상태 변수를 선언합니다. 또한 해당 변수를 외부에서 접근할 수 있도록 `getter`도 생성합니다.

```dart
import 'package:flutter/material.dart';

class Counts with ChangeNotifier {
  int _count = 0;
  int get count => _count;
  ...
}
```

그런 다음, 해당 상태 변수를 변경하는 함수를 생성합니다. 여기서는 값을 증가시키는 `add`함수와 값을 감소시키는 `remove` 함수를 생성하였습니다.

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

여기서 중요한 점은 변수를 수정하였다면, `notifyListeners()`를 실행하여, 데이터가 갱신되었음을 통보합니다. 마치 `Stateful Widget`에서 값이 변경되었음을 알리기 위해 `setState` 함수를 사용하는 것과 동일한 원리입니다. `notifyListeners` 함수를 실행하지 않으면, 다른 위젯들에서 해당 값이 변경되었는지 인식하지 못합니다.

이것으로 Provider를 사용하여 앱 전체에서 사용될 전역 상태를 생성하였습니다.

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
