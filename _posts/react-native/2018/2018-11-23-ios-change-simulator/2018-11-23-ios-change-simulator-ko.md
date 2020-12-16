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

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [iOS 시뮬레이터 확인](#ios-시뮬레이터-확인)
- [시뮬레이터 변경](#시뮬레이터-변경)
- [완료](#완료)

</div>

## 개요

RN(react native)으로 앱을 개발할 때 항상 아래에 명령어를 이용하여 iOS를 개발합니다.

```bash
npm run ios
```

개발할 때는 크게 문제가 없는데 개발을 완료하고 여러 디바이스(Device)에서 테스트를 하고 싶을 때는 항상 불편했습니다. 그래서 명령어를 사용해서 시뮬레이터(simulator)를 변경하는 방법을 소개합니다.

## iOS 시뮬레이터 확인

현재 사용 가능한 iOS 시뮬레이터(simulator)를 확인합니다.

```bash
xcrun simctl list devices
```

명령어를 실행하면 아래와 같이 사용 가능한 시뮬레이터의 리스트를 확인할 수 있습니다.

```bash
iPhone 8 (066D55DB-AB0A-41D3-84A0-612E68F88063)
iPhone 8 Plus (3AA8DBD0-20FF-4FA4-8745-F63F6A078E6E)
iPhone 11 (DD6577E9-8092-479F-8DE4-0F2D00326574)
iPhone 11 Pro (41166CD6-5270-4919-BE03-272D1835E3E1)
iPhone 11 Pro Max (BE84015E-FC1C-42EA-B708-73258190ED6F)
iPhone SE (2nd generation) (8CEB8C23-1BB7-4B2F-A51F-4C2623F4BCEF)
iPad Pro (9.7-inch) (3495B155-8378-4A8B-817E-D0CAB8A793F0)
iPad (7th generation) (DBF8AFFF-D166-4ACB-8041-59A414FBB8F8)
iPad Pro (11-inch) (2nd generation) (5283A04B-EFE1-41F9-944B-C66EFF1E1498)
iPad Pro (12.9-inch) (4th generation) (DDAD2AAE-3506-4456-9F8F-29BA7DF0B1A3)
iPad Air (3rd generation) (526BEA39-E657-47AF-A7A2-22BA93D81FA1)
```

## 시뮬레이터 변경

이제 아래에 명령어를 통해 사용하고 싶은 시뮬레이터(simulator)로 RN(react native)를 실행합니다.

```bash
npm run ios -- --simulator="iPhone 5s"
```

아래에 명령어 리스트는 시뮬레이터(simulator)를 변경하는 예제입니다.

```bash
npm run ios -- --simulator="iPhone 5s"
npm run ios -- --simulator="iPhone 6"
npm run ios -- --simulator="iPhone 6 Plus"
npm run ios -- --simulator="iPhone 6s"
npm run ios -- --simulator="iPhone 6s Plus"
npm run ios -- --simulator="iPhone 7"
npm run ios -- --simulator="iPhone 7 Plus"
npm run ios -- --simulator="iPhone 8"
npm run ios -- --simulator="iPhone 8 Plus"
npm run ios -- --simulator="iPhone SE"
npm run ios -- --simulator="iPhone X"
npm run ios -- --simulator="iPhone XR"
npm run ios -- --simulator="iPhone XS"
npm run ios -- --simulator="iPhone Xs Max"
npm run ios -- --simulator="iPad Air"
npm run ios -- --simulator="iPad Air 2"
npm run ios -- --simulator="iPad"
npm run ios -- --simulator="iPad Pro"
```

## 완료

이것으로 React Native 프로젝트를 시뮬레이터에서 확인할 때, 기본 시뮬레이터가 아닌 시뮬레이터를 실행하는 방법에 대해서 알아보았습니다. 이제 여러분도 위에 명령어를 통해 다양한 시뮬레이터에서 테스트해 보시기 바랍니다.
