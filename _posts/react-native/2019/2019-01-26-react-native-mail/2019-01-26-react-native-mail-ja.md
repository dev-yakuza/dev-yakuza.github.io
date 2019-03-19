---
layout: 'post'
permalink: '/react-native/react-native-mail/'
paginate_path: '/react-native/:num/react-native-mail/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'メール送信機能'
description: 'RN(React Native)プロジェクトでreact-native-mailライブラリを使って端末にインストールされてあるメールアプリを起動してメールを送信してみましょう。'
image: '/assets/images/category/react-native/react-native-mail.jpg'
---


## 概要
RN(React Native)でメール発信するため端末にインストールされてある基本メールアプリを起動するライブラリを紹介します。このブログでは```react-native-mail```ライブラリを使ってメールアプリを実行してメールを発信する方法について紹介します。

- react-native-mail 公式サイト: [https://github.com/chirag04/react-native-mail](https://github.com/chirag04/react-native-mail){:rel="nofollow noreferrer" target="_blank"}

## インストール
RN(React Native)でメールアプリを起動してメールを発信するため下記のコマンドで```react-native-mail```ライブラリをインストールします。

```bash
npm install --save react-native-mail
```

インストールが終わったら下記のコマンドで```react-native-mail```をRN(React Native)プロジェクトと連結します。

```bash
react-native link react-native-mail
```

## 使い方
下記に紹介する方法は[公式サイト](https://github.com/chirag04/react-native-mail){:rel="nofollow noreferrer" target="_blank"}にある内容をそのままコピした内容になります。

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

- subject: メールのタイトル
- recipients: メールを受信するメールリスト
- ccRecipients: ccで受信するメールリスト
- bccRecipients: bccで受信するメールリスト
- body: メールの本文
- isHTML: メールの本文がHTML形式かどうか
- attachment: 添付ファイルがある場合使う
  - path: ファイルの位置
  - type: ファイルのmime type
  - name(Optional): カスタムファイル名

下は添付ファイルの例題です。ファイルの位置は```react-native-fs```を使ってファイルの位置を取得しました。

```js
attachment: {
  path: `${RNFS.DocumentDirectoryPath}/${file.name}`,
  type: 'xls',
  name: file.name,
},
```

添付が可能なファイルのmime typeは下記になります。

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

メールアプリが起動された後、またアプリに戻る時実行されるコールバック関数(Callback function)を上で説明したオプションと一緒に```Mailer.mail```関数に伝達します。

メールアプリが実行中発生したエラーやメールアプリで発生したイベントがパラメータ(Parameter)で伝達されて実行されます。

パラメータ(Parameter)で伝達される```event```は下記のようです。

```js
sent
saved
cancelled
failed
error
```

エラーが発生したら```error```パラメータ(Parameter)にエラー内容が伝達されます。下記のコードは私たちが実際使ってるコードの一部です。

```js
(error, event) => {
  if (error) {
    // エラーの処理
    ...
  } else if (event === 'sent') {
    // メール送信成功の処理
    ...
  }
}
```

## 完了
上で実装した```react-native-mail```機能を実行したら下のような画面が見えます。(写真の出所: [公式サイト](https://github.com/chirag04/react-native-mail){:rel="nofollow noreferrer" target="_blank"})

![react-native-mailスクリンショット](/assets/images/category/react-native/react-native-mail/screenshot.png)

## 参考
- react-native-mail公式サイト: [https://github.com/chirag04/react-native-mail](https://github.com/chirag04/react-native-mail){:rel="nofollow noreferrer" target="_blank"}