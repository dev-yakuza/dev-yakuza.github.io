---
layout: 'post'
permalink: '/blaboo/update-review/'
paginate_path: '/blaboo/:num/update-review/'
lang: 'ko'
categories: 'blaboo'
comments: true

title: 'BlaBoo 업데이트 후기'
description: 'RN(React Native)를 사용하여 BlaBoo라는 앱을 제작하고 배포하였습니다. 앱 배포후 BlaBoo는 어떤 업데이트 하고 있는지에 대해 설명합니다.'
image: '/assets/images/category/blaboo/update-review/app_concept.png'
---


## 개요
RN(React Native)를 사용하여 BlaBoo라는 앱을 제작하고 배포하였습니다. 이 블로그에서는 앱 배포후 BlaBoo를 어떻게 관리하고 업데이트하고 있는지에 대해 이야기해 보려고 합니다. BlaBoo를 간단하게 다시 한번 소개하고 본격적인 이야기를 해 보도록 하겠습니다.


## BlaBoo란?
BlaBoo(블라부)는 영어의 ```blah blah(블라 블라)```라는 단어와 아기들이 잘 내는 ```boo(부)```라는 단어를 합친 의미로, 유아/어린이를 대상으로 하는 단어 공부 앱입니다.

- BlaBoo 소개 페이지: [BlaBoo]( https://dev-yakuza.github.io/app/blaboo/ko/){:target="_blank"}

아래는 BlaBoo 앱을 다운로드 받을 수 있는 링크 입니다.

<div class="download_link_container">
    <a class="download_link_ios" href="https://itunes.apple.com/app/blaboo/id1441741187" target="_blank">
        <img src="/assets/images/apple_download.png" alt="어린이 단어 학습 앱 blaboo iOS 다운로드"/>
    </a>
    <a class="download_link_android" href="https://play.google.com/store/apps/details?id=io.github.dev.yakuza.blaboo" target="_blank">
        <img src="/assets/images/google play_download.png" alt="어린이 단어 학습 앱 blaboo 안드로이드 다운로드"/>
    </a>
</div>

유아/어린이가 그림을 보고 그 그림을 선택하면 음성으로 단어를 읽어주는 아주 간단한 앱입니다.

![유아/어린이용 단어 공부 앱 BlaBoo 개발기](/assets/images/category/blaboo/update-review/app_concept.png)

앱 개발에 관한 자세한 내용은 이전 블로그를 참고해 주세요.

- [BlaBoo 앱 개발기(RN, React Native)]({{site.url}}/react-native/development-journal/){:target="_blank"}


## 앱 관리
사실 처음 BlaBoo 앱을 기획할 때는 앱이 정말로 간단해서 딱히 관리하지 않아도 될 거라고 생각하였습니다. 한번 만들고 배포하면 필요한 사람들이 다운받고 지우고 할거라는 생각으로 개발했습니다.

하지만 막상 앱을 배포하고 사람들이 다운로드를 하니 처음 생각과는 달리 자꾸 손이 가게 되었습니다.

![유아/어린이용 단어 공부 앱 BlaBoo 개발기](/assets/images/category/blaboo/update-review/blaboo_analytics.png)


## 업데이트
BlaBoo는 처음에 영어, 일본어, 한국어만 번역하여 배포하였습니다. 일단 제 눈으로 확인할 수 있는 언어만을 대상으로 하였기 때문에 핵심 기능인 단어 음성 기능에는 별 문제가 없다고 생각했습니다.

그러나 앱 배포후 첫 다운로드는 중국에서 발생했고, 그로 인해 급히 구글 번역기를 통해 중국어로 번역하여 첫 업데이트를 하였습니다.

- [중국어 홍보 사이트](https://dev-yakuza.github.io/app/blaboo/zh/){:target="_blank"}

![BlaBoo 업데이트 전략 - 중국어](/assets/images/category/blaboo/update-review/blaboo_zh.png)

구글 번역기이다보니 단어를 제대로 번역한건지, 사이트를 제대로 번역한 건지 알수가 없습니다. 다행이 타이완 친구가 있어 앱을 사용 테스트를 해봤는데 단어가 잘 맞는거 같다고 하여 안심했습니다만, 그 친구도 모든 단어를 다 들어본게 아니여서 여전히 걱정이 남아있습니다.

그래도 조금 틀린 언어가 있더라도 자국어를 지원하는게 더 매력적이지 않을까하는 생각에 이때부터 다운로드 국가를 확인하면서 다운로드가 발생한 국가의 언어로 앱과 사이트를 번역하며 업데이트를 진행하였습니다.

이렇게 업데이트를 진행하다가 베트남어를 추가할 때 문제가 발생하였습니다. 구글 번역기를 사용하여 단어를 번역한 후 테스트하는 과정에서 베트남어를 제대로 발음하지 못하는 것을 확인하였습니다. 문제의 원인을 파악한 결과, 사용하는 라이브러리에서 베트남어를 지원하지 않았습니다.

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

저는 언어-국가 코드를 아래에 사이트에서 확인하고 있습니다.

- [https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html){:rel="nofollow noreferrer" target="_blank"}

이 사이트에서 베트남어-베트남을 찾아보면 ```vi-VN```이라는 것을 확인할 수 있고, 이 언어-국가 코드가 위에 리스트에 없는 것을 확인할 수 있었습니다. ```git checkout .```으로 한 시간 가량 작업한 내용을 다시 되돌리는 뼈아픈 경험을 했습니다.

이후 다운로드 국가를 확인하고 다운로드가 발생한 국가가 지금까지 추가하지 않은 국가인 경우 먼저 언어-국가 코드를 확인하여 ```react-native-tts```가 지원하는지 확인하게 되었습니다.


## 안드로이드 버그
앱을 공개한 후, 별다른 문제가 없어보였습니다. 저는 아이폰 유저다보니 안드로이드에 대해서 크게 신경쓰지 못했습니다. 그런데 친구중 한명이 안드로이드에서 버튼이 눌리지 않는다고 피드백을 주었습니다. 아마 이 친구가 이 버그를 찾지 않았으면 영원히 쓰레기 앱으로 안드로이드 마켓에 남아 있을거 같습니다.

BlaBoo에서는 일러스트가 등작할 때 바운스인(bounceIn) 애니메이션을 ```react-native-animatable```이라는 라이브러리를 사용하여 구현하고 있습니다.

- react-native-animatable 사용 방법: [react-native-animatable]({{site.url}}/react-native/react-native-animatable/){:target="_blank"}

BlaBoo 앱에서는 하나의 뷰위에 이미지 리스트를 ```map```을 사용하여 보여주고 있고, 페이지 전환시 이 이미지 리스트를 갱신함으로써 새로운 이미지들을 보여주고 있습니다.

```js
{pageData.things.map((lineData: Array<IThing>, lineIndex: number) =>
    lineData.map((item: IThing, index: number) => (
        <Animatable.View
            key={`${pageIndex}-${lineIndex}-${index}`}
            animation="bounceIn"
            delay={(index + 2) * 100}
            useNativeDriver={true}>
                <Thing
                    row={item.row}
                    column={item.column}
                    width={this._calculateWidth(pageData.lines[lineIndex])}
                    height={thingHeight}
                    marginRow={item.marginRow}
                    marginColumn={item.marginColumn}
                    src={item.src}
                    locale={locale}
                    text={item[locale]}
                />
        </Animatable.View>
    ))
)}
```

그런데 안드로이드에서 이미지를 갱신하였지만, 이전 ```Animatable.View```가 화면에 남아 있어, 새로운 이미지 위에 표시되고 있었습니다. ```react-native-animatable```은 애니메이션의 퍼포먼스(Performance)를 위해 Native Driver를 사용할 수 있도록 ```useNativeDriver``` 옵션을 제공하고 있습니다. 위에 소스를 보면 알 수 있듯이 저도 당연히 퍼포먼스(Performance)를 위해 이 옵션을 사용하고 있었습니다.

정확히 원인은 모르겠지만, 이 옵션을 제거하면 정상적으로 동작하였습니다. 하지만 정확한 원인 분석이 되지 않은 상태였고, 이미 배포한 상태에서 아주 큰 이슈였기 때문에 ```Animatable.View```를 제거하는 업데이트를 하였습니다. 등장 애니메이션이 없어져 조금 아쉬웠지만, 정확한 원인을 모른체로 이 기능을 사용하기에는 리스크가 너무 컸기 때문에 완전 제거로 결정하였습니다. 혹시 같은 문제를 겪으신 분중에 원인을 파악하신 분이 계신다면 공유해 주시면 좋겠네요.


## 업데이트 후기
지금의 업데이트는 아래와 같이 단순한 절차로 진행하고 있습니다.

1. 다운로드가 발생한 국가 확인
1. 이미 번역이 추가된 국가인지 확인
1. 번역이 되어 있지 않은 국가이면 언어-국가 코드 확인
1. 언어-국가 코드가 라이브러리(```react-native-tts```)에서 지원하는지 확인
1. 라이브러리(```react-native-tts```)가 언어-국가 코드를 지원하는 경우 앱, 웹, 앱스토어, 스크린샷 번역
1. 테스트
1. iOS, 안드로이드 배포

간단해 보일 수 있지만, 여러 실패를 통한 절차를 나름 정리해서 사용하고 있습니다. 여러분도 혹시 ```react-native-tts```를 사용하고 다국어를 지원하는 앱을 기획/개발할 예정이시라면 라이브러리가 제공하는 언어를 확인하시길 권장합니다.

지금까지 첫 배포후 업데이트 한 내용은 아래와 같습니다.

1. Splash 스크린을 강제로 1초간 유지한 후 앱 실행(사용한 라이브러리: [react-native-splash-screen]({{site.url}}/react-native/react-native-splash-screen/){:target="_blank"})
1. 앱 리뷰에 숫자를 더 추가해달라고 하는 요청이 있어 숫자 내용 추가
1. 앱의 첫 화면에서 ```start``` 버튼을 못 찾는 테스터가 있어 ```start``` 버튼에 애니메이션을 추가하여 쉽게 찾을 수 있도록 설정
1. 중국어, 이탈리아어, 힌디어, 네덜란드어, 태국어, 독일어 추가
1. 앱 스토어 리뷰를 작성할 수 있도록 유도(사용한 라이브러리: [react-native-rate]({{site.url}}/react-native/react-native-rate/){:target="_blank"})
1. 태플릿 지원
1. 버그 수정

앱 다운로드 링크

<div class="download_link_container">
    <a class="download_link_ios" href="https://itunes.apple.com/app/blaboo/id1441741187" target="_blank">
        <img src="/assets/images/apple_download.png" alt="어린이 단어 학습 앱 blaboo iOS 다운로드"/>
    </a>
    <a class="download_link_android" href="https://play.google.com/store/apps/details?id=io.github.dev.yakuza.blaboo" target="_blank">
        <img src="/assets/images/google play_download.png" alt="어린이 단어 학습 앱 blaboo 안드로이드 다운로드"/>
    </a>
</div>

## 결론
사실 이 블로그를 쓴 가장 큰 이유는 여러분의 힘을 빌리고자 함에 있습니다. 위에서도 이야기했지만 영어, 일본어, 한국어 이외에 언어는 구글 번역기를 통해서 번역을 진행하고 있습니다. 웹이나 앱스토어에 내용은 조금 틀려도 크게 문제가 되지 않지만, BlaBoo 앱의 특성상 어린이 또는 외국어를 배우는 사람들을 대상으로 하기 때문에 앱내에 존재하는 단어는 틀리면 안된다고 생각합니다. 하지만 제가 전 세계 언어를 알고 있는 것도 아니고, 그렇다고 돈이 많아 전부 번역할 수 있는 상황이 아니여서 이렇게 염치불구하고 글을 쓰게 되었습니다.

아래는 BlaBoo 앱내에서 사용하고 있는 다국어 파일을 정리해서 공개한 저장소(Repository)입니다. 혹시 외국어가 특기이신 분들은 아래에 저장소(Repository)를 보시고 단어를 수정해 주십사 부탁드리고 싶습니다.

- github: [https://github.com/dev-yakuza/blaboo-translate](https://github.com/dev-yakuza/blaboo-translate){:target="_blank"})

여러분의 도움이 한 개발자에게 큰 희망이, 많은 사용자들에게는 제대로 된 단어 학습이 가능하도록 만들어 주지 않을까 싶네요.
