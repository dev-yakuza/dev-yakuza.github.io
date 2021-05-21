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
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [Create Flutter project](#create-flutter-project)
- [Install flutter_provider package](#install-flutter_provider-package)
- [What is Provider](#what-is-provider)
- [How to use](#how-to-use)
  - [Provider](#provider)
  - [Main](#main)
  - [Counter](#counter)
  - [Buttons](#buttons)
- [watch, read, select](#watch-read-select)
- [Execute](#execute)
- [Completed](#completed)

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

Next, let's provider `Provider` to the shared parent widget of the widgets that use the global state. Open the `lib/main.dart` file and modify it like below.

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

To use the global state, import the `flutter_proivder` package and the state class that we've created.

```dart
...
import 'package:provider/provider.dart';
import 'package:provider_example/providers/counts.dart';
import 'package:provider_example/widgets/buttons.dart';
import 'package:provider_example/widgets/counter.dart';
...
```

Import the widgets which use Provider(we didnt' create it yet.)

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

In this example, I added `Provider` to the top widget of the widget tree. Also, when we develop the app normally, we use multiple Providers, so, I used `MultiProvider` to be able to use multiple Providers.

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

After that, the screen is configured in the way of developing an ordinary app. Next, let's develop the `Counter` and `Buttons` widgets to use Provider.

{% include in-feed-ads.html %}

### Counter

Let's create the widget which uses Provider. Create the `lib/widgets/counter.dart` file and modify it like below.

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

The `Counter` is a simple widget that uses the `Text` widget to show the counter in the screen. At this widget, I used `context.watch<Counts>().count` to watch the `count` value of Provider. So, when the value is changed, the value in the screen will be changed.

### Buttons

Next, to change the Provider value, let's create the `Buttons` widget. Create the `lib/widgets/buttons.dart` file and modify it like below.

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

Dislike the `Counter` widget, The `Buttons` widget uses `context.read<Counts>()` to call the `add` and `remove` functions to change the `count` value in Provider.

When the `add` and `remove` functions are called in the `Buttons` widget, the Provider changes the values, and calls the `notifyListeners()` function to notify the value is changed. After changing the value like this, the widgets, which use `context.watch` or `context.select` to use Provider's value, is `re-built` and shown up with the new value.

{% include in-feed-ads.html %}

## watch, read, select

Provider provides `watch`, `read`, `select` features.

- read: the widget reads the state, but doesn't watch the changes.
- watch: the widget watches the state changes.
- select: the widget watches a part of the state.

Normally, we use the `read` to access the function to change the Provider's state value, and use the `watch` to use the state value. To show the changed state value, the `re-build` occurs, but this `re-build` is high costs. So, like below, we can optimize `re-build` to use `select` to watch a part of the state.

```dart
Widget build(BuildContext context) {
  final name = context.select((Person p) => p.name);
  return Text(name);
}
```

## Execute

Execute the command below to star the app which we've created.

```bash
flutter run
```

Or, when you can execute the app via your editor's debug feature, you can see the screen lik below.

![flutter provider](/assets/images/category/flutter/2021/provider/counter_app.jpg)

And then, when you press the `+` button on the screen, you can see the counter is increased. Also, when you press the `-` button, you can see the number is decreased.

## Completed

Done! we've see how to use Provider to manage the global state in Flutter. Also, we've created a simple app to understand how to use Provider.
