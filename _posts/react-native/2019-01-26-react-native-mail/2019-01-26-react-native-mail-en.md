---
layout: 'post'
permalink: '/react-native/react-native-mail/'
paginate_path: '/react-native/:num/react-native-mail/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'sending email feature'
description: let's see how to execute the email app installed basically on the phone at RN(React Native) project.
image: '/assets/images/category/react-native/react-native-mail.jpg'
---


## Outline
we will introduce how to execute the email app which installed basically on the phone to send the email. in this blog, we will talk about how to use ```react-native-mail``` library to execute the email app and send the email at RN(React Native) project.

- react-native-mail official site: [https://github.com/chirag04/react-native-mail](https://github.com/chirag04/react-native-mail){:rel="nofollow noreferrer" target="_blank"}

## Installation
execute below command to install ```react-native-mail``` library to execute the email app for sending the email.

```bash
npm install --save react-native-mail
```

after installing, execute below command to link ```react-native-mail``` to RN(React Native).

```bash
react-native link react-native-mail
```

## How to use
below source code is from [official site](https://github.com/chirag04/react-native-mail){:rel="nofollow noreferrer" target="_blank"}. we've copied it.

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

- subject: email title
- recipients: recipient email list. 수신하는 이메일의 리스트
- ccRecipients: cc recipient email list.
- bccRecipients: bcc recipient email list.
- body: the body of the email
- isHTML: whether the body of the email is in HTML format
- attachment: use this if attachment exists
  - path: file path
  - type: file mime type
  - name(Optional): custom file name

below is the attachment example. we've used ```react-native-fs``` to get the file path.

```js
attachment: {
  path: `${RNFS.DocumentDirectoryPath}/${file.name}`,
  type: 'xls',
  name: file.name,
},
```

below list is the mime type which can be attached.

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

when RN(React Native) app is executed after the email app was executed, Callback function which is configured with above options is called at ```Mailer.mail```.

errors which occurred and the event on the email app are passed to the parameters.

below list is ```event``` parameter examples.

```js
sent
saved
cancelled
failed
error
```

if error is occured, error is passed to ```error```parameter. below code is the part of our code which we used on the production.

```js
(error, event) => {
  if (error) {
    // error process
    ...
  } else if (event === 'sent') {
    // handling email sent success
    ...
  }
}
```

## Completed
you can see below screen when you execute ```react-native-mail``` feature.(image source: [official site](https://github.com/chirag04/react-native-mail){:rel="nofollow noreferrer" target="_blank"})

![react-native-mail screenshot](/assets/images/category/react-native/react-native-mail/screenshot.png)

## Reference
- react-native-mail official site: [https://github.com/chirag04/react-native-mail](https://github.com/chirag04/react-native-mail){:rel="nofollow noreferrer" target="_blank"}