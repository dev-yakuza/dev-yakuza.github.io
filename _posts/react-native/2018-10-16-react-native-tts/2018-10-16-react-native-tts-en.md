---
layout: 'post'
permalink: '/react-native/react-native-tts/'
paginate_path: '/react-native/:num/react-native-tts/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'react-native-tts'
description: 'implement text-to-speech to use react-native-tts'
image: '/assets/images/category/react-native/react-native-tts.jpg'
---


## outline
use [react-native-tts](https://github.com/ak1394/react-native-tts){:rel="nofollow noreferrer" target="_blank" } library for implementing text-to-speech feature to RN project.

## react-native-tts library installaction
install react-native-tts library by below code.

{% include_relative common/installation.md %}

after installing, link react-native-tts library to RN project by below command.

{% include_relative common/link.md %}

## how to use
we only write a blog post if we have used libraries. so we will add contents to here when we use.

if you want to knwo how to use, see official site.
- official site: [react-native-tts](https://github.com/ak1394/react-native-tts){:rel="nofollow noreferrer" target="_blank" }

## text-to-speech.
implement text-to-speech feature by below code.

{% include_relative common/usage.md %}

- setDefaultLanguage: this is default language code. if you want to knwo language codes, see [Language codes](https://docs.fedoraproject.org/en-US/Fedora_Contributor_Documentation/1/html/Users_Guide/appe-Users_Guide-Language_codes.html){:rel="nofollow noreferrer" target="_blank" }
- speak: tts will speak this sentence.

## configure default voice
you can change default voice on react-native-tt. change default voice with below code.

```js
Tts.setDefaultVoice('com.apple.ttsbundle.Yuna-compact');
```

you can see all supported voices with below code.

```js
Tts.voices().then(voices => console.log(voices));
```

we checked all supported voices with above code.

### iOS supported voices
if you set country code by ```setDefaultLanguage``` function, react-native-tts automatically set that country voice. if you already use ```setDefaultLanguage``` function for setting the coutnry, it's better to skip this section.

you can change default voice by passing ```id``` of below list to ```setDefaultVoice``` parameter

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

## reference
- official site: [react-native-tts](https://github.com/ak1394/react-native-tts){:rel="nofollow noreferrer" target="_blank" }
- Language codes: [Language codes](https://docs.fedoraproject.org/en-US/Fedora_Contributor_Documentation/1/html/Users_Guide/appe-Users_Guide-Language_codes.html){:rel="nofollow noreferrer" target="_blank" }