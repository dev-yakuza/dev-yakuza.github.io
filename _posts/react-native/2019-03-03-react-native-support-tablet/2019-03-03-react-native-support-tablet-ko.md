---
layout: 'post'
permalink: '/react-native/react-native-support-tablet/'
paginate_path: '/react-native/:num/react-native-support-tablet/'
lang: 'ko'
categories: 'react-native'
comments: true

title: 'RN(React Naitve) 태블릿 지원하기'
description: 'RN(React Native) 프로젝트에서 태블릿 지원하는 방법에 대해서 알아봅시다.'
image: '/assets/images/category/react-native/react-native-support-tablet/background.jpg'
---


## 개요
RN(React Native)으로 우리는 크로스 플랫폼 앱(Cross Platform App)을 제작할 수 있습니다. 이 말은 아이폰(iPhone), 안드로이드 폰(Android phone) 이외에도 아이패드(iPad), 안드로이드 태블릿(Android Tablet)을 제작할 수 있습니다. 이번 블로그에서는 스마트폰으로 제작한 앱을 태블릿에 적용하는 방법에 대해서 알아봅니다.

## 안드로이드
안드로이드는 특별한 처리를 하지 않아도 폰과 태블릿을 지원합니다. 여기에서는 자신의 앱이 어떤 디바이스를 지원하는지 확인하는 방법을 설명합니다.

아래의 링크를 눌러 구글 플레이 콘솔(Google Play Console)에 접속합니다.

- 구글 플레이 콘솔: [https://play.google.com/apps/publish/](https://play.google.com/apps/publish/){:rel="nofollow noreferrer" target="_blank"}

로그인 후, 확인하고자 하는 앱을 선택합니다.

![구글 플레이 - 안드로이드 앱 디바이스 지원 목록](/assets/images/category/react-native/react-native-support-tablet/android-support-devices.png)

왼쪽 메뉴에서 `Release management` > `Device catalog`를 선택하면 위와 같은 화면을 볼 수 있습니다. 만약 `동의` 화면이 나온다면 동의하면 위와 같은 화면을 볼 수 있습니다.

![구글 플레이 - 안드로이드 앱 마켓 정보 수정](/assets/images/category/react-native/react-native-support-tablet/android-market-info.png)

왼쪽 메뉴에서 `Store presence` > `Store listing`을 누르고 `TABLET`의 이미지를 추가해 줍니다.


## iOS
iOS도 특별히 코딩을 할 필요는 없습니다. RN(React Native)의 프로젝트 폴더에서 `ios/[project name].xcodeproj` 또는 `ios/[project name].xcworkspace`을 열어 xcode를 실행합니다.

![xcode universal 앱 설정](/assets/images/category/react-native/react-native-support-tablet/ios-universal-configuration.png)

위와 같이 왼쪽의 프로젝트명, `TARGETS`도 프로젝트명을 선택합니다. `Development Info`의 `Devices`를 선택하고 `Universal`을 선택합니다.

iOS도 안드로이도와 같이 앱 스토어(App store) 정보를 수정하시기 바랍니다.


## 완료
이것으로 RN(React Native)로 개발한 앱이 스마트폰과 태블릿을 지원하게 되었습니다. 태블릿을 지원하는 것은 설정만 변경하게 되므로 엄청 간단합니다. 또한 RN(React Native)는 `Flexbox`를 사용하기 때문에 responsive 대응도 쉽게 할 수 있습니다. 다만, 특정 위치를 지정하거나, 특정 사이즈를 지정하게 될 때는 화면 사이즈를 생각하며 제작해야 합니다. 저는 [react-native-device-info]({{site.url}}/{{page.categories}}/react-native-device-info/){:target="_blank"}의 `DeviceInfo.isTablet()`를 사용하여, 디바이스에 영향이 있는 부분은 처리하고 있습니다.

