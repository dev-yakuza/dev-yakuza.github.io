---
layout: 'post'
permalink: '/django/routing/'
paginate_path: '/django/:num/routing/'
lang: 'en'
categories: 'django'
comments: true

title: 'django Routing'
description: let's see how to manage the website routing via django url management feature.
image: '/assets/images/category/django/2019/routing/background.jpg'
---

## Outline
I try to develop a web service by python django. for the web service, we need to make web pages and connect urls to each webpage(Routing). in this blog, we'll try to use django url management feature to manage the web service routing.

this blog is a series. if you want to check other blog posts of the series, see the links below.

- [django installation]({{site.url}}/{{page.categories}}/installation/){:target="_blank"}
- [Start django Project]({{site.url}}/{{page.categories}}/start/){:target="_blank"}
- [Use Models in django]({{site.url}}/{{page.categories}}/models/){:target="_blank"}
- [django Administrator Page]({{site.url}}/{{page.categories}}/admin/){:target="_blank"}
- django Routing
- [django ORM]({{site.url}}/{{page.categories}}/orm/){:target="_blank"}
- [django View]({{site.url}}/{{page.categories}}/view/){:target="_blank"}
- [django Form]({{site.url}}/{{page.categories}}/form/){:target="_blank"}
- [Upload django project to Heroku]({{site.url}}/{{page.categories}}/heroku/){:target="_blank"}

also, this blog series source code is opened on Github. you can see full source code via the link below.

- github: [https://github.com/dev-yakuza/django_exercise](https://github.com/dev-yakuza/django_exercise){:target="_blank"}

## Check Routing
django has a big unit called Project and a small unit called Application. djanog Project can include many applications. this means django has Project unit Routing and Application unit Routing. first, open `django_exercise/urls.py` file to check django Project Unit Routing.

```python
...
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
```

when you open the file, you can see the contents like above. in previous blog post([django Administrator Page]({{site.url}}/{{page.categories}}/admin/){:target="_blank"}), we've opend `http://127.0.0.1:8000/admin` URL to connect the administrator page. we've not configured any settings but we could see the administrator page, because the django administrator routing has been configured basically. we'll add a new application routing file we created in here to manage each application routing.

## Create Views
we need to create Views to connect an URL by the application Routing. open `blog/views.py` and modify it like below.

```python
from django.shortcuts import render

def posts(request):
    return render(request, 'blog/posts.html', {})
```

## Create HTML File
now, we'll create `blog/posts.html` fil referred in Views. create `blog/templates/blog/posts.html` file and modify it like below.

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

the webpage is prepared to connect the URL via Routing. let's see how to connect the URL to the webpage via Routing.

{% include in-feed-ads.html %}

## Create Application Routing
we need to make django Application Routing in our blog web service. create `blog/urls.py` file and modify it like below.

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
]
```


## Register Application Routing
we need to register django Application Routing(`blog/urls.py`) to django Project. open and modify `django_exercise/urls.py` file like below

```python
from django.contrib import admin
from django.urls import path, include # <<< here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')), # <<< here
]
```

## Check
execute the django command below to start test server, and connect `http://127.0.0.1:8000/` to check the Routing works well

```bash
# source venv/bin/activate
# pip install -r requirements.txt
# cd django_exercise
python manage.py runserver
```

we can see `Hello World` on the web browser.

## Completed
we've seen how to make and use django Routing. now, we can connect webpages and URLs via Routing!