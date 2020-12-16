---
layout: 'post'
permalink: '/django/installation/'
paginate_path: '/django/:num/installation/'
lang: 'ko'
categories: 'django'
comments: true

title: '장고(django) 설치하기'
description: '장고(django) 개발을 위해 장고(django)를 설치하고 설정하는 방법에 대해서 알아봅니다.'
image: '/assets/images/category/django/2019/installation/background.jpg'
---

## 개요
파이썬(python)의 장고(django)로 서버사이드를 개발해보려고 합니다. 이 블로그 포스트에서는 장고(django)로 개발하기 위한 설치와 설정에 대해서 설명합니다.

이 블로그는 시리즈로 작성되어 있으며, 아래에 링크를 통해 시리즈의 다른 글을 확인할 수 있습니다.

- 장고(django) 설치하기
- [장고(django) 프로젝트 시작하기]({{site.url}}/{{page.categories}}/start/){:target="_blank"}
- [장고(django) 모델(models) 사용해보기]({{site.url}}/{{page.categories}}/models/){:target="_blank"}
- [장고(django)의 관리자 페이지]({{site.url}}/{{page.categories}}/admin/){:target="_blank"}
- [장고(django)의 라우팅(Routing)]({{site.url}}/{{page.categories}}/routing/){:target="_blank"}
- [장고(django)의 ORM]({{site.url}}/{{page.categories}}/orm/){:target="_blank"}
- [장고(django)의 뷰(View)]({{site.url}}/{{page.categories}}/view/){:target="_blank"}
- [장고(django)의 폼(Form)]({{site.url}}/{{page.categories}}/form/){:target="_blank"}
- [장고(django) 프로젝트를 헤로쿠(heroku)에 업로드하기]({{site.url}}/{{page.categories}}/heroku/){:target="_blank"}

또한 이 블로그 시리즈에서 다룬 소스는 github에 공개되어 있습니다. 아래에 링크를 통해 확인 가능합니다.

- github: [https://github.com/dev-yakuza/django_exercise](https://github.com/dev-yakuza/django_exercise){:target="_blank"}

## 설치
장고(django)를 사용하기 위해서는 파이썬(python)을 설치해야합니다. 아래에 링크를 통해 자신의 OS에 맞는 파이썬(python)를 다운로드 받은 후 설치합니다.

- 파이썬(python) 다운로드: [https://www.python.org/downloads/](https://www.python.org/downloads/){:rel="nofollow noreferrer noopener" target="_blank"}

저는 주로 맥(Mac)을 사용하여 개발합니다. 또한 터미널로는 `zsh`를 사용하고 있습니다. 아래에 링크를 통해 맥(Mac)과 zsh를 사용하여 파이썬(python)을 설정하는 방법을 확인하세요.

- [맥(Mac) 개발 환경 구축(1) - iTerm과 zsh]({{site.url}}/environment/mac-iterm-zsh/){:target="_blank"}
- [맥(Mac) 개발 환경 구축(3) - 개발 환경]({{site.url}}/environment/mac-development-environment/){:target="_blank"}

위에 링크를 통해 zsh와 파이썬(python)을 설정하였다면 아래에 명령어로 버전을 확인합니다.

```bash
python --version
Python 3.7.2
```

아래에 명령어를 통해 파이썬의 가상 환경(Virtual Environment)을 간단하게 사용할 수 있게 도와주는 `virtualenv` 모듈을 설치합니다.

```bash
pip install virtualenv pylint autopep8
```

아래에 명령어를 통해 장고(django)를 사용하기 위한 환경을 만듭니다.

```bash
mkdir server
cd server
virtualenv venv
```

아래에 명령어로 가상 환경(Virtual Environment)을 활성화시킵니다.

```bash
source venv/bin/activate
```

아래 명령어로 장고(django)를 가상 환경(Virtual Environment)에 설치합니다.

```bash
pip install django
```

설치가 완료되었다면 아래에 명령어로 장고(django)가 잘 설치되었는지 확인합니다.

```bash
django-admin --version
# 2.2
```

아래에 명령어로 설치된 개발 환경을 파일로 저장합니다.

```bash
# cd server
pip freeze > requirements.txt
```

설치가 확인되었다면 아래에 명령어로 가상 환경(Virtual Environment)을 종료합니다.

```bash
deactivate
```

다시 아래에 명령어를 실행하여 가상 환경(Virtual Environment)가 정상적으로 종료되었는지 확인합니다.

```bash
django-admin --version
# zsh: command not found: django-admin
```

위에 명령어를 통해 가상 환경(Virtual Environment)을 이해할 수 있을거 같습니다. 위에서 설치한 장고(django)는 가상 환경(Virtual Enviroment)에 설치하였습니다. 따라서 가상 환경(Virtual Environment)가 종료된 환경에서 장고(django) 명령어를 실행하면 장고(django)를 찾을 수 없다는 에러가 나옵니다. 이처럼 파이썬 가상 환경(python virtual environment)를 사용하여 파이썬(python) 개발 환경을 고립시킬 수 있습니다.

{% include in-feed-ads.html %}

## 다른 머신에서 사용하기
파이썬(python)의 가상 환경(Virtual Environment)는 말 그대로 환경입니다. 따라서 이 환경을 git로 버전 관리를 할 필요하 없습니다. `.gitignore`에 아래에 내용을 추가합니다.

```bash
# .gitignore
...
venv
```

그리고 git에는 `requirements.txt`를 저장합니다. 다른 머신에서는 git를 가져오고 명령어로 가상 환경(Virtual Environment)을 설치하고 실행한 후 아래에 명령어로 장고(django)를 설치합니다.

```bash
# cd server
pip install -r requirements.txt
```

개발을 하면서 여러 모듈을 설치할텐데, 설치가 완료되면 항상 아래에 명령어를 실행하여 `requirements.txt`를 갱신합니다.

```bash
# cd server
pip freeze > requirements.txt
```

## 완료
장고(django)를 사용하기 위해 파이썬(python)과 파이썬(python)의 가상 환경(Virtual Environment)을 구성하고 장고(django)를 설치해 보았습니다. 이로써 장고(django) 개발에 준비를 맞췄습니다. 앞으로는 장고를 사용하여 서버사이드를 개발하는 방법에 대해서 설명하도록 하겠습니다.