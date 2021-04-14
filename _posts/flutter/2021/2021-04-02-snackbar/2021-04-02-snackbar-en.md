---
layout: 'post'
permalink: '/flutter/widget/snackbar/'
paginate_path: '/flutter/:num/widget/snackbar/'
lang: 'en'
categories: 'flutter'
comments: true

title: '[Flutter] Snackbar widget'
description: I try to develop an app with Flutter. In this blog post, I will introduce how to use the Snackbar widget to show simple messages in Flutter.
image: '/assets/images/category/flutter/background.png'
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [Create project](#create-project)
- [Snackbar](#snackbar)
- [Completed](#completed)

</div>

## Outline

I try to develop an app with Flutter. In this blog post, I will introduce how to show the Snackbar for the simple messages in Flutter.

![Flutter - snackbar](/assets/images/category/flutter/2021/snackbar/snackbar.jpg)

You can see the example source code of this blog post on the link below.

- GitHub: [https://github.com/dev-yakuza/study-flutter/tree/main/widget](https://github.com/dev-yakuza/study-flutter/tree/main/widget){:rel="nofollow noreferrer" target="_blank"}

## Create project

To see how to use the Snackbar in Flutter, execute the command below to create a new project.

```bash
flutter create my_app
cd my_app
```

{% include in-feed-ads.html %}

## Snackbar

Let's see how to display the Snackbar in the new project. Open `main.dart` file and modify it like below.

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

The code above shows a button on the center of the screen, and if the button is pressed, the Snackbar is shown up.

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

To show the Snackbar, we should use `ScaffoldMessenger`.

```dart
ScaffoldMessenger.of(context).showSnackBar(
  SnackBar(
    content: Text('Hello world'),
  ),
);
```

At this case, we sholud pass `SnackBar` widget to `showSnackBar`, and write the message in there.

{% include in-feed-ads.html %}

We can use `SnackBar` with various options like below.

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

When we use the options like above, we can show the Snackbar like below.

![Flutter - snackbar with options](/assets/images/category/flutter/2021/snackbar/snackbar_with_options.jpg)

## Completed

Done! we've seen how to use the Snackbar in Flutter. Also, we've seen the Snackbar's options. From now, let's use the Snackbar to show simple message in Flutter!
