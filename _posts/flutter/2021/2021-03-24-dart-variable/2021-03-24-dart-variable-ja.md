---
layout: 'post'
permalink: '/flutter/dart/variable/'
paginate_path: '/flutter/:num/dart/variable/'
lang: 'ja'
categories: 'flutter'
comments: true

title: '[Flutter] Dartの変数'
description: Flutterでアプリを開発するためFlutterの開発言語であるDartについて説明します。今回のブログポストではDartの変数について説明します。
image: '/assets/images/category/flutter/2021/dart/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [開発環境](#開発環境)
- [Hello world](#hello-world)
- [変数](#変数)
  - [var](#var)
  - [int](#int)
  - [double](#double)
  - [String](#string)
  - [bool](#bool)
  - [List](#list)
  - [Map](#map)
  - [enum](#enum)
- [定数](#定数)
  - [finalとconst](#finalとconst)
- [String Interpolation](#string-interpolation)
- [Nullable](#nullable)
- [変数の特徴](#変数の特徴)
- [完了](#完了)

</div>

## ブログシリーズ

このブログはシリーズで作成しております。下記のリンクを参考して他のブログポストも確認してみてください。

- [[MacOS] Flutterのインストール]({{site.url}}/{{page.categories}}/installation/){:target="_blank"}
- [Flutter] Dartの変数
- [[Flutter] Dartの演算子]({{site.url}}/{{page.categories}}/dart/operator/){:target="_blank"}
- [[Flutter] DartのStatement]({{site.url}}/{{page.categories}}/dart/statement/){:target="_blank"}
- [[Flutter] Dartの関数]({{site.url}}/{{page.categories}}/dart/function/){:target="_blank"}
- [[Flutter] Dartのクラス]({{site.url}}/{{page.categories}}/dart/class/){:target="_blank"}

## 概要

Flutterはグーグルで開発したDartと言う言語を使って開発します。

- Dart: [公式サイト](https://dart.dev/){:rel="nofollow noreferrer" target="_blank"}

このブログポストではFlutterで使ってるDart言語の基本的な使い方を説明して、Dartの変数について詳しく説明します。

このブログポストで紹介するソースコードは下記のリンクで確認できます。

- GitHub: [https://github.com/dev-yakuza/study-flutter/tree/main/dart](https://github.com/dev-yakuza/study-flutter/tree/main/dart){:rel="nofollow noreferrer" target="_blank"}

## 開発環境

Dartをローカルで開発するためにはFlutterをインストールして設定する必要があります。以前のブログポストを参考して開発環境を構築してください。

- [[MacOS] Flutterのインストール]({{site.url}}/{{page.categories}}/installation/){:target="_blank"}

今回のブログポストではFlutterのインストールや設定はできた前提で進めます。そしたら、Dartの言語を使うため新しフォルダを生成します。

```bash
mkdir dart
cd dart
```

そして下記のコマンドw実行してVSCodeを実行します。

```bash
code .
```

{% include in-feed-ads.html %}

## Hello world

まず、Dartでコーディングするため、Dartファイルを生成してみましょう。VSCodeで下記のように新しファイルを生成してみます。

![VSCode - create Dart file](/assets/images/category/flutter/2021/dart/new_file.jpg)

ファイル名はなんでもいいですが、ここでは`main.dart`で生成します。このようにファイルを生成したら、当該ファイルを開いて下記のように作成します。

```dart
void main() {
  print('Hello world!');
}
```

全ての内容をセク生したら、`cmd + shift + d`を押して、`Debug: restart`を検索して実行します。

![VSCode - Dart debugging](/assets/images/category/flutter/2021/dart/debug_restart.jpg)

そしたらVSCodeが`.vscode/launch.json`ファイルを自動生成してくれます。

![VSCode - Dart launch.json](/assets/images/category/flutter/2021/dart/launch_json.jpg)

私たちはそのファイルで私たちのDartファイルを指定する必要があります。当該ファイルを開いて下記のように修正します。

```json
{
  ...
  "configurations": [
    {
      ...,
      "program": "main.dart"
    }
  ]
}
```

このように修正したら、また`main.dart`ファイルに移動して、`cmd + shift + d`を押して`debug restart`を再び実行します。そしたら下記のように`DEBUG CONSOLE`に私たちが作成した`Hello world`が表示されることが確認できます。

![VSCode - Dart Hello world](/assets/images/category/flutter/2021/dart/hello_world.jpg)

コードの詳しい説明は省略します。

## 変数

Dartで使える変数を説明します。

### var

JavaScriptの`var`と似てる動きをする変数です。どのタイプの変数も割り当てることができます。

```dart
void main() {
  var value1 = 'test';
  print(value1);

  var value2 = 1;
  print(value2);
}
```

宣言と同時に変数を割り当てた場合、Dartは変数のタイプを固定します。上の例では`value1`は`String`タイプになり、`value2`は`int`タイプになります。

このようにタイプが固定された後、他のタイプを入れるとエラーが発生します。

![VSCode - Dart wrong type error](/assets/images/category/flutter/2021/dart/wrong_type_error.jpg)

しかし、宣言と同時に割り当てないと、どのタイプも入れることができる`Dynamic Type`の変数になります。

```dart
void main() {
  var value1;

  value1 = 'test';
  print(value1);

  value1 = 1;
  print(value1);
}
```

例題ではStringタイプを割り当てた後、またintタイプのデータを入れましたが、以前と違ってエラーが発生したいことが確認できます。

{% include in-feed-ads.html %}

### int

Dartで整数型のデータを扱う場合は`int`タイプを使います。

```dart
void main() {
  int num1 = 2;
  int num2 = 4;

  print(num1 + num2);
  print(num1 - num2);
  print(num1 * num2);
  print(num1 / num2);
}
```

`int`タイプで宣言した変数は基本的な数学演算ができます。

### double

Dartでは実数型データを扱う時`double`タイプを使います。

```dart
void main() {
  double num1 = 2.2;
  double num2 = 4.2;

  print(num1 + num2);
  print(num1 - num2);
  print(num1 * num2);
  print(num1 / num2);
}
```

`double`タイプも基本的数学演算ができます。

### String

Dartで文字列を扱う時は`String`タイプを使います。ここで気をつけることがStringタイプは`int`、`double`と違って大文字(`S`)で始めます。

```dart
void main() {
  String name = 'Yakuza';

  print(name);
  print('Dev ' + name);
  print(name.toUpperCase());
  print(name.toLowerCase());
}
```

`String`タイプは他の言語と同じように`+`を使って結合することができますし、色んな関数を使うことができます。 기호를 통해 합칠 수 있습니다.

### bool

Dartでも`true/false`を保存することができる`Boolean`タイプを持ってます。

```dart
void main() {
  bool wrong = true;
  print(wrong);

  wrong = false;
  print(wrong);
}
```

{% include in-feed-ads.html %}

### List

Dartでは下記のようにリスト変数を宣言してデータを追加することができます。

```dart
void main() {
  List<String> fruits = [];

  fruits.add('Apple');
  fruits.add('Banana');
  fruits.add('Kiwi');

  print(fruits);
  fruits.removeAt(1);
  print(fruits);
}
```

または下記のように生成することもできます。

```dart
void main() {
  List<String> fruits = ['Apple', 'Banana', 'Kiwi'];
  print(fruits);
}
```

また下記のように使うこともできます。

```dart
void main() {
  List<String> fruits = List.from(['Apple', 'Banana', 'Kiwi']);
  print(fruits);
}
```

`List`は上のように可変的なリストを作ることもできますが、下記のように固定サイズのリストも生成することもできます。

```dart
void main() {
  List<String> fruits = List.filled(3, '');

  fruits[0] = 'Apple';
  fruits[1] = 'Banana';
  fruits[2] = 'Kiwi';

  print(fruits);
}
```

ここで気をつけることは固定サイズの`List`は`add`と`removeAt`ようにリストの長さを変える関数は使うことができないことです。

`List`キーワードを使う時、可変なリストも作ることができます。下記のように`List`を生成すると可変リストが生成されます。

```dart
void main() {
  List<String> fruits = List.empty(growable: true);

  fruits.add('Apple');
  fruits.add('Banana');
  fruits.add('Kiwi');

  print(fruits);
}
```

{% include in-feed-ads.html %}

Listでは色んな関数を使うことができます。

- join: 各要素を合わせて1つの文字列を生成します。

  ```dart
  void main() {
    List<String> fruits = ['Apple', 'Banana', 'Kiwi'];
    print(fruits.join(', '));
  }
  ```

- indexOf: 要素を探して、その要素のindexを返します。

  ```dart
  void main() {
    List<String> fruits = ['Apple', 'Banana', 'Kiwi'];
    print(fruits.indexOf('Banana'));
  }
  ```

- where: 条件に合う要素で新しいリストを作ります。

  ```dart
  void main() {
    List<String> fruits = ['Apple', 'Banana', 'Kiwi'];
    print(fruits.where((fruit) => fruit.toLowerCase().indexOf('a') >= 0));
  }
  ```

- forEach: forループと同じ役割

  ```dart
  void main() {
    List<String> fruits = ['Apple', 'Banana', 'Kiwi'];

    fruits.forEach((fruit) {
      print('${fruit}!');
    });

    for (String fruit in fruits) {
      print('${fruit}!!');
    }
  }
  ```

- map: forEachのようにループをしますが、ループ中の関数で返した値で新しリストを作成します。

  ```dart
  void main() {
    List<String> fruits = ['Apple', 'Banana', 'Kiwi'];
    Iterable<String> newFruits = fruits.map((e) {
      return 'My name is ${e}';
    });
    print(newFruits);
    print(newFruits.toList());
  }
  ```

- fold: 初期値を持ってループをしながら、以前の値と現在値を持って新しい結果値を作る時、使います。

  ```dart
  void main() {
    List<int> numbers = [1, 2, 3, 4, 5];
    int result = numbers.fold(0, (previousValue, element) {
      int sum = previousValue + element;
      return sum * 2;
    });
    print(result);
  }
  ```

- reduce: foldとは違って初期値がないです。必ず要素と同じタイプを返さなきゃならないです。

  ```dart
  void main() {
    List<int> numbers = [1, 2, 3, 4, 5];
    int total = numbers.reduce((value, element) => value + element);
    print(total);
  }
  ```

- asMap: ListタイプをMapタイプに変更します。この時生成されたMapはListのindexをキーとして使って生成されます。indexの値が必要な時、よく使えます

  ```dart
  void main() {
    List<int> numbers = [10, 20, 30, 40, 50];
    Iterable indexNumbers = numbers.asMap().entries.map((e) {
      return 'index: ${e.key} / value: ${e.value}';
    });
    print(indexNumbers);
    print(indexNumbers.toList());
  }
  ```

{% include in-feed-ads.html %}

### Map

`Map`は`List`と同じように複数の変数を保存することができますが、`List`と違って`Key Value`でデータを保存します。MapはKey-Valueで値を保存するので、Keyはユニークです。

```dart
void main() {
  Map fruitCount = {
    'Apple': 3,
    'Banana': 4,
    'Kiwi': 10,
  };

  print(fruitCount);
  print(fruitCount['Apple']);
}
```

MapもListと同じように変数を宣言し後、データを追加、削除、変更することができます。

```dart
void main() {
  Map fruitCount = {};

  fruitCount.addAll({
    'Apple': 3,
    'Banana': 4,
    'Kiwi': 10,
  });

  print(fruitCount);
  fruitCount.remove('Apple');
  print(fruitCount);
  fruitCount['Banana'] = 20;
  print(fruitCount);
}
```

Mapは次のように使うこともできます。

```dart
void main() {
  Map fruitCount = new Map.from({
    'Apple': 3,
    'Banana': 4,
    'Kiwi': 10,
  });

  print(fruitCount);
}
```

Mapは色んな機能も提供してます。例えば次のようにMapのKeyとValueをまとめて出力することができます。

```dart
void main() {
  Map fruitCount = new Map.from({
    'Apple': 3,
    'Banana': 4,
    'Kiwi': 10,
  });

  print(fruitCount.keys.toList());
  print(fruitCount.values.toList());
}
```

MapもListようにタイプを設定することができます。

```dart
void main() {
  Map<String, int> fruitCount = {
    'Apple': 3,
    'Banana': 4,
    'Kiwi': 10,
  };

  print(fruitCount);
}
```

Mapには`entries`を使ってループすることができて、結果で新しいリストを作ることができます。

```dart
void main() {
  Map<String, int> fruitCount = {
    'Apple': 3,
    'Banana': 4,
    'Kiwi': 10,
  };

  Iterable newFruitCount =
      fruitCount.entries.map((e) => '${e.key} is ${e.value}!');
  print(newFruitCount);
  print(newFruitCount.toList());
}
```

{% include in-feed-ads.html %}

### enum

Dartでは下記のように`enum`を使うことができます。

```dart
enum Status {
  wait,
  approved,
  reject,
}

void main() {
  Status currentStatus = Status.wait;
  print(currentStatus == Status.approved);
  print(Status.values.toList());
}
```

## 定数

Dartで定数を使う方法について説明します。

### finalとconst

Dartでは`final`と`const`を使って定数を宣言することができます。

```dart
void main() {
  final String firstName = 'Yakuza';
  const String lastName = 'Dev';
  print(firstName);
  print(lastName);
}
```

定数で宣言した変数は変更ができません。

```dart
void main() {
  final String name = 'Yakuza';
  name = 'Dev'; << ERROR
  print(name);
}
```

`final`と`const`は下記のような違さがあります。

- final: ランタイムで定数が指定される
- const: コンパイル時点で定数が指定される。

```dart
void main() {
  final DateTime now = DateTime.now();
  print(now);
}
```

例えば、次のように`DateTime`を使って現在時間を定数で作ってみました。しかし現在時間はランタイムの時、分かるので、次のように`const`で定数を指定するとエラーが発生します。

```dart
void main() {
  const DateTime now = DateTime.now();
  print(now);
}
```

現在時間はプログラムを実装してみないと分からないので、コンパイルの時点では指定できません。

## String Interpolation

Dartでは下記のように文字列に変数を入れって出力することができます。

```dart
void main() {
  String name = 'Yakuza';
  int num = 1;

  print('User: (${num}) ${name}');
}
```

この例題を実行すると下記のような結果が表示されます。

```bash
User: (1) Yakuza
```

## Nullable

今までみた変数は全て初期値を入れてました。初期値を入れないとエラーが発生します。しかしDartでは下記のように初期値を入れなく変数を宣言することもできます。

```dart
void main() {
  String? name;
  name = 'Yakuza';
  print(name);

  name = null;
  print(name);
}
```

上のように`?`を使って、初期値を設定しなくて変数を宣言することができるし、このように宣言した変数は初期値で`null`を持ってます。また、`null`を入れることもできます。

## 変数の特徴

変数は次のような特徴を持ってます。

- 同じ変数名で重複宣言ができない。

    ```dart
    void main() {
      String name = 'Yakuza';
      String name = 'Dev';
      int name = 1;
    }
    ````

- 変数名は小文字で始まり、キャメルケース(Camelcase)で作ります。
- 変数の名前は`_`で始まることが出来ますが、この変数はクラスの`private`変数名で使えます。
- クラスは大文字で始めます。だから、変数の名前を大文字で宣言する場合、クラスと変数を区分することが難しくなります。

## 完了

これでFlutterでアプリを開発するためDartの変数についてみてみました。私たちはDartで自由に変数と定数を宣言することができるようになりました！
