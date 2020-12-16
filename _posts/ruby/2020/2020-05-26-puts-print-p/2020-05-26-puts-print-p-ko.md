---
layout: 'post'
permalink: '/ruby/puts-print-p/'
paginate_path: '/ruby/:num/puts-print-p/'
lang: 'ko'
categories: 'ruby'
comments: true

title: Ruby에서 문자열 출력 함수
description: Ruby에서 문자열을 출력하는 함수인, puts, print, 그리고 p 함수에 대해서 알아봅시다.
image: '/assets/images/category/ruby/2020/puts-print-p/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

- [목차](#목차)
- [개요](#개요)
- [puts 함수](#puts-함수)
- [print 함수](#print-함수)
- [p 함수](#p-함수)
- [완료](#완료)

</div>

## 개요

Ruby에서 문자열을 출력하는 함수는 `puts`, `print`, 그리고 `p` 함수가 있습니다. 각각의 함수가 어떻게 다른지에 대해서 알아봅시다.

## puts 함수

Ruby에서 `puts`은 문자열을 출력하기 위한 기본 함수입니다. 아래와 같이 사용할 수 있습니다.

```ruby
puts 'Hello World!'
# Hello World!
```

아래와 같이 괄호를 사용할 수 도 있습니다.

```ruby
puts ('Hello World!')
# Hello World!
```

아래와 같이 여러 문자열을 출력할 수 있습니다.

```ruby
puts 'Hello', 'World!'
# Hello
# World!
```

puts는 문자열을 화면에 출력한 후, 마지막에 줄바꿈이 표시됩니다.

## print 함수

Ruby에서 `print` 함수는 `puts` 함수와 동일하게 문자열을 출력하지만, 자동으로 줄바꿈을 하지 않습니다.

```ruby
print 'Hello World!'
# Hello World!
```

아래와 같이 작성하면, 차이를 확인할 수 있습니다.

```ruby
print 'Hello', ' World!'
# Hello World!
```

print 함수를 사용하여 줄바꿈을 하고자 한다면, 줄바꿈 문자(`\n`)를 추가해 주어야 합니다.

```ruby
print "Hello\nWorld!"
# Hello
# World!
```

여기서 주의할 점은, 줄바꿈 문자(`\n`)와 같은 이스케이프 시퀀스는 큰따옴표(`"`)안에서 사용해야 제대로 표시됩니다.

## p 함수

Ruby에서 `p` 함수를 사용하면, 문자열을 자체를 표시할 수 있습니다.

```ruby
p '100'
# '100'
```

아래와 같이 수치와 문자열을 구별할 때, 사용하기 좋습니다.

```ruby
p '100'
p 100
# '100'
# 100
```

## 완료

Ruby에서 문자열 출력 함수에 대해서 알아보았습니다. 생각보다 많은 함수가 존재하네요. 보통은 `puts` 함수를 많이 사용함으로, 일단 `puts`만 기억해도 큰 문제없을거 같습니다.
