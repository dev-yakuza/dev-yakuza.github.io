---
published: false
layout: 'post'
permalink: '/react-native/ios-testflight/'
paginate_path: '/react-native/:num/ios-testflight/'
lang: 'ko'
categories: 'react-native'
comments: true

title: '(iOS)testflight'
description: 'iOS의 testflight를 이용하여 RN(react native)로 제작한 어플을 테스트해 보자.'
image: '/assets/images/category/react-native/ios-testflight.jpg'
---


## 개요
이전 블로그인 [개발자 등록]({{site.url}}/{{page.categories}}/enroll-developer-program/){:target="_blank"}을 잘 하신 분들은 이제 등록한 애플 개발자 계정(Apple Developer account)으로 ```testflight```를 사용하여 RN(react native)로 제작한 어플리케이션을 테스트해 봅시다.

## 앱 빌드
이전 블로그인 [빌드 및 테스트]({{site.url}}/{{page.categories}}/running-on-device/){:target="_blank"}를 통해 빌드를 하신 분들은 빌드하신 파일을 지우시고 진행하셔야 합니다.

### 빌드된 앱 삭제
애플 개발자 프로그램(Apple Developer Program) 등록전에 xcode의 ```Product```의 ```Archive``` 메뉴로 앱을 빌드한 적이 있다면 빌드된 앱을 삭제합니다.

![Organizer Menu](/assets/images/category/react-native/ios-testflight/organizer-menu.png)

xcode의 상단 메뉴중 ```Window```를 선택하고 ```Organizer```를 선택하여 빌드된 파일 리스트를 확인합니다. 이전에 빌드된 파일을 마우스 우클릭으로 선택하고 삭제합니다.

### 빌드
xcode의 상단 메뉴중 ```Product```의 ```Archive```를 선택하여 앱을 빌드합니다.

![build for production](/assets/images/category/react-native/ios-testflight/build-for-production.png)

### 앱 제출하기
위에 보이는 창(```Organizer```)에서 빌드한 앱을 선택한 후 ```Distribute App```을 선택하여 앱을 제출합니다. 앱 스토어(App store) 등록을 위한 제출이 ```App store connect```에 제출하는 것임으로 안심하고 눌러주세요.

![select platform](/assets/images/category/react-native/ios-testflight/select-platform.png)

위와 같이 플랫폼 설정 화면이 나오면 ```iOS App Store```를 선택하고 ```Next```를 눌러 다음 화면으로 진행합니다.

![select upload export](/assets/images/category/react-native/ios-testflight/upload-export.png)

개발한 앱을 ```Upload```할지 ```Export```할지 선택하는 화면이 나옵니다.

- Upload: xcode가 직접 빌드한 파일을 ```App Store Connect```에 업로드합니다.
- Export: 물리적인 ```.ipa```파일을 PC에 저장합니다.

우리는 ```Upload```를 선택하고 ```Next``` 버튼을 눌러 진행하도록 하겠습니다.

![select options](/assets/images/category/react-native/ios-testflight/options.png)

위와 같은 옵션 선택 화면이 나오면 디폴트로 설정된 값을 유지한 상태에서 ```Next```를 눌러 진행합니다.

인증서를 선택하는 화면이 나옵니다. 여기에서 사용할 인증서는 앱 스토어의 제출까지 가능한 인증서, 프로비저닝 프로파일(Provisioning Profile)을 사용해야 합니다. 이전 블로그인 [개발자 등록]({{site.url}}/{{page.categories}}/enroll-developer-program/){:target="_blank"}에서 이미 만들었으므로 인증서와 프로비저닝 프로파일(Provisioning Profile)가 없는 분은 이전 블로그를 참고해 주시기 바랍니다.

![Upload app](/assets/images/category/react-native/ios-testflight/upload.png)

최종적으로 ```Upload``` 버튼을 눌러 앱을 ```App Store Connect```에 업로드합니다.







빌드가 무사히 성공하면 ```Archives``` 창을 볼 수 있습니다. ```Archives``` 창을 실수로 닫으셨거나 다시 창을 열고 싶으신 분은 xcode 상단 메뉴의 ```Window```를 선택하고 ```Organizer```를 선택합니다.

![Organizer Menu](/assets/images/category/react-native/ios-testflight/organizer-menu.png)



## 어플 등록
RN(react native) 프로젝트로 제작한 어플을 ```testflight```에 등록하여 테스트가 가능한 상태를 만들어 보겠습니다. 아래에 링크를 눌러 애플 개발자(Apple Developer) 사이트로 이동합니다.

- 애플 개발자 사이트: [https://developer.apple.com/](https://developer.apple.com/){:rel="nofollow noreferrer" :target="_blank"}

오른쪽 위에 ```Account```를 눌러 Account 페이지로 이동합니다.

![apple developer site after enrolling](/assets/images/category/react-native/ios-testflight/apple-developer-site-after-enrolling.png)

위와 같은 페이지에서 ```App Store Connect```를 눌러 App store connector 사이트로 이동합니다.

![apple developer site after enrolling](/assets/images/category/react-native/ios-testflight/apple-developer-site-after-enrolling.png)

위와 같은 화면에서 ```나의앱```을 눌러 어플 등록 화면으로 이동합니다.

![ko empty app list](/assets/images/category/react-native/ios-testflight/ko-empty-app-list.png)

아직 등록한 앱이 없으므로 공백화면이 보입니다. 왼쪽 위에 ```+```버튼을 선택하고 ```신규 앱```을 선택하여 새로운 어플을 등록합니다.

![ko new app](/assets/images/category/react-native/ios-testflight/ko-new-app.png)

새로운 어플의 정보를 입력합니다. 우리는 이미 어플을 빌드한 상태이므로 번들ID에 빌드한 어플 선택이 가능합니다. 어플을 빌드하지 않으신 분은 이전 블로그인 [빌드 및 테스트]({{site.url}}/{{page.categories}}/running-on-device/){:target="_blank"}를 확인해 주세요. 사용자 액세스 권한은 전체 액세스, 플랫폼은 iOS를 선택하고 나머지 정보는 개발중인 어플에 맞춰 입력합니다. 다 입력하셨다면 ```생성```을 눌러 신규 앱 등록을 완료합니다.

상단 메뉴에 ```TestFlight```를 눌러 ```TestFlight``` 페이지로 이동합니다.

![ko testflight](/assets/images/category/react-native/ios-testflight/ko-testflight.png)

위와 같은 화면이 나오면 ```승인```을 눌러 창을 종료시킵니다.



앱 스토어에 등록할 정보를 입력하는 화면이 나옵니다. 해당 어플을 앱 스토어에 등록할 때 사용할 정보를 입력하세요. 실제로 심사에 들어가는 것이 아니기 때문에 너무 걱정할 필요없습니다.


## 테스터 추가
애플이 제공하는 ```testflight```를 사용하면 앱 스토어(App store)에 올리기전에 테스터들과 제작한 앱을 테스트할 수 있습니다. 그러기 위해서는 테스터를 추가해야합니다. 애플 개발자 프로그램(Apple Developer Program)에 등록한 계정으로만 테스트하시려는 분은 이 부분을 건너뛰셔도 됩니다. 아래에 링크를 클릭하여 애플 개발자 사이트로 이동합니다.

- 애플 개발자 사이트: [https://developer.apple.com/](https://developer.apple.com/){:rel="nofollow noreferrer" :target="_blank"}

![apple developer site](/assets/images/category/react-native/ios-testflight/apple-developer-site.png)

오른쪽 위에 ```Account```를 눌러 Account 페이지로 이동합니다.

![apple developer site after enrolling](/assets/images/category/react-native/ios-testflight/apple-developer-site-after-enrolling.png)

위와 같은 페이지에서 ```App Store Connect```를 눌러 App store connector 사이트로 이동합니다.

![ko app store connector](/assets/images/category/react-native/ios-testflight/ko-app-store-connector.png)

왼쪽 밑에 ```사용자 및 액세스``` 메뉴를 눌러 테스터 등록 페이지로 이동합니다.

![ko user access](/assets/images/category/react-native/ios-testflight/ko-user-access.png)

이미 애플 개발자 프로그램(Apple Developer Program)에 등록한 계정은 등록이 되어있습니다. 이제 새로운 테스터를 왼쪽 위에 ```+``` 버튼을 눌러 추가합시다.

![ko add user](/assets/images/category/react-native/ios-testflight/ko-add-user.png)

테스터의 이름과 이메일을 입력합니다. 여기서 사용하는 이메일은 애플 아이디(Apple ID), 즉 아이폰 앱스토어(App store)에서 어플을 다운로드 받으실 때 사용하는 이메일 또는 사용할 이메일을 입력합니다. 애플 아읻(Apple ID)가 아닌 경우 이 이메일을 사용하여 애플 아이디(Apple ID)를 등록하셔야 합니다. ```앱 관리```를 선택하고 하단에 ```초대``` 버튼을 눌러 테스터를 초대합니다. 특정 어플만 테스트하기 위해서는 ```앱``` 항목에서 특정 어플을 선택해 주세요.

![invite mail](/assets/images/category/react-native/ios-testflight/invite-mail.png)

입력한 테스터 메일에 초대 메일이 도착합니다. 초대 메일에서 ```activate your account``` 눌러 계정을 활성화 페이지로 이동합니다.

![activate account](/assets/images/category/react-native/ios-testflight/activate-account.png)

위와 같은 화면이 보이면 테스터로 등록한 아이디를 확인하고 패스워드를 입력합니다. 앱 스토어(App store) 아이디임으로 앱 스토어(App store)의 패스워드를 입력하시면 됩니다.

![privacy](/assets/images/category/react-native/ios-testflight/privacy.png)

약관을 확인하고 ```Continue```를 다음으로 진행합니다.

![trust browser](/assets/images/category/react-native/ios-testflight/trust-browser.png)

지금 사용하고 있는 웹브라우저가 신뢰가능한 브라우저인지 물어보는 화면이 나옵니다. 공용 PC가 아니라면 ```Trust```를 눌러 다음으로 진행합니다.

서비스 약관 화면이 나옵니다. 하단에 ```위의 서비스 약관을 읽었으며 이에 동의합니다.```를 선택하고 ```수락``` 버튼을 눌러 다음으로 진행합니다.

테스터 등록이 완료되었습니다. 이제 어플을 등록하고 실제 ```testflight```를 이용하는 방법에 대해서 알아보겠습니다.

