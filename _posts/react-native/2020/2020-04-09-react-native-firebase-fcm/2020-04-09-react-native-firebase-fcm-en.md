---
layout: 'post'
permalink: '/react-native/react-native-firebase-fcm/'
paginate_path: '/react-native/:num/react-native-firebase-fcm/'
lang: 'en'
categories: 'react-native'
comments: true

title: Push message via react-native-firebase(V5)
description: Let's see how to use FCM(Firebase Cloud Messaging) via react-native-firebase(V5) to implement Push message on React Native.
image: '/assets/images/category/react-native/2020/react-native-firebase-fcm/background.jpg'
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [Install library](#install-library)
- [Link library](#link-library)
  - [Over 0.60 version](#over-060-version)
  - [Under 0.59 version](#under-059-version)
- [Create Firebase project](#create-firebase-project)
- [iOS settings](#ios-settings)
- [Configure iOS project on Firebase](#configure-ios-project-on-firebase)
  - [Configure Permissions](#configure-permissions)
  - [APNS setting](#apns-setting)
- [Android settings](#android-settings)
  - [Modify Android package name](#modify-android-package-name)
- [Configure Android proejt on Firbase](#configure-android-proejt-on-firbase)
- [Test](#test)
- [Add Javascript source code](#add-javascript-source-code)
  - [iOS test](#ios-test)
  - [Android test](#android-test)
- [Completed](#completed)

</div>

## Outline

The app developed by React Native is also a normal app, so it can receive a Push message. In this blog post, I will show you how to use `FCM(Firebase Cloud Messaging)` via `react-native-firebase(V5)` library to revceive a Push message on React Native.

- react-native-firebase v5: [https://v5.rnfirebase.io/](https://v5.rnfirebase.io/){:rel="nofollow noreferrer" target="_blank"}
- FCM(Firebase Cloud Messaging): [https://firebase.google.com/docs/cloud-messaging](https://firebase.google.com/docs/cloud-messaging){:rel="nofollow noreferrer" target="_blank"}

## Install library

Execute the command below to install react-native-firebase library.

```bash
npm install --save react-native-firebase
```

## Link library

We need to link react-native-firebase library to use it.

### Over 0.60 version

Execute the command below to link react-native-firebase library to React Native project.

```bash
cd ios
pod install
cd ..
```

### Under 0.59 version

Execute the command below to link react-native-firebase library to React Native project.

```bash
react-native link react-native-firebase
```

{% include in-feed-ads.html %}

## Create Firebase project

Next, we need to create a project on Google Firebase. Click the link below to go to Google Firebase.

- Google Firebase: [https://firebase.google.com](https://firebase.google.com){:rel="nofollow noreferrer" target="_blank"}

![google firebase](/assets/images/category/react-native/2020/react-native-firebase-fcm/google-firebase.jpg)

Click the `SIGN IN` button on the right top to login.

![google firebase after login](/assets/images/category/react-native/2020/react-native-firebase-fcm/google-firebase-after-login.jpg)

After login, click the `GO TO CONSOLE` button on the right tope to go to Google Firebase Console.

![google firebase console](/assets/images/category/react-native/2020/react-native-firebase-fcm/google-firebase-console.jpg)

On Google Firebase Console, click `+ Add project` to add a new project.

![google firebase console add project](/assets/images/category/react-native/2020/react-native-firebase-fcm/google-firebase-console-add-project.jpg)

After inserting the project information, click the `Create project` button to create the project.

{% include in-feed-ads.html %}

## iOS settings

Let's see how to configure react-native-firebase for iOS.

## Configure iOS project on Firebase

When you click the project on Google Firebase Console, you can see the screen like below.

![google firebase console project](/assets/images/category/react-native/2020/react-native-firebase-fcm/google-firebase-console-project.jpg)

click the `iOS` button on the center to go to iOS configuration.

![google firebase console project ios](/assets/images/category/react-native/2020/react-native-firebase-fcm/google-firebase-console-project-ios.jpg)

Insert Bundle ID of the app, and click `Register app` button

![GoogleService-Info.plist download](/assets/images/category/react-native/2020/react-native-firebase-fcm/googleservice-info-plist-download.jpg)

Download `GoogleService-Info.plist` file which is created by Google Firebase, and move it to the same location of `info.plist` file. after adding `GoogleService-Info.plist` file, click `Next` button.

![add Firebase SDK](/assets/images/category/react-native/2020/react-native-firebase-fcm/add-firebase-sdk.jpg)

We need to add Google Firebase SDK to React Native poject like above.

If you use React Native under 0.59 version, execute the command below.

```bash
pod init
```

To add Google Firebase SDK, modify `./ios/Podfile` file like below.

```ruby
target 'blaboo' do
  ...
  pod 'Firebase/Core'
  pod 'Firebase/Analytics' // if you use Analytics
  pod 'Firebase/Messaging'
  ...
end
```

Install Google Firebase SDK.

```bash
pod install
# pod update
```

![edit appdelegate.m for firebase](/assets/images/category/react-native/2020/react-native-firebase-fcm/edit-appdelegate.jpg)

Open `AppDelegate.m` file on React Native porject, and modify it like below,

```js
...
@import Firebase;
#import "RNFirebaseNotifications.h"
...
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
  [FIRApp configure];
  [RNFirebaseNotifications configure];
  ...
  return YES;
}
...
```

To initialize Google Firebase SDK.

![connect firebase to app](/assets/images/category/react-native/2020/react-native-firebase-fcm/connect-firebase-to-app.jpg)

At this part, I clicked `Skip this step` to skip this section.

### Configure Permissions

To configure the permissions, open `ios/[project name].xcworkspace` file to execute Xcode.

After executing the Xcode, click the proejct on the left menu, and click the `Signing & Capabilities` tab.

![react native firebase analytics](/assets/images/category/react-native/2020/react-native-firebase-fcm/ios-fcm-capability.jpg)

click `+Capabilty` on the top. Search and add the permissions below.

- Push Notifications
- Background modes

When you add Background modes, you can see the checkbox list unlike Push Notifications permmision. Select `Remote notifications` in the list.

{% include in-feed-ads.html %}

### APNS setting

We need to configure `APNS(Apple Push Notification Service)` to use Push message on iOS.

open `Keychain Access` on macOS. And the, click `Keychain Access` > `Certificate Assistant` > `Request a Certificate From a Certificate Authority...` menu.

![APNS(Apple Push Notification Service) - request a certificate from a certicate authority](/assets/images/category/react-native/2020/react-native-firebase-fcm/request_a_certificate_from_a_certicate_authority.jpg)

If the screen blow is shown up, insert `User Email Address` and `Common Name`, and select `Saved to disk`. After it, click `Continue` button to go to the next.

![APNS(Apple Push Notification Service) - request a certificate from a certicate authority insert information](/assets/images/category/react-native/2020/react-native-firebase-fcm/request_a_certificate_from_a_certicate_authority_insert_information.jpg)

When you see the screen like below, select the folder which you want to save the file, and click `Save` button to save it.

![APNS(Apple Push Notification Service) - request a certificate from a certicate authority save certification](/assets/images/category/react-native/2020/react-native-firebase-fcm/request_a_certificate_from_a_certicate_authority_save_certification.jpg)

Next, go to [https://developer.apple.com/](https://developer.apple.com/){:rel="nofollow noreferrer" target="_blank"} site.

![APNS(Apple Push Notification Service) - apple developer site](/assets/images/category/react-native/2020/react-native-firebase-fcm/apple_developer_site.jpg)

click the `Account` menu on the right top, and login. If you see the screen like below, click `Certificates, Identifiers & Profiles` menu.

![APNS(Apple Push Notification Service) - apple developer site Certificates, Identifiers & Profiles](/assets/images/category/react-native/2020/react-native-firebase-fcm/certificates_identifieers_profiles.jpg)

When you see the screen like below, click `Certificates` menu and click `+` button on the top.

![APNS(Apple Push Notification Service) - Certificates, Identifiers & Profiles Add Certificates](/assets/images/category/react-native/2020/react-native-firebase-fcm/certificates_identifieers_profiles_add_certificates.jpg)

Next, when `Create a New Certificate` is shown up, scroll it to go down. When you scroll down, you can find `Apple Push Notification service SSL (Sandbox & Production)` on `Service` section. Select it, and click `Continue` button on the right top to go to the next.

![APNS(Apple Push Notification Service) - Certificates, Identifiers & Profiles Apple push notification service](/assets/images/category/react-native/2020/react-native-firebase-fcm/apple_push_notification_service_ssl.jpg)

When you see the screen like below, select the app which you want to implement FCM feature, and click `Continue` button to go to the next.

![APNS(Apple Push Notification Service) - Certificates, Identifiers & Profiles Apple push notification service](/assets/images/category/react-native/2020/react-native-firebase-fcm/select_app_id.jpg)

When you see the screen like below, click `Choose File` and select the file which you've made via Keychain. After selecting, click `Continue` button.

![APNS(Apple Push Notification Service) - Certificates, Identifiers & Profiles Apple push notification service](/assets/images/category/react-native/2020/react-native-firebase-fcm/select_app_id.jpg)

If you see the screen like below, you made a certification well. Click `Download` button on the right top to download the certification.

![APNS(Apple Push Notification Service) - Certificates, Identifiers & Profiles Apple push notification service](/assets/images/category/react-native/2020/react-native-firebase-fcm/download_your_certificate.jpg)

We need to transform this certification to `.p12` format. Double-click the certification to register it to Keychain.

![APNS(Apple Push Notification Service) - generate .p12](/assets/images/category/react-native/2020/react-native-firebase-fcm/generate_p12_file.jpg)

Right-click the registered certification, select `Export "Apple Push Services: package name"...` menu.

![APNS(Apple Push Notification Service) - generate .p12 export](/assets/images/category/react-native/2020/react-native-firebase-fcm/generate_p12_file_export.jpg)

When the screen above is shown up, select `Personal Information Exchange (.p12)` on `File Format` and click `Save` button to save the file.

![APNS(Apple Push Notification Service) - generate .p12 insert password](/assets/images/category/react-native/2020/react-native-firebase-fcm/generate_p12_file_insert_password.jpg)

We need to insert a password to save p12 file like above. Insert the password to save .p12 file.

Next, go to [Firebase Console](https://console.firebase.google.com/){:rel="nofollow noreferrer" target="_blank"}, and click the project which we've made above. After it, you can see the `iOS` project on the right side.

![APNS(Apple Push Notification Service) - Firebase Console select ios](/assets/images/category/react-native/2020/react-native-firebase-fcm/firebase_console_select_ios.jpg)

Click the iOS project, and click the configuration icon to go to the iOS project setting screen. Click `Cloud Messaging` menu on the iOS setting screen.

![APNS(Apple Push Notification Service) - Firebase Console cloud messaging](/assets/images/category/react-native/2020/react-native-firebase-fcm/firebase_console_cloud_messaging.jpg)

You can see the `APNs certificates` on `iOS app configuration` section on the bottom. Click `Upload` button on `No development APNs certificate` and `No production APNs certificate`.

![APNS(Apple Push Notification Service) - Firebase Console upload p12 file](/assets/images/category/react-native/2020/react-native-firebase-fcm/firebase_console_upload_p12_file.jpg)

When this screen is shown up, upload `.p12` file, and insert the password which you made `.p12` file.

![APNS(Apple Push Notification Service) - Firebase Console finish settings](/assets/images/category/react-native/2020/react-native-firebase-fcm/firebase_console_finish.jpg)

We've done all configurations for APNS(Apple Push Notification Service).

{% include in-feed-ads.html %}

## Android settings

Next, let's see how to configure Anddroid to use react-native-firebase.

### Modify Android package name

- Modify `android/app/BUCK` file on React Native project like below.

  ```xml
  ...
  android_build_config(
      ...
      package = "package_name",
  )
  ...
  android_resource(
      ...
      package = "package_name",
      ...
  )
  ...
  ```

- Modify `android/app/src/main/AndroidManifest.xml` file on React Native project like below.

  ```xml
  <manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="package_name">
  ...
  ```

- Modify `android/app/src/main/java/com/ProjectName/MainActivity.java` file on React Native project like below.

  ```java
  package package_name;
  ...
  ```

- Modify `android/app/src/main/java/com/ProjectName/MainApplication.java` file on React Native project like below.

  ```java
  package package_name;
  ...
  ```

- Modify `android/app/build.gradle` file on React Native project like below.

  ```java
  ...
  defaultConfig {
      applicationId package_name
      ...
  }
  ...
  ```

{% include in-feed-ads.html %}

## Configure Android proejt on Firbase

Click `Project Overview` on left top of the Google Firebase Console.

![Google Firebase Console Project Overview](/assets/images/category/react-native/2020/react-native-firebase-fcm/firebase-project-overview.jpg)

Click `+ Add app` > `Android icon` to go to the Android project setting.

![Google Firebase Android app register](/assets/images/category/react-native/2020/react-native-firebase-fcm/register-android.jpg)

Insert Android Package Name, and click `REgister app` button.

![Google Firebase google-services.json setting](/assets/images/category/react-native/2020/react-native-firebase-fcm/set-google-services-json.jpg)

Copy `google-services.json` file which Google Firebase generates to `android/app` folder on React Native project. And then, click `Next` button to go to the next.

![Google Firebase setting on android](/assets/images/category/react-native/2020/react-native-firebase-fcm/setting-android.jpg)

Open `android/build.gradle` file on React Native project and modify it like below.

```js
buildscript {
  repositories {
    google()
    jcenter()
  }
  dependencies {
    classpath("com.android.tools.build:gradle:3.4.2")
    classpath 'com.google.gms:google-services:4.3.3'
  }
}
...
allprojects {
  repositories {
    mavenLocal()
    google()
    jcenter()
    ...
  }
}
```

As you see above, `google()` should be in `repositories` and be defined above `jcenter()`.

Open `android/app/build.gradle` file and modify it like below.

```js
dependencies {
    // under 59 version
    // implementation project(':react-native-firebase')
    ...
    implementation 'com.google.android.gms:play-services-base:17.2.1'
    implementation 'com.google.firebase:firebase-core:17.0.0'
    implementation "com.google.firebase:firebase-messaging:20.0.0"
    implementation 'me.leolin:ShortcutBadger:1.1.21@aar'
}
```

And the, add the code below to the bottom of the same file.

```js
...
apply plugin: 'com.google.gms.google-services'
```

Next, Open `./android/build.gradle` file and modify it like below.

```js
buildscript {
    ext {
        ...
    }
    repositories {
        ...
    }
    dependencies {
        classpath("com.android.tools.build:gradle:3.4.2")
        classpath 'com.google.gms:google-services:4.3.3'
    }
}
```

- Over 0.60 version

To use react-native-firebase, open `android/app/src/main/java/com/[app name]/MainApplication.java` file and modify it like below.

```java
import io.invertase.firebase.RNFirebasePackage;
import io.invertase.firebase.analytics.RNFirebaseAnalyticsPackage;
import io.invertase.firebase.messaging.RNFirebaseMessagingPackage;
import io.invertase.firebase.notifications.RNFirebaseNotificationsPackage;
...
@Override
protected List<ReactPackage> getPackages() {
  @SuppressWarnings("UnnecessaryLocalVariable")
  List<ReactPackage> packages = new PackageList(this).getPackages();
  // Packages that cannot be autolinked yet can be added manually here, for example:
  // packages.add(new MyReactNativePackage());
  packages.add(new RNFirebaseAnalyticsPackage());
  packages.add(new RNFirebaseMessagingPackage());
  packages.add(new RNFirebaseNotificationsPackage());
  return packages;
}
...
```

- Under 0.59 version

To use react-native-firebase, open `android/app/src/main/java/com/[app name]/MainApplication.java` file and modify it like below.

```java
import io.invertase.firebase.RNFirebasePackage;
import io.invertase.firebase.analytics.RNFirebaseAnalyticsPackage;
import io.invertase.firebase.messaging.RNFirebaseMessagingPackage;
...

@Override
protected List<ReactPackage> getPackages() {
  return Arrays.<ReactPackage>asList(
    ...
    new RNFirebasePackage(),
    new RNFirebaseAnalyticsPackage(),
    new RNFirebaseMessagingPackage()
    ...
  );
}
```

To receive the Push message, open `android/app/src/main/AndroidManifest.xml` file and modify it like below.

```xml
<application ...>
...
<service android:name="io.invertase.firebase.messaging.RNFirebaseMessagingService">
  <intent-filter>
    <action android:name="com.google.firebase.MESSAGING_EVENT" />
  </intent-filter>
</service>
<service android:name="io.invertase.firebase.messaging.RNFirebaseBackgroundMessagingService" />
...
</application>
```

Open the Android proejct via Android Studio and click `Gradle Sync`.

{% include in-feed-ads.html %}

## Test

Let's test FCM to check the configuration well.

## Add Javascript source code

To test, we need FCM Token. To get this token, we need to use Javascript. You can use this source code to the production projecton.

Create `./src/Components/FCMContainer/index.tsx` file and modify it like below to use FCM.

```js
import React, { useEffect } from 'react';
import { Platform, Alert } from 'react-native';
import firebase from 'react-native-firebase';
import DeviceInfo from 'react-native-device-info';
import AsyncStorage from '@react-native-community/async-storage';
import Axios from 'axios';

import Config from '~/Config';

interface Props {
  children: JSX.Element;
  onNotificationOpened?: (data: { [key: string]: string }) => any;
}

const FCMContainer = ({ children, onNotificationOpened }: Props): JSX.Element => {
  const CHANNEL_ID = 'io.github.dev.yakuza.poma';
  const APP_NAME = 'POMA';
  const DESCRIPTION = 'POMA channel';

  let _onTokenRefreshListener: any = undefined;
  let _notificationDisplayedListener: any = undefined;
  let _notificationListener: any = undefined;
  let _notificationOpenedListener: any = undefined;

  const _registerMessageListener = (): void => {
    firebase
      .notifications()
      .getInitialNotification()
      .then((notificationOpen) => {
        if (
          onNotificationOpened &&
          typeof onNotificationOpened === 'function' &&
          notificationOpen &&
          notificationOpen.notification &&
          notificationOpen.notification.data &&
          notificationOpen.notification.data.notifications_id
        ) {
          onNotificationOpened(notificationOpen.notification.data);
        }
      });

    const channel = new firebase.notifications.Android.Channel(
      CHANNEL_ID,
      APP_NAME,
      firebase.notifications.Android.Importance.Max,
    ).setDescription(DESCRIPTION);
    firebase.notifications().android.createChannel(channel);

    _notificationListener = firebase.notifications().onNotification((notification) => {
      // Process your notification as required
      notification.android.setPriority(firebase.notifications.Android.Priority.Max);
      notification.android.setChannelId(CHANNEL_ID);

      firebase.notifications().displayNotification(notification);
    });
    _notificationDisplayedListener = firebase.notifications().onNotificationDisplayed(() => {});
    _notificationOpenedListener = firebase
      .notifications()
      .onNotificationOpened((notificationOpen) => {
        if (onNotificationOpened && typeof onNotificationOpened === 'function') {
          onNotificationOpened(notificationOpen.notification.data);
        }
      });
  };

  const _registerToken = async (fcmToken: string): Promise<void> => {
    console.log(fcmToken);
    // try {
    //   const deviceUniqueId = DeviceInfo.getUniqueId();
    //   const token = await AsyncStorage.getItem('token');
    //   await Axios.post(
    //     `URL`,
    //     {
    //       token: fcmToken,
    //       device_unique_id,
    //     },
    //     {
    //       headers: { Authorization: 'Bearer ' + token },
    //     },
    //   );
    // } catch (error) {
    //   console.log('ERROR: _registerToken');
    //   console.log(error.response.data);
    // }
  };

  const _registerTokenRefreshListener = (): void => {
    if (_onTokenRefreshListener) {
      _onTokenRefreshListener();
      _onTokenRefreshListener = undefined;
    }

    _onTokenRefreshListener = firebase.messaging().onTokenRefresh((fcmToken) => {
      // Process your token as required
      _registerToken(fcmToken);
    });
  };
  const _updateTokenToServer = async (): Promise<void> => {
    try {
      const fcmToken = await firebase.messaging().getToken();
      _registerMessageListener();
      _registerToken(fcmToken);
    } catch (error) {
      console.log('ERROR: _updateTokenToServer');
      console.log(error);
    }
  };

  const _requestPermission = async (): Promise<void> => {
    try {
      // User has authorised
      await firebase.messaging().requestPermission();
      await _updateTokenToServer();
    } catch (error) {
      // User has rejected permissions
      Alert.alert("you can't handle push notification");
    }
  };

  const _checkPermission = async (): Promise<void> => {
    try {
      const enabled = await firebase.messaging().hasPermission();
      if (enabled) {
        // user has permissions
        _updateTokenToServer();
        _registerTokenRefreshListener();
      } else {
        // user doesn't have permission
        _requestPermission();
      }
    } catch (error) {
      console.log('ERROR: _checkPermission', error);
      console.log(error);
    }
  };

  useEffect(() => {
    _checkPermission();
    return (): void => {
      if (_onTokenRefreshListener) {
        _onTokenRefreshListener();
        _onTokenRefreshListener = undefined;
      }
      if (_notificationDisplayedListener) {
        _notificationDisplayedListener();
        _notificationDisplayedListener = undefined;
      }
      if (_notificationListener) {
        _notificationListener();
        _notificationListener = undefined;
      }
      if (_notificationOpenedListener) {
        _notificationOpenedListener();
        _notificationOpenedListener = undefined;
      }
    };
  }, []);

  if (Platform.OS === 'ios') {
    firebase.notifications().setBadge(0);
  }

  return children;
};

export default FCMContainer;
```

You should change `Channel ID`, `App Name` and `Description` to fit yours.

```js
const CHANNEL_ID = 'io.github.dev.yakuza.poma';
const APP_NAME = 'POMA';
const DESCRIPTION = 'POMA channel';
```

Alos, For testing, just disply FCM token on the log,

```js
const _registerToken = async (fcmToken: string): Promise<void> => {
  console.log(fcmToken);
  // try {
  //   const deviceUniqueId = DeviceInfo.getUniqueId();
  //   const token = await AsyncStorage.getItem('token');
  //   await Axios.post(
  //     `URL`,
  //     {
  //       token: fcmToken,
  //       device_unique_id,
  //     },
  //     {
  //       headers: { Authorization: 'Bearer ' + token },
  //     },
  //   );
  // } catch (error) {
  //   console.log('ERROR: _registerToken');
  //   console.log(error.response.data);
  // }
};
```

For production, You should make this part to send FCM Token to the server via API.

To use the source code above, open `App.tsx` file and modify it like below.

```js
import React from 'react';
import FCMContainer from '~/Component/FCMContainer';

const App = (): JSX.Element => {
  return (
    <FCMContainer>
      ...
    </FCMContainer>
  );
};

export default App;
```

{% include in-feed-ads.html %}

### iOS test

To test FCM on iOS, we need a device. Connect the device to the PC, and open `Xcode`.

![iOS FCM test - select device](/assets/images/category/react-native/2020/react-native-firebase-fcm/ios_fcm_test_select_device.jpg)

Select the device on the left tope menu, and clic `>` button to execute the project.

![iOS FCM test - permission](/assets/images/category/react-native/2020/react-native-firebase-fcm/ios_fcm_test_permission.jpg)

After executing the app on the device, you can see the screen like above. Click `Allow` button.

![iOS FCM test - get token](/assets/images/category/react-native/2020/react-native-firebase-fcm/ios_fcm_test_get_token.jpg)

After allowing, you can see the FCM token on the console. copy the Token key.

Next, go to [Firebase Console](https://console.firebase.google.com/){:rel="nofollow noreferrer" target="_blank"}, click `Cloud Messaging` on the left menu, and `Send your first message` button.

![ios FCM test - Firebase console](/assets/images/category/react-native/2020/react-native-firebase-fcm/android_fcm_test_firebase_console.jpg)

When the next screen is shown up, insert a test message to `Notification title` and `Notification text`. After inserting, click `Send test message`.

![ios FCM test - insert message](/assets/images/category/react-native/2020/react-native-firebase-fcm/android_fcm_test_insert_message.jpg)

When the screen below is shown up, paste the FCM Token which you copied above on the console to `Add an FCM registration token`, and click `+` button.

![ios FCM test - insert token](/assets/images/category/react-native/2020/react-native-firebase-fcm/android_fcm_test_insert_token.jpg)

Next, click `Test` button to send the message.

![ios FCM test - send message](/assets/images/category/react-native/2020/react-native-firebase-fcm/android_fcm_test_send_message.jpg)

And then, you can see the screen like below that the app received the message well.

![ios FCM test - receive message](/assets/images/category/react-native/2020/react-native-firebase-fcm/ios_fcm_test_receive_message.jpg)

{% include in-feed-ads.html %}

### Android test

Execute the command below to test FCM on Android.

```bash
npm run android
```

After executing, you can see the FCM Token on the console. copy the key.

![Android FCM test - FCM token](/assets/images/category/react-native/2020/react-native-firebase-fcm/android_fcm_test_fcm_token.jpg)

Next, go to [Firebase Console](https://console.firebase.google.com/){:rel="nofollow noreferrer" target="_blank"}, and click `Cloud Messaging` menu on the left, and click `Send your first message` button.

![Android FCM test - Firebase console](/assets/images/category/react-native/2020/react-native-firebase-fcm/android_fcm_test_firebase_console.jpg)

When the next screen is show up, insert a test message to `Notification title` and `Notification text`. After it, click `Send test message` button on the right side.

![Android FCM test - insert message](/assets/images/category/react-native/2020/react-native-firebase-fcm/android_fcm_test_insert_message.jpg)

When the screen blow is shown up, paste FCM token which you copied above to `Add an FCM registration token`, and click `+` button.

![Android FCM test - insert token](/assets/images/category/react-native/2020/react-native-firebase-fcm/android_fcm_test_insert_token.jpg)

And then, click `Test` button to send the test message.

![Android FCM test - send message](/assets/images/category/react-native/2020/react-native-firebase-fcm/android_fcm_test_send_message.jpg)

And then, you can see the screen like below that the app received the message well.

![Android FCM test - receive message](/assets/images/category/react-native/2020/react-native-firebase-fcm/android_fcm_test_receive_message.jpg)

## Completed

We've seen how to receive FCM message on React Native project by react-native-firebase library. You can implement the Push notification by saving the FCM token on the server, and send a message with the Token!
