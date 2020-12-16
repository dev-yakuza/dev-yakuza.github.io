---
layout: 'post'
permalink: '/react-native/react-native-admob-native-ads/'
paginate_path: '/react-native/:num/react-native-admob-native-ads/'
lang: 'en'
categories: 'react-native'
comments: true

title:  Admob Native Advanced on React Native
description: Let's see how to use react-native-admob-native-ads to display Admob Native Advanced on React Native.
image: '/assets/images/category/react-native/2020/react-native-admob-native-ads/background.jpg'
---

<div id="contents_list" markdown="1">

## Contents

- [Contents](#contents)
- [Outline](#outline)
- [react-native-admob-native-ads installation](#react-native-admob-native-ads-installation)
- [react-native-admob-native-ads configuration](#react-native-admob-native-ads-configuration)
- [How to use react-native-admob-native-ads](#how-to-use-react-native-admob-native-ads)
- [Other components](#other-components)
- [Completed](#completed)

</div>

## Outline

When I develop the applications, I always use Admob Banner. I use `react-native-firebase` V6 to implement Admob Banner.

- [react-native-firebase V6 Admob]({{site.url}}/{{page.categories}}/react-native-firebase-v6-admob/){:target="_blank"}

However, when I made a toy project, I needed to show Admob Native Advanced.

- [「Clog」 Service Development Journal(React Native, Laravel, Django)]({{site.url}}/clog/development-journal/){:target="_blank"}

Unfortunately, react-native-firebase does not support Native Advanced. If you want to know more details, see the link below.

- [New Native Ad Format](https://invertase.canny.io/react-native-firebase/p/new-native-ad-format){:rel="nofollow noreferrer" target="_blank"}

In this blog post, we will see how to use `react-native-admob-native-ads` library to display Admob Native Advanced on React Native.

- [react-native-admob-native-ads](https://github.com/ammarahm-ed/react-native-admob-native-ads){:rel="nofollow noreferrer" target="_blank"}

## react-native-admob-native-ads installation

Execute the command below to install react-native-admob-native-ads.

```bash
npm install --save react-native-admob-native-ads
```

## react-native-admob-native-ads configuration

To show Native Advanced viat react-native-admob-native-ads, we need to configure the follows.

- [iOS Setup](https://github.com/ammarahm-ed/react-native-admob-native-ads#ios-setup){:rel="nofollow noreferrer" target="_blank"}
- [Android Setup](https://github.com/ammarahm-ed/react-native-admob-native-ads#android-setup){:rel="nofollow noreferrer" target="_blank"}

However, I've already used react-native-fireabse, so I didn't configure above. If you want to know how to configure via react-native-firebase, see the link below.바랍니다.

- [react-native-firebase V6 Admob]({{site.url}}/{{page.categories}}/react-native-firebase-v6-admob/){:target="_blank"}

{% include in-feed-ads.html %}

## How to use react-native-admob-native-ads

There is nice official document about how to use. see the link below.

- [Basic Usage Example](https://github.com/ammarahm-ed/react-native-admob-native-ads#basic-usage-example){:rel="nofollow noreferrer" target="_blank"}

The source code below is what I use to display Native Advanced on my application by react-native-admob-native-ads.

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

## Other components

You can design the advertisement by Admob Native Advacned. See the link below what you can use other components in react-native-admob-native-ads.
Admob의 Native Advanced 광고는 자신의 디자인에 맞춰 자유롭게 변경할 수 있는 장점이 있습니다. 아래 링크를 통해, 사용 가능한 컴포넌트들을 확인하시기 바랍니다.

- [react-native-admob-native-ads reference](https://github.com/ammarahm-ed/react-native-admob-native-ads#-reference){:rel="nofollow noreferrer" target="_blank"}

## Completed

We've seen how to use react-native-admob-native-ads to display Admob Native Advanced on React Native. Now, you can design the advertisements to protect the user experience.
