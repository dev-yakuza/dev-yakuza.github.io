---
layout: 'post'
permalink: '/jekyll/preview-speed-up/'
paginate_path: '/jekyll/:num/preview-speed-up/'
lang: 'ko'
categories: 'jekyll'
comments: true

title: '블로그 미리보기를 빠르게'
description: '지킬(jekyll)로 작성하고 있는 글을 빠르게 확인하는 방법에 대해서 알아봅시다.'
image: '/assets/images/category/jekyll/preview-speed-up.jpg'
---

## 문제점
지금 지킬(jekyll)로 관리하고 있는 블로그가 작성한 글이 많아지면서 로컬에서 작성한 글을 확인하는 과정에서 시간이 많이 걸리게 되었습니다. 저는 아래에 지킬(jekyll) 명령어로 글을 공개하기전에 로컬에서 작성한 글을 확인하고 있습니다.

```bash
bundle exec jekyll serve
```

그러나 글에 양이 많고 사용하는 플러그인이 많다 보니 글을 확인하기 위해서 ```209.498985 seconds```를 기다려야 하는 문제가 발생하였습니다. 배포하기 위해 빌드 시간이 이정도면 상관없지만 새로 작성한 글을 확인할 때마다 이만큼의 시간이 걸리는건 조금 낭비라는 생각이 들었습니다.

## 해결책
많은 해결책이 있을거 같지만 저는 아래에 지킬(jekyll) 설정으로 빌드 속도를 향상시켰습니다.

우선 ```_config.yml```을 복사하여 ```_config-dev.yml```을 만들었습니다. 그리고 아래에 코드를 추가하였습니다.

```yml
# 다국어를 사용하기 때문에 3 설정. 보통 1을 설정하면 됨.
limit_posts: 3
```

그리고 작성한 글을 확인하기 위해 아래에 지킬(jekyll) 명령어를 사용합니다.

```bash
bundle exec jekyll serve --config _cong-dev.yml
```

이 코드는 하나에 블로그 포스트만을 빌드하도록 만듭니다. 저는 이 지킬(jekyll) 설정을 사용하니 ```74.639 seconds```만 기다리면 작성한 글을 확인할 수 있게 되었습니다. 또한 지킬(jekyll) 플러그인 중 시간이 많이 걸리는 ```minify``` 플러그인을 사용하지 않도록 아래와 같이 설정하였습니다.

```yml
jekyll-minifier:
  remove_spaces_inside_tags: false
  remove_multi_spaces: false
  remove_comments: false
  compress_css: false
  compress_javascript: false
  compress_json: false
```

이렇게 설정하니 빌드 시간이 ```50.668 seconds```, 20초 가량 빨라졌습니다.

## 완료
위에서 설명한 방법으로 200초에서 50초로 시간이 1/4로 감소하였습니다. 하지만 여전히 50초라는 시간이 걸리네요. 이건 지킬(jekyll) 블로그에 큰 문제점인거 같습니다.