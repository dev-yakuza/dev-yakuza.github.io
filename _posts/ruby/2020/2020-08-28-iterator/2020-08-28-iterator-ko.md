---
layout: 'post'
permalink: '/ruby/iterator/'
paginate_path: '/ruby/:num/iterator/'
lang: 'ko'
categories: 'ruby'
comments: true

title: Ruby의 이터레이터
description: Ruby에서 배열을 좀 더 편하게 다루기 위해 이터레이터를 사용하는 방법에 대해서 알아봅시다.
image: '/assets/images/category/ruby/2020/iterator/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [이터레이터](#이터레이터)
  - [each 메서드](#each-메서드)
  - [times 메서드](#times-메서드)
  - [loop 메서드](#loop-메서드)
- [이터레이터의 활용](#이터레이터의-활용)
  - [each_with_index 메서드](#each_with_index-메서드)
  - [해시](#해시)
  - [파일](#파일)
- [이터레이터 정의하기](#이터레이터-정의하기)
- [완료](#완료)autoauto

</div>

## 개요

이번 블로그에서는 Ruby에서 이터레이터란 무엇이며, 배열을 좀 더 쉽게 다루기 위해 이터레이터를 사용하는 방법에 대해서 설명합니다.

## 이터레이터

이터레이터(iterator)란 배열과 같이 여러 개의 요소가 있는 오브젝트의 각 요소를 반복 처리할 때 사용하는 메서드를 말합니다. 이번 블로그에서는 자주 사용되는 이터레이터를 소개합니다.

### each 메서드

배열의 각 요소가 `|변수|`에 대입되어 반복을 실행합니다.

```ruby
배열.each { |변수|
  반복하려는 처리
}
```

다음과 같이 `each`를 사용할 수 있습니다.

```ruby
fruits = ['apple', 'banana', 'orange']
fruits.each {|fruit|
  puts fruit
}
```

### times 메서드

반복할 횟수가 정해져 있는 경우, `times` 메서드를 사용합니다.

```ruby
4.times {
  puts 'Hello world'
}
```

Ruby에서는 수치도 오브젝트임으로 위와 같이 `times` 메서드를 사용할 수 있습니다.

### loop 메서드

loop 메서드는 종료 없이 반복을 수행합니다.

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

위에 예제와 같이 `break`를 사용하여 `loop` 메서드를 종료시키지 않는다면, 무한 루프에 빠지므로 주의해야 합니다.

{% include in-feed-ads.html %}

## 이터레이터의 활용

배열을 처리할 때 이터레이터를 사용하면 좀 더 편리하게 사용할 수 있습니다.

### each_with_index 메서드

배열의 요소 이외에도 인덱스가 필요한 경우, `each_with_index` 메서드를 활용할 수 있습니다.

```ruby
fruits = ['apple', 'banana', 'orange']
fruits.each_with_index {|fruit, i|
  puts "#{i}: #{fruit}"
}
```

### 해시

배열과 마찬가지로 해시에서도 이터레이터를 사용할 수 있습니다.

```ruby
fruits = {:Apple => 'apple', :Banana => 'banana', :Orange => 'orange'}
fruits.each {|key, value|
  puts "#{key}: #{value}"
}
```

### 파일

File 클래스에서도 이터레이터를 사용할 수 있습니다. 파일에서 이터레이터를 사용하면 텍스트 파일의 한 줄을 요소로 가져올 수 있습니다.

```ruby
file = File.open("test.txt")
file.each {|line|
  puts line
}
file.close
```

## 이터레이터 정의하기

메서드를 정의할 때, `yield`를 사용하면 이터레이터를 정의할 수 있습니다.

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

## 완료

이것으로 Ruby에서 이터레이터가 무엇이며, 이터레이터를 어떻게 사용하는지에 대해서 살펴보았습니다. 또한 필요하다면, 이터레이터를 만들 수 있음도 확인하였습니다. 이제 배열, 해시등과 함께 반복적인 처리를 할 때, 이터레이터를 활용하여 좀 더 효율적으로 작업해 보시기 바랍니다.
