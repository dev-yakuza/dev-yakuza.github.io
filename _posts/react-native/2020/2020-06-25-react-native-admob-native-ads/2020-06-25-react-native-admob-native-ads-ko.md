---
layout: 'post'
permalink: '/react-native/react-native-admob-native-ads/'
paginate_path: '/react-native/:num/react-native-admob-native-ads/'
lang: 'ko'
categories: 'react-native'
comments: true

title: React Native에서 Admob의 Native Advanced 광고 사용하기
description: React Native에서 Admob의 Native Advanced 광고를 사용하기 위해 react-native-admob-native-ads 라이브러리를 사용하는 방법에 대해서 알아봅시다.
image: '/assets/images/category/react-native/2020/react-native-admob-native-ads/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

- [목차](#목차)
- [개요](#개요)
- [react-native-admob-native-ads 설치](#react-native-admob-native-ads-설치)
- [react-native-admob-native-ads 설정](#react-native-admob-native-ads-설정)
- [react-native-admob-native-ads 사용법](#react-native-admob-native-ads-사용법)
- [다른 컴포넌트](#다른-컴포넌트)
- [완료](#완료)

</div>

## 개요

React Native를 사용하여 앱을 개발할 때, Admob의 Banner 광고 위주로 사용했었습니다. Admob의 Banner 광고는 `react-native-firebase`의 V6를 사용하여 구현하였습니다.

- [react-native-firebase V6 Admob]({{site.url}}/{{page.categories}}/react-native-firebase-v6-admob/){:target="_blank"}

하지만, 토이프로젝트를 진행하면서 Admob의 Native Advanced 광고를 사용할 필요가 생겼습니다.

- [「Clog」 서비스 개발기(React Native, Laravel, Django)]({{site.url}}/clog/development-journal/){:target="_blank"}

불행이도 react-native-firebase에서는 Native Advanced 광고를 지원하지 않습니다. 자세한 내용은 아래에 링크를 참고하시기 바랍니다.

- [New Native Ad Format](https://invertase.canny.io/react-native-firebase/p/new-native-ad-format){:rel="nofollow noreferrer" target="_blank"}

이번 블로그 포스트에서는 React Native에서 Admob의 Native Advanced 광고를 사용하기 위해, `react-native-admob-native-ads` 라이브러리를 사용하는 방법에 대해서 알아봅시다.

- [react-native-admob-native-ads](https://github.com/ammarahm-ed/react-native-admob-native-ads){:rel="nofollow noreferrer" target="_blank"}

## react-native-admob-native-ads 설치

아래에 명령어를 사용하여 react-native-admob-native-ads를 설치합니다.

```bash
npm install --save react-native-admob-native-ads
```

## react-native-admob-native-ads 설정

react-native-admob-native-ads를 사용하여 Native Advanced 광고를 표시하기 위해서는 아래와 같은 절차를 진행해야 합니다.

- [iOS Setup](https://github.com/ammarahm-ed/react-native-admob-native-ads#ios-setup){:rel="nofollow noreferrer" target="_blank"}
- [Android Setup](https://github.com/ammarahm-ed/react-native-admob-native-ads#android-setup){:rel="nofollow noreferrer" target="_blank"}

하지만 저는 이미 react-native-firebase를 사용하고 있었기 때문에, 위에 설정을 진행하지 않았습니다. react-native-firebase를 통해 Admob을 설정하는 방법에 대해서는 아래에 링크를 참고하시기 바랍니다.

- [react-native-firebase V6 Admob]({{site.url}}/{{page.categories}}/react-native-firebase-v6-admob/){:target="_blank"}

{% include in-feed-ads.html %}

## react-native-admob-native-ads 사용법

공식 문서에 상세하게 사용하는 방법이 나와있습니다. 아래에 링크를 참고하시기 바랍니다.

- [Basic Usage Example](https://github.com/ammarahm-ed/react-native-admob-native-ads#basic-usage-example){:rel="nofollow noreferrer" target="_blank"}

아래 소스코드는 react-native-admob-native-ads를 사용하여 Native Advanced 광고를 표시하기 위해, 제가 앱에서 사용하는 소스코드입니다.

```js
import React, { Component } from 'react';
import { Platform } from 'react-native';
import Styled from 'styled-components/native';
import NativeAdView, {
  IconView,
  HeadlineView,
  TaglineView,
  MediaView,
} from 'react-native-admob-native-ads';
import FastImage from 'react-native-fast-image';

import ENV from '~/ENV';

const Container = Styled.View`
  background-color: #FFFFFF;
  margin-bottom: 12px;
  height: 330px;
`;
const AdsContainer = Styled(NativeAdView)``;
const AdsContents = Styled.View`
  background-color: #FFFFFF;
`;
const Header = Styled.View`
  padding: 16px 8px 8px 16px;
  flex-direction: row;
`;
const AdvertiserImage = Styled(IconView)`
  width: 32px;
  height: 32px;
  border-radius: 32px;
  background-color: #EEEEEE;
  border-width: 1px;
  border-color: #EEEEEE;
`;
const AdvertiserInfoContainer = Styled.View`
  flex: 1;
  margin-horizontal: 8px;
`;
const AdvertiserName = Styled(HeadlineView)`
  font-size: 12px;
  font-weight: 600;
  color: #2A365D;
  width: 100%;
`;
const PublishedDate = Styled.Text`
  font-size: 12px;
  font-weight: 300;
  color: #2A365D;
`;

const AdvertisementImage = Styled(MediaView)`
  width: 100%;
  height: 209px;
  background-color: #FFFFFF;
  border-top-width: 1px;
  border-bottom-width: 1px;
  border-color: #EEEEEE;
`;

const Content = Styled.View`
  height: 64px
  justify-content: center;
`;
const AdvertiserDescription = Styled(TaglineView)`
  color: #2A365D;
  font-size: 16px;
  line-height: 22px;
  font-weight: 400;
  padding: 4px 8px 16px 8px;
`;

const AuthorImage = Styled(FastImage)`
  width: 32px;
  height: 32px;
  border-radius: 32px;
  background-color: #EEEEEE;
  border-width: 1px;
  border-color: #EEEEEE;
`;
const AuthorName = Styled.Text`
  font-size: 12px;
  width: 100%;
  background-color: #ECEFF1;
  width: 80px;
`;
const PublishedDatePlaceholder = Styled.Text`
  font-size: 12px;
  font-weight: 300;
  width: 100px;
  background-color: #ECEFF1;
`;

const MainImage = Styled.View`
  width: 100%;
  height: 209px;
  background-color: #CFD8DC;
`;

const PostDescription = Styled.Text`
  background-color: #ECEFF1;
  font-size: 16px;
  line-height: 22px;
  font-weight: 400;
  margin: 4px 8px 16px 8px;
  width: 80%;
`;

const TEST_NATIVE_AD_ID =
  Platform.OS === 'ios'
    ? 'YOUR IOS NATIVE ADVANCE ID'
    : 'YOUR ANDROID NATIVE ADVANCE ID';

interface State {
  isShow: boolean;
  isLoaded: boolean;
}

interface Props {
  showDelay?: boolean;
}

class NativeBanner extends Component<Props, State> {
  constructor(props: Props) {
    super(props);

    this.state = {
      isShow: true,
      isLoaded: false,
    };
  }

  private timer: NodeJS.Timeout | undefined;

  private onAdFailedToLoad = (event: any): void => {
    console.log('NativeBanner failed');
    console.log(event.nativeEvent.error.message);
    this.setState({
      isLoaded: false,
    });
  };

  private onAdLoaded = (): void => {
    console.log('Ad has loaded');
    this.setState({
      isLoaded: true,
    });
  };

  private cancelTimer = (): void => {
    if (this.timer) {
      clearTimeout(this.timer);
      this.timer = undefined;
    }
  };

  render(): JSX.Element {
    const { showDelay } = this.props;
    const { isShow, isLoaded } = this.state;
    const adUnitID = __DEV__ ? TEST_NATIVE_AD_ID : ENV.nativeAdsId;
    return (
      <Container>
        {isShow && (
          <AdsContainer
            onAdLoaded={this.onAdLoaded}
            onAdFailedToLoad={this.onAdFailedToLoad}
            adUnitID={adUnitID}
            enableTestMode={__DEV__}
            delayAdLoading={showDelay ? 3000 : 0}>
            <AdsContents>
              <Header>
                {isLoaded ? (
                  <AdvertiserImage />
                ) : (
                  <AuthorImage source={require('~/Assets/Images/author.png')} />
                )}
                <AdvertiserInfoContainer>
                  {isLoaded ? <AdvertiserName numberOfLines={1} /> : <AuthorName />}
                  {isLoaded ? <PublishedDate>Sponsor</PublishedDate> : <PublishedDatePlaceholder />}
                </AdvertiserInfoContainer>
              </Header>
              {isLoaded ? <AdvertisementImage resizeMode="cover" /> : <MainImage />}
              <Content>
                {isLoaded ? <AdvertiserDescription numberOfLines={2} /> : <PostDescription />}
              </Content>
            </AdsContents>
          </AdsContainer>
        )}
      </Container>
    );
  }

  componentDidCatch(error: any): void {
    console.log('[NativeBanner] ERROR: ', error.toString());
    this.setState({
      isShow: false,
    });

    this.cancelTimer();
    this.timer = setTimeout(() => {
      this.setState({
        isShow: true,
      });
    }, 3000);
  }

  componentWillUnmount(): void {
    this.cancelTimer();
  }
}

export default NativeBanner;
```

## 다른 컴포넌트

Admob의 Native Advanced 광고는 자신의 디자인에 맞춰 자유롭게 변경할 수 있는 장점이 있습니다. 아래 링크를 통해, 사용 가능한 컴포넌트들을 확인하시기 바랍니다.

- [react-native-admob-native-ads reference](https://github.com/ammarahm-ed/react-native-admob-native-ads#-reference){:rel="nofollow noreferrer" target="_blank"}

## 완료

이것으로 React Native에서 Admob의 Native Advanced 광고를 표시하는 방법에 대해서 알아보았습니다. 이제 좀 더 자유롭게 광고를 디자인해서, 사용자의 UX를 해치지 않는 광고를 제공해 보시기 바랍니다.
