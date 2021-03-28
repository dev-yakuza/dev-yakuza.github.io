---
layout: 'post'
permalink: '/flutter/dart/function/'
paginate_path: '/flutter/:num/dart/function/'
lang: 'ja'
categories: 'flutter'
comments: true

title: '[Flutter] Dartの関数'
description: Flutterでアプリを開発するためFlutterの開発言語であるDartについて説明します。今回のブログポストではDartの関数について説明します。
image: '/assets/images/category/flutter/2021/dart/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [関数](#関数)
- [Optionalパラメーター](#optionalパラメーター)
- [Namedパラメーター](#namedパラメーター)
- [typedef](#typedef)
- [完了](#完了)

</div>

## ブログシリーズ

このブログはシリーズで作成しております。下記のリンクを参考して他のブログポストも確認してみてください。

- [[MacOS] Flutterのインストール]({{site.url}}/{{page.categories}}/installation/){:target="_blank"}
- [[Flutter] Dartの変数]({{site.url}}/{{page.categories}}/dart/variable/){:target="_blank"}
- [[Flutter] Dartの演算子]({{site.url}}/{{page.categories}}/dart/operator/){:target="_blank"}
- [[Flutter] DartのStatement]({{site.url}}/{{page.categories}}/dart/statement/){:target="_blank"}
- [Flutter] Dartの関数
- [[Flutter] Dartのクラス]({{site.url}}/{{page.categories}}/dart/class/){:target="_blank"}

## 概要

今回のブログポストではDartで関数を使う方法について説明します。

## 関数

Dartでは下記のように`関数`を宣言して使うことができます。

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

## Optionalパラメーター

次のように関数を宣言するとき、`Optionalパラメーター`を設定することができますし、Optionalパラメータの基本値を設定することができます。

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

## Namedパラメーター

関数のパラメーターが多くなると、パラメーターの順番を覚えて使うことが難しくなります。この時、使うことが`Namedパラメーター`です。Namedパラメーターを使うと、関数を呼び出す時、もっと明確パラメーターを設定することができます。

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

Dartでは関数をパラメーターで渡すことができます。しかし、渡された関数のタイプを指定しないと、どのパラメーターで渡されたか、渡された関数がどんな形か分かりづらいです。

この時使うことが`typedef`です。`typedef`は次のようにパラメーターで渡される関数のタイプを宣言して指定することができます。

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

## 完了

これでFlutterでアプリを開発するためDartで使える関数についてみてみました。基本的に他のプログラミング言語で宣言して使う関数と大きな違さはないことが分かります。また`typedef`を使って関数のタイプを宣言してパラメーターで指定する方法もみてみました。
