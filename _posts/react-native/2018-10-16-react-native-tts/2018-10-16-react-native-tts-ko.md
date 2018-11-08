---
layout: 'post'
permalink: '/react-native/react-native-tts/'
paginate_path: '/react-native/:num/react-native-tts/'
lang: 'ko'
categories: 'react-native'
comments: true

title: 'react-native-tts'
description: 'react-native-tts를 사용하여 text-to-speech 기능을 구현해보자.'
image: '/assets/images/category/react-native/react-native-tts.jpg'
---


## 개요
[react-native-tts](https://github.com/ak1394/react-native-tts){:rel="nofollow noreferrer" :target="_blank" }를 사용하여 RN 프로젝트에서 text-to-speech 기능을 구현해보도록 하겠습니다.

## 라이브러리 설치
아래에 명령어로 react-native-tts을 설치합니다.

{% include_relative common/installation.md %}

설치가 완료되면 아래에 명령어로 react-native-tts 라이브러리와 프로젝트를 연결합니다.

{% include_relative common/link.md %}

## 사용법
우리는 기본적으로 사용한적이 있는 경우만 블로그로 작성합니다. 따라서 여기에 작성된 내용은 우리가 사용할 때마다 추가될 것입니다.

사용법에 대한 자세한 사항은 공식 홈페이지를 참조하세요.
- 공식 사이트: [react-native-tts](https://github.com/ak1394/react-native-tts){:rel="nofollow noreferrer" :target="_blank" }

## text-to-speech.
아래에 방법으로 text-to-speech를 구현합니다.

{% include_relative common/usage.md %}

- setDefaultLanguage: 언어 설정을 합니다. 언어 코드는 [Language codes](https://docs.fedoraproject.org/en-US/Fedora_Contributor_Documentation/1/html/Users_Guide/appe-Users_Guide-Language_codes.html){:rel="nofollow noreferrer" :target="_blank" }을 참고하세요.
- speak: 해당 단어를 소리내어 읽습니다.

## 참고
- 공식 사이트: [react-native-tts](https://github.com/ak1394/react-native-tts){:rel="nofollow noreferrer" :target="_blank" }
- Language codes: [Language codes](https://docs.fedoraproject.org/en-US/Fedora_Contributor_Documentation/1/html/Users_Guide/appe-Users_Guide-Language_codes.html){:rel="nofollow noreferrer" :target="_blank" }