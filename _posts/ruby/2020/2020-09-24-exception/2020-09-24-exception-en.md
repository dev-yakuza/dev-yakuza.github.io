---
layout: 'post'
permalink: '/ruby/exception/'
paginate_path: '/ruby/:num/exception/'
lang: 'en'
categories: 'ruby'
comments: true

title: Exception handling in Ruby
description: Let's see how to handle exceptions to prevent the program from terminating, when an unexpected error occurs in Ruby.
image: '/assets/images/category/ruby/2020/exception/background.jpg'
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [Exception handling](#exception-handling)
- [Debugging variables](#debugging-variables)
- [Example](#example)
- [Completed](#completed)

</div>

## Outline

When we develop the programs, sometimes we get unexpected errors. When these exceptions occur, the programs are terminated unintentionally. The exception handling is to prevent the programs from terminating when we get errors like this situation.

Let's see how to handle the exceptions in Ruby.

## Exception handling

Other program languages normally use the `try-catch` statement. However, In Ruby, we use the `begin-rescue-end` statement to handle exceptions.

```ruby
begin
  # Where an exception might occur
rescue
  # Handling when exception occurs
else
  # Handling when no exception occurs
ensure
  # Last processing to be executed
end
```

As above, between `begin` and `rescue`, we write the code where unexpected errors may occur. If the errors occurs in here, the code between `rescue` and `else` is executed and lastly the code between `ensure` and `end is executed.

If the error doesn't occur between `begin` and `rescue`, the code between `else` and `ensure` is executed and lastly the code between `ensure` and `end` is executed.

## Debugging variables

When the error occurs and the exception handling is executed in Ruby, the following variables are automatically assigned.

- `$!₩`: Information of the last raised exception 마지막으로 일어난 예외와 관련된 정보
- `$@`: Location information of the last raised exception

{% include in-feed-ads.html %}

## Example

You can use the exception handling like below.

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

Let's see the source code carefully.

```ruby
file_name = gets.chop
```

The file name to be searched is received from the user through the `gets` method and use `chop` to remove newline characters(`\n`) from the input string.

```ruby
puts File.ftype(file_name)
```

Using `ftype` method of `File` gets the file type from the input string.

```bash
[Search a file with file name]
file name: example.txt
file
```

If the file of the file name exists, the file type will be shown like above. If the file doesn't exist, an error will occur.

```ruby
rescue
  puts "Error!!"
  puts "#{$@}"
  puts "#{$!}"
end
```

If the error occurs, the code between `rescue` and `end` is executed and the `Error!!` string will be shown on the screen, and the location information of the error(`$@`) and the error information(`$!`) will be shown, too.

```bash
Error!!
No such file or directory @ rb_file_s_ftype - test
["./index.rb:5:in `ftype'", "./index.rb:5:in `<main>'"]
```

## Completed

We've seen how to handle the exception in Ruby. Now, you can use `begin-rescue` to prevent the program from terminating!
