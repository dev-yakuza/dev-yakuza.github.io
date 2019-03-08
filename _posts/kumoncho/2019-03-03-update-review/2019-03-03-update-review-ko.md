---
published: false
layout: 'post'
permalink: '/kumoncho/update-review/'
paginate_path: '/kumoncho/:num/update-review/'
lang: 'ko'
categories: 'kumoncho'
comments: true

title: 'Kumoncho 업데이트 후기(RN, React Native)'
description: 'RN(React Native)를 사용하여 쿠몬쵸(Kumoncho)라는 그림 동화책 앱을 제작하여 배포하였습니다. 배포후 어떤 업데이트를 했는지에 대해서 정리해보았습니다.'
image: '/assets/images/category/kumoncho/background.png'
---

## 개요
RN(React Native)를 사용하여 Kumoncho(쿠몬쵸)라는 앱을 제작하고 배포하였습니다. 이 블로그에서는 앱 배포후 Kumoncho 앱에 어떤 업데이트를 진행하였는지에 대해서 이야기하려고 합니다. Kumoncho 앱을 제작하면서 겪은 이야기는 아래의 앱 개발기 블로그를 참고하시기 바랍니다.

- [Kumoncho 앱 개발기(RN, React Native)]({{site.url}}/kumoncho/development-journal/){:target="_blank"}

본격적인 이야기에 앞서 Kumoncho를 간단하게 다시 한번 소개하고 진행하도록 하겠습니다.


## 쿠몬쵸(Kumoncho)란?
쿠몬쵸(Kumoncho)는 구름의 나라 이카루스 왕자와 그의 구름 친구 쿠몬쵸의 우정과 용기를 그린 어린이 그림 동화책 앱입니다.

- Kumoncho 소개 페이지: [Kumoncho]( https://dev-yakuza.github.io/app/kumoncho/ko/){:target="_blank"}

아래는 앱을 다운로드 받을 수 있는 링크입니다.

<div class="download_link_container">
    <a class="download_link_ios" href="https://itunes.apple.com/app/kumoncho/id1450902241" target="_blank">
        <img src="/assets/images/apple_download.png" alt="어린이 그림 동화책 앱 쿠몬쵸 iOS 다운로드"/>
    </a>
    <a class="download_link_android" href="https://play.google.com/store/apps/details?id=io.github.dev.yakuza.kumoncho" target="_blank">
        <img src="/assets/images/google play_download.png" alt="어린이 그림 동화책 앱 쿠몬쵸 안드로이드 다운로드"/>
    </a>
</div>

<div class="download_link_container">
    <a class="download_link_ios" href="https://itunes.apple.com/app/blaboo/id1441741187" target="_blank">
        <img src="/assets/images/apple_download.png" alt="어린이 단어 학습 앱 blaboo iOS 다운로드"/>
    </a>
    <a class="download_link_android" href="https://play.google.com/store/apps/details?id=io.github.dev.yakuza.blaboo" target="_blank">
        <img src="/assets/images/google play_download.png" alt="어린이 단어 학습 앱 blaboo 안드로이드 다운로드"/>
    </a>
</div>


## 문제점
이전 블로그에서도 이야기했지만, 이번 프로젝트는 UX면에서 실패한 프로젝트였습니다. 그래서 최대한 UX를 좋게 만드는 부분에 집중하여 업데이트를 진행하였습니다.

또한 개발시 태블릿을 고려하지 않은 설계로 인해, 태블릿 지원에 실패하였습니다. 그래서 리펙토링(리펙토링이라 쓰고 다시 개발했다고 읽자)을 통해 앱이 태블릿을 지원할 수 있도록 수정하였습니다.

그리고 작가 친구는 현재 마이크로 인터랙션(Micro-interaction) 전문가를 꿈꾸고 있습니다. 그래서 현업에서도 사용할 수 있고, 이번 앱을 좀 더 효과적으로 표현할 수 있도록 애니메이션을 추가하였습니다.


## 앱 업데이트
Kumoncho v2는 아래에 기능들을 추가하였습니다.

1. 태블릿 지원
1. 애니메이션
1. 페이지 전환
1. 튜토리얼
1. 상태바(StatusBar)

하나하나 자세히 살펴보겠습니다.


### 태블릿 지원
RN(React Native)는 크로스 플랫폼(Cross Platform)을 지원하므로, 스마트폰과 태블릿을 지원하는 Universal App을 간단하게 제작할 수 있습니다. 물론 화면 사이즈가 다양하므로 그에 맞게 코딩을 해야합니다. RN(React Native)는 기본적으로 ```flexbox```를 사용함으로 간단하게 responsive 앱을 제작할 수 있습니다.

하지만 Kumoncho는 어린이 그림 동화책 앱입니다. 따라서 전체 그림을 다양한 레이어(Layer)로 나누고 그 안에 이미지 위치를 고정하여 표시하고 있습니다. 그래서 처음부터 태블릿을 생각하지 않고 설계하여 간단하게 responsive 앱으로 제작할 수 없었습니다.

![어린이 그림 동화책 앱 Kumoncho 레이어](/assets/images/category/kumoncho/update-review/kumoncho_layer.png)

Kumoncho는 위에서 보는 것과 같이, 배경 레이어, 메인 이미지 레이어, 주변 이미지 레이어, 설명(Description) 레이어로 나누어 관리하고 있습니다. 이렇게 나눈 레이어를 ```object``` 형식으로 각 페이지를 관리하고 있으며 React 컴포넌트를 활용해 간단하게 구현하여 사용하고 있었습니다.

```js
{
    key: 'page1',
    src: ...,
    description: {
        ja: [...],
        ko: [...],
        en: [...],
    },
    color: ...,
    background: [...],
    direction: {
        start: { ... },
        end: { ... },
    },
    width: ...,
    descriptionImage: ...,
    additionalImages: [
        {...},
        {...},
        {...},
        {...},
    ],
},
```

위에 보이는 ```object```는 실제로 사용하고 있는 object의 일부입니다. 보시는 바와같이 tablet과 관련된 어떤 설정도 존재하지 않고 있습니다. 처음에는 React 컴포넌트 부분에서 스마트폰인지 태블릿인지 구별하여 스타일을 적용하려고 애썼지만, 근본적인 문제가 해결이 되지 않아 결국 ```object``` 부분은 리펙토링(재작성)하게 되었습니다.

```js
{
    key: 'page1',
    background: {
      color: [...],
      direction: {
        start: { ... },
        end: { ... },
      },
    },
    layers: [
      {
        data: ...,
        ...
        style: {
          phone: { ... },
          tablet: { ... },
        },
      },
      {
        images: [
          {
            src: ...,
            style: {
              phone: {...},
              tablet: {...},
            },
          },
          ...
        ],
      },
    ],
    description: {
      text: {
        ja: [...],
        ko: [...],
        en: [...],
      },
      color: ...,
      image: ...,
      style: {
        container: {
          phone: {...},
          tablet: {...},
        },
        label: {
          phone: {...},
          tablet: {...},
        },
      },
    },
},
```

이렇게 레이어를 데이터(애니메이션)와 이미지 등을 지원할 수 있게 제작하였으며, 스타일을 스마트폰과 태블릿을 나누어 관리하게 만들었습니다. 또한 스타일을 특정 스타일(width 또는 color 등)만 지원하였지만, 이번 리펙토링에서는 어떤 스타일도 지원 가능하도록 수정하였습니다. 이로써 스마트폰과 상관없이 태블릿만 집중하여 개발할 수 있게 되었습니다.


### 애니메이션
Kumoncho는 어린이 그림 동화책 ```앱```입니다. 따라서 일반 종이책에서는 보여줄 수 없는 기능들을 제공하는게 가능합니다. 그중 하나가 애니메이션 기능으로, 유저(어린이)가 좀더 책을 집중하여 볼 수 있도록, 마이크로 인터랙선을 집어 넣었습니다.

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/kumoncho/update-review/kumoncho_animation.gif" alt="어린이 동화책 쿠몬쵸 스크롤">
</div>

각 페이지별 애니메이션을 추가하였으며, 이로인해 좀 더 재밌게 그림 동화책을 볼수 있게 되었습니다. 애니메이션은 `lottie`를 사용했으며, 이에 관한 블로그는 아래 링크를 통해 확인할 수 있습니다.

- [애프터이펙트(AEF) 사용]({{site.url}}//react-native/react-native-lottie/){:target="_blank"}


### 페이지 전환
이전 블로그([Kumoncho 앱 개발기(RN, React Native)]({{site.url}}/kumoncho/development-journal/){:target="_blank"})에서도 설명했지만, 이번 프로젝트는 UX 부분에서 실패작이였습니다. 열심히 책을 읽다고 앱을 종료하면, 다시 처음부터 책을 읽어야하는 문제가 있었습니다. 이번 업데이트를 통해 이 부분을 해결하고자 하였으며, 페이지 전환 기능을 추가하게 되었습니다.

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/kumoncho/update-review/kumoncho_page_change.gif" alt="어린이 동화책 쿠몬쵸 스크롤">
</div>

화면을 더블 터치하면, 페이지 리스트가 보이는 화면이 나오고 그중에 원하는 페이지를 선택하면 해당 페이지로 이동하는 기능을 추가하였습니다.


### 튜토리얼
현재는 화면 스와이프, 화면 더블 터치 등으로 페이지 이동을 하고 있습니다. 이런 부분을 처음 사용하는 사용자는 잘 이해하지 못할 거 같아, 앱을 처음 실행하면 튜토리얼 화면이 보이도록 추가하였습니다.

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/kumoncho/update-review/kumoncho_tutorial.png" alt="어린이 동화책 쿠몬쵸 스크롤">
</div>


### 상태바(StatusBar)
iOS을 중심으로 개발을 하다보니, 안드로이드를 크게 신경쓰지 못했습니다. iOS는 상태바(StatusBar)가 투명하여 큰 문제가 없었습니다. 앱을 배포하고 나서 안드로이드쪽에서 상태바(StatusBar)를 투명하게 하면 좋겠다는 의견이 있었습니다. 그래서 안드로이드에서 상태바를 투명하게 만들고, Splash가 표시될 때는 상태바를 숨기는 작업을 하였습니다. 아래에 링크는 이에 관한 블로그입니다.

- [StatusBar 다루기]({{site.url}}/react-native/react-native-status-bar/){:target="_blank"}


## 결론
이번 업데이트를 통해 완전 실패했던 UX부분을 조금은 좋게 만들었다고 생각합니다. 또한 애니메이션을 통해 좀 더 재밌게 동화를 즐길 수 있도록 했습니다. 이번 기회를 통해 만든 앱을 베이스로 다음 그림 동화책 앱을 만들 예정입니다. 좀 더 추가했으면 좋겠다는 의견이 있으면 아래 댓글을 남겨주세요!