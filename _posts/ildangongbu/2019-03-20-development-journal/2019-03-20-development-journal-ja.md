---
layout: 'post'
permalink: '/ildangongbu/development-journal/'
paginate_path: '/ildangongbu/:num/development-journal/'
lang: 'ja'
categories: 'ildangongbu'
comments: true

title: '「일단공부(イルタンコンブ)」アプリ開発日誌(RN, React Native)'
description: 'RN(React Native)を使って「일단공부(イルタンコンブ)」と言うJLPT日本語単語勉強アプリを開発してみました。このアプリを開発した時のエピソードをまとめてみました。'
image: '/assets/images/category/ildangongbu/background.png'
---

## 概要
RN(React Native)を使って開発したアプリがもう3番目ですね。下記は以前のアプリを作る時作成した開発日誌です。以前のアプリが気になる方は下記のリンクをクリックして確認してください。

- [BlaBooアプリ開発日誌(RN, React Native)]({{site.url}}/blaboo/development-journal/){:target="_blank"}
- [Kumonchoアプリ開発日誌(RN, React Native)]({{site.url}}/kumoncho/development-journal/){:target="_blank"}

このアプリは韓国人向けの日本語単語アプリです。


## 일단 공부란?
JLPT 일본어 단어를 레벨별로 공부할 수 있으며, 하루하루 공부할 수 있는 분량과 복습 기능으로 단어 암기를 도와주는 앱입니다.

- 일단 공부 소개 페이지: [일단 공부]( https://dev-yakuza.github.io/app/ildangongbu/){:target="_blank"}

아래는 앱을 다운로드 받을 수 있는 링크입니다.

<div class="download_link_container">
    <a class="download_link_ios" href="https://itunes.apple.com/app/id1456091125" target="_blank">
        <img src="/assets/images/apple_download.png" alt="JLPT 일본어 단어 앱, 일단 공부 ios 다운로드"/>
    </a>
    <a class="download_link_android" href="https://play.google.com/store/apps/details?id=io.github.dev.yakuza.ildangongbu" target="_blank">
        <img src="/assets/images/google play_download.png" alt="JLPT 일본어 단어 앱, 일단 공부 안드로이드 다운로드"/>
    </a>
</div>


## 왜 만들게 되었나?
개요에서도 잠깐 이야기 했지만, 책을 들고 일본의 전철(지옥철)에서 공부하기가 너무 어렵습니다. 그리고 책은 단어와 의미가 같이 보여서, 의식적으로 의미를 안보려고 노력하지만 자꾸 의미가 눈에 들어옵니다. 아직 한자를 잘 모를때는 어떻게 발음해야 하는지 잘 모를때도 있습니다. 그리고 단어 공부는 반복해서 봐야하는데 이놈의 책으로 반복해서 보자니 앞 챕터에서 계속 머물게 됩니다. 이런 문제들을 해결하고자 간단한 JLPT 일본어 단어 앱을 제작하게 되었습니다.

![JLPT 일본어 단어 앱, 일단 공부](/assets/images/category/ildangongbu/background.png)


## 앱 기획
일단 네이밍은 일본어 단어 공부의 `일`본어 `단`어 `공부`에서 따왔습니다. 이중적인 의미로 `일단 공부하자`라는 의미도 포함하고 있습니다.

일단 공부의 MVP(Minimum Viable Product: 최소 기능 제품)는 아래와 같이 정의했습니다.

1. JLPT 일본어 단어를 레벨별로 볼 수 있다.
1. 하루하루 공부할 분량(15 단어)로 단어를 볼 수 있다.
1. 일본어 단어가 의미가 보이지 않는 상태로 리스트로 보인다.
1. 의미를 보기 위한 버튼이 있고 읽는 방법(히라가나/가타카나)과 의미가 보인다.
1. 읽는 방법을 선택하면 단어를 읽어준다.
1. 공부한 단어를 테스트를 통해 복습한다.
1. 테스트시 틀린 단어를 보여준다.
1. 레벨별 또는 전체 단어를 복습할 수 있는 기능을 추가한다.
1. 복습 기능에는 자주 틀리는 단어를 자주 보여주는 로직을 넣는다.

이렇게 정리하다보니 꽤 많은 기능이 있는 것처럼 보이네요. 최대한 단순하게 만들기 위해 노력했지만 역시 제가 쓰기 편한 앱을 만들다 보니 여러 기능이 추가되었습니다. 사실 더 많은 기능을 넣고 싶었지만, 우선 MVP, MVP!


## 디자인
역시 디자인 센스가 제로네요...어떤 디자인이 좋은가 여러 패턴을 만들고 여러 색상을 넣어서 도전해봤지만...아직도 디자인은 어렵습니다.

![JLPT 일본어 단어 앱 일단 공부 디자인](/assets/images/category/ildangongbu/development-journal/ildangongbu-design.png)

디자인은 `sketchapp`으로 제작했습니다. 여러 디자인 패턴중에서 최대한 간단한 디자인을 선택했습니다. 또한 불필요한 화면도 제거하고 최종적으로 아래와 같은 디자인을 선택했습니다.

![JLPT 일본어 단어 앱 일단 공부 디자인](/assets/images/category/ildangongbu/development-journal/ildangongbu-final-design.png)

디자이너분들 존경합니다.


## 앱 개발
앱 개발에는 당연히 RN(React Native)를 사용하였습니다. 일단공부는 기본적으로 RN(```React Native```)과 타입스크립트(```typescript```)를 사용합니다.

- RN(React Native) 설치 방법: [RN 설치]({{site.url}}/react-native/installation/){:target="_blank"}
- RN(React Native)에 typescript 적용하기: [typescript]({{site.url}}/react-native/typescript/){:target="_blank"}

또한 RN(React Native)의 기본적인 UI는 ```NativeBase```를 스타일에는 ```styled-components```을 사용하였습니다.

- RN(React Native)에 NativeBase 적용하기: [nativebase]({{site.url}}/react-native/nativebase/){:target="_blank"}
- RN(React Navtive)에서 styled-components 사용하기: [styled-components]({{site.url}}/react-native/styled-components/){:target="_blank"}

일단 공부의 기본 네비게이션 시스템으로는 ```react-navigation```을 사용하고 있습니다.

- react-navigation 사용 방법: [react-navigation]({{site.url}}/react-native/react-navigation/){:target="_blank"}

MVP(Minimum Viable Product: 최소 기능 제품)의 기능중 하나인 음성 지원은 ```react-native-tts```를 사용하여 ```tts(Text To Speech)``` 기능을 구현하였습니다.

- react-native-tts 사용 방법: [react-native-tts]({{site.url}}/react-native/react-native-tts/){:target="_blank"}

일단 공부앱에서 사용되는 단어는 sqlite를 사용하여 앱과 함께 배포하고 있습니다. 앱에서 sqlite를 사용하는 방법은 아래에 링크를 통해 확인할 수 있습니다.

- react-native-sqlite-storage 사용 방법: [react-native-sqlite-storage]({{site.url}}/react-native/react-native-sqlite-storage/){:target="_blank"}

최종적으로 앱의 광고와 분석을 위해 구글의 파이어베이스(Google Firebase)와 구글 애드몹(Google Admob)을 사용하였습니다. 이를 앱에 구현하기 위해 ```react-native-firebase```를 사용하였습니다.

- react-native-firebase admob 사용 방법: [react-native-firebase-admob]({{site.url}}/react-native/react-native-firebase-admob/){:target="_blank"}
- react-native-firebase analytics 사용 방법: [react-native-firebase-analytics]({{site.url}}/react-native/react-native-firebase-analytics/){:target="_blank"}
- react-native-firebase Crasylytics 사용 방법: [firebase-crashlytics]({{site.url}}/react-native/firebase-crashlytics/){:target="_blank"}


## 마지막으로
이번 앱은 단어를 보여주는 단순한 앱이였습니다. 역시 디자인에서 시간이 제일 많이 걸렸네요. 또한 `react-native-sqlite-storage`가 안드로이드에서는 퍼포먼스 문제가 있는거 같습니다. 로컬에서 데이터를 읽어오는데 서버에서 받아오는 것처럼 시간이 많이 걸리네요. 제가 앱을 잘못 만든걸지도...다시 한번 sql 튜닝을 해보고 안되면 라이브러리 소스도 좀 봐봐야 할거 같습니다.

일본어 단어 공부하시는 분들 「일단 공부」해보세요.^^

<div class="download_link_container">
    <a class="download_link_ios" href="https://itunes.apple.com/app/id1456091125" target="_blank">
        <img src="/assets/images/apple_download.png" alt="JLPT 일본어 단어 앱, 일단 공부 ios 다운로드"/>
    </a>
    <a class="download_link_android" href="https://play.google.com/store/apps/details?id=io.github.dev.yakuza.ildangongbu" target="_blank">
        <img src="/assets/images/google play_download.png" alt="JLPT 일본어 단어 앱, 일단 공부 안드로이드 다운로드"/>
    </a>
</div>