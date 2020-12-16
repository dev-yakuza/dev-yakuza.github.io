---
layout: 'post'
permalink: '/ruby/iterator/'
paginate_path: '/ruby/:num/iterator/'
lang: 'ja'
categories: 'ruby'
comments: true

title: Rubyのイテレータ
description: Rubyで配列をもっと簡単に使えるためイテレータの使い方を説明します。
image: '/assets/images/category/ruby/2020/iterator/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [イテレータ](#イテレータ)
  - [eachメソッド](#eachメソッド)
  - [timesメソッド](#timesメソッド)
  - [loopメソッド](#loopメソッド)
- [イテレータの活用](#イテレータの活用)
  - [each_with_indexメソッド](#each_with_indexメソッド)
  - [ハッシュ](#ハッシュ)
  - [ファイル](#ファイル)
- [イテレータを定義する](#イテレータを定義する)
- [完了](#完了)

</div>

## 概要

このブログではRubyでイテレータとは何か、配列をとっと簡単に使えるためイテレータを使う方法について説明します。

## イテレータ

イテレータ(iterator)とは配列ように複数の要素があるオブジェクトを反復処理する時使えるメソッドです。今回のブログではよく使えるイテレータを紹介します。

### eachメソッド

配列の各要素が`|変数|`へ入れてループを実行します。

```ruby
配列.each { |変数|
  反復処理
}
```

次のように`each`を使えます。

```ruby
fruits = ['apple', 'banana', 'orange']
fruits.each {|fruit|
  puts fruit
}
```

### timesメソッド

反復する回数が決めてある時は`times`メソッドを使います。

```ruby
4.times {
  puts 'Hello world'
}
```

Rubyでは数値もオブジェクトなので上のように`times`メソッドを使えます。

### loopメソッド

loopメソッドは終了なしで反復を実行します。

```ruby
i = 0
loop {
  i += 1
  puts 'Hello world'
  if i == 4
    break
  end
}
```

上の例ように`break`を使って`loop`メソッドを終了させない場合は、無限ループへ入るので注意する必要があります。

{% include in-feed-ads.html %}

## イテレータの活用

配列を処理する時イテレータを使うともっと便利に使えることができます。

### each_with_indexメソッド

配列の要素以外にIndexが必要な場合、`each_with_index`メソッドを活用することができます。

```ruby
fruits = ['apple', 'banana', 'orange']
fruits.each_with_index {|fruit, i|
  puts "#{i}: #{fruit}"
}
```

### ハッシュ

配列と同じようにハッシュにもイテレータを使うことができます。

```ruby
fruits = {:Apple => 'apple', :Banana => 'banana', :Orange => 'orange'}
fruits.each {|key, value|
  puts "#{key}: #{value}"
}
```

### ファイル

Fileクラスでもイテレータを使うことができます。ファイルでイテレータを使うとテキストファイルの一列を要素として取って来ることができます。

```ruby
file = File.open("test.txt")
file.each {|line|
  puts line
}
file.close
```

## イテレータを定義する

メソッドを定義する時、`yield`を使うとイテレータを定義することができます。

```ruby
def temp
  yield 10
  yield 'Hello'
end

temp {|value|
  puts value * 2
}
# 20
# HelloHello
```

## 完了

これでRubyのイテレータとは何か、イテレータをどう使うかに関して見てみました。また、必要な時、イテレータを作ることもできることを確認しました。今度、配列やハッシュなどと一緒に反復処理をする時、イテレータを活用してもっと効率的に作業をやってみてください。
