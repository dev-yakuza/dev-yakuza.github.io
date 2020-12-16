---
layout: 'post'
permalink: '/react-native/react-native-firebase-v6-admob/'
paginate_path: '/react-native/:num/react-native-firebase-v6-admob/'
lang: 'en'
categories: 'react-native'
comments: true

title: react-native-firebase V6 Admob
description: Let's how to use react-native-firebase(V6) for Firebase Admob.
image: '/assets/images/category/react-native/2020/react-native-firebase-v6-admob/background.jpg'
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [Install and prepare react-natiev-firebase](#install-and-prepare-react-natiev-firebase)
- [Admob configuration](#admob-configuration)
  - [Signup Google Admob](#signup-google-admob)
  - [Create Admob](#create-admob)
- [Install library](#install-library)
- [Configure Admob ID](#configure-admob-id)
- [Javascript](#javascript)
  - [Configure Advertisement](#configure-advertisement)
  - [Banner ads](#banner-ads)
  - [Example source](#example-source)
- [Completed](#completed)

</div>

## Outline

In this blog post, I will show you how to use `react-native-firebase` to use [Admob](https://firebase.google.com/docs/crashlytics){:rel="nofollow noreferrer" target="_blank"} via [Firebase](https://firebase.google.com/){:rel="nofollow noreferrer" target="_blank"}.

- react-native-firebase(V6): [https://rnfirebase.io/](https://rnfirebase.io/){:rel="nofollow noreferrer" target="_blank"}

This blog post is a series. If you want to know more, see the blog posts below.

- [react-native-firebase V6 installation]({{site.url}}/{{page.categories}}/react-native-firebase-v6-installation/){:target="_blank"}
- [react-native-firebase V6 Crashlytics]({{site.url}}/{{page.categories}}/react-native-firebase-v6-crashlytics/){:target="_blank"}
- react-native-firebase V6 Admob

If you want to know how to use react-native-firebase previous version(V5), see the blog posts below.

- [Firebase Analytics]({{site.url}}/{{page.categories}}/react-native-firebase-analytics/){:target="_blank"}
- [Firebase Crashlytics]({{site.url}}/{{page.categories}}/firebase-crashlytics/){:target="_blank"}
- [Firebase Admob]({{site.url}}/{{page.categories}}/react-native-firebase-admob/){:target="_blank"}
- [Push message via react-native-firebase(V5)]({{site.url}}/{{page.categories}}/react-native-firebase-fcm/){:target="_blank"}

## Install and prepare react-natiev-firebase

see the blog post to install react-native-firebase, and prepare Firebase project.

- [react-native-firebase V6 설치]({{site.url}}/{{page.categories}}/react-native-firebase-v6-installation/){:target="_blank"}

{% include in-feed-ads.html %}

## Admob configuration

To use Admob in React native, we need to use Admob service.

### Signup Google Admob

Go to Google Admob site and signup. This is normal process of the signup, so I skip to explain.

- Google Admob site: [https://www.google.com/admob/](https://www.google.com/admob/){:rel="nofollow noreferrer" target="_blank" }

### Create Admob

Let's see how to use Google Admob. To use Google Admob, when you signup and signin Google Admob, you can see the screen like below.

![signin google admob](/assets/images/category/react-native/2020/react-native-firebase-v6-admob/signin_google_admob.jpg)

Click `GET STARTED` button on the bootom to start to use Google Admob.

![configure admob](/assets/images/category/react-native/2020/react-native-firebase-v6-admob/configure_admob.jpg)

The screen asks that your app is already registered on the markets. We didn't register the app, so select `NO`.

![configure app name on admob](/assets/images/category/react-native/2020/react-native-firebase-v6-admob/configure_app_name.jpg)

To use Google Admob, insert App name, and select the platform. In here, we select `iOS` first.

![completed to configure](/assets/images/category/react-native/2020/react-native-firebase-v6-admob/completed_configure.jpg)

Done! we've registered Google Admob. There are details about next step.

1. copy `App ID` for setting react-native-admob
1. we need to configure Ad Unit in Google Admob.
1. after releasing the app to Market, we need to link it in Google Admob.

Click `NEXT: CREATE AD UNIT` to go to Advertisement configuration.

![select advertisement type](/assets/images/category/react-native/2020/react-native-firebase-v6-admob/select_ad_uni.jpg)

In here, I will show how to use Banner via react-native-firebase, so clic `SELECT` button on the bottom of `Banner`.

![input banner name](/assets/images/category/react-native/2020/react-native-firebase-v6-admob/set_banner_name.jpg)

Insert Banner name. This banner name just helps you find and recognize this banner on Google Admob. After inserting, Click `CREATE AD UNIT` button.

![finished configuration](/assets/images/category/react-native/2020/react-native-firebase-v6-admob/finished_configuration.jpg)

Completed to set Google Admob banner. Copy App ID and ad unit ID.

For Android, create a banner by the same way above, and create App ID and Ad Unit ID, too.

{% include in-feed-ads.html %}

## Install library

Execute the command below to install `Admob` in `react-native-firebase`.

```bash
npm install --save @react-native-firebase/admob
```

## Configure Admob ID

Create `firebase.json` on the root folder of React Native project, and configure `App ID` created on Admob above like below.

```json
{
  "react-native": {
    "admob_android_app_id": "ca-app-pub-xxxxxxxx~xxxxxxxx",
    "admob_ios_app_id": "ca-app-pub-xxxxxxxx~xxxxxxxx"
  }
}
```

Execute the command below for iOS.

```bash
# cd ios
pod install
```

{% include in-feed-ads.html %}

## Javascript

Now, let's see Javascript source code to use Admob in React Native.

### Configure Advertisement

Before sending an advertisement request, we need to configure the request for what we want to receive the advertisement based on the target users. Before sending the request, configure the advertisement like below.

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

- maxAdContentRating: Set Admob's ad rating.
  - G: All spectators
  - PG: Parental supervision required
  - T: Teenagers and Over
  - MA: Teenagers not allowed
- tagForChildDirectedTreatment: If the children is your app target, you need to set true.
- tagForUnderAgeOfConsent: If the teenagers is your app target, you need to set true.

After this settings, you can send the advertisement request.

### Banner ads

You can use the code below to show Banner ads.

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

### Example source

The code below is that I use for production. I hope this code is helpful.

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

## Completed

We've seen how to display Admob on React Native by `react-native-firebase`. When I use other advertisement types, I will modify this blog post!
