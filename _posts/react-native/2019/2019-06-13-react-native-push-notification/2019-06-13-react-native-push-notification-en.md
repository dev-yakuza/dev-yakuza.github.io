---
layout: 'post'
permalink: '/react-native/react-native-push-notification/'
paginate_path: '/react-native/:num/react-native-push-notification/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'Local Push Notificatoin'
description: let's see how to implement Local Push Notification by using react-native-push-notification.
image: '/assets/images/category/react-native/2019/react-native-push-notification/background.jpg'
---

<div id="contents_list" markdown="1">

1. [Outline](#outline)
1. [Install Library](#install-library)
    - [Link the library upper 0.60](#link-the-library-upper-060)
    - [Link the library under 0.59](#link-the-library-under-059)
1. [Configure Android Permmisions](#configure-android-permmisions)
1. [How To Use react-native-push-notification](#how-to-use-react-native-push-notification)
1. [Apply To The App](#apply-to-the-app)
1. [Android ic_launcher icon](#android-ic_launcher-icon)
1. [Check](#check)
1. [Problem](#problem)
1. [Completed](#completed)

</div>

## Outline

my applications what I've developed alone are downloaded more than before, but DAU(Daily Active User) is not changed big. so I try to implement Push Notification to increase DAU(Daily Active User). however I am a poor developer. so I can't impelment Serverside Push Notification instead of Local Push Notification. the list below is my applications what I implement Local Push Notification.(sorry, it only supports Korean and Japanese) if you have any interested, please download it and see the demonstration.

- 일본어 단어 공부, 일단 공부: [https://dev-yakuza.posstree.com/app/ildangongbu/]( https://dev-yakuza.posstree.com/app/ildangongbu/){:target="_blank"}
- 韓国語単語勉強、カンタン勉強: [https://dev-yakuza.posstree.com/app/kantanbenkyo/]( https://dev-yakuza.posstree.com/app/kantanbenkyo/){:target="_blank"}
- TOPIK単語勉強、TOPIK単語1/2: [https://dev-yakuza.posstree.com/app/topik12/]( https://dev-yakuza.posstree.com/app/topik12/){:target="_blank"}
- TOPIK単語勉強、TOPIK単語3/4: [https://dev-yakuza.posstree.com/app/topik34/]( https://dev-yakuza.posstree.com/app/topik34/){:target="_blank"}
- TOPIK単語勉強、TOPIK単語5/6: [https://dev-yakuza.posstree.com/app/topik56/]( https://dev-yakuza.posstree.com/app/topik56/){:target="_blank"}

in this blog post, we'll see how to implement Local Push Notification by using `react-native-push-notification` library.

- react-native-push-notification: [https://github.com/zo0r/react-native-push-notification](https://github.com/zo0r/react-native-push-notification){:rel="nofollow noreferrer" target="_blank"}

## Install Library

execute the command below to install `react-native-push-notification` library.

```bash
npm install --save react-native-push-notification
```

### Link the library upper 0.60

Execute the command below to install an additional library to use `react-native-push-notification`.

```bash
npm install --save @react-native-community/push-notification-ios
```

And then, execute the command below to link `@react-native-community/push-notification-ios` library.

```bash
react-native link @react-native-community/push-notification-ios
```

Lastly, execute the command below.

```bash
cd ios
pod install
cd ..
```

### Link the library under 0.59

execute the command below to link `react-native-push-notification` library to the App.

```bash
react-native link react-native-push-notification
```

as you can see the result of the command above, it only links on Android.

```bash
info Linking "react-native-push-notification" Android dependency
info Android module "react-native-push-notification" has been successfully linked
```

we should link by following the link below.

- iOS manual Installation: [https://facebook.github.io/react-native/docs/linking-libraries-ios#manual-linking](https://facebook.github.io/react-native/docs/linking-libraries-ios#manual-linking){:rel="nofollow noreferrer" target="_blank"}

first, execute `/ios/[project-name].xcworkspace` or `/ios/[project-name].xcodeproj` to start xcode.

![link react-native-push-notification library on iOS](/assets/images/category/react-native/2019/react-native-push-notification/add-library.jpg)

drag `node_modules/react-native/libraries/PushNotificationIOS/RCTPushNotification.xcodeproj` to `libraries` on the botto of the project name in xcode. be careful. you should use `react-native` in node_moduels not react-native-push-notification.

next, click `project name > Build Phases > Link Binary with Libraries`.

![link react-native-push-notification library - build phases](/assets/images/category/react-native/2019/react-native-push-notification/build-phases.jpg)

click `+` button on the bottom and search `Push`. select `libRCTPushNotification.a` in the search result and click `Add` to add it.

![link react-native-push-notification library on iOS - add library in build phases](/assets/images/category/react-native/2019/react-native-push-notification/add-library-to-build-phases.jpg)

{% include in-feed-ads.html %}

## Configure Android Permmisions

open `./android/app/src/main/AndroidManifest.xml` file and modify it like below to use Local Push Message.

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

after modifying, you should change `CHANGE YOUR INFO!!` to your information. In my case, I changed three of them to Package ID.

## How To Use react-native-push-notification

the code below is what I use for my applications.

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
    '잠깐 시간내서 일본어 공부를 해보는건 어떨까요?',
    '오늘 일본어 공부하셨나요?',
    '일본어 단어를 공부해 보세요.',
    '단어 공부는 매일매일 하는 것이 중요해요.',
    '새로운 단어와 암기한 공부를 복습해 보세요.',
    '일본어를 공부할 시간이에요.',
    '테스트 기능을 사용해서 자신의 실력을 확인해 보세요.',
    '일본어 단어들이 당신을 기다리고 있어요.',
    '일본어, 어렵지 않아요. 공부해 봅시다.',
    '일본어 마스터가 되기위해!',
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

let's see more details.

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

first, I've modularized this source code to use on many applications. when `register()` function is executed, `PushNotification` is initialized and then, call the function that registers Local Push Notification.

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

when `_registerLocalNotification` is called to register Local Push Notification,

```js
PushNotification.setApplicationIconBadgeNumber(0);
PushNotification.cancelAllLocalNotifications();
```

initialize Badge, and remove all Notifications registered before. why I cancel all Notifications, Local Push Notification is registered every times when the app is executed and that makes duplicate messages. I thought to use AsyncStorage to solve it, but I choose to delete all and register again.

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

the variables for making random message and for sending a message on tomorrow at one hour earlier than now.

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

retister Local Push Notification. there are many options. you can see all options on the link below.

- [https://github.com/zo0r/react-native-push-notification#local-notifications](https://github.com/zo0r/react-native-push-notification#local-notifications){:rel="nofollow noreferrer" target="_blank"}

in my case, if my app is in Production,

```js
repeatType: 'day', // (optional) Repeating interval. Check 'Repeating Notifications' section for more info.
date: nextHour,
```

show Local Push Notification at 1 hour earlier on every day. for the test,

```js
// test to trigger one time
date: new Date(Date.now() + 20 * 1000),
```

trigger Local Push Notification one time after 20 seconds or,

```js
// test to trigger each miniute
repeatType: 'minute',
date: new Date(Date.now()),
```

trigger at every minutes for testing.

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

I check the app going to the background or in-activate by using AppState, and if the app is activated again, Local Push Notification is registered again. it's for making random Local Push Notification message.

{% include in-feed-ads.html %}

## Apply To The App

we need to implement Local Push Notification module that we created above on the screen component that is always used when the app is executed like below.

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

## Android ic_launcher icon

you can see small icon on the left top of the Push Notification message on Android. I used `generator-rn-toolbox` to make this icon.

- generator-rn-toolbox: [https://github.com/bamlab/generator-rn-toolbox/blob/master/generators/assets/README.md#generate-android-notification-icons](https://github.com/bamlab/generator-rn-toolbox/blob/master/generators/assets/README.md#generate-android-notification-icons){:rel="nofollow noreferrer" target="_blank"}

create 96x96 px size png file and check the file can be ic_launcher on the site below.

- icons-notification: [http://romannurik.github.io/AndroidAssetStudio/icons-notification.html#source.type=image&source.space.trim=0&source.space.pad=-0.1&name=ic_stat_ic_notification](http://romannurik.github.io/AndroidAssetStudio/icons-notification.html#source.type=image&source.space.trim=0&source.space.pad=-0.1&name=ic_stat_ic_notification){:rel="nofollow noreferrer" target="_blank"}

lastly, execute the command below to create iclauncher icon.

```bash
yo rn-toolbox:assets --android-notification-icon icon.jpg
```

if you want to know how to install generator-rn-toolbox and how to use it, see the previous blog posts.

- [App icon]({{site.url}}/{{page.categories}}/app-icon/){:target="_blank"}
- [Splash image]({{site.url}}/{{page.categories}}/splash-image/){:target="_blank"}

## Check

for checking, use the option below to register Local Push Notification in the app.

```js
repeatType: 'minute',
date: new Date(Date.now()),
```

execute the app and make the app in-activate(exit or background). you can see Local Push Notification message like below after 1 minitue.

![check Local Push Notification with react-native-push-notification ](/assets/images/category/react-native/2019/react-native-push-notification/local-push-notification.jpg)

be careful. you should execute the app and make it in-activate to show the message.

## Problem

when the app is executed, Local Push Notification is registered. in this time, the message is also registered, so if user doesn't execute the app again to re-register Local Push Notification, the message will be always same.

I hope random messages are displayed, but if user doesn't execute the app, maybe the same message makes user annoyed.

## Completed

I think react-native-push-notification library is awesome. you can also control Serverside Push Notification with this library. if I become a rich developer, I will try to impelment Serverside Push Notification with react-native-push-notification library.

also, I will check Local Push Notification increases DAU(Daily Active User) or makes users annoyed and they delete the app.
