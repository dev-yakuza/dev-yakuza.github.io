---
published: false
layout: 'post'
permalink: '/react-native/ios-enroll-developer-program/'
paginate_path: '/react-native/:num/ios-enroll-developer-program/'
lang: 'ko'
categories: 'react-native'
comments: true

title: '개발자 등록'
description: 'RN(react native)로 개발한 프로젝트를 마켓에 등록하기 위해서는 개발자 프로그램 등록을 해야합니다. 어떻게 등록하는지 그 방법에 대해 알아봅니다.'
image: '/assets/images/category/react-native/ios-enroll-developer-program.jpg'
---


## 개요
지금까지 RN(react native) 프로젝트로 개발하고 디바이스에 올리는 방법까지 알아봤습니다. 이제 완성된 어플리케이션을 마켓에 등록하기 위해 개발자 등록을 하는 방법에 대해 알아 봅시다.

## iOS
우리가 만든 RN(react native) 어플을 앱스토어(App store)에 올리기 위해서는 애플의 개발자 프래그램(Apple developer program)에 등록을 해야합니다.

### 애플 개발자 프로그램 등록

아래에 링크를 눌러 애플 개발자(Apple developer) 사이트로 이동합니다.

- 애플 개발자(Apple developer) 사이트: [https://developer.apple.com/](https://developer.apple.com/){:rel="nofollow noreferrer" :target="_blank"}

![apple developer site](/assets/images/category/react-native/ios-enroll-developer-program/apple-developer-site.png)

오른쪽 상단에 ```Account```를 눌러 로그인 화면으로 이동합니다.

![apple developer login](/assets/images/category/react-native/ios-enroll-developer-program/login.png)

개발자 계정이 없는 분은 [디바이스 테스트]({{site.url}}/{{page.categories}}/test-on-device/){:target="_blank"} 블로그를 참고하여 계정을 생성해 주세요.

![after login](/assets/images/category/react-native/ios-enroll-developer-program/after-login.png)

로그인을 하고 나면 위와 같은 화면을 볼 수 있습니다. 하단에 있는 ```Join the Apple Developer Program```을 눌러 애플 개발자 프로그램(Apple Developer Program) 페이지로 이동합니다.

![Apple Developer Program site](/assets/images/category/react-native/ios-enroll-developer-program/apple-developer-program-site.png)

오른쪽 위에 ```Enroll``` 버튼을 눌러 애플 개발자 프로그램(Apple Developer Program) 가입 조건 페이지로 이동합니다.

![Apple Developer Program condition](/assets/images/category/react-native/ios-enroll-developer-program/apple-developer-program-condition.png)

애플 개발자 프로그램(Apple Developer Program)에 가입하기 위한 조건이 나와있습니다. 개발자 계정을 무사히 생성하였다면 모든 조건을 클리어한 상태입니다. 스크롤을 해서 아래로 이동하여 ```Start Your Enrollment``` 버튼을 눌러 등록 페이지로 이동합니다.

![Apple Developer Program condition](/assets/images/category/react-native/ios-enroll-developer-program/apple-developer-program-condition.png)

어떤 애플 개발자 프로그램(Apple Developer Program)에 등록할지 선택하는 화면입니다. 자신에 상황에 맞는 애플 개발자 프로그램(Apple Developer Program)을 선택하세요. 여기에서는 ```Individula / Sole Proprietor / Single Person Business```를 설명합니다. 해당 프로그램을 선택하고 왼쪽 하단에 ```Continue```를 눌러 등록을 진행합니다.

![select apple developer program](/assets/images/category/react-native/ios-enroll-developer-program/select-apple-developer-program.png)

사용할 애플 개발자 계정(Apple developer account)의 개인 정보를 입력한 후 약관에 동의합니다. 오른쪽 하단에 ```Continue```를 눌러 다음으로 진행합니다.

![apple developer account private information](/assets/images/category/react-native/ios-enroll-developer-program/information.png)

자신이 입력한 내용이 맞는지 확인하는 페이지가 나옵니다. 내용이 맞다면 ```Continue```를 눌러 진행합니다.

이제 구매 화면을 보실 수 있습니다. ```Purchase```버튼을 눌러 구매합니다. 구매 절차는 설명을 생략하도록 하겠습니다.

### 인증서 설정
구매후 구매 완료까지 조금 시간이 걸립니다. 아무리 기다려도 구매 완료 메일이 오지 않는 분은 애플 개발자 사이트([https://developer.apple.com/](https://developer.apple.com/){:rel="nofollow noreferrer" :target="_blank"})에 ```Contact Us```를 누르고 ```멤버십 및 계정``` 메뉴를선택한 다음 ```프로그램 구입 및 갱신```을 누르고 ```전화받기```를 눌러 전화로 상담하시면 바로 구매 완료 메일을 받으실 수 있습니다.

구매 완료 이메일이 받고나서 애플 개발자 사이트([https://developer.apple.com/](https://developer.apple.com/){:rel="nofollow noreferrer" :target="_blank"})로 이동합니다. 아까와는 다른 화면을 볼 수 있습니다.

![apple developer site after enrolling](/assets/images/category/react-native/ios-enroll-developer-program/apple-developer-site-after-enrolling.png)

왼쪽 위에 ```Certificates, IDs & Profiles```를 선택하여 인증서 발급 페이지로 이동합니다.

![download certification](/assets/images/category/react-native/ios-enroll-developer-program/download-certification.png)

인증서가 이미 하나 존재합니다. ~~~해당 인증서를 ```Download``` 버튼을 눌러 원하는 위치에 잘 저장합니다.만약 인증서가 보이지 않는 분들은 아래에 절차를 이용하시기 바랍니다.~~~
이 인증서를 사용해서 작업하다가 실패하였기 때문에 성공한 케이스로 기록합니다. 우리는 이 인증서를 ```Revoke```를 눌러 삭제하고 아래에 인증서 생성을 통해 새로운 인증서를 생성하였습니다.

#### 인증서 생성
인증서 다운로드에 성공하시 분들은 이 부분을 건너뛰셔도 좋습니다.

Mac에서 ```키체인 접근``` 프로그램을 실행 시킵니다.

![키체인 접근](/assets/images/category/react-native/ios-enroll-developer-program/ko-keychain.png)

키체인이 실행되면 왼쪽 상단에 ```키체인 접근```을 선택하고 ```인증서 지원```을 누른 후 ```인증 기관에서 인증서 요청...```을 선택합니다.

![키체인 접근 인증서 요청](/assets/images/category/react-native/ios-enroll-developer-program/ko-request-certification.png)

위와 같이 ```인증 기관에서 인증서 요청...```을 누르면 아래와 같이 ```인증서 지원``` 다이얼로그가 나옵니다.

![키체인 접근 인증서 요청 대화상자](/assets/images/category/react-native/ios-enroll-developer-program/ko-certification-dialog.png)

하단에 ```확인```을 눌러 진행합니다.

![키체인 접근 인증서 정보 입력](/assets/images/category/react-native/ios-enroll-developer-program/ko-certification-info.png)

위와 같은 화면이 나오면 ```사용자 이메일 주소```와 ```일반 이름```에 정보를 입력하고 ```요청 항목```에서 ```디스크에 저장```과 ```본인이 키 쌍 정보 지정```을 선택하고 ```계속```을 누릅니다.

![키체인 접근 인증서 저장](/assets/images/category/react-native/ios-enroll-developer-program/ko-certification-key.png)

위와 같은 화면에서 인증서를 저장할 폴더를 선택하고 키 쌍 정보를 입력합니다.

![키체인 접근 인증서 저장 완료](/assets/images/category/react-native/ios-enroll-developer-program/ko-certification-completed.png)

디스크에 인증서가 잘 저장되었습니다.

![download certification](/assets/images/category/react-native/ios-enroll-developer-program/download-certification.png)

애플 개발자 사이트([https://developer.apple.com/](https://developer.apple.com/){:rel="nofollow noreferrer" :target="_blank"})에 ```Certificates, IDs & Profiles```를 눌러 이동했던 사이트에 오른쪽 위에 ```+```버튼을 누릅니다.

![certification selection](/assets/images/category/react-native/ios-enroll-developer-program/select-certification.png)

인증서 선택화면에서 ```iOS App Development```를 선택하고 밑으로 스크롤한 후 ```Continue```를 누릅니다.

인증서 파일을 만드는 방법에 대한 설명 페이지가 나옵니다. 우리는 위에서 ```키체인 접근```을 통해 이미 만들었으므로 밑으로 스크롤하여 ```Continue```를 누릅니다.

![create csr file](/assets/images/category/react-native/ios-enroll-developer-program/create-csr-file.png)

생성한 인증서 파일을 선택하는 화면에서 ```Chose File``` 버튼을 눌러 이전에 만든 인증서 파일을 선택하고 하단에 ```Continue```를 눌러 다음으로 진행합니다.

![choose csr file](/assets/images/category/react-native/ios-enroll-developer-program/choose-csr-file.png)

생성이 완료되었습니다. ```Download``` 버튼을 눌러 인증서를 원하는 폴더에 잘 저장합니다.

### 프로비저닝 프로파일 생성
애플 개발자 사이트(Apple Developer)에서 스크롤하여 하단으로 이동하면 ```Provisioning Profiles```를 항목을 확인할 수 있습니다.

![provisioning profiles](/assets/images/category/react-native/ios-enroll-developer-program/provisioning-profiles.png)

메뉴에서 ```All```을 눌러 프로비저닝 프로파일(Provisioning Profiles)를 등록하는 화면으로 이동합니다.

![provisioning profiles detail](/assets/images/category/react-native/ios-enroll-developer-program/provisioning-profiles-detail.png)

위와 같은 화면이 보이면 오른쪽 위에 ```+``` 버튼을 눌러 새로운 프로비저닝 프로파일(Provisioning Profile)을 추가합니다.

![provisioning profiles ios](/assets/images/category/react-native/ios-enroll-developer-program/provisioning-profiles-ios.png)

위와 같은 화면에서 ```iOS App Development```를 선택하고 ```Continue```를 눌러 진행합니다.

![provisioning profiles app id](/assets/images/category/react-native/ios-enroll-developer-program/provisioning-profiles-app-id.png)

우리가 앱을 개발할 때 사용한 ```Bundle Identifier```를 선택합니다. ```Bundle Identifier```는 xcode에서 왼쪽 위 ```프로젝트명```을 선택하고 ```General``` 탭으로 이동하면 제일 상단에 ```Identity``` 항목에서 확인 할 수 있습니다.

![xcode bundle identifier](/assets/images/category/react-native/ios-enroll-developer-program/xcode-bundle-identifier.png)

선택을 완료하고 ```Continue```를 눌러 진행합니다. 인증서와 테스트 장치를 선택하고 다음으로 진행합니다.

![provisioning profiles name](/assets/images/category/react-native/ios-enroll-developer-program/provisioning-profiles-name.png)

최종적으로 프로비저닝 프로파일(Provisioning Profile)의 이름을 설정하고 ```Continue```를 눌러 다음으로 진행합니다.

프로비저닝 프로파일(Provisioning Profile)의 생성이 완료되었습니다. ```Download```를 눌러 파일을 다운로드한 후 알기 쉬운 곳에 보관해 둡니다.

### 인증서 등록
생성한 인증서를 ```키체인 접근```에 넣어줄 필요가 있습니다. ```키체인 접근```을 실행합니다.

![키체인 접근](/assets/images/category/react-native/ios-enroll-developer-program/ko-keychain.png)

아래와 같이 ```키체인 접근``` 창이 활성화 되면 왼쪽 하단에 ```내 인증서```를 선택하고 해당 화면에 위에서 생성한 인증서를 드래그해서 추가합니다.

위와 동일한 방식으로 ```Production```의 ```App store and Ad Hoc```의 인증서와 프로비저닝 프로파일(Provisioning Profile)도 생성하여 추가합니다.

### 인증서 설정 완료
애플 개발자 프로그램(Apple Developer Program) 등록 및 인증서 다운로드 절차가 완료되었습니다. ~~~이제 다운로드 받은 인증서를 사용하여 개발을 하면 됩니다. 이전 블로그 [디바이스 테스트]({{site.url}}/{{page.categories}}/app-store/){:target="_blank"}를 하신 분들은 이미 인증서가 연결이 된 상태입니다.~~~(연결된 인증서로 실패하여 내용을 수정합니다.)

### 인증서 연결
애플 개발자 사이트(Apple Developer)와 ```키체인 접근```에 등록한 인증서를 현재 프로젝트에 연결할 필요가 있습니다. RN(react native) 프로젝트 폴더에서 ```ios/프로젝트명.xcodeproj``` 파일을 실행시킵니다.

xcode에서 왼쪽 위 ```프로젝트명```을 선택하고 ```General``` 탭으로 이동합니다.

![xcode provisioning](/assets/images/category/react-native/ios-enroll-developer-program/xcode-provisioning.png)

위와 같은 화면이 보이면 ```Signing``` 섹션의 ```Automatically manage signing```을 클릭하여 체크박스를 해제합니다. 체크박스를 해제하면 화면과 같이 ```Signing(Debug)```와 ```Signing(Release)```섹션이 확성화됩니다. 둘다 ```Provision Profile``` 옆 드롭다운 메뉴를 선택하여 ```Import Profile```을 선택합니다.

위에서 생성하여 다운로드한 프로비저닝 프로파일(Provisioning Profile)을 선택합니다. 이제 모든 설정이 완료되었습니다.

## 안드로이드
안드로이드 부분은 우리가 실제로 등록하게 되면 이 부분에 설명하도록 하겠습니다.

## 완료
이제 개발자 등록이 완료되었습니다. 여기서 등록한 개발자 계정으로 ```testflight```를 이용하는 방법(iOS)와 앱스토어에 등록하는 방법에 대해서 알아보겠습니다.

- 배포 준비하기: [배포 준비]({{site.url}}/{{page.categories}}/prepare-release/){:target="_blank"}
- testflight를 이용하여 테스트하기: [testflight]({{site.url}}/{{page.categories}}/test-flight/){:target="_blank"}
- 앱스토어(App store)에 등록하기: [App store]({{site.url}}/{{page.categories}}/app-store/){:target="_blank"}