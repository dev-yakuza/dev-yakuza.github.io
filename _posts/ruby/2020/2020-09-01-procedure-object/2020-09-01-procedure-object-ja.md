---
layout: 'post'
permalink: '/ruby/procedure-object/'
paginate_path: '/ruby/:num/procedure-object/'
lang: 'ja'
categories: 'ruby'
comments: true

title: RubyのProcオブジェクト
description: RubyのProcオブジェクトとは何か、どう使うかについて説明します。
image: '/assets/images/category/ruby/2020/procedure-object/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [Procオブジェクト](#procオブジェクト)
- [procとlambda](#procとlambda)
- [eval](#eval)
- [完了](#完了)

</div>

## 概要

このブログではRubyのProcオブジェクトとは何か、Procオブジェクトを使う方法について説明します。

## Procオブジェクト

Procオブジェクト(Procedure Object)とはプログラムの手順(Procedure)をデータで保存するオブジェクトを意味し、procとlambdaなどがこれに当該します。

Procオブジェクトは基本的Procクラスを使って保存して、保存した手順はcallメソッドを使って呼び出します。

```ruby
p = Proc.new {
  puts 'This is a procedure object'
}

p.call
# This is a procedure object
```

Procオブジェクトも他のオブジェクトと同じように保存したり、パラメーターで渡すことができます。

```ruby
p = Proc.new { |count|
  puts "Counts: #{count}"
}

p.call(2)
# Counts: 2
```

{% include in-feed-ads.html %}

## procとlambda

porcとlambdaはProc.newと同じ機能をします。

- proc

    ```ruby
    p = proc { |count|
      puts "Counts: #{count}"
    }

    p.call(2)
    # Counts: 2
    ```

- lambda

    ```ruby
    p = lambda { |count|
      puts "Counts: #{count}"
    }

    p.call(2)
    # Counts: 2
    ```

しかし、lambdaはprocとProc.newより少しストリクトします。

- Proc.new

    ```ruby
    p = Proc.new { |a, b|
      puts "Number: #{a}"
    }

    p.call(2)
    # Number: 2
    ```

- proc

    ```ruby
    p = proc { |a, b|
      puts "Number: #{a}"
    }

    p.call(2)
    # Number: 2
    ```

上のようにProc.newとprocは2つのパラメーター中で1つしかもらいましたが、問題にならないですが、lambdaは次のようにエラーが発生します。

```ruby
p = lambda { |a, b|
  puts "Number: #{a}"
}

p.call(2)
# index.rb:1:in `block in <main>': wrong number of arguments (given 1, expected 2) (ArgumentError)
```

{% include in-feed-ads.html %}

## eval

Rubyではバッククォート(\`)で囲まれた文字列はコマンドプロンプトで実行すると結果の値を表示します。

```ruby
puts `date`
# Wed Sep  2 12:58:05 JST 2020
```

evalは与えれた文字列をRubyのプログラムとして解析して実行します。

```ruby
a = 5
b = 10
eval ("puts #{a + b}")
# 15
```

もし、複数の手順が含まれている文字列を渡されると、最後の手順だけ実行されます。

```ruby
a = "1..10; 1..4;"
eval(a).each {|v| puts v}
# 1
# 2
# 3
# 4
```

## 完了

これでRubyのProcオブジェクトが何か、どう使うか見てみました。実際はよく使われないですが、知っておくと便利に使うことができます。
