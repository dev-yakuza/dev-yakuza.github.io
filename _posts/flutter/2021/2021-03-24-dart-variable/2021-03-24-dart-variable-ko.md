---
layout: 'post'
permalink: '/flutter/dart/variable/'
paginate_path: '/flutter/:num/dart/variable/'
lang: 'ko'
categories: 'flutter'
comments: true

title: '[Flutter] Dart에서 변수'
description: Flutter로 앱을 개발하기 위해서 Flutter의 개발 언어인 Dart에 대해서 알아봅시다. 이번 블로그 포스트에서는 Dart의 변수에 대해서 알아봅니다.
image: '/assets/images/category/flutter/2021/dart/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [개발 환경](#개발-환경)
- [Hello world](#hello-world)
- [변수](#변수)
  - [var](#var)
  - [int](#int)
  - [double](#double)
  - [String](#string)
  - [bool](#bool)
  - [List](#list)
  - [Map](#map)
  - [enum](#enum)
- [상수](#상수)
  - [final과 const](#final과-const)
- [String Interpolation](#string-interpolation)
- [Nullable](#nullable)
- [변수의 특징](#변수의-특징)
- [완료](#완료)

</div>

## 블로그 시리즈

이 블로그는 시리즈로 제작되었습니다. 다음 링크를 통해 다른 블로그 포스트도 확인해 보시기 바랍니다.

- [[MacOS] Flutter 설치]({{site.url}}/{{page.categories}}/installation/){:target="_blank"}
- [Flutter] Dart에서 변수
- [[Flutter] Dart에서 연산자]({{site.url}}/{{page.categories}}/dart/operator/){:target="_blank"}
- [[Flutter] Dart에서 Statement]({{site.url}}/{{page.categories}}/dart/statement/){:target="_blank"}
- [[Flutter] Dart에서 함수]({{site.url}}/{{page.categories}}/dart/function/){:target="_blank"}
- [[Flutter] Dart에서 클래스]({{site.url}}/{{page.categories}}/dart/class/){:target="_blank"}

## 개요

Flutter는 구글에서 개발한 Dart라는 언어를 사용하여 개발을 하게 됩니다.

- Dart: [공식 홈페이지](https://dart.dev/){:rel="nofollow noreferrer" target="_blank"}

이번 블로그 포스트에서는 Flutter에서 사용되는 Dart 언어의 기본 사용법에 대해서 알아보고, Dart의 변수에 대해서 자세히 알보겠습니다.

이 블로그 포스트에서 소개하는 소스 코드는 아래에 링크에서 확인할 수 있습니다.

- GitHub: [https://github.com/dev-yakuza/study-flutter/tree/main/dart](https://github.com/dev-yakuza/study-flutter/tree/main/dart){:rel="nofollow noreferrer" target="_blank"}

## 개발 환경

Dart를 로컬에서 개발하기 위해서는 Flutter를 설치하고 설정할 필요가 있습니다. 이전 블로그 포스트를 참고하여 개발 환경을 구축하시기 바랍니다.

- [[MacOS] Flutter 설치]({{site.url}}/{{page.categories}}/installation/){:target="_blank"}

이번 블로그 포스트에서는 Flutter의 설치 및 설정이 완료되었다고 가정하고 진행합니다. 그럼 Dart 언어를 사용하기 위해 새로운 폴더를 생성합니다.

```bash
mkdir dart
cd dart
```

그리고 아래 명령어를 사용하여 VSCode를 실행합니다.

```bash
code .
```

{% include in-feed-ads.html %}

## Hello world

그럼 이제 Dart 언어를 사용하여 코딩하기 위해, Dart 파일을 생성해 봅시다. VSCode에서 다음과 같이 새 파일 버튼을 눌러 새로운 파일을 생성합니다.

![VSCode - create Dart file](/assets/images/category/flutter/2021/dart/new_file.jpg)

파일명은 아무거나 사용할 수 있지만, 여기서는 `main.dart`이라고 지정하겠습니다. 이렇게 새로운 파일이 생성되면, 해당 파일을 열고 다음과 같이 작성합니다.

```dart
void main() {
  print('Hello world!');
}
```

모든 내용을 작성하였다면, 이제 `cmd + shift + d` 키를 누르고, `Debug: restart`를 검색한 후 실행합니다.

![VSCode - Dart debugging](/assets/images/category/flutter/2021/dart/debug_restart.jpg)

그럼 VSCode에서 `.vscode/launch.json` 파일을 자동으로 생성해 줍니다.

![VSCode - Dart launch.json](/assets/images/category/flutter/2021/dart/launch_json.jpg)

그럼 해당 파일에 우리가 생성한 Dart 파일을 지정해 줄 필요가 있습니다. 해당 파일을 열고 다음과 같이 수정합니다.

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

이렇게 파일을 수정하였다면 다시 `main.dart` 파일로 이동한 후, `cmd + shift + d` 키를 누르고, `debug restart`를 다시 실행합니다. 그럼 다음과 같이 VSCode 하단의 `DEBUG CONSOLE`에 우리가 작성한 `Hello world`가 표시되는 것을 확인할 수 있습니다.

![VSCode - Dart Hello world](/assets/images/category/flutter/2021/dart/hello_world.jpg)

코드의 자세한 설명은 생략하도록 하겠습니다.

## 변수

Dart에서 사용되는 변수를 설명합니다.

### var

자바스크립트의 `var`와 비슷한 동작을 하는 변수 타입입니다. 어떤 타입의 변수도 할당할 수 있습니다.

```dart
void main() {
  var value1 = 'test';
  print(value1);

  var value2 = 1;
  print(value2);
}
```

선언과 동시에 변수를 할당한 경우, Dart는 해당 변수의 타입을 고정시키게 됩니다. 즉 `value1`은 `String` 타입이 되며 `value2`는 `int`형 타입이 됩니다.

이렇게 타입이 고정된 상태에서 다른 타입에 데이터를 추가하게 되면 에러가 발생하게 됩니다.

![VSCode - Dart wrong type error](/assets/images/category/flutter/2021/dart/wrong_type_error.jpg)

하지만 반대로, 선언과 동시에 할당하지 않은 경우, 어떠한 데이터 타입도 저장할 수 있는 `Dynamic Type` 변수가 됩니다.

```dart
void main() {
  var value1;

  value1 = 'test';
  print(value1);

  value1 = 1;
  print(value1);
}
```

예제와 같이 String 데이터를 할당한 후, 다시 int 데이터를 할당하였지만, 이전과 다르게 에러가 발생하지 않는 것을 확인할 수 있습니다.

{% include in-feed-ads.html %}

### int

Dart에서 정수형 데이터를 다룰때는 `int` 타입을 사용합니다.

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

`int` 타입으로 선언된 변수는 기본적인 수학 연산이 가능합니다.

### double

Dart에서 실수형 데이터를 다룰때는 `double` 타입을 사용합니다.

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

`double` 타입으로 선언된 변수는 기본적인 수학 연산이 가능합니다.

### String

Dart에서 문자열 데이터를 다룰때는 `String` 타입을 사용합니다. 여기서 주의해야할 점은 String 타입은 `int`, `double`과는 다르게 대문자(`S`)로 시작합니다.

```dart
void main() {
  String name = 'Yakuza';

  print(name);
  print('Dev ' + name);
  print(name.toUpperCase());
  print(name.toLowerCase());
}
```

`String` 타입은 다른 언어들과 마찬가지로 `+` 기호를 통해 합칠 수 있으며, 여러 함수들을 사용할 수 있습니다.

### bool

Dart에서도 `참/거짓`을 저장할 수 있는 `Boolean` 변수를 선언하여 사용할 수 있습니다.

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

Dart에서는 다음과 같이 리스트 변수를 선언하고 데이터를 추가할 수 있습니다.

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

또는 다음과 같이 생성할 수도 있습니다.

```dart
void main() {
  List<String> fruits = ['Apple', 'Banana', 'Kiwi'];
  print(fruits);
}
```

또는 다음과 같이도 사용할 수 있습니다.

```dart
void main() {
  List<String> fruits = List.from(['Apple', 'Banana', 'Kiwi']);
  print(fruits);
}
```

`List`는 위와 같이 가변적인 길이를 가지는 리스트를 만들 수 있지만, 다음과 같이 고정된 크기의 리스트를 생성할 수도 있습니다.

```dart
void main() {
  List<String> fruits = List.filled(3, '');

  fruits[0] = 'Apple';
  fruits[1] = 'Banana';
  fruits[2] = 'Kiwi';

  print(fruits);
}
```

주의해야할 점은 고정된 크기로 생성된 `List`는 `add`와 `removeAt`과 같이 리스트의 길이를 변경하는 함수는 사용할 수 없습니다.

`List` 키워드를 사용해서 꼭 고정된 크기의 리스트만 생성할 수 있는 것은 아닙니다. 다음과 같이 `List`를 생성하면, 가변적인 리스트도 생성할 수 있습니다.

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

List에서는 다양한 함수를 사용할 수 있다.

- join: 각 요소를 합쳐서 하나의 문자열로 만듬

  ```dart
  void main() {
    List<String> fruits = ['Apple', 'Banana', 'Kiwi'];
    print(fruits.join(', '));
  }
  ```

- indexOf: 요소를 찾고, 해당 요소의 index를 반환한다.

  ```dart
  void main() {
    List<String> fruits = ['Apple', 'Banana', 'Kiwi'];
    print(fruits.indexOf('Banana'));
  }
  ```

- where: 조건에 맞는 요소를 새로운 리스트로 만들어 반환한다.

  ```dart
  void main() {
    List<String> fruits = ['Apple', 'Banana', 'Kiwi'];
    print(fruits.where((fruit) => fruit.toLowerCase().indexOf('a') >= 0));
  }
  ```

- forEach: for 루프와 같은 역할을 한다.

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

- map: forEach와 같이 루프를 돌지만, 루프안에 함수에서 반환한 값을 가지고 새로운 리스트를 만든다.

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

- fold: 초기 시작값을 시작으로 루프를 돌면서, 이전값과 현재값을 가지고 새로운 결과값을 생성할 때 사용한다.

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

- reduce: fold와 다르게 초기 시작값이 없으며, 반드시 요소와 같은 타입을 반환해야한다.

  ```dart
  void main() {
    List<int> numbers = [1, 2, 3, 4, 5];
    int total = numbers.reduce((value, element) => value + element);
    print(total);
  }
  ```

- asMap: List 타입을 Map 타입으로 변경하며, 이때 새롭게 생성되는 Map은 List의 index를 키값으로 가지게 됩니다. index 값이 필요할 때 자주 사용됩니다.

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

`Map`은 `List`와 같이 복수의 변수를 저장할 수 있지만, `List`와는 달리 `Key Value`로 데이터를 저장합니다. Map은 Key-Value로 값을 저장하므로 Key는 항상 유니크해야합니다.

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

Map도 List와 같이 변수를 선언한 후, 데이터를 추가, 삭제, 변경을 할 수 있습니다.

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

Map은 다음과 같이도 사용할 수 있습니다.

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

Map에는 다양한 기능들이 제공되고 있습니다. 예를 들어 다음과 같이 Map의 Key 값 또는 Value 값만 모아서 출력할 수 있습니다.

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

Map도 List와 같이 타입을 지정할 수 있습니다.

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

Map에서는 `entries`를 사용해서 루프를 돌 수 있으며, 결과값으로 List를 생성할 수 있습니다.

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

Dart에서는 다음과 같이 `enum`을 사용할 수 있습니다.

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

## 상수

Dart에서 상수를 사용하는 방법에 대해서 알아봅시다.

### final과 const

Dart에서는 `final`과 `const`를 사용하여 상수를 선언할 수 있습니다.

```dart
void main() {
  final String firstName = 'Yakuza';
  const String lastName = 'Dev';
  print(firstName);
  print(lastName);
}
```

상수로 선언된 변수는 변경이 불가능합니다.

```dart
void main() {
  final String name = 'Yakuza';
  name = 'Dev'; << ERROR
  print(name);
}
```

`final`과 `const`는 다음과 같은 차이점을 가지고 있습니다.

- final: 런타임에 상수가 지정된다.
- const: 컴파일 시점에 상수가 지정되야 한다.

```dart
void main() {
  final DateTime now = DateTime.now();
  print(now);
}
```

예를 들어, 다음과 같이 `DateTime`을 사용하여 현재 시간을 상수로 만들었습니다. 하지만 현재 시간은 런타임에서 알 수 있으므로, 다음과 같이 `const`로는 상수를 지정할 수 없습니다.

```dart
void main() {
  const DateTime now = DateTime.now();
  print(now);
}
```

현재 시간은 프로그램을 구동시켜야만 알 수 있고, 컴파일 시점에는 알 수가 없기 때문이다.

## String Interpolation

Dart에서는 다음과 같이 문자열에 변수를 삽입할 수 있습니다.

```dart
void main() {
  String name = 'Yakuza';
  int num = 1;

  print('User: (${num}) ${name}');
}
```

이 예제를 실행하면 다음과 같은 결과를 얻을 수 있습니다.

```console
User: (1) Yakuza
```

## Nullable

지금까지 살펴본 변수는 모두 초기값을 대입했습니다. 초기값을 대입하지 않으면 에러가 발생합니다. 하지만, Dart에서도 다음과 같이 초기값을 대입하지 않고 변수를 선언할 수 있습니다.

```dart
void main() {
  String? name;
  name = 'Yakuza';
  print(name);

  name = null;
  print(name);
}
```

위와 같이 `?` 기호를 사용하면, 초기값을 설정하지 않고 변수를 선언할 수 있으며, 이렇게 선언한 변수는 초기값으로 `null`을 가지게 됩니다. 또한, `null`을 대입할 수도 있습니다.

## 변수의 특징

변수는 다음과 같은 특징을 가지고 있습니다.

- 같은 변수명을 가지고 중복 선언을 할 수 없다.

    ```dart
    void main() {
      String name = 'Yakuza';
      String name = 'Dev';
      int name = 1;
    }
    ````

- 변수 이름은 소문자로 시작하고, 카멜케이스(Camelcase)를 따른다.
- 변수의 이름은 `_`로 시작할 수 있으며, 이 변수는 클래스의 `private` 변수명으로 사용된다.
- 클래스는 대문자로 시작한다. 따라서 변수의 이름을 대문자로 선언하면, 클래스와 변수 구분이 어려워진다.

## 완료

이것으로 Flutter로 앱을 개발하기 위해 Dart의 변수에 대해서 알아보았습니다. 이제 Dart에서 자유롭게 변수와 상수를 선언할 수 있게 되었습니다.
