---
layout: 'post'
permalink: '/flutter/dart/ceil-floor-round/'
paginate_path: '/flutter/:num/dart/ceil-floor-round/'
lang: 'ko'
categories: 'flutter'
comments: true

title: '[Dart] 올림, 버림, 반올림'
description: Flutter에서 소수점에 대해 올림, 버림, 반올림을 하는 방법에 대해서 알아봅시다.
image: '/assets/images/category/flutter/2021/dart/background.jpg'
published: false
---

<div id="contents_list" markdown="1">

## 목차

</div>

## 개요

Flutter에서 소수점이 있는 숫자를 사용하다보면, 해당 숫자에 대한, 올림, 버림 또는 반올림을 해야할 때가 있습니다. 이번 블로그 포스트에서는 Flutter에서 소수점 이하를 올리거나, 버리거나 반올림 하는 방법에 대해서 알아봅니다.

## 올림

Flutter에서 소수점 이하를 올리기 위해서는 `ceil`이라는 함수를 사용합니다. 다음과 같이 `ceil`을 사용하면 소수점 이하를 올릴 수 있습니다.

```dart
var targetNum = 3.514;
print(targetNum.ceil());
// 4
```

## 버림

Flutter에서 소수점 이하를 버리기 위해서는 `floor`라는 함수를 사용합니다. 다음과 같이 `floor`를 사용하면 소수점 이하를 버릴 수 있습니다.

```dart
var targetNum = 3.514;
print(targetNum.floor());
// 3
```

## 반올림

Flutter에서 소수점 이하를 반올림하기 위해서는 `round`라는 함수를 사용합니다. 다음과 같이 `round`를 사용하면 소수점 이하를 반올림할 수 있습니다.

```dart
var targetNum = 3.514;
print(targetNum.round());
// 4
targetNum = 3.154;
print(targetNum.round());
// 3
```

## 소수점 길이 고정

Flutter에서 소수점 길이를 고정하기 위해서는 `toStringAsFixed`라는 함수를 사용합니다. 다음과 같이 `toStringAsFixed`를 사용하면 소수점 길이를 고정할 수 있습니다.

```dart
var targetNum = 3.125;
print(targetNum.toStringAsFixed(2));
// 3.13
targetNum = 3.121;
print(targetNum.toStringAsFixed(2));
// 3.12
```

`toStringAsFixed` 함수는 소수점의 길이를 고정하여 문자열을 반환합니다. 그러므로 반환된 결과를 숫자로 사용하기 위해서는 double 타입으로 형변환을 해야합니다.

```dart
var targetNum = 3.125;
print(double.parse(targetNum.toStringAsFixed(2)));
// 3.13
targetNum = 3.121;
print(double.parse(targetNum.toStringAsFixed(2)));
// 3.12
```

## 완료

이것으로 Flutter에서 소수점 이하를 올리거나 버리거나 또는 반올림하는 방법에 대해서 알아보았습니다. 또한 소수점 길이를 고정하는 방법에 대해서도 알아보았습니다. 소수점의 길이를 고정할 때에는, 문자열이 반환된다는 점을 주의해서 사용하시기 바랍니다.
