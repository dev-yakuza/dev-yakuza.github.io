---
published: false
layout: 'post'
permalink: '/kumoncho/development-journal/'
paginate_path: '/kumoncho/:num/development-journal/'
lang: 'en'
categories: 'kumoncho'
comments: true

title: 'Kumoncho development journal(RN, React Native)'
description: I've developed the picture fairy tale book app that is called Kumoncho. in here, I wrote the development journal about what I experience.
image: '/assets/images/category/kumoncho/background.png'
---

## Outline
at previous my project, I've developed the app from start to end by myself using RN(React Native). at this project, I wanted to develop the app with someone together. especially, I wanted to work with a designer because the design has taken too much time at previous project. if you want to know more details about previous project, see the development journal about previous project.

- [BlaBoo development journal (RN, React Native)]({{site.url}}/blaboo/development-journal/){:target="_blank"}


## What is Kumoncho?
Kumoncho is the picture fairy tale book about the friendship and courage between prince Ikaros of the cloud kingdom and his cloud friend, Kumoncho.

- Kumoncho landing page: [Kumoncho]( https://dev-yakuza.github.io/app/kumoncho/ko/){:target="_blank"}

you can download to click the link below.

<div class="download_link_container">
    <a class="download_link_ios" href="https://itunes.apple.com/app/kumoncho/id1450902241" target="_blank">
        <img src="/assets/images/apple_download.png" alt="children picture fairy tale book, Kumoncho iOS download"/>
    </a>
    <a class="download_link_android" href="https://play.google.com/store/apps/details?id=io.github.dev.yakuza.kumoncho" target="_blank">
        <img src="/assets/images/google play_download.png" alt="children picture fairy tale book, Kumoncho Android download"/>
    </a>
</div>


## Why did I make it?
I've focused to make the app by RN(React Native) by myself at previous project.

- [BlaBoo development journal(RN, React Native)]({{site.url}}/blaboo/development-journal/){:target="_blank"}

so, at this project, I wanted to focus the collaboration with someone. also, I wanted to develop an app more fastly by collaborating the design that has taken too much time at previous project.

마지막으로, 만화가가 되고 싶었지만 그 꿈을 이루지 못하고 디자이너로써 살아가는 친구가 한명 있었습니다. 하지만 재능이 너무 아까워 이번 프로젝트에 동참하도록 설득하였습니다. 만화가는 수만 페이지 수만가지 이야기를 그려야 하기만, 어린이 그림 동화책은 짧은 주제로 그릴 수 있으니 현재 업무를 하면서 취미로 충분히 만들 수 있지 않겠냐고, 취미로 같이 한번 만들어보자고 설득하여 이번 프로젝트에 참가하게 되었습니다.

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/kumoncho/development-journal/profile_shu.png" alt="어린이 동화책 작가 shu 프로필">
</div>

- Shu: <a href="mailto:meiki.shuzou@gmail.com">meiki.shuzou@gmail.com</a>

다행이 같이 만들기로 했고, 이 친구는 그림과 스토리를, 제가 프로젝트 디렉팅과 개발을 담당하여 진행하게 되었습니다.

이 프로젝트를 시작으로 이 친구와 함께 계속적으로 어린이 동화책 앱을 제작할 예정이고 동화책을 출판하는 것에 최종 목표를 두고 있습니다. 쿠몬쵸를 배포하면서 벌써 두번째 어린이 동화책 앱을 준비하고 있습니다.

서로 다니는 회사가 다르기 때문에, 피드백은 주로 라인으로 메세지를 주고 받아 진행했으며, 필요에 따라서는 점심 시간에 화상 회의를 했습니다. 담당 파트가 겹치지 않고 확실하게 나눠져 있다보니, 협업에는 큰 충돌없이 진행할 수 있었습니다.


## 앱 기획
이번 프로젝트가 어린이 그림 동화책 앱이지만 작가 친구는 동화책용 이야기나 그림을 그려본 적이 없고, 저도 동화책 앱을 만들어본 적이 없었습니다. 그래서 일단 자료 조사를 시작했습니다.

최종 목표는 동화책을 출판하는 것이기 때문에, 현재 어린이 그림 동화책의 기준으로 조사하였습니다.

어린이 동화책은 16, 24, 48 페이지 책들도 있지만 32 페이지를 업계 표준으로 하고 있습니다.(틀렸다면 댓글로 주세요.)

![어린이 동화책 32페이지](/assets/images/category/kumoncho/development-journal/picture_book.jpg)
(사진 출처: [https://taralazar.com](https://taralazar.com/2009/02/22/picture-book-construction-know-your-layout/){:rel="nofollow noreferrer" target="_blank"})

또한 우리는 출판할 책(정말 출판이 될지 모르겠지만)과 앱에 차이를 주어서, 앱으로 이미 본 사용자도 책을 구매할 수 있도록 기획했습니다. 그렇게 결론내린 페이지가 9페이지. 너무 길지도 너무 짧지도 않게 페이지를 설정하였습니다.(책 출판은 32페이지를 예정하고 있음)

이렇게 페이지를 결정하니 작가 친구는 쉽게 스토리와 일러스트의 레이아웃을 구성할 수 있게 되었습니다.


## 스토리 및 일러스트
작가 친구나 저나 어린이 그림 동화책 앱은 처음 제작하기때문에, 첫 스토리는 무난한 내용으로 정했습니다. 앱을 다운로드 받아 보시면 알겠지만, 어디선가 본듯한, 있을 법한 이야기를 첫 스토리로 정했습니다.

<div class="download_link_container">
    <a class="download_link_ios" href="https://itunes.apple.com/app/kumoncho/id1450902241" target="_blank">
        <img src="/assets/images/apple_download.png" alt="children picture fairy tale book, Kumoncho iOS download"/>
    </a>
    <a class="download_link_android" href="https://play.google.com/store/apps/details?id=io.github.dev.yakuza.kumoncho" target="_blank">
        <img src="/assets/images/google play_download.png" alt="children picture fairy tale book, Kumoncho Android download"/>
    </a>
</div>

스토리가 정하지자 작가 친구는 스케치를 통해 인물과 배경을 구체화하였습니다.

![쿠몬쵸 스케치](/assets/images/category/kumoncho/development-journal/sketch.png)

그리고 스토리를 다듬어, 그 스토리에 맞게 일러스트를 그려내기 시작했습니다.

![쿠몬쵸 일러스트](/assets/images/category/kumoncho/development-journal/illustration.png)

제 친구라서가 아니라 정말 그림고 스토리에는 재능이 있는게 아닌가 싶습니다.


## 앱 개발
앱 개발에는 당연히 RN(React Native)를 사용하였습니다. 쿠몬쵸는 기본적으로 RN(```React Native```)과 타입스크립트(```typescript```)를 사용합니다.

- RN(React Native) 설치 방법: [RN 설치]({{site.url}}/react-native/installation/){:target="_blank"}
- RN(React Native)에 typescript 적용하기: [typescript]({{site.url}}/react-native/typescript/){:target="_blank"}

또한 RN(React Native)의 기본적인 스타일에는 ```styled-components```을 사용하였습니다.

- RN(React Navtive)에서 styled-components 사용하기: [styled-components]({{site.url}}/react-native/styled-components/){:target="_blank"}

페이지의 배경에는 ```react-native-linear-gradient```를 사용하여 그라데이션 효과를 주었습니다.

- RN(React Navtive)에서 그라데이션(Gradient) 사용하기: [react-native-linear-gradient]({{site.url}}/react-native/react-native-linear-gradient/){:target="_blank"}

처음 개발할 때, 페이지 전환에는 아래와 같이 스크롤을 사용하였습니다.

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/kumoncho/development-journal/kumoncho_scroll.gif" alt="어린이 동화책 쿠몬쵸 스크롤">
</div>

하지만, 자연스러운 페이지 전환 연출을 위해 [react-native-linear-gradient]({{site.url}}/react-native/react-native-linear-gradient/){:target="_blank"}에서 소개한 그라데이션의 애니메이션 적용 방법으로 배경을 변경하였으며, [react-native-animatable]({{site.url}}/react-native/react-native-animatable/){:target="_blank"}의 fadein/fadeout으로 이미지의 등장 효과를 주었습니다.

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/kumoncho/development-journal/kumoncho_swipe.gif" alt="어린이 동화책 쿠몬쵸 스와이프">
</div>

페이지 전환에는 사용자 스와이프 이벤트를 사용하였습니다.

- RN(React Native)에서 스와이프 감지: [react-native-swipe-gestures]({{site.url}}/react-native/react-native-swipe-gestures/){:target="_blank"}

최종적으로 앱의 광고와 분석을 위해 구글의 파이어베이스(Google Firebase)와 구글 애드몹(Google Admob)을 사용하였습니다. 이를 앱에 구현하기 위해 ```react-native-firebase```를 사용하였습니다.

- react-native-firebase admob 사용 방법: [react-native-firebase-admob]({{site.url}}/react-native/react-native-firebase-admob/){:target="_blank"}
- react-native-firebase analytics 사용 방법: [react-native-firebase-analytics]({{site.url}}/react-native/react-native-firebase-analytics/){:target="_blank"}
- react-native-firebase Crasylytics 사용 방법: [firebase-crashlytics]({{site.url}}/react-native/firebase-crashlytics/){:target="_blank"}

아래의 목록은 부가적인 기능을 구현하기 위해 사용한 라이브러리입니다.

- RN(React Native)에서 메일 발송: [react-native-mail]({{site.url}}/react-native/react-native-mail/){:target="_blank"}
- RN(React Native)에서 리뷰 안내: [react-native-rate]({{site.url}}/react-native/react-native-rate/){:target="_blank"}
- RN(React Native)에서 splash 이미지 조절: [react-native-splash-screen]({{site.url}}/react-native/react-native-splash-screen/){:target="_blank"}
- RN(React Native)에서 TTS(Text To Speech) 사용하기: [react-native-tts]({{site.url}}/react-native/react-native-tts/){:target="_blank"}


## 앱 등록
이전 프로젝트에서는 앱 등록에 많은 어려움을 겪었습니다.([BlaBoo 앱 개발기(RN, React Native)]({{site.url}}/blaboo/development-journal/){:target="_blank"}) 그 때의 경험 덕인지, 이번 프로젝트의 앱 등록엔 큰 어려움없이 진행할 수 있었습니다.

iOS는 어린이 카테고리를 선택하여 등록을 시도하였으나, 외부 링크가 있어 심사 거절(Reject)을 받았습니다. 어린이 카테고리인 경우 Parental Gate라는 기능으로 외부 링크를 보호해야 하는 의무가 있는데 이를 무시했기 때문에 문제가 되었습니다. Parental Gate에 관한 라이브러리를 찾지 못했기 때문에, 어린이 카테고리를 포기하고 등록 신청을 하여 등록하였습니다.

<div class="download_link_container">
    <a class="download_link_ios" href="https://itunes.apple.com/app/kumoncho/id1450902241" target="_blank">
        <img src="/assets/images/apple_download.png" alt="children picture fairy tale book, Kumoncho iOS download"/>
    </a>
    <a class="download_link_android" href="https://play.google.com/store/apps/details?id=io.github.dev.yakuza.kumoncho" target="_blank">
        <img src="/assets/images/google play_download.png" alt="children picture fairy tale book, Kumoncho Android download"/>
    </a>
</div>


## 마지막으로
이번 어린이 동화책 앱 프로젝트에서는 기획 단계에서 좀 더 벤치마킹과 경쟁사(동화책)를 분석했어야 했습니다. 우리는 페이지 장수가 결정나자 스토리와 일러스트에 집중하는 바람에 정작 한 페이지에 들어갈 내용, 즉 문자수를 결정하지 않은 실수를 저질렀습니다. ```스토리와 일러스트``` 섹션에서 일러스트 그림을 보셔서 아시겠지만, 처음 일러스트에는 그림만 있었습니다. 앱을 개발하는 단계에서 그림에 대한 내용을 전달하기 위해, 뒤늦게 내용을 집어 넣어습니다. 그 바람에 일러스트의 구도와 스토리 전달력이 떨어지는 문제가 발생하게 되었습니다

또한 책을 기준으로 작업하다 보니, 앱으로 책을 읽는 부분, 즉 UX를 깊게 생각하지 못했습니다. 지금도 중간에 앱을 종료하고 앱은 새로 시작하는 경우, 항상 처음부터 전부 다시 봐야한다. 중간 페이지로 넘어가는 기능도 없다. UX에서는 완전히 실패한 프로젝트라고 생각된다.

개발쪽에도 문제가 있습니다. 앱을 배포한 후, 작가 친구가 태블릿을 지원하면 좋겠다고 했습니다. RN(React Native)는 원래 크로스플랫폼을 지원함으로 간단히 전환을 될 줄 알았습니다. 실제로 이전 프로젝트([BlaBoo 앱 개발기(RN, React Native)]({{site.url}}/blaboo/development-journal/){:target="_blank"})는 워낙 간단한 앱이여서 그런지 간단하게 전환되었습니다. 하지만 이번 프로젝트는 이미지가 많고 그 이미지의 위치를 설정하는 부분에서 태블릿을 고려하지 않은 설계로 태블릿 전환에 실패하였다. 시간이 있으면 고쳐서 태블릿도 지원할 예정이지만 처음부터 잘 만들었어야 했습니다.

<div class="download_link_container">
    <a class="download_link_ios" href="https://itunes.apple.com/app/kumoncho/id1450902241" target="_blank">
        <img src="/assets/images/apple_download.png" alt="children picture fairy tale book, Kumoncho iOS download"/>
    </a>
    <a class="download_link_android" href="https://play.google.com/store/apps/details?id=io.github.dev.yakuza.kumoncho" target="_blank">
        <img src="/assets/images/google play_download.png" alt="children picture fairy tale book, Kumoncho Android download"/>
    </a>
</div>

정말 마지막으로, 출판 업계에 계신 분중 저희 앱을 책으로 출판하고 싶은 분이 계시면 연락주시기 바랍니다!!

<a href="mailto:dev.yakuza@gmail.com">dev.yakuza@gmail.com</a>
