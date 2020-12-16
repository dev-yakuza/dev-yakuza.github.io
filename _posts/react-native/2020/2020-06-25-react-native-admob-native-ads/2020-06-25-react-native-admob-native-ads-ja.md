---
layout: 'post'
permalink: '/react-native/react-native-admob-native-ads/'
paginate_path: '/react-native/:num/react-native-admob-native-ads/'
lang: 'ja'
categories: 'react-native'
comments: true

title: React NativeでAdmobのNative Advanced広告を使う方法
description: React NativeでAdmobのNative Advanced広告を使うため、react-native-admob-native-adsライブラリを使う方法について説明します。
image: '/assets/images/category/react-native/2020/react-native-admob-native-ads/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [目次](#目次)
- [概要](#概要)
- [react-native-admob-native-adsインストール](#react-native-admob-native-adsインストール)
- [react-native-admob-native-ads設定](#react-native-admob-native-ads設定)
- [react-native-admob-native-ads使い方](#react-native-admob-native-ads使い方)
- [他のコンポーネント](#他のコンポーネント)
- [完了](#完了)

</div>

## 概要

React Nativeを使ってアプリを開発する時、AdmobのBanner広告を結構使いました。AdmobのBanner広告は`react-native-firebase`のV6を使って実装しました。

- [react-native-firebase V6 Admob]({{site.url}}/{{page.categories}}/react-native-firebase-v6-admob/){:target="_blank"}

しかし、トーイプロジェクトを進める時、AdmobのNative Advanced広告を使う必要がありました。

- [「Clog」 サービス開発日誌(React Native, Laravel, Django)]({{site.url}}/clog/development-journal/){:target="_blank"}

残念ながら、react-native-firebaseではNative Advanced広告をサーポートしてないです。詳しく内容は下記のリンクを参考してください。

- [New Native Ad Format](https://invertase.canny.io/react-native-firebase/p/new-native-ad-format){:rel="nofollow noreferrer" target="_blank"}

このブログポストではReact NativeでAdmobのNative Advanced広告を使うため、`react-native-admob-native-ads`ライブラリを使う方法について説明します。

- [react-native-admob-native-ads](https://github.com/ammarahm-ed/react-native-admob-native-ads){:rel="nofollow noreferrer" target="_blank"}

## react-native-admob-native-adsインストール

下記のコマンドを使ってreact-native-admob-native-adsをインストールします。

```bash
npm install --save react-native-admob-native-ads
```

## react-native-admob-native-ads設定

react-native-admob-native-adsを使ってNative Advanced広告を表示するためには下記のように設定する必要があります。

- [iOS Setup](https://github.com/ammarahm-ed/react-native-admob-native-ads#ios-setup){:rel="nofollow noreferrer" target="_blank"}
- [Android Setup](https://github.com/ammarahm-ed/react-native-admob-native-ads#android-setup){:rel="nofollow noreferrer" target="_blank"}

しかし、私は既にreact-native-firebaseを使っているので、上の設定はしませんんでした。react-native-firebaseを使ってAdmobを設定する方法については下記のリンクを参考してください。

- [react-native-firebase V6 Admob]({{site.url}}/{{page.categories}}/react-native-firebase-v6-admob/){:target="_blank"}

{% include in-feed-ads.html %}

## react-native-admob-native-ads使い方

公式ドキュメントへ詳しく使い方が載せております。下記のリンクを参考してください。

- [Basic Usage Example](https://github.com/ammarahm-ed/react-native-admob-native-ads#basic-usage-example){:rel="nofollow noreferrer" target="_blank"}

下記のソースコードはreact-native-admob-native-adsを使ってNative Advanced広告を表示するため、私がアプリで使ってるソースコードです。

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

## 他のコンポーネント

AdmobのNative Advanced広告は自分のデザインに合わせて自由に変更することができます。下記のリンクを見て、使えるコンポーネントを確認してください。

- [react-native-admob-native-ads reference](https://github.com/ammarahm-ed/react-native-admob-native-ads#-reference){:rel="nofollow noreferrer" target="_blank"}

## 完了

これでReact NativeでAdmobのNative Advanced広告を表示する方法を見てみました。今後はもっと自由に広告をデザインして、ユーザのUXを守れながら、広告を提供してみてください。
