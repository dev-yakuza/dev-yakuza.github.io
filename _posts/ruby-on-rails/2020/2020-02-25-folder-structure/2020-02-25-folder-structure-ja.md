---
layout: 'post'
permalink: '/ruby-on-rails/folder-structure/'
paginate_path: '/ruby-on-rails/:num/folder-structure/'
lang: 'ja'
categories: 'ruby-on-rails'
comments: true

title: 'Railsで作ったプロジェクトのフォルダ構造'
description: 'Ruby on Railsで生成したプロジェクトのフォルダの構造を確認してみましょう。'
image: '/assets/images/category/ruby-on-rails/2020/folder-structure/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [プロジェクトの構造](#プロジェクトの構造)
- [Controller関連](#controller関連)
- [View関連](#view関連)
- [URL関連](#url関連)
- [完了](#完了)
- [参考](#参考)

</div>

## 概要

今回のブログではRuby on RailsをインストールしてRuby on Railsを使って新しプロジェクトを生成する方法について確認しました。

- [MacでRuby on Railsを始める]({{site.url}}/{{page.categories}}/rails-on-mac/){:target="_blank"}

今回のブログポストでは、新しく生成したRailsのプロジェクトの構造を把握してみようかと思います。

このブログポストはシリーズで作成されてます。詳しく内容は下記のリンクを参考してください。

- [MacでRuby on Railsを始める]({{site.url}}/{{page.categories}}/folder-structure/){:target="_blank"}
- Railsで作ったプロジェクトのフォルダ構造
- [Ruby on Railsを使って新しウェブページを作る]({{site.url}}/{{page.categories}}/create-page/){:target="_blank"}
- [ControllerとView、Routeとのデータ交換]({{site.url}}/{{page.categories}}/data-in-controller-view-route/){:target="_blank"}
- [RailsでDBを使う方法]({{site.url}}/{{page.categories}}/database/){:target="_blank"}

ここで使ったソースコードはGithubで確認できます。

- [Github ソースコード](https://github.com/dev-yakuza/study-rails){:rel="nofollow noreferrer" target="_blank"}

## プロジェクトの構造

Ruby on Railsでプロジェクトを生成すると、下記のようなプロジェクトが生成されます。下記の内容は生成されたプロジェクトのフォルダ中で重要な部分だけまとめました。

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

## Controller関連

Ruby on Railsも他のフレームワークと同じように`MVCパタン`(Model-View-Controllerパタン)を使ってます。したがって、Ruby on Railsを使ってModel, View, Controllerを作ることでウェブサービスを作ることができます。

Ruby on RailsでControllerを生成して、下記のようなフォルダ、ファイルを使うことになります。

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

次のブログポストで紹介しますが、RailsのコマンドでConrollerを生成すると上のようなファイルが生成されます。ここではhome_controllerを生成した例題になります。

Controllerを生成する方法については下記のリンクを参考してください。

- [Ruby on Railsを使って新しウェブページを作る - Controller]({{site.url}}/{{page.categories}}/create-page/#controller){:target="_blank"}

## View関連

Ruby on Railsで画面を表示するためにはViewを下記のフォルダに生成することになります。

```bash
├── app
│   ├── views
│   │   ├── home
```

ここでは上と同じようにhome_controllerを生成した後のフォルダの構造です。皆さんはまだ、homeフォルダが見えないと思います。home_controllerをRailsのコマンドで生成すると、そこに必要なViewを保管するhomeフォルダが自動で生成されます。

ControllerとViewを生成する方法については下記のリンクを参考してください。

- [Ruby on Railsを使って新しウェブページを作る - View]({{site.url}}/{{page.categories}}/create-page/#view){:target="_blank"}

## URL関連

RailsはRubyと言う言語を使ってウェブサービスを作るためのフレームワークとなります。ウェブサービスを作るためのフレームワークなので、当たり前ですが、URLを管理する機能を持っています。

RailsでURLはconfigフォルダ中のroutes.rbファイルで管理します。

```bash
├── config
│   ├── routes.rb
```

Railsへ新しURLを追加する方法については下記のリンクを参考してください。

- [Ruby on Railsを使って新しウェブページを作る - Route]({{site.url}}/{{page.categories}}/create-page/#routes){:target="_blank"}

{% include in-feed-ads.html %}

## Database

Ruby on RailsでDataを使うためのファイルたちは下記のようです。

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

- config/database.yml: Databaseの連結情報の設定ファイル
- app/models/post.rb: 実際テーブルと連動するModel
- db/migrate/20200313092804_create_posts.rb: テーブルを生成するためのmigratoinファイル
- test/fixtures/posts.yml: テストのためのDummyデータ
- test/models/post_test.rb: Modelのユニットテストするためのファイル

データベースを設定して、データを使う方法については下記のブログを参考してください。

- [RailsでDBを使う方法]({{site.url}}/{{page.categories}}/data){:target="_blank"}

## 完了

これでRuby on Railsのフォルダの構造をみてみました。今後はウェブサービスを作成するためController, View,そしてModelを生成する方法について紹介します。

## 参考

このブログポストはシリーズで作成されてます。詳しく内容は下記のリンクを参考してください。

- [MacでRuby on Railsを始める]({{site.url}}/{{page.categories}}/folder-structure/){:target="_blank"}
- Railsで作ったプロジェクトのフォルダ構造
- [Ruby on Railsを使って新しウェブページを作る]({{site.url}}/{{page.categories}}/create-page/){:target="_blank"}
- [ControllerとView、Routeとのデータ交換]({{site.url}}/{{page.categories}}/data-in-controller-view-route/){:target="_blank"}
- [RailsでDBを使う方法]({{site.url}}/{{page.categories}}/database/){:target="_blank"}

ここで使ったソースコードはGithubで確認できます。

- [Github ソースコード](https://github.com/dev-yakuza/study-rails){:rel="nofollow noreferrer" target="_blank"}
