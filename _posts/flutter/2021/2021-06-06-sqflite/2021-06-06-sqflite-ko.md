---
layout: 'post'
permalink: '/flutter/widget/sqflite/'
paginate_path: '/flutter/:num/widget/sqflite/'
lang: 'ko'
categories: 'flutter'
comments: true

title: '[Flutter] SQLite'
description: 이번 블로그 포스트에서는 Flutter에서 SQLite를 사용하는 방법에 대해서 살펴봅시다.
image: '/assets/images/category/flutter/background.png'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [Shared preferences](#shared-preferences)
- [sqflite 설치](#sqflite-설치)
- [DB 준비](#db-준비)
  - [DB 열기](#db-열기)
  - [DB 닫기](#db-닫기)
  - [기존 DB 사용하기](#기존-db-사용하기)
- [사용 방법](#사용-방법)
  - [모델 클래스](#모델-클래스)
  - [Select](#select)
  - [Insert](#insert)
  - [Update](#update)
  - [Delete](#delete)
- [테스트](#테스트)
  - [준비](#준비)
  - [Select 테스트](#select-테스트)
  - [Insert 테스트](#insert-테스트)
  - [Update 테스트](#update-테스트)
  - [Delete 테스트](#delete-테스트)
- [완료](#완료)

</div>

## 개요

이번 블로그 포스트에서는, Flutter에서 사용자 디바이스에 데이터를 저장하기 위해 `SQLite`를 사용하는 방법에 대해서 알아봅시다. Flutter에서 `SQLite`를 사용하기 위해서는 `sqflite` 패키지를 사용합니다.

- sqflite: [https://pub.dev/packages/sqflite](https://pub.dev/packages/sqflite){:rel="nofollow noreferrer" target="_blank"}

Flutter의 공식 문서에도 `sqflite`을 사용하는 방법에 대해 나와있습니다. 아래에 링크를 통해 공식 문서를 참고하시기 바랍니다.

- 공식 문서: [https://flutter.dev/docs/cookbook/persistence/sqlite](https://flutter.dev/docs/cookbook/persistence/sqlite){:rel="nofollow noreferrer" target="_blank"}

## Shared preferences

SQLite는 복잡한 데이터를 사용자의 디바이스에 저장하기 위해 사용됩니다. 사용자의 디바이스의 간단한 데이터를 `키-값` 형태를 저장할 때에는 `shared_preferences` 패키지를 사용합니다.

`shared_preferences` 패키지를 사용하는 방법에 대해서는 아래에 링크를 참고하시기 바랍니다.

- [[Flutter] Shared preferences]({{site.url}}/{{page.categories}}/shared-preferences/){:target="_blank"}

{% include in-feed-ads.html %}

## sqflite 설치

Flutter에서 SQLite를 사용하기 위해 `sqflite` 패키지를 설치할 필요가 있습니다. 다음 명령어를 실행하여 `sqflite` 패키지를 설치합니다.

```bash
flutter pub add sqflite
```

## DB 준비

Flutter에서 `sqflite` 패키지를 사용하여 SQLite DB를 사용하기 위해 DB를 준비하는 방법에 대해서 알아봅시다.

### DB 열기

SQLite를 사용하기 위해서는 SQLite DB를 열어야 합니다. 다음 코드를 사용하여 SQLite DB를 열 수 있습니다.

```dart
import 'package:sqflite/sqflite.dart';
...
var db = await openDatabase('my_db.db');
...
```

`openDatabase`에 지정한 위치에 DB 파일이 존재하면, 해당 DB를 열며, 존재하지 않는 경우 DB 파일을 생성하고 DB를 열게 됩니다. DB 파일은 안드로이드에 경우는 기본 database 디렉토리에, iOS인 경우 dcouments 디렉토리에 생성됩니다.

### DB 닫기

`sqflite` 패키지의 `openDatabase`을 사용하여 SQLite 데이터베이스를 열어 사용한 경우, 앱이 종료되면, 열었던 DB 접속은 자동으로 닫힙니다. 만약, 앱 종료와 함께 DB 접속을 닫는 것이 아니라, 특정 타이밍에 접속을 닫고 싶은 경우, 다음과 같은 코드를 사용할 수 있습니다.

```dart
...
await db.close();
...
```

### 기존 DB 사용하기

`sqflite` 패키지를 사용하여, 미리 만든 SQLite DB를 사용할 수 있습니다. 우선, 미리 만든 SQLite DB를 `assets/` 폴더에 복사합니다. 그런 다음, `pubspec.yaml` 파일을 열고 다음과 같이 수정합니다.

```yaml
assets:
  - assets/data.db
```

그리고 다음과 같이 SQLite DB가 존재하지 않는 경우, 미리 준비한 DB를 복사하여 사용하도록 할 수 있습니다.

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

## 사용 방법

`sqflite`을 사용하여 SQLite DB에 데이터를 CRUD(Create, Read, Update, Delete)하는 방법에 대해서 알아봅시다.

### 모델 클래스

Flutter에서 SQLite에 데이터를 저장하거나 사용하기 위해 모델 클래스를 정의할 수 있습니다. 이는 SQLite를 사용하기 위한 필수 조건은 아니지만, SQLite로 부터 가져온 데이터를 사용할 때, 또는 데이터를 추가할 때에 좀 더 명확하게 사용할 수 있습니다.

모델로 사용할 클래스는 다음과 같이 작성할 수 있습니다.

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

다음과 같이 모델 클래스와 `sqflite`을 사용하여 SQLite DB에 저장된 데이터를 가져올 수 있습니다.

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

다음과 같이 모델 클래스와 `sqflite`을 사용하여 SQLite DB에 데이터를 추가할 수 있습니다.

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

다음과 같이 모델 클래스와 `sqflite`을 사용하여 SQLite DB에 데이터를 업데이트할 수 있습니다.

```dart
await db.update('dogs', dog.toMap(), where: 'id = ?', whereArgs: [dog.id]);
// await db.rawUpdate('UPDATE dogs SET age = ${dog.age} WHERE id = ${dog.id}');
```

### Delete

다음과 같이 `sqflite`을 사용하여 SQLite DB에 있는 데이터를 삭제할 수 있습니다.

```dart
await db.delete('dogs', where: 'id = ?', whereArgs: [id]);
// await database.rawDelete('DELETE FROM dogs WHERE id = ?', [id]);
```

{% include in-feed-ads.html %}

## 테스트

SQLite는 기본적으로 사용자의 디바이스에 DB가 생성되고, `sqflite` 패키지는 디바이스에서 동작되도록 설계되어 유닛 테스트(Unit Test)를 할 수가 없습니다.

하지만, `sqflite_ffi`을 사용하면, 테스트 코드에서 직접 DB를 열고, CRUD 쿼리(Query)를 테스트할 수 있습니다.

### 준비

다음과 같이 실제 사용되는 SQLite DB를 복사하고, `sqflite_ffi`을 초기화하여, 테스트할 환경을 준비합니다.

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

### Select 테스트

다음과 같이 `sqflite_ffi`을 사용하여 Select 쿼리를 테스트 할 수 있습니다.

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

### Insert 테스트

다음과 같이 `sqflite_ffi`을 사용하여 Insert 쿼리를 테스트 할 수 있습니다.

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

### Update 테스트

다음과 같이 `sqflite_ffi`을 사용하여 Update 쿼리를 테스트 할 수 있습니다.

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

### Delete 테스트

다음과 같이 `sqflite_ffi`을 사용하여 Delete 쿼리를 테스트 할 수 있습니다.

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

## 완료

이것으로 Flutter에서 SQLite를 사용하기 위해 `sqflite` 패키지를 사용하는 방법에 대해서 알아보았습니다. 여러분도 SQLite를 사용하여 사용자의 디바이스에 데이터를 저장하고 사용해 보시기 바랍니다.
