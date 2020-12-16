---
layout: 'post'
permalink: '/ruby-on-rails/database/'
paginate_path: '/ruby-on-rails/:num/database/'
lang: 'ko'
categories: 'ruby-on-rails'
comments: true

title: 'Rails에서 DB 데이터 다루기'
description: 'Ruby on Rails를 사용해서 DB에 데이터를 CRUD(Create Read Update Delete)하는 방법에 대해서 알아봅니다.'
image: '/assets/images/category/ruby-on-rails/2020/database/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [DB 설정](#db-설정)
- [mysql2](#mysql2)
- [Model 만들기](#model-만들기)
- [테이블 생성](#테이블-생성)
- [CRUD](#crud)
  - [Create](#create)
  - [Read](#read)
  - [Update](#update)
  - [Delete](#delete)
- [완료](#완료)
- [참고](#참고)

</div>

## 개요

이번 블로그 포스트에서는 Rails를 사용하여 본격적으로 데이터를 다루어 보려고 합니다. 본격적으로 데이터를 다루기 위해 DB를 설정하고, DB에 테이블을 생성할 예정입니다.
이렇게 생성된 DB에 Rails를 사용하여 CRUD(Create Read Update Delete)를 해 봄으로써, Rails에서 데이터를 다루는 방법에 대해서 이해해 보려고 합니다.

이 블로그 포스트는 시리즈로 제작되었습니다. 자세한 내용은 아래에 링크를 참고하시기 바랍니다.

- [Mac에서 Ruby on Rails 시작하기]({{site.url}}/{{page.categories}}/rails-on-mac/){:target="_blank"}
- [Ruby on Rails로 생성한 프로젝트의 폴더 구조]({{site.url}}/{{page.categories}}/folder-structure/){:target="_blank"}
- [Ruby on Rails를 사용하여 새로운 웹 페이지 만들기]({{site.url}}/{{page.categories}}/create-page/){:target="_blank"}
- [Controller와 View, Route에서 데이터 교환]({{site.url}}/{{page.categories}}/data-in-controller-view-route/){:target="_blank"}
- Rails에서 DB 데이터 다루기

여기서 사용한 소스코드는 Github에서 확인할 수 있습니다.

- [Github 소스코드](https://github.com/dev-yakuza/study-rails){:rel="nofollow noreferrer" target="_blank"}

{% include in-feed-ads.html %}

## DB 설정

우선 DB를 다루기 위해서는 Rails에 DB에 대한 설정을 해 주어야합니다. 여기서는 mysql을 설정하는 방법에 대해서만 다룹니다.
mysql은 이미 로컬에 설치되었다는 가정하에 진행합니다.

Rails에서 DB 설정은 `config/database.yml` 파일이 담당하고 있습니다. `config/database.yml` 파일을 열면 아래와 같은 내용을 확인할 수 있습니다.

```yml
default: &default
  adapter: sqlite3
  pool: <%= ENV.fetch("RAILS_MAX_THREADS") { 5 } %>
  timeout: 5000

development:
  <<: *default
  database: db/development.sqlite3

test:
  <<: *default
  database: db/test.sqlite3

production:
  <<: *default
  database: db/production.sqlite3
```

Rails는 기본적으로 sqlite3를 설정하고 있습니다. 우리는 mysql을 사용할 예정이므로 위에 설정을 아래와 같이 수정합니다.

```yml
default: &default
  adapter: mysql2
  encoding: utf8
  database: study_rails
  pool: 5
  username: root
  password:
  socket: /tmp/mysql.sock

development:
  <<: *default

test:
  <<: *default

production:
  <<: *default
```

위에 설정에서 database, username, password를 자신의 로컬 환경에 맞춰서 수정해 줍니다.

위에 설정은 모든 설정을 `default`에 작성하였으며, 다른 환경에서는 default에 모든 내용을 참조하도록 하였습니다. 특정 환경에서 특정 정보를 수정하고 싶다면 아래와 같이 변경할 수 있습니다.

```yml
production:
  <<: *default
  username: root
  password: XXXX
```

위와 같이 작성하면 production 환경인 경우는 주어진 username과 password를 사용하게 됩니다.

DB 설정에 사용할 수 있는 매개 변수는 다음과 같습니다.

| 이름     | 설명                                                     |
| -------- | -------------------------------------------------------- |
| adapter  | 접속할 데이터베이스 종류(sqlite3, mysql2, postgresql 등) |
| database | 데이터베이스 이름(sqlite는 데이터베이스 파일 경로)       |
| host     | 호스트 이름 또는 IP 주소                                 |
| port     | 포트 번호                                                |
| pool     | 확보할 접속 풀                                           |
| timeout  | 접속 타임아웃(밀리초 단위)                               |
| encoding | 사용할 문자 코드                                         |
| username | 사용자 이름                                              |
| password | 비밀 번호                                                |
| socket   | 소켓(/tmp/mysql.sock)                                    |

{% include in-feed-ads.html %}

## mysql2

Rails에서 Mysql에 연결하기 위해서는 `mysql2`라는 gem이 필요합니다. 아래에 명령어로 `mysql2`를 설치합니다.

```bash
bundle add mysql2
```

설치가 완료되었다면, 아래에 명령어를 사용하여 데이터베이스를 생성합니다.

```bash
bundle exec rake db:create
```

만약 아래와 같은 메세지가 나오면서 데이터베이스가 생성되지 않는다면,

```bash
warning: Using the last argument as keyword parameters is deprecated; maybe ** should be added to the call
The called method `initialize' is defined here
[BUG] Segmentation fault at 0x0000000000000000
...
```

아래에 명령어를 사용하여 mysql2를 설치합니다.

```bash
gem install mysql2 -- --with-ldflags=-L/usr/local/opt/openssl/lib --with-cppflags=-I/usr/local/opt/openssl/include
```

그리고 다시 아래에 명령어를 사용하여 데이터베이스를 생성합니다.

```bash
bundle exec rake db:create
```

무사히 데이터베이스가 생성되었다면 아래와 같은 메세지를 확인할 수 있습니다.

```bash
Created database 'study_rails'
Database 'study_rails' already exists
```

{% include in-feed-ads.html %}

## Model 만들기

데이터베이스를 만들었으니, 이제 데이터를 저장할 테이블을 만들어 봅시다. Rails를 사용하여 테이블을 만들기 위해서는 우선 Model을 생성할 필요가 있습니다.

아래에 명령어를 사용하여 Model을 생성합니다.

```bash
# bundle exec rails generate model post
bundle exec rails g model post
```

이렇게 Model을 생성하면 아래와 같은 파일들이 생성되는 것을 확인할 수 있습니다.

```bash
├── app
│   ├── models
│   │   ├── post.rb
├── db
│   ├── migrate
│   │   ├── 20200315053129_create_posts.rb
├── test
│   ├── fixtures
│   │   ├── posts.yml
│   ├── models
│   │   ├── post_test.rb
```

- app/models/post.rb: 실제 테이블과 연결되는 Model
- db/migrate/20200315053129_create_posts.rb: 테이블을 생성하기 위한 migratoin 파일
- test/fixtures/posts.yml: 테스트를 위한 Dummy 데이터
- test/models/post_test.rb: Model의 유닛 테스트를 위한 파일

## 테이블 생성

이제 실제 데이터를 데이터베이스에 저장하기 위해 테이블을 생성해 봅시다. 데이터베이스에 테이블을 생성하기 위해서는 Migration 파일을 수정할 필요가 있습니다.

posts 테이블을 생성하기 위해 `db/migrate/20200315053129_create_posts.rb` 파일을 열고 아래와 같이 수정합니다.

```rb
class CreatePosts < ActiveRecord::Migration[6.0]
  def change
    create_table :posts do |t|
      t.string :title
      t.text :content
      t.timestamps
    end
  end
end
```

이 posts 테이블은 기본적으로 String 타입의 `title`과 긴 문자열을 저장하기 위해 Text 타입의 `content`를 가지고 있습니다. 또한

```bash
bundle exec rake db:migrate
```

명령어를 실행하여 테이블을 생성하면 `db/schema.rb` 파일이 생성되는 것을 확인할 수 있습니다. `db/schema.rb` 파일을 열면 아래와 같은 내용을 확인할 수 있습니다.

```rb
ActiveRecord::Schema.define(version: 2020_03_15_053129) do

  create_table "posts", options: "ENGINE=InnoDB DEFAULT CHARSET=utf8", force: :cascade do |t|
    t.string "title"
    t.text "content"
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
  end

end
```

또한 데이터베이스 툴을 사용하여 실제 테이블이 생성되었는지 확인하면, 아래와 같이 잘 생성된 것을 확인할 수 있습니다.

![Ruby on Rails 테이블 생성 결과](/assets/images/category/ruby-on-rails/2020/database/result-create-table.jpg)

Migration을 사용하여 테이블을 생성하였다면, 아래에 명령어를 사용하여 생성전으로 돌아갈 수 있습니다.

```bash
bundle exec rake db:rollback
```

{% include in-feed-ads.html %}

## CRUD

지금부터는 위에서 생성한 테이블에 Rails를 사용하여 `CRUD(Create Read Update Delete)`을 해보도록 하겠습니다.

### Create

데이터를 생성하기 위해 우선 `app/controllers/home_controller.rb` 파일을 열고 아래와 같이 수정합니다.

```rb
class HomeController < ApplicationController
    ...
    def form

    end
end
```

사용자로부터 입력을 받을 화면을 표시할 `form`를 생성하였습니다. 해당 `form` Action에 관한 View를 작성하기 위해, `app/views/home/form.erb` 파일을 생성하고 아래와 같이 수정합니다.

```html
<a href="/list">Go back</a><br/>
<form action="/create" method="POST">
  <input type="hidden" name="authenticity_token" value="<%= form_authenticity_token %>" />
  <label for="title">title:</label>
  <input type="text" name="title" />
  <label for="content">content:</label>
  <input type="text" name="content" />
  <input type="submit" />
</form>
```

사용자가 `submit` 버튼을 누르면 `POST` 방식으로 `/create`라는 URL에 데이터를 보내도록 만들었습니다.

그리고 Route에 해당 URL을 등록하기 위해, `config/routes.rb` 파일을 열고 아래와 같이 수정합니다.

```rb
Rails.application.routes.draw do
  ...
  get '/form', to: 'home#form'
end
```

그리고 확인을 위해 아래에 명령어로 Rails 서버를 실행합니다.

```bash
bundle exec rails s
```

그리고 `http://127.0.0.1:3000/form`에 이동하면 아래와 같은 화면을 볼 수 있습니다.

![Ruby on Rails, CRUD 데이터 생성 form](/assets/images/category/ruby-on-rails/2020/database/form-page.jpg)

이제 실제로 데이터를 받고 처리하는 부분을 만들어 봅시다. `app/controllers/home_controller.rb` 파일을 열고 아래와 같이 수정합니다.

```rb
class HomeController < ApplicationController
    ...
    def create
        post = Post.new
        post.title = params[:title]
        post.content = params[:content]
        post.save

        redirect_to '/list'
    end

    def list

    end
end
```

위에 내용을 자세히 살펴보면,

- `post = Post.new`: 우리가 만든 POST 모델을 사용하여 새로운 데이터를 생성할 준비를 합니다.
- `post.title = params[:title]`: 새롭게 생성할 POST 데이터의 title에 사용자가 입력한 title 데이터를 대입합니다
- `post.content = params[:content]`: 새롭게 생성할 POST 데이터의 content에 사용자가 입력한 content 데이터를 대입합니다
- `post.save`: 마지막으로 해당 데이터를 저장함으로써, 데이터베이스에 데이터를 생성(create)합니다.
- `redirect_to '/list'`: 생성을 완료한 후, `/list`라는 URL로 Redirect 시킵니다.
- `def list`: 일단 Redirect할 때, 에러가 나오지 않도록 빈 Action을 추가하였습니다. 추후 이 Action에 데이터를 표시하는 처리를 하도록 할 예정입니다.

위에 내용을 보면 알 수 있듯이, `create` 액션은 redirect를 시키므로, View가 필요하지 않습니다. 하지만 추후 데이터를 표시할 `list` 액션은 View가 필요하므로, `app/views/home/list.erb` 파일을 생성해 둡니다.

이제 이렇게 추가한 Action들을 사용하기 위해 `config/routes.rb` 파일을 열고 아래와 같이 수정합니다.

```rb
Rails.application.routes.draw do
  ...
  post '/create', to: 'home#create'
  get '/list', to: 'home#list'
end
```

그리고 `http://127.0.0.1:3000/form`에 데이터를 넣고 Submit 버튼을 누르면 `http://127.0.0.1:3000/list`로 이동하는 것을 확인할 수 있습니다. 또한 데이터베이스 툴을 사용하면 아래와 같이 데이터가 잘 추가된 것을 확인할 수 있습니다.

![Ruby on Rails, CRUD 데이터 생성 확인](/assets/images/category/ruby-on-rails/2020/database/result-create-data.jpg)

{% include in-feed-ads.html %}

### Read

이제 위에서 생성한 데이터를 읽어와서(Read), 화면에 표시해 보도록 합시다. `app/controllers/home_controller.rb` 파일을 열고 아래와 같이 수정합니다.

```rb
class HomeController < ApplicationController
    ...
    def list
        @posts = Post.all
    end
end
```

위에서 `Post.all`을 사용하여 Post 테이블에 저장된 모든 데이터를 가져왔습니다. 이렇게 가져온 데이터를 View에 전달하기 위해 `@posts` 라는 인스턴스 변수에 저장하였습니다.

이렇게 저장한 데이터를 화면에 표시하기 위해, `app/views/home/list.erb` 파일을 열고 아래와 같이 수정합니다.

```html
<style>
table, th, td {
  border: 1px solid black;
}
</style>
<a href="/form">Create New Post</a>
<table>
    <thead>
        <tr>
            <th>Title</th>
            <th>Content</th>
            <th>Action</th>
        </tr>
    </thead>
    <tbody>
        <% @posts.each do |post| %>
        <tr>
            <td><%= post.title %></td>
            <td><%= post.content %></td>
            <td></td>
        </tr>
        <% end %>
    </tbody>
</table>
```

여기서 중요한 부분은 `@posts` 인스턴스 변수를 통해 가져온 데이터를 아래에 코드를 사용하여 루프를 돌면서 하나씩 `post` 변수에 할당합니다.

```rb
<% @posts.each do |post| %>
...
<% end %>
```

이렇게 할당한 `post` 변수에서 title과 content를 가져와서 화면에 표시합니다.

```html
<td><%= post.title %></td>
<td><%= post.content %></td>
```

이렇게 작성하고 다시 `http://127.0.0.1:3000/list`에 접속해 보면 아래와 같이 데이터를 잘 표시하는 것을 확인할 수 있습니다.

![Ruby on Rails 데이터베이스로부터 가져온 데이터를 화면에 표시](/assets/images/category/ruby-on-rails/2020/database/display-data.jpg)

{% include in-feed-ads.html %}

### Update

이제 위에서 생성한 데이터를 수정(Update)하는 방법에 대해서 알아보자. `app/controllers/home_controller.rb` 파일을 열고 아래와 같이 수정합니다.

```rb
class HomeController < ApplicationController
    ...
    def modify
        @post = Post.find(params[:id])
    end
end
```

위에 `modify`는 사용자에게 수정할 수 있는 Form을 제공하기 위한 액션이다. 사용자로부터 수정하고 싶은 `id`를 전달받고, 전달 받은 id로 필요한 데이터를 찾고(`Post.find`), 찾은 데이터를 View에 전달하기 위해 인스턴스 변수(`@post`)에 할당하였다.

이제 추가되어 있는 데이터를 수정하기 위한 Form을 사용자에게 제공하기 위해 `app/views/home/modify.erb` 파일을 생성하고 아래와 같이 수정한다.

```html
<a href="/list">Go back</a><br/>
<form action="/update/<%= @post.id %>" method="POST">
  <input type="hidden" name="authenticity_token" value="<%= form_authenticity_token %>" />
  <label for="title">title:</label>
  <input type="text" name="title" value="<%= @post.title %>"/>
  <label for="content">content:</label>
  <input type="text" name="content" value="<%= @post.content %>" />
  <input type="submit" />
</form>
```

데이터 생성을 위해 만든 `app/views/home/form.erb`과 거의 동일하다. 다른 부분은 Input 태그의 `value`에 Controller로부터 전달 받은 데이터를 표시하고 있다.

```html
<input type="text" name="title" value="<%= @post.title %>%"/>
<input type="text" name="content" value="<%= @post.content %>%" />
```

이렇게 생성한 페이지를 표시하기 위해 Route를 설정해 봅시다. `config/routes.rb` 파일을 열고 아래와 같이 수정합니다.

```rb
Rails.application.routes.draw do
  ...
  get '/modify/:id', to: 'home#modify'
end
```

데이터를 수정하기 위한 View인 `modify`는 URL에 파라메터를 전달하는 방식을 사용하였습니다.
이렇게 URL로 `id`를 전달받고, Controller는 전달받은 id로 데이터를 조회한 후, 화면에 표시할 예정입니다.

이제 `modify` 페이지를 열기 위한 링크를 추가하기 위해 `app/views/home/list.erb` 파일을 열고 아래와 같이 수정합니다.

```html
...
<table>
    <thead>
        ...
    </thead>
    <tbody>
        <% @posts.each do |post| %>
        <tr>
            <td><%= post.title %></td>
            <td><%= post.content %></td>
            <!-- add this line -->
            <td><a href="/modify/<%= post.id %>">modify</a></td>
        </tr>
        <% end %>
    </tbody>
</table>
```

이렇게 작성하고 다시 `http://127.0.0.1:3000/list`에 접속해 보면 아래와 같이 데이터를 잘 표시하는 것을 확인할 수 있습니다.

![Ruby on Rails 데이터를 수정하기 위한 링크 추가](/assets/images/category/ruby-on-rails/2020/database/add-modify-link.jpg)

여기서 `modify` 링크를 클릭하면 아래와 같은 화면을 확인할 수 있습니다.

![Ruby on Rails 데이터 수정 페이지](/assets/images/category/ruby-on-rails/2020/database/modify-page.jpg)

이제 데이터를 실제로 업데이트할 액션을 만들어 봅시다. 위의 `modify` 페이지에서 submit 버튼을 누르면 `/update/:id`로 이동하도록 설정하였습니다.

```html
<a href="/list">Go back</a><br/>
<form action="/update/<%= @post.id %>" method="POST">
  ...
</form>
```

그럼 이 링크에 해당하는 액션을 생성하기 위해, `app/controllers/home_controller.rb`를 열고 아래와 같이 수정합니다.

```rb
class HomeController < ApplicationController
    ...
    def update
        post = Post.find(params[:id])
        post.title = params[:title]
        post.content = params[:content]
        post.save

        redirect_to '/list'
    end
end
```

파라메터로 전달받은 `id`로 저장한 데이터를 가져오고, 사용자가 입력한 `title`과 `content` 데이터로 저장된 데이터를 갱신한 후, `post.save`를 사용하여 데이터를 업데이트했습니다.
마지막으로 데이터를 업데이트하면 `/list` 페이지로 Redirect되도록 설정하였습니다.

그럼 이 액션을 사용할 수 있도록 Route에 URL을 추가해 봅시다. `config/routes.rb` 파일을 열고 아래와 같이 수정합니다.

```rb
Rails.application.routes.draw do
  ...
  post '/update/:id', to: 'home#update'
end
```

URL을 통해 `id` 파라메터를 전달받을 예정이고, 사용자가 입력한 데이터는 POST 방식으로 전달받을 예정입니다.

이제 데이터 수정 페이지로 이동한 후,

![Ruby on Rails 데이터를 수정하기 위한 링크 추가](/assets/images/category/ruby-on-rails/2020/database/add-modify-link.jpg)

아래와 같이 기존 데이터와 다른 내용을 입력해 봅니다.

![Ruby on Rails 데이터 수정 페이지 - 데이터 수정](/assets/images/category/ruby-on-rails/2020/database/update-data.jpg)

그리고 `Submit` 버튼을 누르면 아래와 같이, 데이터가 잘 수정된 것을 확인할 수 있습니다.

![Ruby on Rails 데이터 리스트 페이지 - 데이터 수정 결과](/assets/images/category/ruby-on-rails/2020/database/update-data-result.jpg)

{% include in-feed-ads.html %}

### Delete

이제 CRUD의 마지막인 데이터 삭제(Delete)에 관해서 알아봅시다. 데이터를 삭제하는 액션을 추가하기 위해 `app/controllers/home_controller.rb` 파일을 열고 아래와 같이 수정합니다.

```rb
class HomeController < ApplicationController
    ...
    def delete
        Post.destroy(params[:id])

        redirect_to '/list'
    end
end
```

전달받은 `id`를 가지고 Post 모델의 데이터를 삭제(`Post.destroy`)하고 `/list` 페이지로 Redirect하도록 하였습니다.

이제 이 액션을 URL에 추가하기 위해 `config/routes.rb` 파일을 열고 아래와 같이 수정합니다.

```rb
Rails.application.routes.draw do
  ...
  get '/delete/:id', to: 'home#delete'
end
```

그리고 이 페이지를 호출할 수 있도록 `list` 페이지를 수정해 봅시다. `app/views/home/list.erb` 파일을 열고 아래와 같이 수정합니다.

```html
...
<table>
    <thead>
        ...
    </thead>
    <tbody>
        <% @posts.each do |post| %>
        <tr>
            <td><%= post.title %></td>
            <td><%= post.content %></td>
            <td>
                <a href="/modify/<%= post.id %>">modify</a><br/>
                <a href="/delete/<%= post.id %>">delete</a><br/>
            </td>
        </tr>
        <% end %>
    </tbody>
</table>
```

다시 `http://127.0.0.1:3000/list`에 접속하면 아래와 같이 `delete` 링크가 추가된 것을 확인할 수 있습니다.

![Ruby on Rails 데이터 리스트 페이지 - 삭제 링크](/assets/images/category/ruby-on-rails/2020/database/delete-link.jpg)

그럼 `delete` 링크를 눌러봅니다. `delete` 링크를 누르면 저장된 데이터가 잘 삭제되고, 아래와 같이 리스트 페이지에도 데이터가 표시되지 않는 것을 확인할 수 있습니다.

![Ruby on Rails 데이터 리스트 페이지 - 삭제 성공](/assets/images/category/ruby-on-rails/2020/database/deleted.jpg)

## 완료

이것으로 Ruby on Rails에서 데이터베이스를 생성하고 데이터를 CRUD(Create Read Update Delete)하는 방법에 대해서 알아보았습니다. 이제 여러분은 Ruby on Rails로 기본적인 웹 서비스를 개발할 준비가 되었습니다.

이제 웹 서비스를 만들어보면서 Rails를 깊게 공부해 보시기 바랍니다.

## 참고

이 블로그 포스트는 시리즈로 제작되었습니다. 자세한 내용은 아래에 링크를 참고하시기 바랍니다.

- [Mac에서 Ruby on Rails 시작하기]({{site.url}}/{{page.categories}}/rails-on-mac/){:target="_blank"}
- [Ruby on Rails로 생성한 프로젝트의 폴더 구조]({{site.url}}/{{page.categories}}/folder-structure/){:target="_blank"}
- [Ruby on Rails를 사용하여 새로운 웹 페이지 만들기]({{site.url}}/{{page.categories}}/create-page/){:target="_blank"}
- [Controller와 View, Route에서 데이터 교환]({{site.url}}/{{page.categories}}/data-in-controller-view-route/){:target="_blank"}
- Rails에서 DB 데이터 다루기

여기서 사용한 소스코드는 Github에서 확인할 수 있습니다.

- [Github 소스코드](https://github.com/dev-yakuza/study-rails){:rel="nofollow noreferrer" target="_blank"}
