---
layout: 'post'
permalink: '/jekyll/jekyll-last-modified-at/'
paginate_path: '/jekyll/:num/jekyll-last-modified-at/'
lang: 'ko'
categories: 'jekyll'
comments: true

title: 'jekyll-last-modified-at'
description: '파일의 마지막 수정일을 sitemap.xml에 사용해보자.'
image: '/assets/images/category/jekyll/jekyll-last-modified-at.jpg'
---

## 개요
지금 관리하고 있는 블로그의 ```sitemap.xml```에

```<lastmod>{% raw %}{{ site.time | date: '%Y-%m-%d' }}{% endraw %}</lastmod>```

를 사용하여 빌드된 시점에 시간을 모든 페이지에 적용하고 있었습니다. 하지만 실제 갱신하지 않은 파일도 빌드한 시점에 시간이 들어가므로 그 모든 파일을 크롤링하느라 실제 갱신한 파일의 크롤링이 늦어지지 않을까 싶은 의문이 들었습니다. 그래서 ```jekyll-last-modified-at``` 플로그인을 이용하여 실제로 파일이 수정된 경우만 ```sitemap.xml```에 반영되도록 변경하기로 했습니다.

## 플러그인
아래에 링크를 클릭하여 ```jekyll-last-modified-at``` 사이트로 이동하면 모든 설명이 자세히 나와있습니다. 한번 따라해 보도록 하겠습니다.

- jekyll-last-modified-at: [https://github.com/gjtorikian/jekyll-last-modified-at](https://github.com/gjtorikian/jekyll-last-modified-at){:rel="nofollow noreferrer" :target="_blank"}

## 플러그인 설치
아래에 명령어를 이용하여 ```jekyll-last-modified-at``` 플러그인을 설치합니다.

```bash
gem install jekyll-last-modified-at
```

## 플로그인 사용법
파일 수정일을 표시하고 싶은 부분에 아래에 코드중 원하는 형식을 선택하여 삽입합니다.

```html
{% raw %}
{% last_modified_at %}

{% last_modified_at %Y:%B:%A:%d:%S:%R %}

{{ page.last_modified_at }}

{{ page.last_modified_at | date: '%Y:%B:%A:%d:%S:%R' }}
{% endraw %}
```

우리는 사용하던 ```sitemap.xml```을 아래와 같이 수정하였습니다.

```xml
<!-- <lastmod>{% raw %}{{ site.time | date: '%Y-%m-%d' }}{% endraw %}</lastmod> -->
<lastmod>{% raw %}{{ post.last_modified_at | date: '%Y-%m-%d' }}{% endraw %}</lastmod>
```

## 확인
실제로 프로젝트를 빌드하여 삽입한 코드를 확인해 본 결과, 실제 파일을 수정한 날짜가 잘 들어가 있는 것을 확인하였습니다.

```bash
bundle exec jekyll build
```

구글의 크롤링에 영향이 있을지 모르지만 일단 실제 시간을 표시함으로써 프로그래머로써 일 처리를 한거 같아 기분이 좋습니다.