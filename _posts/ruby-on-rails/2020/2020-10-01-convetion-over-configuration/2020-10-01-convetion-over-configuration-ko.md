---
layout: 'post'
permalink: '/ruby-on-rails/convention-over-configuration/'
paginate_path: '/ruby-on-rails/:num/convention-over-configuration/'
lang: 'ko'
categories: 'ruby-on-rails'
comments: true

title: '설정 보다는 규약'
description: 'Ruby on Rails는 설정(Configuration)보다는 규약(Convention)을 중요시 합니다. Rails에서 사용되는 규약에 대해서 알아봅시다.'
image: '/assets/images/category/ruby-on-rails/2020/convention-over-configuration/background.jpg'
published: false
---

<div id="contents_list" markdown="1">

## 목차

</div>

## 개요

Ruby on Rails는 다음과 같은 설계 철학을 가지고 있습니다.

- DRY: Don't Repeat Yourself. 같은 코드를 반복하지 말것.
- CoC: Convention over Configuration. 설정보다 규약이 중요.

이번 블로그 포스트에서는 Rails의 철학중 하나인 CoC(Convention over Configuration)에 대해서 알아봅시다.

## Convention over Configuration

Rails는 설정(Configuration)보다는 규약(Convention)을 더 중요시 합니다. Rails에서 말하는 대표적인 규약은 이름 규약이 있습니다. 예를 들어 `users` 테이블을 읽어 들이려면 User라는 이름의 클래스를 이용해야 합니다.

이처럼 Rails에서 미리 정의한 규약을 사용하면, 특별한 설정을 하지 않아도 사용이 가능합니다.

- DB 테이블과 클래스: users(복수형) 과 User(단수형) 사용

이제 Rails에서 사용하는 규약들에 대해서 알아봅시다.

{% include in-feed-ads.html %}

## Controller 이름 규칙

Rails에서는 다음과 같은 명령어로 Controller를 생성할 수 있습니다.

```bash
rails generate controller <Controller Name> <Option>
# rails g controller <Controller Name> <Option>
# rails g controller hello
```

이렇게 명령어를 사용하여 생성하면, Rails는 다음과 같은 규칙으로 Controller를 생성합니다.

| 종류                        | 설명                                                                                 | 예                       |
| --------------------------- | ------------------------------------------------------------------------------------ | ------------------------ |
| Controller 클래스           | 앞 글자는 대문자로 뒤에 "Controller"라는 글자를 붙인다.                              | HelloController          |
| Controller 클래스 파일 이름 | Controller 클래스의 파일 이름은 소문자로 만들고, 각 단어를 언더스코어(_)로 구분한다. | hello_controller.rb      |
| Helper 파일 이름            | Conroller 이름 뒤에 "_helper.rb"를 붙인다.                                           | hello_helper.rb          |
| Test 파일 이름              | Controller 이름 뒤에 "_controller_test.rb"를 붙인다.                                 | hello_controller_test.rb |

명령어를 사용하지 않고 수동으로 Controller를 생성하는 경우 위에 Controller 이름 규칙을 따라서 생성하시기 바랍니다. 만약, 코드를 정확하게 작성하였지만, 원하는 결과가 나오지 않는 경우, 이름 규칙을 잘 따르고 있는지 확인하시기 바랍니다.

## View 이름 규칙

View 파일만을 생성하기 위한 명령어는 없습니다. 아래와 같이 Controller를 생성할 때, 옵션을 추가하면 해당하는 View 파일이 생성됩니다.

```bash
rails generate controller <Controller Name> <View List>
# rails g controller hello index show create
```

Controller가 생성된 이후에 View 파일이 필요하게 되면, 다음의 규칙을 사용하여 View 파일을 생성해야 한다.

| 종류               | 설명                                                                | 예                                        |
| -------------------| ------------------------------------------------------------------- | ----------------------------------------- |
| View 파일 이름 | "app/views" 폴더 하위에 "/<Controller Name>/<Action Name>.html.erb" | app/views/hello/index.html.erb |

이 규칙에 맞게 View 파일을 생성하면, Rails는 액션 메서드가 실행된 이후에 대응되는 템플릿 파일을 찾아 실행합니다. 위에 규칙을 따라 View 파일을 생성하였다면, 액션 메서드가 존재하지 않아도, View 파일을 호출할 수 있습니다.

예를 들어 `/hello/show`라는 URL로 접근하면, hello 컨트롤러의 show 액션을 찾습니다. 하지만 액션이 없다면 곧바로 `hello/show.html.erb` 파일을 찾아 실행하게 됩니다.

만약, 규칙과는 상관없는 View 파일을 사용하고 싶다면, 다음과 같이 Controller의 액션 메서드를 수정하여 사용해야 합니다.

```ruby
def index
  render 'hello/show'
end
```

{% include in-feed-ads.html %}

## Model 이름 규칙

Ruby에서는 아래의 명령어를 사용하여 Model을 생성할 수 있습니다.

```bash
rails generate model <Model Name> <Options>
# rails g model book
```

이렇게 명령어를 사용하여 생성하면, Rails는 다음과 같은 규칙으로 Model을 생성합니다.

| 종류                   | 설명                                                                         | 예           |
| -----------------------| ---------------------------------------------------------------------------- | ------------ |
| Model 클래스           | 첫 글자를 대문자로 하고 단수형을 사용                                        | Book         |
| Model 클래스 파일 이름 | 첫 글자를 소문자로 하고 단수형을 사용                                        | book.rb      |
| 테이블                 | 첫 글자를 소문자로 하고 복수형을 사용                                        | books        |
| 테스트 스크립트        | 첫 글자를 소문자로하고 단수형을 사용하는 Model 이름 뒤에 "test.rb"를 붙인다. | book_test.rb |


## 완료
