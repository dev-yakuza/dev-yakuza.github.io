---
layout: 'post'
permalink: '/ruby/begin-end-block/'
paginate_path: '/ruby/:num/begin-end-block/'
lang: 'en'
categories: 'ruby'
comments: true

title: BEGIN, END in Ruby
description: Let's see what BEGIN and END are, and how to use them in Ruby.
image: '/assets/images/category/ruby/2020/begin-end-block/background.jpg'
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [BEGIN block](#begin-block)
- [END block](#end-block)
- [Completed](#completed)

</div>

## Outline

In this blog post, we will see what `BEGIN` and `END` are, and how to use them. Simply, the BEGIN block is executed before the program is started, and the END block is executed after the program is finished.

## BEGIN block

When you define something in the BEGIN block, the block is executed before all definitions.

```ruby
puts "Hello"
BEGIN { puts "World" }
# World
# Hello
```

If there are multiple BEGIN blocks, the blocks are executed in order.

```ruby
puts "Hello"
BEGIN { puts "World" }
BEGIN { puts "BEGIN" }
# World
# BEGIN
# Hello
```

The BEGIN block has a local variable scope, so you can't share the other local variables.

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

## END block

The END block is executed after all codes are executed.

```ruby
END { puts 5 }
puts 1
# 1
# 5
```

If there are multiple END blocks, the blocks are executed in the reverse order.

```ruby
END { puts 5 }
END { puts 3 }
puts 1
# 1
# 3
# 5
```

Unlike the BEGIN block, the END block shares the variable scope. So you can share the local variable with the END block.

```ruby
i = 1
END { puts i }
# 1
```

## Completed

The BEGIN/END blocks are not often used, but it's Ruby's unique feature, so I think it has valuable for remembering.
