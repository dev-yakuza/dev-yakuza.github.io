---
layout: 'post'
permalink: '/react-native/android-test-on-device/'
paginate_path: '/react-native/:num/android-test-on-device/'
lang: 'ko'
categories: 'react-native'
comments: true

title: '안드로이드 디바이스 테스트'
description: 'RN(react native)로 개발한 프로젝트를 안드로이드(Android) 디바이스에서 테스트해 봅시다.'
image: '/assets/images/category/react-native/android-test-on-device.jpg'
---


## 개요
안드로이드(Android) 개발은 역시 에뮬레이터에서 개발하기가 너무 힘드네요. RN(react native) 프로젝트를 안드로이드용으로 개발할 때 에뮬레이터가 아닌 안드로이드(Android) 디바이스에서 테스트하도록 설정해보겠습니다. RN(react native)를 iOS 디바이스에서 테스트하는 방법이 궁금하시는 분은 이전 블로그인 [iOS 디바이스 테스트]({{site.url}}/{{page.categories}}/ios-test-on-device/){:target="_blank"}를 확인해 주시기 바랍니다.

## 준비물
당연한 이야기 이지만 RN(react native) 프로젝트를 안드로이드(Android) 디바이스에서 테스트하려면 아래와 같은 준비물이 필요합니다.

- 안드로이드 스튜디오(Android Studio)
- 안드로이드(Android) 디바이스
- RN(react native) 프로젝트

PC에 RN(react native) 개발 환경을 구성하는 방법에 대해서 궁금하신 분은 이전 블로그인 [RN 설치]({{site.url}}/{{page.categories}}/installation/){:target="_blank"}을 참고하시기 바랍니다.

## 안드로이드 디바이스 테스트
RN(react native)의 공식 사이트에 가면 RN(react native)를 안드로이드(Android)에서 테스트하는 방법에 대해서 자세히 나와있습니다. 그럼 한번 따라해보도록 하겠습니다.

- 공식 사이트: [https://facebook.github.io/react-native/docs/running-on-device](https://facebook.github.io/react-native/docs/running-on-device){:rel="nofollow noreferrer" target="_blank"}

## 안드로이드 디바이스 설정
사용하고 있는 안드로이드(Android) 디바이스의 개발자 옵션을 활성화 시켜야합니다. 안드로이드(Android) 디바이스의 ```설정``` > ```디바이스 정보```에 ```빌드 번호```를 여러번 누르면 개발자 옵션이 활성화됩니다.

개발자 옵션이 활성화되었다면, ```USB 디버깅``` 기능을 활성화 해야합니다. ```설정``` > ```개발자 옵션``` > ```USB 디버깅``` 메뉴를 선택하여 USB 디버깅 기능을 활성화 시킵니다.

## 안드로이드 디바이스 연결
안드로이드(Android) 디바이스를 USB를 이용해서 PC와 연결합니다. 안드로이드(Android) 디바이스에서 USB 디버깅을 허용할지 묻는 메세지가 나오면 허용해 테스트가 가능한 상태를 만듭니다.

## 안드로이드 디바이스에서 실행
안드로이드(Android) 디바이스가 연결된 상태에서 안드로이드 스튜디오(Android Studio)를 실행하고 왼쪽 위에 ```Debug app``` 버튼(벌레 위에 화살표가 있는 버튼)을 누르면 자신의 에뮬레이터 이외에 자신의 디바이스가 보입니다. 자신의 디바이스를 선택하고 ```OK```를 누르면 디바이스에서 자신이 개발한 RN(react native) 앱이 기동하시는 걸 볼 수 있습니다.

주의: 디바이스에 테스트를 위한 실행입니다. 따라서 에뮬레이터와 동일하게 PC에 개발서버가 활성화되고 그 서버와 디바이스가 통신하여 테스트가 가능하도록 동작합니다. 따라서 같은 Wifi 환경 / 네트워크가 아니면 서버를 찾을 수 없기 때문에 디바이스 테스트가 불가능합니다.

## 안드로이드 5.0 버전 이하
테스트하려는 디바이스가 안드로이드(Android) 버전이 5.0이하인 경우 몇가지 추가적으로 수정을 해 주셔야합니다. 밑에 나온 동작으로 우리는 안드로이드 4.4.2에서 RN(react native) 프로젝트를 구동시켜 테스트하였습니다.

RN(react native) 프로젝트 폴더에서 ```android/app/build.gradle``` 파일을 아래와 같이 수정합니다.

```xml
defaultConfig {
    ...
    ndk {
        // abiFilters "armeabi-v7a", "x86"
    }
}
```

안드로이드 스튜디오(Android Studio)를 열고 ```gradle```을 ```sync```버튼을 눌러 동기화합니다. 동기화가 완료되면 RN(react native) 프로젝트를 실행합니다.

```bash
react-native run-android
```

RN(react native)의 서버가 PC에 활성화되고 디바이스에도 어플이 잘 설치되지만 빨간 에러 화면이 나옵니다.

디바이스를 흔들어서 개발자 메뉴(Developer Menu)를 띄웁니다. 개발자 메뉴에서 ```Dev Settings``` > ```Debug server host & port for device```를 선택합니다. IP 주소와 포트를 넣는 화면이 나옵니다. 거기에 자신의 피씨 IP와 8081 포트를 입력합니다.(ex> 10.0.1.1:8081) 다시 개발자 메뉴로 돌아와 ```Reload JS```를 눌러 프로젝트를 재실행합니다.

## 완료
안드로이드(Android) 디바이스에서 RN(react native)를 기동시키는 방법을 살펴보았습니다. 이제 에뮬레이터에서 벗어나 실제 디바이스에서 테스트해 보세요.