---
layout: 'post'
permalink: '/react-native/react-native-voice/'
paginate_path: '/react-native/:num/react-native-voice/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'ユーザ音声認識'
description: 'リアクトネイティブ(React Native)プロジェクトでreact-native-voiceライブラリを使ってユーザの音声を認識して文字で変換する機能を追加してみます。'
image: '/assets/images/category/react-native/react-native-voice.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [インストール](#インストール)
- [権限設定](#権限設定)
  - [iOS](#ios)
  - [アンドロイド(未確認)](#アンドロイド未確認)
- [使い方](#使い方)
- [提供言語選定](#提供言語選定)
- [参考](#参考)

</div>

## 概要

リアクトネイティブ(React Native)プロジェクトでユーザ音声を認識して文字に変換する機能(STT, Speech To Text)が必要な時`react-native-voice`ライブラリを使うことをお勧めします。このブログでは`react-native-voice`を使ってユーザの音声を文字で変換する機能(STT, Speech To Text)を追加する方法について説明します。

- react-native-voice公式サイト: [https://github.com/wenkesj/react-native-voice](https://github.com/wenkesj/react-native-voice){:rel="nofollow noreferrer" target="_blank"}

## インストール

ユーザ音声を認識して文字に変換する機能であるSTT(Speech To Text)を使うため下のコマンドで`react-native-voice`ライブラリをリアクトネイティブ(React Native)プロジェクトへインストールします。

```bash
npm install --save react-native-voice
```

インストールが終わったら下のコマンドで`react-native-voice`をリアクトネイティブ(React Native)プロジェクトと連結します。

```bash
npx pod-install
```

{% include in-feed-ads.html %}

## 権限設定

ユーザ音声を認識して文字に変換する機能であるSTT(Speech To Text)を使うためそれそれのOSに合う権限設定が必要です。

### iOS

iOSで権限を設定するため下記の内容をリアクトネイティブ(React Native)プロジェクトフォルダの`ios/app_name/Info.plist`に追加します。

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

### アンドロイド(未確認)

アンドロイド(Android)で権限を設定するため下記の内容をリアクトネイティブ(React Native)プロジェクトのフォルダの`android/app/src/AndroidManifest.xml`に追加します。(参考: アンドロイドで権限の問題があるかどうかはまだ確認してないです。)

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

## 使い方

ここで説明するリアクトネイティブ(React Native)のコードは基本的`typescript`と`styled-components`が適応されています。リアクトネイティブ(React Native)にtypescriptとstyled-componentsを適応する方法については以前のブログを参考してください。

- [typescript]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}
- [styled-components]({{site.url}}/{{page.categories}}/styled-components/){:target="_blank"}

下記の内容はユーザ音声を認識して文字で変換する機能であるSTT(Speech To Text)を使うため`react-native-voice`を使う方法です。

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

上のソースを詳しく見てみます。

```js
Voice.onSpeechStart = _onSpeechStart;
Voice.onSpeechEnd = _onSpeechEnd;
Voice.onSpeechResults = _onSpeechResults;
Voice.onSpeechError = _onSpeechError;
```

useEffectでreact-native-voiceに使うイベント関数を連結します。

```js
// componentWillUnmount
useEffect(() => {
  ...
  return () => {
    Voice.destroy().then(Voice.removeAllListeners);
  };
}, []);
```

react-native-voiceを使ってるコンポーネント(Component)が除去(Unmount)される時react-native-voiceライブラリも除去します。

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

特定イベントでユーザ音声を認識したり、中止したりします。

```js
const _onSpeechResults = (event) => {
  console.log('onSpeechResults');
  setText(event.value[0]);
};
```

react-native-voiceが`Voice.start('en-US');`で起動したら、マイクを通じて認識されたユーザの音声が`Voice.onSpeechResults = _onSpeechResults;`を通じで継続的に更新されます。

全てのソースコードは下記のレポジトリ(Repository)で確認できます。

- react native voice exerciseレポジトリ(Repository): [https://github.com/dev-yakuza/react_native_voice_exercise](https://github.com/dev-yakuza/react_native_voice_exercise){:rel="nofollow noreferrer" target="_blank"}

{% include in-feed-ads.html %}

## 提供言語選定

ユーザ音声を認識して文字に変換する機能であるSTT(Speech To Text)を使うためにはユーザの音声がどんな言語か設定する必要があります。

```js
Voice.start('ja-JP');
```

下記のリストは言語を設定するための言語-国家コードです。

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

## 参考

- react-native-voice公式サイト: [https://github.com/wenkesj/react-native-voice](https://github.com/wenkesj/react-native-voice){:rel="nofollow noreferrer" target="_blank"}
