---
layout: 'post'
permalink: '/ruby-on-rails/data-in-controller-view-route/'
paginate_path: '/ruby-on-rails/:num/data-in-controller-view-route/'
lang: 'ja'
categories: 'ruby-on-rails'
comments: true

title: 'ControllerとView、Routeとのデータ交換'
description: 'Ruby on RailsでControllerとView、そしてRouteを通じてデータを送る方法について調べてみましょう。'
image: '/assets/images/category/ruby-on-rails/2020/data-in-controller-view-route/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [変数](#変数)
- [ControllerからViewへデータ伝達](#controllerからviewへデータ伝達)
- [ViewからControllerでデータを伝達](#viewからcontrollerでデータを伝達)
  - [GET方式](#get方式)
  - [POST方式](#post方式)
- [完了](#完了)
- [参考](#参考)

</div>

## 概要

Ruby on RailsでControllerとView、そしてRoute間でデータを送る方法についてデータを送る方法について調べてみます。

このブログポストはシリーズで作成されてます。詳しく内容は下記のリンクを参考してください。

- [MacでRuby on Railsを始める]({{site.url}}/{{page.categories}}/folder-structure/){:target="_blank"}
- [Railsで作ったプロジェクトのフォルダ構造]({{site.url}}/{{page.categories}}/folder-structure/){:target="_blank"}
- [Ruby on Railsを使って新しウェブページを作る]({{site.url}}/{{page.categories}}/create-page/){:target="_blank"}
- ControllerとView、Routeとのデータ交換
- [RailsでDBを使う方法]({{site.url}}/{{page.categories}}/database/){:target="_blank"}

ここで使ったソースコードはGithubで確認できます。

- [Github ソースコード](https://github.com/dev-yakuza/study-rails){:rel="nofollow noreferrer" target="_blank"}

## 変数

データのやりとり方法を調べる前に、Rubyの変数について少し確認します。Rubyには下記のような変数たちを使えます。

| 名前 | 特徴 | 変数の使い方 |
|---|
| ローカル変数 | - 特定なエアリア（アクション）中のみで使える変数<br/>特定なエアリア（アクション）中だけ使える変数なので、特定なエアリア（アクション）中でしか参照できない。 | var = 1 |
| インスタンス変数 | - 1つのオブジェクト中のみで使える変数<br/>- 変数が参照できるところはselfが指定するオブジェクトの内部に制限する。 | @var = 1 |
| クラス変数 | - 該当するクラスの全てのオブジェクトが共有する変数<br/>- クラスメソッドを使ってアクセス可能<br/>- クラスの内部メソッドを定義する前のClassの宣言すぐ下に宣言する。 | @@var = 1 |
| グローバル変数 | - プログラムのどこでも使える変数 | $var = 1 |

{% include in-feed-ads.html %}

## ControllerからViewへデータ伝達

上でまず変数をみた理由は、ControllerからViewへデータを伝達する時、インストアんつ変数を使うのでです。データが伝達することを確認するため、`app/controllers/home_controller.rb`ファイルを開いて下記のように修正します。

```rb
class HomeController < ApplicationController
    def index
        @name = 'dev-yakuza'
    end
end
```

そして修正したアクションに該当するViewファイルを修正します。`app/views/home/index.erb`ファイルを開いて下記のように修正します。

```rb
Hello <%= @name %>!!
```

確認するため、下記のコマンドを使ってRailsサーバを起動します。

```bash
bundle exec rails s
# bundle exec rails server
```

そしてブラウザで`http://127.0.0.1:3000/`に接続したら、下記のように設定した変数が画面に表示されたことが確認できます。

![Ruby on Rails サーバー実行の結果 - ControllerとViewのデーター交換](/assets/images/category/ruby-on-rails/2020/data-in-controller-view-route/result-data-controller-view.jpg)

このようにControllerからViewへデータを伝達するためにはインスタンス変数を使えます。

## ViewからControllerでデータを伝達

ControllerからViewへデータを伝達するためには簡単にインスタンスヘンスを使えば良いでした。この理由はURLでRailsのウェブにリクエストが入ってくるとControllerがそのリクエストを処理して、Viewど表示するためです。

ViewからControllerへデータを伝達する意味は、ユーザがViewを使ってデータを入力したことです。

Viewは既にユーザのブラウザへ表示され他ので、ViewからControllerへデータを伝達する場合はユーザがデータを入力した時しかないのでです。

ViewからControllerへデータを送るためには、ウェブサービスでユーザの入力を送る方法と同じなので、GET方式とPOST方式でURLへリクエスト(Request)を送ることで送ることができます。

### GET方式

GET方式でデータを送るため、Viewファイルを修正してみましょう。`app/views/home/index.erb`ファイルを開いて、下記のように修正します。

```rb
Hello <%= @name %>!!<br/>
<a href="/?name=yakuza">Display yakuza</a>
```

そして送信されたGETパラメータを表示するためControllerを修正します。`app/controllers/home_controller.rb`ファイルを開いて下記のように修正します。

```rb
class HomeController < ApplicationController
    def index
        name = params[:name]
        @name = name ? name : 'dev-yakuza'
    end
end
```

GET方式なのでデータを送るのでaタグを使ってデータ(`name=yakuza`)を送りました。このように送信されたデータはControllerで`params`と言うヘンスを使ってデータを取得することができます。(`params[:name]`)

{% include in-feed-ads.html %}

### POST方式

POST方式でデータを送るため、Viewファイルを修正してみましょう。`app/views/home/index.erb`ファイルを開いて下記のように修正します。

```rb
Hello <%= @name %>!!<br/>
<a href="/?name=yakuza">Display yakuza</a><br/>
<form action="/" method="POST">
  <label for="name">name:</label>
  <input type="text" name="name" />
  <input type="submit" />
</form>
```

そしてブラウザをみると下記のような画面が確認できます。

![POST転送 - データを入力する前の画面](/assets/images/category/ruby-on-rails/2020/data-in-controller-view-route/before-send-data.jpg)

そして入力欄へデータを入力して`Submit`ボタンを押したら下記のようなエラーが発生します。

![POST転送 - データ送信エラー画面](/assets/images/category/ruby-on-rails/2020/data-in-controller-view-route/send-data-error.jpg)

エラーメッセージ(`Routing Error`)を見ると分かると思いますが、Route設定をしてないので、このようなエラーが発生しました。

まず、今現在のRouteファイルを確認するため、`config/routes.rb`ファイルを開いてみます。

```rb
Rails.application.routes.draw do
  get '/', to: 'home#index'
end
```

上のファイル内容でも分かると思いますが、Railsは`/`のURLで`get`方式のリクエストだけ連結されてます。したがって、POST方式のリクエストがくると、上のように`Routing Error`が発生します。

そしたら、POSTのリクエストを受けるように、Routeを修正してみます。`config/routes.rb`ファイルを開いて下記のように修正します。

```rb
Rails.application.routes.draw do
  get '/', to: 'home#index'
  post '/', to: 'home#index'
end
```

そして、また、`submit`ボタンを押すと下記のようなエラーメッセージが表示されることが見えます。

![POST転送 - データ転送エラー画面 authenticity token](/assets/images/category/ruby-on-rails/2020/data-in-controller-view-route/send-data-error-authenticity-token.jpg)

他の言語のフレームワークようにRailsも基本的セキュリティーの脆弱性を保護してます。ここでRailsは`CSRF - Cross-site request forgery`の脆弱性を保護するため、POSTデータを送信する時、特定キー(key)を一緒に送るようにしてます。

このエラーを解決するためにはPOSTデータを転送する時、`authenticity_token`と言うパラメータでRailsが提供する`form_authenticity_token`を一緒に送る必要があります。

もう一回`app/views/home/index.erb`ファイルを開いて下記のように修正します。

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

そしてまた、`http://127.0.0.1:3000/`接続して、入力欄にtestを入力してsubmitボタンを押すと下記のようにデータが上手く送信されて表示されることが確認できます。

![POST転送 - データ転送成功画面](/assets/images/category/ruby-on-rails/2020/data-in-controller-view-route/result-post-data.jpg)

## 完了

これでControllerとViewの間でデータを転送する方法についてみてみました。

ControllerからViewへデータを転送するためにはインスタンス変数を使って、ViewからControllerへデータを送信するためにはGET/POST形式でデータを転送しました。
POST方式で転送するため、RouteへPOSTのURLも追加してみました。

本格的データを使う前、準備段階でControllerとView間へデータを転送する方法をみてみました。次のブログポストではデータをDBへ保存して、保存したデータを表示する方法についてみてみます。

## 参考

このブログポストはシリーズで作成されてます。詳しく内容は下記のリンクを参考してください。

- [MacでRuby on Railsを始める]({{site.url}}/{{page.categories}}/folder-structure/){:target="_blank"}
- [Railsで作ったプロジェクトのフォルダ構造]({{site.url}}/{{page.categories}}/folder-structure/){:target="_blank"}
- [Ruby on Railsを使って新しウェブページを作る]({{site.url}}/{{page.categories}}/create-page/){:target="_blank"}
- ControllerとView、Routeとのデータ交換
- [RailsでDBを使う方法]({{site.url}}/{{page.categories}}/database/){:target="_blank"}

ここで使ったソースコードはGithubで確認できます。

- [Github ソースコード](https://github.com/dev-yakuza/study-rails){:rel="nofollow noreferrer" target="_blank"}
