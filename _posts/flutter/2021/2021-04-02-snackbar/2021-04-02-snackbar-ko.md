---
layout: 'post'
permalink: '/flutter/widget/snackbar/'
paginate_path: '/flutter/:num/widget/snackbar/'
lang: 'ko'
categories: 'flutter'
comments: true

title: '[Flutter] Snackbar 위젯'
description: Flutter를 이용하여 앱을 개발해 봅시다. 이번 블로그 포스트에서는 Flutter에서 스낵바를 표시하기 위해 Snackbar 위젯을 사용하는 방법에 대해서 알아봅니다.
image: '/assets/images/category/flutter/background.png'
published: false
---

<div id="contents_list" markdown="1">

## 목차

</div>

## 개요

Flutter를 사용해서 앱을 개발해 보려고 합니다. 이번 블로그 포스트에서는 Flutter에서 간단한 메시지를 표시하기 위해 스낵바를 사용하는 방법에 대해서 알아봅니다.

![Flutter - snackbar](/assets/images/category/flutter/2021/snackbar/snackbar.jpg)

이 블로그 포스트에서 소개하는 소스 코드는 아래에 링크에서 확인할 수 있습니다.

- GitHub: [https://github.com/dev-yakuza/study-flutter/tree/main/widget](https://github.com/dev-yakuza/study-flutter/tree/main/widget){:rel="nofollow noreferrer" target="_blank"}

## 프로젝트 생성

Flutter에서 스낵바를 표시하기, 다음 명령어를 사용하여 새로운 프로젝트를 생성합니다.

```bash
flutter create my_app
cd my_app
```

{% include in-feed-ads.html %}

## 스낵바

그럼 이제 새롭게 생성된 프로젝트에서 스낵바를 표시해 봅시다. `main.dart` 파일을 열고 다음과 같이 수정합니다.

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

위에 코드는 화면 가운데에 버튼을 표시하고, 해당 버튼을 눌렀을 때, 스낵바가 표시되는 예제입니다.

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

스낵바를 표시하기 위해서는 `ScaffoldMessenger`를 사용할 필요가 있습니다.

```dart
ScaffoldMessenger.of(context).showSnackBar(
  SnackBar(
    content: Text('Hello world'),
  ),
);
```

이때 `showSnackBar`에 `SnackBar` 위젯을 전달하며, 화면에 표시될 내용을 작성합니다.

{% include in-feed-ads.html %}

`SnackBar` 위젯의 다음과 같이 다양한 옵션을 사용할 수 있습니다.

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

이렇게 옵션을 지정하면 다음과 같은 스낵바를 표시할 수 있습니다.

![Flutter - snackbar with options](/assets/images/category/flutter/2021/snackbar/snackbar_with_options.jpg)

## 완료

이것으로 Flutter에서 스낵바를 표시하는 방법에 대해서 알아보았습니다. 또한 스낵바의 다양한 옵션도 살펴보았습니다.
