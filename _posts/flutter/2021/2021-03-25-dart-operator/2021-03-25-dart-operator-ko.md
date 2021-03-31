---
layout: 'post'
permalink: '/flutter/dart/operator/'
paginate_path: '/flutter/:num/dart/operator/'
lang: 'ko'
categories: 'flutter'
comments: true

title: '[Flutter] Dart에서 연산자'
description: Flutter로 앱을 개발하기 위해서 Flutter의 개발 언어인 Dart에 대해서 알아봅시다. 이번 블로그 포스트에서는 Dart의 연산자에 대해서 알아봅니다.
image: '/assets/images/category/flutter/2021/dart/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [산술 연산자](#산술-연산자)
- [비교 연산자](#비교-연산자)
- [타입 비교 연산자](#타입-비교-연산자)
- [논리 연산자](#논리-연산자)
- [Null-aware operator](#null-aware-operator)
- [완료](#완료)

</div>

## 블로그 시리즈

이 블로그는 시리즈로 제작되었습니다. 다음 링크를 통해 다른 블로그 포스트도 확인해 보시기 바랍니다.

- [[MacOS] Flutter 설치]({{site.url}}/{{page.categories}}/installation/){:target="_blank"}
- [[Flutter] Dart에서 변수]({{site.url}}/{{page.categories}}/dart/variable/){:target="_blank"}
- [Flutter] Dart에서 연산자
- [[Flutter] Dart에서 Statement]({{site.url}}/{{page.categories}}/dart/statement/){:target="_blank"}
- [[Flutter] Dart에서 함수]({{site.url}}/{{page.categories}}/dart/function/){:target="_blank"}
- [[Flutter] Dart에서 클래스]({{site.url}}/{{page.categories}}/dart/class/){:target="_blank"}

## 개요

이번 블로그 포스트에서는 Dart에서 연산자를 사용하는 방법에 대해서 살펴보도록 하겠습니다.

이 블로그 포스트에서 소개하는 소스 코드는 아래에 링크에서 확인할 수 있습니다.

- GitHub: [https://github.com/dev-yakuza/study-flutter/tree/main/dart](https://github.com/dev-yakuza/study-flutter/tree/main/dart){:rel="nofollow noreferrer" target="_blank"}

## 산술 연산자

Dart에서 숫자를 연산할 때, 기본적으로 다른 프로그래밍 언어에서 사용되는 연산자를 모두 사용할 수 있습니다.

```dart
void main() {
  double num1 = 4;

  print(num1 + 2);
  print(num1 - 2);
  print(num1 * 2);
  print(num1 / 2);
  print(num1 % 3);
  print(num1++);
  print(num1--);
  print(++num1);
  print(--num1);
  print(num1 += 1);
  print(num1 -= 1);
  print(num1 *= 1);
  print(num1 /= 2);
  print(num1 %= 3);
}
```

{% include in-feed-ads.html %}

## 비교 연산자

Dart에서는 다른 언어에서 사용하는 비교 연산자를 사용할 수 있습니다.

```dart
void main() {
  int num1 = 3;
  int num2 = 5;

  print(num1 > num2);
  print(num1 < num2);
  print(num1 >= num2);
  print(num1 <= num2);
  print(num1 == num2);
  print(num1 != num2);
}
```

## 타입 비교 연산자

Dart에서는 타입을 비교할 수 있는 연산자가 있습니다.

```dart
void main() {
  int num = 3;

  print(num is int);
  print(num is String);
  print(num is List);
}
```

다음과 같이 타입이 같지 않음을 확인할 수 있습니다.

```dart
void main() {
  int num = 3;

  print(num is! int);
  print(num is! String);
  print(num is! List);
}
```

{% include in-feed-ads.html %}

## 논리 연산자

Dart에서도 다른 언어에서와 같이 논리 연산자를 사용할 수 있습니다.

```dart
void main() {
  print(true && true);
  print(true && false);
  print(false && true);
  print(false && false);
  print(true || true);
  print(true || false);
  print(false || true);
  print(false || false);
}
```

## Null-aware operator

`??=` 연산자는 변수의 값이 `null`인 경우에만 값을 할당합니다.

```dart
void main() {
  var name = null;
  name ??= 'Yakuza';
  print(name);

  name ??= 'Dev';
  print(name);
}
```

`name` 변수에 초기값이 `null`이므로 첫번째 `??=`가 동작하여 `Yakuza`라는 값이 `name`에 할당되지만, 두번째 `??=` 연산자는 이미 값이 할당된 변수이므로 재할당하지 않습니다.

## 완료

이것으로 Flutter로 앱을 개발하기 위해 Dart에서 사용되는 기본적인 연산자에 대해서 살펴보았습니다. 기본적으로 다른 프로그래밍 언어에서 사용할 수 있는 연산자들을 그대로 사용할 수 있는 것을 알 수 있었습니다.
