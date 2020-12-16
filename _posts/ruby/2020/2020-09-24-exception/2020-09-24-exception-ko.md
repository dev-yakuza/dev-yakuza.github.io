---
layout: 'post'
permalink: '/ruby/exception/'
paginate_path: '/ruby/:num/exception/'
lang: 'ko'
categories: 'ruby'
comments: true

title: Ruby에서 예외 처리
description: Ruby에서 예상치 못한 에러가 발생하였을 때, 프로그램이 종료되지 않게 하기 위해 예외 처리를 하는 방법에 대해서 알아봅시다.
image: '/assets/images/category/ruby/2020/exception/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [예외 처리](#예외-처리)
- [디버깅 변수](#디버깅-변수)
- [예제](#예제)
- [완료](#완료)

</div>

## 개요

프로그램을 작성하다보면, 우리가 예성하지 못한 에러가 발생하기도 합니다. 이런 에러가 발생을 하면, 프로그램이 의도치 않게 종료됩니다. 예외 처리는 이렇게 우리가 예상치 못한 에러가 발생하였을 때, 프로그램이 종료되지 않게 해 줍니다.

그럼 Ruby에서 예외 처리를 하는 방법에 대해서 살펴봅시다.

## 예외 처리

보통 다른 언어에서는 `try-catch` 구문을 사용하여 예외 처리를 합니다. 하지만 Ruby에서 예외 처리를 하기 위해서는 `begin-rescue-end` 구문을 사용합니다.

```ruby
begin
  # 예외가 발생할 만한 부분
rescue
  # 예외 처리
else
  # 예외가 발생하지 않은 경우의 처리
ensure
  # 마지막으로 실행할 처리
end
```

위와 같이 `begin`과 `rescue` 사이에는 우리가 예상치 못한 에러가 발생할 만한 부분을 작성합니다. 이곳에서 예외가 발생하면 `rescue`와 `else` 사이에 구문이 실행되고, 마지막으로 `ensure`와 `end` 구문이 실행됩니다.

만약 `begin`과 `rescue`사이에서 에러가 발생하지 않는 다면, `else`와 `ensure` 사이에 구문과 `ensure`와 `end`사이에 구문이 실행됩니다.

## 디버깅 변수

Ruby에서는 에러가 발생하여 예외 처리 부분이 실행되면, 다음과 같은 변수가 자동 할당됩니다.

- `$!₩`: 마지막으로 일어난 예외와 관련된 정보
- `$@`: 마지막으로 일어난 예외의 위치와 관련된 정보

{% include in-feed-ads.html %}

## 예제

다음과 같이 예외 처리를 사용할 수 있습니다.

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

위에 예제를 조금 자세히 살펴봅시다.

```ruby
file_name = gets.chop
```

검색하고자 하는 파일 이름을 `gets` 메서드를 통해 사용자로부터 입력받습니다. 입력받은 문자열을 `chop`을 사용하여 개행 문자(`\n`)를 제거합니다.

```ruby
puts File.ftype(file_name)
```

사용자로 부터 입력 받은 파일 이름을 `File`의 `ftype` 메서드를 통해 파일 타입을 가져옵니다.

```bash
[Search a file with file name]
file name: example.txt
file
```

실제로 존재하는 파일을 입력한다면 위와 같이 파일의 종류를 반환합니다. 하지만, 존재하지 않는 파일의 이름을 입력한다면 에러가 발생합니다.

```ruby
rescue
  puts "Error!!"
  puts "#{$@}"
  puts "#{$!}"
end
```

에러가 발생한다면, `rescue`와 `end` 사이에 구문이 실행되며 화면에는 `Error!!`라는 문자가 표시되며, 발생한 위치에 대한 정보(`$@`)와 에러에 대한 정보(`$!`)가 표시됩니다.

```bash
Error!!
No such file or directory @ rb_file_s_ftype - test
["./index.rb:5:in `ftype'", "./index.rb:5:in `<main>'"]
```

## 완료

이것으로 Ruby에서 예외 처리를 사용하는 방법에 대해서 알아보았습니다. 이제 `begin-rescue`를 사용하여 프로그램이 의도치 않게 종료되는 것을 방지해 보시기 바랍니다.
