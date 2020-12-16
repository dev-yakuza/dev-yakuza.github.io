---
layout: 'post'
permalink: '/ruby/iterator/'
paginate_path: '/ruby/:num/iterator/'
lang: 'en'
categories: 'ruby'
comments: true

title: Iterator in Ruy
description: Let's see how to use the Iterator to handle the arrays more comfortable in Ruby.
image: '/assets/images/category/ruby/2020/iterator/background.jpg'
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [Iterator](#iterator)
  - [each method](#each-method)
  - [times method](#times-method)
  - [loop method](#loop-method)
- [Iterators usage](#iterators-usage)
  - [each_with_index method](#each_with_index-method)
  - [Hash](#hash)
  - [File](#file)
- [Define the iterator](#define-the-iterator)
- [Completed](#completed)

</div>

## Outline

In this blog post, we'll see what the Iterator is, and how to use the Iterator to handle arrays easily.

## Iterator

The Iterator is a method to iterate over each element of an object with multiple elements, such as an array. In this blog post, I will introduce the frequently used iterators.

### each method

Each element of the array is assigned to `|variable|` and iterates over it.

```ruby
<Array>.each { |<Variable>|
  Repeat actions
}
```

You can use `each` method like below.

```ruby
fruits = ['apple', 'banana', 'orange']
fruits.each {|fruit|
  puts fruit
}
```

### times method

If the number of iterations is fixed, you can use `times` method.

```ruby
4.times {
  puts 'Hello world'
}
```

In Ruby, the number is also an object, so you can use `times` method like above.

### loop method

The loop method performs iteration without termination.

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

You can terminate `loop` by using `break` like above, but If you don't, it will be into the infinite loop, so be careful to use this.

{% include in-feed-ads.html %}

## Iterators usage

When you handle the Arrays, it is more convenient to use iterators.

### each_with_index method

If you need the Index in the Arrays, you can use `each_with_index` method.

```ruby
fruits = ['apple', 'banana', 'orange']
fruits.each_with_index {|fruit, i|
  puts "#{i}: #{fruit}"
}
```

### Hash

You can also use the Iterators in Hash.

```ruby
fruits = {:Apple => 'apple', :Banana => 'banana', :Orange => 'orange'}
fruits.each {|key, value|
  puts "#{key}: #{value}"
}
```

### File

You can use the Iterators in the File class. If you use the Iterator in the File, you can get the line of the text file.

```ruby
file = File.open("test.txt")
file.each {|line|
  puts line
}
file.close
```

## Define the iterator

When you define the method, you can define the Iterator by using `yield`.

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

## Completed

We've seen what the iterator is, and how to use the iterator. Also, we can define a new iterator when we need. From now on, let's use the Iterators to handle Arrays, Hash, and so on.
