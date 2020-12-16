---
layout: 'post'
permalink: '/ruby/begin-end-block/'
paginate_path: '/ruby/:num/begin-end-block/'
lang: 'ja'
categories: 'ruby'
comments: true

title: RubyのBEGIN, END
description: RubyのBEGIN, ENDブロックについて説明します。
image: '/assets/images/category/ruby/2020/begin-end-block/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [BEGINブロック](#beginブロック)
- [ENDブロック](#endブロック)
- [完了](#完了)

</div>

## 概要

Rubyの`BEGIN`と`END`について説明します。BEGINブロックはプログラムを開始する前実行する物を、ENDブロックはプログラムが終了する直前に実行する物を定義することができます。

## BEGINブロック

BEGINブロックで定義したものは他の物より先に実行されます。

```ruby
puts "Hello"
BEGIN { puts "World" }
# World
# Hello
```

複数のBEGINブロックを持ってる場合、宣言した順で実行されます。

```ruby
puts "Hello"
BEGIN { puts "World" }
BEGIN { puts "BEGIN" }
# World
# BEGIN
# Hello
```

BEGINブロックはローカル変数の範囲を持ってるので、他のローカル変数と参照することができません。

```ruby
BEGIN {
  $a = 0
  b = 0
}
puts $a # Global Variable
puts b # Local Variable

# 0
# undefined local variable or method 'b' for main:Object (NameError)
```

## ENDブロック

ENDブロックで定義した物は全ての物が実行された後、実行されます。

```ruby
END { puts 5 }
puts 1
# 1
# 5
```

ENDブロックが複数ある場合は、宣言の逆順で実行されます。

```ruby
END { puts 5 }
END { puts 3 }
puts 1
# 1
# 3
# 5
```

ENDブロックはBEGINとは違って、変数の範囲を共有します。

```ruby
i = 1
END { puts i }
# 1
```

## 完了

Rubyで良く使われないものですが、ユニークな文法なので、覚えとくと良いかと思います。
