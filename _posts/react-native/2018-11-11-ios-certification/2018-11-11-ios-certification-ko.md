---
layout: 'post'
permalink: '/react-native/ios-certification/'
paginate_path: '/react-native/:num/ios-certification/'
lang: 'ko'
categories: 'react-native'
comments: true

title: 'iOS 인증서(Certification)'
description: '애플 개발자 프로그램(Apple Developer Program) 등록을 완료했다면, 개발자 인증서(Certification)을 설정하는 방법에 대해 알아봅니다.'
image: '/assets/images/category/react-native/ios-certification.jpg'
---


## 개요
이 블로그는 애플 개발자 프로그램(Apple Developer Program)에 이미 등록된 개발자를 위한 설명입니다. 애플 개발자 프로그램(Apple Developer Program)에 아직 등록을 하지 않으신 분은 이전 블로그인 [iOS 개발자 등록]({{site.url}}/{{page.categories}}/ios-enroll-developer-program/){:target="_blank"}을 보고 애플 개발자 프로그램(Apple Developer Program)에 등록해 주시기 바랍니다.

그럼 개발자 인증서(Certification)을 생성하고 설정하는 방법에 대해 알아보겠습니다.

## 인증서 다운로드
애플 개발자 프로그램(Apple Developer Program)을 구매하고 구매 완료 이메일을 받았다면 애플 개발자 사이트([https://developer.apple.com/](https://developer.apple.com/){:rel="nofollow noreferrer" :target="_blank"})의 ```Account``` 페이지로 이동합니다.

![apple developer site after enrolling](/assets/images/category/react-native/ios-certification/apple-developer-site-after-enrolling.png)

애플 개발자 프로그램(Apple Developer Program)에 등록하기 전과 화면이 조금 다릅니다. 왼쪽 위에 ```Certificates, IDs & Profiles```를 선택하여 인증서(Certification) 발급 페이지로 이동합니다.

![download certification](/assets/images/category/react-native/ios-certification/download-certification.png)

인증서(Certification)가 이미 하나 존재합니다. 해당 인증서(Certification)를 선택하고 ```Download``` 버튼을 눌러 원하는 위치에 잘 저장합니다. 인증서가 보이지 않는 분은 아래에 인증서 생성을 통해 인증서를 새로 생성해 주시기 바랍니다.

이 인증서는 개발용 인증서입니다. 이 인증서가 있는 분도 아래에 인증서 생성 부분을 통해 배포용 인증서를 생성해 주시기 바랍니다.

## 인증서 생성
Mac에서 ```키체인 접근``` 프로그램을 실행 시킵니다.

![키체인 접근](/assets/images/category/react-native/ios-certification/ko-keychain.png)

키체인이 실행되면 왼쪽 상단에 ```키체인 접근```을 선택하고 ```인증서 지원```을 누른 후 ```인증 기관에서 인증서 요청...```을 선택합니다.

![키체인 접근 인증서 요청](/assets/images/category/react-native/ios-certification/ko-request-certification.png)

위와 같이 ```인증 기관에서 인증서 요청...```을 누르면 아래와 같이 ```인증서 지원``` 다이얼로그가 나옵니다.

![키체인 접근 인증서 정보 입력](/assets/images/category/react-native/ios-certification/ko-certification-info.png)

위와 같은 화면이 나오면 ```사용자 이메일 주소```와 ```일반 이름```에 정보를 입력하고 ```요청 항목```에서 ```디스크에 저장```과 ```본인이 키 쌍 정보 지정```을 선택하고 ```계속```을 누릅니다. 파일 저장 화면이 나오면 원하는 장소를 선택하여 파일을 저장합니다.

![키체인 접근 인증서 저장](/assets/images/category/react-native/ios-certification/ko-certification-key.png)

키 쌍 정보를 위와 같이 입력하고 ```계속```을 누릅니다.

![키체인 접근 인증서 저장 완료](/assets/images/category/react-native/ios-certification/ko-certification-completed.png)

디스크에 인증서가 잘 저장되었습니다.

![download certification](/assets/images/category/react-native/ios-certification/download-certification.png)

애플 개발자 사이트([https://developer.apple.com/](https://developer.apple.com/){:rel="nofollow noreferrer" :target="_blank"})에 ```Account``` 페이지에서 ```Certificates, IDs & Profiles```를 눌러 이동했던 사이트에 오른쪽 위에 ```+```버튼을 누릅니다.

![certification selection](/assets/images/category/react-native/ios-certification/select-certification.png)

인증서 선택화면에서 ```iOS App Development```를 선택하고 밑으로 스크롤한 후 ```Continue```를 누릅니다.

배포용 인증서를 생성하시는 분은 ```Production``` 섹션의 ```App Store and Ad Hoc```을 선택하고 진행하시기 바랍니다.

인증서 파일(CSR)을 만드는 방법에 대한 설명 페이지가 나옵니다. 우리는 위에서 ```키체인 접근```을 통해 인증서 파일(CSR) 파일을 이미 만들었으므로 밑으로 스크롤하여 ```Continue```를 누릅니다.

![create csr file](/assets/images/category/react-native/ios-certification/create-csr-file.png)

생성한 인증서 파일을 선택하는 화면에서 ```Choose File``` 버튼을 눌러 이전에 만든 인증서 파일을 선택하고 하단에 ```Continue```를 눌러 다음으로 진행합니다.

![choose csr file](/assets/images/category/react-native/ios-certification/choose-csr-file.png)

인증서 생성이 완료되었습니다. ```Download``` 버튼을 눌러 인증서를 원하는 폴더에 잘 저장합니다.

![complete create certification file](/assets/images/category/react-native/ios-certification/complete-create-certification.png)

## 인증서 등록
생성한 인증서를 ```키체인 접근```에 넣어줄 필요가 있습니다. ```키체인 접근```을 실행합니다.

![키체인 접근](/assets/images/category/react-native/ios-certification/ko-keychain.png)

아래와 같이 ```키체인 접근``` 창이 활성화 되면 왼쪽 하단에 ```내 인증서```를 선택하고 해당 화면에 위에서 다운로드한 인증서를 드래그해서 추가합니다.

![키체인 접근 인증서](/assets/images/category/react-native/ios-certification/ko-keychain-certification.png)

## 애플 개발자 계정 연결
애플 개발자 계정(Apple Developer)과 현재 프로젝트를 연결할 필요가 있습니다. RN(react native) 프로젝트 폴더에서 ```ios/프로젝트명.xcodeproj``` 파일을 실행시킵니다.

xcode에서 왼쪽 위 ```프로젝트명```을 선택하고 ```General``` 탭으로 이동합니다.

![xcode certification](/assets/images/category/react-native/ios-certification/xcode-certification.png)

위와 같은 화면에서 ```Signing``` 항목의 ```Team``` 옆 드롭다운 메뉴를 선택합니다.

![xcode certification add new](/assets/images/category/react-native/ios-certification/xcode-certification-add-new.png)

이미 xcode와 애플 개발자 계정(Apple Developer) 연동을 시키신 분은 해당 계정을 선택하시면 됩니다. 계정 연동을 하지 않으신 분은 ```Add an Account```을 선택합니다.

![xcode certification login](/assets/images/category/react-native/ios-certification/xcode-certification-login.png)

애플 개발자 계정(Apple Developer)으로 로그인합니다. 애플 개발자 계정(Apple Developer) 생성을 하지 않은 분은 [iOS 디바이스 테스트]({{site.url}}/{{page.categories}}/ios-test-on-device/){:target="_blank"}에서 애플 개발자 계정 생성법을 확인해 주세요. 로그인을 완료하면 왼쪽위에 닫기 버튼을 눌러 창을 닫습니다.

![xcode certification add new](/assets/images/category/react-native/ios-certification/xcode-certification-add-new.png)

다시 ```Team``` 옆에 드롭다운 메뉴를 선택하면 방금 추가한 애플 개발자 계정을 볼 수 있습니다. 개발자 계정을 선택합니다.

같은 방식으로 Test 부분도 애플 개발자 계정(Apple Developer)과 연결합니다.

![xcode certification add test](/assets/images/category/react-native/ios-certification/xcode-certification-add-test.png)

이로써 개발자 계정 연결을 완료하였습니다. 이제 배포를 위한 빌드시 사용하는 프로비저닝 프로파일(Provisioning Profiles)을 생성하고 연결하겠습니다.


## 프로비저닝 프로파일 생성
애플 개발자 사이트(Apple Developer)의 ```Account``` 페이지에서 스크롤하여 하단으로 이동하면 ```Provisioning Profiles``` 항목을 확인할 수 있습니다.

프로비저닝 프로파일(Provisioning Profiles)도 개발자용과 배포용이 필요하므로 아래에 과정을 개발자용과 배포용, 두 번 진행하셔야합니다.

![provisioning profiles](/assets/images/category/react-native/ios-certification/provisioning-profiles.png)

메뉴에서 ```All```을 눌러 프로비저닝 프로파일(Provisioning Profiles)를 등록하는 화면으로 이동합니다.

![provisioning profiles detail](/assets/images/category/react-native/ios-certification/provisioning-profiles-detail.png)

위와 같은 화면이 보이면 오른쪽 위에 ```+``` 버튼을 눌러 새로운 프로비저닝 프로파일(Provisioning Profile)을 추가합니다.

![provisioning profiles ios](/assets/images/category/react-native/ios-certification/provisioning-profiles-ios.png)

위와 같은 화면에서 ```iOS App Development```를 선택하고 ```Continue```를 눌러 진행합니다.

배포용 프로비저닝 프로파일(Provisioning Profiles)은 ```Distribution```의 ```App Store```를 선택하고 진행합니다.

![provisioning profiles app id](/assets/images/category/react-native/ios-certification/provisioning-profiles-app-id.png)

우리가 앱을 개발할 때 사용한 ```Bundle Identifier```를 선택합니다. ```Bundle Identifier```는 xcode에서 왼쪽 위 ```프로젝트명```을 선택하고 ```General``` 탭으로 이동하면 제일 상단에 ```Identity``` 항목에서 확인 할 수 있습니다.

![xcode bundle identifier](/assets/images/category/react-native/ios-certification/xcode-certification.png)

선택을 완료하고 ```Continue```를 눌러 진행합니다. 개발자 계정과 테스트 장치를 선택하고 다음으로 진행합니다.

![provisioning profiles name](/assets/images/category/react-native/ios-certification/provisioning-profiles-name.png)

최종적으로 프로비저닝 프로파일(Provisioning Profile)의 이름을 설정하고 ```Continue```를 눌러 다음으로 진행합니다.

프로비저닝 프로파일(Provisioning Profile)의 생성이 완료되었습니다. ```Download```를 눌러 파일을 다운로드한 후 알기 쉬운 곳에 보관해 둡니다.

## 프로비저닝 프로파일 연결
xcode에서는 기본적으로 자동으로 ```Signing```을 관리하도록 설정되어있습니다.(```Signing``` 항목의 ```Automatically manage signing```)

![xcode bundle identifier](/assets/images/category/react-native/ios-certification/xcode-certification.png)

이 상태로 프로비저닝 프로파일(Provisioning Profile)과 연결이라던지, 배포 빌드시 별 문제가 없는 분들은 그대로 사용을 하시면 됩니다.(```Signing``` 항목에 빨간 에러가 나오지 않는 분들) 저희는 프로비저닝 프로파일(Provisioning Profile)과의 연결이 제대로 되지 않아 이 옵션을 풀고 수동으로 연동하였습니다.

아래는 수동으로 프로비저닝 프로파일(Provisioning Profile)을 연결하는 방법입니다.

![xcode bundle identifier](/assets/images/category/react-native/ios-certification/xcode-certification.png)

위와 같은 화면에서 ```Signing``` 섹션의 ```Automatically manage signing```을 클릭하여 체크박스를 해제합니다.

![disable automatically manage signing](/assets/images/category/react-native/ios-certification/disable_auto.png)

체크박스를 해제하면 위와 같이 ```Signing(Debug)```와 ```Signing(Release)```섹션이 확성화됩니다. 둘다 ```Provision Profile``` 옆 드롭다운 메뉴에서 ```Import Profile```을 선택하고 위에서 생성하여 다운로드한 프로비저닝 프로파일(Provisioning Profile)을 선택합니다. 같은 방식으로 Test부분도 수정해줍니다.

![disable automatically manage signing test](/assets/images/category/react-native/ios-certification/disable_auto_test.png)

## 완료
이제 모든 설정이 완료되었습니다. 인증서 연결을 하였으므로 개발은 물론 배포준비까지 끝났습니다. 다음 블로그에서는 배포 준비와 ```TestFlight``` 사용법, 실제 배포에 대해서 알아보도록 하겠습니다.