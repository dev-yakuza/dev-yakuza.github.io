---
layout: 'post'
permalink: '/flutter/widget/sqflite/'
paginate_path: '/flutter/:num/widget/sqflite/'
lang: 'ja'
categories: 'flutter'
comments: true

title: '[Flutter] SQLite'
description: 今回のブログポストではFlutterでSQLiteを使う方法について説明します。
image: '/assets/images/category/flutter/background.png'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [Shared preferences](#shared-preferences)
- [sqfliteインストール](#sqfliteインストール)
- [DB準備](#db準備)
  - [DBオープン](#dbオープン)
  - [DBクローズ](#dbクローズ)
  - [既存DBを使う場合](#既存dbを使う場合)
- [使い方](#使い方)
  - [モデルクラス](#モデルクラス)
  - [Select](#select)
  - [Insert](#insert)
  - [Update](#update)
  - [Delete](#delete)
- [テスト](#テスト)
  - [準備](#準備)
  - [Selectテスト](#selectテスト)
  - [Insertテスト](#insertテスト)
  - [Updateテスト](#updateテスト)
  - [Deleteテスト](#deleteテスト)
- [完了](#完了)

</div>

## 概要

このブログポストでは、Flutterでユーザデバイスにデータを保存するため`SQLite`を使う方法について説明します。Flutterで`SQLite`を使うためには`sqflite`パッケージを使います。

- sqflite: [https://pub.dev/packages/sqflite](https://pub.dev/packages/sqflite){:rel="nofollow noreferrer" target="_blank"}

Flutterの公式ドキュメントでも`sqflite`を使う方法について書いております。下記のリンクで公式ドキュメントも参考してみてください。

- 公式ドキュメント: [https://flutter.dev/docs/cookbook/persistence/sqlite](https://flutter.dev/docs/cookbook/persistence/sqlite){:rel="nofollow noreferrer" target="_blank"}

## Shared preferences

SQLiteは複雑なデータをユーザのデバイスに保存する時使います。ユーザのデバイスに簡単なデータを`Key-Value`の形式で保存する時には`shared_preferences`パッケージを使います。

`shared_preferences`パッケージを使う方法については下記のリンクを参考してください。

- [[Flutter] Shared preferences]({{site.url}}/{{page.categories}}/shared-preferences/){:target="_blank"}

{% include in-feed-ads.html %}

## sqfliteインストール

FlutterでSQLiteを使うため`sqflite`パッケージをインストールする必要があります。次のコマンドを使って`sqflite`パッケージをインストールします。

```bash
flutter pub add sqflite
```

## DB準備

Flutterで`sqflite`パッケージを使ってSQLite DBを使うため、DBを準備する方法について説明します。

### DBオープン

SQLiteを使うためにはSQLite DBをオープンする必要があります。次のコードを使ってSQLite DBをオープンすることができます。

```dart
import 'package:sqflite/sqflite.dart';
...
var db = await openDatabase('my_db.db');
...
```

`openDatabase`に指定したDBファイルが存在すると、当該DBをオープンします。存在しない場合は、DBファイルを生成してDBをオープンします。DBファイルはアンドロイドの場合、基本Databaseディレクトリに、iOSの場合はdcoumentsディレクトリに生成されます。

### DBクローズ

`sqflite`パッケージの`openDatabase`を使ってSQLiteデータベースをオープンして使う場合、アプリが終了されると、オープンされたDBのアクセスも自動でクローズされます。もし、アプリ終了と一緒にDBのアクセスをクローズするではなく、特定したタイミングでクローズしたい場合、次のコードを使います。

```dart
...
await db.close();
...
```

### 既存DBを使う場合

`sqflite`パッケージを使って、事前に作ったSQLite DBを使うこともできます。まず、事前に作ったSQLite DBを`assets/`フォルダにコピーします。その後、`pubspec.yaml`ファイルを開いて下記のように修正します。

```yaml
assets:
  - assets/data.db
```

そして、次のようにSQLite DBが存在しない場合、事前に作ったDBをコピーして使えるようにすることができます。

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

## 使い方

`sqflite`を使ってSQLite DBにデータをCRUD(Create, Read, Update, Delete)する方法について説明します。

### モデルクラス

FlutterでSQLiteにデータを保存したり使うためモデルクラスを定義して使うことができます。こレはSQLiteを使うため必須条件ではなく、SQLiteからデータを取ってくる時、またはデータを追加する時、もっt明確にするため使います。

モデルを使うクラスは下記のように作成します。

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

次のようにモデルクラスと`sqflite`を使ってSQLite DBに保存されたデータを取ってくることができます。

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

次のようにモデルクラスと`sqflite`を使ってSQLite DBにデータを追加することができます。

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

次のようにモデルクラスと`sqflite`を使ってSQLite DBにデータを更新することができます。

```dart
await db.update('dogs', dog.toMap(), where: 'id = ?', whereArgs: [dog.id]);
// await db.rawUpdate('UPDATE dogs SET age = ${dog.age} WHERE id = ${dog.id}');
```

### Delete

次のように`sqflite`を使ってSQLite DBにあるデータを削除することができます。

```dart
await db.delete('dogs', where: 'id = ?', whereArgs: [id]);
// await database.rawDelete('DELETE FROM dogs WHERE id = ?', [id]);
```

{% include in-feed-ads.html %}

## テスト

SQLiteは基本的ユーザのデバイスにDBが生成されて、`sqflite`パッケージはデバイスで動作されるように設計されてますので、ユニットテスト(Unit Test)することができません。

しかし、`sqflite_ffi`を使って、テストコードで直接DBをオープンしてCRUDクエリ(Query)をテストすることはできます。

### 準備

次のように実際使ってるSQLite DBをコピーと`sqflite_ffi`を初期化して、テストする環境を準備します。

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

### Selectテスト

次のように`sqflite_ffi`を使ってSelectクエリをテストすることができます。

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

### Insertテスト

次のように`sqflite_ffi`を使ってInsertクエリをテストすることができます。

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

### Updateテスト

次のように`sqflite_ffi`を使ってUpdateクエリをテストすることができます。

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

### Deleteテスト

次のように`sqflite_ffi`を使ってDeleteクエリをテストすることができます。

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

## 完了

これでFlutterでSQLiteを使うため`sqflite`パッケージを使う方法についてみてみました。皆さんもSQLiteを使ってユーザのデバイスにデータを保存して使ってみてください。
