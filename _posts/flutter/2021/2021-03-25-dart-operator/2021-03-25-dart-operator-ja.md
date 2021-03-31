---
layout: 'post'
permalink: '/flutter/dart/operator/'
paginate_path: '/flutter/:num/dart/operator/'
lang: 'ja'
categories: 'flutter'
comments: true

title: '[Flutter] Dartの演算子'
description: Flutterでアプリを開発するためFlutterの開発言語であるDartについて説明します。今回のブログポストではDartの演算子について説明します。
image: '/assets/images/category/flutter/2021/dart/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [算術演算子](#算術演算子)
- [比較演算子](#比較演算子)
- [タイプ比較演算子](#タイプ比較演算子)
- [論理演算子](#論理演算子)
- [Null-aware operator](#null-aware-operator)
- [完了](#完了)

</div>

## ブログシリーズ

このブログはシリーズで作成しております。下記のリンクを参考して他のブログポストも確認してみてください。

- [[MacOS] Flutterのインストール]({{site.url}}/{{page.categories}}/installation/){:target="_blank"}
- [[Flutter] Dartの変数]({{site.url}}/{{page.categories}}/dart/variable/){:target="_blank"}
- [Flutter] Dartの演算子
- [[Flutter] DartのStatement]({{site.url}}/{{page.categories}}/dart/statement/){:target="_blank"}
- [[Flutter] Dartの関数]({{site.url}}/{{page.categories}}/dart/function/){:target="_blank"}
- [[Flutter] Dartのクラス]({{site.url}}/{{page.categories}}/dart/class/){:target="_blank"}

## 概要

このブログポストではDartで演算子を使う方法について説明します。

このブログポストで紹介するソースコードは下記のリンクで確認できます。

- GitHub: [https://github.com/dev-yakuza/study-flutter/tree/main/dart](https://github.com/dev-yakuza/study-flutter/tree/main/dart){:rel="nofollow noreferrer" target="_blank"}

## 算術演算子

Dartでは数字を計算する時、基本的他のプログラミング言語で使える演算子を全て使えます。

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

## 比較演算子

Dartでは他の言語で使える比較演算子を使えます。

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

## タイプ比較演算子

Dartでは変数のタイプを比較する演算子があります。

```dart
void main() {
  int num = 3;

  print(num is int);
  print(num is String);
  print(num is List);
}
```

次のようにタイプが一致しないことも確認できます。

```dart
void main() {
  int num = 3;

  print(num is! int);
  print(num is! String);
  print(num is! List);
}
```

{% include in-feed-ads.html %}

## 論理演算子

Dartでも他の言語と同じように論理演算子を使うことができます。

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
  print(!true);
  print(!false);
}
```

## Null-aware operator

`??=`演算子は変数の値が`null`の場合だけ、値を割り当てます。

```dart
void main() {
  var name = null;
  name ??= 'Yakuza';
  print(name);

  name ??= 'Dev';
  print(name);
}
```

`name`変数には初期値が割り当てないので`null`が入ってます。それで最初の`??=`で`Yakuza`と言う値が`name`に値が割り当てられますが、2番目の`??=`演算子を使う時には既に値が入ってるので再び割り当てることができません。

## 完了

これでFlutterでアプリを開発するためDartで使える基本演算子を確認してみました。基本的に他のプログラミング言語で使える演算子はそのまま使えることが分かりました。
