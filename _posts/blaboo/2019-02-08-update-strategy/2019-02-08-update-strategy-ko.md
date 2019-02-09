---
published: false
layout: 'post'
permalink: '/blaboo/update-strategy/'
paginate_path: '/blaboo/:num/update-strategy/'
lang: 'ko'
categories: 'blaboo'
comments: true

title: 'BlaBoo 업데이트 기록'
description: 'RN(React Native)를 사용하여 BlaBoo라는 앱을 제작하고 배포하였습니다. 앱 배포후 BlaBoo는 어떤 업데이트 전략을 취하고 있는지 설명합니다.'
image: '/assets/images/category/blaboo/update-strategy.png'
---


## 개요
RN(React Native)를 사용하여 BlaBoo라는 앱을 제작하고 배포하였습니다. 이 블로그에서는 앱 배포후 BlaBoo를 어떻게 관리하고 있는지, 어떤 업데이트 전략을 취하고 있는지에 대해 이야기해 보려고 합니다. BlaBoo를 간단하게 다시 한번 소개하고 본격적인 이야기를 해 보도록 하겠습니다.


## BlaBoo란?
BlaBoo(블라부)는 영어의 ```blah blah(블라 블라)```라는 단어와 아기들이 잘 내는 ```boo(부)```라는 단어를 합친 의미로, 유아/어린이를 대상으로 하는 단어 공부 앱입니다.

- BlaBoo 소개 페이지: [BlaBoo]( https://dev-yakuza.github.io/app/blaboo/ko/){:target="_blank"}

아래는 BlaBoo 앱을 다운로드 받을 수 있는 링크 입니다.

- 다운로드: [애플 앱 스토어](https://itunes.apple.com/app/blaboo/id1441741187){:rel="nofollow noreferrer" target="_blank"}
- 다운로드: [구글 앱 스토어](https://play.google.com/store/apps/details?id=io.github.dev.yakuza.blaboo){:rel="nofollow noreferrer" target="_blank"}

유아/어린이가 그림을 보고 그 그림을 선택하면 음성으로 단어를 읽어주는 아주 간단한 앱입니다.

![유아/어린이용 단어 공부 앱 BlaBoo 개발기](/assets/images/category/blaboo/update-strategy/app_concept.png)

앱 개발기에 관한 자세한 내용은 이전 블로그를 참고해 주세요.

- [BlaBoo 앱 개발기(RN, React Native)]({{site.url}}/react-native/development-journal/){:target="_blank"}


## 앱 관리
사실 처음 BlaBoo 앱을 기획할 때는 앱이 정말로 간단해서 딱히 관리하지 않아도 될 거라고 생각하였습니다. 한번 만들고 방치하면 필요한 사람들이 알아서 다운받고 지우고 하겠지...라는 생각으로 개발했습니다.

하지만 막상 앱을 배포하고 사람들이 다운로드를 하니 처음 생각과는 달리 자꾸 손이 가게 되었습니다.

![유아/어린이용 단어 공부 앱 BlaBoo 개발기](/assets/images/category/blaboo/update-strategy/blaboo_analytics.png)

## 업데이트
BlaBoo는 처음에 영어, 일본어, 한국어만 번역하여 배포하였습니다. 일단 제 눈으로 확인할 수 있는 언어만을 대상으로 하였기 때문에 핵심 기능인 단어 음성 기능에는 별 문제가 없다고 생각했습니다.

그러나 앱 배포후 첫 다운로드는 중국에서 발생했고, 그로 인해 급히 구글 번역기를 통해 중국어로 번역하여 첫 업데이트를 하였습니다.

- [중국어 홍보 사이트](https://dev-yakuza.github.io/app/blaboo/zh/){:target="_blank"}

![BlaBoo 업데이트 전략 - 중국어](/assets/images/category/blaboo/update-strategy/blaboo_zh.png)

구글 번역기이다보니 단어를 제대로 번역한건지, 사이트를 제대로 번역한 건지 알수가 없습니다. 다행이 타이완 친구가 있어 앱을 사용 테스트를 해봤는데 단어가 잘 맞는거 같다고 하여 안심했습니다만, 그 친구도 전 단어를 다 들어본게 아니여서 아직도 걱정이 남아있습니다.

그래도 조금 틀린 언어가 있더라도 자국어를 지원하는게 더 매력적이지 않을까하는 생각에 이때부터 다운로드 국가를 확인하면서 다운로드가 발생한 국가의 언어로 앱과 사이트를 번역하며 하나씩 하나씩 추가하였습니다.

이렇게 하나씩 하나씩 추가하다 베트남어를 추가할 때, 베트남어를 추가할 때 문제가 발생하였습니다. 구글 번역기를 사용하여 단어를 번역한 후 테스트하는 과정에서 베트남어를 제대로 발음하지 못하는 것을 확인하였습니다. 문제의 원인을 파악한 결과, 사용하는 라이브러리에서 베트남어를 지원하지 않았습니다.

BlaBoo는 TTS(Text To Speech) 기능으로 아래에 라이브러리를 사용하고 있습니다.

- react-native-tts 소개: [react-native-tts]({{site.url}}/react-native/react-native-tts/){:target="_blank"}

이 라이브러리는 지원하는 언어-국가가 정해져있습니다.

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

저는 언어-국가 코드는 아래에 사이트에서 확인하고 있습니다.

- [https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html){:rel="nofollow noreferrer" target="_blank"}

이 사이트에서 베트남어-베트남을 찾아보면 ```vi-VN```이라는 것을 확인할 수 있고, 이 언어-국가 코드가 위에 리스트에 없는 것을 확인할 수 있었습니다. ```git checkout .```으로 한 시간 가량 작업한 내용을 다시 되돌리는 뼈아픈 경험을 했습니다.

이후 다운로드를 확인하고 다운로드가 발생한 국가가 지금까지 추가하지 않은 국가인 경우 먼저 언어-국가 코드를 확인하여 ```react-native-tts```가 지원하는지 확인하게 되었습니다.

## 업데이트 전략
업데이트 전략이라고 거창하게 썼지만, 결국 단순한 절차로 업데이트를 결정하고 있습니다.

1. 다운로드가 발생한 국가 확인
1. 이미 번역이 추가된 국가인지 확인
1. 번역이 되어 있지 않은 국가이면 언어-국가 코드 확인
1. 언어-국가 코드가 라이브러리(```react-native-tts```)에서 지원하는지 확인
1. 라이브러리(```react-native-tts```)가 언어-국가 코드를 지원하는 경우 앱, 웹, 앱스토어, 스크린샷 번역
1. 테스트
1. iOS, 안드로이드 배포

간단해 보일 수 있지만, 여러 실패를 통한 절차를 나름 정리해서 사용하고 있습니다. 여러분도 혹시 ```react-native-tts```를 사용하고 다국어를 지원하는 앱을 기획/개발할 예정이시라면 라이브러리가 제공하는 언어를 확인하시길 권장합니다.

## 결론
사실 이 블로그를 쓴 가장 큰 이유는 여러분의 힘을 빌리고자 함에 있습니다. 위에서도 이야기했지만 영어, 일본어, 한국어 이외에 언어는 구글 번역기를 통해서 번역을 진행하고 있습니다. 웹이나 앱스토어에 내용은 조금 틀려도 크게 문제가 되지 않지만, BlaBoo 앱의 특성상 어린이 또는 외국어를 배우는 사람들을 대상으로 하기 때문에 앱내에 단어는 틀리면 안된다고 생각합니다. 하지만 제가 전 세계 언어를 알고 있는 것도 아니고, 그렇다고 돈이 많아 전부 번역할 수 있는 상황이 아니여서 이렇게 염치불구하고 글을 쓰게 되었습니다.

아래는 BlaBoo 앱내에서 사용하고 있는 다국어 파일을 정리해서 공개한 저장소(Repository)입니다. 혹시 외국어가 특기이신 분들은 아래에 저장소(Repository)를 보시고 단어를 수정해 주십사 부탁드리고 싶습니다.

- github: [https://github.com/dev-yakuza/blaboo-translate](https://github.com/dev-yakuza/blaboo-translate){:target="_blank"})

여러분의 도움이 한 개발자에게 큰 희망이, 많은 사용자들에게는 제대로 된 단어 학습이 가능하도록 만들어 줍니다.
