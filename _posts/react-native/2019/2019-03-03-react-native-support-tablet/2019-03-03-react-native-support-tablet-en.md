---
layout: 'post'
permalink: '/react-native/react-native-support-tablet/'
paginate_path: '/react-native/:num/react-native-support-tablet/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'RN(React Naitve) Support Tablets'
description: let's see how to make RN(React Native) project support tablets
image: '/assets/images/category/react-native/react-native-support-tablet/background.jpg'
---


## Outline
we can make the cross platform app by RN(React Native). in other words, we can make the app support not only iPhone, Android phone but also iPad, Android tablet. in this blog, I'll introduce how to make the app support the tablets.

## Android
we don't need anything to make the app support the tablets. in here, we just see how to check what kind of the devices supported.

click the link below to go to Google Play Console.

- Google Play Console: [https://play.google.com/apps/publish/](https://play.google.com/apps/publish/){:rel="nofollow noreferrer" target="_blank"}

after login, click the app that you want to check.

![Google Play - Android App Device support list](/assets/images/category/react-native/react-native-support-tablet/android-support-devices.png)

to click `Release management` > `Device catalog` on the left menu, you can see the screen like above. if you see the agreement page, click `Agree`.

![Google Play - Android App Market Info edit](/assets/images/category/react-native/react-native-support-tablet/android-market-info.png)

click `Store presence` > `Store listing` and add images on `TABLET`.


## iOS
we don't need to add the code. click `ios/[project name].xcodeproj` or `ios/[project name].xcworkspace` on RN(React Native) proejct to execute xcode.

![xcode universal app configuration](/assets/images/category/react-native/react-native-support-tablet/ios-universal-configuration.png)

click the project name on left menu and click the project name on `TARGETS`, too. select `Universal` on `Development Info` > `Devices`.

also, you need to edit the app store info like Android.


## Completed
now, your app supports smartphone and tablets. it's simple to make the app support the tablet. also, RN(React Native) uses `Flexbox` so the app basically support responsive. just, if you use specifi position or specific size, you should consider about the screen size. I use `DeviceInfo.isTablet()` in [react-native-device-info]({{site.url}}/{{page.categories}}/react-native-device-info/){:target="_blank"} library to support it.

