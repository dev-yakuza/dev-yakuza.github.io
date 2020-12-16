---
layout: 'post'
permalink: '/react-native/react-native-firebase-v6-admob/'
paginate_path: '/react-native/:num/react-native-firebase-v6-admob/'
lang: 'ja'
categories: 'react-native'
comments: true

title: react-native-firebase V6 Admob
description: react-native-firebase(V6)を使ってFirebaseのAdmobを使う方法について説明します。
image: '/assets/images/category/react-native/2020/react-native-firebase-v6-admob/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [react-natiev-firebaseのインストールや準備](#react-natiev-firebaseのインストールや準備)
- [Admob設定](#admob設定)
  - [グーグルAdmob登録](#グーグルadmob登録)
  - [Admob生成](#admob生成)
- [ライブラリインストール](#ライブラリインストール)
- [Admob ID 設定](#admob-id-設定)
- [Javascript](#javascript)
  - [広告設定](#広告設定)
  - [Banner広告](#banner広告)
  - [例題ソースコード](#例題ソースコード)
- [完了](#完了)

</div>

## 概要

React Nativeプロジェクトで[Firebase](https://firebase.google.com/){:rel="nofollow noreferrer" target="_blank"}の[Admob](https://firebase.google.com/docs/crashlytics){:rel="nofollow noreferrer" target="_blank"}を使うため`react-native-firebase`を使う方法について説明します。

- react-native-firebase(V6): [https://rnfirebase.io/](https://rnfirebase.io/){:rel="nofollow noreferrer" target="_blank"}

このブログポストはシリーズで作成されております。他の内容を確認したい方は下記のブログリストを参考してください。

- [react-native-firebase V6 インストール]({{site.url}}/{{page.categories}}/react-native-firebase-v6-installation/){:target="_blank"}
- [react-native-firebase V6 Crashlytics]({{site.url}}/{{page.categories}}/react-native-firebase-v6-crashlytics/){:target="_blank"}
- react-native-firebase V6 Admob

react-native-firebaseの以前のバージョン(V5)を使う方法については下記のブログリストを参考してください。

- [Firebase Analytics]({{site.url}}/{{page.categories}}/react-native-firebase-analytics/){:target="_blank"}
- [Firebase Crashlytics]({{site.url}}/{{page.categories}}/firebase-crashlytics/){:target="_blank"}
- [Firebase Admob]({{site.url}}/{{page.categories}}/react-native-firebase-admob/){:target="_blank"}
- [react-native-firebase(V5)を使ってPush Message]({{site.url}}/{{page.categories}}/react-native-firebase-fcm/){:target="_blank"}

## react-natiev-firebaseのインストールや準備

下記のブログを参考してreact-native-firebaseをインストールして、Firebaseプロジェクトを生成します。

- [react-native-firebase V6 インストール]({{site.url}}/{{page.categories}}/react-native-firebase-v6-installation/){:target="_blank"}

{% include in-feed-ads.html %}

## Admob設定

React NativeプロジェクトでAdmobを使うためにはAdmobサービスを利用する必要があります。

### グーグルAdmob登録

GoogleのAdmobサイトへ移動して会員登録をします。一般的な会員登録やログインなので説明は省略します。

- GoogleのAdmobサイト: [https://www.google.com/admob/](https://www.google.com/admob/){:rel="nofollow noreferrer" target="_blank" }

### Admob生成

GoogleのAdmobの使い方について説明します。GoogleのAdmobを使う待てGoogleのAdmobサイトで会員登録してログインをすると下記のような画面が見えます。

![signin google admob](/assets/images/category/react-native/2020/react-native-firebase-v6-admob/signin_google_admob.jpg)

下にある`GET STARTED`ボタンを押してGoogleのAdmobを使い始めます。

![configure admob](/assets/images/category/react-native/2020/react-native-firebase-v6-admob/configure_admob.jpg)

すでにアプリがマーケットへ登録されたかどうかを選択します。ここではまだアプリを登録してないので、`NO`を選択します。

![configure app name on admob](/assets/images/category/react-native/2020/react-native-firebase-v6-admob/configure_app_name.jpg)

GoogleのAdmobを使うためアプリの名前を作成して、Platformを選択します。ここではまず、`iOS`を選択して進めます。

![completed to configure](/assets/images/category/react-native/2020/react-native-firebase-v6-admob/completed_configure.jpg)

GoogleのAdmobの登録が終わりました。次のステップが書いてる手順が表示されます。

1. まず、react-native-admobを設定する時必要な`App ID`をコピーします。
1. 広告のタイプ(ad unit)をグーグルアドモブ(Google admob)に設定します。
1. アプリをマーケットへ登録したらグーグルアドモブ(Google admob)へ連携する必要があります。

下にある`NEXT: CREATE AD UNIT`を押して広告タイプを設定する画面へ移動します。

![select advertisement type](/assets/images/category/react-native/2020/react-native-firebase-v6-admob/select_ad_uni.jpg)

ここではバナーを使ってみます。`Banner`の下の`SELECT`ボタンを選択します。

![input banner name](/assets/images/category/react-native/2020/react-native-firebase-v6-admob/set_banner_name.jpg)

バナーの名前を設定します。GoogleのAdmobで該当するバナーを簡単に探すための名前なので、自分が分かりやすい名前で設定します。入力が終わったら、`CREATE AD UNIT`ボタンを押して設定をします。

![finished configuration](/assets/images/category/react-native/2020/react-native-firebase-v6-admob/finished_configuration.jpg)

GoogleのAdmobのバナーの設定が終わりました。また、でったApp IDとバナーのAd Unit IDをコピーしておきます。

アンドロイドも上と同じ方法でバナー広告を生成してApp IDとAd Unit IDを生成します。

{% include in-feed-ads.html %}

## ライブラリインストール

下記のコマンドを使って`react-native-firebase`の`Admob`をインストールします。

```bash
npm install --save @react-native-firebase/admob
```

## Admob ID 設定

React NativeプロジェクトのRootフォルダへ`firebase.json`ファイルを作って、Admobで作った`App ID`を設定します。

```json
{
  "react-native": {
    "admob_android_app_id": "ca-app-pub-xxxxxxxx~xxxxxxxx",
    "admob_ios_app_id": "ca-app-pub-xxxxxxxx~xxxxxxxx"
  }
}
```

iOSを使う場合は下記のコマンドを実行します。

```bash
# cd ios
pod install
```

{% include in-feed-ads.html %}

## Javascript

次は、React NativeでAdmobを使うためのスースコードを説明します。

### 広告設定

Admobで広告をリクエストする前、どんな広告を貰いたいかターゲットユーザベースで設定する必要があります。広告をリクエストする前下記のように広告を設定します。

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

- maxAdContentRating: Admobの広告レベルを設定します。
  - G: 全体観覧可
  - PG: 保護者の監督の要望
  - T: 青少年以上観覧可
  - MA: 青少年観覧不可
- tagForChildDirectedTreatment: アプリが子供用の場合trueを設定します。
- tagForUnderAgeOfConsent: アプリが大人以下をターゲットにする場合trueを設定します。

このように設定した後、アプリで広告をリクエストします。

### Banner広告

バナー広告を使うため下記のようなソースコードを使います。s

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

### 例題ソースコード

私が使ってるバナー広告のソースコードです。参考できたら嬉しいです。

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

## 完了

これでReact NativeでAdmobを表示するため、`react-native-firebase`を使う方法について説明しました。他の広告を使うことになったら、その内容をまた追加します。
