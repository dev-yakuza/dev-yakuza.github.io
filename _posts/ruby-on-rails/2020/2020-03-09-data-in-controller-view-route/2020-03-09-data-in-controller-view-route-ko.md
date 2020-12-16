---
layout: 'post'
permalink: '/ruby-on-rails/data-in-controller-view-route/'
paginate_path: '/ruby-on-rails/:num/data-in-controller-view-route/'
lang: 'ko'
categories: 'ruby-on-rails'
comments: true

title: 'Controller와 View, Route에서 데이터 교환'
description: 'Ruby on Rails에서 Controller와 View, 그리고 Route를 통해 데이터를 전달하는 방법에 대해서 알아봅시다.'
image: '/assets/images/category/ruby-on-rails/2020/data-in-controller-view-route/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [변수](#변수)
- [Controller에서 View에 데이터 전달](#controller에서-view에-데이터-전달)
- [View에서 Controller로 데이터 전달](#view에서-controller로-데이터-전달)
  - [GET 방식](#get-방식)
  - [POST 방식](#post-방식)
- [완료](#완료)
- [참고](#참고)

</div>

## 개요

Ruby on Rails에서 Controller와 View, 그리고 Route 사이에서 데이터를 전달하는 방법에 대해서 알아보려고 합니다.

이 블로그 포스트는 시리즈로 제작되었습니다. 자세한 내용은 아래에 링크를 참고하시기 바랍니다.

- [Mac에서 Ruby on Rails 시작하기]({{site.url}}/{{page.categories}}/rails-on-mac/){:target="_blank"}
- [Ruby on Rails로 생성한 프로젝트의 폴더 구조]({{site.url}}/{{page.categories}}/folder-structure/){:target="_blank"}
- [Ruby on Rails를 사용하여 새로운 웹 페이지 만들기]({{site.url}}/{{page.categories}}/create-page/){:target="_blank"}
- Controller와 View, Route에서 데이터 교환
- [Rails에서 DB 데이터 다루기]({{site.url}}/{{page.categories}}/database/){:target="_blank"}

여기서 사용한 소스코드는 Github에서 확인할 수 있습니다.

- [Github 소스코드](https://github.com/dev-yakuza/study-rails){:rel="nofollow noreferrer" target="_blank"}

## 변수

데이터를 전달하는 방법을 보기전에 Ruby의 변수에 대해서 잠깐 살펴보도록 하겠습니다. Ruby에서는 아래와 같은 변수들을 사용할 수 있습니다.

| 명칭 | 특징 | 변수 할당 |
|---|
| 지역 변수 | - 특정 동작 내부에서만 사용하는 변수<br/>특정 동작 내부에서만 사용하는 변수이므로, 특정 동작이외에서는 변수를 참조할 수 없다. | var = 1 |
| 인스턴스 변수 | - 한 객체에서만 사용이 가능한 변수<br/>- 변수 영역은 self가 가리키는 객체 내부로 제한됨. | @var = 1 |
| 클래스 변수 | - 해당 클래스의 모든 객체가 공유하는 변수<br/>- 클래스 메소드를 통해 접근이 가능.<br/>- 클래스의 내부 메소드를 정의하기 전에 class 선언부 바로안에 선언. | @@var = 1 |
| 전역 변수 | - 프로그램의 어떤 곳에서도 사용이 가능한 변수 | $var = 1 |

{% include in-feed-ads.html %}

## Controller에서 View에 데이터 전달

위에서 먼저 변수를 살펴본 이유는, Controller에서 View에 데이터를 전달할 때, 인스턴스 변수로 하기 때문입니다. 데이터가 전달되는지 확인하기 위해 `app/controllers/home_controller.rb`를 열고 아래와 같이 수정합니다.

```rb
class HomeController < ApplicationController
    def index
        @name = 'dev-yakuza'
    end
end
```

그리고 수정한 Action에 해당하는 View 파일을 수정합니다. `app/views/home/index.erb` 파일을 열고 아래와 같이 수정합니다.

```rb
Hello <%= @name %>!!
```

그리고 아래에 명령어를 통해 Rails 서버를 기동합니다.

```bash
bundle exec rails s
# bundle exec rails server
```

그리고 브라우저로 `http://127.0.0.1:3000/`에 접속해보면 아래와 같이 우리가 설정한 변수가 화면에 잘 표시되는 것을 확인할 수 있습니다.

![Ruby on Rails 서버 실행 결과 - Controller와 View의 데이터 교환](/assets/images/category/ruby-on-rails/2020/data-in-controller-view-route/result-data-controller-view.jpg)

이와 같이 Controller에서 View에 데이터를 전달하기 위해서는 인스턴스 변수를 사용하게 됩니다.

## View에서 Controller로 데이터 전달

Controller에서 View에 데이터를 전달하기 위해서는 간단하게 인스턴스 변수를 사용하면 됩니다. 그 이유는 URL로 Rails의 웹 서버로 요청이 들어오면 Controller가 그 요청에 해당하는 작업을 하고, View를 표기하기 때문입니다.

View에서 Controller로 데이터를 전달한다는 의미는, 사용자가 View를 통해 데이터를 입력한다는 의미와 같습니다.
View는 이미 사용자의 브라우저에 표시되었기 때문에 View에서 Controller로 데이터를 전달하는 경우는 사용자가 입력을 할 때 뿐이기 때문입니다.

View에서 Controller로 데이터를 전달하기 위해서는, 웹 서비스에서 사용자의 입력을 전달하는 방식과 동일하므로, GET 방식과 POST 방식으로 URL에 요청(Request)을 보내는 것으로 해결할 수 있습니다.

### GET 방식

GET 방식으로 데이터를 보내기 위해 View 파일을 수정해 봅시다. `app/views/home/index.erb` 파일을 열고 아래와 같이 수정합니다.

```rb
Hello <%= @name %>!!<br/>
<a href="/?name=yakuza">Display yakuza</a>
```

그리고 전달 받은 GET 파라메터를 표시하기 위해 Controller를 수정합니다. `app/controllers/home_controller.rb` 파일을 열고 아래와 같이 수정합니다.

```rb
class HomeController < ApplicationController
    def index
        name = params[:name]
        @name = name ? name : 'dev-yakuza'
    end
end
```

GET 방식은 URL로 데이터를 전달하므로, a 태그를 사용하여 데이터(`name=yakuza`)를 전달하였습니다. 이렇게 전달한 데이터는 Controller에서는 `params`라는 변수를 통해 데이터를 습득하게 됩니다.(`params[:name]`)

{% include in-feed-ads.html %}

### POST 방식

POST 방식으로 데이터를 보내기 위해 View 파일을 수정해 봅시다. `app/views/home/index.erb` 파일을 열고 아래와 같이 수정합니다.

```rb
Hello <%= @name %>!!<br/>
<a href="/?name=yakuza">Display yakuza</a><br/>
<form action="/" method="POST">
  <label for="name">name:</label>
  <input type="text" name="name" />
  <input type="submit" />
</form>
```

그리고 브라우저를 보면 아래와 같은 화면을 확인할 수 있습니다.

![POST 전송 - 데이터 입력전 화면](/assets/images/category/ruby-on-rails/2020/data-in-controller-view-route/before-send-data.jpg)

그리고 입력창에 데이터를 입력하고 `Submit` 버튼을 누르면 다음과 같이 에러가 발생합니다.

![POST 전송 - 데이터 전송 에러 화면](/assets/images/category/ruby-on-rails/2020/data-in-controller-view-route/send-data-error.jpg)

에러 메세지(`Routing Error`)에서 보면 알 수 있듯이, Route 설정을 제대로 하지 않아서 에러가 발생하였습니다.

우선 지금 현재의 Route 파일을 확인하기 위해, `config/routes.rb` 파일을 열어봅니다.

```rb
Rails.application.routes.draw do
  get '/', to: 'home#index'
end
```

위에 파일 내용에서도 알 수 있듯이 우리는 `/`의 URL에 `get` 방식의 요청(Request)만 연결한 상태입니다. 그렇기 때문에, POST 방식의 요청으로 들어온 경우 위와 같은 `Routing Error`를 확인할 수 있습니다.

그럼 POST 요청도 받을 수 있도록, Route를 수정해 보도록 합시다. `config/routes.rb` 파일을 아래와 같이 수정합니다.

```rb
Rails.application.routes.draw do
  get '/', to: 'home#index'
  post '/', to: 'home#index'
end
```

그리고 다시 `submit` 버튼을 누르면 아래와 같은 에러 화면을 볼 수 있습니다.

![POST 전송 - 데이터 전송 에러 화면 authenticity token](/assets/images/category/ruby-on-rails/2020/data-in-controller-view-route/send-data-error-authenticity-token.jpg)

다른 언어의 프레임워크들처럼 Rails도 기본적인 보안 취약점을 기본적으로 보호해 주고 있습니다. 여기서는 Rails가 `CSRF - Cross-site request forgery` 취약점을 보호하기 위해 POST 데이터를 전송할 시, 특정 키(key)값을 같이 전송하도록 하고 있습니다.

이 에러를 해결하기 위해서는 POST 데이터를 전송할 때, `authenticity_token`이라는 파라메터로 Rails에서 제공하는 `form_authenticity_token`을 전달해야 합니다.

다시 `app/views/home/index.erb` 파일을 열고 아래와 같이 수정합니다.

```rb
Hello <%= @name %>!!<br/>
<a href="/?name=yakuza">Display yakuza</a><br/>
<form action="/" method="POST">
  <input type="hidden" name="authenticity_token" value="<%= form_authenticity_token %>" />
  <label for="name">name:</label>
  <input type="text" name="name" />
  <input type="submit" />
</form>
```

그리고 다시 `http://127.0.0.1:3000/` 접속해서 입력칸에 test를 입력하고 submit 버튼을 누르면 아래와 같이 데이터가 잘 표시되는 것을 확인할 수 있습니다.

![POST 전송 - 데이터 전송 성공 화면](/assets/images/category/ruby-on-rails/2020/data-in-controller-view-route/result-post-data.jpg)

## 완료

이것으로 Controller와 View 사이에 데이터 전송에 대해서 알아보았습니다.

Controller에서 View로 데이터를 전달하기 위해서는 인스턴스 변수를 사용하였고, View에서 Controller에 데이터를 전송하기 위해서는 GET/POST 방식으로 데이터를 전달해야 했습니다.
POST 방식으로 전달하기 위해 Route에 POST용 URL도 추가하였습니다.

본격적으로 데이터를 다루기전에 준비 단계로 Controller와 View 사이에 데이터 전달에 대해서 알아보았습니다. 다음 블로그 포스트에서는 데이터를 DB에 저장하고, 저장한 데이터를 표시하는 방법에 대해서 알아보도록 하겠습니다.

## 참고

이 블로그 포스트는 시리즈로 제작되었습니다. 자세한 내용은 아래에 링크를 참고하시기 바랍니다.

- [Mac에서 Ruby on Rails 시작하기]({{site.url}}/{{page.categories}}/rails-on-mac/){:target="_blank"}
- [Ruby on Rails로 생성한 프로젝트의 폴더 구조]({{site.url}}/{{page.categories}}/folder-structure/){:target="_blank"}
- [Ruby on Rails를 사용하여 새로운 웹 페이지 만들기]({{site.url}}/{{page.categories}}/create-page/){:target="_blank"}
- Controller와 View, Route에서 데이터 교환
- [Rails에서 DB 데이터 다루기]({{site.url}}/{{page.categories}}/database/){:target="_blank"}

여기서 사용한 소스코드는 Github에서 확인할 수 있습니다.

- [Github 소스코드](https://github.com/dev-yakuza/study-rails){:rel="nofollow noreferrer" target="_blank"}
