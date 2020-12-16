---
layout: 'post'
permalink: '/ruby/procedure-object/'
paginate_path: '/ruby/:num/procedure-object/'
lang: 'en'
categories: 'ruby'
comments: true

title: Procedure Object in Ruby
description: Let's see what the procedure object and how to use it in Ruby.
image: '/assets/images/category/ruby/2020/procedure-object/background.jpg'
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [Procedure Object](#procedure-object)
- [proc and lambda](#proc-and-lambda)
- [eval](#eval)
- [Completed](#completed)

</div>

## Outline

In this blog post, we'll see what the procedure object is and how to use the procedure object in Ruby.

## Procedure Object

Procedure Object means that the object includes program procedures as data, and you can use `proc` and `lambda` for it in Ruby.

Procedure Object is basically stored in the `Proc` class, and we can use the `call` method to call the procedures saved in the class.

```ruby
p = Proc.new {
  puts 'This is a procedure object'
}

p.call
# This is a procedure object
```

You can save the Procedure Object like other objects, and pass it via parameters.

```ruby
p = Proc.new { |count|
  puts "Counts: #{count}"
}

p.call(2)
# Counts: 2
```

{% include in-feed-ads.html %}

## proc and lambda

porc and lambda have the same features as Proc.new.

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

However, lambda is more strict than proc and Proc.new.

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

As above, Proc.new and proc don't matter if only one of the two parameters is passed, but the errors occur in lambda like below.

```ruby
p = lambda { |a, b|
  puts "Number: #{a}"
}

p.call(2)
# index.rb:1:in `block in <main>': wrong number of arguments (given 1, expected 2) (ArgumentError)
```

{% include in-feed-ads.html %}

## eval

In Ruby, if you execute the string enclosed in backquotes(\`) at the command prompt, the string will be executed and display the result.

```ruby
puts `date`
# Wed Sep  2 12:58:05 JST 2020
```

If you execute eval with string, Ruby will execute the string as a program.

```ruby
a = 5
b = 10
eval ("puts #{a + b}")
# 15
```

If the eval receives many procedures, the eval executes only the last one.

```ruby
a = "1..10; 1..4;"
eval(a).each {|v| puts v}
# 1
# 2
# 3
# 4
```

## Completed

We've seen what the Procedure Object is and how to use it. Actually, the Procedure Object is not used normally, but it's useful if you remember it.
