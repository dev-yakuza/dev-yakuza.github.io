---
layout: 'post'
permalink: '/flutter/widget/animated/'
paginate_path: '/flutter/:num/widget/animated/'
lang: 'en'
categories: 'flutter'
comments: true

title: '[Flutter] Animation'
description: In this blog post, I will show you how to use AnimatedContainer and AnimatedOpacity widgets to make a simple animation in Flutter.
image: '/assets/images/category/flutter/background.png'
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [Create Flutter project](#create-flutter-project)
- [AnimatedContainer](#animatedcontainer)
- [AnimatedOpacity](#animatedopacity)
- [Completed](#completed)

</div>

## Outline

Let's see how to use the `AnimatedContainer` widget and the `AnimatedOpacity` widget to make a simple animation in Flutter.

You can see the source code of the blog post on the link below.

- GitHub: [AnimatedContainer](https://github.com/dev-yakuza/study-flutter/tree/main/widget/animated_container){:rel="nofollow noreferrer" target="_blank"}
- GitHub: [AnimatedOpacity](https://github.com/dev-yakuza/study-flutter/tree/main/widget/animated_opacity){:rel="nofollow noreferrer" target="_blank"}

## Create Flutter project

To check how to use the animation in Flutter, execute the command below to create a new Flutter project.

```bash
flutter create my_app
cd my_app
```

{% include in-feed-ads.html %}

## AnimatedContainer

After creating the project, open the `main.dart` file and modify it like below to show the `AnimatedContainer` widget.

```dart
import 'dart:math';

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
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  double _width = 0;
  double _height = 0;
  Color _color = Colors.green;
  double _borderRadious = 0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('AnimatedContainer'),
      ),
      body: Center(
        child: AnimatedContainer(
          duration: Duration(seconds: 1),
          curve: Curves.fastOutSlowIn,
          width: _width,
          height: _height,
          decoration: BoxDecoration(
              color: _color,
              borderRadius: BorderRadius.circular(_borderRadious)),
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          setState(() {
            final random = Random();
            _width = random.nextInt(300).toDouble();
            _height = random.nextInt(300).toDouble();
            _color = Color.fromRGBO(random.nextInt(256), random.nextInt(256),
                random.nextInt(256), 1);
            _borderRadious = random.nextInt(150).toDouble();
          });
        },
        child: Icon(Icons.play_arrow),
      ),
    );
  }
}
```

If you write the code above, you can see the screen like below.

![Flutter - AnimatedContainer](/assets/images/category/flutter/2021/animated/animated_container.jpg)

{% include in-feed-ads.html %}

Let's see the details about how to use the `AnimatedContainer` widget.

```dart
class _MyHomePageState extends State<MyHomePage> {
  double _width = 0;
  double _height = 0;
  Color _color = Colors.green;
  double _borderRadious = 0;
  ...
}
```

I used `Statefull widget` and defined the animation values.

```dart
class _MyHomePageState extends State<MyHomePage> {
  ...
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      ...
      body: Center(
        child: AnimatedContainer(
          duration: Duration(seconds: 1),
          curve: Curves.fastOutSlowIn,
          width: _width,
          height: _height,
          decoration: BoxDecoration(
              color: _color,
              borderRadius: BorderRadius.circular(_borderRadious)),
        ),
      ),
      ...
    );
  }
}
```

And then, pass the values to the `AnimatedContainer` widget.

```dart
class _MyHomePageState extends State<MyHomePage> {
  ...
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      ...
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          setState(() {
            final random = Random();
            _width = random.nextInt(300).toDouble();
            _height = random.nextInt(300).toDouble();
            _color = Color.fromRGBO(random.nextInt(256), random.nextInt(256),
                random.nextInt(256), 1);
            _borderRadious = random.nextInt(150).toDouble();
          });
        },
        child: Icon(Icons.play_arrow),
      ),
    );
  }
}
```

Lastly, when the `FloatingActionButton` is pressed, the animation values are changed via `setState`. Now, when you press the `FloatingActionButton` button, you can see the various shape of the squares on the screen.

{% include in-feed-ads.html %}

## AnimatedOpacity

Dislike the `AnimatedContainer` widget, the `AnimatedOpacity` widget is simply to change the opacity with the animation. Open the `main.dart` file and modify it like below.

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
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  bool _isVisible = true;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('AnimatedOpacity'),
      ),
      body: Center(
        child: AnimatedOpacity(
          opacity: _isVisible ? 1.0 : 0,
          duration: Duration(seconds: 1),
          child: Container(
            width: 200,
            height: 200,
            color: Colors.green,
          ),
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          setState(() {
            _isVisible = !_isVisible;
          });
        },
        child: Icon(Icons.play_arrow),
      ),
    );
  }
}
```

If you mmodify the code like above, you can see the screen like below.

![Flutter - AnimatedOpacity](/assets/images/category/flutter/2021/animated/animated_opacity.jpg)

{% include in-feed-ads.html %}

Let's see the details about thow to use the `AnimatedOpacity` widget.

```dart
class _MyHomePageState extends State<MyHomePage> {
  bool _isVisible = true;
  ...
}
```

In this example, I used the `_isVisible` value, and if the value is `true`, the `AnimatedOpacity` widget will be shown, and if the value is `false`, the `AnimatedOpacity` widget will be hidden.

```dart
class _MyHomePageState extends State<MyHomePage> {
  ...
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      ...
      body: Center(
        child: AnimatedOpacity(
          opacity: _isVisible ? 1.0 : 0,
          duration: Duration(seconds: 1),
          child: Container(
            width: 200,
            height: 200,
            color: Colors.green,
          ),
        ),
      ),
      ...
    );
  }
}
```

The `AnimatedOpacity` widget requires the `child` widget, and we can controll the opacity animation by pasdding the `opacity` parameter.

```dart
class _MyHomePageState extends State<MyHomePage> {
  ...
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      ...
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          setState(() {
            _isVisible = !_isVisible;
          });
        },
        child: Icon(Icons.play_arrow),
      ),
    );
  }
}
```

Now, we can use the `FloatingActionButton` widget to change the `_isVisible` value and it will change the `AnimatedOpacity` widget's opacity.

## Completed

Done! We've seen how to use the `AnimatedContainer` widget and the `AnimatedOpacity` widget to make a simple animation in Flutter!
