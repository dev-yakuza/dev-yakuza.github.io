---
layout: 'post'
permalink: '/django/data-seed/'
paginate_path: '/django/:num/data-seed/'
lang: 'ko'
categories: 'django'
comments: true

title: '장고(django) 프로젝트에 마스터 데이터 넣기'
description: '장고(django) 프로젝트에서 필요한 마스터 데이터 또는 테스트 데이터를 넣는 방법(data-seed)에 관해서 알아보겠습니다.'
image: '/assets/images/category/django/2019/data-seed/background.jpg'
---

## 개요
일반적으로 웹 서비스를 개발하다보면 초기에 기본적으로 세팅이 필요한 마스터 데이터 또는 테스트 데이터가 필요합니다. 이 블로그에서는 장고(django) 프로젝트에서 `fixtures`을 이용하여 마스터 데이터를 생성하는 방법에 대해서 알아보겠습니다.

이 블로그 포스트에 소개되는 소스코드는 github에 공개되어 있습니다. 아래에 링크를 참고하시기 바랍니다.

- github: [https://github.com/dev-yakuza/django_data_seed](https://github.com/dev-yakuza/django_data_seed){:target="_blank"}

## 장고(django) 프로젝트 준비
이전 블로그 시리즈에서 장고(django) 프로젝트를 사용하는 방법에 대해서 설명하였습니다. 장고(django)를 사용하여 프로젝트를 구성하는 방법에 대한 자세한 내용은 아래에 링크를 통해 확인하시기 바랍니다.

- [장고(django) 설치하기]({{site.url}}/{{page.categories}}/installation/){:target="_blank"}
- [장고(django) 프로젝트 시작하기]({{site.url}}/{{page.categories}}/start/){:target="_blank"}
- [장고(django) 모델(models) 사용해보기]({{site.url}}/{{page.categories}}/models/){:target="_blank"}
- [장고(django)의 관리자 페이지]({{site.url}}/{{page.categories}}/admin/){:target="_blank"}
- [장고(django)의 라우팅(Routing)]({{site.url}}/{{page.categories}}/routing/){:target="_blank"}
- [장고(django)의 ORM]({{site.url}}/{{page.categories}}/orm/){:target="_blank"}
- [장고(django)의 뷰(View)]({{site.url}}/{{page.categories}}/view/){:target="_blank"}
- [장고(django)의 폼(Form)]({{site.url}}/{{page.categories}}/form/){:target="_blank"}
- [장고(django) 프로젝트를 헤로쿠(heroku)에 업로드하기]({{site.url}}/{{page.categories}}/heroku/){:target="_blank"}

이 블로그에서는 장고(django) 설치와 프로젝트 설정등에 대해서는 설명하지 않도록 하겠습니다. 간단하게 프로젝트가 진행될 수준으로만 설명하겠습니다.

아래에 명령어를 통해 장고(django) 프로젝트를 생성합니다.

```bash
django-admin startproject django_jwt
```

아래에 블로그를 참고하여 데이터베이스 연동 및 테이블을 생성합니다.

- [장고(django) 프로젝트 시작하기]({{site.url}}/{{page.categories}}/start/){:target="_blank"}

데이터베이스 연동이 완료되었다면 아래에 명령어를 통해 관리자(`superuser`)를 생성합니다.

```bash
python manage.py createsuperuser
```

아래에 블로그를 참고하여 `Blog` 장고(django) 앱(App)과 `Post` 모델(Model)을 생성합니다.

- [장고(django) 모델(models) 사용해보기]({{site.url}}/{{page.categories}}/models/){:target="_blank"}

{% include in-feed-ads.html %}

## 마스터 데이터 준비
위에 장고(django) 프로젝트 과정을 진행하면 `blog/models.py`에 아래와 같은 내용을 확인할 수 있습니다.

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

우리는 이 모델(Models)에 맞는 마스터 데이터(Master data)를 준비하고 데이터를 추가(Seed)할 것입니다. `blog/fixtures/posts-data.json` 파일을 생성하고 아래와 같이 추가합니다.

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

이 json 파일을 보면 알 수 있듯이 우리는 두 개의 테스트 데이터를 추가할 예정입니다.

{% include in-feed-ads.html %}

## 마스터 데이터 넣기(Data Seed)
아래에 명령어를 통해 우리가 만든 데이터 시드(Data Seed)를 데이터베이스에 넣습니다.

```bash
python manage.py loaddata blog/fixtures/posts-data.json
```

## 확인
데이터베이스 툴을 이용하여 데이터가 잘 들어갔는지 확인해 봅니다.

![장고(django) 마스터 데이터 추가(django data seed) - 데이터베이스 툴을 이용한 데이터 확인](/assets/images/category/django/2019/data-seed/check-data-seed-via-database-tool.jpg)

물론, 장고(django)의 관리자 화면을 통해서도 확인이 가능합니다. 아래에 장고(django) 명령어로 테스트 서버를 실행 시킵니다.

```bash
python manage.py runserver
```

그리고 관리자 페이지의 URL(http://127.0.0.1:8000/admin)에 접속하여 추가된 데이터를 확인할 수 있습니다.

![장고(django) 마스터 데이터 추가(django data seed) - 장고(django) 관리자 화면을 이용한 데이터 확인](/assets/images/category/django/2019/data-seed/check-data-seed-via-admin.jpg)

## 완료
이것으로 장고(django)의 마스터 데이터 추가(Data seed)에 대해서 알아보았습니다. 이제 장고(django) 프로젝트를 진행할 때, 마스터 데이터 또는 테스터 데이터를 미리 준비할 수 있게 되었습니다!
