---
layout: 'post'
permalink: '/git/sync-fork-repository/'
paginate_path: '/git/:num/sync-fork-repository/'
lang: 'ko'
categories: 'git'
comments: true

title: 'Fork 저장소 동기화하기'
description: Fork한 저장소(Repository)와 원본 저장소(Repository)를 동기화(Sync)하는 방법에 대해서 알아봅시다.
image: '/assets/images/category/git/2020/sync-fork-repository/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [원본 저장소 추가](#원본-저장소-추가)
- [원본 저장소 내용 가져오기](#원본-저장소-내용-가져오기)
- [Rebase](#rebase)
- [Fork 브랜치 동기화](#fork-브랜치-동기화)
- [완료](#완료)

</div>

## 개요

오픈 소스에 기여(Commit)하거나, 회사가 소스코드를 GitHub에서 관리할 때, 우리는 Fork를 사용하여 해당 저장소(Repository)를 자신의 저장소로 가지고 옵니다. 이렇게 가지고 온 저장소의 소스코드를 Clone하고 수정하여, 원본 저장소에 Pull Request를 보내고 Merge함으로써 소스 코드를 관리하게 됩니다.

하지만, 오픈 소스나 회사 소스코드는 혼자만 사용하는 것이기 아니기 때문에, 내가 Fork한 시점의 원본 저장소의 Master와 Pull Request를 보내는 현 시점의 원본 저정소의 Master에는 차이가 발생합니다.

이번 블로그에서는 이렇게 차이가 발생한 원본 저장소의 Master와 Fork한 저장소의 Master를 동기화 하는 방법에 대해서 알아보려고 합니다.

## 원본 저장소 추가

원본 저장소와 Fork한 저장소를 동기화(Sync)하기 위해서는 우선 원본 저장소를 로컬 환경의 원격 주소에 추가할 필요가 있습니다.

아래에 명령어를 실행하여 현재 추가된 원격 주소를 확인합니다.

```bash
git remote -v
```

위에 명령어를 실행하면 아래와 같은 결과를 확인할 수 있습니다.

```bash
origin  https://github.com/USER_NAME/FORK_REPOSITORY.git (fetch)
origin  https://github.com/USER_NAME/FORK_REPOSITORY.git (push)
```

로컬은 당연히 Fork한 저장소를 Clone하였으므로 위와 같은 결과를 확인할 수 있습니다. 이제 아래에 명령어를 사용하여 원본 저장소를 로컬의 원격 주소에 추가합니다.

```bash
git remote add upstream https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git
```

보통 `upstream`이라는 이름으로 원본 저장소를 추가합니다만, 단지 해당 저장소에 이름을 부여하는 것이기 때문에 다른 이름을 부여할 수 있습니다.

```bash
git remote add test https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git
```

여기에서는 `upstream`이라고 명명한 상태로 진행하도록 하겠습니다. 아래에 명령어를 실행하여 원본 저장소가 원격 주소에 잘 추가되었는지 확인합니다.

```bash
git remote -v
```

문제없이 잘 추가하였다면 아래와 같은 결과를 확인할 수 있습니다.

```bash
origin    https://github.com/USER_NAME/FORK_REPOSITORY.git (fetch)
origin    https://github.com/USER_NAME/FORK_REPOSITORY.git (push)
upstream  https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git (fetch)
upstream  https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git (push)
```

{% include in-feed-ads.html %}

## 원본 저장소 내용 가져오기

로컬의 원격 주소에 원본 저장소를 추가하였습니다. 이제 `Fetch`를 사용하여 원격 저장소의 내용을 로컬에 가져오도록 하겠습니다.

아래에 명령어를 실행하여 원격 저장소의 내용을 가져옵니다.

```bash
git fetch upstream master
```

## Rebase

현재 로컬의 Master 브랜치는 Fork한 저장소를 Clone하였으므로, Fork 저장소의 Master 브랜치를 Base로 하고 있습니다. 이제 `Rebase`를 통해 로컬의 Master 브랜치가 `Fetch`로 가져온 원본 저장소의 Master 브랜치를 Base로 하도록 변경합니다.

아래에 명령어를 사용하여 로컬의 Master 브랜치의 Base를 원본 저장소의 Master 브랜치로 변경합니다.

```bash
git rebase upstream/master
```

이제 로컬의 Master 브랜치의 Base는 원본 저장소의 Master 브랜치가 되었습니다.

## Fork 브랜치 동기화

Rebase를 통해 현재 로컬의 Master 브랜치는 원본 저장소의 Master 브랜치로 변경이 되어있는 상태입니다. 이제 Fork한 원격 저장소도 원본 저장소의 Master 브랜치로 변경해야 합니다.

아래에 명령어를 통해 Fork한 원격 저장소의 Master 브랜치를 원본 저장소의 Master 브랜치로 동기화합니다.

```bash
git push origin master -f
```

## 완료

업무중이나 오픈 소스의 기여할 때, 이렇게 종종 저장소를 동기화할 때가 발생합니다. 여러분도 Rebase를 통해 Fork한 저장소를 동기화해 보시기 바랍니다.
