---
layout: 'post'
permalink: '/django/pre-commit/'
paginate_path: '/django/:num/pre-commit/'
lang: 'ko'
categories: 'django'
comments: true

title: '[Django] pre-commit 사용법'
description: Django 프로젝트에서 pre-commit을 사용하여 Git에 커밋을 할 때, flake8을 실행하도록 설정해 보자.
image: '/assets/images/category/django/2021/pre-commit/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [pre-commit 설치](#pre-commit-설치)
- [pre-commit 설정](#pre-commit-설정)
- [flake8 설정하기](#flake8-설정하기)
- [pre-commit 실행](#pre-commit-실행)
- [완료](#완료)

</div>

## 개요

이전 블로그 포스트에서 파이썬의 코드 정적 분석기인 `flake8`을 사용하여 코드 스타일을 통일하고, 잠재적인 버그를 줄이는 방법에 대해서 알아보았습니다.

- [[Django] flake8 사용법]({{site.url}}/{{page.categories}}/flake8/){:target="_blank"}

이번 블로그 포스트에서는 `pre-commit`을 사용하여 소스코드를 Git에 커밋할 때, 설정한 flake8을 자동으로 실행하는 방법에 대해서 알아봅니다.

- pre-commit: [https://pre-commit.com/](https://pre-commit.com/){:rel="nofollow noreferrer" target="_blank"}

## pre-commit 설치

pre-commit을 사용하여 flake8을 자동으로 실행하기 위해서는,  pre-commit을 설치할 필요가 있습니다. 다음 명령어를 사용하여 pre-commit을 설치합니다.

```bash
pip install pre-commit
```

설치를 완료하였다면, 잊지말고 `requirements.txt`에 저장해 둡니다.

```bash
pip freeze > requirements.txt
```

이것으로 pre-commit을 설치하는 방법에 대해서 알아보았습니다.

## pre-commit 설정

pre-commit을 사용하여 flake8을 자동으로 실행하기 위해서는, pre-commit의 설정 파일을 작성할 필요가 있습니다. 다음 명령어를 사용하여 pre-commit의 설정 파일을 생성합니다.

```bash
pre-commit sample-config > .pre-commit-config.yaml
```

생성된 `.pre-commit-config.yaml` 파일을 열어보면 다음과 같습니다.

```yml
# See https://pre-commit.com for more information
# See https://pre-commit.com/hooks.html for more hooks
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v3.2.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
```

pre-commit에서 제공하는 샘플 내용을 확인할 수 있습니다.

{% include in-feed-ads.html %}

## flake8 설정하기

이제 pre-commit의 설정 파일에 flake8을 설정하는 방법에 대해서 알아봅시다. pre-commit의 설정 파일인 `.pre-commit-config.yaml`은 기본적으로 다음과 같은 구조를 가지고 있습니다.

```yml
repos:
  - repo: repo-url
    rev: version
    hooks:
      - id: hook-id
```

- repo: pre-commit이 제공하는 기능의 Repository URL
- rev: 사용하려는 기능의 버전
- id: pre-commit이 제공하는 기능

pre-commit은 기본적으로 제공하는 기능들이 있습니다. 다음 링크를 통해 어떤 기능들이 있는지 확인할 수 있습니다.

- hooks: [https://pre-commit.com/hooks.html](https://pre-commit.com/hooks.html){:rel="nofollow noreferrer" target="_blank"}

우리는 이중에서 flake8을 사용할 예정입니다. 그럼 `.pre-commit-config.yaml` 파일을 열고 다음과 같이 수정합니다.

```yml
repos:
  - repo: https://gitlab.com/pycqa/flake8
    rev: 3.8.4
    hooks:
      - id: flake8
```

pre-commit에서 제공하는 repo의 URL과 버전, flake8 hook을 설정하였습니다. 이 부분은 flake8 공식 문서에서도 확인할 수 있습니다.

- flake8 hooks: [https://flake8.pycqa.org/en/latest/user/using-hooks.html](https://flake8.pycqa.org/en/latest/user/using-hooks.html){:rel="nofollow noreferrer" target="_blank"}

이제 이렇게 설정한 파일을 실제 Git의 Commit hook에 등록하기 위해 다음 명령어를 실행합니다.

```bash
pre-commit install
```

이것으로 pre-commit을 사용하여 flake8을 사용할 준비가 되었습니다.

## pre-commit 실행

그럼 우리가 설정한 pre-commit이 잘 동작하는지 확인해 봅시다. 다음 명령어를 실행하면 우리가 설정한 `.pre-commit-config.yaml` 파일을 기준으로 pre-commit을 실행할 수 있습니다.

```bash
pre-commit run --all-files
```

명령어를 실행하면 다음과 같은 결과를 확인할 수 있습니다.

```bash
flake8...................................................................Passed
```

이것으로 우리가 설정한 pre-commit이 잘 동작하는 것을 확인하였습니다. 이제 지금까지 설정한 내용을 Git에 커밋합니다.

```bash
git add .
git commit -m 'Add pre-commit for flake8'
git push origin main
```

## 완료

이것으로 pre-commit을 사용하여 Git에 커밋을 할 때마다, flake8을 실행하는 방법에 대해서 알아보았습니다. 주의해야할 점은, 새롭게 Repository를 Clone한 경우 잊지말고 `pre-commit install`을 실행하여 pre-commit의 설정 내용을 Git hooks에 등록해야 합니다.

```bash
git clone repository_url
# virtualenv venv
# source venv/bin/activate
pip install -r requirement.txt
pre-commit install
```

그럼 이제 자동화된 flake8으로 더욱 생산성 높은 개발을 해보시기 바랍니다.
