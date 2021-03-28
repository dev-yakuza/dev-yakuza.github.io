---
layout: 'post'
permalink: '/flutter/dart/statement/'
paginate_path: '/flutter/:num/dart/statement/'
lang: 'en'
categories: 'flutter'
comments: true

title: '[Flutter] Statement in Dart'
description: Let's see how to use Dart for developing an app with Flutter. In this blog post, I will introduce how to use the Statement like if/else, for/while, etc in Dart.
image: '/assets/images/category/flutter/2021/dart/background.jpg'
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [if statement](#if-statement)
- [switch statement](#switch-statement)
- [for statement](#for-statement)
- [while statement](#while-statement)
- [Completed](#completed)

</div>

## Blog series

This blog post is a series. You can see the other posts on the link below.

- [[MacOS] Flutter installation]({{site.url}}/{{page.categories}}/installation/){:target="_blank"}
- [[Flutter] Variable in Dart]({{site.url}}/{{page.categories}}/dart/variable/){:target="_blank"}
- [[Flutter] Operator in Dart]({{site.url}}/{{page.categories}}/dart/operator/){:target="_blank"}
- [Flutter] Statement in Dart
- [[Flutter] Function in Dart]({{site.url}}/{{page.categories}}/dart/function/){:target="_blank"}
- [[Flutter] Class in Dart]({{site.url}}/{{page.categories}}/dart/class/){:target="_blank"}

## Outline

In this blog post, you can see how to use Statement like `if/else` and `for/while` in Dart.

## if statement

You can use `if` statement like other programming languages like below.

```dart
void main() {
  int num = 19;

  if (num % 2 == 0) {
    print('2');
  } else if (num % 3 == 0) {
    print('3');
  } else {
    print('No!');
  }
}
```

## switch statement

You can use `switch` statement in Dart like below.

```dart
void main() {
  int num = 19;

  switch (num % 2) {
    case 0:
      print('2');
      break;
    case 1:
      print('3');
      break;
    default:
      print('No!');
      break;
  }
}
```

{% include in-feed-ads.html %}

## for statement

You can use `for` statement in Dart like below.

```dart
void main() {
  for (int i = 0; i < 10; i++) {
    print(i);
  }

  List<int> numbers = [1, 4, 5, 10];
  int total = 0;
  for (int i = 0; i < numbers.length; i++) {
    total += numbers[i];
  }
  print(total);

  total = 0;
  for (int number in numbers) {
    total += number;
  }
  print(total);

  for (int i = 0; i < 10; i++) {
    print(i);
    if (i == 5) {
      break;
    }
  }
  for (int i = 0; i < 10; i++) {
    if (i == 5) {
      continue;
    }
    print(i);
  }
}
```

## while statement

You can use `while` statement in Dart like below.

```dart
void main() {
  int i = 0;
  while (i < 10) {
    print(i);
    i++;
  }

  i = 0;
  do {
    print(i);
    i++;
  } while (i < 10);

  i = 0;
  while (true) {
    print(i);
    i++;
    if (i == 5) {
      break;
    }
  }

  i = 0;
  while (i < 10) {
    if (i == 5) {
      continue;
    }
    print(i);
    i++;
  }
}
```

## Completed

We've seen how to use Statement in Dart for developing an app with Flutter. Now, we know that we can use almost statement of the other programming languages in Dart!