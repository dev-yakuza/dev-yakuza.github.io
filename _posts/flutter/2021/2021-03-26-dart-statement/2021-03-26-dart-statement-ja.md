---
layout: 'post'
permalink: '/flutter/dart/statement/'
paginate_path: '/flutter/:num/dart/statement/'
lang: 'ja'
categories: 'flutter'
comments: true

title: '[Flutter] DartのStatement'
description: Flutterでアプリを開発するためFlutterの開発言語であるDartについて説明します。今回のブログポストではDartでif/else、for/whileなどStatementを使う方法について説明します。
image: '/assets/images/category/flutter/2021/dart/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [if文](#if文)
- [switch文](#switch文)
- [for文](#for文)
- [while文](#while文)
- [完了](#完了)

</div>

## ブログシリーズ

このブログはシリーズで作成しております。下記のリンクを参考して他のブログポストも確認してみてください。

- [[MacOS] Flutterのインストール]({{site.url}}/{{page.categories}}/installation/){:target="_blank"}
- [[Flutter] Dartの変数]({{site.url}}/{{page.categories}}/dart/variable/){:target="_blank"}
- [[Flutter] Dartの演算子]({{site.url}}/{{page.categories}}/dart/operator/){:target="_blank"}
- [Flutter] DartのStatement
- [[Flutter] Dartの関数]({{site.url}}/{{page.categories}}/dart/function/){:target="_blank"}
- [[Flutter] Dartのクラス]({{site.url}}/{{page.categories}}/dart/class/){:target="_blank"}

## 概要

今回のブログポストではDartで`if/else`、`for/while`などStatementを使う方法について説明します。

## if文

Dartでも他のプログラミング言語と同じように`if`文を使うことができます。

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

## switch文

Dartでは`switch`文を使うことができます。

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

## for文

Dartでは`for`文を使うことができます。

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

## while文

Dartでは`while`文を使えます。

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

## 完了

これでFlutterでアプリを開発するためDartで使える基本的なStatementについてみてみました。基本的他のプログラミング言語で使えるStatementをそのまま使えることが分かりました。
