---
layout: 'post'
permalink: '/git/default-branch/'
paginate_path: '/git/:num/default-branch/'
lang: 'ko'
categories: 'git'
comments: true

title: "[Git] 기본 브랜치를 master에서 main으로 설정하기"
description: Git을 사용할 때, 기본 브랜치를 master에서 main으로 변경하는 방법에 대해서 알아봅시다.
image: '/assets/images/category/git/2021/default-branch/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [Git config](#git-config)
- [완료](#완료)

</div>

## 개요

Git의 기본 브랜치 명인 `master`라는 단어가 많은 논란이 되면서, 많은 서비스에서 `master`의 이름을 사용하지 않게 되었습니다.

- GitHub [Renaming the default branch from master](https://github.com/github/renaming){:rel="nofollow noreferrer noopener" target="_blank"}

하지만, 아직도 로컬에서 Git을 사용하면 `master`가 기본 브랜치로 생성이 되어 불편함이 있었습니다. 이번 블로그 포스트에서는 로컬에서 Git을 사용할 때, 기본적으로 `master`가 아닌 `main`으로 브랜치가 생성되도록 하는 방법에 대해서 살펴봅시다.

## Git config

`git config` 명령어을 사용하면 Git에 관한 대부분의 설정을 할 수 있습니다. 물론, 기본 브랜치 명을 변경할 때에도 이 명령어를 사용합니다. 그럼 다음 명령어를 실행하여 Git의 기본 브랜치 명을 `master`에서 `main`으로 변경합니다.

```bash
git config --global init.defaultBranch main
```

이 명령어를 실행한 후, 다음과 명령어를 사용하여 Git을 초기화하면, 이제 `master` 브랜치가 아닌 `main` 브랜치가 생성되는 것을 확인할 수 있습니다.

```bash
git init
```

## 완료

이것으로 Git의 기본 브랜치명을 `master`에서 `main`으로 변경하는 방법에 대해서 알아보았습니다. 여러분도 이번 설정을 통해 Git의 기본 브랜치명을 변경해 보시기 바랍니다.
