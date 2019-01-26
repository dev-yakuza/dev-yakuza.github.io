---
layout: 'post'
permalink: '/react-native/react-native-mail/'
paginate_path: '/react-native/:num/react-native-mail/'
lang: 'ko'
categories: 'react-native'
comments: true

title: '이메일 발송 기능'
description: 'RN(React Native) 프로젝트에서 react-native-mail 라이브러리를 사용하여 단말기에 설치되어 있는 이메일 앱을 실행하고 이메일(email)을 보내봅시다.'
image: '/assets/images/category/react-native/react-native-mail.jpg'
---


## 개요
RN(React Native)에서 이메일을 발송하기 위해 단말기에 설치되어 있는 기본 이메일 앱을 기동하는 라이브러리를 소개하겠습니다. 이 블로그에서는 ```react-native-mail``` 라이브러리를 사용하여 이메일 앱을 실행하고 이메일을 발송하는 방법에 대해서 소개하겠습니다.

- react-native-mail 공식 사이트: [https://github.com/chirag04/react-native-mail](https://github.com/chirag04/react-native-mail){:rel="nofollow noreferrer" target="_blank"}

## 설치
RN(React Native)에서 이메일을 앱을 기동하고 이메일을 발송하기 위해 아래에 명령어로 ```react-native-mail``` 라이브러리를 설치합니다.

```bash
npm install --save react-native-mail
```

설치가 완료되면 아래에 명령어로 ```react-native-mail```를 RN(React Native) 프로젝트와 연결합니다.

```bash
react-native link react-native-mail
```

## 사용 방법
아래에 소개하는 방법은 [공식 사이트](https://github.com/chirag04/react-native-mail){:rel="nofollow noreferrer" target="_blank"}에 내용을 그대로 복사한 내용입니다.

```js
/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 * @flow
 */

import React, { Component } from 'react';
import { View, Alert, Button } from 'react-native';
import Mailer from 'react-native-mail';

export default class App extends Component {

  handleEmail = () => {
    Mailer.mail({
      subject: 'need help',
      recipients: ['support@example.com'],
      ccRecipients: ['supportCC@example.com'],
      bccRecipients: ['supportBCC@example.com'],
      body: '<b>A Bold Body</b>',
      isHTML: true,
      attachment: {
        path: '',  // The absolute path of the file from which to read data.
        type: '',   // Mime Type: jpg, png, doc, ppt, html, pdf, csv
        name: '',   // Optional: Custom filename for attachment
      }
    }, (error, event) => {
      Alert.alert(
        error,
        event,
        [
          {text: 'Ok', onPress: () => console.log('OK: Email Error Response')},
          {text: 'Cancel', onPress: () => console.log('CANCEL: Email Error Response')}
        ],
        { cancelable: true }
      )
    });
  }

  render() {
    return (
      <View style={styles.container}>
        <Button
          onPress={this.handleEmail}
          title="Email Me"
          color="#841584"
          accessabilityLabel="Purple Email Me Button"
        />
      </View>
    );
  }
}
```

- subject: 이메일의 제목
- recipients: 이메일을 수신하는 이메일의 리스트
- ccRecipients: cc로 수신하는 이메일의 리스트
- bccRecipients: bcc로 수신하는 이메일의 리스트
- body: 이메일의 본문
- isHTML: 이메일의 본문이 HTML 형식인지 여부
- attachment: 첨부 파일이 있는 경우 사용
  - path: 파일의 위치
  - type: 파일의 mime type
  - name(Optional): 사용자 정의 파일 이름

아래는 첨부 파일의 예제입니다. 파일 위치는 ```react-native-fs```를 사용하여 파일의 위치를 가져왔습니다.

```js
attachment: {
  path: `${RNFS.DocumentDirectoryPath}/${file.name}`,
  type: 'xls',
  name: file.name,
},
```

첨부가 가능한 파일의 mime type은 아래와 같습니다.

```
jpg
png
doc
docx
ppt
pptx
html
csv
pdf
vcard
json
zip
text
mp3
wav
aiff
flac
ogg
xls
xlsx
```

```js
Mailer.mail(options, (error, event) => {})
```

이메일 앱을 실행한 후, 다시 앱으로 돌아올 때 실행되는 콜백 함수(Callback function)를 위에서 설명한 옵션과 함께 ```Mailer.mail``` 함수에 전달합니다.

이메일 앱을 실행하던 중 발생한 에러나, 이메일 앱에서 발생한 이벤트가 파라메터(Parameter)에 전달되어 실행됩니다.

파라메터(Parameter)로 전달 받는 ```event```는 아래와 같습니다.

```js
sent
saved
cancelled
failed
error
```

에러가 발생하면  ```error``` 파라메터(Parameter)에 에러 내용을 전달합니다. 아래의 코드는 우리가 실제 사용하는 코드의 일부분입니다.

```js
(error, event) => {
  if (error) {
    // 에러처리
    ...
  } else if (event === 'sent') {
    // 이메일 발송 성공 처리
    ...
  }
}
```

## 완료
위에서 구현한 ```react-native-mail``` 기능을 실행하면 아래와 같은 화면을 볼수 있습니다.(사진 출처: [공식 사이트](https://github.com/chirag04/react-native-mail){:rel="nofollow noreferrer" target="_blank"})

![react-native-mail 스크린샷](/assets/images/category/react-native/react-native-mail/screenshot.png)

## 참고
- react-native-mail 공식 사이트: [https://github.com/chirag04/react-native-mail](https://github.com/chirag04/react-native-mail){:rel="nofollow noreferrer" target="_blank"}