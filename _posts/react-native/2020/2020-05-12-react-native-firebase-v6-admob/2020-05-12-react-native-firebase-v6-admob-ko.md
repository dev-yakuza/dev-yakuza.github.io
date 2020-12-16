---
layout: 'post'
permalink: '/react-native/react-native-firebase-v6-admob/'
paginate_path: '/react-native/:num/react-native-firebase-v6-admob/'
lang: 'ko'
categories: 'react-native'
comments: true

title: react-native-firebase V6 Admob
description: react-native-firebase(V6)을 사용하여 Firebase의 Admob을 사용하는 방법에 대해서 알아봅시다.
image: '/assets/images/category/react-native/2020/react-native-firebase-v6-admob/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [react-natiev-firebase 설치 및 준비](#react-natiev-firebase-설치-및-준비)
- [Admob 설정](#admob-설정)
  - [구글 애드몹 가입](#구글-애드몹-가입)
  - [Admob 생성](#admob-생성)
- [라이브러리 설치](#라이브러리-설치)
- [Admob ID 설정](#admob-id-설정)
- [Javascript](#javascript)
  - [광고 설정](#광고-설정)
  - [Banner 광고](#banner-광고)
  - [예제 소스](#예제-소스)
- [완료](#완료)

</div>

## 개요

React Native 프로젝트에서 [Firebase](https://firebase.google.com/){:rel="nofollow noreferrer" target="_blank"}의 [Admob](https://firebase.google.com/docs/crashlytics){:rel="nofollow noreferrer" target="_blank"}을 사용하기 위해 `react-native-firebase`를 사용하는 방법에 대해서 알아보려고 합니다.

- react-native-firebase(V6): [https://rnfirebase.io/](https://rnfirebase.io/){:rel="nofollow noreferrer" target="_blank"}

이 블로그는 시리즈로 제작되어있습니다. 다른 내용을 확인하고 싶으신 분들은 아래에 블로그 리스트를 참고하시기 바랍니다.

- [react-native-firebase V6 설치]({{site.url}}/{{page.categories}}/react-native-firebase-v6-installation/){:target="_blank"}
- [react-native-firebase V6 Crashlytics]({{site.url}}/{{page.categories}}/react-native-firebase-v6-crashlytics/){:target="_blank"}
- react-native-firebase V6 Admob

react-native-firebase의 이전 버전(V5)을 사용하는 방법에 대해서는 아래에 블로그 리스트를 참고하시기 바랍니다.

- [Firebase Analytics]({{site.url}}/{{page.categories}}/react-native-firebase-analytics/){:target="_blank"}
- [Firebase Crashlytics]({{site.url}}/{{page.categories}}/firebase-crashlytics/){:target="_blank"}
- [Firebase Admob]({{site.url}}/{{page.categories}}/react-native-firebase-admob/){:target="_blank"}
- [react-native-firebase(V5)를 이용한 Push message]({{site.url}}/{{page.categories}}/react-native-firebase-v6-admob/){:target="_blank"}

## react-natiev-firebase 설치 및 준비

아래에 블로그를 참고하여 react-native-firebase를 설치하고, Firebase 프로젝트를 생성합니다.

- [react-native-firebase V6 설치]({{site.url}}/{{page.categories}}/react-native-firebase-v6-installation/){:target="_blank"}

{% include in-feed-ads.html %}

## Admob 설정

React Native 프로젝트에서 Admob을 사용하기 위해서는, Admob 서비스를 이용할 필요가 있습니다.

### 구글 애드몹 가입

구글 애드몹(Google admob) 사이트로 이동하여 회원가입을 합니다. 일반적인 회원가입/로그인 절차임으로 설명을 생략합니다.

- 구글 애드몹(Google admob) 사이트: [https://www.google.com/admob/](https://www.google.com/admob/){:rel="nofollow noreferrer" target="_blank" }

### Admob 생성

구글 애드몹(Google admob) 사용법에 대해서 알아봅니다. 구글 애드몹(Google admob)을 사용하기 위해 구글 애드몹(Google admob) 사이트에 회원가입을 하고 로그인을 하면 아래와 같은 화면을 볼 수 있습니다.

![signin google admob](/assets/images/category/react-native/2020/react-native-firebase-v6-admob/signin_google_admob.jpg)

하단에 있는 `GET STARTED` 버튼을 눌러 구글 애드몹(Google Admob)에 사용을 시작합니다.

![configure admob](/assets/images/category/react-native/2020/react-native-firebase-v6-admob/configure_admob.jpg)

이미 앱이 마켓에 등록되어있는지 여부를 선택합니다. 우리는 아직 앱을 등록하지 않은 상태이므로 `NO`를 선택합니다.

![configure app name on admob](/assets/images/category/react-native/2020/react-native-firebase-v6-admob/configure_app_name.jpg)

구글 애드몹(Google admob)을 사용하기 위해 앱 이름을 작성하고 사용할 플랫폼을 선택합니다. 우리는 우선 `iOS`를 선택하여 진행하겠습니다.

![completed to configure](/assets/images/category/react-native/2020/react-native-firebase-v6-admob/completed_configure.jpg)

구글 애드몹(Google admob) 등록이 완료되었습니다. 친절하게 하단에 다음 단계에 대한 설명이 잘 나와있습니다.

1. react-native-admob을 설정할때 필요한 `App ID`를 복사해둡니다.
1. 광고 타입(ad unit)을 구글 애드몹(Google admob)에서 설정합니다.
1. 앱을 앱스토어에 등록하면 구글 애드몹(Google Admob)에서 연결해줘야합니다.

하단에 있는 `NEXT: CREATE AD UNIT`을 눌러 광고 타입 설정화면으로 이동합니다.

![select advertisement type](/assets/images/category/react-native/2020/react-native-firebase-v6-admob/select_ad_uni.jpg)

우리는 일단 배너 광고 사용해 보겠습니다. `Banner`의 하단에 `SELECT`버튼을 선택합니다.

![input banner name](/assets/images/category/react-native/2020/react-native-firebase-v6-admob/set_banner_name.jpg)

해당 배너의 이름을 설정합니다. 구글 애드몹(Google admob) 서비스에서 해당 배너를 쉽게 찾기 위한 이름이므로 자신이 쉽게 인식할 수 있는 이름을 설정합니다. 입력을 완료했으면 `CREATE AD UNIT` 버튼을 눌러 설정을 끝냅니다.

![finished configuration](/assets/images/category/react-native/2020/react-native-firebase-v6-admob/finished_configuration.jpg)

구글 애드몹(Google admob)의 배너 설정을 완료했습니다. 다시 나온 App ID와 배너의 Ad Unit ID를 잘 복사해 둡니다.

안드로이드도 위와 같은 방식으로 배너 광고를 생성하여 App ID와 Ad Unit ID를 생성합니다.

{% include in-feed-ads.html %}

## 라이브러리 설치

아래에 명령어를 사용하여 `react-native-firebase`의 `Admob`를 설치합니다.

```bash
npm install --save @react-native-firebase/admob
```

## Admob ID 설정

React Native 프로젝트의 루트 폴더에 `firebase.json` 파일을 만들고, Admob에서 만든 `App ID`를 설정합니다.

```json
{
  "react-native": {
    "admob_android_app_id": "ca-app-pub-xxxxxxxx~xxxxxxxx",
    "admob_ios_app_id": "ca-app-pub-xxxxxxxx~xxxxxxxx"
  }
}
```

iOS를 사용하시는 분들은 아래에 명령어를 실행합니다.

```bash
# cd ios
pod install
```

{% include in-feed-ads.html %}

## Javascript

이제 React Native에서 Admob을 사용하기 위한 소스코드를 살펴보도록 하겠습니다.

### 광고 설정

Admob에 광고를 요청하기 전에, 어떤 광고를 받고 싶은지 타겟 고객 기반으로 설정할 필요가 있습니다. 광고를 요청하기 전에 아래와 같이 광고를 설정합니다.

```js
import admob, { MaxAdContentRating } from '@react-native-firebase/admob';

admob()
  .setRequestConfiguration({
    maxAdContentRating: MaxAdContentRating.PG,
    tagForChildDirectedTreatment: true,
    tagForUnderAgeOfConsent: true,
  })
  .then(() => {
    // Request config successfully set!
  });
```

- maxAdContentRating: Admob의 광고 등급을 설정합니다.
  - G: 전체 관람가
  - PG: 보호자 감독 요망
  - T: 청소년 이상 관람가
  - MA: 청소년 관람 불가
- tagForChildDirectedTreatment: 앱이 어린이용인 경우 true를 설정합니다.
- tagForUnderAgeOfConsent: 앱이 성인 이하를 대상으로 하는 경우 true를 설정합니다.

이렇게 설정을 한 후, 앱에서 광고를 요청합니다.

### Banner 광고

배너 광고를 사용하기 위해서는 아래와 같은 소스 코드를 이용합니다.

```js
{% raw %}
import React from 'react';
import { BannerAd, BannerAdSize, TestIds } from '@react-native-firebase/admob';

const adUnitId = __DEV__ ? TestIds.BANNER : 'ca-app-pub-xxxxxxxxxxxxx/yyyyyyyyyyyyyy';

function App() {
  return (
    <BannerAd
      unitId={adUnitId}
      size={BannerAdSize.FULL_BANNER}
      requestOptions={{
        requestNonPersonalizedAdsOnly: true,
      }}
    />
  );
}
{% endraw %}
```

{% include in-feed-ads.html %}

### 예제 소스

제가 사용하고 있는 배너 광고 예제 소스입니다. 참고가 되면 좋겠습니다.

```js
{% raw %}
import React, { useState, useEffect } from 'react';
import admob, {
  MaxAdContentRating,
  BannerAd,
  BannerAdSize,
  TestIds,
} from '@react-native-firebase/admob';
import Styled from 'styled-components/native';

import ENV from '~/ENV';

interface StyledProp {
  isRectangleBanner?: boolean;
}

const Container = Styled.SafeAreaView`
  background-color: #F4F5F8;
`;
const Contents = Styled.View`
  width: 100%;
  height: ${(props: StyledProp): string => (props.isRectangleBanner ? '100%' : '70px')};
  justify-content: center;
  align-items: center;
`;

interface Props {
  size?: 'MEDIUM_RECTANGLE';
}

const BannerContainer = ({ size }: Props): JSX.Element => {
  const [showBanner, setShowBanner] = useState<boolean>(false);

  let hideBannerTimer: NodeJS.Timeout | undefined = undefined;
  let showBannerTimer: NodeJS.Timeout | undefined = undefined;

  const clearHideBannerTimer = (): void => {
    if (hideBannerTimer) {
      clearTimeout(hideBannerTimer);
      hideBannerTimer = undefined;
    }
  };

  const clearShowBannerTimer = (): void => {
    if (showBannerTimer) {
      clearTimeout(showBannerTimer);
      showBannerTimer = undefined;
    }
  };

  useEffect(() => {
    admob()
      .setRequestConfiguration({
        maxAdContentRating: MaxAdContentRating.PG,
        tagForChildDirectedTreatment: false,
        tagForUnderAgeOfConsent: true,
      })
      .then(() => {
        setShowBanner(true);
      });

    return (): void => {
      clearHideBannerTimer();
      clearShowBannerTimer();
    };
  }, []);

  const adUnitID = __DEV__ ? TestIds.BANNER : ENV.adUnitID;
  const bannerSize = size ? size : BannerAdSize.SMART_BANNER;

  return (
    <Container>
      <Contents isRectangleBanner={bannerSize === 'MEDIUM_RECTANGLE'}>
        {showBanner && (
          <BannerAd
            unitId={adUnitID}
            size={bannerSize}
            requestOptions={{
              requestNonPersonalizedAdsOnly: true,
            }}
            onAdLoaded={(): void => {
              console.log('Advert loaded');
              clearHideBannerTimer();
              hideBannerTimer = setTimeout(() => {
                setShowBanner(false);
                clearShowBannerTimer();
                showBannerTimer = setTimeout(() => {
                  setShowBanner(true);
                }, 600);
              }, 30000);
            }}
            onAdFailedToLoad={(error: any): void => {
              console.log('Advert fail');
              console.log(error.code);
              console.log(error.message);
              setShowBanner(false);
              setTimeout(() => {
                setShowBanner(true);
              }, 3000);
            }}
          />
        )}
      </Contents>
    </Container>
  );
};

export default BannerContainer;
{% endraw %}
```

## 완료

이것으로 React Native에 Admob을 표시하기 위해서, `react-native-firebase`를 사용하는 방법에 대해서 알아보았습니다. 다른 광고를 사용하게 되면 해당 내용을 추가하도록 하겠습니다.
