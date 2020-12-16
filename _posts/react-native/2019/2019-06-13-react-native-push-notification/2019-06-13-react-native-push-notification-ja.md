---
layout: 'post'
permalink: '/react-native/react-native-push-notification/'
paginate_path: '/react-native/:num/react-native-push-notification/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'Local Push Notificatoin'
description: 'react-native-push-notificationライブラリを使ってLocal Push Notification, つまりアプリ(App)自体からお知らせを送る方法について説明します。'
image: '/assets/images/category/react-native/2019/react-native-push-notification/background.jpg'
---

<div id="contents_list" markdown="1">

1. [概要](#概要)
1. [ライブラリインストール](#ライブラリインストール)
    - [0.60以上ライブラリリンク](#060以上ライブラリリンク)
    - [0.59以下ライブラリリンク](#059以下ライブラリリンク)
1. [アンドロイド権限設定](#アンドロイド権限設定)
1. [react-native-push-notificationの使い方](#react-native-push-notificationの使い方)
1. [アプリ(App)に適用する](#アプリappに適用する)
1. [アンドロイドのic_launcherアイコン](#アンドロイドのic_launcherアイコン)
1. [確認](#確認)
1. [問題点](#問題点)
1. [完了](#完了)

</div>

## 概要

一人で開発した単語勉強アプリがダウンロードは多くなりましたが、DAU(Daily Active User, アクティブユーザー)がそんなに多くないことを見つけました。それでDAU(Daily Active User, アクティブユーザー)を上げるためメッセージ送信(Push Notification)を適用することにしました。しかし、貧乏な開発者なので、サーバーを利用するメッセージ送信(Push Notification)じゃなくアプリ(App)自体からメッセージを送信する方法(Local Push Notification)で実装することにしました。ここで紹介する方法が適用された私のアプリです。もし、興味がある方はダウンロードして見てください。

- 일본어 단어 공부, 일단 공부: [https://dev-yakuza.posstree.com/app/ildangongbu/]( https://dev-yakuza.posstree.com/app/ildangongbu/){:target="_blank"}
- 韓国語単語勉強、カンタン勉強: [https://dev-yakuza.posstree.com/app/kantanbenkyo/]( https://dev-yakuza.posstree.com/app/kantanbenkyo/){:target="_blank"}
- TOPIK単語勉強、TOPIK単語1/2: [https://dev-yakuza.posstree.com/app/topik12/]( https://dev-yakuza.posstree.com/app/topik12/){:target="_blank"}
- TOPIK単語勉強、TOPIK単語3/4: [https://dev-yakuza.posstree.com/app/topik34/]( https://dev-yakuza.posstree.com/app/topik34/){:target="_blank"}
- TOPIK単語勉強、TOPIK単語5/6: [https://dev-yakuza.posstree.com/app/topik56/]( https://dev-yakuza.posstree.com/app/topik56/){:target="_blank"}

このブログポストでは`react-native-push-notification`のライブラリを使ってアプリ(App)自体からメッセージを送信する方法(Local Push Notification)について説明します。

- react-native-push-notification: [https://github.com/zo0r/react-native-push-notification](https://github.com/zo0r/react-native-push-notification){:rel="nofollow noreferrer" target="_blank"}

## ライブラリインストール

下記のコマンドで`react-native-push-notification`のライブラリをインストールします。

```bash
npm install --save react-native-push-notification
```

### 0.60以上ライブラリリンク

下記のコマンドで`react-native-push-notification`を使うため追加ライブラリをインストールします。

```bash
npm install --save @react-native-community/push-notification-ios
```

そして下記のコマンドでインストールした`@react-native-community/push-notification-ios`ライブラリをリンクします。

```bash
react-native link @react-native-community/push-notification-ios
```

最後に、下記のコマンドを実行します。

```bash
cd ios
pod install
cd ..
```

### 0.59以下ライブラリリンク

下記のコマンドで`react-native-push-notification`のライブラリを連結(Link)します。

```bash
react-native link react-native-push-notification
```

上の実行したコマンドの結果を見たら分かると思いますが、アンドロイド(Android)だけ連結(Link)されました。

```bash
info Linking "react-native-push-notification" Android dependency
info Android module "react-native-push-notification" has been successfully linked
```

iOSは下記のリンクを参考して進める必要があります。

- iOS manual Installation: [https://facebook.github.io/react-native/docs/linking-libraries-ios#manual-linking](https://facebook.github.io/react-native/docs/linking-libraries-ios#manual-linking){:rel="nofollow noreferrer" target="_blank"}

まず、`/ios/[project-name].xcworkspace`や`/ios/[project-name].xcodeproj`を実行してxcodeを起動します。

![react-native-push-notificationライブラリiOS連結(link)](/assets/images/category/react-native/2019/react-native-push-notification/add-library.jpg)

上のように`node_modules/react-native/libraries/PushNotificationIOS/RCTPushNotification.xcodeproj`をxcodeのプロジェクト名下の`libraries`にドラックして追加します。注意点はnode_modulesのreact-native-push-notificationではなく`react-native`です。

次は下記のように`プロジェクト名 > Build Phases > Link Binary with Libraries`を選択します。

![react-native-push-notificationライブラリiOS連結(link) - build phases](/assets/images/category/react-native/2019/react-native-push-notification/build-phases.jpg)

下にある`+`ボタンを押して`Push`で検索します。検索結果にある`libRCTPushNotification.a`を選択して`Add`を押して追加します。

![react-native-push-notificationライブラリiOS連結(link) - build phasesへライブラリ追加](/assets/images/category/react-native/2019/react-native-push-notification/add-library-to-build-phases.jpg)

{% include in-feed-ads.html %}

## アンドロイド権限設定

アンドロイドでlocal push messageを使うためには、`./android/app/src/main/AndroidManifest.xml`ファイルを開いて下記のように修正します。

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
  package="CHANGE YOUR INFO!!">
    ...
    <uses-permission android:name="android.permission.VIBRATE" />
    <uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED"/>

    <application
      android:name=".MainApplication"
      android:label="@string/app_name"
      android:icon="@mipmap/ic_launcher"
      android:allowBackup="false"
      android:theme="@style/AppTheme">

      <meta-data  android:name="com.dieam.reactnativepushnotification.notification_channel_name"
            android:value="CHANGE YOUR INFO!!"/>
      <meta-data  android:name="com.dieam.reactnativepushnotification.notification_channel_description"
                  android:value="CHANGE YOUR INFO!!"/>
      <receiver android:name="com.dieam.reactnativepushnotification.modules.RNPushNotificationPublisher" />
      <receiver android:name="com.dieam.reactnativepushnotification.modules.RNPushNotificationBootEventReceiver">
          <intent-filter>
              <action android:name="android.intent.action.BOOT_COMPLETED" />
          </intent-filter>
      </receiver>
      <service android:name="com.dieam.reactnativepushnotification.modules.RNPushNotificationRegistrationService"/>
      <service
          android:name="com.dieam.reactnativepushnotification.modules.RNPushNotificationListenerService"
          android:exported="false" >
          <intent-filter>
              <action android:name="com.google.firebase.MESSAGING_EVENT" />
          </intent-filter>
      </service>

      <activity
        android:name=".MainActivity"
      ...
</manifest>
```

上記のように修正したら、`CHANGE YOUR INFO!!`の部分へ自分の情報を入力します。私は3つ、全てPacakage IDで変更して使っています。

## react-native-push-notificationの使い方

下記のコードは実際私が使ってるコードです。

```js
import { AppState, PushNotificationIOS } from 'react-native';
import PushNotification from 'react-native-push-notification';

const _handleAppStateChange = nextAppState => {
  if (nextAppState === 'active') {
    _registerLocalNotification();
  }
};

const _registerLocalNotification = () => {
  PushNotification.setApplicationIconBadgeNumber(0);
  PushNotification.cancelAllLocalNotifications();

  const messages = [
    'ちょっと時間を作って韓国語を勉強するのはどうですか?',
    '今日韓国語は勉強しましたか?',
    '韓国語の単語を勉強しましょう',
    '単語の勉強は毎日毎日するのが重要です。',
    '新しい単語や暗記した単語を復習してみてください。',
    '韓国語を勉強する時間です。',
    'テスト機能であなたの実力を試してみてください。',
    '韓国語単語たちがあなたを待っています。',
    '韓国語、難しくないです。勉強して見ましょう。',
    '韓国語マスターになるため！',
  ];
  const message = messages[Math.floor(Math.random() * messages.length)];

  let nextHour = new Date();
  nextHour.setDate(nextHour.getDate() + 1);
  nextHour.setHours(nextHour.getHours() - 1);


  PushNotification.localNotificationSchedule({
    /* Android Only Properties */
    vibrate: true,
    vibration: 300,
    priority: 'hight',
    visibility: 'public',
    importance: 'hight',

    /* iOS and Android properties */
    message, // (required)
    playSound: false,
    number: 1,
    actions: '["OK"]',

    // for production
    repeatType: 'day', // (optional) Repeating interval. Check 'Repeating Notifications' section for more info.
    date: nextHour,

    // test to trigger each miniute
    // repeatType: 'minute',
    // date: new Date(Date.now()),

    // test to trigger one time
    // date: new Date(Date.now() + 20 * 1000),
  });
};
export default {
  register: async () => {
    PushNotification.configure({
      onNotification: function(notification) {
        notification.finish(PushNotificationIOS.FetchResult.NoData);
      },
      popInitialNotification: true,
    });

    _registerLocalNotification();

    AppState.addEventListener('change', _handleAppStateChange);
  },
  unregister: () => {
    AppState.removeEventListener('change', _handleAppStateChange);
  },
};
```

一つずつ詳しく見て見ましょう。

```js
import PushNotification from 'react-native-push-notification';
...
export default {
  register: () => {
    PushNotification.configure({
      onNotification: function(notification) {
        notification.finish(PushNotificationIOS.FetchResult.NoData);
      },
      popInitialNotification: true,
    });
    _registerLocalNotification();
    ...
  },
  ...
};
```

まず、このソースコードをモジュール化しました。`register()`のファンクションを実行すると`PushNotification`を初期化してアプリ(App)自体お知らせ(Local Push Notification)を登録するファンクションを呼びます。

```js
const _registerLocalNotification = () => {
  PushNotification.setApplicationIconBadgeNumber(0);
  PushNotification.cancelAllLocalNotifications();

  const messages = [
    ...
  ];
  const message = messages[Math.floor(Math.random() * messages.length)];

  let nextHour = new Date();
  nextHour.setDate(nextHour.getDate() + 1);
  nextHour.setHours(nextHour.getHours() - 1);


  PushNotification.localNotificationSchedule({
    /* Android Only Properties */
    vibrate: true,
    vibration: 300,
    priority: 'hight',
    visibility: 'public',
    importance: 'hight',

    /* iOS and Android properties */
    message, // (required)
    playSound: false,
    number: 1,
    actions: '["OK"]',

    // for production
    repeatType: 'day', // (optional) Repeating interval. Check 'Repeating Notifications' section for more info.
    date: nextHour,

    // test to trigger each miniute
    // repeatType: 'minute',
    // date: new Date(Date.now()),

    // test to trigger one time
    // date: new Date(Date.now() + 20 * 1000),
  });
};
```

アプリ(App)自体お知らせ(Local Push Notification)を登録するため`_registerLocalNotification`のファンクションを実行すると、

```js
PushNotification.setApplicationIconBadgeNumber(0);
PushNotification.cancelAllLocalNotifications();
```

バッジ(Badge)を初期化して、既存に登録したお知らせ(Notification)を全て無くします。既存のお知らせ(Notification)を無くした理由はアプリを実行するたびに登録をして重複されて同じメッセージが発信される問題がありました。AsyncStorageを使ってコントロールするかとも思いましたが、ただ全てを無くして新しく登録する方法を採用しました。

```js
...
const messages = [
...
];
const message = messages[Math.floor(Math.random() * messages.length)];

let nextHour = new Date();
nextHour.setDate(nextHour.getDate() + 1);
nextHour.setHours(nextHour.getHours() - 1);
...
```

お知らせのメッセージをランダムで表示するため変数と、アプリ(App)が実装された時間を基準に次の日同じ時間より１時間早くお知らせを送るように設定しました。

```js
PushNotification.localNotificationSchedule({
    /* Android Only Properties */
    vibrate: true,
    vibration: 300,
    priority: 'hight',
    visibility: 'public',
    importance: 'hight',

    /* iOS and Android properties */
    message, // (required)
    playSound: false,
    number: 1,
    actions: '["OK"]',

    // for production
    repeatType: 'day', // (optional) Repeating interval. Check 'Repeating Notifications' section for more info.
    date: nextHour,

    // test to trigger each miniute
    // repeatType: 'minute',
    // date: new Date(Date.now()),

    // test to trigger one time
    // date: new Date(Date.now() + 20 * 1000),
});
```

アプリ自体お知らせ(Local Push Notification)を登録します。色んなオプションがあります。下記のリンクを参考してください。

- [https://github.com/zo0r/react-native-push-notification#local-notifications](https://github.com/zo0r/react-native-push-notification#local-notifications){:rel="nofollow noreferrer" target="_blank"}

私は本番(Production)では

```js
repeatType: 'day', // (optional) Repeating interval. Check 'Repeating Notifications' section for more info.
date: nextHour,
```

毎日、最後に起動した時間より1時間早くメッセージ(Local Push Notification)を表示するようにしました。テストする時は、

```js
// test to trigger one time
date: new Date(Date.now() + 20 * 1000),
```

20秒後メッセージ(Local Push Notification)を表示するようにするか

```js
// test to trigger each miniute
repeatType: 'minute',
date: new Date(Date.now()),
```

今から毎分、メッセージを表示してテストしました。

```js
import { AppState, PushNotificationIOS } from 'react-native';
...
const _handleAppStateChange = nextAppState => {
  if (nextAppState === 'active') {
    _registerLocalNotification();
  }
};
...
export default {
  register: async () => {
   ...
    AppState.addEventListener('change', _handleAppStateChange);
  },
  unregister: () => {
    AppState.removeEventListener('change', _handleAppStateChange);
  },
};
```

AppStateを使ってアプリ(App)がバックグラウンド(Background)から戻ってくる時、アクティブ(Active)になる時をチェックしてアプリ(App)内部お知らせ機能(Local Push Notification)を再登録するようにしました。このようにした理由はアプリのメッセージ(Local Push Notification)をランダムに表示するためです。

{% include in-feed-ads.html %}

## アプリ(App)に適用する

上で作ったモジュール化したアプリ(App)内部お知らせ機能(Local Push Notification)を使うためアプリ(App)が実行される時必ず実行されるコンポーネント(Component)に下記のように使っています。

```js
...
import LocalNotification from '~/Util/LocalNotification';
...
export default class LevelScreen extends React.Component<Props, State> {
    ...
    componentWillUnmount() {
        LocalNotification.unregister();
        ...
    }
    componentDidMount() {
        LocalNotification.register();
        ...
    }
}
```

## アンドロイドのic_launcherアイコン

アンドロイド(Android)のお知らせ(Push Notification)を見ると左上に小さいアイコンが表示されることが確認できます。このアイコンを作るため`generator-rn-toolbox`を使いました。

- generator-rn-toolbox: [https://github.com/bamlab/generator-rn-toolbox/blob/master/generators/assets/README.md#generate-android-notification-icons](https://github.com/bamlab/generator-rn-toolbox/blob/master/generators/assets/README.md#generate-android-notification-icons){:rel="nofollow noreferrer" target="_blank"}

96x96 pxサイズのpngファイルを作って下記のサイズでこのイメージがic_launcherとしてうまく表示されるか確認します。

- icons-notification: [http://romannurik.github.io/AndroidAssetStudio/icons-notification.html#source.type=image&source.space.trim=0&source.space.pad=-0.1&name=ic_stat_ic_notification](http://romannurik.github.io/AndroidAssetStudio/icons-notification.html#source.type=image&source.space.trim=0&source.space.pad=-0.1&name=ic_stat_ic_notification){:rel="nofollow noreferrer" target="_blank"}

最後に、下記のコマンドでic_launcherアイコンを生成します。

```bash
yo rn-toolbox:assets --android-notification-icon icon.jpg
```

generator-rn-toolboxのインストールや使い方については以前のブログポストを参考してください。

- [App icon]({{site.url}}/{{page.categories}}/app-icon/){:target="_blank"}
- [Splashイメージ]({{site.url}}/{{page.categories}}/splash-image/){:target="_blank"}

## 確認

確認のためアプリ(App)内部お知らせ機能(Local Push Notification)を登録する時、下記のオプションを使いました。

```js
repeatType: 'minute',
date: new Date(Date.now()),
```

アプリ(App)を実行して、アプリ(App)を無効化(終了やバックグラウンド)すると、1分後下記のようにメッセージ(Local Push Notification)が表示されることが確認できます。

![react-native-push-notification アプリ(App)内部お知らせ機能(Local Push Notification)確認](/assets/images/category/react-native/2019/react-native-push-notification/local-push-notification.jpg)

アプリ(App)を必ず実行する必要があることとアプリ(App)を無効化する必要があることを注意してください。

## 問題点

アプリ(App)を実行する時、アプリ(App)内部お知らせ(Local Push Notification)が登録されます。この時メッセージも一緒に登録されますが、アプリ(App)を再起動させてアプリ(App)内部お知らせ(Local Push Notification)を再登録しないといつも同じメッセージが表示されます。

もっと色んなメッセージを表示したいですが、アプリ(App)を再起動しないユーザーにはいつも同じメッセージが見える不便さがあります。

## 完了

結構いいライブラリと思います。アプリ(App)内部メッセージ以外も外部メッセージ(Push Notification)も処理することができるみたいです。後でこの貧乏をだ脱出すると、サーバーを使ってメッセージ(Push Notification)も実装して見たいですね。

また, この機能でDAU(Daily Active User, アクティブユーザー)が上がるかイライラさせてアプリ(App)を削除することになるかもうちょっと見てみる必要があります。
