---
layout: 'post'
permalink: '/flutter/dart/class/'
paginate_path: '/flutter/:num/dart/class/'
lang: 'ja'
categories: 'flutter'
comments: true

title: '[Flutter] Dartのクラス'
description: Flutterでアプリを開発するためFlutterの開発言語であるDartについて説明します。今回のブログポストではDartでクラスを使う方法について説明します。
image: '/assets/images/category/flutter/2021/dart/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [クラス](#クラス)
  - [コンストラクト](#コンストラクト)
  - [final](#final)
  - [Private変数](#private変数)
  - [GetterとSetter](#getterとsetter)
  - [継承](#継承)
  - [オーバーライド](#オーバーライド)
  - [静的メンバー](#静的メンバー)
  - [インタフェース](#インタフェース)
- [Cascade Operator](#cascade-operator)
- [完了](#完了)

</div>

## ブログシリーズ

このブログはシリーズで作成しております。下記のリンクを参考して他のブログポストも確認してみてください。

- [[MacOS] Flutterのインストール]({{site.url}}/{{page.categories}}/installation/){:target="_blank"}
- [[Flutter] Dartの変数]({{site.url}}/{{page.categories}}/dart/variable/){:target="_blank"}
- [[Flutter] Dartの演算子]({{site.url}}/{{page.categories}}/dart/operator/){:target="_blank"}
- [[Flutter] DartのStatement]({{site.url}}/{{page.categories}}/dart/statement/){:target="_blank"}
- [[Flutter] Dartの関数]({{site.url}}/{{page.categories}}/dart/function/){:target="_blank"}
- [Flutter] Dartのクラス

## 概要

今回のブログポストではDartでクラスを使う方法について説明します。

## クラス

クラスを宣言する時、クラス名は大文字で始めます。クラスはメンバー変数やメンバー関数を持ってることができます。

```dart
class Fruit {
  String name = 'Apple';

  void printName() {
    print('My name is ${this.name}!');
  }
}

void main() {
  Fruit fruit = new Fruit();
  fruit.printName();
  fruit.name = 'Banana';
  fruit.printName();
}
```

クラスのメンバー変数とメンバー関数は`.`を使って使うことができます。

{% include in-feed-ads.html %}

### コンストラクト

クラスは`コンストラクト(Constructor)`を持ってます。コンストラクトはクラスと同じ名前で宣言をします。

```dart
class Fruit {
  String? name;
  String? color;

  Fruit(String name, String color) {
    this.name = name;
    this.color = color;
  }

  void printName() {
    print('My name is ${this.name}(${this.color})!');
  }
}

void main() {
  Fruit fruit = new Fruit('Apple', 'Red');
  fruit.printName();
}
```

クラスのコンストラクトは下記のように宣言することもできます。

```dart
class Fruit {
  String? name;
  String? color;

  Fruit(String name, String color)
      : this.name = name,
        this.color = color;

  void printName() {
    print('My name is ${this.name}(${this.color})!');
  }
}

void main() {
  Fruit fruit = new Fruit('Apple', 'Red');
  fruit.printName();
}
```

コンストラクトにも`Namedパラメーター`を使うことができます。

```dart
class Fruit {
  String? name;
  String? color;

  Fruit({String? name, String? color})
      : this.name = name,
        this.color = color;

  void printName() {
    print('My name is ${this.name}(${this.color})!');
  }
}

void main() {
  Fruit fruit = new Fruit(color: 'Red', name: 'Apple');
  fruit.printName();
}
```

Dartでは`Namedコンストラクト`と言う機能も提供しております。

```dart
class Fruit {
  String? name;
  String? color;

  Fruit({String? name, String? color})
      : this.name = name,
        this.color = color;

  // Named Constructor: You can use any name on [fromMap]
  Fruit.fromMap(Map<String, String> fruit)
      : this.name = fruit['name'],
        this.color = fruit['color'];

  void printName() {
    print('My name is ${this.name}(${this.color})!');
  }
}

void main() {
  Fruit fruit = new Fruit(name: 'Apple', color: 'Red');
  fruit.printName();

  Fruit fruitFromMap = new Fruit.fromMap({'color': 'Red', 'name': 'Apple'});
  fruitFromMap.printName();
}
```

{% include in-feed-ads.html %}

### final

クラスで`final`を使ってインスタンスを生成する時、定数を設定することができます。

```dart
class Fruit {
  final String? name;
  final String? color;

  Fruit({String? name, String? color})
      : this.name = name,
        this.color = color;

  void printName() {
    print('My name is ${this.name}(${this.color})!');
  }
}

void main() {
  Fruit fruit = new Fruit(name: 'Apple', color: 'Red');
  fruit.printName();

  fruit.name = 'Kiwi'; // << ERROR
}
```

### Private変数

Dartでは変数名の前に`_`を追加して`Private変数`を作ることができます。クラスの中だけPrivate変数が使える他の言語とは違って、Dartではクラスが定義されたファイル中でPrivate変数にアクセスすることができます。

```dart
class Fruit {
  String? _name;

  Fruit(String name) : this._name = name;

  void printName() {
    print('My name is ${this._name}!');
  }
}

void main() {
  Fruit fruit = new Fruit('Apple');
  fruit.printName();
  // Print Private variable
  // It's possibe because of same file.
  print(fruit._name);
}
```

### GetterとSetter

クラスがPrivate変数を持って流場合、当該変数について`Getter`と`Setter`を生成することができます。GetterとSetterの名前は何でもつけることができますが、普通Privateの変数名で`_`を抜いた名前を使います。

```dart
class Fruit {
  String? _name;

  Fruit(String name) : this._name = name;

  String get name {
    return this._name ?? '';
  }

  void set name(String name) {
    this._name = name;
  }
}

void main() {
  Fruit fruit = new Fruit('Apple');

  print(fruit.name); // Getter
  fruit.name = 'Banana'; //Setter
  print(fruit.name);
}
```

{% include in-feed-ads.html %}

### 継承

クラスは他のクラスを`継承(Inheritance)`することができます。継承する時は`extends`キーワードを使います。Dartでは1つのクラスだけ継承することができるし、親クラスにアクセスする時は`super`キーワードを使います。

```dart
class Food {
  String? name;

  Food(String name) : this.name = name;

  void printName() {
    print('My name is ${this.name}!');
  }
}

// Inheritance
class Fruit extends Food {
  // Call parent constructor
  Fruit(String name) : super(name);

  void printFruit() {
    print('${this.name} is Fruit!');
  }
}

void main() {
  Fruit fruit = new Fruit('Apple');
  fruit.printName();
  fruit.printFruit();

  Food food = new Food('Rice');
  food.printName();
  food.printFruit(); // << ERROR
}
```

### オーバーライド

子クラスで親クラスの関数を`オーバーライド(Override)`することができます。オーバーライドとは親クラスで定義された関数を子クラスで再定義することを意味します。

```dart
class Food {
  String? name;

  Food(String name) : this.name = name;

  void printName() {
    print('My name is ${this.name}!');
  }
}

class Fruit extends Food {
  Fruit(String name) : super(name);

  void printName() {
    super.printName();
    print('${this.name} is Fruit!');
  }
}

void main() {
  Fruit fruit = new Fruit('Apple');
  fruit.printName();

  Food food = new Food('Rice');
  food.printName();
}
```

オーバーライドをする時、`@override`キーワードを使ってもうちょっと明確オーバーライドを指定することできます。

```dart
class Food {
  String? name;

  Food(String name) : this.name = name;

  void printName() {
    print('My name is ${this.name}!');
  }
}

class Fruit extends Food {
  Fruit(String name) : super(name);

  @override
  void printName() {
    print('${this.name} is Fruit!');
  }
}

void main() {
  Fruit fruit = new Fruit('Apple');
  fruit.printName();

  Food food = new Food('Rice');
  food.printName();
}
```

{% include in-feed-ads.html %}

### 静的メンバー

Dartでも静的メンバー変数と関数を使うことができます。静的メンバーを宣言する時には`static`キーワードを使います。

```dart
class Food {
  static String? kind;
  String? name;

  Food(String name) : this.name = name;

  static printAll(String name, String kind) {
    print('${name} is ${kind}!');
  }

  void printName() {
    print('My name is ${this.name}! I am ${kind}!');
  }

}

void main() {
  Food apple = new Food('Apple');
  apple.printName();
  Food banana = new Food('Banana');
  banana.printName();

  Food.kind = 'Fruit';
  apple.printName();
  banana.printName();

  Food.printAll('Apple', 'Red Fruit');
}
```

### インタフェース

Dartではクラスを使って`インタフェース(Interface)`を定義します。インタフェースはクラスを定義する時、必ず定義する変数や関数を指定するとき使います。他の言語とは違ってDartでは`Interface`と言うキーワードの代わりで`class`を使ってインタフェースを定義し、`implements`を使って使います。

```dart
class Food {
  String? name;

  void printName() {}
}

class Fruit implements Food {
  String? name;

  Fruit(String name) : this.name = name;

  void printName() {
    print('My name is ${this.name}!');
  }
}

void main() {
  Fruit fruit = new Fruit('Apple');
  fruit.printName();
}
```

インタフェースではクラスで使う関数だけ定義して、関数の内容は作成しません。インタフェースを使うクラスにその関数の内容を作成します。

## Cascade Operator

Dartには`Cascade Operator`と言う機能が提供されております。クラス以外にも使えますが、クラスで説明することが簡単なので、ここで紹介します。

```dart
class Fruit {
  String? name;
  String? color;

  Fruit(String name, String color)
      : this.name = name,
        this.color = color;

  void printAll() {
    print('My name is ${this.name}(${this.color})!');
  }

  void printName() {
    print('My name is ${this.name}!');
  }

  void printColor() {
    print('I am ${this.color}');
  }
}

void main() {
  Fruit fruit = new Fruit('Apple', 'Red');
  fruit.printAll();
  fruit.printName();
  fruit.printColor();

  new Fruit('Apple', 'Red')
    ..printAll()
    ..printName()
    ..printColor();
}
```

例題ように`Cascade Operator`(`..`)を使うとクラスを宣言する時、クラスの関数も同時に使うことができます。

{% include in-feed-ads.html %}

## 完了

これでFlutterでアプリを開発するためDartで使えるクラスについてみてみました。Dartも`オブジェクト指向プログラミング(Object-Oriented Programming, OOP)`なので、クラスを提供するし、他のOOP言語で活用できる機能をほとんど提供しております。
