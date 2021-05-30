---
layout: 'post'
permalink: '/flutter/widget/shared-preferences/'
paginate_path: '/flutter/:num/widget/shared-preferences/'
lang: 'ja'
categories: 'flutter'
comments: true

title: '[Flutter] Shared preferences'
description: 今回のブログポストではFlutterでローカルに簡単なデータを保存するためShared preferencesパッケージを使う方法について説明します。
image: '/assets/images/category/flutter/background.png'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [Shared preferencesパッケージのインストール](#shared-preferencesパッケージのインストール)
- [Shared preferencesの使い方](#shared-preferencesの使い方)
  - [データの保存](#データの保存)
  - [データの読み取り](#データの読み取り)
  - [データの削除](#データの削除)
- [ユニットテスト](#ユニットテスト)
- [完了](#完了)

</div>

## 概要

Flutterでアプリを開発する時、ウェブのlocalStorageやReact NativeのAsyncStorageように、ユーザの端末に簡単なデータを保存したい時があります。この時、Flutterで使えるパッケージが`Shared preferences`です

- [shared_preferences](https://pub.dev/packages/shared_preferences){:rel="nofollow noreferrer" target="_blank"}

Flutterの公式ドキュメントでも使い方が詳しく乗っておりますので、ご参考してください。

- 公式ドキュメント: [Store key-value data on disk](https://flutter.dev/docs/cookbook/persistence/key-value){:rel="nofollow noreferrer" target="_blank"}

## Shared preferencesパッケージのインストール

`Shared preferences`はユーザの端末に`key-value`の形で簡単なデータを保存することができます。そしたら、Shared preferencesを使うため下記のコマンを使ってパッケージをインストールします。

```dart
flutter pub add shared_preferences
```

## Shared preferencesの使い方

`Shared preferences`では`int`、`double`、`bool`、`string`または、`List<String>`のデータを保存んすることができます。そしたら、`Shared preferences`を使ってデータの読み取り/書き込み/削除について説明します。

### データの保存

`Shared preferences`を使って下記のようにデータを保存することができます。

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

### データの読み取り

`Shared preferences`を使って次のようにデータを読むことができます。

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

### データの削除

次のように`Shared preferences`を使って保存したデータを削除することができます。

```dart
...
import 'package:shared_preferences/shared_preferences.dart';
...
final prefs = await SharedPreferences.getInstance();
prefs.remove('counter');
```

または次のように全てのデータを削除することもできます。

```dart
prefs.clear();
```

## ユニットテスト

`Shared preferences`パッケージを使うコードをユニットテスト（Unit Test）をする時、次のように`Shared preferences`が提供する`setMockInitialValues`を使ってデータを初期化することができます。

```dart
...
import 'package:shared_preferences/shared_preferences.dart';
...
setUp(() {
  SharedPreferences.setMockInitialValues({});
});
```

## 完了

これでFlutterで簡単なデータをユーザの端末に保存するため`Shared preferences`を使う方法についてみてみました。`Shared preferences`パッケージは基本的簡単なデータを保存するように設計されました。したがって、大きいデータを保存するには適していません。単純にユーザが選択した設定のオプションなどを保存する時、使うことをお勧めします。
