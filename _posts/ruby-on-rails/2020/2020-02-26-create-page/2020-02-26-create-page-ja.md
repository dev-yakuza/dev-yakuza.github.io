---
layout: 'post'
permalink: '/ruby-on-rails/create-page/'
paginate_path: '/ruby-on-rails/:num/create-page/'
lang: 'ja'
categories: 'ruby-on-rails'
comments: true

title: 'Ruby on Railsを使って新しウェブページを作る'
description: 'Ruby on Railsを使って新しウェブページを作る方法について説明します。'
image: '/assets/images/category/ruby-on-rails/2020/create-page/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [Controller](#controller)
  - [Controller生成エラー](#controller生成エラー)
  - [Controller生成ファイル](#controller生成ファイル)
  - [ControllerへActionを追加](#controllerへactionを追加)
- [View](#view)
  - [ControllerとViewを連結](#controllerとviewを連結)
- [Routes](#routes)
- [確認](#確認)
- [完了](#完了)
- [参考](#参考)

</div>

## 概要

Ruby on Railsを使って新しウェブページを生成する方法についてみてみようかと思います。

このブログポストはシリーズで作成されてます。詳しく内容は下記のリンクを参考してください。

- [MacでRuby on Railsを始める]({{site.url}}/{{page.categories}}/folder-structure/){:target="_blank"}
- [Railsで作ったプロジェクトのフォルダ構造]({{site.url}}/{{page.categories}}/folder-structure/){:target="_blank"}
- Ruby on Railsを使って新しウェブページを作る
- [ControllerとView、Routeとのデータ交換]({{site.url}}/{{page.categories}}/data-in-controller-view-route/){:target="_blank"}
- [RailsでDBを使う方法]({{site.url}}/{{page.categories}}/database/){:target="_blank"}

ここで使ったソースコードはGithubで確認できます。

- [Github ソースコード](https://github.com/dev-yakuza/study-rails){:rel="nofollow noreferrer" target="_blank"}

Ruby on Railsも他の言語のフレームワークと同じに`MVCパタン`(Model-View-Controllerパタン)を持っています。したがって、新しウェブページを作成するためには基本的`View`と`Controller`を作成する必要があります。

## Controller

まず、下記のコマンドを使ってControllerを生成します。

```bash
# cd StudyRails
bundle exec rails generate controller home
```

generateのコマンドを下記のように簡単に`g`で使うこともできます。

```bash
bundle exec rails g controller home
```

### Controller生成エラー

上のコマンドを実行しても、何も動作しない場合、実行したコマンドを停止して、下記のコマンドを実行します。

```bash
rake app:update:bin
```

そしたら下記のようなメッセージを確認することができます。`Y`を入力して進めます。

```bash
/StudyRails/bin/rails? (enter "h" for help) [Ynaqdhm]
/StudyRails/bin/rake? (enter "h" for help) [Ynaqdhm]
```

そして、まだ、下記のコマンドでControllerを生成します。

```bash
# cd StudyRails
bundle exec rails generate controller home
```

また、下記のようなメッセージが表示されて、Controllerが生成されない時は、

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

上の説明にもありますが、下記のコマンドを実行します。

```bash
yarn install --check-files
```

そして、また、下記のコマンドを使ってControllerを生成します。

```bash
# cd StudyRails
bundle exec rails generate controller home
# bundle exec rails g controller home
```

問題なく生成されたら、下記のようなメッセージが確認されます。

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

### Controller生成ファイル

RailsのコマンドでControllerを生成した場合は下記のようなファイルが生成されます。

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

このようなファイル中で、`app/controllers/home_controller.rb`を使って、ほとんどの処理を作ります。

### ControllerへActionを追加

上ので生成された`app/controllers/home_controller.rb`ファイルを開いて下記のように修正します。

```rb
class HomeController < ApplicationController
    def index
    end
end
```

ここではhome_controllerへindex関数を追加しました。RailsではControllerへ追加した関数をActionと表現します。

## View

Railsのコマンドを使ってControllerを生成したら、下記のようなフォルダが確認できます。

```bash
├── app
│   ├── views
│   │   ├── home
```

Railsのコマンドで生成されたhomeフォルダへhome_controller.rbに必要なViewファイルを生成して連結する予定です。

homeフォルダの中へ`index.erb`ファイルを生成して下記のように修正します。

```rb
Hello Rails!!
```

### ControllerとViewを連結

ControllerとViewを連結するためには特にすることがないです。ControllerのAction名(関数名 - `def index`)とViewファイルのファイル名(`index.erb`)を一致させると、Railsは他に設定しなくても、自動的に該当するViewファイルを連結します。

{% include in-feed-ads.html %}

## Routes

Railsで`Routes`はURLとControllerを連結する役割をします。上で作ったControllerを連結するため`config/routes.rb`ファイルを開いて下記のように修正します。

```rb
Rails.application.routes.draw do
  get '/', to: 'home#index'
end
```

上のように修正すると、`/`のURLに`GET`のリクエストが来ると、`home_controller`の`index`アクション（関数）が実行されます。このように実行されあたindexアクションは同じ名前である`home/index.erb`ファイルを探して画面に表示します。

## 確認

これで新しページを表示する準備は終わりました。下記のコマンドでRailsサーバーを起動します。

```bash
rails server
```

または、簡単に下記のコマンドを使うこともできます。

```bash
rails s
```

そしてブラウザを開いて`http://127.0.0.1:3000/`へ接続すると下記のように私たちが作った画面が確認されます。

![Ruby on Railsサーバー実行結果](/assets/images/category/ruby-on-rails/2020/create-page/rails-server.jpg)

## 完了

これでRuby on Railsを使って新しページを生成する方法について確認しました。

Controllerを生成してController中にアクション（関数）を作って、アクション名（関数名）と同じ名前のViewファイルを作って、最後にRouteへURLとControllerを連結することで新しいページを表示することができました。

じゃ、一旦ページを作ることはできましたので、次はデータを使う方法について調べてみましょう！

## 参考

このブログポストはシリーズで作成されてます。詳しく内容は下記のリンクを参考してください。

- [MacでRuby on Railsを始める]({{site.url}}/{{page.categories}}/folder-structure/){:target="_blank"}
- [Railsで作ったプロジェクトのフォルダ構造]({{site.url}}/{{page.categories}}/folder-structure/){:target="_blank"}
- Ruby on Railsを使って新しウェブページを作る
- [ControllerとView、Routeとのデータ交換]({{site.url}}/{{page.categories}}/data-in-controller-view-route/){:target="_blank"}
- [RailsでDBを使う方法]({{site.url}}/{{page.categories}}/database/){:target="_blank"}

ここで使ったソースコードはGithubで確認できます。

- [Github ソースコード](https://github.com/dev-yakuza/study-rails){:rel="nofollow noreferrer" target="_blank"}
