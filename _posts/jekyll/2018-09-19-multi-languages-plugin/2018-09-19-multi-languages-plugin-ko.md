---
layout: 'post'
permalink: '/jekyll/multi-languages-plugin/'
paginate_path: '/jekyll/:num/multi-languages-plugin/'
lang: 'ko'
categories: 'jekyll'
comments: true

title: '다국어 플러그인'
description: 'jekyll에서 다국어를 대응하기 위해 사용하는 플러그인을 소개합니다. 다국어 플러그인 jekyll-polyglot의 설치와 설정에 대해서 알아봅니다.'
image: '/assets/images/category/jekyll/multi-languages-plugin.jpg'
---


## 다국어 플러그인
jekyll에 다국어를 지원하기 위한 플러그인 설치와 설정에 대해 알아봅니다. 여러 다국어 플러그인이 있지만 여기에서는 [jekyll-polyglot](https://github.com/untra/polyglot){:rel="nofollow noreferrer" target="_blank"}를 소개합니다.

다른 다국어 플러그인에 대해 궁금하신 분은 [awesome-jekyll-plugins](https://github.com/planetjekyll/awesome-jekyll-plugins#multi-language--multi-lingual){:rel="nofollow noreferrer" target="_blank"}을 참고하세요.

## 플러그인 설치
- 콘솔에서 아래에 명령어를 통해 플러그인을 설치합니다.

{% include_relative common/install_plugin.md %}

- ```_config.yml```에 플러그인을 세팅합니다.

{% include_relative common/set_plugin.md %}

## 플러그인 글로벌 설정
```_config.yml``` 파일에 아래와 같이 설정합니다.

{% include jekyll/configuration_multi_languages.md %}

- languages: 사이트에서 지원할 다국어 리스트입니다.
- default_lang: 지원하는 다국어중 디폴트 언어를 설정합니다.
- exclude_from_localization: 다국어를 지원하지 않을 폴더 리스트를 설정합니다.
- parallel_localization: true로 설정하면 jekyll이 페이지를 컴파일할 때 fork()를 이용해 사이트를 동시에 컴파일 합니다. Windows OS는 fork()를 지원하지 않으므로 false로 설정해야합니다.

## 페이지 설정

- ```_posts```폴더에 아래와 같이 폴더와 파일을 만듭니다.

{% include_relative common/folder_structure.md %}

- 2018-09-19-multi-languages-plugin: 관리를 위해 ```_posts``` 폴더 하위에 포스트 제목으로 폴더를 만듭니다.
- common: 다국어 파일에서 공통으로 사용할 파일을 저장합니다. 예를 들어 지금 보고 있는 디렉토리 구조는 ```folder_structre.md```에 작성하고 ```{% raw %}{% include_relative common/folder_structure.md %}{% endraw %}```을 이용하여 표시합니다.
- 2018-09-19-multi-languages-plugin-[언어].md: ```_config.yml```의 ```languages```에 설정한 언어별 페이지를 작성합니다.
- 각 언어별 페이지 상단에 해당 페이지의 언어를 설정합니다.

```yml
---
layout: 'post'
lang: 'ko'
...
---
```

## 확인
모든 설정이 완료되었습니다. 각 페이지를 확인하는 방법에 대해 알아봅니다.

- 페이지 설정을 통해 생성된 페이지는 아래와 같은 URL로 접근이 가능합니다.

{% include_relative common/page_link.md %}

- ```_config.yml```의 ```default_lang```에 설정한 언어는 ```http://site_url/path```로 바로 접근이 가능합니다.
- ```default_lang```이외에 언어는 ```http://site_url/[언어]/path```로 해당 언어 페이지에 접근이 가능합니다.
- jekyll의 테스트 서버를 기동하거나 빌드를 하게 되면 ```_site``` 폴더 하위에 다국어로 된 폴더를 확인할 수 있다.
    - 서버 기동 명령어: {% include jekyll/test_server_command.md %}
    - 빌드 명령어: {% include jekyll/build_command.md %}

