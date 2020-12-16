---
layout: 'post'
permalink: '/ruby/begin-end-block/'
paginate_path: '/ruby/:num/begin-end-block/'
lang: 'ko'
categories: 'ruby'
comments: true

title: Ruby에서 BEGIN, END
description: Ruby에서 BEGIN, END 블록에 관해서 알아봅시다.
image: '/assets/images/category/ruby/2020/begin-end-block/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [BEGIN 블록](#begin-블록)
- [END 블록](#end-블록)
- [완료](#완료)

</div>

## 개요

Ruby의 `BEGIN`과 `END`에 대해서 알아보려고 합니다. BEGIN 블록은 프로그램을 개시하기 전에 실행할 문장을, END 블록은 프로그램 종료 직전에 실행할 문장을 지정합니다.

## BEGIN 블록

BEGIN 블록으로 지정한 문장은 해당 파일의 다른 어떤 문장의 실행보다 먼저 실행됩니다

```ruby
puts "Hello"
BEGIN { puts "World" }
# World
# Hello
```

여러 개의 BEGIN을 가지고 있는 경우, 선언한 순서대로 실행됩니다.

```ruby
puts "Hello"
BEGIN { puts "World" }
BEGIN { puts "BEGIN" }
# World
# BEGIN
# Hello
```

BEGIN 블록은 로컬 변수 범위를 가지고 있으므로, 다른 로컬 변수와 값을 공유할 수 없습니다.

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

## END 블록

END 블록으로 지정한 문장은 모든 문장이 끝난 후 실행됩니다.

```ruby
END { puts 5 }
puts 1
# 1
# 5
```

END 블록이 여러개인 경우 선언의 역순으로 호출됩니다.

```ruby
END { puts 5 }
END { puts 3 }
puts 1
# 1
# 3
# 5
```

END 블록은 BEGIN 블록과 달리, 변수 범위를 공유합니다.

```ruby
i = 1
END { puts i }
# 1
```

## 완료

Ruby에서 크게 활용되지는 않지만, 독특한 문법이므로 기억해두면 좋을거 같습니다.
