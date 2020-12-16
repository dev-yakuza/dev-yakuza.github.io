---
layout: 'post'
permalink: '/react-native/app-icon/'
paginate_path: '/react-native/:num/app-icon/'
lang: 'ko'
categories: 'react-native'
comments: true

title: 'App icon'
description: 'generator-rn-toolbox을 이용하여 앱 아이콘을 생성해보자.'
image: '/assets/images/category/react-native/app-icon.jpg'
---

<div id="contents_list" markdown="1">

## 목차

1. [Deprecated](#deprecated)
1. [개요](#개요)
1. [이미지 준비하기](#이미지-준비하기)
1. [라이브러리 설치](#라이브러리-설치)
1. [사용법](#사용법)
1. [참고](#참고)

</div>

## Deprecated

이 블로그 포스트는 generator-rn-toolbox가 `Deprecated`되었기 때문에 더이상 관리되지 않습니다. generator-rn-toolbox의 새로운 라이브러리인 `react-native-make`를 사용하시길 권장합니다.

react-native-make에 관해서는 아래에 블로그를 참고하시기 바랍니다.

- [react-native-make]({{site.url}}/{{page.categories}}/react-native-make/){:target="_blank"}

## 개요

mac osx에서 [generator-rn-toolbox](https://github.com/bamlab/generator-rn-toolbox){:rel="nofollow noreferrer" target="_blank" }를 사용하여 앱 아이콘을 만드는 방법을 설명하겠습니다.

## 이미지 준비하기

앱 아이콘으로 사용할 1024x1024px 사이즈에 이미지를 준비합니다.

## 라이브러리 설치

아래의 명령어로 라이브러리를 설치합니다.

{% include_relative common/installation.md %}

- generator-rn-toolbox: RN에 도움을 주는 툴을 제공해 줍니다. 자세한 사항은 공식 홈페이지를 참조하세요. (공식사이트: [generator-rn-toolbox](https://github.com/bamlab/generator-rn-toolbox){:rel="nofollow noreferrer" target="_blank" })
- yo: generator-rn-toolbox을 기동시키기 위한 라이브러리입니다.

앱 아이콘 생성을 위해서는 ```imagemagick```를 설치해야 합니다.

{% include_relative common/imagemagick_installation.md %}

{% include in-feed-ads.html %}

## 사용법

- 아래에 명령어로 아이콘을 생성합니다.

{% include_relative common/usage.md %}

아이콘 생성되어 프로젝트에 반영되었습니다. 프로젝트를 실행하여 아이콘이 반영되었는지 확인하세요.

{% include_relative common/start_project.md %}

아이콘이 제대로 표시되지 않는 경우 시뮬레이터/단말기에서 어플을 지우고 다시 실행해 보시길 바랍니다.

## 참고

- 공식 홈페이지: [generator-rn-toolbox](https://github.com/bamlab/generator-rn-toolbox){:rel="nofollow noreferrer" target="_blank" }
