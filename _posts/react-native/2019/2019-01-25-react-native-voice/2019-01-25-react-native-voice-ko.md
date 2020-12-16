---
layout: 'post'
permalink: '/react-native/react-native-voice/'
paginate_path: '/react-native/:num/react-native-voice/'
lang: 'ko'
categories: 'react-native'
comments: true

title: '사용자 음성 인식'
description: 'RN(React Native) 프로젝트에서 react-native-voice 라이브러리를 사용하여 사용자 음성을 인식하여 문자로 변환해주는 기능을 추가해 봅시다.'
image: '/assets/images/category/react-native/react-native-voice.jpg'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [설치](#설치)
- [권한 설정](#권한-설정)
  - [iOS](#ios)
  - [안드로이드(미확인)](#안드로이드미확인)
- [사용 방법](#사용-방법)
- [지원 언어 설정](#지원-언어-설정)
- [참고](#참고)

</div>

## 개요

RN(React Native) 프로젝트에서 사용자 음성을 인식하여 문자로 변경하는 기능(STT, Speech To Text)이 필요할 때 `react-native-voice` 라이브러리를 사용하는 것을 추천합니다. 이 블로그에서는 `react-native-voice`를 사용하여 사용자 음성을 인식하여 문자로 변경하는 기능(STT, Speech To Text)을 추가하는 방법에 대해서 알아보겠습니다.

- react-native-voice 공식 사이트: [https://github.com/wenkesj/react-native-voice](https://github.com/wenkesj/react-native-voice){:rel="nofollow noreferrer" target="_blank"}

## 설치

사용자 음성을 인식하여 문자로 변경하는 기능인 STT(Speech To Text)를 사용하기 위해 아래에 명령어로 `react-native-voice` 라이브러리를 RN(React Native) 프로젝트에 설치합니다

```bash
npm install --save react-native-voice
```

설치가 완료되면 아래에 명령어로 `react-native-voice`를 RN(React Native) 프로젝트와 연결합니다.

```bash
npx pod-install
```

{% include in-feed-ads.html %}

## 권한 설정

사용자 음성을 인식하여 문자로 변경하는 기능인 STT(Speech To Text)를 사용하기 위해서 각 OS에 맞는 권한 설정이 필요합니다.

### iOS

iOS에서 권한 설정을 하기 위해 아래에 내용을 RN(React Native) 프로젝트 폴더의 `ios/app_name/Info.plist`에 추가합니다.

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

### 안드로이드(미확인)

안드로이드(Android)에서 권한 설정을 하기 위해 아래에 내용을 RN(React Native) 프로젝트 폴더의 `android/app/src/AndroidManifest.xml`에 추가합니다. (참고: 안드로이드에서 권한 문제가 없는지 아직 확인하지 않았습니다.)

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

## 사용 방법

여기서 설명하는 RN(React Native) 코드는 기본적으로 `typescript`와 `styled-components`가 적용되어있습니다. RN(React Native)에 typescript와 styled-components를 적용하는 방법에 대해서는 이전 블로그를 참고하시기 바랍니다.

- [typescript]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}
- [styled-components]({{site.url}}/{{page.categories}}/styled-components/){:target="_blank"}

아래의 내용은 사용자 음성을 인식하여 문자로 변경하는 기능인 STT(Speech To Text)를 사용하기 위해 `react-native-voice`를 사용하는 방법입니다.

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

위에 소스를 자세히 보겠습니다.

```js
Voice.onSpeechStart = _onSpeechStart;
Voice.onSpeechEnd = _onSpeechEnd;
Voice.onSpeechResults = _onSpeechResults;
Voice.onSpeechError = _onSpeechError;
```

useEffect에서 react-native-voice에서 사용할 이벤트 함수를 연결합니다.

```js
// componentWillUnmount
useEffect(() => {
  ...
  return () => {
    Voice.destroy().then(Voice.removeAllListeners);
  };
}, []);
```

react-native-voice를 사용하는 컴포넌트(Component)가 제거(Unmount)될때 react-native-voice 라이브러리도 제거해 줍니다.

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

특정 이벤트에서 사용자 음성을 인식하거나 중지하도록 연결하였습니다.

```js
const _onSpeechResults = (event) => {
  console.log('onSpeechResults');
  setText(event.value[0]);
};
```

react-native-voice가 `Voice.start('en-US');`로 시작되었다면, 마이크를 통해 인식된 사용자의 음성이 `Voice.onSpeechResults = _onSpeechResults;`을 통해 계속적으로 갱신이 됩니다.

전체 소스코드는 아래에 링크에서 확인할 수 있습니다.

- react native voice exercise 저장소(Repository): [https://github.com/dev-yakuza/react_native_voice_exercise](https://github.com/dev-yakuza/react_native_voice_exercise){:rel="nofollow noreferrer" target="_blank"}

{% include in-feed-ads.html %}

## 지원 언어 설정

사용자 음성을 인식하여 문자로 변경하는 기능인 STT(Speech To Text)를 사용하기 위해서는 사용자의 음성이 어떤 언어인지 설정할 필요가 있습니다.

```js
Voice.start('ja-JP');
```

아래의 목록은 언어를 설정하기위한 언어-국가 코드입니다.

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

## 참고

- react-native-voice 공식 사이트: [https://github.com/wenkesj/react-native-voice](https://github.com/wenkesj/react-native-voice){:rel="nofollow noreferrer" target="_blank"}
