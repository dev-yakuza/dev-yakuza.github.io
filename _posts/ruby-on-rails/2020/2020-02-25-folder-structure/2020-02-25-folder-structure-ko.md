---
layout: 'post'
permalink: '/ruby-on-rails/folder-structure/'
paginate_path: '/ruby-on-rails/:num/folder-structure/'
lang: 'ko'
categories: 'ruby-on-rails'
comments: true

title: 'Ruby on Rails로 생성한 프로젝트의 폴더 구조'
description: 'Ruby on Rails를 사용하여 생성한 프로젝트의 폴더 구조를 확인해 봅시다.'
image: '/assets/images/category/ruby-on-rails/2020/folder-structure/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [프로젝트 구조](#프로젝트-구조)
- [Controller 관련](#controller-관련)
- [View 관련](#view-관련)
- [URL 관련](#url-관련)
- [완료](#완료)
- [참고](#참고)

</div>

## 개요

이전 블로그에서 Ruby on Rails를 설치하고 Ruby on Rails를 사용하여 새로운 프로젝트를 생성하는 방법에 대해서 알아보았습니다.

이번 블로그에서는 새롭게 생성된 Rails 프로젝트의 폴더 구조를 파악해보려고 합니다.

이 블로그 포스트는 시리즈로 제작되었습니다. 자세한 내용은 아래에 링크를 참고하시기 바랍니다.

- [Mac에서 Ruby on Rails 시작하기]({{site.url}}/{{page.categories}}/rails-on-mac/){:target="_blank"}
- Ruby on Rails로 생성한 프로젝트의 폴더 구조
- [Ruby on Rails를 사용하여 새로운 웹 페이지 만들기]({{site.url}}/{{page.categories}}/create-page/){:target="_blank"}
- [Controller와 View, Route에서 데이터 교환]({{site.url}}/{{page.categories}}/data-in-controller-view-route/){:target="_blank"}
- [Rails에서 DB 데이터 다루기]({{site.url}}/{{page.categories}}/database/){:target="_blank"}

여기서 사용한 소스코드는 Github에서 확인할 수 있습니다.

- [Github 소스코드](https://github.com/dev-yakuza/study-rails){:rel="nofollow noreferrer" target="_blank"}

## 프로젝트 구조

Ruby on Rails로 프로젝트를 생성하면 아래와 같이 프로젝트가 생성됩니다. 아래에 내용은 생성된 프로젝트에서 중요한 부분만 간추렸습니다.

```bash
├── Gemfile
├── Gemfile.lock
├── README.md
├── Rakefile
├── app
│   ├── controllers
│   │   ├── application_controller.rb
│   │   └── concerns
│   ├── models
│   │   ├── application_record.rb
│   │   └── concerns
│   └── views
│       └── layouts
│           ├── application.html.erb
│           ├── mailer.html.erb
│           └── mailer.text.erb
├── babel.config.js
├── bin
├── config
│   ├── locales
│   │   └── en.yml
│   ├── routes.rb
├── config.ru
├── db
│   ├── development.sqlite3
│   └── seeds.rb
├── lib
├── log
│   └── development.log
├── package.json
├── postcss.config.js
├── public
├── storage
├── temp
├── test
├── vendor
└── yarn.lock
```

{% include in-feed-ads.html %}

## Controller 관련

Ruby on Rails도 여타 다른 프레임워크와 마찬가지로 `MVC 패턴`(Model-View-Controller 패턴)을 따릅니다. 따라서 Ruby on Rails을 사용하여 Model, View, Controller를 만듬으로써 웹 서비스를 만들 수 있습니다.

Ruby on Rails로 Controller를 생성하면 아래와 같은 폴더, 파일을 다루게 됩니다.

```bash
├── app
│   ├── assets
│   │   ├── stylesheets
│   │   │   ├── home.scss
│   ├── controllers
│   │   ├── home_controller.rb
│   ├── helpers
│   │   ├── home_helper.rb
├── test
│   ├── controllers
│   │   ├── home_controller_test.rb
```

다음 블로그에서 소개하겠지만, Rails의 명령어로 Conroller를 생성하면 위와 같이 파일들이 생성됩니다. 여기에서는 home_controller를 생성한 예제입니다.

Controller를 생성하는 방법에 대해서는 아래에 링크를 참고하시기 바랍니다.

- [Ruby on Rails를 사용하여 새로운 웹 페이지 만들기 - Controller]({{site.url}}/{{page.categories}}/create-page/#controller){:target="_blank"}

## View 관련

Ruby on Rails에서 화면을 표시하기 위한 View는 아래의 폴더에 생성하게 됩니다.

```bash
├── app
│   ├── views
│   │   ├── home
```

여기에서는 위와 같이 home_controller를 생성한 후의 폴더 모습입니다. 여러분은 아마 home 폴더가 보이지 않으실겁니다. home_controller를 Rails의 명령어로 통해 생성하면, 거기에 필요한 View를 보관할 home 폴더를 자동으로 생성됩니다.

Controller와 View를 생성하는 방법에 대해서는 아래에 링크를 참고하시기 바랍니다.

- [Ruby on Rails를 사용하여 새로운 웹 페이지 만들기 - View]({{site.url}}/{{page.categories}}/create-page/#view){:target="_blank"}

## URL 관련

Rails는 Ruby라는 언어를 사용하여 웹 서비스를 만들기 위한 프레임워크입니다. 웹 서비스를 만들기 위한 프레임워크이므로 당연히, URL을 관리하는 기능을 가지고 있습니다.

Rails에서 URL은 config 폴더 하단의 routes.rb 파일에서 관리하게 됩니다.

```bash
├── config
│   ├── routes.rb
```

Rails에 새로운 URL을 추가하는 방법에 대해서는 아래에 링크를 참고하시기 바랍니다.

- [Ruby on Rails를 사용하여 새로운 웹 페이지 만들기 - Route]({{site.url}}/{{page.categories}}/create-page/#routes){:target="_blank"}

{% include in-feed-ads.html %}

## Database

Ruby on Rails에서 Data를 다루기 위한 파일들은 아래와 같습니다.

```bash
├── app
│   ├── models
│   │   ├── post.rb
├── config
│   ├── database.yml
├── db
│   ├── migrate
│   │   ├── 20200313092804_create_posts.rb
├── test
│   ├── fixtures
│   │   ├── posts.yml
│   ├── models
│   │   ├── post_test.rb
```

- config/database.yml: Database의 연결 정보를 설정하는 파일
- app/models/post.rb: 실제 테이블과 연결되는 Model
- db/migrate/20200313092804_create_posts.rb: 테이블을 생성하기 위한 migratoin 파일
- test/fixtures/posts.yml: 테스트를 위한 Dummy 데이터
- test/models/post_test.rb: Model의 유닛 테스트를 위한 파일

데이터베이스를 설정하고, 데이터를 다루기 위한 방법에 대해서는 아래에 블로그를 참고하시기 바랍니다.

- [Rails에서 DB 데이터 다루기]({{site.url}}/{{page.categories}}/data){:target="_blank"}

## 완료

이것으로 Ruby on Rails의 폴더를 살펴보았습니다. 앞으로는 웹 서비스를 제작하기 위한 Controller, View, 그리고 Model을 생성하는 방법에 대해서 알아보도록 하겠습니다.

## 참고

이 블로그 포스트는 시리즈로 제작되었습니다. 자세한 내용은 아래에 링크를 참고하시기 바랍니다.

- [Mac에서 Ruby on Rails 시작하기]({{site.url}}/{{page.categories}}/rails-on-mac/){:target="_blank"}
- Ruby on Rails로 생성한 프로젝트의 폴더 구조
- [Ruby on Rails를 사용하여 새로운 웹 페이지 만들기]({{site.url}}/{{page.categories}}/create-page/){:target="_blank"}
- [Controller와 View, Route에서 데이터 교환]({{site.url}}/{{page.categories}}/data-in-controller-view-route/){:target="_blank"}
- [Rails에서 DB 데이터 다루기]({{site.url}}/{{page.categories}}/database/){:target="_blank"}

여기서 사용한 소스코드는 Github에서 확인할 수 있습니다.

- [Github 소스코드](https://github.com/dev-yakuza/study-rails){:rel="nofollow noreferrer" target="_blank"}
