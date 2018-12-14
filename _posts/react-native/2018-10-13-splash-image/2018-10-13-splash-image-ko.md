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


## 개요
mac osx에서 [generator-rn-toolbox](https://github.com/bamlab/generator-rn-toolbox){:rel="nofollow noreferrer" target="_blank" }를 사용하여 splash 이미지를 만드는 방법을 설명하겠습니다.

## 라이브러리 설치
generator-rn-toolbox 라이브러리 설치는 이전 블로그 [App icon]({{site.url}}/{{page.categories}}/app-icon/){:target="_blank"}을 참고하시기 바랍니다.

## 이미지 준비하기
splash 이미지로 사용할 2208x2208px 사이즈에 psd 파일을 준비합니다.

### sketchapp에서 psd 파일 생성
우리는 디자인에 sketchapp을 사용합니다. sketchapp은 psd파일을 내보낼 수 없으므로 이미지 준비하기 불가능합니다. 하지만 아래에 방법을 통해 psd 파일을 준비할 수 있습니다.

1. sketchapp으로 splash 이미지 디자인하기
1. 디자인한 splash 이미지를 pdf로 내보내기
1. 인터넷에서 pdf to psd converter를 검색하여 온라인 변환 사이트를 찾습니다.(우리가 사용한 [사이트](https://www.pdfconvertonline.com/pdf-to-psd-online.html){:rel="nofollow noreferrer" target="_blank" })

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



## 참고
- 공식 사이트: [generator-rn-toolbox](https://github.com/bamlab/generator-rn-toolbox){:rel="nofollow noreferrer" target="_blank" }