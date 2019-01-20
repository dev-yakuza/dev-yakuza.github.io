---
layout: 'post'
permalink: '/blaboo/development-journal/'
paginate_path: '/blaboo/:num/development-journal/'
lang: 'ko'
categories: 'blaboo'
comments: true

title: 'BlaBoo 앱 개발기(RN, React Native)'
description: 'RN(React Native)를 사용하여 BlaBoo라는 앱을 제작해 보았습니다. 이 앱을 제작하면서 격은 내용을 정리해보려고 합니다.'
image: '/assets/images/category/blaboo/development-journal.png'
---


## 개요
지금까지 RN(React Native)를 공부했지만 앱을 처음부터 끝까지 개발해본 적이 없었습니다. 그래서 RN(React Native)를 활용하고 최대한 빠르게 앱을 처음부터 끝가지 개발해보고자 이번 프로젝트를 진행하였습니다.

## BlaBoo란?
BlaBoo(블라부)는 영어의 ```blah blah(블라 블라)```라는 단어와 아기들이 잘 내는 ```boo(부)```라는 단어를 합친 의미로, 유아/어린이를 대상으로 하는 단어 공부 앱입니다.

- 다운로드: [애플 앱 스토어](https://itunes.apple.com/kr/app/blaboo/id1441741187){:rel="nofollow noreferrer" target="_blank"}
- 다운로드: [구글 앱 스토어](https://play.google.com/store/apps/details?id=io.github.dev.yakuza.blaboo){:rel="nofollow noreferrer" target="_blank"}

유아/어린이가 그림을 보고 그 그림을 선택하면 음성으로 단어를 읽어주는 아주 간단한 앱입니다.

![유아/어린이용 단어 공부 앱 BlaBoo 개발기](/assets/images/category/blaboo/development-journal/app_concept.png)

## 왜 만들게 되었나?
사실 유아/어린이용 단어 공부 앱은 많이 나와있습니다. 이 앱을 만들게 된 주목적은 아래와 같습니다.

1. 유아/어린이용으로 다국어를 배울 수 있는 단어 앱 만들기.
1. 지금까지 공부한 RN(React Naitve)로 앱을 개발해 정식 배포해 보기.

외국에 살다보니 아이에게 외국어와 모국어를 가르치고 싶은 마음에 여러 앱을 찾아보았지만 한 앱에서 다국어를 배우기 위한 기능을 제공하는 앱이 별로 없었습니다. 문제도 찾았고 그것을 해결할 기술도 있었으니 한번 만들어 보자는 생각에 만들게 되었습니다.

## 앱 기획
하지만 앱을 혼자 다 만들려니 시간이 충분하지 않았습니다. 그래서 일단 유아/어린이용으로 사용되는 여러 앱을 밴치마킹하였고, 그에 따른 MVP(Minimum Viable Product: 최소 기능 제품)를 정했습니다. BlaBoo의 MVP(Minimum Viable Production: 최소 기능 제품)은 아래와 같습니다.

1. 단어의 카테고리: 카테고리를 정의하고 그 안에 해당 단어들을 표시하자(ex> 자동차, 과일, 야채)
1. 단어를 그림/사진으로 표시: 단어를 그림/사진으로 표시하여 유아/어린이에게 흥미를 유발시키자.
1. 그림/사진 선택시 단어의 음성 지원: 그림/사진을 선택하면 단어를 소리내어 읽어주어 유아/어린이가 자연스럽게 그림/사진과 단어를 공부하도록 하자.
1. 다국어 지원: 다국어를 지원하여 한 단어를 여러 국가의 언어로 공부할 수 있게 하자.

이렇게 MVP(Minimum Viable Production: 최소 기능 제품)를 정의하고 간단한 스케치로 앱의 동선을 기획하였습니다.

![유아/어린이용 단어 공부 앱 BlaBoo 개발기 - 스케치](/assets/images/category/blaboo/development-journal/hand_sketch.png)

스케치 탬플릿은 아래에 사이트에서 다운로드하였습니다.

- [http://sneakpeekit.com/](http://sneakpeekit.com/){:rel="nofollow noreferrer" target="_blank"}

혼자 앱을 취미로 만들다 보니 기획이 그렇게 거창하지 않네요. 목표, 타겟, 비즈니스 모델... 이런건 넣어두고 대략적인 기능과 대략적인 스케치를 하는 정도만 했습니다. 그래도 나름 가설도 세워보고 할일을 나열하는 등 노력은 했지만 이걸 기획이라 불러야할지 민망하네요.

![유아/어린이용 단어 공부 앱 BlaBoo 개발기 - 기획](/assets/images/category/blaboo/development-journal/plan_trello.png)

## 앱 디자인
위에서 기획한 내용을 바탕으로 기본적인 디자인을 했습니다. 역시 디자인 전문가가 아니므로 디자인이 그렇게 이쁘지 않습니다. 그래도 디자인을 통해 앱의 기본적인 색상이나 컨셉 등을 구체화할 수 있었습니다.

기본 디자인은 [sketchapp](https://www.sketchapp.com/){:rel="nofollow noreferrer" target="_blank"}을 사용하여 간단히 디자인 했고 일러스트는 [freepik](https://www.freepik.com/){:rel="nofollow noreferrer" target="_blank"}이라는 사이트에서 다운로드받았습니다.

![유아/어린이용 단어 공부 앱 BlaBoo 개발기 - 디자인](/assets/images/category/blaboo/development-journal/sketch_design.png)

## 앱 개발
개발에는 RN(React Native)를 사용하였습니다. 개발자 한명이 iOS/Android를 동시에 개발할 수 있고 javascript이다보니 진입장벽도 Swift나 Kotlin처럼 높지 않았습니다. BlaBoo는 기본적으로 RN(```React Native```)과 타입스크립트(```typescript```)를 사용합니다.

- RN(React Native) 설치 방법: [RN 설치]({{site.url}}/react-native/installation/){:target="_blank"}
- RN(React Native)에 typescript 적용하기: [typescript]({{site.url}}/react-native/typescript/){:target="_blank"}

또한 RN(React Native)의 기본적인 UI는 ```NativeBase```를 스타일에는 ```styled-components```을 사용하였습니다.

- RN(React Native)에 NativeBase 적용하기: [nativebase]({{site.url}}/react-native/nativebase/){:target="_blank"}
- RN(React Navtive)에서 styled-components 사용하기: [styled-components]({{site.url}}/react-native/styled-components/){:target="_blank"}

RN(React Native)는 기본적으로 네비게이션 시스템이 없습니다. BlaBoo는 ```react-navigation```을 사용하여 네비게이션 시스템을 구현하였습니다.

- react-navigation 사용 방법: [react-navigation]({{site.url}}/react-native/react-navigation/){:target="_blank"}

MVP(Minimum Viable Product: 최소 기능 제품)의 기능중 하나인 음성 지원은 ```react-native-tts```를 사용하여 ```tts(Text To Speech)``` 기능을 구현하였습니다.

- react-native-tts 사용 방법: [react-native-tts]({{site.url}}/react-native/react-native-tts/){:target="_blank"}

또한 유저의 단말기 지역 정보를 이용하여 앱과 ```react-native-tts```의 기본 언어를 설정하였습니다. 유저의 단말기 정보를 얻기 위해 ```react-native-device-info```를 사용하였습니다.

- react-native-device-info 사용 방법: [react-native-device-info]({{site.url}}/react-native/react-native-device-info/){:target="_blank"}

그리고 이미지 선택시 이미지가 움직이는 애니메이션이 있는데 이 애니메이션을 넣기 위해 ```react-native-animatable```을 사용하였습니다.

- react-native-animatable 사용 방법: [react-native-animatable]({{site.url}}/react-native/react-native-animatable/){:target="_blank"}

최종적으로 앱의 광고와 분석을 위해 구글의 파이어베이스(Google Firebase)와 구글 애드몹(Google Admob)을 사용하였습니다. 이를 앱에 구현하기 위해 ```react-native-firebase```를 사용하였습니다.

- react-native-firebase admob 사용 방법: [react-native-firebase-admob]({{site.url}}/react-native/react-native-firebase-admob/){:target="_blank"}
- react-native-firebase analytics 사용 방법: [react-native-firebase-analytics]({{site.url}}/react-native/react-native-firebase-analytics/){:target="_blank"}

이렇게 정리하다보니 거의 오픈소스를 가져다가 구현한 것 이외에는 한게 별로 없어보이네요. 다들 너무 훌륭한 오픈소스를 만들어 줘서 너무 감사합니다. 훌륭한 오픈소스로 주요 기능을 구현하고 RN(React Native)를 활용하여 재사용 가능한 컴포넌트(Component)를 사용하니 개발은 수월하게 진행할 수 있었습니다. 단지 화면에 표시하기 위한 일러스트와 음성을 위한 단어를 모으고 정리하는데 시간이 더 많이 걸렸습니다.

![유아/어린이용 단어 공부 앱 BlaBoo 개발기 - 리소스 코드](/assets/images/category/blaboo/development-journal/resource.png)

## 앱 등록
이렇게 BlaBoo의 MVP(Minimum Viable Product: 최소 기능 제품)가 완성되었습니다. 개발이 끝나면 금방 앱을 등록하고 다운로드를 받을 수 있을 줄 알았는데, 앱 등록 절차도 시간이 많이 걸리는 일이였습니다.

애플의 앱 심사(App Review)가 시간이 많이 걸린다는 사실을 알고 있었기 때문에 일단 iOS 앱 등록을 먼저 하였고, iOS 앱이 등록된 후 안드로이드를 진행하였습니다. 애플의 앱 등록이 2달 넘게 걸렸고 안드로이드 앱 등록은 2일 걸렸습니다.

애플은 역시 여러 이유로 앱 심사 거부(App Review reject)가 많아 기간이 많이 걸려고, 안드로이드는 유아/어린이용으로 앱이지만 ```Designed for Families program```을 선택하지 않고 등록하여 거부(Reject) 당했습니다.

![유아/어린이용 단어 공부 앱 BlaBoo 개발기 - 구글 앱 심사 거부](/assets/images/category/blaboo/development-journal/google_reject.png)

앱을 등록하기 위해 애플 개발자 프로그램(Apple Developer Program) 등록과 안드로이 개발자 등록(Google Play Developer)이 필요합니다.

- 애플 개발자 프로그램 등록 방법: [iOS 개발자 등록]({{site.url}}/react-native/ios-enroll-developer-program/){:target="_blank"}
- 안드로이드 개발자(Google Play Developer) 등록: [안드로이드 개발자 등록]({{site.url}}/react-native/android-enroll-google-play-developer/){:target="_blank"}

또한 앱을 등록할 때 여러 정보가 필요했습니다. 이 정보를 제작하는데도 생각보다 많은 시간이 걸렸습니다.

- iOS 앱 등록 방법: [iOS App store 등록]({{site.url}}/react-native/ios-app-store/){:target="_blank"}
- 안드로이드 앱 등록 방법: [안드로이드 앱 스토어 등록]({{site.url}}/react-native/android-google-play/){:target="_blank"}

그리고 역시나 무서운 애플의 앱 심사(App Review). 5차례 정도 앱 심사(App Review)가 거부(Reject)되었습니다. 정말 등록하기 싫어지더군요. 결국 최종 거부(Recject) 이유는 앱이 사용자와 적절한 상호 작용을 하지 않아 애플 앱 스토어에는 필요없는 앱이라고 하더군요.

처음엔 열이 받아 기획할 때 벤치마킹한 앱과 비교하여 여기보다 카테고리, 단어량이 많고 저기에는 없는 다국어 기능이 있다 등을 어필했지만, 쉽게 승인해 주지 않았습니다. 오히려 제가 생각하는 다른 앱들이 앱 스토어의 위반된다고 생각되면 신고해달라고...다른 개발자들이 힘들게 만든 앱을 어떻게 신고하겠습니까...그래서 결국 처음 기획과는 달리 엉뚱한 기능이 추가되었습니다.

![유아/어린이용 단어 공부 앱 BlaBoo 개발기 - 복습 기능](/assets/images/category/blaboo/development-journal/add_card_mode.png)

카드 형태로 카테고리에서 공부한 단어들을 복습하는 기능을 추가하였습니다. 20장의 카드가 렌덤으로 표시되고 그 카드를 왼쪽 또는 오른쪽으로 넘겨 복습하는 기능입니다.

처음 기획에 있던 기능도 아니고, 급하게 앱 심사(App Review)를 통과하기 위해 하루만에 디자인하고 하루만에 기능을 만들다 보니 이전 앱 기능에 잘 녹아 들어가지 못했습니다. 아직도 한 앱에 두 앱이 들어가 있는 기분입니다. 그래도 이 기능을 추가하고 무사히 앱 심사(App Review)를 통과할 수 있었습니다.

처음엔 애플의 앱 심사(App Review)가 너무 심하고 화가 났지만, 이 심사가 있기에 iOS의 앱들의 UI/UX가 뛰어나구나 생각이 들었습니다. 또한 애플 앱 심사(App Review)를 거치다 보니 다음 앱을 좀 더 사용자 친화적으로 만들어야겠다는 생각이 들었습니다. 애플 앱 심사자(Apple App Reviewer)님들께 진심으로 감사드립니다.

- 다운로드: [애플 앱 스토어](https://itunes.apple.com/kr/app/blaboo/id1441741187){:rel="nofollow noreferrer" target="_blank"}
- 다운로드: [구글 앱 스토어](https://play.google.com/store/apps/details?id=io.github.dev.yakuza.blaboo){:rel="nofollow noreferrer" target="_blank"}

## 앱 개발기를 마치며
이런 저런 일들이 있었지만 무사히 첫 앱을 릴리스할 수 있었습니다. 보잘것 없는 앱으로 보실 수 있지만, 이 앱은 유저를 많이 늘리고 광고 수익을 내기 위함보다는 자신이 사용하기 위해, 그리고 지금까지 공부한 RN(React Native)를 활용하여 앱을 최종적으로 등록하는 프로세스를 확인하기 위해 제작하였습니다.

뒤돌아 보면, 개발보다는 디자인, 특히 일러스트를 수집하는데 시간이 많이 걸렸습니다. 개발은 1주일 정도했나...역시 RN(React Native)의 개발 퍼포먼스를 확인할 수 있었습니다. (많은 오픈소스를 만들고 계신 분들께 진심으로 감사드립니다.)

애플의 꼼꼼한 앱 심사(App Review). 그로인해 급하게 앱 컨셉 변경, 하지만 이로인해 유저 친화적 앱을 개발해야 한다는 마음가짐을 갖게 되었습니다. 다시 한번 애플 심사자(App Reviewer)님께 감사드립니다.

BlaBoo에서 검증하고 싶던 무료 리소스로 앱을 개발할 수 있다는 가설은 검증되었습니다. 여러분도 무료 리소스를 활용하여 앱을 개발해 보세요.

## 마지막으로
역시 ```TTS(Text To Speech)```는 목소리에 거부감이 있네요. 그리고 잘못 읽어주는 경우도 많았습니다. 한국어로 ```스파게티```는 제대로 발음하지 못해 ```파스타```로 변경하였습니다. 혹시 목소리 기부해주실 분 대환영입니다.([Contact Us](https://dev-yakuza.github.io/ko/contact/){:target="_blank"})

일러스트도 무료 일러스트를 사용하다보니 하나의 스타일로 통일되지 않은 감이 있습니다. 역시 일러스트도 기부해주실 분, 대환영입니다.([Contact Us](https://dev-yakuza.github.io/ko/contact/){:target="_blank"})

다국어는 일본어, 영어, 한국어를 기본으로 제공했고 중국과 이탈리아에서 앱 다운로드가 발생하여 중국어와 이탈리아어를 추가하였습니다. 하지만 중국어, 이탈리아어를 할 수 없기 때문에 번역기를 돌렸습니다. 틀릭 중국어, 이탈리아어가 있다면 피드백 부탁드립니다. 또한 다른 언어 번역을 기부해주실 분들도 환영합니다.([Contact Us](https://dev-yakuza.github.io/ko/contact/){:target="_blank"})

- 다운로드: [애플 앱 스토어](https://itunes.apple.com/kr/app/blaboo/id1441741187){:rel="nofollow noreferrer" target="_blank"}
- 다운로드: [구글 앱 스토어](https://play.google.com/store/apps/details?id=io.github.dev.yakuza.blaboo){:rel="nofollow noreferrer" target="_blank"}