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

左下の`アプリ内課金`(In-App Purcahses)の`管理`(Manage)を選択してプラスボタン(`+`)を押すと、上のように追加する商品を選ぶ画面がでます。

私は私のアプリへ`自動更新購読`(Auto-Renewable Subscription)を追加し他ので、`自動更新購読`を中心に説明します。他の商品を追加することになると、このブログポストへ追加します。

![in-app purchases reference name and product id](/assets/images/category/react-native/2020/react-native-iap/in-app-purchases-reference-name-product-id.jpg)

ここで`識別情報`(Reference Name)はAppstore connectだけ表示される名前なので、自分が分かりやすい名前に設定します。`商品ID`(Product ID)はアプリ中でアプリ内商品を取ってくる時、使います。

![in-app purchases group name](/assets/images/category/react-native/2020/react-native-iap/in-app-purchases-group-name.jpg)

その後、`購読グループ識別情報`(Subscription Group Reference Name)を入力します。`識別情報`(Reference Name)と同じように、Appstore connect中だけ表示されるので、自分が分かりやすい名前を設定します。

#### アプリ内課金メタデータを入力する

上のようにアプリ中購入アイテムを生成したら、次はアプリ中購入アイテムのメタデータを入力する必要があります。

![in-app purchases metadata](/assets/images/category/react-native/2020/react-native-iap/in-app-purchases-metadata.jpg)

左メニューでまた、`アプリ内課金`(In-App Purchases)の`管理`(Manage)を押すと上のようにメタデータ(Metadata)が入力されてないことが確認できます。ここで、識別情報の名前を選択して当該項目の詳細ページへ移動します。

![in-app purchases insert metadata](/assets/images/category/react-native/2020/react-native-iap/in-app-purchases-insert-metadata.jpg)

上のような詳細ページへ移動したらアプリ内課金アイテムへ必要な情報を入力します。

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

次はアプリ内でアプリ内課金を使うため必要な権限を設定する必要があります。

![in-app purchases insert metadata](/assets/images/category/react-native/2020/react-native-iap/xcode-in-app-purchase.jpg)

Xcodeでプロジェクトを開いて`Signing & Capbilities`へ`In-App PUrchase`の権限を追加します。

{% include in-feed-ads.html %}

### アンドロイドのアプリ内商品生成

#### Payments設定

アプリ内課金で収入が発生すると、その収入が入金される`Payments`の情報を設定する必要があります。Google Play Consoleで`設定`(Settings) > `開発者アカウント`(Developer account) > `Payments設定`(Payments settings)を選択して`Payments`情報を設定します。

![Android Payments settings](/assets/images/category/react-native/2020/react-native-iap/android-payments-settings.jpg)

私はGoogle Adsenseを連動してるので、設定したPayments情報を使うことができました。

#### アンドロイドのアプリ権限設定

アンドロイドでアプリ内課金を生成するためGoogle Play Consoleへ移動したいアプリを選択して、左の`購読`(Subscriptions)メニューを選択したら下記のような画面が確認できます。

![android subscription](/assets/images/category/react-native/2020/react-native-iap/android-subscription-menu.jpg)

アンドロイドでアプリ内課金を生成するためには`BILLING`の権限が設定されたアプリがGoogle Playへアップロードする必要があります。まず、`android/app/src/main/AndroidManifest.xml`のファイルを開いて下記のように`BILLING`の権限を追加します。

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
  package="io.github.dev.yakuza.toeicwords">
  ...
  <uses-permission android:name="com.android.vending.BILLING"/>
  ...
  <application
      android:name=".MainApplication"
```

このように権限を設定して、ビルドしてGoogle Playへアップロードします。

![android subscription](/assets/images/category/react-native/2020/react-native-iap/android-after-uploading.jpg)

アップロードが完了されると上のように`購読`(Subscriptions)メニューが変わったことが確認できます。

#### アンドロイドでアプリ内課金アイテムを生成する

次は`購読`(Subscriptions)メニューで`購読生成`(Create subscription)ボタンを押して購読アイテムを生成します。
이제 `구독`(Subscriptions) 메뉴에서 `구독 만들기`(Create subscription) 버튼을 눌러 구독 항목을 생성합니다.

![android subscription](/assets/images/category/react-native/2020/react-native-iap/android-after-uploading.jpg)

そして購読アイテムへ必要な情報を入力して購読アイテムを生成します。

- 商品ID / Product ID
- 購読詳細情報(名前、説明) / Subscription details(Name, Description)
- 金額(決済期間、基本金額) / Price(Billing period, Default price)

iOSと同じように`商品ID`(Product ID)はアプリ内課金で使うIDです。私は普通、iOSと同じIDを使います。react-native-iapを使って購読の詳細情報、金額などを取ってくる時使います。(これを表示しない場合Rejectとされるかどうかは知らないですが、私はこの情報をiOSと同じように表示してます。)

{% include in-feed-ads.html %}

## コーディング

### react-native-iapのインストール

次のコマンドを使って`react-native-iap`をインストールします。

```bash
npm install react-native-iap --save
```

そして次のコマンドを使ってiOSへ必要なライブラリをインストールします。

```bash
npx pod-install
```

### JavaScript

下記のコードは実際、私が使ってるコードです。

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

上のソースコードは私のプロジェクトへ依存してる部分が多いなので、そのまま使うことはできません。また、私の決済ロジックはContext APIを使って実装しました。上のコードを一つづつ見て、決済ロジックをどう作ったか確認しましょう。

まず、決済ロジックの大きい流れは`初期化`, `決済`, `決済確認`, `復元`で分かれています。

{% include in-feed-ads.html %}

#### 初期化

アプリ内課金をするためにはまず、ライブラリを初期化して、購読商品の情報を取ってくる必要があります。

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

ライブラリを初期化するためには下記のようなコードを使います。

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

上のコードで`clearProductsIOS`と`flushFailedPurchasesCachedAsPendingAndroid`ようにプラットフォームに依存してるコードがありますが、あえて`Platform.OS`を使ってロジックを分離する必要はありません。

そして購読商品の情報を取ってくるため、商品のIDを設定する必要があります。

```js
const itemSubs = Platform.select({
  default: [ENV.subscriptionId],
});
```

私はiOSもとアンドロイドも同じIDを使うので、一つを使いましたが、もしiOSとアンドロイドのIDが違う場合は下記のように設定することができます。

```js
const itemSubs = Platform.select({
  ios: [ENV.subscriptionId],
  android: [ENV.subscriptionId],
});
```

このように設定した商品のIDを使って商品の情報を取ってきます。

```js
const subscriptions = await RNIap.getSubscriptions(itemSubs);
setSubscription({
  ...subscriptions[0],
});
```

そして取ってきた情報を`state`へ保存します。私の場合は一つの購読商品しかないので`subscriptions[0]`で最初の商品だけ設定しました。

このように取ってきた情報を下記のように画面に表示します。

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

#### 決済

次は取ってきた情報を使って実際決済するところの部分です。

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

実際決済が実行されると、決済の成功/失敗の結果を貰うため、リスナー(Listener)を登録する必要があります。

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

決済が成功したら`purchaseUpdatedListener`が実行されて`finishTransaction`を使って決済が成功したかを教えてくれます。決済が失敗するときは`purchaseErrorListener`が実行されてユーザに決済が失敗したことをお知らせします。

また、`useEffect`を使ってコンポーネントが`Unmount`される時、リスター(Listener)を消します。

次は上で定義した`_requestSubscription`関数を決済ボタンと連結します。

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

#### 決済確認

決済が成功したら、これに関する結果を貰えます。このように貰った結果が本当のものかどうかを確認(Validate)する必要があります。iOSはアプリ中またはサーバで確認ができます。アンドロイドはサーバを使って確認ができます。

私はサーバを持ってないので、iOSはアプリ中で、アンドロイドは検証しなくて、決済情報をもう一度取ってくることで決済の結果を確認しました。

iOSは`validateReceiptIos`を使ってアプリで検証ができます。まず、`getReceiptIOS`で現在の領収書(Receipt)を取ってきて、その領収書(Receipt)が有効かどうか`validateReceiptIos`を使って確認します。

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

上のように`validateReceiptIos`を使って領収書を検証する時、`password`が必要です。この`password`は`Appstore connect`の`共有パスワード(Shared secret)`です。

共有パスワードを発行するためにはAppstore connectへ移動して`ユーザやアクセス`(Users and Access)へ移動します。

![ios shared secret](/assets/images/category/react-native/2020/react-native-iap/ios-shared-secret.jpg)

上にある`共有パスワード(Shared secret)`を選択して共有パスワードを作ります。ここで発行した共有パスワードは全てのアプリで使うことができます。特定なアプリだけ使いたい場合は次のように共有パスワードを作ることもできます。

![ios app shared secret](/assets/images/category/react-native/2020/react-native-iap/ios-app-shared-secret.jpg)

特定したアプリたけ使える共有パスワードを作りたい場合は共有パスワードを作りたいアプリへ移動した後、`アプリ内課金`(In-App Purchases)の`管理`(Manage)へ移動します。そしたら右の方に`アプリ共有パスワード`(App-Specific Shared Secret)を使って特定したアプリだけ使う共有パスワードを生成することがdきます。

アンドロイドは[validateReceiptAndroid](https://github.com/dooboolab/react-native-iap#with-google-play){:rel="nofollow noreferrer" target="_blank"}を使って確認できますが、`accessToken`を発行するにはサーバが必要です。

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

私はサーバがないので、`getAvailablePurchases`を使って商品の情報を取ってきて情報があったら有効なユーザと判断してます。

{% include in-feed-ads.html %}

#### 復元

決済をしたユーザがアプリを削除したりなんかの問題で決済連結が切れった場合、`getAvailablePurchases`を使って決済を復元することができます。

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

iOSではこの決済復元の機能がないと、Rejectされるので必ず実装する必要があります。

```jsx
<Link onPress={() => _restorePurchases()}>
  {ENV.language['Restoring purchases']}
</Link>
```

このように作った関数を決済復元ボタンと連結します。

## テスト

### iOS

#### iOSテストアカウント登録

iOSでテストするためには`アップルアカウントで使ったことがないEmail`が必要です。そしてAppstore connectへ移動して、`ユーザやアクセス`(Users and Access)へ移動します。

![ios sandbox tester](/assets/images/category/react-native/2020/react-native-iap/ios-sandbox-testers.jpg)

ここで左下にある`Sandbox`の`テスター`(Testers)を選択して用意したEmailでSandboxアカウントを作ります。

#### iOSテスト

シミュレータではアプリ内課金テストができません。開発したアプリをデバイスでテストする必要があります。

一旦、App storeで実際使ってるアカウントをログアウトします。

その後、開発してるアプリをデバイスで実行して、決済ボタンを押します。決済が進むと、上で作ったSandboxアカウントを使ってログインして決済をします。

{% include in-feed-ads.html %}

### アンドロイド

#### アンドロイドテストアカウント登録

アンドロイドはiOSとは違ってGoogleで使ってるアカウントをそのまま使えます。Google Play Consoleへ移動して、`設定`(Settings) > `ライセンステスト`(License testing)を選択します。

![android license testing](/assets/images/category/react-native/2020/react-native-iap/android-license-testing.jpg)

そして使ってるGoogleアカウントを入力して追加します。

#### アンドロイドテスト

アンドロイドもiOSと同じようにエミュレータではテストができません。iOSとは違って実際つかてるアカウントでテストができるので、特にログアウトする必要はありません。

アンドロイドは更新期間テストと購読期間が終わった場合のテストができます。更新期間については公式サイトを参考してください。

- [Android in-app test period](https://developer.android.com/google/play/billing/test#renewals){:rel="nofollow noreferrer" target="_blank"}

{% include in-feed-ads.html %}

## デプロイ

### iOSのデプロイ

アプリ内課金を含めてアプリをデプロイするためにはアプリをデプロイする時`アプリ内課金`(In-App Purchases)項目を設定する必要があります。

![in-app purchases deployment](/assets/images/category/react-native/2020/react-native-iap/in-app-purchases-deployment.jpg)

### アンドロイドのデプロイ

アンドロイドはiOSとは違って特に設定をする必要はありません。

## 完了

これでreact-native-iapを使ってアプリ内課金を実装する方法について見てみました。全ての内容を一つのブログへまとめたので、ブログの内容が長くなりました。

それで私は私が経験した内容だけ共有してるのでアプリ内課金中でも自動更新購読に関して作成しました。一般商品課金などは少し違うので上のロジックを参考して実装してください。
