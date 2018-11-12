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

## 기본 목소리 설정
기본 목소리 설정은 ```setDefaultLanguage```를 해당 국가로 설정하면 자동으로 변경됩니다. 따라서 ```setDefaultLanguage```를 사용하여 국가를 변경하는 경우 아래에 목소리 설정을 따로 해줄 필요가 없습니다.

react-native-tt는 기본 목소리 설정이 가능합니다. 아래에 코드를 사용하여 기본 목소리 설정을 변경해 보세요.

```js
Tts.setDefaultVoice('com.apple.ttsbundle.Yuna-compact');
```

지원하는 목소리를 확인하고 싶은 분은 아래에 코드를 이용하면 확인이 가능합니다.

```js
Tts.voices().then(voices => console.log(voices));
```

우리가 확인한 목소리 리스트는 아래와 같습니다.

### iOS 지원 목소리 리스트
아래에 리스트에서 원하는 목소리의 ```id```를 ```setDefaultVoice``` 함수의 파라미터로 넘겨서 설정이 가능합니다.

```js
{language: "ar-SA", id: "com.apple.ttsbundle.Maged-compact", quality: 300, name: "Maged"}
{language: "cs-CZ", id: "com.apple.ttsbundle.Zuzana-compact", quality: 300, name: "Zuzana"}
{language: "da-DK", id: "com.apple.ttsbundle.Sara-compact", quality: 300, name: "Sara"}
{language: "de-DE", id: "com.apple.ttsbundle.Anna-compact", quality: 300, name: "Anna"}
{language: "el-GR", id: "com.apple.ttsbundle.Melina-compact", quality: 300, name: "Melina"}
{language: "en-AU", id: "com.apple.ttsbundle.Karen-compact", quality: 300, name: "Karen"}
{language: "en-GB", id: "com.apple.ttsbundle.Daniel-compact", quality: 300, name: "Daniel"}
{language: "en-IE", id: "com.apple.ttsbundle.Moira-compact", quality: 300, name: "Moira"}
{language: "en-US", id: "com.apple.ttsbundle.Samantha-compact", quality: 300, name: "Samantha"}
{language: "en-ZA", id: "com.apple.ttsbundle.Tessa-compact", quality: 300, name: "Tessa"}
{language: "es-ES", id: "com.apple.ttsbundle.Monica-compact", quality: 300, name: "Monica"}
{language: "es-MX", id: "com.apple.ttsbundle.Paulina-compact", quality: 300, name: "Paulina"}
{language: "fi-FI", id: "com.apple.ttsbundle.Satu-compact", quality: 300, name: "Satu"}
{language: "fr-CA", id: "com.apple.ttsbundle.Amelie-compact", quality: 300, name: "Amelie"}
{language: "fr-FR", id: "com.apple.ttsbundle.Thomas-compact", quality: 300, name: "Thomas"}
{language: "he-IL", id: "com.apple.ttsbundle.Carmit-compact", quality: 300, name: "Carmit"}
{language: "hi-IN", id: "com.apple.ttsbundle.Lekha-compact", quality: 300, name: "Lekha"}
{language: "hu-HU", id: "com.apple.ttsbundle.Mariska-compact", quality: 300, name: "Mariska"}
{language: "id-ID", id: "com.apple.ttsbundle.Damayanti-compact", quality: 300, name: "Damayanti"}
{language: "it-IT", id: "com.apple.ttsbundle.Alice-compact", quality: 300, name: "Alice"}
{language: "ja-JP", id: "com.apple.ttsbundle.Kyoko-compact", quality: 300, name: "Kyoko"}
{language: "ko-KR", id: "com.apple.ttsbundle.Yuna-compact", quality: 300, name: "Yuna"}
{language: "nl-BE", id: "com.apple.ttsbundle.Ellen-compact", quality: 300, name: "Ellen"}
{language: "nl-NL", id: "com.apple.ttsbundle.Xander-compact", quality: 300, name: "Xander"}
{language: "no-NO", id: "com.apple.ttsbundle.Nora-compact", quality: 300, name: "Nora"}
{language: "pl-PL", id: "com.apple.ttsbundle.Zosia-compact", quality: 300, name: "Zosia"}
{language: "pt-BR", id: "com.apple.ttsbundle.Luciana-compact", quality: 300, name: "Luciana"}
{language: "pt-PT", id: "com.apple.ttsbundle.Joana-compact", quality: 300, name: "Joana"}
{language: "ro-RO", id: "com.apple.ttsbundle.Ioana-compact", quality: 300, name: "Ioana"}
{language: "ru-RU", id: "com.apple.ttsbundle.Milena-compact", quality: 300, name: "Milena"}
{language: "sk-SK", id: "com.apple.ttsbundle.Laura-compact", quality: 300, name: "Laura"}
{language: "sv-SE", id: "com.apple.ttsbundle.Alva-compact", quality: 300, name: "Alva"}
{language: "th-TH", id: "com.apple.ttsbundle.Kanya-compact", quality: 300, name: "Kanya"}
{language: "tr-TR", id: "com.apple.ttsbundle.Yelda-compact", quality: 300, name: "Yelda"}
{language: "zh-CN", id: "com.apple.ttsbundle.Ting-Ting-compact", quality: 300, name: "Ting-Ting"}
{language: "zh-HK", id: "com.apple.ttsbundle.Sin-Ji-compact", quality: 300, name: "Sin-Ji"}
{language: "zh-TW", id: "com.apple.ttsbundle.Mei-Jia-compact", quality: 300, name: "Mei-Jia"}
```
## 참고
- 공식 사이트: [react-native-tts](https://github.com/ak1394/react-native-tts){:rel="nofollow noreferrer" :target="_blank" }
- Language codes: [Language codes](https://docs.fedoraproject.org/en-US/Fedora_Contributor_Documentation/1/html/Users_Guide/appe-Users_Guide-Language_codes.html){:rel="nofollow noreferrer" :target="_blank" }