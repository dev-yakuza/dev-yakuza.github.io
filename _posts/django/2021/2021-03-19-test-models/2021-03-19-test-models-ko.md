---
layout: 'post'
permalink: '/django/test/models/'
paginate_path: '/django/:num/test/models/'
lang: 'ko'
categories: 'django'
comments: true

title: '[Django] Model 테스트'
description: Django 프로젝트에서 Model의 테스트 코드를 작성하는 방법에 대해서 알아봅시다.
image: '/assets/images/category/django/2021/test-models/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [프로젝트 준비](#프로젝트-준비)
- [사용자 모델](#사용자-모델)
- [사용자 모델 테스트](#사용자-모델-테스트)
  - [test_default_values](#test_default_values)
  - [test_updated_at](#test_updated_at)
- [테스트 실행](#테스트-실행)
- [완료](#완료)

</div>

## 개요

이제 소프트웨어 개발에서 테스트 코드 작성은 빼놓을 수 없는 부분으로 자리잡았습니다. 테스트 코드는 서비스의 품질 상승, 서비스 검증의 시간 감소 및 개발 생산성 향상 등 서비스를 제공하는 회사에 여러면에서 큰 이익을 가져다 줍니다.

이번 블로그 포스트에서는 Django 프로젝트에서 Model을 테스트하는 방법에 대해서 소개합니다.

- Mozilla Web Docs: [Testing a Django web application](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing){:rel="nofollow noreferrer" target="_blank"}

## 프로젝트 준비

다음 블로그 포스트를 참고하여 새로운 장고 프로젝트를 생성합니다.

- [장고(django) 설치하기]({{site.url}}/{{page.categories}}/installation/){:target="_blank"}
- [장고(django) 프로젝트 시작하기]({{site.url}}/{{page.categories}}/start/){:target="_blank"}
- [장고(django) 모델(models) 사용해보기]({{site.url}}/{{page.categories}}/models/){:target="_blank"}

{% include in-feed-ads.html %}

## 사용자 모델

우선 테스트의 대상이 되는 사용자 모델(User model)에 대해서 살펴봅시다. 이번 블로그에서 소개할 유저 모델은 다음과 같습니다.

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

위의 모델은 Django의 기본 사용자 모델을 커스터마이징한 사용자 모델 일부입니다. Django에서 커스텀 사용자 모델을 사용하는 방법에 대해서는 아래 링크를 참고하시기 바랍니다.

- [장고(django)의 커스텀 유저 모델(Custom User Model)]({{site.url}}/{{page.categories}}/custom-user-model/){:target="_blank"}

이 사용자 모델은 다음과 같은 특징을 가지고 있습니다.

- email: 사용자 이름 대신 이메일을 사용합니다.
- wrong_pw: 암호를 틀린 횟수를 저장하기 위한 필드
- password_lock: 암호를 연속해서 3번 틀렸을 경우, 1시간 동안 암호를 입력하지 못하게 하기 위한 필드
- certificated_at: 이메일의 본인 인증을 한 시점을 저장하기 위한 필드
- created_at: 사용자 생성 시점
- updated_at: 사용자 정보의 업데이트 시점

그럼 이제 이런 특징을 가진 사용자 모델을 테스트 하는 방법에 대해서 알아봅시다.

{% include in-feed-ads.html %}

## 사용자 모델 테스트

그럼 위에서 만든 사용자 모델에 관한 테스트 코드를 작성해 봅시다. 모델에 관한 테스트 코드는 `./AppName/test_models.py`을 생성하고 다음과 같이 수정합니다.

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

그럼 테스트 코드를 좀 더 자세히 살펴봅시다.

```python
class UserModelTest(TestCase):
    def test_default_values(self):
        ...
    def test_updated_at(self):
        ...
```

이 테스트 코드는 `test_default_values`와 `test_updated_at`, 두 가지 테스트 케이스를 가지고 있습니다.

- test_default_values: 모델을 통해 데이터를 생성했을 때, 기본값들을 테스트
- test_updated_at: 모델을 통해 데이터를 업데이트 했을 때, `updated_at`이 잘 동작하는지 확인하는 테스트

{% include in-feed-ads.html %}

### test_default_values

새로운 데이터를 생성할 때, `created_at`은 생성 시점의 timestamp를 사용합니다. 이 값이 제대로 동작하는지 확인하기 위해서는 시스템 시간을 Mocking할 필요가 있습니다.

```python
mock_date = datetime(2021, 3, 4, 14, 57, 11, 703055)
with mock.patch('django.utils.timezone.now') as mock_now:
    mock_now.return_value = mock_date
    user = User.objects.create(email='test@test.test', password='12345')
```

이렇게 시간을 Mocking하여 새로운 사용자를 생성한 후, 새롭게 생성된 데이터의 기본값들을 체크합니다.

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

이 때, 위에서 Mocking한 시간이 `created_at`과 `updated_at`에 잘 저장되었는지도 확인합니다.

```python
self.assertEquals(user.created_at, mock_date)
self.assertEquals(user.updated_at, mock_date)
```

### test_updated_at

모델을 사용하여 생성된 데이터를 업데이트하였을 때, `updated_at`이 잘 갱신되는지 확인하기 위한 테스트 케이스입니다.

```python
mock_date = datetime(2021, 3, 4, 14, 57, 11, 703055)
with mock.patch('django.utils.timezone.now') as mock_now:
    mock_now.return_value = mock_date
    user = User.objects.create(email='test@test.test', password='12345')

self.assertEquals(user.created_at, mock_date)
self.assertEquals(user.updated_at, mock_date)
self.assertEquals(user.updated_at.strftime("%Y-%m-%d"), '2021-03-04')
```

우선 시스템 시간을 Mocking하여 새로운 유저 데이터를 생성합니다. 그리고 해당 데이터가 현재 시간을 잘 가지고 있는지 테스트합니다.

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

그런 다음, 시간을 새롭게 Mocking하고, 사용자 데이터를 업데이트합니다. 이렇게 업데이트 한 후, `updated_at`에 업데이트한 시점의 시간이 잘 기록되었는지 확인합니다.

## 테스트 실행

이렇게 모델을 가지고 우리가 할 수 있는 동작들을 테스트 케이스로 작성한 후, 다음 명령어를 사용하여 테스트 코드를 실행합니다.

```bash
python manage.py test
```

그럼 다음과 같이 우리가 작성한 테스트 코드가 문제없이 통과되는 것을 확인할 수 있습니다.

```bash
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
......................
----------------------------------------------------------------------
Ran 22 tests in 2.453s
```

## 완료

이것으로 Django에서 모델을 테스트하는 방법에 대해서 알아보았습니다. 모델에 큰 로직이 포함되어있지 않기 때문에, 간단한 테스트 코드로 모델을 테스트할 수 있음을 알 수 있었습니다.

이제 여러분도, 여러분의 Django 프로젝트에 모델 테스트 코드를 작성해 보시기 바랍니다.
