---
layout: 'post'
permalink: '/react-native/test-on-device/'
paginate_path: '/react-native/:num/test-on-device/'
lang: 'ko'
categories: 'react-native'
comments: true

title: '디바이스 테스트'
description: 'RN(react native)로 개발한 프로젝트를 디바이스에서 테스트해 봅시다.'
image: '/assets/images/category/react-native/test-on-device.jpg'
---


## 개요
RN(react native)로 개발한 프로젝트를 시뮬레이터로만 테스트하기 힘드시죠? 지금까지 개발한 RN(react native) 프로젝트를 시뮬레이터가 아닌 디바이스에서 테스트해 봅시다.

## iOS / Mac
아이폰에서 테스트하려면 Mac이 있어야겠죠. Mac과 iOS 디바이스 그리고 테스트 하고 싶은 프로젝트를 준비합니다.

![prepare iphone mac](/assets/images/category/react-native/test-on-device/mac-iphone.jpg)

### 개발자 생성
디바이스에서 테스트하기 위해서는 애플 개발자 계정(Apple developer account)이 필요합니다. 개발자 등록이 아닌 계정을 생성하는 것이므로 무료로 사용이 가능합니다. 애플 개발자 계정(Apple developer account)이 있으신 분은 이 항목을 넘어가셔도 괜찮습니다.

아래에 링크를 눌러 애플 개발자 계정(Apple developer account) 생성 사이트로 이동합니다.

- 애플 개발자 계정(Apple developer account): [https://developer.apple.com/](https://developer.apple.com/){:rel="nofollow noreferrer" :target="_blank"}

![apple developer site](/assets/images/category/react-native/test-on-device/apple-developer-site.png)

오른쪽 위에 ```account``` 메뉴를 선택합니다.

![apple developer site login](/assets/images/category/react-native/test-on-device/apple-developer-site-login.png)

애플 계정이 있으신 분은 로그인을 하시면 됩니다. 계정이 없으신 분은 ```Create Apple ID```로 애플 계정을 생성합니다. 애플 개발자 계정이 아닌 애플 계정, 아이폰에서 어플을 다운로드하실 때 사용하시는 계정을 사용하시면 됩니다.

![agreement](/assets/images/category/react-native/test-on-device/agreement.png)

애플 개발자 계정으로 사용하기 위한 약관이 표시됩니다. ```By checking this box I confirm that I have read and agree to be bound by the Agreement above.```를 눌러 동의하고 ```Submit```을 눌러 다음으로 진행합니다.

![completed to create developer account](/assets/images/category/react-native/test-on-device/completed-create-account.png)

애플 개발자 계정(Apple developer account) 생성이 완료되었습니다.

### 디바이스 테스트
공식 사이트([react native](https://facebook.github.io/react-native/docs/running-on-device){:rel="nofollow noreferrer" :target="_blank"})에 친절하게 설명이 잘 나와있습니다. 한번 따라해 봅시다.

1. USB를 이용하여 테스트하고 싶은 디바이스와 Mac을 연결합니다.
1. RN(react native) 프로젝트가 있는 폴더에 ```ios/[프로젝트명].xcodeproj``` 파일을 실행 시킵니다.
1. xcode가 실행되면 왼쪽 위에 프로젝트명을 선택하고 프로젝트명 오른쪽 화면 위에 있는 ```General``` 탭을 선택합니다. 스크롤을 해서 내려가다보면 ```Signing``` 섹션이 보입니다. ```Team``` 항목 옆에 ```Add an Account...```를 클릭합니다.

    ![signing in xcode](/assets/images/category/react-native/test-on-device/signing.png)

    상단에서 만든 애플 개발자 계정(Apple developer account)의 아이디/패스워드를 입력하고 ```Next```를 누릅니다.

    ![login signing in xcode](/assets/images/category/react-native/test-on-device/signing-login.png)

    로그인 후에 나오는 화면에서 하단에 ```Download Manual Profiles```를 눌러 다운로드한 후 창을 닫습니다.


    이제 ```Team```옆에 항목이 드롭다운 메뉴로 변경된걸 확인할 수 있습니다. 위에서 추가한 아이디를 선택합니다.

    ![signing error in xcode](/assets/images/category/react-native/test-on-device/signing-error.png)

    위와 같이 에러가 나오시는 분들은 상단에 ```Identity```의 ```Bundle Identifier```를 변경해 주세요.

    ![signing error solve in xcode](/assets/images/category/react-native/test-on-device/signing-error-solve.png)

    왼쪽에 ```Targets``` 항목에 ```프로젝트명Tests```를 선택하고 ```Team```옆에 드롭다운 메뉴를 선택하여 ```signing```(ID 선택)해줍니다.

    ![signing test target in xcode](/assets/images/category/react-native/test-on-device/signing-target-test.png)
1. 왼쪽위에 프로젝트를 실행시킬 장치를 USB로 연결한 Device로 변경하고 화살표를 눌러 프로젝트를 실행시킵니다.

    ![device test in xcode](/assets/images/category/react-native/test-on-device/device-test.png)

    주의: 디바이스에 테스트를 위한 빌드입니다. 따라서 시뮬레이터와 동일하게 PC에 개발서버가 활성화되고 그 서버와 디바이스가 통신하여 테스트가 가능하도록 동작합니다. 따라서 같은 Wifi 환경 / 네트워크가 아니면 서버를 찾을 수 없기 때문에 디바이스 테스트가 불가능합니다.

1. 성공적으로 프로젝트가 빌드되면 아래와 같은 메세지를 볼수 있습니다.

    ![security error](/assets/images/category/react-native/test-on-device/security-error.png)

    친절하게 설명이 나와있으므로 따라해봅니다. 디바이스의 ```설정```을 실행합니다. ```일반```을 선택하고 ```프로파일 및 기기 관리```를 선택합니다. ```개발자 앱``` 항목에 자신의 애플 개발자 계정(Apple developer account)을 선택하고 ```신뢰함```을 선택합니다. 그리고 xcode에 왼쪽 위에 실행 버튼을 다시 눌러 프로젝트를 실행하면 잘 동작하는 것을 확인할 수 있습니다.

## 안드로이드(Android)
우리가 안드로이드(Android)로 테스트할 때 내용을 수정하도록 하겠습니다.


## 참고
- 공식 사이트: [react native](https://facebook.github.io/react-native/docs/running-on-device){:rel="nofollow noreferrer" :target="_blank"}
