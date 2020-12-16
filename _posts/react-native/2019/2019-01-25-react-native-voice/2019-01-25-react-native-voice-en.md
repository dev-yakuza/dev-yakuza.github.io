---
layout: 'post'
permalink: '/react-native/react-native-voice/'
paginate_path: '/react-native/:num/react-native-voice/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'recognize user voice'
description: let's see how to add the feature to recognize user voice and transform to text by react-native-voice on RN(React Native)
image: '/assets/images/category/react-native/react-native-voice.jpg'
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [Installation](#installation)
- [Configure Permission](#configure-permission)
  - [iOS](#ios)
  - [Android(Unidentified)](#androidunidentified)
- [How to use](#how-to-use)
- [Configure Language](#configure-language)
- [Reference](#reference)

</div>

## Outline

if you need to recognize the user voice and transform to text(STT, Speech To Text), you can use `react-native-voice`. in this blog, we will see how to add the feature to recognize the user voice and transform to text by using `react-native-voice`.

- react-native-voice official site: [https://github.com/wenkesj/react-native-voice](https://github.com/wenkesj/react-native-voice){:rel="nofollow noreferrer" target="_blank"}

## Installation

install `react-native-voice` library by executing below command for STT(Speech To Text) feature which recognize user voice and transform to text.

```bash
npm install --save react-native-voice
```

after installing, execute below command to link `react-native-voice` to RN(React Native) project.

```bash
npx pod-install
```

{% include in-feed-ads.html %}

## Configure Permission

we need to configure the permission to use STT(Speech To Text) feature which recognize user voice and transform to text.

### iOS

add below code to `ios/app_name/Info.plist` file in RN(React Native) project folder to set the permission on iOS.

```xml
<dict>
    ...
    <key>NSMicrophoneUsageDescription</key>
    <string>Description of why you require the use of the microphone</string>
    <key>NSSpeechRecognitionUsageDescription</key>
    <string>Description of why you require the use of the speech recognition</string>
    ...
</dict>
```

### Android(Unidentified)

add contents below to `android/app/src/AndroidManifest.xml` file in RN(React Native) project folder to set the permission on Android. (Warning: I didn't check this is OK on Android for the permission yet.)

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="package_name">
    ...
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.SYSTEM_ALERT_WINDOW"/>
    <uses-permission android:name="android.permission.RECORD_AUDIO" />
    ...
</manifest>
```

{% include in-feed-ads.html %}

## How to use

in here, I will use RN(React Native) code basically applied `typescript` and `styled-components`. if you want to know how to apply `typescript` and `styled-components` to RN(React Native), see my previous blogs.

- [typescript]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}
- [styled-components]({{site.url}}/{{page.categories}}/styled-components/){:target="_blank"}

below is how to use `react-native-voice` about STT(Speech To Text) feature which recognize user voice and transform to text.

```js
import React, {useState, useEffect} from 'react';
import Styled from 'styled-components/native';
import Voice from 'react-native-voice';

const Container = Styled.View`
  flex: 1;
  justify-content: center;
  align-items: center;
  background-color: #f5fcff;
`;
const ButtonRecord = Styled.Button``;
const VoiceText = Styled.Text`
  margin: 32px;
`;

const App = () => {
  const [isRecord, setIsRecord] = useState<boolean>(false);
  const [text, setText] = useState<string>('');
  const buttonLabel = isRecord ? 'Stop' : 'Start';
  const voiceLabel = text
    ? text
    : isRecord
    ? 'Say something...'
    : 'press Start button';

  const _onSpeechStart = () => {
    console.log('onSpeechStart');
    setText('');
  };
  const _onSpeechEnd = () => {
    console.log('onSpeechEnd');
  };
  const _onSpeechResults = (event) => {
    console.log('onSpeechResults');
    setText(event.value[0]);
  };
  const _onSpeechError = (event) => {
    console.log('_onSpeechError');
    console.log(event.error);
  };

  const _onRecordVoice = () => {
    if (isRecord) {
      Voice.stop();
    } else {
      Voice.start('en-US');
    }
    setIsRecord(!isRecord);
  };

  useEffect(() => {
    Voice.onSpeechStart = _onSpeechStart;
    Voice.onSpeechEnd = _onSpeechEnd;
    Voice.onSpeechResults = _onSpeechResults;
    Voice.onSpeechError = _onSpeechError;

    return () => {
      Voice.destroy().then(Voice.removeAllListeners);
    };
  }, []);
  return (
    <Container>
      <VoiceText>{voiceLabel}</VoiceText>
      <ButtonRecord onPress={_onRecordVoice} title={buttonLabel} />
    </Container>
  );
};

export default App;
```

let's see the source above deeply.

```js
Voice.onSpeechStart = _onSpeechStart;
Voice.onSpeechEnd = _onSpeechEnd;
Voice.onSpeechResults = _onSpeechResults;
Voice.onSpeechError = _onSpeechError;
```

connect react-native-voice event functions in the useEffect.

```js
// componentWillUnmount
useEffect(() => {
  ...
  return () => {
    Voice.destroy().then(Voice.removeAllListeners);
  };
}, []);
```

when the component which use react-native-voice is unmounted, make react-native-voice also removed.

```js
const _onRecordVoice = () => {
  if (isRecord) {
    Voice.stop();
  } else {
    Voice.start('en-US');
  }
  setIsRecord(!isRecord);
};
```

you should bind a specific event to recognize or stop the user voice.

```js
const _onSpeechResults = (event) => {
  console.log('onSpeechResults');
  setText(event.value[0]);
};
```

if react-native-voice is executed by `Voice.start('en-US');`, user voice which is recognized by the mic is continuously changed through `Voice.onSpeechResults = _onSpeechResults;`.

you can see full source code via the link below.

- react native voice exercise reepository: [https://github.com/dev-yakuza/react_native_voice_exercise](https://github.com/dev-yakuza/react_native_voice_exercise){:rel="nofollow noreferrer" target="_blank"}

{% include in-feed-ads.html %}

## Configure Language

if you want to use STT(Speech To Text) feature which recognize the user voice and transform text, you should set what user use language.

```js
Voice.start('ja-JP');
```

The list blow is the language-country code to configure the language.

```bash
ar-SA
cs-CZ
da-DK
de-DE
el-GR
en-AU
en-GB
en-IE
en-US
en-ZA
es-ES
es-MX
fi-FI
fr-CA
fr-FR
he-IL
hi-IN
hu-HU
id-ID
it-IT
ja-JP
ko-KR
nl-BE
nl-NL
no-NO
pl-PL
pt-BR
pt-PT
ro-RO
ru-RU
sk-SK
sv-SE
th-TH
tr-TR
zh-CN
zh-HK
zh-TW
```

{% include in-feed-ads.html %}

## Reference

- react-native-voice official site: [https://github.com/wenkesj/react-native-voice](https://github.com/wenkesj/react-native-voice){:rel="nofollow noreferrer" target="_blank"}
