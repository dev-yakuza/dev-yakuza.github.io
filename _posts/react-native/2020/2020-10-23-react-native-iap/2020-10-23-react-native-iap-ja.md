---
layout: 'post'
permalink: '/react-native/react-native-iap/'
paginate_path: '/react-native/:num/react-native-iap/'
lang: 'ja'
categories: 'react-native'
comments: true

title: React Nativeでアプリ内課金を実装する
description: React Nativeでアプリ内課金を実装するためreact-native-iapを使う方法について説明します。
image: '/assets/images/category/react-native/2020/react-native-iap/background.jpg'
published: false
---

<div id="contents_list" markdown="1">

## 目次

</div>

## 概要

React Nativeでアプリ内課金を実装するため`react-native-iap`を使う方法に関して説明します。

- [react-native-iap](https://github.com/dooboolab/react-native-iap){:rel="nofollow noreferrer" target="_blank"}

## アプリ内商品を生成する

アプリ内課金を実装するためには、まずアプリ内商品を生成する必要があります。各プラットフォームに合わせてアプリ内商品を作る方法について説明します。

### iOSのアプリない商品を生成する

#### 契約、税金や金融取引の設定

iOSでアプリ内商品を作るためには、まず、`契約、税金や金融取引`を設定する必要があります。`契約、税金や金融取引`を設定するためAppstore Connectへ移動します。

![Appstore connect](/assets/images/category/react-native/2020/react-native-iap/appstoreconnect.jpg)

下にある`契約、税金や金融取引`(Agreements, Tax, and Banking)を選択して移動します。

![Paid apps](/assets/images/category/react-native/2020/react-native-iap/paid-apps.jpg)

私はすでに設定したので、上のような画面が表示されますが、皆さんは`有料アプリ`(Paid Apps)を設定する必要があります。必要な項目をうまく入力したら問題なく設定することができます。

#### アプリ内の購入アイテム生成

次はアプリ内の購入アイテムを生成する必要があります。アプリ内課金を実装するアプリを選択します。

![manage in-app purchases](/assets/images/category/react-native/2020/react-native-iap/manage-in-app-purchases.jpg)

左下の`アプリ内購入`(In-App Purcahses)の`管理`(Manage)を選択してプラスボタン(`+`)を押すと、上のように追加する商品を選ぶ画面がでます。

私は私のアプリへ`自動更新購読`(Auto-Renewable Subscription)を追加し他ので、`自動更新購読`を中心に説明します。他の商品を追加することになると、このブログポストへ追加します。

![in-app purchases reference name and product id](/assets/images/category/react-native/2020/react-native-iap/in-app-purchases-reference-name-product-id.jpg)

ここで`識別情報`(Reference Name)はAppstore connectだけ表示される名前なので、自分が分かりやすい名前に設定します。`商品ID`(Product ID)はアプリ中でアプリ内商品を取ってくる時、使います。

![in-app purchases group name](/assets/images/category/react-native/2020/react-native-iap/in-app-purchases-group-name.jpg)

その後、`購読グループ識別情報`(Subscription Group Reference Name)を入力します。`識別情報`(Reference Name)と同じように、Appstore connect中だけ表示されるので、自分が分かりやすい名前を設定します。

#### アプリ内購入メタデータを入力する

上のようにアプリ中購入アイテムを生成したら、次はアプリ中購入アイテムのメタデータを入力する必要があります。

![in-app purchases metadata](/assets/images/category/react-native/2020/react-native-iap/in-app-purchases-metadata.jpg)

左メニューでまた、`アプリ内購入`(In-App Purchases)の`管理`(Manage)を押すと上のようにメタデータ(Metadata)が入力されてないことが確認できます。ここで、識別情報の名前を選択して当該項目の詳細ページへ移動します。

![in-app purchases insert metadata](/assets/images/category/react-native/2020/react-native-iap/in-app-purchases-insert-metadata.jpg)

上のような詳細ページへ移動したらアプリ内購入アイテムへ必要な情報を入力します。

- 購読期間(Subscription Duration)
- 購読価格(Subscription Prices)
- App Store情報(App Store Information)のローカリゼーション(Localizations)
- 審査情報

ここでApp store情報はアプリ内でも、アプリストアでも表示される名前と説明なので、注意して作成します。この名前と説明をアプリ中でreact-native-iapを使って取ってきますが、この内容をそのまま表示しないとRejectされる可能性があります。

私はRejectを避けるため、審査情報を詳しく作成しました。どうすれば、購入画面を見ることができるか、購入ページにはどんな内容が含めてあるかを作成しました。

– Title of publication or service
– Length of subscription (time period and/or content/services provided during each subscription period)
– Price of subscription, and price per unit if appropriate
– Payment will be charged to iTunes Account at confirmation of purchase
– Subscription automatically renews unless auto-renew is turned off at least 24-hours before the end of the current period
– Account will be charged for renewal within 24-hours prior to the end of the current period, and identify the cost of the renewal
– Subscriptions may be managed by the user and auto-renewal may be turned off by going to the user's Account Settings after purchase
– Links to Your Privacy Policy and Terms of Use
– Any unused portion of a free trial period, if offered, will be forfeited when the user purchases a subscription to that publication, where applicable

上の内容でRejectされるので上の内容が含まれているか、どこので確認できるかスクリンショットをと説明を使って詳しく作成しました。

#### iOSアプリ権限の設定

이제 앱내에서 앱 내 구입을 사용하기 위해서는 권한을 설정할 필요가 있습니다.

![in-app purchases insert metadata](/assets/images/category/react-native/2020/react-native-iap/xcode-in-app-purchase.jpg)

Xcode로 프로젝트를 열고 `Signing & Capbilities`에 `In-App PUrchase` 권한을 추가합니다.

{% include in-feed-ads.html %}

### 안드로이드 인앱 상품 생성

#### Payments 설정

인앱 상품으로 수익이 발생하면, 해당 수익을 입금받을 `Payments` 정보를 설정해야 합니다. Google Play Console에서 `설정`(Settings) > `개발자 계정`(Developer account) > `Payments 설정`(Payments settings)를 선택하여 `Payments` 정보를 설정합니다.

![Android Payments settings](/assets/images/category/react-native/2020/react-native-iap/android-payments-settings.jpg)

저는 Google Adsense를 연동하고 있었기 때문에, 특별한 설정없이, 사용중인 Payments 정보를 설정할 수 있었습니다.

#### 안드로이드 앱 권한 설정

안드로이드에 인앱 상품을 생성하기 위해 Google Play Console로 이동하고 설정하고 하는 앱을 선택한 후, 왼쪽의 `구독`(Subscriptions) 메뉴를 선택하면 다음과 같은 화면을 확인할 수 있습니다.

![android subscription](/assets/images/category/react-native/2020/react-native-iap/android-subscription-menu.jpg)

안드로이드에 인앱 상품을 생성하기 위해서는 `BILLING` 권한이 설정된 앱이 Google Play에 업로드해야 합니다. 우선 `android/app/src/main/AndroidManifest.xml` 파일을 열고 아래와 같이 `BILLING` 권한을 추가합니다.

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
  package="io.github.dev.yakuza.toeicwords">
  ...
  <uses-permission android:name="com.android.vending.BILLING"/>
  ...
  <application
      android:name=".MainApplication"
```

이렇게 권한을 설정하였다면, 일단 빌드하여 Google Play에 업로드 합니다.

![android subscription](/assets/images/category/react-native/2020/react-native-iap/android-after-uploading.jpg)

업로드를 완료하면 위와 같이 `구독`(Subscriptions) 메뉴가 바뀐 것을 확인할 수 있습니다.

#### 안드로이드 앱 내 구입 항목 생성

이제 `구독`(Subscriptions) 메뉴에서 `구독 만들기`(Create subscription) 버튼을 눌러 구독 항목을 생성합니다.

![android subscription](/assets/images/category/react-native/2020/react-native-iap/android-after-uploading.jpg)

그리고 구독 항목에 필요한 정보를 입력하여 구독 항목을 생성합니다.

- 제품 ID / Product ID
- 구독 세부정보(이름, 설명) / Subscription details(Name, Description)
- 가격(결제 기간, 기본 가격) / Price(Billing period, Default price)

iOS와 마찬가지로 `제품 ID`(Product ID)는 앱 내에서 결제할 때 사용하는 ID입니다. 저는 보통 iOS와 동일한 ID를 사용합니다. react-native-iap를 통해 구독 세부정보, 가격등을 가져올 수 있습니다. (이를 표시하지 않으면 리젝(reject)을 당하는지는 모르겠습니다만, 저는 이 정보를 iOS와 마찬가지로 표시합니다.)

{% include in-feed-ads.html %}

## 코딩

### react-native-iap 설치

다음 명령어를 사용하여 `react-native-iap`를 설치합니다.

```bash
npm install react-native-iap --save
```

그리고 다음 명령어를 사용하여 iOS에 연결합니다.

```bash
npx pod-install
```

### javascript

아래에 코드는 실제로 제가 사용하는 코드입니다.

```js
import React, { createContext, useState, useEffect, useCallback, useRef, useContext } from 'react';
import AsyncStorage from '@react-native-community/async-storage';
import {
  Alert,
  EmitterSubscription,
  Platform,
  Linking,
  ActivityIndicator,
  AppState,
} from 'react-native';
import Styled from 'styled-components/native';
import Icon from 'react-native-vector-icons/MaterialCommunityIcons';
import SplashScreen from 'react-native-splash-screen';

import ENV from '~/env';
import { ThemeContext } from '~/Context';
import { ActionSheet } from '~/Component';

import RNIap, {
  InAppPurchase,
  SubscriptionPurchase,
  finishTransaction,
  purchaseErrorListener,
  purchaseUpdatedListener,
  Subscription,
  PurchaseError,
} from 'react-native-iap';

import { checkReceipt } from './checkReceipt';

let purchaseUpdateSubscription: EmitterSubscription;
let purchaseErrorSubscription: EmitterSubscription;

const itemSubs = Platform.select({
  default: [ENV.subscriptionId],
});

const Container = Styled.View`
`;
const TitleContainer = Styled.View`
  justify-content: center;
  align-items: center;
  padding: 16px;
`;
const Title = Styled.Text`
  font-size: 16px;
  font-weight: bold;
  color: ${({ theme }: { theme: Theme }): string => theme.black};
`;
const SubTitle = Styled.Text`
  font-size: 16px;
  color: ${({ theme }: { theme: Theme }): string => theme.black};
`;
const DescriptionContainer = Styled.View`
  padding: 0 24px;
  width: 100%;
`;
const Description = Styled.Text`
  font-size: 14px;
  color: ${({ theme }: { theme: Theme }): string => theme.black};
`;
const PurchaseButton = Styled.TouchableOpacity`
  margin: 16px;
  padding: 16px;
  border-radius: 10px;
  background-color: ${({ theme }: { theme: Theme }): string => theme.black};
  justify-content: center;
  align-items: center;
`;
const PurchaseLabel = Styled.Text`
  color: ${({ theme }: { theme: Theme }): string => theme.white};
  font-size: 16px;
`;
const Terms = Styled.Text`
  font-size: 12px;
  color: ${({ theme }: { theme: Theme }): string => theme.black};
`;
const Link = Styled.Text`
  color: ${({ theme }: { theme: Theme }): string => theme.primary};
`;
const LoadingContainer = Styled.View`
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  justify-content: center;
  align-items: center;
`;
const LoadingBackground = Styled.View`
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: ${({ theme }: { theme: Theme }): string =>
    theme.isLightTheme ? theme.black : theme.white};
  opacity: 0.8;
`;

interface Props {
  children: JSX.Element | Array<JSX.Element>;
}

const IAPContext = createContext<IAPContext>({
  isSubscription: false,
  subscription: undefined,
  showPurchase: () => {},
});

const IAPProvider = ({ children }: Props): JSX.Element => {
  const [showLoading, setShowLoading] = useState<boolean>(false);
  const [isSubscription, setIsSubscription] = useState<boolean>(false);
  const [subscription, setSubscription] = useState<Subscription | undefined>(undefined);
  const actionSheetRef = useRef<ActionSheet>(null);
  const { theme } = useContext<ThemeContext>(ThemeContext);

  const showPurchase = () => {
    actionSheetRef.current?.open();
  };

  const _checkReceipt = async () => {
    const isValidated = await checkReceipt();

    setIsSubscription(isValidated);
    setTimeout(() => {
      SplashScreen.hide();
    }, 1000);
  };

  const _requestSubscription = () => {
    setShowLoading(true);
    if (subscription) {
      RNIap.requestSubscription(subscription.productId);
    }
  };

  const _restorePurchases = () => {
    setShowLoading(true);
    RNIap.getAvailablePurchases()
      .then((purchases) => {
        console.debug('restorePurchases');
        let receipt = purchases[0].transactionReceipt;
        if (Platform.OS === 'android' && purchases[0].purchaseToken) {
          receipt = purchases[0].purchaseToken;
        }
        AsyncStorage.setItem('receipt', receipt);
        setShowLoading(false);
        setIsSubscription(true);
        Alert.alert(
          ENV.language['restore successful'],
          ENV.language['you have successfully restored your purchase history'],
          [{ text: ENV.language['ok'], onPress: () => actionSheetRef.current?.close() }],
        );
      })
      .catch((err) => {
        console.debug('restorePurchases');
        console.error(err);
        setShowLoading(false);
        setIsSubscription(false);
        AsyncStorage.removeItem('receipt');
        Alert.alert(ENV.language['restore failed'], ENV.language['restore failed reason']);
      });
  };

  const _initIAP = useCallback(async (): Promise<void> => {
    RNIap.clearProductsIOS();

    try {
      const result = await RNIap.initConnection();
      await RNIap.flushFailedPurchasesCachedAsPendingAndroid();
      if (result === false) {
        Alert.alert(ENV.language["couldn't get in-app-purchase information"]);
        return;
      }
    } catch (err) {
      console.debug('initConnection');
      console.error(err.code, err.message);
      Alert.alert(ENV.language['fail to get in-app-purchase information']);
    }

    purchaseUpdateSubscription = purchaseUpdatedListener(
      (purchase: InAppPurchase | SubscriptionPurchase) => {
        console.debug('purchaseUpdatedListener');
        setShowLoading(false);
        setTimeout(() => {
          actionSheetRef.current?.close();
        }, 400);
        const receipt =
          Platform.OS === 'ios' ? purchase.transactionReceipt : purchase.purchaseToken;
        if (receipt) {
          finishTransaction(purchase)
            .then(() => {
              AsyncStorage.setItem('receipt', receipt);
              setIsSubscription(true);
            })
            .catch(() => {
              setIsSubscription(false);
              Alert.alert(
                ENV.language['purchase is failed'],
                ENV.language['the purchase is failed'],
              );
            });
        }
      },
    );

    purchaseErrorSubscription = purchaseErrorListener((error: PurchaseError) => {
      console.debug('purchaseErrorListener');
      console.error(error);
      setShowLoading(false);
      if (error.code !== 'E_USER_CANCELLED') {
        Alert.alert(ENV.language['purchase is failed'], ENV.language['the purchase is failed']);
      }
    });

    const subscriptions = await RNIap.getSubscriptions(itemSubs);
    setSubscription({
      ...subscriptions[0],
    });
  }, []);

  const handleAppStateChange = (nextAppState: string): void => {
    if (nextAppState === 'active') {
      _checkReceipt();
    }
  };

  useEffect(() => {
    // AsyncStorage.removeItem('receipt');
    _initIAP();
    _checkReceipt();
    AppState.addEventListener('change', handleAppStateChange);

    return (): void => {
      if (purchaseUpdateSubscription) {
        purchaseUpdateSubscription.remove();
      }
      if (purchaseErrorSubscription) {
        purchaseErrorSubscription.remove();
      }
      if (handleAppStateChange) {
        AppState.removeEventListener('change', handleAppStateChange);
      }
    };
  }, []);

  console.log(subscription);
  return (
    <IAPContext.Provider
      value={{
        isSubscription,
        subscription,
        showPurchase,
      }}>
      {children}
      <ActionSheet
        ref={actionSheetRef}
        height={Platform.OS === 'ios' ? 380 : 420}
        disableClose={showLoading}
        customStyles={{
          container: {
            backgroundColor: theme.white,
          },
        }}>
        {subscription && (
          <Container>
            <TitleContainer>
              <Title>{subscription.title.split(' (')[0]}</Title>
              <SubTitle>{subscription.description}</SubTitle>
            </TitleContainer>
            <DescriptionContainer>
              <Description>
                <Icon name="information-outline" />{' '}
                {
                  ENV.language[
                    "I'm developing the app alone. So your subscription is a great help to me"
                  ]
                }
              </Description>
              <Description>
                {'  '}
                {ENV.language['Your subscription helps me keep the good words app']}
              </Description>
              <Description>
                {'  '}
                {
                  ENV.language[
                    'Learn vocabulary without ads for the price of a cup of coffee each month'
                  ]
                }
              </Description>
            </DescriptionContainer>
            <PurchaseButton
              onPress={() => {
                _requestSubscription();
              }}>
              <PurchaseLabel>
                {subscription.localizedPrice} / {ENV.language['month']}
              </PurchaseLabel>
            </PurchaseButton>
            <DescriptionContainer>
              <Terms>
                - {ENV.language['Already subscribed?']}{' '}
                <Link onPress={() => _restorePurchases()}>
                  {ENV.language['Restoring purchases']}
                </Link>
              </Terms>
              <Terms>- {ENV.language['cancel the purchase']}</Terms>
              {Platform.OS === 'ios' && (
                <Terms>- {ENV.language['payment is charged to your iTunes account']}</Terms>
              )}
              <Terms>
                - {ENV.language['If you have any question,']}{' '}
                <Link onPress={() => Linking.openURL('https://dev-yakuza.posstree.com/ko/contact/')}>
                  Contact
                </Link>{' '}
                {ENV.language['us']}
              </Terms>
              <Terms>
                - {ENV.language['see the']}
                <Link onPress={() => Linking.openURL('https://dev-yakuza.posstree.com/privacy/ko/')}>
                  {ENV.language['terms of use']}
                </Link>{' '}
                {ENV.language['details']}
              </Terms>
            </DescriptionContainer>
          </Container>
        )}
        {showLoading && (
          <LoadingContainer>
            <LoadingBackground />
            <ActivityIndicator color={theme.primary} size="large" />
          </LoadingContainer>
        )}
      </ActionSheet>
    </IAPContext.Provider>
  );
};

export { IAPProvider, IAPContext };
```

위에 소스 코드는 제 프로젝트에 의존되는 부분들이 많기 때문에 그대로 사용하실 수 없습니다. 또한 저는 결제 로직을 Context API를 사용하여 구현하였습니다. 위에 코드를 하나하나 살펴보면서 결제 로직을 어떻게 만드는지 확인해 봅시다.

우선 결제 로직의 큰 흐름은 `초기화`, `결제`, `결제 확인`, `복원`으로 나눌 수 있습니다.

{% include in-feed-ads.html %}

#### 초기화

인앱 결제를 위해서는 우선 라이브러리를 초기화하고, 구독 상품의 정보를 가져올 필요가 있습니다.

```js
...
const itemSubs = Platform.select({
  default: [ENV.subscriptionId],
});
...
const IAPProvider = ({ children }: Props): JSX.Element => {
  ...
  const _initIAP = useCallback(async (): Promise<void> => {
    RNIap.clearProductsIOS();

    try {
      const result = await RNIap.initConnection();
      await RNIap.flushFailedPurchasesCachedAsPendingAndroid();
      if (result === false) {
        Alert.alert(ENV.language["couldn't get in-app-purchase information"]);
        return;
      }
    } catch (err) {
      console.debug('initConnection');
      console.error(err.code, err.message);
      Alert.alert(ENV.language['fail to get in-app-purchase information']);
    }
    ...
    const subscriptions = await RNIap.getSubscriptions(itemSubs);
    setSubscription({
      ...subscriptions[0],
    });
  }, []);
  ...
  useEffect(() => {
    _initIAP();
    ...
  }, []);

  return (
    ...
  );
};
...
```

라이브러리를 초기화하기 위해서는 아래와 같은 코드를 사용합니다.

```js
RNIap.clearProductsIOS();

try {
  const result = await RNIap.initConnection();
  await RNIap.flushFailedPurchasesCachedAsPendingAndroid();
  if (result === false) {
    Alert.alert(ENV.language["couldn't get in-app-purchase information"]);
    return;
  }
} catch (err) {
  console.debug('initConnection');
  console.error(err.code, err.message);
  Alert.alert(ENV.language['fail to get in-app-purchase information']);
}
```

위에서 `clearProductsIOS`와 `flushFailedPurchasesCachedAsPendingAndroid`같이 플랫폼에 의존하는 코드가 있지만 굳이 `Platform.OS`를 사용하여 로직을 분리할 필요없습니다.

그리고 구독 상품의 정보를 가져오기 위해서는 상품 ID를 설정할 필요가 있습니다.

```js
const itemSubs = Platform.select({
  default: [ENV.subscriptionId],
});
```

저는 iOS와 안드로이드 모두 같은 ID를 사용하기 때문에 하나로 사용했지만, 만약 iOS와 안드로이드가 다른 경우는 아래와 같이 설정할 수 있습니다.

```js
const itemSubs = Platform.select({
  ios: [ENV.subscriptionId],
  android: [ENV.subscriptionId],
});
```

이렇게 설정한 상품 ID를 사용하여 상품의 정보를 가져옵니다.

```js
const subscriptions = await RNIap.getSubscriptions(itemSubs);
setSubscription({
  ...subscriptions[0],
});
```

그리고 가져온 정보를 `state`에 저장합니다. 저의 경우는 하나의 구독 상품만을 사용하기 때문에 `subscriptions[0]`로 첫번째 상품만을 설정하였습니다.

이렇게 가져온 정보를 아래와 같이 화면에 표시합니다.

```jsx
...
<Title>{subscription.title.split(' (')[0]}</Title>
<SubTitle>{subscription.description}</SubTitle>
...
<PurchaseLabel>
  {subscription.localizedPrice} / {ENV.language['month']}
</PurchaseLabel>
...
```

{% include in-feed-ads.html %}

#### 결제

다음은 가져온 상품 정보를 사용하여 실제 결제를 실행하는 부분입니다.

```js
...
let purchaseUpdateSubscription: EmitterSubscription;
let purchaseErrorSubscription: EmitterSubscription;
...
const IAPProvider = ({ children }: Props): JSX.Element => {
  ...
  const _requestSubscription = () => {
    setShowLoading(true);
    if (subscription) {
      RNIap.requestSubscription(subscription.productId);
    }
  };
  ...
  const _initIAP = useCallback(async (): Promise<void> => {
    ...
    purchaseUpdateSubscription = purchaseUpdatedListener(
      (purchase: InAppPurchase | SubscriptionPurchase) => {
       ...
        const receipt =
          Platform.OS === 'ios' ? purchase.transactionReceipt : purchase.purchaseToken;
        if (receipt) {
          finishTransaction(purchase)
            .then(() => {
              AsyncStorage.setItem('receipt', receipt);
              setIsSubscription(true);
            })
            .catch(() => {
              setIsSubscription(false);
              Alert.alert(
                ENV.language['purchase is failed'],
                ENV.language['the purchase is failed'],
              );
            });
        }
      },
    );

    purchaseErrorSubscription = purchaseErrorListener((error: PurchaseError) => {
      console.debug('purchaseErrorListener');
      console.error(error);
      setShowLoading(false);
      if (error.code !== 'E_USER_CANCELLED') {
        Alert.alert(ENV.language['purchase is failed'], ENV.language['the purchase is failed']);
      }
    });
    ...
  }, []);
  ...

  useEffect(() => {
    ...
    return (): void => {
      if (purchaseUpdateSubscription) {
        purchaseUpdateSubscription.remove();
      }
      if (purchaseErrorSubscription) {
        purchaseErrorSubscription.remove();
      }
      ...
    };
  }, []);
  ...
};
...
```

실제 결제가 이루어진 후, 결제 성공 여부와 실패 여부를 전달 받기 위해서, 리스너(Listener)를 등록할 필요가 있습니다.

```js
...
let purchaseUpdateSubscription: EmitterSubscription;
let purchaseErrorSubscription: EmitterSubscription;
...
purchaseUpdateSubscription = purchaseUpdatedListener(
  (purchase: InAppPurchase | SubscriptionPurchase) => {
    ...
    const receipt =
      Platform.OS === 'ios' ? purchase.transactionReceipt : purchase.purchaseToken;
    if (receipt) {
      finishTransaction(purchase)
        .then(() => {
          AsyncStorage.setItem('receipt', receipt);
          setIsSubscription(true);
        })
        .catch(() => {
          setIsSubscription(false);
          Alert.alert(
            ENV.language['purchase is failed'],
            ENV.language['the purchase is failed'],
          );
        });
    }
  },
);

purchaseErrorSubscription = purchaseErrorListener((error: PurchaseError) => {
  ...
});
...
useEffect(() => {
  ...
  return (): void => {
    if (purchaseUpdateSubscription) {
      purchaseUpdateSubscription.remove();
    }
    if (purchaseErrorSubscription) {
      purchaseErrorSubscription.remove();
    }
    ...
  };
}, []);
...
```

결제 성공시에는 `purchaseUpdatedListener`이 호출되며 `finishTransaction`을 사용하여 결제가 잘 이루어졌음을 알림니다. 결제가 실패하였을 때는 `purchaseErrorListener`가 호출되며 사용자에게 결제가 실패되었음을 알림니다.

또한 `useEffect`을 사용하여 컴포넌트가 `Unmount`될 때, 리스너(Listener)를 제거합니다.

이제 위에서 정의한 `_requestSubscription` 함수를 결제 버튼과 연결합니다.

```jsx
<PurchaseButton
  onPress={() => {
    _requestSubscription();
  }}>
  <PurchaseLabel>
    {subscription.localizedPrice} / {ENV.language['month']}
  </PurchaseLabel>
</PurchaseButton>
```

{% include in-feed-ads.html %}

#### 결제 확인

결제가 성공했다면, 이에 대한 결과값을 받아 올 수 있습니다. 이렇게 받아온 결과가 제대로된 결과인지 확인(Validate)할 필요가 있습니다. iOS는 앱 자제체에서, 서버에서 확인이 가능하며, 안드로이드는 서버를 통해서 확인이 가능합니다.

저는 서버를 가지고 있지 않기 때문에, iOS는 앱 자체 검증으로, 안드로이드는 검증을 하지 않고, 결제 정보를 한번 더 가져옴으로써 결제를 확인하였습니다.

iOS는 `validateReceiptIos`을 사용하여 앱 자체에서 검증이 가능합니다. 우선 `getReceiptIOS`으로 현제 영수증(Receipt)을 가져오고 그 영수증(Receipt)이 유효한지 `validateReceiptIos`을 통해 확인합니다.

```js
const checkReceiptIOS = async () => {
  let isValidated = false;
  const receipt = await AsyncStorage.getItem('receipt');
  if (receipt) {
    const newReceipt = await getReceiptIOS();
    const validated = await validateReceiptIos(
      {
        'receipt-data': newReceipt,
        password: '****************',
      },
      __DEV__,
    );

    if (validated !== false && validated.status === 0) {
      isValidated = true;
      AsyncStorage.setItem('receipt', newReceipt);
    } else {
      isValidated = false;
      AsyncStorage.removeItem('receipt');
    }
  }
  return isValidated;
};
```

위와 같이 `validateReceiptIos`을 통해 영수증을 검증할때, `password`가 필요합니다. 이 `password`는 `Appstore connect`의 `공유 암호(Shared secret)`입니다.

공유 암호(Shared secret)를 발급받기 위해서는 Appstore connect로 이동한 후 `사용자 및 액세스`(Users and Access)로 이동합니다.

![ios shared secret](/assets/images/category/react-native/2020/react-native-iap/ios-shared-secret.jpg)

상단에 `공유 암호(Shared secret)`를 선택하고 공유 암호를 생성합니다. 여기서 발급한 공유 암호는 모든 앱에서 사용이 가능합니다. 특정 앱에만 한정한 공유 암호를 생성할 수도 있습니다.

![ios app shared secret](/assets/images/category/react-native/2020/react-native-iap/ios-app-shared-secret.jpg)

특정 앱에서만 사용 가능한 공유 암호를 생성하기 위해서는 공유 암호를 생성하고자 하는 앱으로 이동 한 후, `앱 내 구입`(In-App Purchases)의 `관리`(Manage)로 이동합니다. 그럼 오른쪽에 `앱 공유 암호`(App-Specific Shared Secret)을 통해 특정 앱에서만 사용 가능한 공유 암호를 생성할 수 있습니다.

안드로이드는 [validateReceiptAndroid](https://github.com/dooboolab/react-native-iap#with-google-play){:rel="nofollow noreferrer" target="_blank"}을 통해 확인이 가능합니다. 하지만 `accessToken`을 발급받기 위해서는 서버가 필요합니다.

```js
const checkReceiptAndroid = async () => {
  let isValidated = false;
  const receipt = await AsyncStorage.getItem('receipt');
  if (receipt) {
    try {
      const purchases = await RNIap.getAvailablePurchases();
      console.debug('checkReceiptAndroid');
      let receipt = purchases[0].transactionReceipt;
      if (Platform.OS === 'android' && purchases[0].purchaseToken) {
        receipt = purchases[0].purchaseToken;
      }
      AsyncStorage.setItem('receipt', receipt);
      isValidated = true;
    } catch (error) {
      isValidated = false;
      AsyncStorage.removeItem('receipt');
    }
  }
  return isValidated;
};
```

저는 서버를 사용하지 않기 때문에, `getAvailablePurchases`을 통해 상품 정보를 가져와 정보가 있으면 유용한 사용자라고 판단하도록 했습니다.

{% include in-feed-ads.html %}

#### 복원

결제를 한 사용자가 앱을 지우거나 어떤 문제가 있어 결제 연결이 해제된 경우, `getAvailablePurchases`을 통해 결제를 복원할 수 있습니다.

```js
const _restorePurchases = () => {
  setShowLoading(true);
  RNIap.getAvailablePurchases()
    .then((purchases) => {
      console.debug('restorePurchases');
      let receipt = purchases[0].transactionReceipt;
      if (Platform.OS === 'android' && purchases[0].purchaseToken) {
        receipt = purchases[0].purchaseToken;
      }
      AsyncStorage.setItem('receipt', receipt);
      setShowLoading(false);
      setIsSubscription(true);
      Alert.alert(
        ENV.language['restore successful'],
        ENV.language['you have successfully restored your purchase history'],
        [{ text: ENV.language['ok'], onPress: () => actionSheetRef.current?.close() }],
      );
    })
    .catch((err) => {
      console.debug('restorePurchases');
      console.error(err);
      setShowLoading(false);
      setIsSubscription(false);
      AsyncStorage.removeItem('receipt');
      Alert.alert(ENV.language['restore failed'], ENV.language['restore failed reason']);
    });
};
```

iOS에서는 결제 복원 기능을 지원하지 않으면, 리젝(Reject)될 수 있으므로 꼭 구현해 주어야 합니다.

```jsx
<Link onPress={() => _restorePurchases()}>
  {ENV.language['Restoring purchases']}
</Link>
```

이렇게 만든 함수를 결제 복원 버튼과 연결합니다.

## 테스트

### iOS

#### iOS 테스트 계정 등록

iOS에서 테스트를 위해서는 `애플 계정으로 사용한 적이 없는 email`이 필요합니다. 그리고 Appstore connect로 이동한 후, `사용자 및 액세스`(Users and Access)로 이동합니다.

![ios sandbox tester](/assets/images/category/react-native/2020/react-native-iap/ios-sandbox-testers.jpg)

그리고 왼쪽 하단에 있는 `Sandbox`의 `테스터`(Testers)를 선택하고 준비한 email로 Sandbox 계정을 생성합니다.

#### iOS 테스트

시뮬레이터에서는 인앱 결제 테스트를 할 수 없습니다. 개발한 앱을 디바이스에서 테스트해야 합니다.

일단, App store에서 실제로 사용하고 있는 계정을 로그아웃합니다.

그 이후, 결발중인 앱을 디바이스에서 실행하고, 결제 버튼을 선택합니다. 결제가 진행될 때, 위에서 만든 Sandbox 계정을 사용하여 로그인 하여 결제합니다.

{% include in-feed-ads.html %}

### 안드로이드

#### 안드로이드 테스트 계정 등록

안드로이드는 iOS와 달리 구글에서 사용하는 계정을 그대로 사용할 수 있습니다. Google Play Console로 이동한 후, `설정`(Settings) > `라이선스 테스트`(License testing)을 선택합니다.

![android license testing](/assets/images/category/react-native/2020/react-native-iap/android-license-testing.jpg)

그리고 사용하고 있는 구글 계정을 입력하여 추가합니다.

#### 안드로이드 테스트

안드로이드도 iOS와 마찬가지로 에뮬레이터에서 테스트를 할 수 없습니다. iOS와는 다르게 실제 사용하는 계정으로 테스트 할 수 있으므로 특별히 로그아웃을 할 필요는 없습니다.

안드로이드는 갱신 기간 테스트와 구독이 완료되었을 경우를 테스트할 수 있습니다. 갱신 기간에 관해서는 공식 사이트를 참고하시기 바랍니다.

- [Android in-app test period](https://developer.android.com/google/play/billing/test#renewals){:rel="nofollow noreferrer" target="_blank"}

{% include in-feed-ads.html %}

## 배포

### iOS 배포

인앱 결제를 포함한 앱을 배포하시기 위해서는 앱을 배포할 때 `앱 내 구입`(In-App Purchases) 항목을 설정해야 합니다.

![in-app purchases deployment](/assets/images/category/react-native/2020/react-native-iap/in-app-purchases-deployment.jpg)

### 안드로이드 배포

안드로이드는 iOS와 다르게 특별한 설정없이 앱을 배포하시면 됩니다.

## 완료

이것으로 react-native-iap를 사용하여 인앱 결제를 구현하는 방법에 대해서 알아보았습니다. 모든 내용을 한 블로그에 담으려다보니 블로그가 많이 길어졌습니다.

그리고 저는 제가 해본 경험을 공유하다보니 인앱 결제중에서도 자동 갱신 구독에 관해서만 작성하였네요. 일반 상품 구매등은 조금 다르므로 위에 로직을 참고해서 구현하시기 바랍니다.
