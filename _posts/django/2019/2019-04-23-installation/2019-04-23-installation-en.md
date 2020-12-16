---
layout: 'post'
permalink: '/django/installation/'
paginate_path: '/django/:num/installation/'
lang: 'en'
categories: 'django'
comments: true

title: 'django installation'
description: let's see how to install django and how to configure django.
image: '/assets/images/category/django/2019/installation/background.jpg'
---

## Outline
I try to develop the serverside by python django. in this blog post, I'll introduce how to install and configure django for developing.

this blog is a series. if you want to check other blog posts of the series, see the links below.

- django installation
- [Start django Project]({{site.url}}/{{page.categories}}/start/){:target="_blank"}
- [Use Models in django]({{site.url}}/{{page.categories}}/models/){:target="_blank"}
- [django Administrator Page]({{site.url}}/{{page.categories}}/admin/){:target="_blank"}
- [django Routing]({{site.url}}/{{page.categories}}/routing/){:target="_blank"}
- [django ORM]({{site.url}}/{{page.categories}}/orm/){:target="_blank"}
- [django View]({{site.url}}/{{page.categories}}/view/){:target="_blank"}
- [django Form]({{site.url}}/{{page.categories}}/form/){:target="_blank"}
- [Upload django project to Heroku]({{site.url}}/{{page.categories}}/heroku/){:target="_blank"}

also, this blog series source code is opened on Github. you can see full source code via the link below.

- github: [https://github.com/dev-yakuza/django_exercise](https://github.com/dev-yakuza/django_exercise){:target="_blank"}

## Installation
we need to install python to use django. click the link below. download and install suitable python on your OS.

- download python: [https://www.python.org/downloads/](https://www.python.org/downloads/){:rel="nofollow noreferrer noopener" target="_blank"}

I mainly use Mac for developing. also, I use `zsh` for the terminal. you can see how to set python and zsh on Mac via the links below.

- [Development Environment on Mac(1) - iTerm & zsh]({{site.url}}/environment/mac-iterm-zsh/){:target="_blank"}
- [Development Environment on Mac(3) - for development]({{site.url}}/environment/mac-development-environment/){:target="_blank"}

after setting zsh and python via the links above, execute the command below to check python version.

```bash
python --version
Python 3.7.2
```

execute the command below to install `virtualenv` module that supports to make python Virtual Environment easily.

```bash
pip install virtualenv pylint autopep8
```

execute the command below to make django development environment.

```bash
mkdir server
cd server
virtualenv venv
```

execute the command below to activate Virtual Environment.

```bash
source venv/bin/activate
```

execute the command below to install django in Virtual Environment.

```bash
pip install django
```

after installation, execute the command below to check django installed well.

```bash
django-admin --version
# 2.2
```

execute the command below to save the development environment to a file.

```bash
# cd server
pip freeze > requirements.txt
```

after checking the installation, execute the command below to quit Virutal Environment.

```bash
deactivate
```

execute the command below again to check Virtual Environment quit well

```bash
django-admin --version
# zsh: command not found: django-admin
```

we can understand what Virtual Environment is via the command above. we've installed django in Virtual Environment. so in Virtual Environment quit state, if we execute the django command, we can see the error message that django command not found. which means, we can isolate python development environment by python Virtual Environment.

{% include in-feed-ads.html %}

## How To Use On Other Machines
python Virtual Environemt is just an environment. so we don't need it to be version controlled by git. add the content below to `.gitignore` file.

```bash
# .gitignore
...
venv
```

and then save `requirements.txt` on git(commit and push). in other machines, clone it from git and install Virtual Environment by the command. after it, install django by the command below.

```bash
# cd server
pip install -r requirements.txt
```

we'll use many modules during developing. after installing the modules, execute the command below to update `requirements.txt`.

```bash
# cd server
pip freeze > requirements.txt
```

## Completed
we've seen how to install python and how to use python Virtual Environment for using django. finally, we're ready to develop with django. after, I'll introduce how to develop the serverside with django.