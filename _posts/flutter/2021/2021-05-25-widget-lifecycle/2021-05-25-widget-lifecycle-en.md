---
layout: 'post'
permalink: '/flutter/widget/lifecycle/'
paginate_path: '/flutter/:num/widget/lifecycle/'
lang: 'en'
categories: 'flutter'
comments: true

title: '[Flutter] Lifecycle'
description: In this blog post, I will introduce the Lifecycl of the widget in Flutter.
image: '/assets/images/category/flutter/background.png'
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [Stateless widget](#stateless-widget)
  - [Stateless widget's Constructor](#stateless-widgets-constructor)
  - [Stateless widget build](#stateless-widget-build)
- [Stateful widget](#stateful-widget)
  - [Stateful widget's Constructor](#stateful-widgets-constructor)
  - [initState](#initstate)
  - [didChangeDependencies](#didchangedependencies)
  - [didUpdateWidget](#didupdatewidget)
  - [Stateful widget build](#stateful-widget-build)
  - [deactivate](#deactivate)
  - [dispose](#dispose)
  - [Order of calling](#order-of-calling)
- [Completed](#completed)

</div>

## Outline

In Flutter, unlike stateless widgets that simply compose a screen, stateful widgets have a `lifecycle`. In this blog post, I will show you the lifecycle of the Stateful widget.

To help you understand the lifecycle functions in Flutter, I made a sample source code. you can see the code on the link below.

- GitHub: [AnimatedContainer](https://github.com/dev-yakuza/study-flutter/tree/main/widget/lifecycle){:rel="nofollow noreferrer" target="_blank"}

## Stateless widget

The Stateless widget simply composes the screen, so it doesn't have a complex lifecycle. Let's see the lifecycle function of the Stateless widget.

### Stateless widget's Constructor

In Flutter we use the class for the widget. The widget is a class, so the widget can use the `constructor` of the class.

The widget constructor is the same as the class constructor. Normarlly, we use it to initialize the variables that is used in the widget(class).

```dart
import 'package:flutter/material.dart';

class Home extends StatelessWidget {
  final String title;

  Home({required this.title});

  ...
}
```

### Stateless widget build

The `build` function in the widget creates the content to be displayed on the screen. It's like the `render` function in `React`. The `build` function returns the widget that is shown up on the screen.

```dart
import 'package:flutter/material.dart';

class Home extends StatelessWidget {
  ...
  @override
  Widget build(BuildContext context) {
    return Center(
      child: Text('Setting Screen'),
    );
  }
}
```

The Stateless widget doesn't have a state. So, when the value, which the parent widget passes, is changed, the widget will `rebuild` and update the screen. At this time, the `Constructor` and `build` functions are called again.

{% include in-feed-ads.html %}

## Stateful widget

The Stateful widget has a state unlike Stateless, so the lifecycle is more complex. Let's see the lifecycle functions of the Stateful widget

### Stateful widget's Constructor

The Stateful widget constructor is also the same as the role of the Stateless widget constructor. When the instance is created from the widget class, the constructor is called first, and we can use it to get the parameters from the parent widget.

```dart
class CounterContainer extends StatefulWidget {
  final int count;

  CounterContainer({required this.count})

  @override
  _CounterContainerState createState() => _CounterContainerState(count: count);
}

class _CounterContainerState extends State<CounterContainer> {
  int count;
  _CounterContainerState({required this.count})
  ...
}
```

### initState

When the Stateful widget is created, this function is called only once and used to initialize the state.

```dart
class _CounterContainerState extends State<CounterContainer> {
  late int count;

  @override
  void initState() {
    super.initState();
    count = 0;
  }
  ...
}
```

### didChangeDependencies

When the widget is created, this function is called only once right after the `initState` function is called. Also, if you use [InheritedWidget](https://api.flutter.dev/flutter/widgets/InheritedWidget-class.html){:rel="nofollow noreferrer" target="_blank"} or [Provider]({{site.url}}/{{page.categories}}/provider/){:target="_blank"}, whne the InheritedWidget or Provider value is changed, this function is called again.

In other words, when the parent widget or own state is changed, this function is not called, but the widget(InheritedWidget or Provider), which the current widget has the dependency with, is changed, the `didChangeDependencies` function is called.

### didUpdateWidget

This function will be called right before `build` function when the value which the parent widget passed is changed. Normally, we use this for the animation restarts when the parent widget is changed.

```dart
@override
void didUpdateWidget(MyWidget oldWidget) {
  super.didUpdateWidget(oldWidget);
  if (widget.value != oldWidget.value) {
    // TODO: start a transition between the previous and new value
  }
}
```

Also, if you need to re-initialize the state according to the parent widget changes, you can re-initialize the state value via `setState` here.

### Stateful widget build

This is the same as the Stateless widget build. This function is used to return the widget that is displayed on the screen. When the state is changed by `setState` in Stateful widget, this function is called again to update the screen.

{% include in-feed-ads.html %}

### deactivate

The Stateful widget has the state object unlike the Stateless widget. This object is changed(dirty), the Stateful widget does `rebuild` with this changed object.

The `deactivate` function is called when the state object is removed on the tree. Sometimes, Flutter deletes the state object and add it again. For example, when you move the widget to the some other place of the widget tree by `GlobalKey`, the state object is removed and added again, so the `deactivate` function is executed when the state object is removed.

You can see the more details on the official document.

- Official document: [deactivate](https://api.flutter.dev/flutter/widgets/State/deactivate.html){:rel="nofollow noreferrer" target="_blank"}

### dispose

When the widget object is removed permanently from the widget tree, this function is called. When the widget is removed completely from the widget tree,, the state object is also removed, so the `deactivate` function is called first to notify the state object is removed and the `dispose` function is called to notify the widget object is removed.

The `dispose` function call means the widget object is deleted permanently, so you can't use `setState` to make the widget `rebuild`.

### Order of calling

- When the Stateful widget is created: `Constructor` > `initState` > `didChangeDependencies` > `build`
- When the setState is called: `build`
- When InheritedWidget or Provider value is changed: `didChangeDependencies` > `build`
- When the value, which the parent widget passed, is cahgned: `didUpdateWidget` > `build`
- When the state object is removed: `deactivate` > `build`
- When the widget object is removed: `deactivate` > `dispose`

## Completed

Done! we've seen the lifecycle of the widget in Flutter. When we use the wrong lifecycle function, There is a risk of falling into an infinite loop or the app performance is degraded, so you should use it with care. Also, the lifecycle of the widget determines when to call `setState` or a specific function, or plays the animation, so it would be a good idea to study carefully at this opportunity.
