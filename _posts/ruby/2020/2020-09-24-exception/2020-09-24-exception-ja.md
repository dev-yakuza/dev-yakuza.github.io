---
layout: 'post'
permalink: '/ruby/exception/'
paginate_path: '/ruby/:num/exception/'
lang: 'ja'
categories: 'ruby'
comments: true

title: Rubyで例外処理
description: Rubyで予想できなかったエラーが発生した場合、プログラムが終了されないようにするため例外処理をする方法について説明します。
image: '/assets/images/category/ruby/2020/exception/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [例外処理](#例外処理)
- [デバッグ変数](#デバッグ変数)
- [例題](#例題)
- [完了](#完了)

</div>

## 概要

プログラムを作成する時、私たちが予想できないエラーが発生する時もあります。このようにエラーが発生したら、プログラムは意図せず終了されます。例外処理はこのように私たちが予想できないエラーが発生する時、プログラムが終了されないようにしてくれます。

このブログポストではRubyで例外処理をする方法について説明します。

## 例外処理

普通の他の言語では`try-catch`文を使って例外処理をします。しかし、Rubyでは例外処理をするためには`begin-rescue-end`文を使います。

```ruby
begin
  # 例外が発生する可能性がある部分
rescue
  # 例外処理
else
  # 例外が発生しない場合の処理
ensure
  # 最後に実行される処理
end
```

上のように`begin`と`rescue`の間には私たちが予想できないエラーが発生する可能性がある部分を作成します。ここで例外が発生する場合、`rescue`と`else`の間が実行されます。最後には`ensure`と`end`の間が実行されます。

もし、`begin`と`rescue`の間でエラーが発生しない場合、`else`と`ensure`の間が実行されって`ensure`と`end`の間の部分が実行されます。

## デバッグ変数

Rubyではエラーが発生して例外処理の部分が実行されると、次のような変数が自動的に割り当てられます。

- `$!₩`: 最後に起きた例外と関連する情報
- `$@`: 最後に起きた例外の位置と関連する情報

{% include in-feed-ads.html %}

## 例題

次のように例外処理を使うことができます。

```ruby
puts "[Search a file with file name]"
begin
  print "file name: "
  file_name = gets.chop
  puts File.ftype(file_name)
rescue
  puts "Error!!"
  puts "#{$@}"
  puts "#{$!}"
end
```

上の例題を少し詳しく見てみます。

```ruby
file_name = gets.chop
```

検索したいファイルの名前を`gets`メソッドを使ってユーザーから入力してもらいます。入力した文字列を`chop`を使って改行文字(`\n`)を消します。

```ruby
puts File.ftype(file_name)
```

ユーザーから入力してもらったファイルの名前を`File`の`ftype`メソッドを使ってファイルタイプを取ってきます。

```bash
[Search a file with file name]
file name: example.txt
file
```

実際、存在するファイルを入力したら上のようにファイルの種類を返します。しかし、存在してないファイルの名前を入力するとエラーが発生します。

```ruby
rescue
  puts "Error!!"
  puts "#{$@}"
  puts "#{$!}"
end
```

エラーが発生したら、`rescue`と`end`の間が実行されて画面には`Error!!`と言う文字が表示されて、発生した位置に関する情報(`$@`)とエラーに関する情報(`$!`)が表示されます。

```bash
Error!!
No such file or directory @ rb_file_s_ftype - test
["./index.rb:5:in `ftype'", "./index.rb:5:in `<main>'"]
```

## 完了

これでRubyで例外処理をする方法について調べて見ました。今からは`begin-rescue`を使ってプログラムが急に終了されることを防止して見てください。
