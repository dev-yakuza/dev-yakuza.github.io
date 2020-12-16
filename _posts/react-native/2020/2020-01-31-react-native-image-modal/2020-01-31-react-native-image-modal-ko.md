---
layout: 'post'
permalink: '/react-native/react-native-image-modal/'
paginate_path: '/react-native/:num/react-native-image-modal/'
lang: 'ko'
categories: 'react-native'
comments: true

title: 'react-native-image-modal'
description: 'react-native-image-modal을 사용해서 이미지를 전체 화면으로 표시해보고, pinch 확대, 축소 등을 사용해 보자'
image: '/assets/images/category/react-native/2020/react-native-image-modal/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [미리보기](#미리보기)
- [설치](#설치)
- [사용법](#사용법)
- [Properties](#properties)
- [기능](#기능)
- [예제 프로젝트](#예제-프로젝트)
- [Contribute](#contribute)
- [완료](#완료)

</div>

## 개요

이미지를 선택하면 전체화면으로 표시하고 확대, 축소 기능이 있는 컴포넌트가 필요하게 되었습니다. 이미 잘 만들어진 많은 컴포넌트들이 있지만, 이번엔 시간을 내어 `react-native-image-modal`이라는 컴포넌트를 제작해 보았습니다.

이번 블로그 포스트에서는 제가 제작한 `react-native-image-modal`을 사용하는 방법에 대해서 알아봅니다.

- Github: [react-native-image-modal](https://github.com/dev-yakuza/react-native-image-modal){:target="_blank"}

## 미리보기

우선 이번에 사용할 react-native-image-modal은 아래와 같이 동작합니다.

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2020/react-native-image-modal/pinch-zoom-and-move.gif" alt="react-native-image-modal 동작 화면">
</div>

{% include in-feed-ads.html %}

## 설치

아래에 명령어로 react-native-image-modal을 설치합니다.

```bash
npm install --save react-native-image-modal
```

## 사용법

아래와 같이 전체 사이즈 이미지를 표시하고 싶은 컴포넌트에 react-native-image-modal을 불러옵니다.

```js
import ImageModal from 'react-native-image-modal';
```

아래와 같이 이미지 모달을 추가하여 사용합니다.

```js
{% raw %}
<ImageModal
  swipeToDismiss={false}
  resizeMode="contain"
  imageBackgroundColor="#000000"
  style={{
    width: imageWidth,
    height: 250,
  }}
  source={{
    uri:
      'https://cdn.pixabay.com/photo/2018/01/11/09/52/three-3075752_960_720.jpg',
  }}
/>
{% endraw %}
```

## Properties

기본적으로 React Native의 Image 컴포넌트의 Props를 그대로 사용할 수 있습니다. 이 Props들은 최초 화면에 표시되는 원본 이미지에 적용됩니다.(전체 사이즈 모달 이미지에 적용되지 않음.)
하단에 나열된 내용은 react-native-image-modal에 특화된 Props들입니다.

| Prop | 필수 여부 | 타입 | 설명 |
|------|----------|------|-------------|
| swipeToDismiss | X | boolean | 스와이프하여 창을 닫을지 여부를 결정합니다.(`default: true`)  |
| imageBackgroundColor | X | string | 원본 이미지의 배경색을 지정합니다. |
| overlayBackgroundColor | X | string | 전체 사이즈 모달의 배경색을 지정합니다.(`default: #000000`)  |
| onLongPressOriginImage | X | () => void | 원본 이미지를 길게 눌렀을 때 호출되는 콜백함수입니다.  |
| renderHeader | X | (close: () => void) => JSX.Element | Array<JSX.Element> | 전체 사이즈 모달의 헤더 부분에 원하는 컴포넌트를 표시하는데 사용됩니다. |
| renderFooter | X | (close: () => void) => JSX.Element | Array<JSX.Element> | 전체 사이즈 모달의 하단 부분에 원하는 컴포넌트를 표시하는데 사용됩니다. |
| onTap | X | (eventParams: {locationX: number; locationY: number; pageX: number; pageY: number;}) => void  | 전체 사이즈 모달의 이미지를 한번 탭하면 호출되는 콜백함수입니다. |
| onDoubleTap | X | () => void | 전체 사이즈 모달의 이미지를 두번 탭하면 호출되는 콜백함수입니다. |
| onLongPress | X | () => void | 전체 사이즈 모달의 이미지를 길게 눌렀을 때 호출되는 콜백함수입니다. |
| onOpen | X | () => void | 전체 사이즈 모달이 열릴 때 호출되는 콜백함수입니다. |
| didOpen | X | () => void | 전체 사이즈 모달이 완전이 열린 후 호출되는 콜백함수입니다.  |
| onMove | X | (position: {type: string; positionX: number; positionY: number; scale: number; zoomCurrentDistance: number;}) => void  | 전체 사이즈 모달의 이미지를 이동시킬 때 호출되는 콜백함수입니다. |
| responderRelease | X | (vx?: number, scale?: number) => void | 손가락 이벤트가 끝날 때 호출되는 콜백 함수입니다. |
| willClose | X | () => void | 전체 사이즈 모달이 닫히기 전에 호출되는 콜백함수 입니다. |
| onClose | X | () => void | 전체 사이즈 모달이 닫힐 때 호출되는 콜백함수입니다. |

{% include in-feed-ads.html %}

## 기능

react-native-image-modal은 다음과 같은 기능을 가지고 있습니다.

- 이미지 모달을 열고 닫기

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2020/react-native-image-modal/open-and-close-image-modal.gif" alt="react-native-image-modal 이미지 모달 열고 닫기">
</div>

- 이미지 pinch 확대, 축소, 이동

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2020/react-native-image-modal/pinch-zoom-and-move.gif" alt="react-native-image-modal pinch 이미지 확대, 축소, 이동">
</div>

- 이미지 더블 탭 확대, 축소

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2020/react-native-image-modal/double-tap-zoom.gif" alt="react-native-image-modal 이미지 더블 탭 확대, 축소">
</div>

- 스와이프로 창 닫기

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2020/react-native-image-modal/swipe-to-dismiss.gif" alt="react-native-image-modal 스와이프로 이미지 창닫기">
</div>

{% include in-feed-ads.html %}

## 예제 프로젝트

Github 저장소에 예제 프로젝트도 포함이 되어있습니다.

- Github: [react-native-image-modal](https://github.com/dev-yakuza/react-native-image-modal){:target="_blank"}

예제 소스를 확인하기 위해서 아래와 같이 Github 저장소를 복사합니다.

```bash
git clone https://github.com/dev-yakuza/react-native-image-modal.git
```

예제 프로젝트에 필요한 라이브러리들을 설치합니다.

```bash
cd Example
npm install

# iOS
cd ios
pod install
```

아래에 명령어를 사용하여 예제 프로젝트를 실행합니다.

```bash
# Example folder
# iOS
npm run ios
# Android
npm run android
```

## Contribute

처음 만든 오픈소스이므로 부족한 점들이 많을거 같습니다. 혹시 잘못된 부분이 있다면 언제든지 풀리퀘 주시기 바랍니다.

조금이라도 편하게 기여할 수 있도록, 이 프로젝트를 개발하는 방법에 대해서 공유합니다.

- 프로젝트를 복사합니다.

```bash
git clone https://github.com/dev-yakuza/react-native-image-modal.git
```

- 아래 명령어로 개발 환경을 구축하고 타입스크립트를 실행합니다.

```bash
npm install
npm start
```

- 아래에 명령어로 개발용 프로젝트를 실행합니다.

```bash
cd Develop
npm install

# android
npm run android

# ios
cd ios
pod install
cd ..
npm run ios
```

## 완료

이것으로 제가 처음으로 만든 오픈소스, react-native-image-modal를 사용하는 방법에 대해서 알아보았습니다. 많은 분들께 도움이 되면 좋겠습니다.