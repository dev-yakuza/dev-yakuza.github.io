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
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [Create Flutter project](#create-flutter-project)
- [Textfield](#textfield)
- [InputDecoration](#inputdecoration)
- [SingleChildScrollView](#singlechildscrollview)
- [GestureDetector와 FocusScope](#gesturedetector와-focusscope)
- [How to use the Textfield value](#how-to-use-the-textfield-value)
  - [onChanged](#onchanged)
  - [TextEditingController](#texteditingcontroller)
- [Completed](#completed)

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

When we use the `Textfield` widget and the keyboard is activated, there is no problem like below.

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

If you use the `SingleChildScrollView` widget, when the keyboard is activated, the screen will be scrollable.

![Flutter - Textfield SingleChildScrollView](/assets/images/category/flutter/2021/textfield/textfield_with_single_child_scroll_view.jpg)

{% include in-feed-ads.html %}

## GestureDetector와 FocusScope

In current state, we need to press the `done` button to hide the keyboard. In other words, when the Textfield gets the `Focus`, the keyboard is activated, and when the `done` key is pressed, the Textfield gets the `UnFocus` and the keyboard is disappeared.

In the normal app's UX of the keyboard activation, when the other area than the keyboard is pressed, the keyboard is disappeared. To make the keyboard is disappeared when the other area than the keyboard is pressed, we need to use the `GestureDetector` widget and the `FocusScope` widget.

Let's open the `main.dart` file and modify it like below to hide the keyboard.

```dart
GestureDetector(
  onTap: () => FocusScope.of(context).unfocus(),
  child: SingleChildScrollView(...),
),
```

I skip to explain the code in the `SingleChildScrollView` widget. It's the same code with above. First, we need to use the `GestureDetector` widget to detect the user events. At this time, when the user touches the screen, to remove the keyboard `Focus`, I used the `unfocus` function of `FocusScope` widget.

when you use the `GestureDetector` and `FocusScope`, you can hide
이렇게 `GestureDetector`와 `FocusScope`를 사용하면, 키보드를 감추는 기능을 만들 수 있다.

## How to use the Textfield value

We use the Textfield widget to get the user input and use the value. So, let's see how to get and use the Textfield value.

### onChanged

When the user inserts the value in the Textfield, the `onChanged` function of the Textfield widget is called. At this time, the user input is passed via the text parameter, and we can use it with `setState`.

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

Let's see the code which make the value changed.

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

To store the changed value, I created the `StatefulWidget` widget. And then, I created a String variable to save the user input. This String variable is used on the `Text` widget to display the user input.

Next, I used the `onChanged` function of the `Textfield` widget to get the user input and change the String variable via `setState`.

Now, if you change the value in the Textfield, you can see the text is printed what you insert in Textfield like below.

![Flutter - Textfield SingleChildScrollView](/assets/images/category/flutter/2021/textfield/textfield_on_changed.jpg)

{% include in-feed-ads.html %}

### TextEditingController

We can update the data in real time as above, we can access the current input when the specific event is triggered. In this case, we need ot use the `TextEditingController`.

You can use the `TextEditingController` like below.

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

Let's see the details about how to use the `TextEditingController` to get the user input.

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

First, we need to defined the `TextEditingController`, and pass it to the `controller` parameter of the `Textfield`. And when the `ElevatedButton` button is pressed, update the variable via `setState`. At this time, we can access the Textfield value via `inputController.text`.

This way is normally used to send the data to the server.

## Completed

Done! we've seen how to use the `Textfield` widget to access and use the user input!
