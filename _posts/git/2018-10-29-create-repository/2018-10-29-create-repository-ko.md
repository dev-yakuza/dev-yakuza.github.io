---
layout: 'post'
permalink: '/git/create-repository/'
paginate_path: '/git/:num/create-repository/'
lang: 'ko'
categories: 'git'
comments: true

title: '저장소(Repository) 생성'
description: 'git를 사용하기 위해 git의 저장소(Repository)를 생성합니다. git의 저장소(Repository)는 소스 코드의 버전을 관리하기 위한 저장 장소입니다.'
image: '/assets/images/category/git/create-repository.jpg'
---

## 개요
git을 설치했으니 이제 git을 사용해서 소스 코드의 버전을 관리해야겠죠? 여기에서는 git에서 소스 코드를 관리하기 위한 저장소(Repository)를 생성 방법에 대해서 알아봅니다. git의 저장소(Repository)는 소스 코드 버전에 대한 이력을 저장하기 위한 별도의 저장 장소를 의미합니다.

## 프로젝트 폴더 생성
Mac은 ```terminal```, Windows는 ```cmd```를 사용하여 진행합니다. git을 활용하기 위한 폴더를 생성합니다.

```bash
mkdir temp_test_git
```
## git 저장소(Repository) 생성
git을 사용하기 위해 생성한 프로젝트 폴더에 git의 저장소(Repository)를 생성합니다.

```bash
cd temp_test_git

git
```
위에 명령어로 git에서 사용 가능한 명령어 리스트를 확인합니다.

![git clone init](/assets/images/category/git/create-repository/clone_init.png)

git 명령어를 확인하면 위와 같이 git의 저장소(Repository)를 ```clone```을 할지 ```init``` 할지 선택하는 명령어를 확인할 수 있습니다.

- init: 새로운 git 저장소(Repository)를 생성합니다.
- clone: 기존에 git의 저장소(Repository)를 복사하여 생성합니다.

### git init
새로운 프로젝트로 시작하는 경우는, ```init``` 명령어를 사용하여 git의 저장소(Repository)를 생성합니다.

```bash
git init
```

### git clone
기존에 존재하는 프로젝트(opensource 또는 기존에 git으로 버전 관리를 하고 있는 프로젝트)가 있는 경우 외부 저장소(Remote Repository)에서 ```clone``` 명령어를 사용하여 저장소(Repository)를 가져옵니다.

우리의 블로그 git 저장소(Repository)를 clone하는 것을 예로 들어 설명하겠습니다.

- git 저장소(Repository): [https://github.com/dev-yakuza/dev-yakuza.github.io](https://github.com/dev-yakuza/dev-yakuza.github.io){:rel="nofollow noreferrer" :target="_blank"}

위에 링크를 눌러 github에서 저장하고 있는 우리의 git 저장소(Repository)로 이동합니다.

![git clone blog](/assets/images/category/git/create-repository/clone.png)

오른쪽에 ```Clone or donwload``` 버튼을 누르면 git 저장소(Repository)의 URL을 복사할 수 있습니다.

```bash
 git clone https://github.com/dev-yakuza/dev-yakuza.github.io.git
```

위에 명령어를 실행하면 우리 블로그의 git 저장소(Repository)가 local PC에 복사됩니다. 참고로 우리 블로그는 ```jekyll```을 이용하여 무료로 서비스하고 있습니다. 관심있으신 분은 [jekyll blog]({{site.url}}/jekyll/){:target="_blank"}를 참고하세요.


## git 저장소(Repository) 생성 확인
git 저장소(Repository)가 잘 생성됐는지 확인하기 위해 아래에 명령어를 입력합니다.

```bash
# Mac
ls -al

# Windows
dir /ah
```

표시되는 리스트에 ```.git```폴더가 보이면 git 저장소(Repository) 생성에 성공한 것입니다. ```.git``` 폴더는 git을 사용하여 소스 코드 버전을 관리하면 그에 해당 되는 정보들이 저장되는 장소입니다. ```.git``` 폴더를 삭제하면 git 저장소(Repository)에 저장한 내용이 전부 삭제되므로 삭제하지 않도록 주의해 주세요.