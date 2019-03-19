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


## Outline
if you need to recognize user voice and transform to text(STT, Speech To Text), you can use ```react-native-voice```. in this blog, we will see how to add the feature to recognize user voice and transform to text by using ```react-native-voice```.

- react-native-voice official site: [https://github.com/wenkesj/react-native-voice](https://github.com/wenkesj/react-native-voice){:rel="nofollow noreferrer" target="_blank"}

## Installation
install ```react-native-voice``` library by executing below command for STT(Speech To Text) feature which recognize user voice and transform to text.

```bash
npm install --save react-native-voice
```

after installing, execute below command to link ```react-native-voice``` to RN(React Native) project.

```bash
react-native link react-native-voice
```

## Configure Permission
we need to configure the permission to use STT(Speech To Text) feature which recognize user voice and transform to text.

### iOS
add below code to ```ios/app_name/Info.plist``` file in RN(React Native) project folder to set the permission on iOS.

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
add below contnet to ```android/app/src/AndroidManifest.xml``` file in RN(React Native) project folder to set the permission on Android. (Warning: I didn't check this is OK on Android for the permission yet.)

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

## How to use
in here, I will use RN(React Native) code basically applied ```typescript``` and ```styled-components```. if you want to know how to apply ```typescript``` and ```styled-components``` to RN(React Native), see my previous blogs.

- [typescript]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}
- [styled-components]({{site.url}}/{{page.categories}}/styled-components/){:target="_blank"}

below is how to use ```react-native-voice``` about STT(Speech To Text) feature which recognize user voice and transform to text.

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

let's see above source deeply.

```js
Voice.onSpeechStart = this._onSpeechStart;
Voice.onSpeechEnd = this._onSpeechEnd;
Voice.onSpeechResults = this._onSpeechResults;
Voice.onSpeechError = this._onSpeechError;
```

connect react-native-voice event functions in constructor.

```js
componentWillUnmount() {
  Voice.destroy().then(Voice.removeAllListeners);
}
```

when the component which use react-native-voice is unmounted, make react-native-voice also removed.

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

you should bind a specific event to recognize or stop the user voice.

```js
...
private _onSpeechResults = event => {
  console.log('onSpeechResults');
  this.setState({
    voice: event.value[0],
  });
};
```

if react-native-voice is executed by ```Voice.start('en-US');```, user voice which is recognized by the mic is continuously changed through ```Voice.onSpeechResults = this._onSpeechResults;```.

you can see full source code via below link.

- react native voice exercise reepository: [https://github.com/dev-yakuza/react_native_voice_exercise](https://github.com/dev-yakuza/react_native_voice_exercise){:rel="nofollow noreferrer" target="_blank"}

## Configure Language
if you want to use STT(Speech To Text) feature which recognize user voice and transform text, you should set what user use language.

```js
Voice.start('ja-JP');
```

below list is language-country code to configure the language.

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


## Reference
- react-native-voice official site: [https://github.com/wenkesj/react-native-voice](https://github.com/wenkesj/react-native-voice){:rel="nofollow noreferrer" target="_blank"}