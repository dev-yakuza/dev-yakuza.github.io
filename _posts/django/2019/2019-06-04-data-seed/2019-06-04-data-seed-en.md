---
layout: 'post'
permalink: '/django/data-seed/'
paginate_path: '/django/:num/data-seed/'
lang: 'en'
categories: 'django'
comments: true

title: 'Insert master data to django project'
description: let's see how to insert master data or test data to django proejct(data-seed)
image: '/assets/images/category/django/2019/data-seed/background.jpg'
---

## Outline
normally, we need master data or test data to develop a web service. in this blog post, we'll see how to prepare master data or test data and insert them to django project with `fixtures`.

you can see the source code introduced in this blog on Github. see the linke below.

- github: [https://github.com/dev-yakuza/django_data_seed](https://github.com/dev-yakuza/django_data_seed){:target="_blank"}

## Prepare django Proejct.
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

in this blog post, we won't see how to install and configure django project. just we'll see simply to prepare the project to be able to talk about data-seed.

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

{% include in-feed-ads.html %}

## Prepare Master Data
after doing `Prepare django Proejct` section, you can see `blog/models.py` model like below.

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

we'll prepare the master data for this model and insert data to database(Seed). create and modify `blog/fixtures/posts-data.json` file like below.

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

as you can see, we'll add two data.

{% include in-feed-ads.html %}

## Insert Master Data(Data Seed)
execute the command below to insert seed-data we've created above to the database.

```bash
python manage.py loaddata blog/fixtures/posts-data.json
```

## Check
let's check the data inserted well via database tool.

![Insert master data on django(django data seed) - check the data via database tool](/assets/images/category/django/2019/data-seed/check-data-seed-via-database-tool.jpg)

of course, we can see them via django administrator page. execute the command below to start django test server.

```bash
python manage.py runserver
```

and then open the administrator page(http://127.0.0.1:8000/admin), you can see the data stored well.

![Insert master data on django(django data seed) - check the data via dajngo administrator page](/assets/images/category/django/2019/data-seed/check-data-seed-via-admin.jpg)

## Completed
we've seen how to add master data(Data seed) in django. now, we can prepare the master data or test data for django project!
