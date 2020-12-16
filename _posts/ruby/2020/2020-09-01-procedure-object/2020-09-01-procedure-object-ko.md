---
layout: 'post'
permalink: '/ruby/procedure-object/'
paginate_path: '/ruby/:num/procedure-object/'
lang: 'ko'
categories: 'ruby'
comments: true

title: Ruby의 절차 오브젝트
description: Ruby의 절차 오브젝트란 무엇이며, 어떻게 사용하는지에 대해서 알아봅니다.
image: '/assets/images/category/ruby/2020/procedure-object/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [절차 오브젝트](#절차-오브젝트)
- [proc와 lambda](#proc와-lambda)
- [eval](#eval)
- [완료](#완료)

</div>

## 개요

이번 블로그에서는 Ruby에서 절차 오브젝트란 무엇이며, 절차 오브젝트를 사용하는 방법에 대해서 설명합니다.

## 절차 오브젝트

절차 오브젝트(Procedure Object)란 프로그램 절차(처리)를 데이터로 저장하는 오브젝트를 의미하며, proc와 lambda 등이 이에 해당합니다.

절차 오브젝트는 기본적으로 Proc 클래스를 사용하여 저장하고 저장된 절차는 call 메서드를 사용하여 호출합니다.

```ruby
p = Proc.new {
  puts 'This is a procedure object'
}

p.call
# This is a procedure object
```

절차 오브젝트도 다른 오브젝트와 똑같이 저장하거나, 매개변수를 받아 전달할 수 있습니다.

```ruby
p = Proc.new { |count|
  puts "Counts: #{count}"
}

p.call(2)
# Counts: 2
```

{% include in-feed-ads.html %}

## proc와 lambda

porc과 lambda는 Proc.new와 같은 기능을 합니다.

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

하지만 lambda는 proc와 Proc.new보다 조금 더 엄격합니다.

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

위와 같이 Proc.new와 proc은 두 개의 파라메터중 하나만 전달 받아도 문제가 되지 않지만, lambda는 다음과 같이 에러가 발생합니다.

```ruby
p = lambda { |a, b|
  puts "Number: #{a}"
}

p.call(2)
# index.rb:1:in `block in <main>': wrong number of arguments (given 1, expected 2) (ArgumentError)
```

{% include in-feed-ads.html %}

## eval

Ruby에서는 백쿼트(\`)로 묶은 문자열은 명령 프롬프트에서 실행되어 결과값을 표시합니다.

```ruby
puts `date`
# Wed Sep  2 12:58:05 JST 2020
```

eval은 주어진 문자열을 Ruby 프로그램으로 해석하고 실행합니다.

```ruby
a = 5
b = 10
eval ("puts #{a + b}")
# 15
```

만약 여러개의 절차가 포함된 문자열을 전달 받으면, 마지막 절차만 실행됩니다.

```ruby
a = "1..10; 1..4;"
eval(a).each {|v| puts v}
# 1
# 2
# 3
# 4
```

## 완료

이것으로 Ruby의 절차 오브젝트가 무엇인지, 어떻게 사용하는지에 대해서 살펴보았습니다. 실전에서는 자주 사용되지 않지만, 알아두면 유용하게 사용할 수 있습니다.
