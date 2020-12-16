---
layout: 'post'
permalink: '/ruby-on-rails/database/'
paginate_path: '/ruby-on-rails/:num/database/'
lang: 'ja'
categories: 'ruby-on-rails'
comments: true

title: 'RailsでDBを使う方法'
description: 'Ruby on Railsを使ってDBへデータをCRUD(Create Read Update Delete)する方法について共有します。'
image: '/assets/images/category/ruby-on-rails/2020/database/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [DB設定](#db設定)
- [mysql2](#mysql2)
- [Modelを作る](#modelを作る)
- [テーブル生成](#テーブル生成)
- [CRUD](#crud)
  - [Create](#create)
  - [Read](#read)
  - [Update](#update)
  - [Delete](#delete)
- [完了](#完了)
- [参考](#参考)

</div>

## 概要

このブログポストではRailsを使って本格的データを使ってみようかと思います。本格的データを使うためDBを設定して、DBテーブ路を生成する予定です。
このように生成されたDBへRailsを使ってCRUD(Create Read Update Delete)をして、Railsでデータを使う方法を理解してみようかと思います。

このブログポストはシリーズで作成されてます。詳しく内容は下記のリンクを参考してください。

- [MacでRuby on Railsを始める]({{site.url}}/{{page.categories}}/folder-structure/){:target="_blank"}
- [Railsで作ったプロジェクトのフォルダ構造]({{site.url}}/{{page.categories}}/folder-structure/){:target="_blank"}
- [Ruby on Railsを使って新しウェブページを作る]({{site.url}}/{{page.categories}}/create-page/){:target="_blank"}
- [ControllerとView、Routeとのデータ交換]({{site.url}}/{{page.categories}}/data-in-controller-view-route/){:target="_blank"}
- RailsでDBを使う方法

ここで使ったソースコードはGithubで確認できます。

- [Github ソースコード](https://github.com/dev-yakuza/study-rails){:rel="nofollow noreferrer" target="_blank"}

{% include in-feed-ads.html %}

## DB設定

まず、DBを使うためにはRailsへDBに関する設定をする必要があります。ここにはmysqlを設定する方法だけ紹介します。
mysqlは既にローカルにインストールされたと思って進めます。

RailsでDBの設定は`config/database.yml`ファイルが担当してます。`config/database.yml`ファイルを開いたら、下記のような内容が確認されます。

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

Railsは基本的sqlite3を設定しております。ここではmysqlを使う予定なので、上の設定を下記のように修正します。

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

上の設定でdatabase, username, passwordを自分のローカル環境に合わせて修正します。

上の設定では全ての設定を`default`へ作成して、他の環境ではdefaultにある内容を参考するようにしました。特定な環境に必要な情報を修正したい場合は、下記のように修正することができます。

```yml
production:
  <<: *default
  username: root
  password: XXXX
```

上のように修正すると、production環境時だけ、ここに書いてるusernameとpasswordを使うようになります。

DBの設定に使えるパラメーターは下記のようです。

| 名前     | 説明                                                        |
| -------- | ----------------------------------------------------------- |
| adapter  | 接続するデータベースの種類(sqlite3, mysql2, postgresqlなど) |
| database | データベースの名前(sqliteはデータベースのファイル位置)      |
| host     | ホスト名前やIPアドレス                                      |
| port     | ポート番号                                                  |
| pool     | 確保する接続プール                                          |
| timeout  | 接続タイムアウト(ミリセコンド)                              |
| encoding | 使う文字コード                                              |
| username | ユーザ名                                                    |
| password | パスワード                                                  |
| socket   | ソケット(/tmp/mysql.sock)                                   |

{% include in-feed-ads.html %}

## mysql2

RailsでMysqlに接続するためには`mysql2`と言うgemが必要です。下記のコマンドで`mysql2`をインストールします。

```bash
bundle add mysql2
```

インストールが完了されたら、下記のコマンドでデータベースを生成します。

```bash
bundle exec rake db:create
```

もし、下記のようなエラーメッセージが表示されて、データベースが生成されない場合、

```bash
warning: Using the last argument as keyword parameters is deprecated; maybe ** should be added to the call
The called method `initialize' is defined here
[BUG] Segmentation fault at 0x0000000000000000
...
```

下記のコマンドを使ってmysql2をインストールします。

```bash
gem install mysql2 -- --with-ldflags=-L/usr/local/opt/openssl/lib --with-cppflags=-I/usr/local/opt/openssl/include
```

そして、まだ、下記のコマンドを使ってデータベースを生成します。

```bash
bundle exec rake db:create
```

問題なくデータベースが生成されたら下記のようなメッセージを確認することができます。

```bash
Created database 'study_rails'
Database 'study_rails' already exists
```

{% include in-feed-ads.html %}

## Modelを作る

データベースを作りましたので、データを保存するテーブルを作ってみましょう。Railsを使ってテーブルを作るためには、まず、Modelを生成する必要があります。

下記のコマンドを使ってModelを生成します。

```bash
# bundle exec rails generate model post
bundle exec rails g model post
```

このようにModelを生成すると、下記のようなファイルが生成されることが確認できます。

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

- app/models/post.rb: 実際テーブルと連結されるModel
- db/migrate/20200315053129_create_posts.rb: テーブルを生成するためのmigratoinファイル
- test/fixtures/posts.yml: テストをするためDummyデータ
- test/models/post_test.rb: Modelのユニットテストをするためのファイル

## テーブル生成

実際データをデータベースへ保存するためテーブルを生成してみましょう。データベースへテーブルを生成するため、Migrationファイルを修正する必要があります。

postsテーブルを生成するため、`db/migrate/20200315053129_create_posts.rb`ファイルを開いて下記のように修正します。

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

このpostsテーブルは基本的Stringタイプの`title`と長い文字を保存するためTextタイプの`content`を持ってます。また、

```bash
bundle exec rake db:migrate
```

コマンドを実行するとテーブルが生成されて`db/schema.rb`ファイルが生成されることが確認できます。`db/schema.rb`ファイルを開いてみると下記のような内容が確認できます。

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

また、データベースツールを使って実際テーブルが生成されたか、確認すると、下記のようにテーブルができてることが確認できます。

![Ruby on Rails テーブル生成結果](/assets/images/category/ruby-on-rails/2020/database/result-create-table.jpg)

Migrationを使ってテーブル生成した後、下記のコマンドでテーブル生成前に戻ることができます。

```bash
bundle exec rake db:rollback
```

{% include in-feed-ads.html %}

## CRUD

今から上で作ったテーブルへRailsを使って`CRUD(Create Read Update Delete)`をしてみます。

### Create

データを生成するため、まず`app/controllers/home_controller.rb`ファイルを開いて、下記のように修正します。

```rb
class HomeController < ApplicationController
    ...
    def form

    end
end
```

ユーザから入力して貰う画面を表示する`form`を生成しました。当該`form`のActionに関するViewを作成するため、`app/views/home/form.erb`ファイルを生成して下記のように修正します。

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

ユーザが`submit`ボタンを押すと、`POST`で`/create`と言うURLへデータを送るように作りました。

そしてRouteへ当該URLを登録するため、`config/routes.rb`ファイルを開いて下記のように修正します。

```rb
Rails.application.routes.draw do
  ...
  get '/form', to: 'home#form'
end
```

そして確認のため、下記のコマンドを実行してRailsサーバを起動します。

```bash
bundle exec rails s
```

実行が終わったら、`http://127.0.0.1:3000/form`へ移動したら、下記のような画面をみることができます。

![Ruby on Rails, CRUD 데이터 생성 form](/assets/images/category/ruby-on-rails/2020/database/form-page.jpg)

今から実際データを貰って処理する部分を作ってみましょう。`app/controllers/home_controller.rb`ファイルを開いて下記のように修正します。

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

上の内容を詳しくみると、

- `post = Post.new`: 上で作ったPOSTモデルを使って新データを生成する準備をします。
- `post.title = params[:title]`: 新く生成するPOSTデータのtitleへユーザが入力したtitleを入れます。
- `post.content = params[:content]`: 新く生成するPOSTデータのcontentへユーザが入力したcontentデータを入力します。
- `post.save`: 最後に当該データを保存することで、データベースへデータを生成(create)します。
- `redirect_to '/list'`: 生成が終わったら、`/list`と言うURLへRedirectさせます。
- `def list`: 一旦Redirectする時、エラーが出ないようにするため、空のActionを追加します。今後、このActionへデータを表示する処理を入れる予定です。

上の内容をみるとわかりますが、`create`アクションはredirectさせますので、Viewが要らないです。しかし、後でデータを表示する`list`アクションはViewが必要なので、`app/views/home/list.erb`ファイルを生成しておきます。

このように追加したActionを使うため`config/routes.rb`ファイルを開いて下記のように修正します。

```rb
Rails.application.routes.draw do
  ...
  post '/create', to: 'home#create'
  get '/list', to: 'home#list'
end
```

そして`http://127.0.0.1:3000/form`へデータを入れてSubmitボタンを押して`http://127.0.0.1:3000/list`へ移動することが確認できます。また、データベースツールを使ってみると、下記のようにデータがうまく追加されたことが確認できます。

![Ruby on Rails, CRUDデータ生成確認](/assets/images/category/ruby-on-rails/2020/database/result-create-data.jpg)

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

上で`Post.all`を使ってPostテーブルへ保存した全てのデータを取ってきました。このように取ってきたデータをViewへ伝達するため`@posts`と言うインスタンス変数へ保存しました。

このように保存したデータを画面に表示するため、`app/views/home/list.erb`ファイルを開いて下記のように修正します。

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

ここで重要な部分は`@posts`のインスタンス変数を通じて持ってきたデータを下記のコードを使ってループしながら、1つづつ`post`の変数へ入れます。

```rb
<% @posts.each do |post| %>
...
<% end %>
```

このように割り当てられた`post`変数からtitleとcontentを取ってきて画面に表示します。

```html
<td><%= post.title %></td>
<td><%= post.content %></td>
```

このように作成して、また、`http://127.0.0.1:3000/list`へ接続してみると、下記のようにデータが表示されることが確認できます。

![Ruby on Rails データベースから取ってきたデータを画面へ表示](/assets/images/category/ruby-on-rails/2020/database/display-data.jpg)

{% include in-feed-ads.html %}

### Update

今から上で生成したデータを修正(Update)する方法について説明します。`app/controllers/home_controller.rb`ファイルを開いて下記のように修正します。

```rb
class HomeController < ApplicationController
    ...
    def modify
        @post = Post.find(params[:id])
    end
end
```

上で`modify`はユーザへ修正するFormを提供するためのアクション(Action)です。ユーザから修正したいデータの`id`を受けて、受けて貰ったidで必要なデータを探して(`Post.find`)、探したデータをViewへ伝達するためインスタンス変数(`@post`)へ保存しました。

次は、追加されたデータを修正するためのFormをユーザへ提供するため`app/views/home/modify.erb`ファイルを生成して下記のように修正します。

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

データを生成するため作った`app/views/home/form.erb`と似てます。違うところはInputタグの`value`へControllerから伝達して貰ったデータを表示してます。

```html
<input type="text" name="title" value="<%= @post.title %>%"/>
<input type="text" name="content" value="<%= @post.content %>%" />
```

このように生成したページを表示するためRouteを設定してみましょう。`config/routes.rb`ファイルを開いて下記のように修正します。

```rb
Rails.application.routes.draw do
  ...
  get '/modify/:id', to: 'home#modify'
end
```

データを修正するためのViewである`modify`はURLへパラメーターを伝達する方法を使ってます。
このようにURLで`id`をもらって、Controllerは受けったidをデータを探して、画面へ表示する予定です。

次は`modify`ページを開くためのリンクを追加するため`app/views/home/list.erb`ファイルを開いて下記のように修正します。

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

このように作成して、また`http://127.0.0.1:3000/list`へ接続してみると、下記のようにデータが上手く表示されることが確認できます。

![Ruby on Railsデータを修正するためのリンク追加](/assets/images/category/ruby-on-rails/2020/database/add-modify-link.jpg)

ここで`modify`リンクを押したら、下記のような画面を確認することができます。

![Ruby on Railsデータを修正するページ](/assets/images/category/ruby-on-rails/2020/database/modify-page.jpg)

次はデータを実際更新するアクション(Action)を作ってみましょう。上の`modify`ページでsubmitボタンを押すと、`/update/:id`へ遷移するように作りました。

```html
<a href="/list">Go back</a><br/>
<form action="/update/<%= @post.id %>" method="POST">
  ...
</form>
```

このリンクに該当するアクションを作るため、`app/controllers/home_controller.rb`を開いて下記のように修正します。

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

パラメーターでもらった`id`で保存したデータを取ってきて、ユーザが入力した`title`と`content`データで保存したデータを更新した後、`post.save`を使ってデータを更新しました。
最後にデータを更新したら、`/list`ページへRedirectするように設定しました。

次はこのアクションを使えるようにするためRouteへURLを追加してみましょう。`config/routes.rb`ファイルを開いて下記のように修正します。

```rb
Rails.application.routes.draw do
  ...
  post '/update/:id', to: 'home#update'
end
```

URLを通じて`id`パラメーターを受ける予定で、ユーザが入力したデータはPOST方式で貰う予定です。

この後、データの修正ページへ移動した後、

![Ruby on Railsデータを修正するためリンク追加](/assets/images/category/ruby-on-rails/2020/database/add-modify-link.jpg)

下記のように既存データとは違う内容を入力してみます。

![Ruby on Rails データ修正ページ - データ修正](/assets/images/category/ruby-on-rails/2020/database/update-data.jpg)

そして`Submit`ボタンを押すと下記のように、データが上手く更新されたことが確認できます。

![Ruby on Railsデータリストページ - データ修正結果](/assets/images/category/ruby-on-rails/2020/database/update-data-result.jpg)

{% include in-feed-ads.html %}

### Delete

次はCRUDの最後であるデータ削除(Delete)に関して説明します。データを削除するアクションを追加するため`app/controllers/home_controller.rb`ファイルを開いて下記のように修正します。

```rb
class HomeController < ApplicationController
    ...
    def delete
        Post.destroy(params[:id])

        redirect_to '/list'
    end
end
```

パラメーターでもらった`id`でPostモデルのデータを削除(`Post.destroy`)して`/list`ページへRedirectするようにしました。

次はこのアクションをURLへ追加するため`config/routes.rb`ファイルを開いて下記のように修正します。

```rb
Rails.application.routes.draw do
  ...
  get '/delete/:id', to: 'home#delete'
end
```

そしてこのページを呼び出せるように`list`ページを修正します。`app/views/home/list.erb`ファイルを開いて下記のように修正します。

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

また`http://127.0.0.1:3000/list`へ接続したら、下記のように`delete`リンクが追加されたことが確認できます。

![Ruby on Railsデータリストページ - 削除リンク](/assets/images/category/ruby-on-rails/2020/database/delete-link.jpg)

そしたら、`delete`リンクを押してみましょう。`delete`リンクを押すと、保存されたデータが上手く削除されて、下記のようにリストページにもデータが表示されないことが確認できます。

![Ruby on Railsデータリストページ削除成功](/assets/images/category/ruby-on-rails/2020/database/deleted.jpg)

## 完了

これで、Ruby on Railsでデータベースを生成してデータをCRUD(Create Read Update Delete)する方法についてみてみました。皆さんはもうRuby on Railsで基本的なウェブサービスを開発する準備ができました。

今後はウェブサービスを作って見ながら、Railsをもっと深く勉強してください。

## 参考

このブログポストはシリーズで作成されてます。詳しく内容は下記のリンクを参考してください。

- [MacでRuby on Railsを始める]({{site.url}}/{{page.categories}}/folder-structure/){:target="_blank"}
- [Railsで作ったプロジェクトのフォルダ構造]({{site.url}}/{{page.categories}}/folder-structure/){:target="_blank"}
- [Ruby on Railsを使って新しウェブページを作る]({{site.url}}/{{page.categories}}/create-page/){:target="_blank"}
- [ControllerとView、Routeとのデータ交換]({{site.url}}/{{page.categories}}/data-in-controller-view-route/){:target="_blank"}
- RailsでDBを使う方法

ここで使ったソースコードはGithubで確認できます。

- [Github ソースコード](https://github.com/dev-yakuza/study-rails){:rel="nofollow noreferrer" target="_blank"}
