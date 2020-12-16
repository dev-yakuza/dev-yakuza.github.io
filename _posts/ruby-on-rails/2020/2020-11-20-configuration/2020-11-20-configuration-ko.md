---
layout: 'post'
permalink: '/ruby-on-rails/configuration/'
paginate_path: '/ruby-on-rails/:num/configuration/'
lang: 'ko'
categories: 'ruby-on-rails'
comments: true

title: 'Rails 설정 파일'
description: 'Ruby on Rails에서 사용되는 설정 파일은 무엇이 있는지 살펴보고, 해당 설정 파일들을 어떻게 사용하는지 살펴보도록 하겠습니다.'
image: '/assets/images/category/ruby-on-rails/2020/configuration/background.jpg'
published: false
---

<div id="contents_list" markdown="1">

## 목차

</div>

## 개요

Rails에서 사용되는 각종 설정들은 `./config` 폴더에 보관되어 있습니다. 이번 블로그 포스트에서는 Rails에서 각종 설정들을 다루는 방법에 대해서 살펴봅니다.

## 주요 설정 파일

Rails에서 설정 파일들은 `./config` 폴더에 존재합니다. 다음은 Rails에서 자주 사용되는 주요 설정 파일들입니다.

```bash
config
├── application.rb
├── environments
│   ├── development.rb
│   ├── production.rb
│   └── test.rb
├── initializers
│   ├── backtrace_silencers.rb
│   ├── filter_parameter_logging.rb
│   ├── inflections.rb
│   └── mime_types.rb
└── locales
```

위에 파일들을 설명하면 다음과 같습니다.

- application.rb: 모든 환경에서 공통적으로 사용되는 설정 파일
- environment: 각 환경에 따른 설정 파일들
  - development.rb: 개발 환경에서의 설정 파일
  - production.rb: 배포 환경에서의 설정 파일
  - test.rb: 테스트 환경에서의 설정 파일
- initializers: 위에 설정 이외에 초기화 처리 또는 설정 정보
  - backtrace_silencers.rb: 예외 백트레이스 파일
  - filter_parameter_logging.rb: 출력하지 않을 로그를 지정하는 매개 변수
  - inflections.rb: 단수형/복수형 변환 규칙
  - mime_types.rb: 애플리케이션에서 이용할 수 있는 MIME 타입 설정
- locales: 국제화 대응을 위한 리소스 파일

{% include in-feed-ads.html %}

## 주요 설정 매개 변수

각 환경에 따른 설정 파일들은 `environment/development.rb`, `environment/production.rb`, `environment/test.rb`에 설정할 수 있습니다. 해당 파일에서 설정할 수 있는 주요 설정 매개 변수는 다음과 같습니다.

| 종류 | 매개 변수 이름 | 설명 | 기본값 |
| -- | -- | -- | -- |
| 기본 | cache_classes | 애플리케이션 클래스를 캐시할지 여부 | 개발/테스트: false, 배포: true |
| 기본 | cache_store | 캐시 저장 장소 설정(:memory_store, :file_store, :mem_cache_store 등) | - |
| 기본 | colorize_logging | 로그 정보에 색을 입혀 표시할지 여부 | true |
| 기본 | autoload_paths | 추가로 로드 대상이 되는 경로 | - |
| 기본 | asset_host | 에셋 헬퍼 호스트 이름 | - |
| 기본 | log_level | 로그 레벨 | :debug |
| 기본 | logger | 사용할 로거의 종류 | nil |
| 기본 | time_zone | 애플리케이션 또는 액티브 레코드에서 사용할 기본 타임존 | - |
| 기본 | i18n.default_locale | 국제화 대응에 사용할 기본 로케일 | :en |
| 액티브 레코드 | active_record.logger | 사용할 로거의 종류 | - |
| 액티브 레코드 | active_record.schema_format | 스키마 덤프 형식(:ruby, :sql) | :ruby |
| 액티브 레코드 | active_record.timestamped_migration | 마이그레이션 파일을 타임스탬프로 관리할지 여부 | true |
| 액션 컨트롤러 | action_controller.default_charset | 기본 문자 코드 | utf-8 |
| 액션 컨트롤러 | action_controller.logger | 사용할 로거 | - |
| 액션 컨트롤러 | action_controller.perform_caching | 캐시 기능을 유효화할지 여부 | - |
| 액션 컨트롤러 | session_store | 세션을 저장할 저장소 이름(:cookie_store, :mem_chache_store, :disabled) | - |
| 액션 뷰 | action_view.default_form_builder | 기본적으로 사용할 입력 양식 빌더 | ActionView::Helpers::FormBuilder |
| 액션 뷰 | action_view.logger | 사용할 로거 | - |
| 액션 뷰 | action_view.field_error_proc | 오류가 발생했을 때 입력 요소를 묶을 태그 | - |

{% include in-feed-ads.html %}

## 커스텀 환경 설정

애플리케이션에서 사용할 고유의 설정 정보는 `./config` 폴더에 새로운 파일을 만들어 관리하는 것을 추천합니다. 예를 들어 `./conf/my_config.yml` 파일을 생성하고 아래와 같이 만들 수 있습니다.

```yml
COMMON: &COMMON
  author: "dev-yakuza"
  details: "This is a test app"

development:
  hoge: "dev"
  <<: *COMMON

test:
  hoge: "test"
  <<: *COMMON

production:
  hoge: "pro"
  <<: *COMMON
```

각 환경에 공통으로 사용될 환경 변수는 `COMMON`이라는 키의 `&COMMON`을 사용하여 YML 파일내에서 참조가 가능하게 설정하였습니다. `COMMON`의 내용을 `<<: *COMMON`을 사용하여 참조하여 필요한 곳에서 추가하였습니다.

이렇게 작성한 파일은 초기화 파일에서 명시적으로 실행하도록 지정해야 합니다. `./config/initializers` 폴더 내에 `my_config.rb`를 만들고 다음과 같이 수정합니다

```rb
MY_APP = YAML.load(File.read("#{Rails.root}/config/my_config.yml"))[Rails.env]
```

이렇게 설정 파일을 불러오면 Rails 애플리케이션 안에서 다음과 같이 사용할 수 있습니다.

```rb
author = MY_APP['author']
```

## 완료

이번 블로그 포스트에서는 Rails의 환경 설정 파일들을 확인해 보았습니다. 또한 기본적으로 제공하는 환경 변수이외에도 애플리케이션에서 필요한 환경 변수를 선언하는 방법에 대해서 알아보았습니다.

이제 여러분도 각 환경에 맞는 설정 파일들을 설정하여, 여러 환경에서 동작할 수 있는 Rails 애플리케이션을 제작해 보시기 바랍니다.
