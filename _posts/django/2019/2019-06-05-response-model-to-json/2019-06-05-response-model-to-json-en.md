---
layout: 'post'
permalink: '/django/response-model-to-json/'
paginate_path: '/django/:num/response-model-to-json/'
lang: 'en'
categories: 'django'
comments: true

title: 'Convert django Models to JSON for response'
description: let's see how to convert QuerySet from Models to JSON type and response it when we use django for API.
image: '/assets/images/category/django/2019/response-model-to-json/background.jpg'
---

## Outline
when we develop API server by django, sometimes we want to response JSON directly from Model QuerySet. in this blog post, we'll see how to convert the data(QuerySet) from django Model to JSON response.

you can see the source code introduced in this blog on Github. see the linke below.

- github: [https://github.com/dev-yakuza/django_response_model_to_json](https://github.com/dev-yakuza/django_response_model_to_json){:target="_blank"}

## Prepare django Project
you can see how to prepare django project on the previous blog post series. if you want more details about how to make django project, see the links below.

- [django installation]({{site.url}}/{{page.categories}}/installation/){:target="_blank"}
- [Start django Project]({{site.url}}/{{page.categories}}/start/){:target="_blank"}
- [Use Models in django]({{site.url}}/{{page.categories}}/models/){:target="_blank"}
- [django Administrator Page]({{site.url}}/{{page.categories}}/admin/){:target="_blank"}
- [django Routing]({{site.url}}/{{page.categories}}/routing/){:target="_blank"}
- [django ORM]({{site.url}}/{{page.categories}}/orm/){:target="_blank"}
- [django View]({{site.url}}/{{page.categories}}/view/){:target="_blank"}
- [django Form]({{site.url}}/{{page.categories}}/form/){:target="_blank"}
- [Upload django project to Heroku]({{site.url}}/{{page.categories}}/heroku/){:target="_blank"}

in this blog post, we won't see how to install and configure django project. just we'll see simply to prepare the project to be able to talk about converting.

execute the command below to create django project.

```bash
django-admin startproject django_jwt
```

connect database and migrate the tables to see the blog below.

- [Start django Project]({{site.url}}/{{page.categories}}/start/){:target="_blank"}

after connecting the database, execute the command below to create an administrator(`superuser`).

```bash
python manage.py createsuperuser
```

create `Blog` django App and `Post` Model by referring the blog post below.

- [Use Models in django]({{site.url}}/{{page.categories}}/models/){:target="_blank"}

and then add test data by referring the blog post below.

- [Insert master data to django project]({{site.url}}/{{page.categories}}/data-seed/){:target="_blank"}

{% include in-feed-ads.html %}

## Create URL
now, we need to create URL for getting the data. you can see details about how to create URL at the blog post below.

- [django Routing]({{site.url}}/{{page.categories}}/routing/){:target="_blank"}

oepn and modify `django_response_model_to_json/urls.py` for new URL.

```python
from django.contrib import admin
from django.urls import path
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
```

and then, create and modify `blog/urls.py` to add new URL to Blog App.

```python
from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.posts, name='posts'),
]
```

## Make View
let's make django View to convert Model data(QuerySet) to JSON type. if you want to know details about how to create django View, see the link below.

- [django View]({{site.url}}/{{page.categories}}/view/){:target="_blank"}

open and modify `blog/views.py` to make the View like below.

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

- `from django.core import serializers`: load(import) serializers to serialize Model data to JSON.
- `from django.http import HttpResponse`: load(import HttpResponse to response JSON data.
- `posts = Post.objects.filter(published_at__isnull=False).order_by('-published_at')`: load data from Post Models.
- `post_list = serializers.serialize('json', posts)`: convert the data(QuerySet) to JSON type `string`.
- `return HttpResponse(post_list, content_type="text/json-comment-filtered")`: post_list is JSON type `string` so we need to remove `(")` to response JSON.

## Check
execute the command below to start django test server to check the result.

```bash
python manage.py runserver
```

and then, send GET to the URL(`http://localhost:8000/posts/`) via Postman, you can get JSON data response well.

![convert Model to JSON in django - check the data via Postman](/assets/images/category/django/2019/response-model-to-json/check-api-with-postman.jpg)

