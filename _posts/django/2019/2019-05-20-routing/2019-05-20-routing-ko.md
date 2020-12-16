---
layout: 'post'
permalink: '/django/routing/'
paginate_path: '/django/:num/routing/'
lang: 'ko'
categories: 'django'
comments: true

title: '장고(django)의 라우팅(Routing)'
description: '장고(django)의 URL 관리 기능을 사용하여 웹 서비스의 라우팅(Routing)을 관리해 봅시다.'
image: '/assets/images/category/django/2019/routing/background.jpg'
---

## 개요
이제 본격적으로 장고(django)를 사용하여 웹 서비스를 작성하려고 합니다. 웹 서비스를 작성하려면 사용자가 접속하는 URL별 페이지를 만들고 그 페이지를 서비스할 필요가 있습니다. 이 블로그 포스트에서는 장고(django)에서 기본적으로 제공하는 URL 관리 기능을 통해 웹 서비스의 라우팅(Routing)을 관리하는 방법에 대해서 설명합니다.

이 블로그는 시리즈로 작성되어 있으며, 아래에 링크를 통해 시리즈의 다른 글을 확인할 수 있습니다.

- [장고(django) 설치하기]({{site.url}}/{{page.categories}}/installation/){:target="_blank"}
- [장고(django) 프로젝트 시작하기]({{site.url}}/{{page.categories}}/start/){:target="_blank"}
- [장고(django) 모델(models) 사용해보기]({{site.url}}/{{page.categories}}/models/){:target="_blank"}
- [장고(django)의 관리자 페이지]({{site.url}}/{{page.categories}}/admin/){:target="_blank"}
- 장고(django)의 라우팅(Routing)
- [장고(django)의 ORM]({{site.url}}/{{page.categories}}/orm/){:target="_blank"}
- [장고(django)의 뷰(View)]({{site.url}}/{{page.categories}}/view/){:target="_blank"}
- [장고(django)의 폼(Form)]({{site.url}}/{{page.categories}}/form/){:target="_blank"}
- [장고(django) 프로젝트를 헤로쿠(heroku)에 업로드하기]({{site.url}}/{{page.categories}}/heroku/){:target="_blank"}

또한 이 블로그 시리즈에서 다룬 소스는 github에 공개되어 있습니다. 아래에 링크를 통해 확인 가능합니다.

- github: [https://github.com/dev-yakuza/django_exercise](https://github.com/dev-yakuza/django_exercise){:target="_blank"}

## 라우팅 확인
장고(django)는 크게 프로젝트(Project) 단위와 어플리케이션(Application) 단위가 존재합니다. 장고(djanog) 프로젝트는 여러 어플리케이션을 가질 수 있습니다. 이것은 곧 프로젝트(Project) 단위의 라우팅(Routing) 관리와 어플리케이션(Application) 단위의 라우팅(Routing) 관리가 존재한다는 것을 의미합니다. 우선 장고(django)의 프로젝트 단위의 라우팅(Routing) 관리를 확인하기 위해 `django_exercise/urls.py` 파일을 확인 합니다.

```python
...
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
```

파일을 열면 위와 같은 화면을 볼수 있습니다. 이전 블로그([장고(django)의 관리자 페이지]({{site.url}}/{{page.categories}}/admin/){:target="_blank"})에서 `http://127.0.0.1:8000/admin` URL로 관리자 페이지에 접속하였습니다. 우리가 아무 설정도 하지 않아도 관리자 화면이 표시된 이유는 `django_exercise/urls.py` 파일에 위와 같은 설정이 기본적으로 설정되어있기 때문입니다. 우리는 이곳에 우리가 만든 새로운 장고(django) 어플리케이션(Application)의 라우팅 파일을 등록하여 어플리케이션(Application)별 라우팅을 관리할 예정입니다.

## 뷰 생성
일단 어플리케이션(Application)의 라우팅(Routing)을 통해 URL에 연결할 `뷰(Views)`를 생성할 필요가 있습니다. `blog/views.py`를 열고 아래와 같이 수정합니다.

```python
from django.shortcuts import render

def posts(request):
    return render(request, 'blog/posts.html', {})
```

## HTML 파일 생성
이제 뷰(Views) 파일에서 참고하고 있는 `blog/posts.html` 파일을 생성해야 합니다. `blog/templates/blog/posts.html` 파일을 생성하고 아래와 같이 코딩합니다.

```html
<html>
  <head>
    <title>Hello World</title>
  </head>
  <body>
    Hello World
  </body>
</html>
```

이것으로 라우팅(Routing)을 통해 URL에 연결할 화면 준비가 끝났습니다. 이제 실제로 라우팅(Routing)을 통해 URL과 화면을 연결하는 방법에 대해서 알아보겠습니다.

{% include in-feed-ads.html %}

## 어플리케이션의 라우팅 파일 생성
우리가 제작중인 블로그 웹 사이트에 해당하는 장고(django) 어플리케이션(Application)을 위한 라우팅(Routing) 파일을 생성할 필요가 있습니다. `blog/urls.py` 파일을 생성하고 아래에 내용을 추가합니다.

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
]
```


## 어플리케이션의 라우팅 등록
위에서 생성한 장고(django) 어플리케이션(Application)의 라우팅(Routing) 파일인 `blog/urls.py`를 장고(django) 프로젝트(Project)에 등록할 필요가 있습니다. `django_exercise/urls.py` 파일을 열고 아래와 같이 수정합니다.

```python
from django.contrib import admin
from django.urls import path, include # <<< here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')), # <<< here
]
```

## 확인
아래에 장고(django) 명령어로 테스트 서버를 실행한 후, `http://127.0.0.1:8000/`에 접속하여 우리가 설정한 라우팅(Routing)이 동작하는지 확인합니다.

```bash
# source venv/bin/activate
# pip install -r requirements.txt
# cd django_exercise
python manage.py runserver
```

브라우저에 `Hello World`가 잘 표시되는 것을 확인할 수 있습니다.

## 완료
이것으로 장고(django)의 라우팅(Routing)에 대해서 알아보았습니다. 이제 라우팅(Routing)을 통해 자신이 만든 화면과 URL을 연결할 수 있습니다.