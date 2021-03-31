---
layout: 'post'
permalink: '/flutter/dart/statement/'
paginate_path: '/flutter/:num/dart/statement/'
lang: 'ko'
categories: 'flutter'
comments: true

title: '[Flutter] Dart에서 Statement'
description: Flutter로 앱을 개발하기 위해서 Flutter의 개발 언어인 Dart에 대해서 알아봅시다. 이번 블로그 포스트에서는 Dart에서 if/else, for/while등 Statement를 사용하는 방법에 대해서 알아봅니다.
image: '/assets/images/category/flutter/2021/dart/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [if문](#if문)
- [switch문](#switch문)
- [for 문](#for-문)
- [while 문](#while-문)
- [완료](#완료)

</div>

## 블로그 시리즈

이 블로그는 시리즈로 제작되었습니다. 다음 링크를 통해 다른 블로그 포스트도 확인해 보시기 바랍니다.

- [[MacOS] Flutter 설치]({{site.url}}/{{page.categories}}/installation/){:target="_blank"}
- [[Flutter] Dart에서 변수]({{site.url}}/{{page.categories}}/dart/variable/){:target="_blank"}
- [[Flutter] Dart에서 연산자]({{site.url}}/{{page.categories}}/dart/operator/){:target="_blank"}
- [Flutter] Dart에서 Statement
- [[Flutter] Dart에서 함수]({{site.url}}/{{page.categories}}/dart/function/){:target="_blank"}
- [[Flutter] Dart에서 클래스]({{site.url}}/{{page.categories}}/dart/class/){:target="_blank"}

## 개요

이번 블로그 포스트에서는 Dart에서 `if/else`, `for/while` 등 Statement를 사용하는 방법에 대해서 설명합니다.

이 블로그 포스트에서 소개하는 소스 코드는 아래에 링크에서 확인할 수 있습니다.

- GitHub: [https://github.com/dev-yakuza/study-flutter/tree/main/dart](https://github.com/dev-yakuza/study-flutter/tree/main/dart){:rel="nofollow noreferrer" target="_blank"}

## if문

Dart에서도 다른 프로그래밍 언어와 같이 `if`문을 사용할 수 있습니다.

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

## switch문

Dart에서 `switch`문을 사용할 수 있습니다.

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

## for 문

Dart에서 `for`문을 사용할 수 있습니다.

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

## while 문

Dart에서 `while`문을 사용할 수 있습니다.

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

## 완료

이것으로 Flutter로 앱을 개발하기 위해 Dart에서 사용되는 기본적인 Statement에 대해서 살펴보았습니다. 기본적으로 다른 프로그래밍 언어에서 사용할 수 있는 Statement들을 그대로 사용할 수 있는 것을 알 수 있었습니다.
