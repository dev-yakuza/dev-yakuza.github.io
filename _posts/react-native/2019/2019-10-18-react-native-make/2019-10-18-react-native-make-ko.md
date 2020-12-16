---
layout: 'post'
permalink: '/react-native/react-native-make/'
paginate_path: '/react-native/:num/react-native-make/'
lang: 'ko'
categories: 'react-native'
comments: true

title: 'React Native에서 App 아이콘 & Splash 이미지 만들기'
description: 'react-native-make 라이브러리를 이용하여 App 아이콘과 Splash 이미지를 생성하는 방법에 대해서 알아봅니다.'
image: '/assets/images/category/react-native/2019/react-native-make/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [react-native-make 설치](#react-native-make-설치)
- [App 아이콘](#app-아이콘)
- [Splash 이미지](#splash-이미지)
  - [Splash 이미지 생성](#splash-이미지-생성)
  - [iOS](#ios)
  - [react-native-splash-screen](#react-native-splash-screen)
- [완료](#완료)

</div>

## 개요

React Native에서 App 아이콘과 Splash 이미지를 만들기 위해, 지금까지는 [generator-rn-toolbox](https://github.com/bamlab/generator-rn-toolbox){:rel="nofollow noreferrer" target="_blank" }을 사용하였습니다. 이와 관련된 블로그는 아래에 링크를 통해 확인할 수 있습니다.

- [App icon]({{site.url}}/{{page.categories}}/app-icon/){:target="_blank"}
- [Splash 이미지]({{site.url}}/{{page.categories}}/splash-image/){:target="_blank"}

지금까지는 generator-rn-toolbox을 잘 사용하고 있었는데, generator-rn-toolbox을 개발한 개발자분이 친절하게도 제 블로그까지 와서 새로운 라이브러리를 만들었다고 알려주셨습니다.

![react-native-make를 이용한 App 아이콘과 Splash 이미지 생성 - 개발자 댓글](/assets/images/category/react-native/2019/react-native-make/comment.jpg)

확인해 보니 현재 generator-rn-toolbox는 `Deprecated` 되었고, 새롭게 [react-native-make](https://github.com/bamlab/react-native-make){:rel="nofollow noreferrer" target="_blank" }을 만들어 제공하고 있습니다.

이번 블로그에서는 react-native-make를 사용하여 App 아이콘과 Splash 이미지를 생성하는 방법에 대해서 살펴보면서 기존 라이브러리보다 좋아진 점도 살펴봅니다.

## react-native-make 설치

아래에 명령어를 사용하여 react-native-make를 설치합니다.

```bash
npm install --save-dev @bam.tech/react-native-make
```

이것으로 react-native-make를 사용할 준비가 끝났습니다. 이전의 generator-rn-toolbox과 조금 비교해 보면 아래와 같습니다.

generator-rn-toolbox를 설치할 때는 아래와 같이 글로벌로 설치를 했어야 했고,

```bash
npm install -g yo generator-rn-toolbox
```

아래와 같이 imagemagick라는 라이브러리를 설치했어야 했었습니다.

```bash
brew install imagemagick
```

이에 비하면 현재 react-native-make는 로컬로 설치되고 추가 라이브러리도 설치할 필요가 없습니다.

## App 아이콘

react-native-make를 통해 App 아이콘을 생성하려면 `1024x1024 px` 사이즈의 `png` 파일이 필요합니다.

아이콘 파일이 준비되면 아래에 명령어를 사용하여 App 아이콘을 생성합니다.

```bash
# react-native set-icon --path [path-to-image]
react-native set-icon --path [path-to-image] --background ["color"]
```

예를 들면 아래와 같습니다.

```bash
# react-native set-icon --path ./src/Assets/images/app_icon.jpg
react-native set-icon --path ./src/Assets/images/app_icon.jpg --background "#FFFFFF"
```

{% include in-feed-ads.html %}

## Splash 이미지

### Splash 이미지 생성

react-native-make를 통해 Splash 이미지를 생성하기 위해서는 최소 `3000x3000px` 사이즈의 `png` 파일이 필요합니다.

Splash 이미지 파일이 준비되면 아래에 명령어를 사용하여 Splash 이미지를 생성합니다.

```bash
# react-native set-splash --path [path-to-image]
# react-native set-splash --path [path-to-image] --resize [contain|cover|center]
react-native set-splash --path [path-to-image] --resize [contain|cover|center] --background ["background-color"]
```

예를 들면 아래와 같습니다.

```bash
# react-native set-splash --path ./src/Assets/images/splash.jpg
# react-native set-splash --path ./src/Assets/images/splash.jpg --resize cover
react-native set-splash --path ./src/Assets/images/splash.jpg --resize center --background "#FFFFFF"
```

여기에서 resize 옵션가 있는데 기본값은 `contain`입니다. 또한 Cover 옵션를 사용할 때는 중요 이미지가 짤리지 않게 하기 위해, Splash 이미지를 만들 때, 중요 이미지를 백그라운드 이미지의 1/3 padding 지점에 위치하도록 합니다.

각각의 옵션에 따른 이미지 상태는 아래에 링크를 통해 확인하실 수 있습니다.

- [resize-modes](https://github.com/bamlab/react-native-make/blob/master/docs/set-splash.md#resize-modes){:rel="nofollow noreferrer" target="_blank" }

저는 주로 단색이 아닌 배경색이 있는 Splash 이미지를 사용합니다. 이 때는, `cover` 옵션을 사용하여 생성하면 원하는 Splash 이미지를 얻을 수 있었습니다.

### iOS

iOS에서 Splash 이미지를 사용하기 위해서는 Splash 이미지용 Storyboard를 설정할 필요가 있습니다. Storyboard를 설정하기 위해 `./ios/[Project Name].xcworkspace` 파일을 선택해서 Xcode를 실행합니다.

![react-native-make를 이용한 App 아이콘과 Splash 이미지 생성 - add storyboard on iOS ](/assets/images/category/react-native/2019/react-native-make/add_files.jpg)


Xcode가 실행되면 왼쪽 상단의 프로젝트에서 프로젝트 이름을 마우스 오른쪽 클릭한 이후, `Add Files to "Project Name"` 메뉴를 선택합니다.

그리고 `ios/SplashScreen.storyboard` 파일을 선택하여 추가합니다.

![react-native-make를 이용한 App 아이콘과 Splash 이미지 생성 - setting launch_screen_file](/assets/images/category/react-native/2019/react-native-make/create-splash-screen.jpg)


파일을 추가하였다면 `General` 탭의 `Launch Screen File`에 `SplashScreen`을 입력해 줍니다.

### react-native-splash-screen

이렇게 Splash 이미지를 만들어 앱에 적용하는 이유는 이 Splash 이미지를 사용해서 Splash 이미지를 화면에 표시하고 그 뒤에서 로그인 처리한다던지, 데이터 송수신 처리를 하기 위해서 이겠죠?

이를 위해서 react-native-make는 [react-native-splash-screen](https://github.com/crazycodeboy/react-native-splash-screen){:rel="nofollow noreferrer" target="_blank"}을 사용하도록 하고 있습니다.

react-native-make만을 위해서는 아니고 React Native에서 Splash 이미지를 컨트롤할 때는, `react-native-splash-screen`을 사용하면 정말 편하게 다룰 수 있습니다. 이에 관해, 작성한 블로그가 있습니다. 아래에 링크를 통해 확인해 보시기 바랍니다.

- [App Splash 스크린]({{site.url}}/{{page.categories}}/react-native-splash-screen/){:target="_blank"}

## 완료

혼자서 디자인도 하고, 개발도 하는 저한테는 App 아이콘과 Splash 이미지를 만들 때, generator-rn-toolbox을 정말 잘 사용했었습니다. 이번에 새로 나온 react-native-make도 정말 많이 도움이 될거 같습니다.

여러분도 react-native-make를 사용하여 더 쉽게 App 아이콘과 Splash 이미지를 생성해 보시기 바랍니다.
