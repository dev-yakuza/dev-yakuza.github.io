---
layout: 'post'
permalink: '/react-native/react-native-rate/'
paginate_path: '/react-native/:num/react-native-rate/'
lang: 'ko'
categories: 'react-native'
comments: true

title: '앱 스토어 리뷰'
description: 'RN(React Native) 프로젝트에서 react-native-rate를 사용하여 앱 스토어의 리뷰를 작성하도록 유도하는 방법에 대해서 설명합니다.'
image: '/assets/images/category/react-native/react-native-rate.jpg'
---


## 개요
RN(React Native)로 앱을 개발하고 배포하고 나니 앱 스토어의 리뷰를 작성해주시는 분들이 나오기 시작했습니다. 그 리뷰를 보니 개발한 보람도 느끼고, 유저가 필요한 기능에 대해 이해할 수 있게 되었습니다. 하지만 지금까지 특별히 앱 리뷰 작성을 유도하지 않고 있기 때문에 앱 리뷰 작성을 유도하면 더 많은 유저의 의견을 들을 수 있지 않을까라는 생각이 들어 이번 블로그를 준비하였습니다.

이 블로그에서는 ```react-native-rate``` 라이브러리를 사용하여 RN(React Native)로 작성한 앱에서 앱 스토어 리뷰 작성을 유도하는 방법에 대해서 설명합니다.

- react-native-rate 공식 사이트: [https://github.com/KjellConnelly/react-native-rate](https://github.com/KjellConnelly/react-native-rate){:rel="nofollow noreferrer" target="_blank"}

## 설치
RN(React Native)에서 ```react-native-rate``` 라이브러리를 사용하기 위해 아래에 명령어로 ```react-native-rate``` 라이브러리를 설치합니다.

```bash
npm install react-native-rate --save
```

## 라이브러릴 연결
라이브러리 설치가 완료되었다면, 아래에 명령어로 ```react-native-rate``` 라이브러리를 RN(React Native) 프로젝트와 연결합니다.

```bash
react-native link react-native-rate
```

## 사용 방법
아래에 소스코드는 [react-native-rate 공식 사이트](https://github.com/KjellConnelly/react-native-rate){:rel="nofollow noreferrer" target="_blank"}의 일부를 발췌한 내용입니다.

```js
import Rate, { AndroidMarket } from 'react-native-rate'
...
render() {
    return (
            <Button title="Rate App" onPress={()=>{
                let options = {
                    AppleAppID:"2193813192",
                    GooglePackageName:"com.mywebsite.myapp",
                    AmazonPackageName:"com.mywebsite.myapp",
                    OtherAndroidURL:"http://www.randomappstore.com/app/47172391",
                    preferredAndroidMarket: AndroidMarket.Google,
                    preferInApp:false,
                    openAppStoreIfInAppFails:true,
                    fallbackPlatformURL:"http://www.mywebsite.com/myapp.html",
                }
                Rate.rate(options, success=>{
                    if (success) {
                        // this technically only tells us if the user successfully went to the Review Page. Whether they actually did anything, we do not know.
                        this.setState({rated:true})
                    }
                })
            } />
    )
}
```

이 소스에서 알수 있듯이 앱 리뷰 작성을 유도하고 싶을 때 여러 옵션들과 함께 ```Rate.rate()```를 실행하면 됩니다. 아래에 소스코드는 우리가 실제로 사용하는 소스코드의 일부입니다.

```js
import { Alert, AsyncStorage } from 'react-native';
import Rate, { AndroidMarket } from 'react-native-rate';
...
const isAlreadyRate = await AsyncStorage.getItem('isAlreadyRate');
const countStartApp = await AsyncStorage.getItem('countStartApp');
const count = countStartApp ? parseInt(countStartApp) : 1;
...
if (!isAlreadyRate && count % 3 === 0) {
  ...
  Alert.alert('App Rating', 'Please give us your opinion!', [
    {
      text: 'Later',
      onPress: () => console.log('Cancel Pressed'),
      style: 'cancel',
    },
    {
      text: 'OK',
      onPress: () => {
        setTimeout(() => {
          let options = {
            AppleAppID: '***************',
            GooglePackageName: '******************',
            preferredAndroidMarket: AndroidMarket.Google,
            preferInApp: false,
            openAppStoreIfInAppFails: true,
          };
          Rate.rate(options, success => {
            if (success) {
              AsyncStorage.setItem('isAlreadyRate', 'true');
            }
          });
        }, 500);
      },
    },
  ]);
}
await AsyncStorage.setItem('countStartApp', `${count + 1}`);
```

우리는 ```AsyncStorage```에 앱 리뷰를 수행했는지 여부를 저장하여 앱 리뷰를 수행한 유저는 다시는 앱 리뷰 유도창이 나오지 않게 처리하고 있습니다. 또한 앱의 실행 횟수가 3의 배수인 경우만 앱 리뷰 유도창을 띄우도록 하여 기존의 사용자 경험에 방해되지 않도록 하였습니다.

위에서 본 ```react-native-rate``` 공식 사이트 소스에는 많은 설정이 있지만 우리는 iOS의 앱 스토어와 안드로이드의 Google Play 스토어만 이용을 하기 때문에 ```AppleAppID```와 ```GooglePackageName``` 옵션만 사용하였습니다. AppleAppID는 앱 스토어 다운로드 링크 URL의 뒷 부분이나 Appstore Connect에서 ```앱 정보```에서 확인하실 수 있습니다.

## 완료
앱의 로드맵도 중요하지만, 역시 가장 중요한건 유저의 의견이 아닌가 싶습니다. 유저가 좀 더 쉽게 의견을 전달 할 수 있도록 안내하는 것도 앱 개발에서 중요하게 고려해야할 사항이 아닐까싶습니다. ```react-native-rate```를 사용해서 여러분도 유저가 좀더 쉽게 의견을 제시할 수 있도록 유도해 보시기 바랍니다

## 참고
- react-native-rate 공식 사이트: [https://github.com/KjellConnelly/react-native-rate](https://github.com/KjellConnelly/react-native-rate){:rel="nofollow noreferrer" target="_blank"}