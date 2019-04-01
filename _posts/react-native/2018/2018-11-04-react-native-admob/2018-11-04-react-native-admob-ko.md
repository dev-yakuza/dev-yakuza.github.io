---
layout: 'post'
permalink: '/react-native/react-native-admob/'
paginate_path: '/react-native/:num/react-native-admob/'
lang: 'ko'
categories: 'react-native'
comments: true

title: '구글 애드몹'
description: '구글 애드몹(google admob) 광고를 사용하기 위해 react-native-admob 라이브러리를 사용해 보자.'
image: '/assets/images/category/react-native/react-native-admob.jpg'
---


## 개요
구글은 광고 플랫폼으로 애드센스(Adsense: [https://www.google.com/adsense/start/](https://www.google.com/adsense/start/){:rel="nofollow noreferrer" target="_blank"})와 애드몹(Admob: [https://www.google.com/admob/](https://www.google.com/admob/){:rel="nofollow noreferrer" target="_blank"})을 가지고 있습니다. 여기에서는 어플리케이션에 구글 애드몹(google admob)을 이용하여 광고를 노출시키는 방법에 대해서 알아보겠습니다.

구글의 애드센스(google adsense)와 애드몹(google admob)의 차이점은 애드센스는 웹사이트용 플랫폼이고 애드몹은 스마트폰 어플리케이션용이라는 점입니다. 우리는 블로그용 광고로 이미 애드센스(google adsense)를 사용하고 있으며 웹사이트에 애드센스(Adsense)를 사용하는 방법에 대해서는 [google service]({{site.url}}/jekyll/google-service/)에서 확인하시기 바랍니다.

## 안내
현재 저는 `react-native-admob`을 사용하지 않고 `react-native-firebase`로 구글 애드몹을 사용하고 있습니다. 따라서 이 블로그 포스트는 최신 정보를 포함하지 않고 있을 가능성이 있습니다. 이 블로그에서는 애드몹 등록 방법만 참고하고, 아래에 링크를 통해 `react-native-firebase`를 사용하시기를 권장합니다.

- [Firebase Admob]({{site.url}}/{{page.categories}}/react-native-firebase-admob/){:target="_blank"}

## 라이브러리 설치
구글 애드몹(google admob)을 RN(react native)에서 사용하기 위해 [react-native-admob](https://github.com/sbugert/react-native-admob){:rel="nofollow noreferrer" target="_blank" } 라이브러리를 설치합니다.

```bash
npm install react-native-admob@next --save
```

설치가 완료되면 아래에 명령어로 react-native-admob 라이브러리와 RN(react native) 프로젝트를 연결합니다.

```bash
react-native link react-native-admob
```

### iOS SDK 설치
구글 애드몹(Google admob)을 iOS에서 사용하기 위해서는 ```Google Mobile Ads SDK```을 설치해야합니다. 아래에 링크를 클릭하여 설치 방법을 확인합니다.

- Google Mobile Ads SDK: [https://developers.google.com/admob/ios/quick-start](https://developers.google.com/admob/ios/quick-start#import_the_mobile_ads_sdk){:rel="nofollow noreferrer" target="_blank" }

여기서는 파일 다운로드 방식으로 설명하겠습니다.

- 다운로드 링크: [https://developers.google.com/admob/ios/download](https://developers.google.com/admob/ios/download){:rel="nofollow noreferrer" target="_blank" }

위에 링크를 눌러 다운로드 사이트로 이동하여 ```Google Mobile Ads SDK```를 다운로드합니다. 다운로드가 완료되면 압축을 풀어줍니다.

RN(react native) 프로젝트 폴더에서 ios 폴더로 이동하여 ```프로젝트명.xcodeproj```파일을 실행합니다.

![add Google Mobile Ads SDK to ios ](/assets/images/category/react-native/react-native-admob/add_sdk.png)

xcode가 실행되면 왼쪽위에 프로젝트명을 우클릭하고 ```Add Files to [프로젝트명]```을 선택합니다. 위에서 다운로드하고 압축을 푼 ```Google Mobile Ads SDK``` 폴더로 이동하여 ```GoogleMobileAds.framework```파일을 선택합니다. 하단에 ```Copy items if needed```를 선택하고 ```add``` 버튼을 눌러 ```Google Mobile Ads SDK``` 라이브러리를 추가합니다.

## 구글 애드몹 가입
구글 애드몹(Google admob) 사이트로 이동하여 회원가입을 합니다. 일반적인 회원가입/로그인 절차임으로 설명을 생략합니다.

- 구글 애드몹(Google admob) 사이트: [https://www.google.com/admob/](https://www.google.com/admob/){:rel="nofollow noreferrer" target="_blank" }

## 구글 애드몹 설정
구글 애드몹(Google admob) 사용법에 대해서 알아봅니다. 구글 애드몹(Google admob)을 사용하기 위해 구글 애드몹(Google admob) 사이트에 회원가입을 하고 로그인을 하면 아래와 같은 화면을 볼 수 있습니다.

![signin google admob](/assets/images/category/react-native/react-native-admob/signin_google_admob.png)

하단에 있는 ```GET STARTED``` 버튼을 눌러 구글 애드몹(Google admob)에 사용을 시작합니다.

![configure admob](/assets/images/category/react-native/react-native-admob/configure_admob.png)

이미 앱이 마켓에 등록되어있는지 여부를 선택합니다. 우리는 아직 앱을 등록하지 않은 상태이므로 ```NO```를 선택합니다.

![configure app name on admob](/assets/images/category/react-native/react-native-admob/configure_app_name.png)

구글 애드몹(Google admob)을 사용하기 위해 앱 이름을 작성하고 사용할 플랫폼을 선택합니다. 우리는 우선 ```iOS```를 선택하여 진행하겠습니다.

![completed to configure](/assets/images/category/react-native/react-native-admob/completed_configure.png)

구글 애드몹(Google admob) 등록이 완료되었습니다. 친절하게 하단에 다음 단계에 대한 설명이 잘 나와있습니다.

1. react-native-admob을 설정할때 필요한 ```App ID```를 복사해둡니다.
1. 광고 타입(ad unit)을 구글 애드몹(Google admob)에서 설정합니다.
1. 앱을 앱스토어에 등록하면 구글 애드몹(Google admob)에서 연결해줘야합니다.

하단에 있는 ```NEXT: CREATE AD UNIT```을 눌러 광고 타입 설정화면으로 이동합니다.

![select advertisement type](/assets/images/category/react-native/react-native-admob/select_ad_uni.png)

우리는 일단 배너 광고 사용해 보겠습니다. ```Banner```의 하단에 ```SELECT```버튼을 선택합니다.

![input banner name](/assets/images/category/react-native/react-native-admob/set_banner_name.png)

해당 배너의 이름을 설정합니다. 구글 애드몹(Google admob) 서비스에서 해당 배너를 쉽게 찾기 위한 이름이므로 자신이 쉽게 인식할 수 있는 이름을 설정합니다. 입력을 완료했으면 ```CREATE AD UNIT``` 버튼을 눌러 설정을 끝냅니다.

![finished configuration](/assets/images/category/react-native/react-native-admob/finished_configuration.png)

구글 애드몹(Google admob)의 배너 설정을 완료했습니다. 다시 나온 app ID와 배너의 ad unit ID를 잘 복사해 둡니다.

## react-native-admob
구글 애드몹(Google admob)에서 설정한 배너를 RN(react-native)에서 사용하기 위해 react-native-admob의 사용법을 알아봅시다.

### iOS 설정
구글 애드몹(Google admob)을 iOS에서 사용하려면 ```ios/프로젝트명/AppDelegate.m```를 수정해야합니다.

```
#import <React/RCTRootView.h>

@import GoogleMobileAds;
```

위에서 다운로드하여 xcode에 추가한 ```Google Mobile Ads SDK``` 라이브러리를 임포트합니다.

```
self.window.rootViewController = rootViewController;

[GADMobileAds configureWithApplicationID:@"ca-app-pub-7987914246691031~8295071692"];

[self.window makeKeyAndVisible];
```

구글 애드몹(Google admob)을 생성할 때 복사한 app ID를 넣은 ```[GADMobileAds configureWithApplicationID:@"구글 애드몹 앱 ID"];``` 코드를 위와 같은 위치에 넣습니다.

이로써 iOS에서 구글 애드몹(Google admob)을 사용할 준비가 되었습니다.


### react-native-admob 사용
구글 애드몹(Google admob)에 설정한 배너를 사용하기위해 배너를 표시하고자하는 파일에 ```react-native-admob``` 라이브러리에 ```AdMobBanner```를 임포트합니다.

```js
import { AdMobBanner } from 'react-native-admob';
```

구글 애드몹(Google admob) 배너를 표시하고 싶은 위치에 아래에 코드를 붙여 넣습니다.

```js
<AdMobBanner
    adSize="fullBanner"
    adUnitID="자신의 ad unit ID"
    testDevices={[AdMobBanner.simulatorId]}
    onAdFailedToLoad={error => console.log(error)}
/>
```

- adSize: 광고의 사이즈를 결정합니다. 사이즈에 관해서는 공식 사이트를 참고하시기 바랍니다.([react-native-admob banner size](https://github.com/sbugert/react-native-admob#admobbanner){:rel="nofollow noreferrer" target="_blank"})
- adUnitID: 구글 애드몹(Google admob)에서 생성한 배너 유닛의 아이디(ad unit ID)를 복사해서 넣습니다.
- testDevices: 테스트용 단말기의 아이디를 넣습니다. 여기서는 시뮬레이터의 아이디를 설정했습니다.
- onAdFailedToLoad: 광고의 로딩이 실패한 경우에 처리 부분입니다.

설정이 완료되었습니다. 프로젝트를 실행하여 광고가 잘 표시되는지 확인합니다.


## 안드로이드(Android)
~~안드로이드(Android) 부분은 실제로 개발하여 추가되면 블로그에 추가할 예정입니다.~~
현재 react-native-admob 라이브러리르 사용하지 않기로 했습니다. 따라서 안드로이드(Android)를 부분이 추가되지 않을 예정입니다.


## 알림
우리는 react-native-firebase를 사용하여 구글 애드몹(Google Admob)을 표시하기로 했습니다. 자세한 사항은 [Firebase Admob]({{site.url}}/{{page.categories}}/react-native-firebase-admob/){:target="_blank"} 블로그를 참고하시기바랍니다.