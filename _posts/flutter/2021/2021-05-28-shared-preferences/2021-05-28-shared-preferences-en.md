---
layout: 'post'
permalink: '/flutter/widget/shared-preferences/'
paginate_path: '/flutter/:num/widget/shared-preferences/'
lang: 'en'
categories: 'flutter'
comments: true

title: '[Flutter] Shared preferences'
description: Let's see how to store the simple data to the user device by Shared preferences in Flutter.
image: '/assets/images/category/flutter/background.png'
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [Install Shared preferences package](#install-shared-preferences-package)
- [How to use Shared preferences](#how-to-use-shared-preferences)
  - [Store data](#store-data)
  - [Read data](#read-data)
  - [Delete data](#delete-data)
- [Unit Test](#unit-test)
- [Completed](#completed)

</div>

## Outline

WHen we develop the app in Flutter, like the web localStorage or React Native AsyncStorage, we want to store the simple data to the user device. At this time, we can use the `Shared preferences` package in Flutter.

- [shared_preferences](https://pub.dev/packages/shared_preferences){:rel="nofollow noreferrer" target="_blank"}

You can see details about how to use the Shared preferences on the Flutter official document.

- Official document: [Store key-value data on disk](https://flutter.dev/docs/cookbook/persistence/key-value){:rel="nofollow noreferrer" target="_blank"}

## Install Shared preferences package

The `Shared preferences` package helps us to simply store data in the form of `key-value` on the user device. To use the Shared preferences package, execute the command below to install it.

```dart
flutter pub add shared_preferences
```

## How to use Shared preferences

We can store `int`, `double`, `bool`, `string` and `List<String>` data by `Shared preferences`. Let's see how to create/read/delete the data by `Shared preferences`.

### Store data

You can store the data by `Shared preferences` like the below.

```dart
...
import 'package:shared_preferences/shared_preferences.dart';
...
final prefs = await SharedPreferences.getInstance();
prefs.setInt('counter', 0);
prefs.setDouble('width', 20.5);
prefs.setBool('isAdmin', true);
prefs.setString('userName', 'dev-yakuza');
prefs.setStringList('alphabet', ['a', 'b', 'c', 'd']);
```

### Read data

You can read the data by `Shared preferences` like the below.

```dart
...
import 'package:shared_preferences/shared_preferences.dart';
...
final prefs = await SharedPreferences.getInstance();
final counter = prefs.getInt('counter') ?? 0;
final width = prefs.getDouble('width') ?? 10.5;
final isAdmin = prefs.getBool('isAdmin') ?? false;
final userName = prefs.getString('userName') ?? '';
final alphabet = prefs.getStringList('alphabet') ?? [];
final data = prefs.get('userInfo') : {};
```

### Delete data

You can delete the data by `Shared preferences` like the below.

```dart
...
import 'package:shared_preferences/shared_preferences.dart';
...
final prefs = await SharedPreferences.getInstance();
prefs.remove('counter');
```

Also, you can delete all data like the below.

```dart
prefs.clear();
```

## Unit Test

When you do the unit test the widget which uses the `Shared preferences` package, you can use `setMockInitialValues`, that the `Shared preferences` package providers, to initialize data.

```dart
...
import 'package:shared_preferences/shared_preferences.dart';
...
setUp(() {
  SharedPreferences.setMockInitialValues({});
});
```

## Completed

Done! we've seen how to use the `Shared preferences` package to store/read/delete the simple data to the user device. the `Shared preferences` package is designed for the simple data, so it is not suitable for storing the large data. I recommend you to use the `Shared preferences` package to store the simple data like the settings option which the user selected.
