---
layout: 'post'
permalink: '/jekyll/github-page/'
paginate_path: '/jekyll/:num/github-page/'
lang: 'ko'
categories: 'jekyll'
comments: true

title: 'github page'
description: '지금까지 만든 jekyll 프로젝트를 github page에 업로드하고 블로그 서비스를 시작해보자.'
image: '/assets/images/category/jekyll/github-page.jpg'
---

## 개요
지금까지 만든 jekyll 프로젝트를 github page에 업로드하여 블로그 서비스를 시작해봅시다. 기본적인 소스는 [bitbucket](https://bitbucket.org/){:rel="nofollow noreferrer" target="_blank"}에서 관리할 예정이고 jekyll에서 build된 static 페이지만 [github](https://github.com/){:rel="nofollow noreferrer" target="_blank"}에 업로드하여 서비스할 예정입니다.

jekyll을 사용하여 프로젝트를 진행하는 방법에 대해 잘 모르시는 분들은 이전 블로그를 확인해 주세요.

### jekyll 프로젝트 생성
- [jekyll 설치]({{site.url}}/{{page.categories}}/installation/){:target="_blank"}
- [테마 설정]({{site.url}}/{{page.categories}}/theme/){:target="_blank"}
- [폴더 구조]({{site.url}}/{{page.categories}}/directory_structure/){:target="_blank"}
- [jekyll 설정]({{site.url}}/{{page.categories}}/configuration/){:target="_blank"}

### jekyll 프로젝트 옵션
- [다국어 플러그인]({{site.url}}/{{page.categories}}/multi-languages-plugin/){:target="_blank"}
- [SEO 지원]({{site.url}}/{{page.categories}}/seo/){:target="_blank"}
- [pagination 플러그인]({{site.url}}/{{page.categories}}/pagination-plugin/){:target="_blank"}
- [Disqus 댓글]({{site.url}}/{{page.categories}}/disqus/){:target="_blank"}
- [이메일 발송 기능]({{site.url}}/{{page.categories}}/send-email/){:target="_blank"}
- [google 서비스]({{site.url}}/{{page.categories}}/google-service/){:target="_blank"}

## bitbucket
bitbucket도 github과 같이 repository를 관리하는 툴입니다. 많은 기능들이 있지만 여기서는 github page에 업로드할 소스를 관리하는 용도로 설명하겠습니다. 자신에 소스를 공개해도 상관없는 분들은 이 부분을 넘어가셔도 됩니다.

아래에 링크를 통해 bitbucket으로 이동합니다.

- bitbucket: [https://bitbucket.org/](https://bitbucket.org/){:rel="nofollow noreferrer" target="_blank"}

### 회원 가입 및 로그인
회원가입과 로그인 부분의 설명은 생략하겠습니다. 보통 서비스 가입과 같은 절차임으로 회원 가입과 로그인을 해주세요.

![bitbucket login](/assets/images/category/jekyll/github-page/bitbucket-login.png)

### Repository 생성
로그인후 아래의 화면과 같은 메뉴가 보이면 ```+````버튼을 눌러주세요.

![bitbucket menu](/assets/images/category/jekyll/github-page/bitbucket-menu.png){:class="narrow-image"}

아래와 같은 메뉴가 보이면 ```Repository```를 눌러 새로운 repository를 생성합니다.

![bitbucket menu repository](/assets/images/category/jekyll/github-page/bitbucket-menu-repository.png){:class="narrow-image"}

repository 정보를 입력합니다.

![bitbucket menu repository information](/assets/images/category/jekyll/github-page/bitbucket-menu-repository-information.png)

repository 생성을 완료했습니다.

### PC에 Repository 연동
개발에 사용하는 PC에 생성된 repository를 연동하여 소스 코드를 관리해 봅시다. git 설치나 사용법에 관해서는 git 블로그를 참고하세요.([git]({{site.url}}/git/){:target="_blank"})

![bitbucket git clone](/assets/images/category/jekyll/github-page/bitbucket-git-clone.png)

repository가 생성이 되면 위와 같은 화면을 볼 수 있습니다. 친절하게도 PC와 연동하는 방법에 대해 잘 나와있습니다. 한번 따라해 봅시다.

{% include_relative common/git-clone.md %}

위에 명령어로 PC에 repository를 clone합니다. 생성된 폴더에 jekyll 프로젝트를 복사합니다.(또는 jekyll 프로젝트를 생성합니다.)

{% include_relative common/git-add-push.md %}

위에 명령어로 local(pc)에 있는 소스를 bitbucket에 있는 repository에 업로드합니다.

[bitbucket 사이트](https://bitbucket.org/){:rel="nofollow noreferrer" target="_blank"}로 이동하여 자신이 추가한 jekyll 프로젝트의 파일이 잘 있는지 확인합니다.

## github page 연동
github page에는 jekyll가 빌드된 static 파일을 업로드하여 블로그를 서비스 합니다.

### 회원 가입 및 로그인
아래에 사이트로 이동하여 회원 가입 및 로그인 합니다. 회원 가입 및 로그인은 일반 서비스 가입과 동일함으로 설명하지 않습니다.

주의: 회원가입시 ```사용자명```에는 주의해주세요. ```https://사용자명.github.io```으로 github page를 서비스할 예정입니다.

- github 사이트: [https://github.com/](https://github.com/){:rel="nofollow noreferrer" target="_blank"}

![github login](/assets/images/category/jekyll/github-page/github-login.png)

### Repository 생성
로그인을 하면 아래와 같은 화면을 볼 수 있습니다. ```Start a project```버튼을 눌러 새로운 프로젝트를 생성합니다.

![github repository](/assets/images/category/jekyll/github-page/github-repository.png)

Repository name에 github에 회원가입 할 때 만든 ```사용자명 + github.io```를 넣고 ```Create repository``` 버튼을 눌러 repository를 생성합니다.

![github crete repository](/assets/images/category/jekyll/github-page/github-create-repository.png)

### PC에 Repository 연동
repository를 생성하면 역시 친절하게 설명이 잘 나와있는 페이지를 볼 수 있습니다. 하지만 우리는 이미 bitbucket과 local을 연동하고 있기 때문에 조금 다른 방식으로 진행합니다.

![github clone repository](/assets/images/category/jekyll/github-page/github-clone-repository.png)

우리는 이미 bitbucket과 연동이 되어 있으므로, 아래에 명령어로 remote repository를 추가합니다.

{% include_relative common/add-remote.md %}

연동이 완료되었습니다. 아래에 명령어로 jekyll이 빌드한 소스만 repository에 업로드합니다.

{% include_relative common/push-subtree.md %}

jekyll이 빌드가 되어 있지 않는 경우 빌드를 해주세요.

{% include jekyll/build_command.md %}

github page가 화면에 표시되는지 확인합니다.

```
https://dev-yakuza.github.io
```

## 마침
현재 소스를 github, bitbucket과 연동하는 방법을 살펴보았습니다. build전 소스는 bitbucket에, build후 static 페이지는 github page에 업로드하여 블로그 서비스를 할 수 있도록 설정했습니다. 이제 여러분도 자신만에 블로그를 시작해보세요.