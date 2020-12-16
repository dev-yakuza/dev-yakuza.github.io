---
layout: 'post'
permalink: '/environment/nvm/'
paginate_path: '/environment/:num/nvm/'
lang: 'ko'
categories: 'environment'
comments: true

title: (macOS) NVM으로 Node 버전 관리하기
description: macOS에 NVM(Node Version Manager)를 설치하고 Node 버전을 관리하는 방법에 대해서 알아봅시다.
image: '/assets/images/category/environment/2020/nvm/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [NVM 설치](#nvm-설치)
- [NVM 설정](#nvm-설정)
- [사용법](#사용법)
  - [Node 버전 리스트](#node-버전-리스트)
  - [Node 설치](#node-설치)
  - [Node 버전 변경](#node-버전-변경)
- [Node 버전 삭제](#node-버전-삭제)
- [프로젝트별 Node 버전 관리하기](#프로젝트별-node-버전-관리하기)
  - [.nvmrc 생성](#nvmrc-생성)
  - [.nvmrc 사용](#nvmrc-사용)
- [완료](#완료)

</div>

## 개요

저는 Mac 유저입니다. Mac에서 여러 프로젝트를 진행하다보니, 프로젝트별 Node 버전을 관리할 필요가 생겼습니다. 이번 블로그 포스트에서는 `NVM(Node Version Manager)`를 사용하여 Node 버전을 관리하는 방법에 대해서 알아봅니다.

- NVM(Node Version Manager): [공식 사이트](https://github.com/nvm-sh/nvm){:rel="nofollow noreferrer" target="_blank"}

여기서 소개하는 방법은 macOS 전용이며, macOS에 `Homebrew`가 설치되었다는 전제하에 설명합니다.

## NVM 설치

아래에 명령어를 사용하여 NVM을 설치합니다.

```bash
brew install nvm
```

{% include in-feed-ads.html %}

## NVM 설정

Terminal에서 NVM을 사용하기 위해서는 `.zshrc` 파일을 수정할 필요가 있습니다. `.zshrc` 파일을 열고 아래와 같이 수정합니다.

```bash
# code ~/.zshrc
...
export NVM_DIR=~/.nvm
source $(brew --prefix nvm)/nvm.sh
```

설정을 완료하였다면 Terminal을 재시작한 후, 아래에 명령어를 실행하여 NVM이 잘 설치되었는지 확인합니다.

```bash
nvm --version
```

설치와 설정에 문제가 없었다면, 아래와 같은 결과를 확인할 수 있습니다.

```bash
0.35.3
```

## 사용법

설치를 완료하였으므로, 이제 NVM을 사용하여 Node 버전을 관리하는 방법에 대해서 알아봅시다.

### Node 버전 리스트

아래에 명령어로 설치가 가능한 Node 버전을 확인할 수 있습니다.

```bash
nvm ls-remote
```

### Node 설치

버전을 확인하였다면, 아래에 명령어를 사용하여 Node를 설치할 수 있습니다.

- 최신 버전의 Node 설치

  ```bash
  nvm install node
  ```

- 최신 버전의 LTS release 설치

  ```bash
  nvm install --lts
  ```

- 특정 버전의 Node 설치

  ```bash
  nvm install 13.12.0
  ```

이렇게 설치하였다면, 아래에 명령어로 현재 설치된 Node 버전들을 확인할 수 있습니다.

```bash
nvm ls
```

{% include in-feed-ads.html %}

### Node 버전 변경

NVM을 사용하여 여러 버전의 Node를 설치하였다면 아래에 명령어를 사용하여, 사용하고자 하는 Node를 선택할 수 있습니다.

```bash
nvm use 13.12.0
```

아래에 명령어를 사용하여 Node 버전이 잘 변경되었는지 확인해 봅니다.

```bash
nvm ls
```

잘 변경되었다면, 아래와 같은 결과를 확인할 수 있습니다.

```bash
       v8.9.0
       v12.16.1
->     v13.12.0
         system
```

## Node 버전 삭제

아래에 명령어를 사용하여 불필요한 Node 버전을 삭제할 수 있습니다.

```bash
nvm uninstall 8.9.0
```

삭제가 완료되면 아래와 같은 결과를 확인할 수 있습니다.

```bash
Uninstalled node v8.9.0
```

## 프로젝트별 Node 버전 관리하기

NVM을 사용하여 Local에 여러 버전의 Node를 설치하고, 사용하는 방법에 대해서 알아보았습니다. 이제 각 프로젝트별로 Node 버전을 관리하는 방법에 대해서 알아봅시다.

### .nvmrc 생성

각 프로젝트별로 Node 버전을 관리하기 위해서는 `.nvmrc` 파일을 생성할 필요가 있습니다. 프로젝트의 Root 폴더에 `.nvmrc` 파일을 생성하고 아래와 같이 수정합니다.

```bash
12.16.1
```

{% include in-feed-ads.html %}

### .nvmrc 사용

이렇게 설정한 Node 버전을 사용하기 위해서, 아래에 명령어를 `.nvmrc` 파일이 존재하는 폴더에서 실행합니다.

```bash
nvm use
```

만약 `.nvmrc` 파일에 설정된 Node 버전이 Local 환경에 존재하는 경우 아래와 같은 결과를 확인할 수 있습니다.

```bash
Found '/projects/.nvmrc' with version <12.16.1>
Now using node v12.16.1 (npm v6.13.4)
```

만약 Local 환경에 존재하지 않는 경우 아래와 같은 결과를 확인할 수 있습니다.

```bash
Found '/projects/.nvmrc' with version <8.9.0>
N/A: version "8.9.0 -> N/A" is not yet installed.

You need to run "nvm install 8.9.0" to install it before using it.
```

위와 같이 `.nvmrc` 파일에 있는 Node 버전이 없는 경우, 아래에 명령어를 사용하여 Node 버전을 설치할 수 있습니다.

```bash
nvm install
```

설치가 완료되면 아래와 같은 화면을 볼 수 있습니다.

```bash
...
Checksums matched!
Now using node v8.9.0 (npm v5.5.1)
```

## 완료

이번 블로그 포스트에서는 NVM(Node Version Manager)를 사용하여 Local에 여러 버전의 Node를 설치하는 방법과 사용 방법을 살펴보았습니다. 또한, 프로젝트별 Node 버전을 관리하기 위해 `.nvmrc` 파일을 생성하고, `.nvmrc` 파일을 사용하여 Node 버전을 설치, 사용하는 방법에 대해서도 알아보았습니다.

이제 .nvmrc 파일을 사용하여 프로젝트별 Node 버전을 관리해 봅시다!
