---
layout: 'post'
permalink: '/react-native/react-native-admob/'
paginate_path: '/react-native/:num/react-native-admob/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'Google Admob'
description: 'use react-native-admob to add google admob advertisement to react-native.'
image: '/assets/images/category/react-native/react-native-admob.jpg'
---


## outline
google has the advertisement platforms those are Adsense([https://www.google.com/adsense/start/](https://www.google.com/adsense/start/){:rel="nofollow noreferrer" target="_blank"}) and Admob([https://www.google.com/admob/](https://www.google.com/admob/){:rel="nofollow noreferrer" target="_blank"}). in here we talk about how to display Google Admob advertisement to RN(react-native).

the difference between Google Adsense and Admob is that Adsense is for the website platform and Admob is for the smartphone application. we already used Adsense on this blog website. if you want to know how to use Google Adsense to the website, see another blog([google service]({{site.url}}/jekyll/google-service/)).

## install library
install [react-native-admob](https://github.com/sbugert/react-native-admob){:rel="nofollow noreferrer" target="_blank" } library for using Google Admob at RN(react native).

```bash
npm install react-native-admob@next --save
```

when installation is completed, link react-native-admob library to RN(react native) project by executing below code.

```bash
react-native link react-native-admob
```

### install SDK for iOS
to use Google Admob on iOS, we need to install ```Google Mobile Ads SDK```. click below link to see how to install ```Google Mobile Ads SDK```.

- Google Mobile Ads SDK: [https://developers.google.com/admob/ios/quick-start](https://developers.google.com/admob/ios/quick-start#import_the_mobile_ads_sdk){:rel="nofollow noreferrer" target="_blank" }

we introduce how to install ```Google Mobile Ads SDK``` by downloading the file.

- donwload link: [https://developers.google.com/admob/ios/download](https://developers.google.com/admob/ios/download){:rel="nofollow noreferrer" target="_blank" }

click above link to go to the download site and download ```Google Mobile Ads SDK``` file. after downloading, unzip the file.

go to iOS folder in RN(react-native) project folder and execute ```[projectname].xcodeproj``` file.

![add Google Mobile Ads SDK to ios ](/assets/images/category/react-native/react-native-admob/add_sdk.png)

after executing xcode, right click project name on the left of the top and ```Add Files to [project name]```. go to the folder which you unzip ```Google Mobile Ads SDK```, and select ```GoogleMobileAds.framework``` file. click ```Copy items if needed``` and ```add``` button for adding ```Google Mobile Ads SDK```.

## signup Googld Admob
go to Google Admob site for signup. it's same process to signup and signin to normal service.

- Google Admob site: [https://www.google.com/admob/](https://www.google.com/admob/){:rel="nofollow noreferrer" target="_blank" }

## Google Admob Configuration
let's check about how to use Google Admob. after signup and signin to Google Admob, you can see below screen.

![signin google admob](/assets/images/category/react-native/react-native-admob/signin_google_admob.png)

click ```GET STARTED``` button for starting Google Admob.

![configure admob](/assets/images/category/react-native/react-native-admob/configure_admob.png)


choose wether the app is already registered in Market or not. we did not register the app to Market, so select ```NO```.

![configure app name on admob](/assets/images/category/react-native/react-native-admob/configure_app_name.png)

create the app name and choose the platform of the app for using Google Admob. we selected ```iOS``` in here.

![completed to configure](/assets/images/category/react-native/react-native-admob/completed_configure.png)

completed to register Google Admob. there are details about next step.
구글 애드몹(Google admob) 등록이 완료되었습니다. 친절하게 하단에 다음 단계에 대한 설명이 잘 나와있습니다.

1. copy ```App ID``` for setting react-native-admob
1. we need to configure Ad Unit in Google Admob.
1. after releasing the app to Market, we need to link it in Google Admob.

click ```NEXT: CREATE AD UNIT``` on the bottom of the page to go to the configuration.

![select advertisement type](/assets/images/category/react-native/react-native-admob/select_ad_uni.png)

we use Banner advertisement first. click ```SELECT``` button on the bottom of the ```Banner``` section.

![input banner name](/assets/images/category/react-native/react-native-admob/set_banner_name.png)

set the banner name. this banner name just helps you find and recognize this banner on Google Admob. after inserting, click ```CREATE AD UNIT``` button.

![finished configuration](/assets/images/category/react-native/react-native-admob/finished_configuration.png)

completed to set Google Admob banner. copy App ID and ad unit ID.

## react-native-admob
let's see how to use react-native-admob for using Google Admob banner to RN(react native)

### iOS configuration.
we need to edit ```ios/[project name]/AppDelegate.m``` for using Google Admob on iOS.

```
#import <React/RCTRootView.h>

@import GoogleMobileAds;
```

import ```Google Mobile Ads SDK``` we downloaded before.

```
self.window.rootViewController = rootViewController;

[GADMobileAds configureWithApplicationID:@"ca-app-pub-7987914246691031~8295071692"];

[self.window makeKeyAndVisible];
```

paste Google Admob App ID to ```[GADMobileAds configureWithApplicationID:@"Google-Admob-App-Id"];``` and insert this code on above position.

now we ready to use Google Admob on iOS.

### react-native-admob usage
import ```AdmobBanner``` from ```react-native-admob``` library on the file you want to display Google Admob banner.

```js
import { AdMobBanner } from 'react-native-admob';
```

copy-paste below code to the position where you want to display Google Admob banner.

```js
<AdMobBanner
    adSize="fullBanner"
    adUnitID="ad unit ID"
    testDevices={[AdMobBanner.simulatorId]}
    onAdFailedToLoad={error => console.log(error)}
/>
```

- adSize: this is the banner size. details about the banner size, see the official site.([react-native-admob banner size](https://github.com/sbugert/react-native-admob#admobbanner){:rel="nofollow noreferrer" target="_blank"})
- adUnitID: copy-paste Ad Unit ID that we created in Google Admob service.
- testDevices: test device ID list. we set the simulator ID.
- onAdFailedToLoad: if the advertisement loading is failed, this is executed.

completed to set. execute RN(react native) and check the banner displayed well.

## Android
introduce about how to apply on Android, when we develop Android application.

