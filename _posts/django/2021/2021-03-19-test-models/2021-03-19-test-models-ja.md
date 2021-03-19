---
layout: 'post'
permalink: '/django/test/models/'
paginate_path: '/django/:num/test/models/'
lang: 'ja'
categories: 'django'
comments: true

title: '[Django] Modelのテスト'
description: DjangoプロジェクトでModelのテストコードを作成する方法について調べてみましょう。
image: '/assets/images/category/django/2021/test-models/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [プロジェクトの準備](#プロジェクトの準備)
- [ユーザモデル](#ユーザモデル)
- [ユーザモデルテスト](#ユーザモデルテスト)
  - [test_default_values](#test_default_values)
  - [test_updated_at](#test_updated_at)
- [テストの実行](#テストの実行)
- [完了](#完了)

</div>

## 概要

ソフトウェア開発でテストコード作成は必須になりました。テストコードはサービスの品質上昇、サービスの検証時間の短縮や開発生産性向上などサービスを提供する会社に多くの面で大きな利益をもたらします。

このブログポストではDjangoプロジェクトでModelをテストする方法を紹介します。

- Mozilla Web Docs: [Testing a Django web application](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing){:rel="nofollow noreferrer" target="_blank"}

## プロジェクトの準備

次のブログポストを参考にして新しいDjangoのプロジェクトを生成します。

- [ジャンゴ(django)インストール]({{site.url}}/{{page.categories}}/installation/){:target="_blank"}
- [ジャンゴ(django)のプロジェクト開始]({{site.url}}/{{page.categories}}/start/){:target="_blank"}
- [ジャンゴ(django)のモデル(models)の使い方]({{site.url}}/{{page.categories}}/models/){:target="_blank"}

{% include in-feed-ads.html %}

## ユーザモデル

まずテストの対象になるユーザモデル(User model)についてみてみましょう。このブログで紹介するユーザモデルは次のようです。

```python
from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
...
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        unique=True,
    )

    wrong_pw = models.DecimalField(max_digits=1, decimal_places=0, default= 0)
    password_lock = models.DateTimeField(blank=True, null=True)
    certificated_at = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
```

上のモデルはDjangoの基本ユーザモデルをカスタマイズしたユーザモデルの一部です。Djangoでカスタムユーザモデルを使う方法については下記のリンクを参考してください。

- [ジャンゴ(django)のカスタムユーザーモデル(Custom User Model)]({{site.url}}/{{page.categories}}/custom-user-model/){:target="_blank"}

このユーザモデルは下記の特徴を持ってます。

- email: ユーザ名の代わりメールを使います。
- wrong_pw: パスワードの間違った回数を保存するフィールドです。
- password_lock: パスワードを連続3回間違うと、1時間パスワードを入力できないようにするためのフィールドです。
- certificated_at: メールの本人確認をした時点を保存するためのフィールドです。
- created_at: ユーザを生成した時点
- updated_at: ユーザの情報をアップデートした時点

このような特徴を持ってるユーザモデルをテストする方法にてついてみてみましょう。

{% include in-feed-ads.html %}

## ユーザモデルテスト

そしたら、上で作ったユーザモデルに関するテストコードを作成してみましょう。モデルに関するテストコードは`./AppName/test_models.py`を生成して次のように修正します。

```python
from django.test import TestCase
from unittest import mock
from datetime import datetime

from .models import User

class UserModelTest(TestCase):
    def test_default_values(self):
        mock_date = datetime(2021, 3, 4, 14, 57, 11, 703055)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_date
            user = User.objects.create(email='test@test.test', password='12345')

        self.assertEquals(user.email, 'test@test.test')
        self.assertEquals(user.wrong_pw, 0)
        self.assertEquals(user.password_lock, None)
        self.assertEquals(user.certificated_at, None)
        self.assertEquals(user.is_active, True)
        self.assertEquals(user.is_admin, False)
        self.assertEquals(user.created_at, mock_date)
        self.assertEquals(user.updated_at, mock_date)

    def test_updated_at(self):
        mock_date = datetime(2021, 3, 4, 14, 57, 11, 703055)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_date
            user = User.objects.create(email='test@test.test', password='12345')

        self.assertEquals(user.created_at, mock_date)
        self.assertEquals(user.updated_at, mock_date)
        self.assertEquals(user.updated_at.strftime("%Y-%m-%d"), '2021-03-04')

        mock_update_date = datetime(2021, 3, 5, 14, 57, 11, 703055)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_update_date
            user.is_admin = True
            user.save()

        self.assertEquals(user.created_at, mock_date)
        self.assertEquals(user.updated_at, mock_update_date)
        self.assertEquals(user.updated_at.strftime("%Y-%m-%d"), '2021-03-05')
```

それでは、テストコードをもっと詳しくみてみましょう。

```python
class UserModelTest(TestCase):
    def test_default_values(self):
        ...
    def test_updated_at(self):
        ...
```

このテストコードは`test_default_values`と`test_updated_at`、二つのテストケースを持ってます。

- test_default_values: モデルを使ってデータを生成した時、基本値をテストする
- test_updated_at: モデルを使ってデータをアップデートした時、`updated_at`がうまく動作したか確認する

{% include in-feed-ads.html %}

### test_default_values

新しいデータを生成した時、`created_at`は生成時点のtimestampを使います。この値が正しいか確認するためにはシステムの時間をMockingする必要があります。

```python
mock_date = datetime(2021, 3, 4, 14, 57, 11, 703055)
with mock.patch('django.utils.timezone.now') as mock_now:
    mock_now.return_value = mock_date
    user = User.objects.create(email='test@test.test', password='12345')
```

このように時間をMockingして新しいユーザを生成した後、新しいデータが生成されたデータの基本値をチェックします。

```python
self.assertEquals(user.email, 'test@test.test')
self.assertEquals(user.wrong_pw, 0)
self.assertEquals(user.password_lock, None)
self.assertEquals(user.certificated_at, None)
self.assertEquals(user.is_active, True)
self.assertEquals(user.is_admin, False)
self.assertEquals(user.created_at, mock_date)
self.assertEquals(user.updated_at, mock_date)
```

この時、上でMockingした時間が`created_at`と`updated_at`に正しく保存されたかも確認します。

```python
self.assertEquals(user.created_at, mock_date)
self.assertEquals(user.updated_at, mock_date)
```

### test_updated_at

モデルを使って生成したデータをアップデートした時、`updated_at`がうまく更新されるか確認するためのテストケースです。

```python
mock_date = datetime(2021, 3, 4, 14, 57, 11, 703055)
with mock.patch('django.utils.timezone.now') as mock_now:
    mock_now.return_value = mock_date
    user = User.objects.create(email='test@test.test', password='12345')

self.assertEquals(user.created_at, mock_date)
self.assertEquals(user.updated_at, mock_date)
self.assertEquals(user.updated_at.strftime("%Y-%m-%d"), '2021-03-04')
```

まず、システム時間をMockingして新しいユーザデータを生成します。そして当該データが現在時間を持ってるかテストします。

```python
mock_update_date = datetime(2021, 3, 5, 14, 57, 11, 703055)
with mock.patch('django.utils.timezone.now') as mock_now:
    mock_now.return_value = mock_update_date
    user.is_admin = True
    user.save()

self.assertEquals(user.created_at, mock_date)
self.assertEquals(user.updated_at, mock_update_date)
self.assertEquals(user.updated_at.strftime("%Y-%m-%d"), '2021-03-05')
```

そして、時間を新しくMockingした後、ユーザデータをアップデートします。このようにアップデートした後、`updated_at`がアップデートした時点の時間を持ってるか確認します。

## テストの実行

このようにモデルで私たちができる動作のテストケースを作成した後、次のコマンドを使ってテストコードを実行します。

```bash
python manage.py test
```

そしたら私たちが作成したテストコードが下記のように問題なく成功することが確認できます。

```bash
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
......................
----------------------------------------------------------------------
Ran 22 tests in 2.453s
```

## 完了

これでDjangoでモデルをテストする方法についてみてみました。モデルは大きいロジックがなかったので、簡単なテストコードでモデルをテストすることができました。

今後は皆さんも、皆さんのDjangoプロジェクトへモデルテストコードを作成してみてください。
