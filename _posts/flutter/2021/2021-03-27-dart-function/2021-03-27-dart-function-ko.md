---
layout: 'post'
permalink: '/flutter/dart/function/'
paginate_path: '/flutter/:num/dart/function/'
lang: 'ko'
categories: 'flutter'
comments: true

title: '[Flutter] Dart에서 함수'
description: Flutter로 앱을 개발하기 위해서 Flutter의 개발 언어인 Dart에 대해서 알아봅시다. 이번 블로그 포스트에서는 Dart에서 함수를 사용하는 방법에 대해서 알아봅니다.
image: '/assets/images/category/flutter/2021/dart/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [함수](#함수)
- [Optional 파라메터](#optional-파라메터)
- [Named 파라메터](#named-파라메터)
- [typedef](#typedef)
- [완료](#완료)

</div>

## 블로그 시리즈

이 블로그는 시리즈로 제작되었습니다. 다음 링크를 통해 다른 블로그 포스트도 확인해 보시기 바랍니다.

- [[MacOS] Flutter 설치]({{site.url}}/{{page.categories}}/installation/){:target="_blank"}
- [[Flutter] Dart에서 변수]({{site.url}}/{{page.categories}}/dart/variable/){:target="_blank"}
- [[Flutter] Dart에서 연산자]({{site.url}}/{{page.categories}}/dart/operator/){:target="_blank"}
- [[Flutter] Dart에서 Statement]({{site.url}}/{{page.categories}}/dart/statement/){:target="_blank"}
- [Flutter] Dart에서 함수
- [[Flutter] Dart에서 클래스]({{site.url}}/{{page.categories}}/dart/class/){:target="_blank"}

## 개요

이번 블로그 포스트에서는 Dart에서 함수를 사용하는 방법에 대해서 설명합니다.

이 블로그 포스트에서 소개하는 소스 코드는 아래에 링크에서 확인할 수 있습니다.

- GitHub: [https://github.com/dev-yakuza/study-flutter/tree/main/dart](https://github.com/dev-yakuza/study-flutter/tree/main/dart){:rel="nofollow noreferrer" target="_blank"}

## 함수

Dart에서는 다음과 같이 `함수`를 선언하고 사용할 수 있습니다.

```dart
String add(int a, int b) {
  int sum = a + b;
  return 'Sum: $sum';
}

void main() {
  print(add(1, 2));
  print(add(3, 4));
  print(add(5, 6));
  print(add(7, 8));
}
```

{% include in-feed-ads.html %}

## Optional 파라메터

다음과 같이 함수를 선언할 때, `Optional 파라메터`를 설정할 수 있으며, Optional 파라메터의 기본값을 설정할 수 있습니다.

```dart
String add(int a, int b, [int c = 0]) {
  int sum = a + b + c;
  return 'Sum: $sum';
}

void main() {
  print(add(1, 1));
  print(add(1, 1, 1));
}
```

## Named 파라메터

함수에서 파라메터가 많아지면, 파라메터의 순서를 기억하고 전달하기가 어려워집니다. 이때, 사용할 수 있는 것이 `Named 파라메터`입니다. Named 파라메터를 사용하면, 함수를 호출할 때, 좀 더 명확하게 파라메터 값을 설정할 수 있습니다.

```dart
String add(int a, int b, {int c = 0, int d = 0}) {
  int sum = a + b + c + d;
  return 'Sum: $sum';
}

void main() {
  print(add(1, 1));
  print(add(1, 1, c: 1));
  print(add(1, 1, d: 1));
  print(add(1, 1, c: 1, d: 1));
}
```

## typedef

Dart에서는 함수를 파라메터로 전달받을 수 있습니다. 하지만, 전달받은 함수의 타입을 지정하지 않으면, 어떤 파라메터를 전달할 수 있는지, 전달받은 함수가 어떤 것인지 정확히 알기가 어렵습니다.

이때 사용할 수 있는 것이 `typedef`입니다. `typedef`는 다음과 같이 파라메터로 전달받을 함수의 타입을 선언하고 지정할 수 있습니다.

```dart
typedef Operator(int n, int m);

String add(int a, int b) {
  int sum = a + b;
  return 'Sum: $sum';
}

String substract(int c, int d) {
  int sub = c - d;
  return 'Sub: $sub';
}

String calculate(int x, int y, Operator op) {
  return op(x, y);
}

void main() {
  print(add(2, 1));
  print(substract(2, 1));

  Operator op = add;
  print(op(2, 1));

  op = substract;
  print(op(2, 1));

  print(calculate(2, 1, add));
  print(calculate(2, 1, substract));
}
```

## 완료

이것으로 Flutter로 앱을 개발하기 위해 Dart에서 사용되는 함수에 대해서 살펴보았습니다. 기본적으로 다른 프로그래밍 언어에서 선언하고 사용하는 함수가 큰 차이가 없음을 알 수 있었습니다. 또한 `typedef`를 사용하여 함수의 타입을 선언하고 파라메터로 지정하는 방법도 알아보았습니다.
