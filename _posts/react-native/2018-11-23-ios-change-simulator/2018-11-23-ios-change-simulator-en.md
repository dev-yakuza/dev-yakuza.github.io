---
layout: 'post'
permalink: '/react-native/ios-change-simulator/'
paginate_path: '/react-native/:num/ios-change-simulator/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'change simulator on iOS'
description: let's see how to change the simulator on iOS when we test RN(react native) on iOS.
image: '/assets/images/category/react-native/ios-change-simulator.jpg'
---


## outline
we always use below command on RN(react native) development.

```bash
react-native run-ios
```

it's not problem when we develop but when we want to test RN(react native) project on different device, it always uncomfortable. so we introduce how to change simulator by command line.

## check iOS simulators
check current iOS simulator we can use.

```bash
xcrun simctl list devices
```

## change simulator
execute below command to start the simulator you want to you.

```bash
react-native run-ios --simulator="iPhone 5s"
```

below command list is examples of how to change the simulator.

```bash
react-native run-ios --simulator="iPhone 5s"
react-native run-ios --simulator="iPhone 6"
react-native run-ios --simulator="iPhone 6 Plus"
react-native run-ios --simulator="iPhone 6s"
react-native run-ios --simulator="iPhone 6s Plus"
react-native run-ios --simulator="iPhone 7"
react-native run-ios --simulator="iPhone 7 Plus"
react-native run-ios --simulator="iPhone 8"
react-native run-ios --simulator="iPhone 8 Plus"
react-native run-ios --simulator="iPhone SE"
react-native run-ios --simulator="iPhone X"
react-native run-ios --simulator="iPhone XR"
react-native run-ios --simulator="iPhone XS"
react-native run-ios --simulator="iPhone XS Max"
react-native run-ios --simulator="iPad Air"
react-native run-ios --simulator="iPad Air 2"
react-native run-ios --simulator="iPad"
react-native run-ios --simulator="iPad Pro"
```
