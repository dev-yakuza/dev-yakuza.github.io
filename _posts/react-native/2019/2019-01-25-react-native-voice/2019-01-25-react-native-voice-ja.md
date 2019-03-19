---
layout: 'post'
permalink: '/react-native/react-native-voice/'
paginate_path: '/react-native/:num/react-native-voice/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'ユーザ音声認識'
description: 'RN(React Native)プロジェクトでreact-native-voiceライブラリを使ってユーザの音声を認識して文字で変換する機能を追加してみます。'
image: '/assets/images/category/react-native/react-native-voice.jpg'
---


## 概要
RN(React Native)プロジェクトでユーザ音声を認識して文字に変換する機能(STT, Speech To Text)が必要な時```react-native-voice```ライブラリを使うことをお勧めします。このブログでは```react-native-voice```を使ってユーザの音声を文字で変換する機能(STT, Speech To Text)を追加する方法について説明します。

- react-native-voice公式サイト: [https://github.com/wenkesj/react-native-voice](https://github.com/wenkesj/react-native-voice){:rel="nofollow noreferrer" target="_blank"}

## インストール
ユーザ音声を認識して文字に変換する機能であるSTT(Speech To Text)を使うため下のコマンドで```react-native-voice```ライブラリをRN(React Native)プロジェクトへインストールします。

```bash
npm install --save react-native-voice
```

インストールが終わったら下のコマンドで```react-native-voice```をRN(React Native)プロジェクトと連結します。

```bash
react-native link react-native-voice
```

## 権限設定
ユーザ音声を認識して文字に変換する機能であるSTT(Speech To Text)を使うためそれそれのOSに合う権限設定が必要です。

### iOS
iOSで権限を設定するため下記の内容をRN(React Native)プロジェクトフォルダの```ios/app_name/Info.plist```に追加します。

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
アンドロイド(Android)で権限を設定するため下記の内容をRN(React Native)プロジェクトのフォルダの```android/app/src/AndroidManifest.xml```に追加します。(参考: アンドロイドで権限の問題があるかどうかはまだ確認してないです。)

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

## 使い方
ここで説明するRN(React Native)のコードは基本的```typescript```と```styled-components```が適応されています。RN(React Native)にtypescriptとstyled-componentsを適応する方法については以前のブログを参考してください。

- [typescript]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}
- [styled-components]({{site.url}}/{{page.categories}}/styled-components/){:target="_blank"}

下記の内容はユーザ音声を認識して文字で変換する機能であるSTT(Speech To Text)を使うため```react-native-voice```を使う方法です。

```js
...
export default class App extends React.Component<Props, State> {
  constructor(props: Props) {
    super(props);
    ...
    Voice.onSpeechStart = this._onSpeechStart;
    Voice.onSpeechEnd = this._onSpeechEnd;
    Voice.onSpeechResults = this._onSpeechResults;
    Voice.onSpeechError = this._onSpeechError;
  }
  ...
  componentWillUnmount() {
    Voice.destroy().then(Voice.removeAllListeners);
  }
  ...
  private _onSpeechStart = event => {
    console.log('onSpeechStart');
    this.setState({
      voice: '',
    });
  };
  private _onSpeechEnd = event => {
    console.log('onSpeechEnd');
    ...
  };
  private _onSpeechResults = event => {
    console.log('onSpeechResults');
    this.setState({
      voice: event.value[0],
    });
  };
  private _onSpeechError = event => {
    console.log('_onSpeechError');
    ...
  };

  private _onRecordVoice = () => {
    const { isRecord } = this.state;
    if (isRecord) {
      Voice.stop();
    } else {
      Voice.start('en-US');
    }
    this.setState({
      isRecord: !isRecord,
    });
  };
  ...
}
```

上のソースを詳しく見てみます。

```js
Voice.onSpeechStart = this._onSpeechStart;
Voice.onSpeechEnd = this._onSpeechEnd;
Voice.onSpeechResults = this._onSpeechResults;
Voice.onSpeechError = this._onSpeechError;
```

constructorでreact-native-voiceに使うイベント関数を連結します。

```js
componentWillUnmount() {
  Voice.destroy().then(Voice.removeAllListeners);
}
```

react-native-voiceを使ってるコンポーネント(Component)が除去(Unmount)される時react-native-voiceライブラリも除去します。

```js
private _onRecordVoice = () => {
  const { isRecord } = this.state;
  if (isRecord) {
    Voice.stop();
  } else {
    Voice.start('en-US');
  }
  this.setState({
    isRecord: !isRecord,
  });
};
```

特定イベントでユーザ音声を認識したり、中止したりします。

```js
...
private _onSpeechResults = event => {
  console.log('onSpeechResults');
  this.setState({
    voice: event.value[0],
  });
};
```

react-native-voiceが```Voice.start('en-US');```で起動したら、マイクを通じて認識されたユーザの音声が```Voice.onSpeechResults = this._onSpeechResults;```を通じで継続的に更新されます。

全てのソースコードは下記のレポジトリ(Repository)で確認できます。

- react native voice exerciseレポジトリ(Repository): [https://github.com/dev-yakuza/react_native_voice_exercise](https://github.com/dev-yakuza/react_native_voice_exercise){:rel="nofollow noreferrer" target="_blank"}

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

## 参考
- react-native-voice公式サイト: [https://github.com/wenkesj/react-native-voice](https://github.com/wenkesj/react-native-voice){:rel="nofollow noreferrer" target="_blank"}