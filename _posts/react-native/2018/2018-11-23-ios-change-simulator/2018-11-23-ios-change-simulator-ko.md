---
layout: 'post'
permalink: '/react-native/ios-change-simulator/'
paginate_path: '/react-native/:num/ios-change-simulator/'
lang: 'ko'
categories: 'react-native'
comments: true

title: 'iOS 시뮬레이터 변경'
description: 'RN(react native)을 iOS에서 시뮬레이터로 테스트할 때 시뮬레이터를 변경하는 방법에 대해서 알아봅시다.'
image: '/assets/images/category/react-native/ios-change-simulator.jpg'
---


## 개요
RN(react native)으로 앱을 개발할 때 항상 아래에 명령어를 이용하여 iOS를 개발합니다.

```bash
react-native run-ios
```

개발할 때는 크게 문제가 없는데 개발을 완료하고 여러 디바이스(Device)에서 테스트를 하고 싶을 때는 항상 불편했습니다. 그래서 명령어를 사용해서 시뮬레이터(simulator)를 변경하는 방법을 소개합니다.

## iOS 시뮬레이터 확인
현재 사용 가능한 iOS 시뮬레이터(simulator)를 확인합니다.

```bash
xcrun simctl list devices
```

## 시뮬레이터 변경
이제 아래에 명령어를 통해 사용하고 싶은 시뮬레이터(simulator)로 RN(react native)를 실행합니다.

```bash
react-native run-ios --simulator="iPhone 5s"
```

아래에 명령어 리스트는 시뮬레이터(simulator)를 변경하는 예제입니다.

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
