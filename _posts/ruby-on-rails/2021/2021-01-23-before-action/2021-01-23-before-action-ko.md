---
layout: 'post'
permalink: '/ruby-on-rails/before_action/'
paginate_path: '/ruby-on-rails/:num/before_action/'
lang: 'ko'
categories: 'ruby-on-rails'
comments: true

title: 'before_action이란'
description: 'Ruby on Rails에서 before_action이 무엇인지, 어떻게 사용하는지에 대해서 알아봅시다.'
image: '/assets/images/category/ruby-on-rails/background.jpg'
published: false
---

<div id="contents_list" markdown="1">

## 목차

</div>

## 개요

이번 블로그 포스트에서는 Rails의 Controller에서 자주 사용되는 `before_action`가 무엇이며, 어떻게 사용하는지에 대해서 알아보려고 합니다.

## before_action

before_action은 Rails에서 Controller에서 사용되며, 액션 메서드를 실행되기 전에 실행할 메서드를 지정할 때 사용합니다.

before_action은 다음과 같은 형태로 사용합니다.

```ruby
before_action method, only: action
```

- method: 액션 메서드가 실행되기전에 실행할 메서드
- action: 특정 액션 메서드를 지정할 때 사용

예를 들면, before_action은 다음과 같이 Rails의 Controller에서 사용할 수 있습니다.

```ruby
class BooksController < ApplicationController
  before_action :set_book, only: :show

  def show
    ...
  end

  private
  def set_book
    @book = Book.find(params[:id])
  end
end
```

이 예제에서는 `show` 액션이 실행되기 전에 `set_book` 메서드가 실행됩니다. 이렇게 `before_action`을 사용하면 여러 개의 액션에서 공통으로 사용되는 처리를 간단하게 작성할 수 있습니다.

## 완료