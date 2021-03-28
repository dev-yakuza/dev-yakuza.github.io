---
layout: 'post'
permalink: '/flutter/dart/class/'
paginate_path: '/flutter/:num/dart/class/'
lang: 'ko'
categories: 'flutter'
comments: true

title: '[Flutter] Dart에서 클래스'
description: Flutter로 앱을 개발하기 위해서 Flutter의 개발 언어인 Dart에 대해서 알아봅시다. 이번 블로그 포스트에서는 Dart에서 클래스를 사용하는 방법에 대해서 알아봅니다.
image: '/assets/images/category/flutter/2021/dart/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [클래스](#클래스)
  - [생성자](#생성자)
  - [final](#final)
  - [Private 변수](#private-변수)
  - [Getter와 Setter](#getter와-setter)
  - [상속](#상속)
  - [오버라이드](#오버라이드)
  - [정적 멤버](#정적-멤버)
  - [인터페이스](#인터페이스)
- [Cascade Operator](#cascade-operator)
- [완료](#완료)

</div>

## 블로그 시리즈

이 블로그는 시리즈로 제작되었습니다. 다음 링크를 통해 다른 블로그 포스트도 확인해 보시기 바랍니다.

- [[MacOS] Flutter 설치]({{site.url}}/{{page.categories}}/installation/){:target="_blank"}
- [[Flutter] Dart에서 변수]({{site.url}}/{{page.categories}}/dart/variable/){:target="_blank"}
- [[Flutter] Dart에서 연산자]({{site.url}}/{{page.categories}}/dart/operator/){:target="_blank"}
- [[Flutter] Dart에서 Statement]({{site.url}}/{{page.categories}}/dart/statement/){:target="_blank"}
- [[Flutter] Dart에서 함수]({{site.url}}/{{page.categories}}/dart/function/){:target="_blank"}
- [Flutter] Dart에서 클래스

## 개요

이번 블로그 포스트에서는 Dart에서 클래스를 사용하는 방법에 대해서 설명합니다.

## 클래스

클래스를 선언할 때, 클래스명은 대문자로 시작해야 합니다. 클래스는 멤버 변수와 멤버 함수를 가질 수 있습니다.

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

클래스의 멤버 변수와 멤버 함수는 `.`을 사용하여 접근할 수 있습니다.

{% include in-feed-ads.html %}

### 생성자

클래스는 `생성자(Constructor)`를 가질 수 있습니다. 생성자는 클래스와 동일한 이름으로 선언합니다.

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

클래스의 생성자는 다음과 같이도 선언할 수 있습니다.

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

생성자에서도 `Named 파라메터`를 사용할 수 있습니다.

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

Dart에서는 `Named 생성자`라는 기능을 제공하고 있습니다.

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

클래스에서 `final`을 사용해서 인스턴스를 생성할 때, 상수를 설정할 수 있습니다.

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

### Private 변수

Dart에서는 변수명 앞에 `_`를 추가함으로써, `Private 변수`를 생성할 수 있습니다. 클래스안에서만 Private 변수가 사용 가능한 다른 언어와는 달리, Dart에서는 클래스가 정의된 파일에서는 Private 변수에 접근할 수 있습니다.

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

### Getter와 Setter

클래스가 Private 변수를 가지고 있으면, 해당 변수에 대해 `Getter`와 `Setter`를 생성할 수 있습니다. Getter와 Setter의 이름은 아무거나 지정할 수 있지만, 보통 Private 변수명에서 `_`를 제거한 이름을 사용합니다.

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

### 상속

클래스는 다른 클래스를 `상속(Inheritance)`받을 수 있습니다. 상속 받을 때에는 `extends`라는 키워드를 사용합니다. Dart에서는 하나의 클래스만 상속이 가능하며, 부모 클래스에 접근하기 위해서는 `super` 키워드를 사용합니다.

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

### 오버라이드

자식 클래스에서 부모 클래스의 함수를 `오버라이드(Override)`이 가능합니다. 오버라이드이란 부모 클래스에 정의된 함수를 자식 클래스에서 재정의 하는 것을 의미합니다.

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

오버라이드을 할 때, `@override` 키워드를 사용하여 좀 더 명확하게 오버라이드을 지정할 수 있습니다.

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

### 정적 멤버

Dart에서도 정적 멤버 변수와 함수를 사용할 수 있습니다. 정적 멤버를 선언할 때에는 `static` 키워드를 사용합니다.

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

### 인터페이스

Dart에서는 클래스를 활용하여 `인터페이스(Interface)`를 정의할 수 있습니다. 인터페이스는 클래스를 정의할 때, 반드시 정의해야하는 변수와 함수를 지정할 때 사용합니다. 다른 언어와는 다르게 Dart에서는 `Interface`라는 키워드 대신 `class`를 사용하여 인터페이스를 정의하고, `implements`를 사용하여 사용합니다.

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

인터페이스로 사용할 클래스에서는 함수는 정의만 하고, 함수의 내용은 작성하지 않습니다. 인터페이스를 사용하는 클래스에서 해당 함수의 기능을 작성합니다.

## Cascade Operator

Dart에서는 `Cascade Operator`라는 기능을 제공합니다. 클래스 이외에서도 사용이 되지만 클래스에서 설명하기 쉽기 때문에, 여기서 소개합니다.

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

예제와 같이 `Cascade Operator`(`..`)을 활용하면 클래스를 선언함과 동시에, 클래스에 함수들을 동시에 사용할 수 있습니다.

{% include in-feed-ads.html %}

## 완료

이것으로 Flutter로 앱을 개발하기 위해 Dart에서 사용되는 클래스에 대해서 살펴보았습니다. Dart도 `객체 지향 프로그래밍(Object-Oriented Programming, OOP)` 언어이므로 클래스를 제공하며, 다른 OOP 언어들에서 활용 가능한 기능들을 대부분 제공하고 있습니다.
