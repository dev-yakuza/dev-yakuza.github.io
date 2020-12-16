---
layout: 'post'
permalink: '/react-native/splash-image/'
paginate_path: '/react-native/:num/splash-image/'
lang: 'ko'
categories: 'react-native'
comments: true

title: 'Splash 이미지'
description: 'generator-rn-toolbox을 이용하여 Splash 이미지를 설정하자.'
image: '/assets/images/category/react-native/splash-image.jpg'
---

<div id="contents_list" markdown="1">

## 목차

1. [Deprecated](#deprecated)
1. [개요](#개요)
1. [라이브러리 설치](#라이브러리-설치)
1. [이미지 준비하기](#이미지-준비하기)
    - [sketchapp에서 psd 파일 생성](#sketchapp에서-psd-파일-생성)
1. [splash 설정하기](#splash-설정하기)
1. [확인](#확인)
1. [에러 대응](#에러-대응)
    - [이미지 생성 불가](#이미지-생성-불가)
1. [Splash 이미지 다루기](#splash-이미지-다루기)
1. [참고](#참고)

</div>

## Deprecated

이 블로그 포스트는 generator-rn-toolbox가 `Deprecated`되었기 때문에 더이상 관리되지 않습니다. generator-rn-toolbox의 새로운 라이브러리인 `react-native-make`를 사용하시길 권장합니다.

react-native-make에 관해서는 아래에 블로그를 참고하시기 바랍니다.

- [react-native-make]({{site.url}}/{{page.categories}}/react-native-make/){:target="_blank"}

## 개요

mac osx에서 [generator-rn-toolbox](https://github.com/bamlab/generator-rn-toolbox){:rel="nofollow noreferrer" target="_blank" }를 사용하여 splash 이미지를 만드는 방법을 설명하겠습니다.

## 라이브러리 설치

generator-rn-toolbox 라이브러리 설치는 이전 블로그 [App icon]({{site.url}}/{{page.categories}}/app-icon/){:target="_blank"}을 참고하시기 바랍니다.


## 이미지 준비하기

splash 이미지로 사용할 2208x2208px 사이즈에 psd 파일을 준비합니다.

### sketchapp에서 psd 파일 생성

우리는 디자인에 sketchapp을 사용합니다. sketchapp은 psd파일을 내보낼 수 없으므로 이미지 준비하기 불가능합니다. 하지만 아래에 방법을 통해 psd 파일을 준비할 수 있습니다.

1. sketchapp으로 splash 이미지 디자인하기
1. 디자인한 splash 이미지를 png로 내보내기
1. 인터넷에서 png to psd converter를 검색하여 온라인 변환 사이트를 찾습니다.(우리가 사용한 [사이트](https://www.photopea.com/){:rel="nofollow noreferrer" target="_blank" })

{% include in-feed-ads.html %}

## splash 설정하기

아래에 명령어를 이용하여 각 os에 맞는 splash 이미지를 생성합니다.

{% include_relative common/usage.md %}

## 확인

splash 이미지가 생성되어 프로젝트에 반영되었습니다. 프로젝트를 실행하여 splash 이미지가 반영되었는지 확인하세요.

{% include_relative common/start_project.md %}

splash 이미지가 제대로 표시되지 않는 경우 시뮬레이터/단말기에서 어플을 지우고 다시 실행해 보시길 바랍니다.

## 에러 대응

안드로이드(Android)에서 splash 이미지가 전체 사이즈로 표시되지 않는 문제가 발생했습니다. 그래서 ```android/app/src/main/res/drawable/launch_screen_bitmap.xml```을 아래와 같이 변경하였습니다.

```xml
<bitmap
    android:src="@drawable/launch_screen"
    android:gravity="fill_horizontal|fill_vertical"/>
```

### 이미지 생성 불가

아래와 같은 에러가 나오면서 이미지 생성이 되지 않은 문제가 발생했습니다.

```bash
Error: Command failed: identify: FailedToExecuteCommand `'gs'
```

아래에 명령어를 통해 ```ghostscript```를 설치합니다.

```bash
brew install ghostscript
```

다시 아래에 명령어를 실행할 경우, 정상 동작하는 것을 확인하실 수 있습니다.

{% include_relative common/usage.md %}

{% include in-feed-ads.html %}

## Splash 이미지 다루기

앱에서 Splash 이미지를 다룰 경우가 있습니다. Splash 이미지를 화면에 표시하고 그 동안 로그인을 체크한다던지, 데이터를 가져올 경우가 있습니다. 이렇게 Splash 이미지를 다룰 필요가 있다면 아래에 블로그를 참고하여 Splash 이미지를 컨트롤하시기 바랍니다.

- [App Splash 스크린]({{site.url}}/{{page.categories}}/react-native-splash-screen/){:target="_blank"}

## 참고

- 공식 사이트: [generator-rn-toolbox](https://github.com/bamlab/generator-rn-toolbox){:rel="nofollow noreferrer" target="_blank" }
