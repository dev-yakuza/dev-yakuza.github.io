---
layout: 'post'
permalink: '/react-native/ios-running-on-device/'
paginate_path: '/react-native/:num/ios-running-on-device/'
lang: 'ko'
categories: 'react-native'
comments: true

title: 'iOS 빌드 및 테스트'
description: 'RN(react native)로 개발한 프로젝트를 iOS용으로 빌드하고 디바이스에서 테스트해봅시다.'
image: '/assets/images/category/react-native/ios-running-on-device.jpg'
---

<div id="contents_list" markdown="1">

## 목차

1. [개요](#개요)
1. [iOS / Mac](#ios--mac)
    - [배포 빌드 준비](#배포-빌드-준비)
        - [HTTPS 통신 설정](#https-통신-설정)
        - [Location 권한 설명 추가](#location-권한-설명-추가)
        - [빌드 스키마 변경](#빌드-스키마-변경)
        - [디바이스에서 기동](#디바이스에서-기동)
1. [참고](#참고)

</div>

## 개요

지난 시간에 RN(react native)로 개발한 프로젝트를 디바이스에서 테스트를 해봤습니다.([디바이스 테스트]({{site.url}}/{{page.categories}}/ios-test-on-device/){:target="_blank"}) 다들 별 문제 없으셨나요? 이제 테스트는 충분히 해봤으니 RN(react native) 프로젝트를 배포하기 위해 빌드해 보고 실제로 디바이스 올려서 기동시켜 봅시다.

이 블로그는 연재물입니다. 아래에 블로그도 함께 확인해보세요.

- [iOS 디바이스 테스트]({{site.url}}/{{page.categories}}/ios-test-on-device/){:target="_blank"}
- [iOS 개발자 등록]({{site.url}}/{{page.categories}}/ios-enroll-developer-program/){:target="_blank"}
- [iOS 인증서(Certification)]({{site.url}}/{{page.categories}}/ios-certification/){:target="_blank"}
- [iOS TestFlight]({{site.url}}/{{page.categories}}/ios-testflight/){:target="_blank"}
- [iOS App store 등록]({{site.url}}/{{page.categories}}/ios-app-store/){:target="_blank"}
- [Fastlane을 통한 앱 자동 배포]({{site.url}}/{{page.categories}}/fastlane/){:target="_blank"}

여기에서는 RN(react native) 프로젝트 빌드와 빌드된 파일을 테스트 디바이스에서 확인하는 방법에 대해 알아보겠습니다. 실제 마켓에 업로드하는 과정은 포함되어 있지 않습니다.

## iOS / Mac

개발자 생성 및 디바이스와의 연결은 이전 블로그를 참고해주세요.([디바이스 테스트]({{site.url}}/{{page.categories}}/ios-test-on-device/){:target="_blank"}) 여기서는 RN(react native) 프로젝트를 배포하기 위해 빌드하는 방법과 빌드된 파일을 디바이스에 올려 테스트하는 내용만 다루겠습니다.

{% include in-feed-ads.html %}

### 배포 빌드 준비

공식 사이트([react-native](https://facebook.github.io/react-native/docs/ios-running-on-device#building-your-app-for-production){:rel="nofollow noreferrer" target="_blank"})에 모든 설명이 친절하게 나와있습니다. 하나하나 따라해봅시다.

#### HTTPS 통신 설정

애플에서 어플이 외부와 ```HTTP``` 통신을 할때는 ```HTTPS```로 통신을 하지 않으면 통신이 불가하도록 설정하는 기능을 넣었다고 합니다. 하지만 RN(react native)를 개발할때는 로컬에 개발 서버를 띄우고 개발 서버와 통신하여 어플을 기동하므로 RN(react native)는 이 기능을 기본적으로 사용하지 않도록 설정해놨습니다. 하지만 실제 빌드하여 제공할 때는 개발 서버를 이용하지 않으므로 이 부분을 제거할 필요가 있습니다. RN(react native) 프로젝트 폴더에서 ```/ios/프로젝트명/info.plist``` 파일을 열어 아래에 부분을 찾아 제거합니다.

```xml
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
    <key>NSExceptionDomains</key>
    <dict>
        <key>localhost</key>
        <dict>
            <key>NSExceptionAllowsInsecureHTTPLoads</key>
            <true/>
        </dict>
    </dict>
</dict>
```

주의: 다시 개발을 할 경우에는 이부분을 복원해야합니다. 위에서 설명했지만 개발시 개발 서버(localhost)와 통신은 HTTP로 하기 때문입니다.

어플이 HTTPS 프로토콜이 아닌 HTTP 프로토콜로 통신을 해야 하시는 분은 아래와 localhost 부분만 제거합니다.

```xml
<key>NSAppTransportSecurity</key>
<dict>
  <key>NSAllowsArbitraryLoads</key>
      <true/>
</dict>
```

{% include in-feed-ads.html %}

#### Location 권한 설명 추가

RN(React Native)의 `info.plist`를 확인하면 아래와 같이 Locaion과 관련된 설정이 있습니다.

```xml
<key>NSLocationWhenInUseUsageDescription</key>
<string></string>
```

사용을 하지 않는 분들은 삭제해도 되지만, 저는 광고에서 위치 정보를 사용하기 때문에 아래와 같이 수정하였습니다.

```xml
<key>NSLocationAlwaysAndWhenInUseUsageDescription</key>
<string>$(PRODUCT_NAME) needs Location access for useful advertisement</string>
<key>NSLocationAlwaysUsageDescription</key>
<string>$(PRODUCT_NAME) needs Location access for useful advertisement</string>
<key>NSLocationWhenInUseUsageDescription</key>
<string>$(PRODUCT_NAME) needs Location access for useful advertisement</string>
```

이부분을 수정하지 않으면 앱을 앱스토어 커넥터(Appstore Connector)에 업로드할시 문제가 발생합니다.

#### 빌드 스키마 변경

RN(react native) 프로젝트를 빌드하기 위해서는 빌드 스키마(build scheme)를 ```Debug```에서 ```Release```로 변경해야 합니다. RN(react native) 프로젝트 폴더에서 ```ios/프로젝트명.xcodeproj```을 실행시킵니다.

xcode가 실행되면 상단 메뉴에서 ```Product``` 메뉴에 ```Scheme``` 항목에 ```Edit Scheme```를 선택합니다.

![change build scheme](/assets/images/category/react-native/ios-running-on-device/change-scheme.jpg)

하단과 같은 화면이 나오면 왼쪽에 ```Run```을 선택하고 오른쪽에 ```Build Configuration```을 ```Debug```에서 ```Release```로 변경하고 하단에 ```Close```를 창을 닫습니다.

![change build scheme to Release from Debug](/assets/images/category/react-native/ios-running-on-device/change-debug-to-release.jpg)

주의: 역시 다시 개발을 할 때에는 이 부분을 ```Release```에서 ```Debug```로 돌려줄 필요가 있습니다.

{% include in-feed-ads.html %}

#### 디바이스에서 기동

모든 설정은 끝났습니다. RN(react native)를 빌드하기 전에 디바이스에서 확인해 봅시다. 디바이스에서 테스트하는 것과 마찬가지로 USB로 Mac과 아이폰을 연결한 후 빌드 타겟을 디바이스로 한 후 화살표 모양을 눌러 실행 시킵니다.

![device test](/assets/images/category/react-native/ios-running-on-device/device-test.jpg)

디바이스에서 테스트와 달리 js(javascript)가 빌드된 bundle 파일을 사용하기 때문에 Mac과 아이폰이 같은 Wifi/Network상에 존재할 필요가 없으며 인스톨후에 Mac과 디바이스가 연결되어 있을 필요가 없습니다. 하지만 정식 인스톨이 아니기 때문에 일정 기간이 지나면 해당 어플을 사용할 수 없습니다.

{% include in-feed-ads.html %}

## 참고

- 공식 사이트: [react native](https://facebook.github.io/react-native/docs/ios-running-on-device){:rel="nofollow noreferrer" target="_blank"}

