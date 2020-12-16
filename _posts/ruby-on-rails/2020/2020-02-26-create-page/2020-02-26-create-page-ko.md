---
layout: 'post'
permalink: '/ruby-on-rails/create-page/'
paginate_path: '/ruby-on-rails/:num/create-page/'
lang: 'ko'
categories: 'ruby-on-rails'
comments: true

title: 'Ruby on Rails를 사용하여 새로운 웹 페이지 만들기'
description: 'Ruby on Rails를 사용하여 새로운 웹 페이지를 생성하는 방법에 대해서 알아봅니다.'
image: '/assets/images/category/ruby-on-rails/2020/create-page/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [Controller](#controller)
  - [Controller 생성 에러](#controller-생성-에러)
  - [Controller 생성 파일](#controller-생성-파일)
  - [Controller에 Action 추가](#controller에-action-추가)
- [View](#view)
  - [Controller와 View 연결](#controller와-view-연결)
- [Routes](#routes)
- [확인](#확인)
- [완료](#완료)
- [참고](#참고)

</div>

## 개요

Ruby on Rails를 사용하여 새로운 웹 페이지를 생성하는 방법에 대해서 알아보려고 합니다.

이 블로그 포스트는 시리즈로 제작되었습니다. 자세한 내용은 아래에 링크를 참고하시기 바랍니다.

- [Mac에서 Ruby on Rails 시작하기]({{site.url}}/{{page.categories}}/rails-on-mac/){:target="_blank"}
- [Ruby on Rails로 생성한 프로젝트의 폴더 구조]({{site.url}}/{{page.categories}}/folder-structure/){:target="_blank"}
- Ruby on Rails를 사용하여 새로운 웹 페이지 만들기
- [Controller와 View, Route에서 데이터 교환]({{site.url}}/{{page.categories}}/data-in-controller-view-route/){:target="_blank"}
- [Rails에서 DB 데이터 다루기]({{site.url}}/{{page.categories}}/database/){:target="_blank"}

여기서 사용한 소스코드는 Github에서 확인할 수 있습니다.

- [Github 소스코드](https://github.com/dev-yakuza/study-rails){:rel="nofollow noreferrer" target="_blank"}

Ruby on Rails도 여타 다른 프레임워크와 마찬가지로 `MVC 패턴`(Model-View-Controller 패턴)을 따릅니다. 따라서 새로운 웹 페이지를 작성하기 위해서는 기본적으로 `View`와 `Controller`를 제작할 필요가 있습니다.

## Controller

우선, 아래에 명령어를 사용하여 Controller를 생성합니다.

```bash
# cd StudyRails
bundle exec rails generate controller home
```

generate 명령어를 간단하게 `g`로 줄여서 아래와 같이 사용할 수도 있습니다.

```bash
bundle exec rails g controller home
```

### Controller 생성 에러

위에 명령어를 실행해도 아무 동작도 하지 않는다면, 실행한 명령어를 중지시키고 아래에 명령어를 실행합니다.

```bash
rake app:update:bin
```

그러면 아래와 같은 메세지를 확인할 수 있습니다. `Y`를 입력하여 다음으로 진행합니다.

```bash
/StudyRails/bin/rails? (enter "h" for help) [Ynaqdhm]
/StudyRails/bin/rake? (enter "h" for help) [Ynaqdhm]
```

그리고 다시 아래에 명령어를 실행하여 Controller를 생성합니다.

```bash
# cd StudyRails
bundle exec rails generate controller home
```

또, 아래와 같은 메세지가 표시되면서 Controller가 생성되지 않는 다면,

```bash
error Couldn't find an integrity file
error Found 1 errors.


========================================
  Your Yarn packages are out of date!
  Please run `yarn install --check-files` to update.
========================================


To disable this check, please change `check_yarn_integrity`
to `false` in your webpacker config file (config/webpacker.yml).
```

위에 설명에도 나온 것처럼 아래에 명령어를 실행합니다.

```bash
yarn install --check-files
```

그리고 다시 아래에 명령어를 사용하여 Controller를 생성합니다.

```bash
# cd StudyRails
bundle exec rails generate controller home
# bundle exec rails g controller home
```

문제없이 생성되었다면 아래와 같은 메세지를 확인할 수 있습니다.

```bash
create  app/controllers/home_controller.rb
invoke  erb
create    app/views/home
invoke  test_unit
create    test/controllers/home_controller_test.rb
invoke  helper
create    app/helpers/home_helper.rb
invoke    test_unit
invoke  assets
invoke    scss
create      app/assets/stylesheets/home.scss
```

{% include in-feed-ads.html %}

### Controller 생성 파일

Rails의 명령어로 Controller를 생성하면 아래와 같은 파일들이 생성됩니다.

```bash
├── app
│   ├── assets
│   │   ├── stylesheets
│   │   │   ├── home.scss
│   ├── controllers
│   │   ├── home_controller.rb
│   ├── helpers
│   │   ├── home_helper.rb
│   ├── views
│   │   ├── home
├── test
│   ├── controllers
│   │   ├── home_controller_test.rb
```

이렇게 생성된 파일중 `app/controllers/home_controller.rb`를 사용하여, 대부분 작업을 처리하게 됩니다.

### Controller에 Action 추가

위에서 생성된 `app/controllers/home_controller.rb` 파일을 열고 아래와 같이 수정합니다.

```rb
class HomeController < ApplicationController
    def index
    end
end
```

여기서 home_controller에 index 함수를 추가하였습니다. Rails에서는 Controller에 추가하는 함수를 Action이라고 표현합니다.

## View

Rails의 명령어를 사용하여 Controller를 생성하였다면 아래와 같은 폴더를 확인할 수 있습니다.

```bash
├── app
│   ├── views
│   │   ├── home
```

Rails 명령어로 생성된 home 폴더에 home_controller.rb에 필요한 View 파일을 생성하여 연결할 예정입니다.

home 폴더안에 `index.erb` 파일을 생성하고 아래와 같이 수정합니다.

```rb
Hello Rails!!
```

### Controller와 View 연결

Controller와 View를 연결하기 위해서 특별한 처리는 없습니다. Controller의 Action명(함수 명 - `def index`)과 View 파일의 파일명(`index.erb`)이 일치한다면, Rails는 따로 지정하지 않아도 자동적으로 해당 View 파일을 연결합니다.

{% include in-feed-ads.html %}

## Routes

Rails에서 `Routes`는 URL과 Controller를 연결해 주는 역할을 합니다. 위에서 만든 Controller를 연결하기 위해 `config/routes.rb` 파일을 열고 아래와 같이 수정합니다.

```rb
Rails.application.routes.draw do
  get '/', to: 'home#index'
end
```

위와 같이 수정하면, `/` URL에 `GET` 요청이 들어오면 `home_controller`의 `index` 액션(함수)를 실행하게 됩니다. 이렇게 실행된 index 액션은 같은 이름으로 된 `home/index.erb` 파일을 찾아 화면에 표시하게 됩니다.

## 확인

이것으로 새로운 페이지를 표시하기 위한 준비는 모두 끝났습니다. 아래에 명령어를 실행하여 Rails 서버를 기동시킵니다.

```bash
rails server
```

또는 간단하게 아래에 명령어를 사용할 수 있습니다.

```bash
rails s
```

그리고 브라우저를 열고 `http://127.0.0.1:3000/`으로 접속하면 아래와 같이 우리가 만든 화면을 볼 수 있습니다.

![Ruby on Rails 서버 실행 결과](/assets/images/category/ruby-on-rails/2020/create-page/rails-server.jpg)

## 완료

이것으로 Ruby on Rails를 사용하여 새로운 페이지를 생성하는 방법에 대해서 알아보았습니다.

Controller를 생성하고 Controller 안에 액션(함수)를 선언하고 액션 이름(함수명)과 동일한 View 파일을 생성하고, 마지막으로 Route에 URL과 Controller를 연결함으로써 새로운 페이지를 표시할 수 있었습니다.

이제 일단 페이지를 만들 수 있게 되었으므로, 다음에는 데이터를 다루는 방법에 대해서 알아보도록 하겠습니다.

## 참고

이 블로그 포스트는 시리즈로 제작되었습니다. 자세한 내용은 아래에 링크를 참고하시기 바랍니다.

- [Mac에서 Ruby on Rails 시작하기]({{site.url}}/{{page.categories}}/rails-on-mac/){:target="_blank"}
- [Ruby on Rails로 생성한 프로젝트의 폴더 구조]({{site.url}}/{{page.categories}}/folder-structure/){:target="_blank"}
- Ruby on Rails를 사용하여 새로운 웹 페이지 만들기
- [Controller와 View, Route에서 데이터 교환]({{site.url}}/{{page.categories}}/data-in-controller-view-route/){:target="_blank"}
- [Rails에서 DB 데이터 다루기]({{site.url}}/{{page.categories}}/database/){:target="_blank"}

여기서 사용한 소스코드는 Github에서 확인할 수 있습니다.

- [Github 소스코드](https://github.com/dev-yakuza/study-rails){:rel="nofollow noreferrer" target="_blank"}
