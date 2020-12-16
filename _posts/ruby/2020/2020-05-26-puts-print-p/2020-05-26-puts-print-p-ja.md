---
layout: 'post'
permalink: '/ruby/puts-print-p/'
paginate_path: '/ruby/:num/puts-print-p/'
lang: 'ja'
categories: 'ruby'
comments: true

title: Rubyで文字列を出力する関数
description: Rubyで文字列を出力する間すであるputs、print、そしてp関数について説明します。
image: '/assets/images/category/ruby/2020/puts-print-p/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [目次](#目次)
- [概要](#概要)
- [puts 関数](#puts-関数)
- [print関数](#print関数)
- [p関数](#p関数)
- [完了](#完了)

</div>

## 概要

Rubyで文字列を出力する時使う関数は`puts`, `print`, そして`p`の関数があります。各関数がどう違うかについて説明します。

## puts 関数

Rubyで`puts`は文字列を出力するための基本関数になります。下記のように使えます。

```ruby
puts 'Hello World!'
# Hello World!
```

下記のように括弧も使えます。

```ruby
puts ('Hello World!')
# Hello World!
```

下記のように複数の文字列を出力することもできます。

```ruby
puts 'Hello', 'World!'
# Hello
# World!
```

putsは文字列を画面に出力した後、最後に改行します。

## print関数

Rubyで`print`関数は`puts`関数と同じように文字列を出力しますが、自動で改行をしません。

```ruby
print 'Hello World!'
# Hello World!
```

下記のように作成すると、違うことが確認できます。

```ruby
print 'Hello', ' World!'
# Hello World!
```

print関数を使って改行をしたい場合、改行文字(`\n`)を追加します。

```ruby
print "Hello\nWorld!"
# Hello
# World!
```

ここで注意する点は、改行文字(`\n`)みたいなEscape Sequenceはダブルクォーテーション(`"`)中で使わないとうまく表示されません。

## p関数

Rubyで`p`関数を使うと文字列自体を表示することができます。

```ruby
p '100'
# '100'
```

下記のように数字と文字列を区分する時、よく使えます。

```ruby
p '100'
p 100
# '100'
# 100
```

## 完了

Rubyで文字列を出力する関数について見てみました。予想より関数が多くてびっくりしました。普通は`puts`関数を主に使ってるので一旦`puts`だけ覚えても特に問題ないと思います。
