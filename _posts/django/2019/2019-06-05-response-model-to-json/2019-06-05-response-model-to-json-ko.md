---
layout: 'post'
permalink: '/django/response-model-to-json/'
paginate_path: '/django/:num/response-model-to-json/'
lang: 'ko'
categories: 'django'
comments: true

title: '장고(django)의 모델(Models)을 JSON으로 응답(Response)하기'
description: '장고(django) 프로젝트에서 API를 사용하여 정보를 전달할 때, 모델(Models)에서 가져온 정보(QuerySet)를 그대로 JSON으로 응답(Response)하는 방법에 대해서 알아봅니다.'
image: '/assets/images/category/django/2019/response-model-to-json/background.jpg'
---

## 개요
장고(django)로 API 서버를 개발하다 보면, 모델(Models)에서 직접 가져온 정보(QuerySet)을 바로 JSON으로 응답하고 싶을 때가 있습니다. 이 블로그 포스트에서는 장고(django)를 이용하여 모델(Models)에서 가져온 정보(QuerySet)을 그대로 JSON으로 보내는 방법에 대해서 알아보겠습니다.

이 블로그에서 사용하는 소스코드는 github에 공개되어 있습니다. 아래에 링크를 통해 확인 가능합니다.

- github: [https://github.com/dev-yakuza/django_response_model_to_json](https://github.com/dev-yakuza/django_response_model_to_json){:target="_blank"}

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
django-admin startproject django_response_model_to_json
```

아래에 블로그를 참고하여 데이터베이스 연동 및 테이블을 생성합니다.

- [장고(django) 프로젝트 시작하기]({{site.url}}/{{page.categories}}/start/){:target="_blank"}

데이터베이스 연동이 완료되었다면 아래에 명령어를 통해 관리자(`superuser`)를 생성합니다.

```bash
python manage.py createsuperuser
```

아래에 블로그를 참고하여 `Blog` 장고(django) 앱(App)과 `Post` 모델(Model)을 생성합니다.

- [장고(django) 모델(models) 사용해보기]({{site.url}}/{{page.categories}}/models/){:target="_blank"}

그리고 아래에 블로그를 참고하여 테스트 데이터를 추가합니다.

- [장고(django) 프로젝트에 마스터 데이터 넣기]({{site.url}}/{{page.categories}}/data-seed/){:target="_blank"}

{% include in-feed-ads.html %}

## URL 작성
이제 테스트 데이터를 가져오기 위한 URL을 생성합니다. 아래에 링크를 통해 자세한 방법을 확인할 수 있습니다.

- [장고(django)의 라우팅(Routing)]({{site.url}}/{{page.categories}}/routing/){:target="_blank"}

URL을 작성하기 위해 `django_response_model_to_json/urls.py`을 열고 아래와 같이 수정합니다.

```python
from django.contrib import admin
from django.urls import path
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
```

그리고 Blog 앱에 URL을 추가하기 위해 `blog/urls.py`을 생성하고 아래와 같이 수정합니다.

```python
from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.posts, name='posts'),
]
```

## 뷰(View) 작성
이제 모델(Models)에서 가져온 데이터(QuerySet)을 JSON으로 반환하기 위한 뷰(View)를 작성해야 합니다. 장고(django)의 뷰(View)에 관해서는 아래에 블로그를 참고하시기 바랍니다.

- [장고(django)의 뷰(View)]({{site.url}}/{{page.categories}}/view/){:target="_blank"}

뷰(View)를 만들기 위해 `blog/views.py`를 열고 아래와 같이 수정합니다.

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

- `from django.core import serializers`: 모델(Models)을 JSON 타입으로 데이터를 직렬화 시키기 위해 serializers를 불러옵니다.
- `from django.http import HttpResponse`: JSON으로 데이터를 반환(Response)하기 위해 HttpResponse를 사용할 예정입니다.
- `posts = Post.objects.filter(published_at__isnull=False).order_by('-published_at')`: Post 모델(Models)을 이용하여 데이터를 가져옵니다.
- `post_list = serializers.serialize('json', posts)`: 가져온 데이터(QuerySet)를 JSON 타입의 `문자열`로 변환합니다.
- `return HttpResponse(post_list, content_type="text/json-comment-filtered")`: post_list가 JSON 타입의 `문자열`이므로 `따옴표(")`를 제거한 JSON을 반환해야 합니다.

## 확인
지금까지 작업한 내용을 확인하기 위해 장고(django)의 테스트 서버를 실행 시킵니다.

```bash
python manage.py runserver
```

그리고 Postman에서 해당 URL(`http://localhost:8000/posts/`)을 GET으로 가져오면 아래와 같이 데이터가 잘 가져와지는 것을 확인할 수 있습니다.

![장고(django) 모델(Models)을 JSON으로 반환하기 - Postman을 이용한 데이터 확인](/assets/images/category/django/2019/response-model-to-json/check-api-with-postman.jpg)

