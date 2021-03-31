---
layout: 'post'
permalink: '/flutter/dart/operator/'
paginate_path: '/flutter/:num/dart/operator/'
lang: 'en'
categories: 'flutter'
comments: true

title: '[Flutter] Operator in Dart'
description: Let's see how to use Dart to develop the app with Flutter. In this blog post, I'll introduce how to use Operators in Dart.
image: '/assets/images/category/flutter/2021/dart/background.jpg'
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [Arithmetic operators](#arithmetic-operators)
- [Comparison operators](#comparison-operators)
- [Type comparison operators](#type-comparison-operators)
- [Logical operators](#logical-operators)
- [Null-aware operator](#null-aware-operator)
- [Completed](#completed)

</div>

## Blog series

This blog post is a series. You can see the other posts on the link below.

- [[MacOS] Flutter installation]({{site.url}}/{{page.categories}}/installation/){:target="_blank"}
- [[Flutter] Variable in Dart]({{site.url}}/{{page.categories}}/dart/variable/){:target="_blank"}
- [Flutter] Operator in Dart
- [[Flutter] Statement in Dart]({{site.url}}/{{page.categories}}/dart/statement/){:target="_blank"}
- [[Flutter] Function in Dart]({{site.url}}/{{page.categories}}/dart/function/){:target="_blank"}
- [[Flutter] Class in Dart]({{site.url}}/{{page.categories}}/dart/class/){:target="_blank"}

## Outline

Let's see what operators are in Dart and how to use them.

You can see the source code, that is introduced on this blog post, on the link below

- GitHub: [https://github.com/dev-yakuza/study-flutter/tree/main/dart](https://github.com/dev-yakuza/study-flutter/tree/main/dart){:rel="nofollow noreferrer" target="_blank"}

## Arithmetic operators

When you calculate the numbers, you can use the arithmetic operators like other languages.

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

## Comparison operators

You can use the Comparison operators in Dart like other langauges.

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

## Type comparison operators

You can compare the Type of the variable like below.

```dart
void main() {
  int num = 3;

  print(num is int);
  print(num is String);
  print(num is List);
}
```

You can check that the types are not the same as follows.

```dart
void main() {
  int num = 3;

  print(num is! int);
  print(num is! String);
  print(num is! List);
}
```

{% include in-feed-ads.html %}

## Logical operators

You can use the logical operators in Dart like other langauges.

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

You can use `??=` operator in Dart. This operator assigns the value only when the variable is `null`.

```dart
void main() {
  var name = null;
  name ??= 'Yakuza';
  print(name);

  name ??= 'Dev';
  print(name);
}
```

The `name` varialbe is not initialized, so it is assinged `null`. First `??=` operator can assign the value because the `name` is `null`, but second `??=` operator doesn't assign because the variable is not `null`.

## Completed

We've seen what operators are in Dart and how to use the operators. We've known that we can use the almost operators of the other languages in Dart.
