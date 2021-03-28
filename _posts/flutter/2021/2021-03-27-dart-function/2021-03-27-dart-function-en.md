---
layout: 'post'
permalink: '/flutter/dart/function/'
paginate_path: '/flutter/:num/dart/function/'
lang: 'en'
categories: 'flutter'
comments: true

title: '[Flutter] Function in Dart'
description: Let's see how to use Dart for developing an app with Flutter. In this blog post, I will introduce how to use Function in Dart.
image: '/assets/images/category/flutter/2021/dart/background.jpg'
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [Function](#function)
- [Optional parameter](#optional-parameter)
- [Named parameter](#named-parameter)
- [typedef](#typedef)
- [Complete](#complete)

</div>

## Blog series

This blog post is a series. You can see the other posts on the link below.

- [[MacOS] Flutter installation]({{site.url}}/{{page.categories}}/installation/){:target="_blank"}
- [[Flutter] Variable in Dart]({{site.url}}/{{page.categories}}/dart/variable/){:target="_blank"}
- [[Flutter] Operator in Dart]({{site.url}}/{{page.categories}}/dart/operator/){:target="_blank"}
- [[Flutter] Statement in Dart]({{site.url}}/{{page.categories}}/dart/statement/){:target="_blank"}
- [Flutter] Function in Dart
- [[Flutter] Class in Dart]({{site.url}}/{{page.categories}}/dart/class/){:target="_blank"}

## Outline

In this blog post, I will introduce how to use Function in Dart.

## Function

We can define the  `Function` and use it in Dart like below.

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

## Optional parameter

When you define the Function, you can set the `Optional parameter` and set the default value on it like below.

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

## Named parameter

When the Function has many parameters, we can't remember the older of the parameters. In this case, we can use `Named parameter`. If you use Named parameter, you can set the parameter more clearly when you call the Function.

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

You can pass the Function via the parameter in Dart. However, if you don't set the type of the parameter, you don't know what value is passed, and how to use it.

In this case, you can use `typedef`. You can define `typedef` and you can set it on the Function parameter.

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

## Complete

We've seen how to use Function in Dart to develop an app with Flutter. We can know there is no difference between Dart and other languages to define the Function and use it. Also, we've seen how to use `typedef` to define the type of the FUnction and set it for the parameter in the Function.
