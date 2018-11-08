---
layout: 'post'
permalink: '/jekyll/pagination-plugin/'
paginate_path: '/jekyll/:num/pagination-plugin/'
lang: 'ko'
categories: 'jekyll'
comments: true

title: 'pagination 플러그인'
description: 'pagination 플러그인을 사용하여 jekyll 프로젝트에 페이지 기능을 추가해보자.'
image: '/assets/images/category/jekyll/pagination.jpg'
---

## 개요
jekyll은 기본적으로 pagination 플러그인을 제공하지만 우리는 [jekyll-paginate-v2](https://github.com/sverrirs/jekyll-paginate-v2){:rel="nofollow noreferrer" :target="_blank"}을 사용하고 있습니다.
이 블로그는 jekyll-paginate-v2의 사용법에 관해 설명합니다.

## 플러그인 설치 및 설정
jekyll-paginate-v2 플러그인을 설치하고 프로젝트에 설정합니다.

### 플러그인 설치
아래에 명령어로 jekyll-paginate-v2 플러그인을 설치합니다.

{% include_relative common/installation.md %}

### 플러그인 설정
아래에 설정 내용을 ```_config.yml``` 파일에 작성합니다.

{% include_relative common/config_yml.md %}

- permalink: 페이지의 기본 링크입니다. 이 링크가 없으면 플러그인이 제대로 동작하지 않습니다.
- pagination: 플러그인의 설정 옵션들입니다. 자세한 사항은 공식 사이트를 참고하세요.([jekyll-paginate-v2:options](https://github.com/sverrirs/jekyll-paginate-v2/blob/master/README-GENERATOR.md){:rel="nofollow noreferrer" :target="_blank"})
- enabled: 플러그인을 활성화합니다.
- per_page: 한 페이지에 표시할 갯수를 나타냅니다.
- sort_reverse: 역정렬을 할지 여부를 나타냅니다. 우리는 최신순으로 표시하기 위해 ```true```로 설정합니다.
- sort_field: 정렬시 사용할 필드입니다. 우리는 최신순으로 표시하기 위해 ```date``` 필드를 이용합니다.
- title: pagination으로 생성된 페이지의 제목을 나타냅니다. ```page.title```변수에 할당될 값을 설정합니다.(ex> :title - page :num)
- trail: 선택된 페이지에 앞/뒤에 몇 페이지를 표시할지 설정합니다.

## 페이지 설정
페이지에 pagination을 표시하기 위한 설정입니다. pagination을 가지고 있는 페이지와 해당 페이지에서 호출된 페이지안에 설정을 해야합니다.

### pagination을 가지고 있는 페이지
pagination을 표시하기 위해 해당 pagination 기능이 필요한 페이지(ex> category 페이지)에 아래와 같이 설정합니다.

{% include_relative common/page_setting.md %}

- enabled: pagination 기능을 사용합니다.
- category: 해당 카테고리의 포스트를 pagination합니다.
- permalink: pagination 기능으로 생성된 페이지의 링크를 설정합니다.(ex> /:num/)

### pagination 페이지에서 호출될 페이지
호출될 페이지(ex> post 페이지)에 아래와 같이 설정합니다.

{% include_relative common/called_page_setting.md %}

- paginate_path: pagination에 의해 호출될 때 페이지 번호를 링크에 포함하기 위한 설정입니다.

## 참고
- 공식 사이트: [jekyll-paginate-v2](https://github.com/sverrirs/jekyll-paginate-v2/blob/master/README-GENERATOR.md){:rel="nofollow noreferrer" :target="_blank"}
- 공식 사이트의 옵션 설명: [jekyll-paginate-v2:options](https://github.com/sverrirs/jekyll-paginate-v2/blob/master/README-GENERATOR.md){:rel="nofollow noreferrer" :target="_blank"}