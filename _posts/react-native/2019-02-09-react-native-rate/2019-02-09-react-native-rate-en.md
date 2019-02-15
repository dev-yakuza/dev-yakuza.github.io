---
layout: 'post'
permalink: '/react-native/react-native-rate/'
paginate_path: '/react-native/:num/react-native-rate/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'App Store Rating'
description: let's see how to induce users to give the rating by react-native-rate library on RN(React Native) project.
image: '/assets/images/category/react-native/react-native-rate.jpg'
---


## Outline
after developing and releasing RN(React Native) app, users started to give the rating of the app. when I saw reviews, I felt rewarding and could know what users want. however, I didn't implement especially inducing users to give the rating in the app, so I thought if I implement it, more I can hear more users opinions.

in this blog, we will talk about how to induce users to give reviews in the app store by using ```react-native-rate``` library.

- react-native-rate officail site: [https://github.com/KjellConnelly/react-native-rate](https://github.com/KjellConnelly/react-native-rate){:rel="nofollow noreferrer" target="_blank"}

## Installation
execute the command below to install ```react-native-rate``` library.

```bash
npm install react-native-rate --save
```

## Link Library
after installing the library, execute the command below to link ```react-native-rate``` library to RN(React Native) project.

```bash
react-native link react-native-rate
```

## How To Use
the source code below is the excerpt from [react-native-rate official site](https://github.com/KjellConnelly/react-native-rate){:rel="nofollow noreferrer" target="_blank"}

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

as you can see from the source above, when you want to induce users to write the reviews, you just execute ```Rate.rate()``` function with some options. the source code below is the part of our code that we actually use.

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

we use ```AsyncStorage``` to check that user already gave the rating of the app and if user already gave the rating, we didn't display the alert inducing user to give the review. also, we check the count of the user open the app and only if the count is multiples of 3, we made the dialog show up not to disturb previous user experience.

there are many options in ```react-native-rate``` official site source code above. we only use iOS App store and Google Play store, so we just use ```AppleAppID``` and ```GooglePackageName``` options. you can see AppleAppID at the end of the app download link URL or at ```App info``` in Appstore Connect.

## Completed
the roadmap of the app is important, but I think users opinions are most important. I think it's the important part of the development to make the entrance that users give their feedback easily. I hope this blog is helpful you to implement the entrance of users reviews by ```react-native-rate```.


## Reference
- react-native-rate Official site: [https://github.com/KjellConnelly/react-native-rate](https://github.com/KjellConnelly/react-native-rate){:rel="nofollow noreferrer" target="_blank"}