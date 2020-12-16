---
layout: 'post'
permalink: '/django/data-seed/'
paginate_path: '/django/:num/data-seed/'
lang: 'ja'
categories: 'django'
comments: true

title: 'ジャンゴ(django)のプロジェクトでマスターデーターを入れる方法'
description: 'ジャンゴ(django)のプロジェクトで必要なマスターデータやテストデーターを入れる方法(data-seed)について説明します。'
image: '/assets/images/category/django/2019/data-seed/background.jpg'
---

## 概要
一般的にウェブサービスを開発する時最初、基本的設定が必要なマスターデーターやテストデーターが必要になります。このブログではジャンゴ(django)のプロジェクトで`fixtures`を使ってマスターデーターを生成する方法について説明します。

このブログで紹介するソースコードはGithubに公開されています。下記のリンクを参考してください。

- github: [https://github.com/dev-yakuza/django_data_seed](https://github.com/dev-yakuza/django_data_seed){:target="_blank"}

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
django-admin startproject django_jwt
```

下記のブログを参考してデーターベースやテーブルを生成します。

- [ジャンゴ(django)のプロジェクト開始]({{site.url}}/{{page.categories}}/start/){:target="_blank"}

データーベースの連動が完了されたら下記のコマンドを使って管理者(`superuser`)を生成します。

```bash
python manage.py createsuperuser
```

下記のブログを参考して`Blog`で言うジャンゴ(djagno)のアプリ(App)と`Post`モデル(Model)を生成します。

- [ジャンゴ(django)のモデル(models)の使い方]({{site.url}}/{{page.categories}}/models/){:target="_blank"}

{% include in-feed-ads.html %}

## マスターデーター準備
上のジャンゴ(django)のプロジェクトの準備を勧めたら`blog/models.py`が下記のように見えます。

```python
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title
```

私たちはこのモデル(Models)に合うマスターデーター(Master data)を準備してデーターを追加(Seed)する予定です。`blog/fixtures/posts-data.json`のファイルを作って下記のように修正します。

```json
[
  {
    "model": "blog.post",
    "fields": {
      "author": 1,
      "title": "test2",
      "content": "test2",
      "created_at": "2019-06-04T15:43:29.899",
      "updated_at": "2019-06-04T15:43:29.899",
      "published_at": "2019-06-04T15:43:28"
    }
  },
  {
    "model": "blog.post",
    "fields": {
      "author": 1,
      "title": "test1",
      "content": "test1\r\n\r\ntest1",
      "created_at": "2019-06-04T15:43:19.760",
      "updated_at": "2019-06-04T15:43:19.760",
      "published_at": "2019-06-04T15:43:18"
    }
  }
]
```

このJSONファイルを見たら分かると思いますが、私たちは2つのテストデーターを入れる予定です。

{% include in-feed-ads.html %}

## マスターデーターを入れる(Data Seed)
下記のコマンドで私たちが作ったデーターシード(Data Seed)をデーターベースに入れます。

```bash
python manage.py loaddata blog/fixtures/posts-data.json
```

## 確認
データーベースツールを使ってデーターがうまく入ったか確認してみます。

![ジャンゴ(django)のマスターデーター追加(django data seed) - データーベースツールを使ってデーター確認](/assets/images/category/django/2019/data-seed/check-data-seed-via-database-tool.jpg)

もちろん、ジャンゴ(django)の管理画面でも確認ができます。下記のコマンドでジャンゴ(django)のテストサーバーを起動します。

```bash
python manage.py runserver
```

そして管理画面のURL(http://127.0.0.1:8000/admin)に接続したら追加されたデーターが確認できます。

![ジャンゴ(django)のマスターデーター追加(django data seed) - ジャンゴ(django)の管理画面を使ってデーター確認](/assets/images/category/django/2019/data-seed/check-data-seed-via-admin.jpg)

## 完了
これでジャンゴ(django)のマスターデーターを追加する方法(Data seed)について見てみました。これからはジャンゴ(django)でプロジェクトを進める時、マスターデーターやテストデーターを準備することができるようになりました！
