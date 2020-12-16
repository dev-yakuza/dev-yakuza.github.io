---
layout: 'post'
permalink: '/ruby/puts-print-p/'
paginate_path: '/ruby/:num/puts-print-p/'
lang: 'en'
categories: 'ruby'
comments: true

title: String output function
description: Let's see how to use and what difference puts, print, and p.
image: '/assets/images/category/ruby/2020/puts-print-p/background.jpg'
---

<div id="contents_list" markdown="1">

## Contents

- [Contents](#contents)
- [Outline](#outline)
- [puts function](#puts-function)
- [print function](#print-function)
- [p function](#p-function)
- [Completed](#completed)

</div>

## Outline

In Ruby, `puts`, `print`, and `p` are String output functions. Let's see what difference and how to use them.

## puts function

In Ruby, `puts` is a basic output function. You can use it like below.

```ruby
puts 'Hello World!'
# Hello World!
```

You can also use it with parentheses.

```ruby
puts ('Hello World!')
# Hello World!
```

You can print multiple strings like below.

```ruby
puts 'Hello', 'World!'
# Hello
# World!
```

The `puts` function prints the string and adds a line break at the last.

## print function

In Ruby, the `print` function is similar to `puts` function, but not add a line break.

```ruby
print 'Hello World!'
# Hello World!
```

You can see a difference when you use it like below.

```ruby
print 'Hello', ' World!'
# Hello World!
```

If you want to break a line, you should add the line break character(`\n`).

```ruby
print "Hello\nWorld!"
# Hello
# World!
```

Note, when you use the Escape Sequences like the line break(`\n`) in Ruby, you should use the double quotation(`"`) to print them well.

## p function

In Ruby, you can print strings by itself via `p` function.

```ruby
p '100'
# '100'
```

It is useful to distinguish numbers and strings like below.

```ruby
p '100'
p 100
# '100'
# 100
```

## Completed

We've seen what difference and how to use String Output Function in Ruby. There are many functions. Normally, `puts` is used, so just don't forget `puts` function to print the string in Ruby.
