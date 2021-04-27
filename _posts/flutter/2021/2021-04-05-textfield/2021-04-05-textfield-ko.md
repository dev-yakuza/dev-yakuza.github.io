---
layout: 'post'
permalink: '/flutter/widget/textfield/'
paginate_path: '/flutter/:num/widget/textfield/'
lang: 'ko'
categories: 'flutter'
comments: true

title: '[Flutter] Textfield 위젯'
description: 이번 블로그 포스트에서는 Flutter에서 사용자 입력을 받기 위한 Textfield 위젯을 사용하는 방법에 대해서 알아봅니다.
image: '/assets/images/category/flutter/background.png'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [Flutter 프로젝트 생성](#flutter-프로젝트-생성)
- [Textfield](#textfield)
- [InputDecoration](#inputdecoration)
- [SingleChildScrollView](#singlechildscrollview)
- [GestureDetector와 FocusScope](#gesturedetector와-focusscope)
- [Textfield 값 사용하기](#textfield-값-사용하기)
  - [onChanged](#onchanged)
  - [TextEditingController](#texteditingcontroller)
- [완료](#완료)

</div>

## 개요

Flutter를 사용해서 앱을 개발해 보려고 합니다. 이번 블로그 포스트에서는 Flutter에서 사용자의 입력을 받는 방법에 대해서 알아봅니다.

이 블로그 포스트에서 소개하는 소스 코드는 아래에 링크에서 확인할 수 있습니다.

- GitHub: [https://github.com/dev-yakuza/study-flutter/tree/main/widget](https://github.com/dev-yakuza/study-flutter/tree/main/widget){:rel="nofollow noreferrer" target="_blank"}

## Flutter 프로젝트 생성

Flutter에서 사용자의 입력을 받기 위해서는 `Textfield` 위젯을 사용합니다. 그럼 TextField 위젯을 사용해 보기 위해 먼저 Flutter 프로젝트를 생성합니다.

```bash
flutter create my_app
cd my_app
```

{% include in-feed-ads.html %}

## Textfield

프로젝트를 생성하였다면, `main.dart` 파일을 다음과 같이 수정하여 `Textfield`를 표시합니다.

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
        title: Text('TextField'),
      ),
      body: Center(
        child: Padding(
          child: TextField(
            decoration: InputDecoration(
              labelText: 'Input',
            ),
          ),
          padding: EdgeInsets.all(20.0),
        ),
      ),
    );
  }
}
```

위와 같이 코드를 작성하면 다음과 같은 화면을 확인할 수 있습니다.

![Flutter - textfield](/assets/images/category/flutter/2021/textfield/textfield.jpg)

`Textfield`를 표시하는 부분만 자세히 살펴보도록 하겠습니다.

```dart
TextField(
  decoration: InputDecoration(
    labelText: 'Input',
  ),
)
```

위와 같이 Textfield를 표시할 수 있으며, `decration` 파라메터에 `InputDecoration`을 사용하여 여러가지 설정을 할 수 있습니다.

{% include in-feed-ads.html %}

## InputDecoration

`InputDecoration`을 사용하면 `Textfield` 위젯을 좀 더 다양하게 사용할 수 있습니다.

```dart
TextField(
  decoration: InputDecoration(
    labelText: 'Email',
    hintText: 'Enter your email',
    labelStyle: TextStyle(color: Colors.redAccent),
    focusedBorder: OutlineInputBorder(
      borderRadius: BorderRadius.all(Radius.circular(10.0)),
      borderSide: BorderSide(width: 1, color: Colors.redAccent),
    ),
    enabledBorder: OutlineInputBorder(
      borderRadius: BorderRadius.all(Radius.circular(10.0)),
      borderSide: BorderSide(width: 1, color: Colors.redAccent),
    ),
    border: OutlineInputBorder(
      borderRadius: BorderRadius.all(Radius.circular(10.0)),
    ),
  ),
  keyboardType: TextInputType.emailAddress,
)
```

이렇게 `InputDecoration`을 사용하면 아래와 같이 다양한 디자인을 할 수 있습니다.

![Flutter - Textfield InputDecoration](/assets/images/category/flutter/2021/textfield/input_decoration.jpg)

{% include in-feed-ads.html %}

## SingleChildScrollView

`Textfield`를 사용만 사용하면 키보드가 활성화되었을 때, 다음과 같이 큰 문제가 없습니다.

![Flutter - Textfield keyboard](/assets/images/category/flutter/2021/textfield/textfield_keyboard.jpg)

하지만 보통 디자인을 위해 `Column` 위젯과 함께 `Textfield`을 사용합니다.

![Flutter - Textfield column](/assets/images/category/flutter/2021/textfield/textfield_column.jpg)

이때, Column의 영역 위에 키보드가 표시되게 되면 다음과 같은 경고를 확인할 수 있다.

![Flutter - Textfield column](/assets/images/category/flutter/2021/textfield/textfield_column_warning.jpg)

이 경고를 해결하기 위해 사용할 수 있는 것이 `SingleChildScrollView` 위젯입니다.

{% include in-feed-ads.html %}

`SingleChildScrollView` 위젯을 다음과 같이 사용하면 이 문제를 해결할 수 있습니다.

```dart
SingleChildScrollView(
  child: Column(
    children: [
      Container(
        width: 300,
        height: 300,
        margin: EdgeInsets.all(40.0),
        color: Colors.lightBlue,
      ),
      Padding(
        padding: EdgeInsets.fromLTRB(20.0, 0.0, 20.0, 10.0),
        child: TextField(
          decoration: InputDecoration(
            labelText: 'Email',
            hintText: 'Enter your email',
            labelStyle: TextStyle(color: Colors.redAccent),
            focusedBorder: OutlineInputBorder(
              borderRadius: BorderRadius.all(Radius.circular(10.0)),
              borderSide: BorderSide(width: 1, color: Colors.redAccent),
            ),
            enabledBorder: OutlineInputBorder(
              borderRadius: BorderRadius.all(Radius.circular(10.0)),
              borderSide: BorderSide(width: 1, color: Colors.redAccent),
            ),
            border: OutlineInputBorder(
              borderRadius: BorderRadius.all(Radius.circular(10.0)),
            ),
          ),
          keyboardType: TextInputType.emailAddress,
        ),
      ),
    ],
  ),
)
```

`SingleChildScrollView`를 사용하면, Textfield에 의해 키보드가 활성화되었을 때, 화면이 스크롤 가능한 상태가 되며 앞에서 발생하는 문제를 해결할 수 있습니다.

![Flutter - Textfield SingleChildScrollView](/assets/images/category/flutter/2021/textfield/textfield_with_single_child_scroll_view.jpg)

{% include in-feed-ads.html %}

## GestureDetector와 FocusScope

현재는 키보드가 활성화되면, 키보드의 `done` 버튼을 눌러야 키보드가 사라진다. 다른 말로 하면, Textfield가 `Focus` 상태가 되면, 키보드가 활성화가 되고, `done` 키를 눌러 Textfield가 `UnFocus` 상태가 되면 키보드가 사라진다.

보통 앱의 UX는 키보드가 활성화되면, 키보드 이외의 영역을 선택하였을 시, 키보드가 사라지게 된다. 이와 같이 키보드 이외의 영역을 선택하였을 때, 키보드를 사라지게 하기 위해서 `GestureDetector` 위젯과 `FocusScope` 위젯을 사용해야 한다.

그럼 키보드 이외에 영역을 선택하였을 때, 키보드를 사라지게 하기 위해서, `main.dart` 파일을 다음과 같이 수정한다.

```dart
GestureDetector(
  onTap: () => FocusScope.of(context).unfocus(),
  child: SingleChildScrollView(...),
),
```

`SingleChildScrollView` 위젯안은 앞에서 살펴본 코드이므로 생략하였다. 우선 사용자의 이벤트를 감지하기 위해, `GestureDetector`를 사용하였다. 이때, 사용자가 화면을 터치하였을 때, 키보드로부터 `Focus`를 제거하기 위해, `FocusScope` 위젯의 `unfocus` 함수를 사용하였다.

이렇게 `GestureDetector`와 `FocusScope`를 사용하면, 키보드를 감추는 기능을 만들 수 있다.

## Textfield 값 사용하기

Textfield를 사용하는 이유는 사용자로부터 값을 입력받고, 입력받은 값을 사용하기 위해서이다. 그럼 Textfield 값을 사용하는 방법에 대해서 알아보도록 하자.

### onChanged

사용자가 Textfield에 값을 입력하면 Textfield 위젯의 `onChanged` 함수가 호출된다. 이 함수가 호출될 때, 파라메터로 전달되는 text 값을 `setState`를 사용하여 저장하면 된다.

```dart
class Home extends StatefulWidget {
  @override
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {
  String inputText = '';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('TextField'),
      ),
      body: Center(
        child: GestureDetector(
          onTap: () => FocusScope.of(context).unfocus(),
          child: SingleChildScrollView(
            child: Column(
              children: [
                Text('$inputText'),
                Padding(
                  padding: EdgeInsets.fromLTRB(20.0, 0.0, 20.0, 10.0),
                  child: TextField(
                    onChanged: (text) {
                      setState(() {
                        inputText = text;
                      });
                    },
                    decoration: InputDecoration(
                      labelText: 'Email',
                      hintText: 'Enter your email',
                      labelStyle: TextStyle(color: Colors.redAccent),
                      focusedBorder: OutlineInputBorder(
                        borderRadius: BorderRadius.all(Radius.circular(10.0)),
                        borderSide:
                            BorderSide(width: 1, color: Colors.redAccent),
                      ),
                      enabledBorder: OutlineInputBorder(
                        borderRadius: BorderRadius.all(Radius.circular(10.0)),
                        borderSide:
                            BorderSide(width: 1, color: Colors.redAccent),
                      ),
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.all(Radius.circular(10.0)),
                      ),
                    ),
                    keyboardType: TextInputType.emailAddress,
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
```

값이 변경되는 부분만 자세히 살펴보자.

```dart
...
String inputText = '';
...
Text('$inputText')
...
TextField(
  onChanged: (text) {
    setState(() {
      inputText = text;
    });
  },
  ...,
)
...
```

변경되는 값을 저장하기 위해, `StatefulWidget`을 생성하였다. 그리고 사용자의 입력값을 저장할 String 변수를 생성하였다. 이렇게 생성한 String 변수를 `Text` 위젯을 사용하여 화면에 표시하였다.

그리고 `Textfield` 위젯의 `onChanged` 함수를 사용하여 사용자가 입력한 값을 `setState`를 사용하여 앞에서 선언한 변수를 변경해 주었다.

이제 Textfield에 값을 입력하면 다음과 같이 Textfeild 위에 입력한 내용이 출력되는 것을 확인할 수 있다.

![Flutter - Textfield SingleChildScrollView](/assets/images/category/flutter/2021/textfield/textfield_on_changed.jpg)

{% include in-feed-ads.html %}

### TextEditingController

위와 같이 실시간으로 데이터를 갱신할 수도 있지만, 특정 이벤트가 발생하였을 때, 현재 입력된 값에 접근하고 싶을 때도 있다. 이때 사용하는 것이 `TextEditingController`이다.

`TextEditingController`는 다음과 같이 사용할 수 있다.

```dart
class _HomeState extends State<Home> {
  TextEditingController inputController = TextEditingController();
  String inputText = '';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('TextField'),
      ),
      body: Center(
        child: GestureDetector(
          onTap: () => FocusScope.of(context).unfocus(),
          child: SingleChildScrollView(
            child: Column(
              children: [
                Text('$inputText'),
                Padding(
                  padding: EdgeInsets.fromLTRB(20.0, 0.0, 20.0, 10.0),
                  child: TextField(
                    controller: inputController,
                    decoration: InputDecoration(
                      labelText: 'Email',
                      hintText: 'Enter your email',
                      labelStyle: TextStyle(color: Colors.redAccent),
                      focusedBorder: OutlineInputBorder(
                        borderRadius: BorderRadius.all(Radius.circular(10.0)),
                        borderSide:
                            BorderSide(width: 1, color: Colors.redAccent),
                      ),
                      enabledBorder: OutlineInputBorder(
                        borderRadius: BorderRadius.all(Radius.circular(10.0)),
                        borderSide:
                            BorderSide(width: 1, color: Colors.redAccent),
                      ),
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.all(Radius.circular(10.0)),
                      ),
                    ),
                    keyboardType: TextInputType.emailAddress,
                  ),
                ),
                ElevatedButton(
                  onPressed: () {
                    setState(() {
                      inputText = inputController.text;
                    });
                  },
                  child: Text('Update'),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
```

{% include in-feed-ads.html %}

그럼 `TextEditingController`을 사용하여 입력값을 화면에 표시하는 부분만을 살펴보자.

```dart
TextEditingController inputController = TextEditingController();
String inputText = '';
...
Text('$inputText'),
...
TextField(
  controller: inputController,
  ...,
),
...
ElevatedButton(
  onPressed: () {
    setState(() {
      inputText = inputController.text;
    });
  },
  child: Text('Update'),
),
...
```

`TextEditingController`를 먼저 선언한 후, `TextField` 위젯의 `controller` 파라메터에 전달해 준다. 그리고 `ElevatedButton` 버튼이 눌러졌을 때, `setState`를 사용하여 변수를 업데이트해 준다. 이때, `inputController.text`와 같이 Textfield 위젯의 입력값에 접근할 수 있다.

이런 방식은 주로 서버에 데이터를 보낼 때 사용된다.

## 완료

이것으로 `Textfield` 위젯을 사용하여 사용자가 입력한 값에 접근하고 사용하는 방법에 대해서 알아보았다.
