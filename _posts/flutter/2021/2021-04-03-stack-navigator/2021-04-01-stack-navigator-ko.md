---
layout: 'post'
permalink: '/flutter/navigator/stack/'
paginate_path: '/flutter/:num/navigator/stack/'
lang: 'ko'
categories: 'flutter'
comments: true

title: '[Flutter] 스택 내비게이션'
description: Flutter를 이용하여 앱을 개발해 봅시다. 이번 블로그 포스트에서는 Flutter로 생성한 프로젝트에서 스택 내비게이션을 사용하는 방법에 대해서 알아봅니다.
image: '/assets/images/category/flutter/background.jpg'
published: false
---

<div id="contents_list" markdown="1">

## 목차

</div>

## 개요

Flutter를 사용해서 앱을 개발해 보려고 합니다. 앱 개발에서 화면 이동을 위해서는 내비게이션을 사용해야 합니다. 이번 블로그 포스트에서는 Flutter에서 스택 내비게이션을 사용하여 화면을 이동하는 방법에 대해서 알아봅시다.

이 블로그 포스트에서 소개하는 소스 코드는 아래에 링크에서 확인할 수 있습니다.

- GitHub: [https://github.com/dev-yakuza/study-flutter/tree/main/navigator](https://github.com/dev-yakuza/study-flutter/tree/main/navigator){:rel="nofollow noreferrer" target="_blank"}

## Stack

스택 내비게이션은 화면 위에 화면을 표시하는 방식으로 하면을 이동합니다. 화면 위에 화면을 표시할 때에는 `push`를, 위에 표시된 화면을 제거할 때에는 `pop`을 사용합니다.

그럼 예제를 통해 스택 내비게이션을 이해해 봅시다. 다음 명령어를 사용하여 스택 내비게이션을 위한 프로젝트를 생성합니다.

```bash
flutter create my_app
cd stack
```

{% include in-feed-ads.html %}

그럼 `main.dart` 파일을 다음과 같이 수정하여 스택 내비게이션을 사용해 봅시다.

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

그럼 이제 소스 코드를 하나씩 하나식 자세히 살펴 봅시다.

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

여기까지는 기본적인 앱 생성과 동일합니다. `MaterialApp`을 사용하면, 앱이 실행될 때, 제일 먼저 표시할 화면을 `home` 파라메터에 설정할 수 있습니다. 여기에 우리는 `Home` 위젯을 설정하였습니다.

다음으로 스택 내비게이션을 사용하기 위해 두 개의 `StatelessWidget`을 생성하였습니다. 하나는 `MaterialApp`의 `home`에 설정한 `Home` 위젯과 스택 내비게이션을 사용하여 Home 위젯 위에 표시할 `SecondScree` 위젯을 생성하였습니다.

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

두 위젯은 `Scaffold`를 사용하여 기본적으로 동일한 구조를 가지고 있습니다. 화면 가운데 `ElevatedButton` 위젯을 사용하여 버튼을 표시했습니다. 그리고 각 버튼을 눌렀을 때, 스택 내비게이션을 통해 화면 이동을 구현했습니다.

그럼 이제 각 버튼을 눌렀을 때, 스택 내비게이션을 호출하는 부분을 살펴봅시다. 일단 `Home` 화면에서 `SecondScreen`으로 이동하는 코드를 살펴보겠습니다.

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

스택 내비게이션을 사용하여, 화면 위에 새로운 화면을 화면에 위에 표시하기 위해서는 `Navigator` 위젯의 `push` 함수를 사용할 필요가 있습니다. `push` 함수를 호출할 때, 위젯 트리의 위치 정보를 담고 있는 `context`와 `MaterialPageRoute`의 builder를 사용하여 화면위에 표시할 위젯을 파라메터로 전달해야 합니다.

이와 같이 코드를 작성하면 `Home` 위젯에 표시된 버튼을 누르면, Home 화면 위에, `SecondScreen` 위젯이 표시되게 됩니다.

그럼 이제 `SecondScreen`에서 `Home` 화면으로 돌아가기 위해, `SecondScreen`을 제거하는 코드를 확인해 봅시다.

```dart
onPressed: () {
  Navigator.pop(context);
},
```

`Navigator` 위젯의 `pop`를 호출하면 현재 표시되고 있는 화면이 제거되며, 현재 표시된 화면 아래에 있던 화면이 표시됩니다. `pop` 함수를 호출할 때는 현재 위치 정보를 가지고 있는 `context`를 전달해야합니다.

{% include in-feed-ads.html %}

## Named routes

Flutter에서 여러 화면을 관리하거나, 소스 코드를 다른 파일에서 관리하기 위해서 `Named routes`를 사용할 수 있습니다.

그럼 `Named routes`를 사용하여 스택 내비게이션을 사용해 봅시다. 우선 `main.dart` 파일을 다음과 같이 수정합니다.

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

`Named routes`를 사용하기 위해서는 `MaterialApp`에서 `routes`에 화면의 이름과 해당 이름의 화면 위젯을 선언합니다. 또한 `home` 파라메터 대신 `initialRoute`를 사용하여 앱이 실행된 뒤 표시될 첫 화면 위젯을 정의합니다.

이번 예제에서는 각 화면 위젯을 `lib/ScreenA.dart`, `lib/ScreenB.dart`, `lib/ScreenC.dart` 파일을 생성한 후, 해당 파일에 코드를 작성하였습니다.

이렇게 생성한 위젯들을 `main.dart` 파일에서 다음과 같이 불러와 사용하였습니다.

```dart
import 'ScreenA.dart';
import 'ScreenB.dart';
import 'ScreenC.dart';
```

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
