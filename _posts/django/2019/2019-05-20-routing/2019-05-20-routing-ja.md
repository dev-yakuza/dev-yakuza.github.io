---
layout: 'post'
permalink: '/django/routing/'
paginate_path: '/django/:num/routing/'
lang: 'ja'
categories: 'django'
comments: true

title: 'ジャンゴ(django)のルーティング(Routing)'
description: 'ジャンゴ(django)のURL管理機能を使ってウェブサービスのルーティング(Routing)を管理してみましょう。'
image: '/assets/images/category/django/2019/routing/background.jpg'
---

## 概要
本格的ジャンゴ(django)を使ってウェブサービスを作ってみようかと思います。ウェべサービスを作るためにはユーザーが接続するURL別ページを作ってそのページをサービスする必要があります。このブログポストではジャンゴ(django)で基本的提供してるURL管理機能を使ってウェブサービスのルーティング(Routing)を管理する方法について説明します。

このブログはシリーズです。下記のリンクでシリーズの他の記事を見ることができます。

- [ジャンゴ(django)インストール]({{site.url}}/{{page.categories}}/installation/){:target="_blank"}
- [ジャンゴ(django)のプロジェクト開始]({{site.url}}/{{page.categories}}/start/){:target="_blank"}
- [ジャンゴ(django)のモデル(models)の使い方]({{site.url}}/{{page.categories}}/models/){:target="_blank"}
- [ジャンゴ(django)の管理者ページ]({{site.url}}/{{page.categories}}/admin/){:target="_blank"}
- ジャンゴ(django)のルーティング(Routing)
- [ジャンゴ(django)のORM]({{site.url}}/{{page.categories}}/orm/){:target="_blank"}
- [ジャンゴ(django)のビュー(View)]({{site.url}}/{{page.categories}}/view/){:target="_blank"}
- [ジャンゴ(django)のフォーム(Form)]({{site.url}}/{{page.categories}}/form/){:target="_blank"}
- [ジャンゴ(django)プロジェクトをヘロク(Heroku)へアップロードする]({{site.url}}/{{page.categories}}/heroku/){:target="_blank"}

また、このブログシリーズで説明したソースコードはgithubに公開されております。下記のリンクで確認できます。

- github: [https://github.com/dev-yakuza/django_exercise](https://github.com/dev-yakuza/django_exercise){:target="_blank"}

## ルーティング確認
ジャンゴ(django)は大きくプロジェクト(Project)単位とアプリケーション(Application)単位が存在します。ジャンゴ(django)プロジェクトはたくさんのアプリケーションを持つことができます。この意味はプロジェクト(Project)単位のルーティング(Routing)管理とアプリケーション(Application)単位のルーティング(Routing)管理が存在してることです。まず、ジャンゴ(django)のプロジェクト単位のルーティング(Routing)管理を確認するため`django_exercise/urls.py`ファイルを確認します。

```python
...
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
```

ファイルを開いたら上のような画面が見えます。以前のブログポスト([ジャンゴ(django)の管理者ページ]({{site.url}}/{{page.categories}}/admin/){:target="_blank"})で`http://127.0.0.1:8000/admin`のURLで管理者ページに接続しました。私たちは何も設定しなかったけど、管理者ページが見えた理由は`django_exercise/urls.py`ファイルに上のように基本的設定がされてるからです。私たちはここに私たちが新しく作ったジャンゴ(django)のアプリケーション(Application)のルーティングファイルを登録してアプリケーション(Application)別ルーティングを管理する予定です。

## ビュー生成
一旦アプリケーション(Application)のルーティング(Routing)を使ってURLに連結する`ビュー(Views)`を生成する必要があります。`blog/views.py`を開いて下記のように修正します。

```python
from django.shortcuts import render

def posts(request):
    return render(request, 'blog/posts.html', {})
```

## HTMLファイル生成
ビュー(Views)ファイルが参照してる`blog/posts.html`ファイルを生成します。`blog/templates/blog/posts.html`ファイルを生成して下記のようにコーディングします。

```html
<html>
  <header>
    <title>Hello World</title>
  </header>
  <body>
    Hello World
  </body>
</html>
```

これでルーティング(Routing)を使ってURLに連結する画面が用意できました。今からはルーティング(Routing)を使ってURLと画面を連結する方法について説明します。

{% include in-feed-ads.html %}

## アプリケーションのルーティングファイル生成
私たちが作っているブログウェブサイトに該当するジャンゴ(django)のアプリケーション(Application)のためルーティング(Routing)ファイルを作る必要があります。`blog/urls.py`ファイルを生成して下記の内容を追加します。

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
]
```


## アプリケーションのルーティング登録
上で生成したジャンゴ(django)のアプリケーション(Application)のルーティング(Routing)ファイルである`blog/urls.py`をジャンゴ(django)のプロジェクト(Project)に登録する必要があります。`django_exercise/urls.py`を開いて下記のように修正します。

```python
from django.contrib import admin
from django.urls import path, include # <<< here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')), # <<< here
]
```

## 確認
下記のジャンゴ(django)のコマンドを使ってテストサーバーを起動した後、`http://127.0.0.1:8000/`に接続して、私たちが設定したルーティング(Routing)が動いてるか確認します。

```bash
# source venv/bin/activate
# pip install -r requirements.txt
# cd django_exercise
python manage.py runserver
```

ブラウザで`Hello World`が表示されることが確認できます。

## 完了
これでジャンゴ(django)のルーティング(Routing)について見てみました。今からはルーティング(Routing)の機能を使って自分が作った画面とURLを連結することができます。