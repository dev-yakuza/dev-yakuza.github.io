---
layout: 'post'
permalink: '/ruby-on-rails/command-and-option/'
paginate_path: '/ruby-on-rails/:num/command-and-option/'
lang: 'ko'
categories: 'ruby-on-rails'
comments: true

title: 'Rails 명령어'
description: 'Ruby on Rails에서 사용되는 명령어는 무엇이 있는지 살펴보고, 그 명령어들을 어떻게 사용하는지 살펴보도록 하겠습니다.'
image: '/assets/images/category/ruby-on-rails/2020/command-and-option/background.jpg'
published: false
---

<div id="contents_list" markdown="1">

## 목차

</div>

## 개요

Ruby on Rails는 웹 애플리케이션 프레임워크로써, 간단하게 웹 애플리케이션을 제작할 수 있게 도와줍니다. Ruby on Rails는 웹 애플리케이션을 보다 간단하게 제작할 수 있도록 많은 명령어들을 준비해 두고 있습니다.

이번 블로그 포스트에서는 Ruby on Rails가 가지고 있는 명령어들을 살펴보고 어떻게 사용하는지 확인하도록 하겠습니다.

## rails new

Rails에서 새로운 프로젝트를 생성할 때 `rails new` 명령어를 사용합니다.

```bash
rails new [Project Name] [Options]
# rails new helloPorject
```

이 명령어를 실행하면, Rails의 기본 구조를 가진 프로젝트가 생성됩니다.

이 명령어에서 사용 가능한 옵션은 다음과 같습니다.

| 분류   | 옵션                        | 설명                                                                    |
| ------ | --------------------------- | ----------------------------------------------------------------------- |
| 기본   | -r, --ruby=PATH             | Ruby의 기본 경로가 아닌 경로를 지정합니다.                              |
| 기본   | -d, --database=DATABASE     | 프로젝트에서 사용할 데이터베이스를 설정합니다. 기본값은 sqlite3 입니다. |
| 기본   | -m, --template=TEMPLATE     | 애플리케이션 템플릿 경로 또는 URL을 지정합니다.                         |
| 동작   | --skip-gemfile              | Gemfile을 생성하지 않습니다.                                            |
| 동작   | --skip-keeps                | .keep 파일을 생성하지 않습니다.                                         |
| 동작   | -B, --skip-bundle           | bundle install을 실행하지 않습니다.                                     |
| 동작   | -G, --skip-git              | .gitignore 파일을 생성하지 않습니다.                                    |
| 동작   | -j, --javascript=JAVASCRIPT | 애플리케이션에서 사용할 자바스크립트 라이브러리를 지정합니다.           |
| 동작   | -J, --skip-javascript       | 자바스크립트 라이브러리를 추가하지 않습니다.                            |
| 동작   | -O, --skip-active-record    | 액티브 레코드를 생성하지 않습니다.                                      |
| 동작   | -S, --skip-sprockets        | Sprockets을 추가하지 않습니다.                                          |
| 런타임 | -T, --skip-test-unit        | Test::Unit을 추가하지 않습니다.                                         |
| 런타임 | -f, --force                 | 프로젝트가 존재하는 경우 프로젝트를 덮어씁니다.                         |
| 런타임 | -q, --quiet                 | 명령어 실행 상태를 표시하지 않습니다.                                   |
| 런타임 | -s, --skip                  | 이미 존재하는 폴더는 건너뜁니다.                                        |
| 기타   | -v, --version               | Rails의 버전을 표시합니다.                                              |
| 기타   | -h, --help                  | 도움말을 표시합니다.                                                    |

다음과 같은 명령어를 사용하면 애플리케이션을 이전 버전으로 생성할 수 있다.

```bash
rails _3.2.0_ new helloProject
```

{% include in-feed-ads.html %}

## rails server

Rails로 웹 애플리케이션을 개발할 때, Apache와 같은 웹 서버를 준비할 필요가 없다. Rails에서는 다음 명령어를 실행하면 웹 개발에 필요한 개발 서버를 실행할 수 있다.

```bash
rails server [Options]
# rails server
```

이는 어디까지나 개발용 서버이므로, 실제 서버 환경에서는 Apache나 Nginx와 같은 웹 서버를 사용해야 한다.

| 옵션                   | 설명                                        | 기본값      |
| ---------------------- | ------------------------------------------- | ----------- |
| -p, --port=PORT        | 사용할 포트 번호를 설정합니다.              | 3000        |
| -b, --binding=IP       | 바인딩할 IP 주소를 설정합니다.              | 0.0.0.0     |
| -d, --daemon           | 서버를 데몬으로 실행할지 여부를 설정합니다. |             |
| -e, --environment=NAME | 특정 환경으로 서버를 실행합니다.            | development |
| -p, --pid=PID          | PID 파일을 설정합니다.                      |             |
| -h, --help             | 도움말을 표시합니다.                        |             |

아래는 `rails server`에서 사용할 수 있는 옵션들입니다.

## rails generate

Rails는 MVC(Model-View-Controller) 패턴을 따르고 있다. 웹 애플리케이션을 제작하기 위해서는 Model, View, Controller 등을 제작해야 한다. 이런 Movel, View, Controller 등과 같은 파일을 생성하기 위해서 Rails는 `rails generate`라는 명령어를 제공하고 있다.

```bash
rails generate [Target] [Name] [Options]
# rails generate controller hello
```

아래는 `rails generate`에서 사용할 수 있는 옵션들이다.

| 옵션          | 설명                                                                     |
| ------------- | ------------------------------------------------------------------------ |
| -f, --force   | 파일이 이미 존재하면 덮어쓰기한다.                                       |
| -p, --pretend | 실제로 파일을 생성하지 않고 시험삼아 명령어를 실행하며, 결과를 표시한다. |
| -q, --quiet   | 명령어의 진행 상태를 표시하지 않는다.                                    |
| -s, --skip    | 같은 이름의 파일이 존재하면 건너뜁니다.                                  |

그럼 `rails generate`를 사용하여 만들 수 있는 명령어들에 대해서 알아봅시다.

### Controller

Rails는 MVC(Model-View-Controller) 패턴을 따르고 있다. 아래에 명령어를 실행하면 Controller를 생성할 수 있다.

```bash
rails generate controller [ControllerName] [Options]
# rails generate controller hello
```

위에 명령어에서 `generate` 대신 `g`를 사용할 수 있다.

```bash
rails g controller [ControllerName] [Options]
# rails g controller hello
```

아래는 `rails generate controller` 명령어와 함께 사용할 수 있는 옵션들입니다.

| 옵션                       | 설명                                    | 기본값    |
| -------------------------- | --------------------------------------- | --------- |
| --assets                   | 에셋을 같이 생성할지 여부를 결정합니다. | true      |
| -e, --template-engine=NAME | 사용할 템플릿 엔진을 설정합니다.        | erb       |
| -t, --test-framework=NAME  | 사용할 테스트 프레임워크를 설정합니다.  | test_unit |
| --helper                   | 헬퍼를 생성할지 여부를 설정합니다.      | true      |

아래에 명령어를 사용하면 Controller를 생성할 때, View도 함께 생성할 수 있습니다.

```bash
rails g controller [ControllerName] [ViewList]
# rails g controller hello index show
```

{% include in-feed-ads.html %}

### model

아래에 명령어를 사용하여 Rails의 Model을 생성할 수 있습니다.

```bash
rails generate model [ModelName] [Options]
# rails generate model book
```

아래는 `rails generate model` 명령어에서 사용할 수 있는 옵션들입니다.

| 옵션                      | 설명                                                                  | 기본값        |
| ------------------------- | --------------------------------------------------------------------- | ------------- |
| --indexes                 | 외부 키를 나타내는 필드에 인덱스를 추가할지 여부를 설정합니다.        | true          |
| -o, --orm=NAEM            | 사용할 ORM을 설정합니다.                                              | active_record |
| --migration               | 마이그레이션 파일 생성 여부를 설정합니다.                             | true          |
| --timestamps              | 타입스탬프(created_at, updated_at) 필드를 생성할지 여부를 설정합니다. | true          |
| -t, --test-framework=NAME | 사용할 테스트 프레임워크를 설정합니다.                                | test_unit     |
| --fixture                 | 픽스처 생성 여부를 설정합니다.                                        | true          |

아래와 같이 `rasil generate model` 명령어로 Model을 생성할 때, Model에서 사용할 필드를 함께 정의할 수 있습니다.

```bash
rails generate model book title:string price: integer published_at:date deleted: boolean
```

## rails destroy

Rails에서 `rails generate` 명령어를 실행하면, 많은 파일들이 생성됩니다. 만약, `rails generate`로 생성한 내용이 불필요한 경우, 생성된 파일들을 하나씩 지워도 되지만, `rails
destroy` 명령어를 사용하여 한번에 모두 삭제할 수 도 있습니다.

```bash
rails destroy [Target] [Name]
# rails destroy controller hello
```

### rails destroy model

데이터베이스나 모델과 관련된 파일을 삭제할 때 사용하는 명령어입니다. 다음과 같이 사용할 수 있습니다.

```bash
rails destroy model book
```

## rails generate scaffold

Rails의 스캐폴딩(scaffolding) 기능을 사용하여 테이블과 관련된 기능을 한꺼번에 생성할 수 있습니다.

```bash
rails generate scaffold [name] [field:type] ... [options]
```

- name: 모델 이름
- field: 필드 이름
- type: 자료형
- options: 동작 옵션

동작 옵션은 `rails generate controller/model`과 같으므로 해당 내용을 참고하시기 바랍니다.

다음 예와 같이 Rails의 스캐폴딩 기능을 사용하여 테이블을 생성할 수 있습니다.

```bash
rails generate scaffold book isbn:string title:string price:integer author:strig published:date
```

위에 명령어를 실행하면 다음과 같은 파일들이 자동 생성됩니다.

```bash
├── app
│   ├── controllers
│   │   └── books_controller.rb
│   ├── models
│   │   └── book.rb
│   └── views
│   │   └── books
│   │       ├── index.html.erb
│   │       ├── index.json.jsbuilder
│   │       ├── edit.html.erb
│   │       ├── show.html.erb
│   │       ├── show.json.jsbuilder
│   │       ├── new.html.erb
│   │       └── _form.html.erb
│   └── assets
│   │   └── stylesheets
│   │       ├── books.css.scss
│   │       └── scaffolds.css.scss
│   └── helpers
│       └── books_helper.rb
│           ├── books.css.scss
│           └── scaffolds.css.scss
├── db
│   └── migrate
│       └── 20201002010101_create_books.rb
└── test
    ├── models
    │   └── book_test.rb
    ├── helpers
    │   └── books_helper_test.rb
    ├── controllers
    │   └── books_controller_test.rb
    └── fixtures
        └── books.yml
```

스캐폴딩 기능을 사용하면 위와 같이 자동으로 필요한 파일들을 생성해주므로 좀 더 간단하게 애플리케이션을 개발할 수 있습니다.

## rails db

Rails를 사용하면 웹 애플리케이션에서 사용할 DB를 쉽게 생성할 수 있습니다. Rails에서 DB 생성과 관련된 명령어를 살펴봅시다.

### rails db:migrate

Rails에서 `rails generate model` 명령어로 Model을 생성하면 Migration 파일이 생성됩니다. 이 Migration 파일에 Table에 대한 정보를 입력하고 아래에 명령어를 실행하면, 실제 데이터베이스에 Migration 파일의 내용으로 Table을 생성할 수 있습니다.

```bash
rails db:migrate
```

### rails db:fixures

Rails에서 `rails generate model` 명령어로 Model을 생성하면 Fixture 파일이 생성됩니다. 이 Fixture 파일에는 미리 준비가 필요한 데이터들를 정의할 수 있습니다. 주로 마스터 데이터를 준비하거나, 테스트를 위한 데이터를 준비할 때 사용됩니다. 이렇게 준비한 데이터를 실제 데이터베이스에 추가하기 위해서는 아래에 명령어를 사용합니다.

```bash
rails db:fixtures:load FIXTURES=[FixtureName]
```

```bash
rails db:migrate
```

### rails dbconsole

Rails는 데이터베이스에 접속하기 위한 데이터베이스 클라이언트를 제공하고 있습니다. 아래에 명령어를 실행하면 Rails가 제공하는 데이터베이스 클라이언트를 사용할 수 있습니다.

```bash
rails dbconsole
```

위와 같이 명령어를 실행하면 아래와 같이 데이터베이스 클라이언트가 실행되는 것을 확인할 수 있습니다.

```bash
sqlite>
```

## rake routes

Rails에서는 웹 애플리케이션의 URL을 `config/routes.rb` 파일에서 관리하고 있습니다. `rake routes` 명령어를 사용하면 해당 Rails 애플리케이션에서 사용하는 모든 URL을 확인할 수 있습니다.

```bash
rails routes
```

위에 명령어를 실행하면 다음과 같이 Rails 애플리케이션에서 사용하는 모든 URL을 확인할 수 있습니다.

```bash
Prefix Verb   URI Pattern   Controller#Action
rails_postmark_inbound_emails POST   /rails/action_mailbox/postmark/inbound_emails(.:format)   action_mailbox/ingresses/postmark/inbound_emails#create
rails_relay_inbound_emails POST   /rails/action_mailbox/relay/inbound_emails(.:format)   action_mailbox/ingresses/relay/inbound_emails#create
...
```

## rake notes

코드에 직접적으로 앞으로 할일, 수정해야할 일, 최적화해야할 일들을 잊지 않기 위해 주석으로 메모를 남기곤 합니다.

```rb
def validate(value)
  # TODO: implement this function
end
```

Rails에서는 이렇게 남긴 메모를 `rails notes` 명령어를 통해 확인할 수 있습니다.

```bash
rails notes
```

사용 가능한 노트는 `TODO`, `FIXME`, `OPTIMIZE`이며, 각각의 노트는 다음과 같은 명령어로 별도로 확인할 수 있습니다.

```bash
rails notes:todo
rails notes:fixme
rails notes:optimize
```

## 완료
