---
layout: 'post'
permalink: '/git/installation/'
paginate_path: '/git/:num/installation/'
lang: 'ko'
categories: 'git'
comments: true

title: 'git 설치'
description: '소스 코드의 버전 관리를 위해 git을 사용하려고 합니다. git을 사용하기 위해 git을 설치합니다.'
image: '/assets/images/category/git/installation.jpg'
---

## 소스 코드 버전 관리
git은 소스 코드의 버전을 관리합니다. 버전을 관리한다는 의미는 소스 코드에 변경 이력을 저장하고 관리한다는 의미입니다. 소스 코드 변경이 잘못되어 변경 전 소스로 돌아가고 싶지만 어디를 어떻게 바꿔는지 기억이 나질 않아 고생하신 적이 있으신가요? git과 같은 소스 코드 버전 관리툴은 이런 상황을 위해 만들어 졌습니다. 하지만 ```ctrl + z```같은 기능처럼 특정 키를 누르면 소스 코드가 변경전으로 돌아가는 그런 마법같은 툴은 아닙니다.

소스 코드 버전 관리툴은 개발자가 소스 코드를 변경한 후에 소스 코드 버전 관리툴을 이용해서 변경 이력과 소스를 다른 곳(Repository)에 저장합니다. 그리고 소스 코드를 변경 전으로 되돌리고 싶으면 변경 이력을 저장한 다른 곳(Repository)에서 변경 전 소스를 불러옵니다. 이런 식으로 버전을 관리합니다.

git은 소스코드 버전 관리툴중 하나로써 많은 기능들이 있습니다. 저도 많은 기능중 일부를 사용하고 있으며, 사실 다른 기능들이 뭐가 있는지 잘 몰라 이 블로그를 시작했습니다. 지금부터 git을 공부하며 배운 내용을 정리하겠습니다. 여러분들에게 도움이 됐으면 좋겠네요.

## git 설치
git을 사용하기 위해서는 먼저 git을 PC에 설치해야합니다. OS에 맞는 설치법을 따라해서 git을 설치해 주세요.

## git을 Mac에 설치
git을 Mac에 설치하기 위해 아래에 링크를 클릭해 설치 파일을 다운로드합니다.

- 다운로드 링크: [https://git-scm.com/download/mac](https://git-scm.com/download/mac){:rel="nofollow noreferrer" :target="_blank"}

자동으로 다운로드가 시작되지 않으시면 ```click here to download manually``` 링크를 눌러 다운로드를 해 주세요.

![git download for mac](/assets/images/category/git/installation/download_mac.png)

파일 다운로드가 완료되면 파일을 클릭하여 설치합니다. 설치 방법은 웹에서 다운로드한 일반적인 Mac 소프트웨어 설치와 동일합니다. 보안 경고가 나오면 Mac 설정에서 확인후에 설치합니다.

설치가 완료되면 ```termial```을 실행하고 아래에 코드로 설치가 되었는지 확인합니다.

```bash
git --version
```

## git을 Windows에 설치
git을 Windows에 설치하기 위해 아래에 링크를 클릭해 설치 파일을 다운로드합니다.

- 다운로드 링크: [https://gitforwindows.org/](https://gitforwindows.org/){:rel="nofollow noreferrer" :target="_blank"}

![git download for windows](/assets/images/category/git/installation/download_windows.png)

다운로드가 완료되면 일반 프로그램 설치와 동일한 방법으로 설치합니다.

설치가 완료되면 ```명령 프롬프트(cmd)```을 실행하고 아래에 코드로 설치가 되었는지 확인합니다.

```bash
git --version
```
명령 프롬프트는 ```윈도우키 + r```을 누르고 ```cmd```를 입력하고 엔터를 눌러 실행시킵니다.

## 완료
설치가 완료되었습니다. 이제 git을 사용하여 소스 버전 관리에 대해서 알아봅시다.