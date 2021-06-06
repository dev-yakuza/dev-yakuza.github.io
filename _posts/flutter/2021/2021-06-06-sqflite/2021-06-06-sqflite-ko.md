---
layout: 'post'
permalink: '/flutter/widget/sqflite/'
paginate_path: '/flutter/:num/widget/sqflite/'
lang: 'ko'
categories: 'flutter'
comments: true

title: '[Flutter] SQLite'
description: 이번 블로그 포스트에서는 Flutter에서 SQLite를 사용하는 방법에 대해서 살펴봅시다.
image: '/assets/images/category/flutter/background.png'
published: false
---

<div id="contents_list" markdown="1">

## 목차

</div>

## 개요

이번 블로그 포스트에서는, Flutter에서 사용자 디바이스에 데이터를 저장하기 위해 `SQLite`를 사용하는 방법에 대해서 알아봅시다. Flutter에서 `SQLite`를 사용하기 위해서는 `sqflite` 패키지를 사용합니다.

- sqflite: [https://pub.dev/packages/sqflite](https://pub.dev/packages/sqflite){:rel="nofollow noreferrer" target="_blank"}

Flutter의 공식 문서에도 `sqflite`을 사용하는 방법에 대해 나와있습니다. 아래에 링크를 통해 공식 문서를 참고하시기 바랍니다.

- 공식 문서: [https://flutter.dev/docs/cookbook/persistence/sqlite](https://flutter.dev/docs/cookbook/persistence/sqlite){:rel="nofollow noreferrer" target="_blank"}

## Shared preferences

SQLite는 복잡한 데이터를 사용자의 디바이스에 저장하기 위해 사용됩니다. 사용자의 디바이스의 간단한 데이터를 `키-값` 형태를 저장할 때에는 `shared_preferences` 패키지를 사용합니다.

`shared_preferences` 패키지를 사용하는 방법에 대해서는 아래에 링크를 참고하시기 바랍니다.

- [[Flutter] Shared preferences]({{site.url}}/{{page.categories}}/installation/){:target="_blank"}

## sqflite 설치

Flutter에서 SQLite를 사용하기 위해 `sqflite` 패키지를 설치할 필요가 있습니다. 다음 명령어를 실행하여 `sqflite` 패키지를 설치합니다.

```bash
flutter pub add sqflite
```


{% include in-feed-ads.html %}


## 완료

이것으로 Flutter에서 통합 테스트를 하기 위한 준비와, 통합 테스트를 작성하는 방법, 그리고 통합 테스트를 실행하는 방법에 대해서 알아보았습니다. 이제 여러분도 실제 환경에서 여러분의 앱을 테스트해 보시기 바랍니다.
