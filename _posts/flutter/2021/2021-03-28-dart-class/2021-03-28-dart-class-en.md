---
layout: 'post'
permalink: '/flutter/dart/class/'
paginate_path: '/flutter/:num/dart/class/'
lang: 'en'
categories: 'flutter'
comments: true

title: '[Flutter] Class in Dart'
description: Let's see how to use Dart for developing an app with Flutter. In this blog post, I will introduce how to create the Class and how to use it.
image: '/assets/images/category/flutter/2021/dart/background.jpg'
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [Class](#class)
  - [Constructor](#constructor)
  - [final](#final)
  - [Private vairables](#private-vairables)
  - [Getter and Setter](#getter-and-setter)
  - [Inheritance](#inheritance)
  - [Override](#override)
  - [Static members](#static-members)
  - [Interface](#interface)
- [Cascade Operator](#cascade-operator)
- [Completed](#completed)

</div>

## Blog series

This blog post is a series. You can see the other posts on the link below.

- [[MacOS] Flutter installation]({{site.url}}/{{page.categories}}/installation/){:target="_blank"}
- [[Flutter] Variable in Dart]({{site.url}}/{{page.categories}}/dart/variable/){:target="_blank"}
- [[Flutter] Operator in Dart]({{site.url}}/{{page.categories}}/dart/operator/){:target="_blank"}
- [[Flutter] Statement in Dart]({{site.url}}/{{page.categories}}/dart/statement/){:target="_blank"}
- [[Flutter] Function in Dart]({{site.url}}/{{page.categories}}/dart/function/){:target="_blank"}
- [Flutter] Class in Dart

## Outline

In this blog post, you'll see how to use the Class in Dart.

You can see the source code, that is introduced on this blog post, on the link below

- GitHub: [https://github.com/dev-yakuza/study-flutter/tree/main/dart](https://github.com/dev-yakuza/study-flutter/tree/main/dart){:rel="nofollow noreferrer" target="_blank"}

## Class

When you define the Class, the Class name should be started with the uppercase letter. The Class has member variables and functions.

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

You can access the Class member variables or functions by using `.`.

{% include in-feed-ads.html %}

### Constructor

The Class can have `Constructor`. The constructor name should be same with the Class name.

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

You can also define the Class constructor like below.

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

You can use `Named parameter` in the Class constrcuctor.

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

Dart provices `Named constructor` feature.

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

You can use `final` in the Class to create constants when the instance is created.

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

### Private vairables

You can add `_` to the variable name to create `Private variable`. The Dart Private variable, that is used only in the Class on the other langauges, can be accessed in the same file.

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

### Getter and Setter

When the Class has the Private variable, you can define `Getter` and `Setter` for the variable. You can define any name for Getter and Setter, but normally the variable name without `_` of the Private variable is used.

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

### Inheritance

The Class can inherit the another Class. You use `extends` keyword to create the inherited Class. In Dart, the Class can inherit just one class, and the `super` keyword is used to acces the parent Class.

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

### Override

The child Class can `override` the parent Class function. The `Override` is that you can re-define the parent Class function in the child Class.

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

When you override, you can use `@override` keyword to override it more clearly.

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

### Static members

In Dart, you can define the Static mebmers and functions. When you define the Static members, you use `static` keyword.

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

### Interface

In Dart, you can use the Class to define the `Interface`. You can use the Interface to define the Class with including the specific variables or functions. Unlike other languages, The `class` keyword is used instead of the `Interface` keyword to define the Interface in Dart, and the `implements` keyword is used to use the Interface.

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

In the Interface, we define the Function, but don't write the contents of the Function. When we create the Class with the Interface, we define the contents of the Function.

## Cascade Operator

Dart provides the `Cascade Operator` feature. This feature is used other parts, but it's easy to explain it with the Class, so I will introduce it here.

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

As the example, you can use the `Cascade Operator`(`..`) to use the various functions when you create the instance of the Class.

{% include in-feed-ads.html %}

## Completed

We've seen how to use the Class in Dart for developing an app with Flutter. Dart is also `Object-Oriented Programming (OOP)` langauge, so Dart provides the Class and we can use the features of OOP like other languages.
