---
layout: 'post'
permalink: '/flutter/widget/sqflite/'
paginate_path: '/flutter/:num/widget/sqflite/'
lang: 'en'
categories: 'flutter'
comments: true

title: '[Flutter] SQLite'
description: Let's see how to use SQLite in Flutter.
image: '/assets/images/category/flutter/background.png'
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [Shared preferences](#shared-preferences)
- [Install sqflite](#install-sqflite)
- [Prepare DB](#prepare-db)
  - [Open DB](#open-db)
  - [Close DB](#close-db)
  - [Use existing DB](#use-existing-db)
- [How to use](#how-to-use)
  - [Model class](#model-class)
  - [Select](#select)
  - [Insert](#insert)
  - [Update](#update)
  - [Delete](#delete)
- [Test](#test)
  - [Prepare](#prepare)
  - [Select test](#select-test)
  - [Insert test](#insert-test)
  - [Update test](#update-test)
  - [Delete test](#delete-test)
- [Completed](#completed)

</div>

## Outline

In this blog post, I will show you how to use `SQLite` to store the data on the user device in Flutter. In Flutter, we'll use the `sqflite` package to use `SQLite`.

- sqflite: [https://pub.dev/packages/sqflite](https://pub.dev/packages/sqflite){:rel="nofollow noreferrer" target="_blank"}

You can see the details about how to use `sqflite` in the Flutter official document.

- Official document: [Persist data with SQLite](https://flutter.dev/docs/cookbook/persistence/sqlite){:rel="nofollow noreferrer" target="_blank"}

## Shared preferences

Normally, we use SQLite to store the complicated data on the user device. To save the simple data on the user device as form of `key-value`, we use the `shared_preferences` package.

If you want to know details about how to use `shared_preferences` package, see the link below.

- [[Flutter] Shared preferences]({{site.url}}/{{page.categories}}/shared-preferences/){:target="_blank"}

{% include in-feed-ads.html %}

## Install sqflite

To use SQLite in Flutter, we need to install the `sqflite` package. Execute the command below to install the `sqflite` package.

```bash
flutter pub add sqflite
```

## Prepare DB

When we use the `sqflite` package to use SQLite DB in Flutter, we need to prepare DB. Let's see how to prepare SQLite DB.

### Open DB

To use SQLite, we need to open the SQLite DB. You can open the SQLite DB by the code below.

```dart
import 'package:sqflite/sqflite.dart';
...
var db = await openDatabase('my_db.db');
...
```

If the DB file exists on the directory which is set on `openDatabase`, the DB file is opened. If the file doens't exist, The new DB file is created and opend. The DB file is basically stored in default database directory on Android, and stored in the document directory on iOS.

### Close DB

When we open the SQLite DB by `openDatabase` of the `sqflite` package, the DB access is closed automatically when the app is closed. If you want to close the DB at a specific timing instead of when the App is closed, you can use the code below to close the DB access.

```dart
...
await db.close();
...
```

### Use existing DB

We can use pre-made SQLite DB with the `sqflite` package. First, copy the existing SQLite DB to the `assets/` folder. And then, open the `pubspec.yaml` file and modify it like below.

```yaml
assets:
  - assets/data.db
```

And then, If the SQLite DB doesn't exist, you can copy the pre-made DB by using the code below.

```dart
import 'dart:io';
import 'package:flutter/services.dart';
import 'package:path/path.dart';
import 'package:sqflite/sqflite.dart';

Future<Database> getDB() async {
  var databasesPath = await getDatabasesPath();
  var path = join(databasesPath, '~www/data.db');
  var exists = await databaseExists(path);

  if (!exists) {
    try {
      await Directory(dirname(path)).create(recursive: true);
    } catch (_) {}

    var data = await rootBundle.load(join('assets', 'data.db'));
    List<int> bytes = data.buffer.asUint8List(
      data.offsetInBytes,
      data.lengthInBytes,
    );

    await File(path).writeAsBytes(bytes, flush: true);
  }

  return await openDatabase(path);
}
```

{% include in-feed-ads.html %}

## How to use

Let's see how to use the `sqflite` package to do CRUD(Create, Read, Update, Delete) on SQLite DB.

### Model class

You can define a model class to store or use the data with SQLite in Flutter. Although this is not a prerequisite for using SQLite, it makes more clear to get or add the data to SQLite.

You can write the modal class like the below.

```dart
class Dog {
  final int id;
  final String name;
  final int age;

  Dog({
    required this.id,
    required this.name,
    required this.age,
  });

  Map<String, dynamic> toMap() {
    return {
      'id': id,
      'name': name,
      'age': age,
    };
  }

  @override
  String toString() {
    return 'Dog{id: $id, name: $name, age: $age}';
  }
}
```

### Select

You can get the data from SQLite DB with the modal class and the `sqflite` package like below.

```dart
final List<Map<String, dynamic>> maps = await db.query('dogs');
// final List<Map<String, dynamic>> maps = await db.rawQuery(
//   'SELECT id, name, age FROM dogs',
// );

return List.generate(maps.length, (i) {
  return Dog(
    id: maps[i]['id'],
    name: maps[i]['name'],
    age: maps[i]['age'],
  );
});
```

### Insert

You can add the data to SQLite DB with the modal class and the `sqflite` package like below.

```dart
var dog = Dog(
  id: 0,
  name: 'Fido',
  age: 35,
);

await db.insert('dogs', dog.toMap());
// await db.rawInsert('INSERT INTO dogs(id, name, age) VALUES (${dog.id}, "${dog.name}", ${dog.age})');
```

### Update

You can update the data on SQLite DB with the modal class and the `sqflite` package like below.

```dart
await db.update('dogs', dog.toMap(), where: 'id = ?', whereArgs: [dog.id]);
// await db.rawUpdate('UPDATE dogs SET age = ${dog.age} WHERE id = ${dog.id}');
```

### Delete

You can delete the data from SQLite DB with the `sqflite` package like below.

```dart
await db.delete('dogs', where: 'id = ?', whereArgs: [id]);
// await database.rawDelete('DELETE FROM dogs WHERE id = ?', [id]);
```

{% include in-feed-ads.html %}

## Test

SQLite DB is basically created on the user device, and the `sqflite` package is designed on the detice, so we can't do the Unit Test with it.

However, if we use `sqflite_ffi`, we can open the DB and test the CRUD queries in the test code.

### Prepare

Copy the SQLite DB that is used for the service like the below, and initialize `sqflite_ffi` to prepare for testing.

```dart
import 'dart:io';

import 'package:flutter_test/flutter_test.dart';
import 'package:sqflite_common_ffi/sqflite_ffi.dart';
import 'package:path/path.dart';

void copyFile(String path, String newPath) {
  File(path).copySync(newPath);
}

void main() {
  sqfliteFfiInit();
  setUp(() {
    File(join('assets', 'my_db.db')).copySync(join('assets', 'test.db'));
  });

  ...
}
```

### Select test

You can test the Select query with `sqflite_ffi` like the below.

```dart
...
void main() {
  ...
  test('Select', () async {
    var db = await databaseFactoryFfi.openDatabase('../../../assets/test.db');
    var dataProvider = DataProvider(db: db);

    var maps = await db.query('dogs');
    var list = List.generate(maps.length, (i) {
      return Dog(
        id: maps[i]['id'],
        name: maps[i]['name'],
        age: maps[i]['age'],
      );
    });

    expect(list[0].toMap(), {'id': 0, 'name': 'Fido', 'age': 35});
  });
  ...
}
```

### Insert test

You can test the Insert query with `sqflite_ffi` like the below.

```dart
...
void main() {
  ...
  test('Insert', () async {
    var db = await databaseFactoryFfi.openDatabase('../../../assets/test.db');
    var dataProvider = DataProvider(db: db);

    var dog = Dog(
      id: 1,
      name: 'Fido',
      age: 35,
    );
    await db.insert('dogs', dog.toMap());

    var maps = await db.rawQuery(
      'SELECT name FROM dogs WHERE id=${dog.id}',
    );
    expect(maps[0].name, dog.name);
  });
  ...
}
```

### Update test

You can test the Update query with `sqflite_ffi` like the below.

```dart
...
void main() {
  ...
  test('Update', () async {
    var db = await databaseFactoryFfi.openDatabase('../../../assets/test.db');
    var dataProvider = DataProvider(db: db);

    var dog = Dog(
      id: 0,
      name: 'Fido',
      age: 10,
    );
    await db.update('dogs', dog.toMap(), where: 'id = ?', whereArgs: [dog.id]);

    var maps = await db.rawQuery(
      'SELECT age FROM dogs WHERE id=$dog.id',
    );
    expect(maps[0].age, 10);
  });
  ...
}
```

### Delete test

You can test the Delete query with `sqflite_ffi` like the below.

```dart
...
void main() {
  ...
  test('Delete', () async {
    var db = await databaseFactoryFfi.openDatabase('../../../assets/test.db');
    var dataProvider = DataProvider(db: db);

    var dog = Dog(
      id: 0,
      name: 'Fido',
      age: 35,
    );
    await db.delete('dogs', where: 'id = ?', whereArgs: [id]);

    var maps = await db.rawQuery(
      'SELECT * FROM dogs WHERE id=$dog.id',
    );
    expect(maps.length, 0);
  });
}
```

## Completed

Done! we've seen how to use the `sqflite` package to use SQLite in Flutter. We encourage you to use SQLite to store and use data on the user device.
