---
layout: 'post'
permalink: '/django/response-model-to-json/'
paginate_path: '/django/:num/response-model-to-json/'
lang: 'ja'
categories: 'django'
comments: true

title: 'ジャンゴ(django)のモデル(Models)をJSONタイプでレスポンス(Response)する'
description: 'ジャンゴ(django)のプロジェクトでAPIを使って情報をやりとりする時、モデル(Models)から貰った情報(QuerySet)をそのままJSONでレスポンス(Response)する方法について説明します。'
image: '/assets/images/category/django/2019/response-model-to-json/background.jpg'
---

## 概要
ジャンゴ(django)でAPIサーバーを開発する時、モデル(Models)から直接持ってきた情報(QuerySet)をそのままJSONで返したい時があります。このブログポストではジャンゴ(django)を使ってモデル(Models)から持ってきた情報(QuerySet)をそのままJSONタイプで返す方法について説明します。

このブログで紹介するソースコードはGithubに公開されております。下記のリンクで確認してください。

- github: [https://github.com/dev-yakuza/django_response_model_to_json](https://github.com/dev-yakuza/django_response_model_to_json){:target="_blank"}

## ジャンゴ(django)のプロジェクトの準備
以前のブログシリーズでジャンゴ(django)のプロジェクトを使う方法について説明しました。ジャンゴ(django)を使ってプロジェクトを構成する方法について詳しく内容は下記のリンクを確認してください。

- [ジャンゴ(django)インストール]({{site.url}}/{{page.categories}}/installation/){:target="_blank"}
- [ジャンゴ(django)のプロジェクト開始]({{site.url}}/{{page.categories}}/start/){:target="_blank"}
- [ジャンゴ(django)のモデル(models)の使い方]({{site.url}}/{{page.categories}}/models/){:target="_blank"}
- [ジャンゴ(django)の管理者ページ]({{site.url}}/{{page.categories}}/admin/){:target="_blank"}
- [ジャンゴ(django)のルーティング(Routing)]({{site.url}}/{{page.categories}}/routing/){:target="_blank"}
- [ジャンゴ(django)のORM]({{site.url}}/{{page.categories}}/orm/){:target="_blank"}
- [ジャンゴ(django)のビュー(View)]({{site.url}}/{{page.categories}}/view/){:target="_blank"}
- [ジャンゴ(django)のフォーム(Form)]({{site.url}}/{{page.categories}}/form/){:target="_blank"}
- [ジャンゴ(django)プロジェクトをヘロク(Heroku)へアップロードする]({{site.url}}/{{page.categories}}/heroku/){:target="_blank"}

このブログではジャンゴ(django)のインストールやプロジェクトの設定などについては説明しません。簡単にプロジェクトが進めるレベルで説明します。

下記のコマンドでジャンゴ(django)のプロジェクトを生成します。

```bash
django-admin startproject django_response_model_to_json
```

下記のブログを参考してデーターベース連動やテーブルを作ります。

- [ジャンゴ(django)のプロジェクト開始]({{site.url}}/{{page.categories}}/start/){:target="_blank"}

データーベースの連動が終わったら下記のコマンドで管理者(`superuser`)を作ります。

```bash
python manage.py createsuperuser
```

下記のブログを参考して`Blog`ジャンゴ(django)のアプリと`Post`モデル(Model)を生成します。

- [ジャンゴ(django)のモデル(models)の使い方]({{site.url}}/{{page.categories}}/models/){:target="_blank"}

そして下記のブログを参考してテストデーターを追加します。

- [ジャンゴ(django)のプロジェクトでマスターデーターを入れる方法]({{site.url}}/{{page.categories}}/data-seed/){:target="_blank"}

{% include in-feed-ads.html %}

## URL作成
テストデーターを持てくるためのURLを生成します。下記のリンクにURLを作る方法について詳しく説明がありますので参考してください。

- [ジャンゴ(django)のルーティング(Routing)]({{site.url}}/{{page.categories}}/routing/){:target="_blank"}

URLを作成するため`django_response_model_to_json/urls.py`を開いて下記のように修正します。

```python
from django.contrib import admin
from django.urls import path
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
```

そしてBlogアプリにURLを追加するため`blog/urls.py`を生成して下記のように修正します。

```python
from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.posts, name='posts'),
]
```

## ビュー(View)作成
モデル(Models)から持てきたデーター(QuerySet)をJSONタイプに変換するためビュー(View)を作成します。ジャンゴ(django)のビュー(View)に関しては下記のブログを参考してください。

- [ジャンゴ(django)のビュー(View)]({{site.url}}/{{page.categories}}/view/){:target="_blank"}

ビュー(View)を作るため`blog/views.py`を開いて下記のように修正します。

```python
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from .models import Post


def posts(request):
    posts = Post.objects.filter(published_at__isnull=False).order_by('-published_at')
    post_list = serializers.serialize('json', posts)
    return HttpResponse(post_list, content_type="text/json-comment-filtered")
```

- `from django.core import serializers`: モデル(Models)をJSONタイプでデーターを直列化捨ためserializersを読んできます。
- `from django.http import HttpResponse`: JSONでデーターをレスポンス(Response)するためHttpResponseを使う予定です。
- `posts = Post.objects.filter(published_at__isnull=False).order_by('-published_at')`: Postモデル(Models)を使ってデーターを持てきます。
- `post_list = serializers.serialize('json', posts)`: 持てきたデーター(QuerySet)をJSONタイプの`文字列`で変換します。
- `return HttpResponse(post_list, content_type="text/json-comment-filtered")`: post_listがJSONタイプの`文字列`なので`(")`を消してJSONをレスポンスします。

## 確認
今まで作った内容を確認するためジャンゴ(django)のテストサーバーを実行します。

```bash
python manage.py runserver
```

そしてPostmanで当該URL(`http://localhost:8000/posts/`)をGETで読んだら下記のようにデーターをちゃんと持ってくることが確認できます。

![ジャンゴ(django)のモデル(Models)をJSONでレスポンス - Postmanを使ってデーター確認](/assets/images/category/django/2019/response-model-to-json/check-api-with-postman.jpg)

