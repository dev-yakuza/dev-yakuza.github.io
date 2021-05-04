---
layout: 'post'
permalink: '/flutter/navigator/stack/'
paginate_path: '/flutter/:num/navigator/stack/'
lang: 'en'
categories: 'flutter'
comments: true

title: '[Flutter] Stack navigation'
description: I try to develop an app with Flutter. In this blog post, I will introduce how to use the Stack navigation in Flutter.
image: '/assets/images/category/flutter/background.png'
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [Stack](#stack)
- [Named routes](#named-routes)
- [popUntil](#popuntil)
- [automaticallyImplyLeading](#automaticallyimplyleading)
- [Swipe back](#swipe-back)
- [Completed](#completed)

</div>

## Outline

I try to develop an app with Flutter. We normally use navigation to move the screen. In this blo post, I wil show you how to use the Stack navigation to navigate the screen in Flutter.

You can see the source code of this blog post on the link below.

- GitHub: [https://github.com/dev-yakuza/study-flutter/tree/main/navigator](https://github.com/dev-yakuza/study-flutter/tree/main/navigator){:rel="nofollow noreferrer" target="_blank"}

## Stack

The Stack navigation stacks the screen over the screen. When we stack the screen over the screen, we use the `push`, and when we remove the screen, we use `pop`.

Let's see the example to understand how to use the Stack navigation. Execute the command below to create a new project for the Stack navigation.

```bash
flutter create my_app
cd stack
```

{% include in-feed-ads.html %}

Next, open `main.dart` file and modify it like below to use the Stack navigation.

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

Let's see the code one by one.

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

until here, it's same the basic app structure. When we use the `MaterialApp` and the app is started, the widget, which is set on `home` parameter, is shown up first. In here, I've set the `Home` widget.

Next, I created two `StatelessWidget` for the Stack navigation. one is the `Home` widget that we've set the `home` parameter of `MaterialApp`, and another is the `SecondScreen` widget which will be used for the next screen by the Stack navigation.

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

Two widgets are basically the same structure by using the `Scaffold`, and show the button on the center with the `ElevatedButton` widget. We'll implement navigating the screen with the Stack navigation when the button is pressed.

Next, let's see the Stack navigation is called when the button is pressed. First, let's see the code that navigate from the `Home` screen to the `SecondScreen`.

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

To show a new screen over the screen by the Stack navigation, we need to use the `push` function of the `Navigator` widget. When we call the `push` function, we need to pass the `context`, which includes the widget tree location info, and the next screen by using the builder of `MaterialPageRoute`.

If you write the code like above, when you press the button on the `Home` widget, the `SecondScreen` widget will be shown up over the `Home` widget.

Let's see the code about how to go back to the `Home` screen from `SecondScreen`.

```dart
onPressed: () {
  Navigator.pop(context);
},
```

When we call the `pop` function of the `Navigator` widget, the current screen is removed, and the screen under it will be shown up. We need to pass the `context` includes the widget tree location info to call the `pop` function.

{% include in-feed-ads.html %}

## Named routes

When we use the various screens in Flutter, we can use the `Named routes` to manage them.

Let's see how to use the `Named routes` with the Stack navigation. First, open `main.dart` file and modify it like below.

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

To use the `Named routes`, we need to define the screen name and screen widget to the `routes` in `MaterialApp`. Also, we should use the `initialRoute` instead of `home` parameter for the first screen after the app is started.

In this example, we'll create `lib/ScreenA.dart`, `lib/ScreenB.dart` and `lib/ScreenC.dart` files, and write the code in them.

We'll import the files in `main.dart` like below.

```dart
import 'ScreenA.dart';
import 'ScreenB.dart';
import 'ScreenC.dart';
```

Let's see the code in the each files. The code of the `ScreenA.dart` file is like below.

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

This widget is a simple widget that uses the `Scafford` and inherits the `StatelessWidget`. I skip to explain the details that is already explained above. In here, I will explain how to use the `Named routes` of the Stack navigation.

```dart
onPressed: () {
  Navigator.pushNamed(context, 'ScreenB');
},
```

To use the `Named routes` for the Stack navigation, we need to use the `pushNamed` function of the `Navigator` widget. At this time, we should pass the `context`, that includes the widget tree location info, and the screen name to the parameters.

{% include in-feed-ads.html %}

The `ScreenB.dart` and `ScreenC.dart` have the same structures, so I just share the code in here.

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

If you use the Named routes, you can navigate the screen simply and manage the variouse screens.

{% include in-feed-ads.html %}

## popUntil

When you use the Stack navigation, many screens are stacked. At this case, we can use the `popUntil` to return the stacked screens at once.

To check how to use the `popUntil`, open `ScreenC.dart` file and modify it like below.

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

To return the `ScreenA` screen that is frist screen, I used the code below in the `ScreenC`.

```dart
onPressed: () {
  Navigator.popUntil(context, (route) => route.isFirst);
},
```

You can use the `popUntil` of the `Navigator` to return the first screen, and `route.isFirst`. If you use the `popUntil` like above, you can navigate to the first screen at once. Also, you can use the code below to go back the specific screen.

```dart
onPressed: () {
  Navigator.popUntil(context, ModalRoute.withName('ScreenA'));
},
```

As above, you can use the screen name, which you define in the `Named routes`, to go back the specific screen in here.

## automaticallyImplyLeading

If you use the Stack navigation to move the screen, you can see the back button on the left top of the screen, even if you didn't configure anything.

Normally, we use this feature, so it's not a problem. However, if you don't want to use this feature, you can use the `automaticallyImplyLeading` option.

If you use the `automaticallyImplyLeading` option like below, you can remove the back button that is automatically generated.

```dart
AppBar(
  ...
  automaticallyImplyLeading: false,
)
```

{% include in-feed-ads.html %}

## Swipe back

If you use the Stack navigation on Flutter, you can use the Swipe back feture to go back the screen.

If you don't want to use it, you can use the `onWillPop` parameter of the `WillPopScope` widget to disable the Swipe back feature like below.

```dart
@override
Widget build(BuildContext context) {
  return WillPopScope(
    onWillPop: () async => false,
    child: Scaffold(
      ...,
    ),
  );
}
```

Wrap the screen, that will be shown up by the Stack navigation, with the `WillPopScope` widget, and you can disable the Swipe back feature by passing the `false` to the `onWillPop` parameter of the `WillPopScope` widget.

## Completed

Done! We've seen how to use the Stack navigatoin. The Stack navigation is used many times, so keep in mind how to use it.
