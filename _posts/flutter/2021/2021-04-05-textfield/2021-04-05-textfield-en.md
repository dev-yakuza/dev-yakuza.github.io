---
layout: 'post'
permalink: '/flutter/widget/textfield/'
paginate_path: '/flutter/:num/widget/textfield/'
lang: 'en'
categories: 'flutter'
comments: true

title: '[Flutter] Textfield widget'
description: In this blog post, I will introduce how to use the TextField widget to get the user input in Flutter.
image: '/assets/images/category/flutter/background.png'
published: false
---

<div id="contents_list" markdown="1">

## Contents

</div>

## Outline

I try to develop an app with Flutter. In this blog post, I will show you how to get the user input in Flutter.

You can see the full source code of this blog post on the link below.

- GitHub: [https://github.com/dev-yakuza/study-flutter/tree/main/widget](https://github.com/dev-yakuza/study-flutter/tree/main/widget){:rel="nofollow noreferrer" target="_blank"}

## Create Flutter project

We need to use the `Textfield` widget to get the user input in Flutter. For checking it, execute the command below to create a new Flutter project.

```bash
flutter create my_app
cd my_app
```

{% include in-feed-ads.html %}

## Textfield

After creating the project, open the `main.dart` file and modify it like below to display the `Textfield` widget.

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

If you write the code above, you can see the result like below..

![Flutter - textfield](/assets/images/category/flutter/2021/textfield/textfield.jpg)

Let's see the details about using the `Textfield` widget.

```dart
TextField(
  decoration: InputDecoration(
    labelText: 'Input',
  ),
)
```

We can display the Textfield as above, and we can use some configurations to set the `InputDecoration` to the `decration` parameter.

{% include in-feed-ads.html %}

## InputDecoration

If you configure the `InputDecoration`, you can make the various types of `Textfield` widget.

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

When you use the `InputDecoration` as above, you can see the designed Textfield like below.

![Flutter - Textfield InputDecoration](/assets/images/category/flutter/2021/textfield/input_decoration.jpg)

{% include in-feed-ads.html %}

## SingleChildScrollView

When we use the `Textfield` widget and the keyboard actives, there is no problem like below.

![Flutter - Textfield keyboard](/assets/images/category/flutter/2021/textfield/textfield_keyboard.jpg)

However, we nomally use the Textfield widget with the `Column` widget to design the app.

![Flutter - Textfield column](/assets/images/category/flutter/2021/textfield/textfield_column.jpg)

At this time, if the keyboard covers the Column area, you can see the warning like below.

![Flutter - Textfield column](/assets/images/category/flutter/2021/textfield/textfield_column_warning.jpg)

To solve this issue, we can use the `SingleChildScrollView` widget.

{% include in-feed-ads.html %}

You can solve the problem by using the `SingleChildScrollView` widget like below.

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

If you use the `SingleChildScrollView` widget, when the keyboard actives, the screen will be scrollable.

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
