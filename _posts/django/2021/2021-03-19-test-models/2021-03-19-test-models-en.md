---
layout: 'post'
permalink: '/django/test/models/'
paginate_path: '/django/:num/test/models/'
lang: 'en'
categories: 'django'
comments: true

title: '[Django] Model test'
description: Let's see how to make a test code for Models on Django project.
image: '/assets/images/category/django/2021/test-models/background.jpg'
---

<div id="contents_list" markdown="1">

## Content

- [Outline](#outline)
- [Prepare project](#prepare-project)
- [User Model](#user-model)
- [User Model test](#user-model-test)
  - [test_default_values](#test_default_values)
  - [test_updated_at](#test_updated_at)
- [Execute the test](#execute-the-test)
- [Completed](#completed)

</div>

## Outline

Recently, developing with the test code is normal in our life. The test code brings great benefits to the company such as increasing the quality of the service, reducing the time for service verification, and improving development productivity.

In this blog post, I'll introduce how to test the Model in Django project.

- Mozilla Web Docs: [Testing a Django web application](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing){:rel="nofollow noreferrer" target="_blank"}

## Prepare project

See the links below to create a new Django porject.

- [Django installation]({{site.url}}/{{page.categories}}/installation/){:target="_blank"}
- [Start Django Project]({{site.url}}/{{page.categories}}/start/){:target="_blank"}
- [Use Models in Django]({{site.url}}/{{page.categories}}/models/){:target="_blank"}

{% include in-feed-ads.html %}

## User Model

First, let's see the User model that is the test target. The User Model is like below.

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

The User Model is the customized User Model for Django. If you want to know how to create the Custom User Model, see the blog post below.

- [Django Customm User Model]({{site.url}}/{{page.categories}}/custom-user-model/){:target="_blank"}

This User Model has the features below.

- email: Use the email instead of the user name.
- wrong_pw: Store the wrong password inserting count.
- password_lock: If the user inserts the wrong password 3 times continuously, the user can't insert the password for one hour.
- certificated_at: The time when the user email is certificated.
- created_at: The time when the user is created.
- updated_at: The time when the user information is updated.

Next, let's see how to test the User Model which has thease features.

{% include in-feed-ads.html %}

## User Model test

Let's make the test code for the User Model above. We need to create the test code file like `./AppName/test_models.py` and modify it like below.

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

Let's see the details of the test code.

```python
class UserModelTest(TestCase):
    def test_default_values(self):
        ...
    def test_updated_at(self):
        ...
```

This test code has `test_default_values` and `test_updated_at` cases.

- test_default_values: The test case to check the default values when we create the data via the Model.
- test_updated_at: When we update the data via the Model, 모델을 통해 데이터를 업데이트 했을 때, `updated_at`이 잘 동작하는지 확인하는 테스트

{% include in-feed-ads.html %}

### test_default_values

When the new data is created, The timestamp stores on the `created_at`. If we want to check this, we need to mock the system time.

```python
mock_date = datetime(2021, 3, 4, 14, 57, 11, 703055)
with mock.patch('django.utils.timezone.now') as mock_now:
    mock_now.return_value = mock_date
    user = User.objects.create(email='test@test.test', password='12345')
```

Like above, we create a new User data with Mocking time. And the, check the default value of the new data.

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

At this time, we can check `created_at` and `updated_at` have a Mocking time that we've created above.

```python
self.assertEquals(user.created_at, mock_date)
self.assertEquals(user.updated_at, mock_date)
```

### test_updated_at

This test case is to check `updated_at` is updated well When we update the data via the Model.

```python
mock_date = datetime(2021, 3, 4, 14, 57, 11, 703055)
with mock.patch('django.utils.timezone.now') as mock_now:
    mock_now.return_value = mock_date
    user = User.objects.create(email='test@test.test', password='12345')

self.assertEquals(user.created_at, mock_date)
self.assertEquals(user.updated_at, mock_date)
self.assertEquals(user.updated_at.strftime("%Y-%m-%d"), '2021-03-04')
```

First, create a new user with the Mocking time. And then, check the data has the Mocking time.

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

Next, create a new Mocking time and update the User data with it. After updating, check the `updated_at` has the new Mocking time.

## Execute the test

We've created the test case that we can do with the Model. Let's check the test case is working well. Execute the command below to execute the test code.

```bash
python manage.py test
```

After executing, you can see the results on the terminal like below. And we can know all test codes are passed.

```bash
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
......................
----------------------------------------------------------------------
Ran 22 tests in 2.453s
```

## Completed

We've seen how to test the Model in the Django project. The Model didn't have a big logic, so we can make a simple test code to test the Model.

Next, let's create a test code for your project!
