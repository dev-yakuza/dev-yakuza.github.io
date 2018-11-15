---
layout: 'post'
permalink: '/react-native/ios-testflight/'
paginate_path: '/react-native/:num/ios-testflight/'
lang: 'ko'
categories: 'react-native'
comments: true

title: 'iOS TestFlight'
description: 'iOS의 TestFlight를 이용하여 개발한 어플을 테스터를 통해 테스트해 보자.'
image: '/assets/images/category/react-native/ios-testflight.jpg'
---


## 개요
iOS는 개발한 앱을 배포하기 전에 자신의 테스터 또는 테스트 버전의 공개 URL을 사용하여 테스트할 수 있는 ```TestFlight``` 시스템을 가지고 있습니다. 여기에서는 ```TestFlight```를 이용하여 개발한 앱을 테스트하는 방법에 대해 알아보겠습니다.

이 블로그는 아래에 과정을 끝내신 분을 위한 블로그입니다.
- [iOS 디바이스 테스트]({{site.url}}/{{page.categories}}/ios-test-on-device/){:target="_blank"}
- [iOS 빌드 및 테스트]({{site.url}}/{{page.categories}}/ios-running-on-device/){:target="_blank"}
- [iOS 개발자 등록]({{site.url}}/{{page.categories}}/ios-enroll-developer-program/){:target="_blank"}
- [iOS 인증서(Certification)]({{site.url}}/{{page.categories}}/ios-certification/){:target="_blank"}

애플 개발자 프로그램(Apple Developer Program) 등록이나 인증서(Certification) 설정에 관해서는 위에 블로그 내용을 참고하시기 바랍니다.


## 배포용 앱 생성
애플이 제공하는 ```TestFlight```를 사용하여 앱을 테스트할 경우 앱 스토어 커넥트(Apple Store Connect)에 배포용 앱을 생성해야합니다. 아래에 링크를 눌러 앱 스토어 커넥트(App Store Connect)에 이동합니다.

- 앱 스토어 커넥트(App Store Connect): [https://appstoreconnect.apple.com/](https://appstoreconnect.apple.com/){:rel="nofollow noreferrer" :target="_blank"}

![App Store Connect](/assets/images/category/react-native/ios-testflight/app-store-connect.png)

애플 개발자 프로그램(Apple Developer Program)에 등록한 개발자 아이디로 로그인합니다. 애플 개발자 프로그램(Apple Developer Program)에 등록하지 않은 분은 [iOS 개발자 등록]({{site.url}}/{{page.categories}}/ios-enroll-developer-program/){:target="_blank"} 블로그를 참고하여 등록하시기 바랍니다.

로그인을 하고 나면 아래와 같은 화면을 볼 수 있습니다. ```나의 앱```을 선택하여 앱 관리 페이지로 이동합니다.

![앱 스토어 커넥트 메인](/assets/images/category/react-native/ios-testflight/ko-app-store-connect-main.png)

왼쪽 위에 ```+``` 버튼을 누르고 ```신규 앱``` 메뉴를 선택합니다.

![앱 리스트](/assets/images/category/react-native/ios-testflight/ko-app-list.png)

앱 등록 화면이 나옵니다. 자신의 앱 정보를 입력합니다. 잘 모르는 부분이 있으면 항목 타이틀 옆 ```?```를 눌러 확인합니다. 이름과 기본 언어는 나중에 변경이 가능합니다.

![앱 생성](/assets/images/category/react-native/ios-testflight/ko-new-app.png)

- 번들 ID: 앱을 개발할 때 사용한 ```bundle ID```입니다. 어디에 있는지 잘 모르시는 분은 이전 블로그인 [iOS 디바이스 테스트]({{site.url}}/{{page.categories}}/ios-test-on-device/){:target="_blank"}에서 확인해 주세요.
- SKU: App Store에 표시되지 않는 앱의 고유한 ID입니다. 보통 URL 형식으로 작성합니다.(ex> io.github.dev-yakuza.blaboo)

![앱 메뉴](/assets/images/category/react-native/ios-testflight/ko-app-menu.png)

앱을 생성하고 나면 위와 같이 메뉴를 볼 수 있습니다. 메뉴중 ```TestFlight``` 메뉴를 선택합니다.

개발한 앱을 ```TestFlight```를 사용하여 테스트하기 위해서는 배포를 위해 빌드되고 앱 스토어 커넥트(App Store Connect)에 업로드를 해야합니다.

## 앱 빌드
개발된 앱을 빌드하여 앱스토어 커넥트(App Store Connect)에 업로드하는 방법을 알아보겠습니다. 이미 빌드한 파일이 있으신 분은 이 부분을 건너뛰셔도 좋습니다.

RN(react native) 프로젝트 폴더에 ```ios/프로젝트명.xcodeproj``` 파일을 실행시킵니다.

![build for production](/assets/images/category/react-native/ios-testflight/build-for-production.png)

xcode가 실행되면 상단 메뉴에서 ```Product``` > ```Archive```를 선택합니다. 애플 개발자 프로그램(Apple Developer Program)에 등록하지 않은 분이나 인증서를 연결하지 않으신 분은 이전 블로그를 확인해 주세요.([iOS 개발자 등록]({{site.url}}/{{page.categories}}/ios-enroll-developer-program/){:target="_blank"}, [iOS 인증서(Certification)]({{site.url}}/{{page.categories}}/ios-certification/){:target="_blank"})

빌드가 무사히 끝나면 아래와 같은 화면을 볼 수 있습니다.

![build for production](/assets/images/category/react-native/ios-testflight/distribute-app.png)

## 앱 업로드
빌드 완료후 보이는 화면을 실수로 닫으셨거나 이미 빌드한 파일을 가지고 계신 분은 xcode 상단 메뉴에서 ```Window``` > ```Organizer```를 선택합니다.

![organizer menu](/assets/images/category/react-native/ios-testflight/organizer-menu.png)

메뉴를 선택하거나 빌드를 완료하신 분은 아래와 같은 화면이 보입니다.

![build for production](/assets/images/category/react-native/ios-testflight/distribute-app.png)

오른쪽에 보이는 ```Distribute App```을 선택합니다. 앱을 배포하는 것이 아니라 앱을 앱 스토어 커넥트(App Store Connect)에 업로드하는 과정입니다.

![select platfom](/assets/images/category/react-native/ios-testflight/select-platform.png)

개발한 앱을 배포할 플랫폼을 선택합니다. 우리는 ```iOS App Store```를 선택하고 진행합니다.

![upload or export](/assets/images/category/react-native/ios-testflight/upload-export.png)

최종 목적지로 앱 스토어 커넥트(App Store Connect)에 업로드할지 ipa파일로 내보낼지(export) 선택하는 화면이 나옵니다. 우리는 앱 스토어 커넥트(App Store Connect)에 업로드할 예정임으로 ```Upload```를 선택합니다.

![options](/assets/images/category/react-native/ios-testflight/options.png)

옵션 선택 화면이 나옵니다. 옵션이 모두 선택된 상태에서 ```Next```를 선택합니다. 다음 화면에서 생성한 인증서와 프로비저닝 프로파일(Provisioning Profile)을 선택합니다. 인증서, 프로비저닝 프로파일(Provisioning Profile) 생성은 이전 블로그인 [iOS 인증서(Certification)]({{site.url}}/{{page.categories}}/ios-certification/){:target="_blank"}를 확인해 주세요.

배포 준비가 끝나면 아래와 같은 화면을 볼 수 있습니다. ```Upload``` 버튼을 눌러 준비된 파일을 앱 스토어 커넥트(App Store Connect)에 업로드합니다.

![upload](/assets/images/category/react-native/ios-testflight/upload.png)

무사히 앱을 앱스토어 커넥트(App Store Connect)에 업로드하였습니다. 업로드한 파일을 사용할 준비가 되면 애플에서 메일이 옵니다. 업로드에서 메일 도착까지 조금 시간이 걸립니다.

## 테스트 그룹 생성
애플에서 메일을 받으신 분들은 앱 스토어 커넥트(App Store Connect) 페이지의 ```TestFlight``` 페이지로 이동합니다.

![빌드 파일 리스트](/assets/images/category/react-native/ios-testflight/ko-testflight-build-file-list.png)

위와 같이 ```TestFlight``` 화면에 업로드된 파일이 보입니다. 왼쪽 밑에 ```새 그룹 +```를 눌러 테스트를 위한 그룹을 생성합니다.

![테스트 그룹 생성](/assets/images/category/react-native/ios-testflight/ko-create-test-group.png)

테스트 그룹을 생성하면 왼쪽 메뉴에 생성시 사용한 그룹명이 추가됩니다. 그룹명을 선택합니다.

![테스트 그룹](/assets/images/category/react-native/ios-testflight/ko-test-group.png)

테스트 그룹 생성이 완료되었습니다. 이제 빌드 파일, 테스터를 추가하여 테스트를 진행해 봅시다.

## 빌드 추가
테스트 그룹을 선택한 상태에서 상단에 있는 ```빌드``` 탭을 선택합니다.

![빌드 탭 선택](/assets/images/category/react-native/ios-testflight/ko-build-tab.png)

빌드 탭에서 ```빌드(0)```옆에 ```+``` 버튼을 눌러 빌드를 선택하는 화면으로 이동합니다. 테스트하고 싶은 빌드를 선택하고 하단에 ```다음``` 버튼을 누릅니다.

![빌드 선택](/assets/images/category/react-native/ios-testflight/ko-select-build.png)

테스트에 로그인 정보가 필요한지 선택하는 화면이 나옵니다. 앱을 테스트할 때 로그인 정보가 필요하면 ```로그인 필요```를 선택하고 아이디/암호를 넣고 ```다음``` 버튼을 누릅니다.

![로그인 필요](/assets/images/category/react-native/ios-testflight/ko-need-login.png)

아래에 화면에서 테스터에게 전달할 메세지 또는 테스트 하는 방법에 대해 작성하고 ```심사를 위해 제출```버튼을 누릅니다.

![메시지 작성](/assets/images/category/react-native/ios-testflight/ko-test-message.png)

테스터에게 테스트를 부탁하기 위한 ```TestFlight```이지만, 기본적으로 간단한 심사 작업이 있습니다. 따라서 테스터들에게 테스트를 바로 부탁할 수 없습니다. 심사가 끝난 후 테스트가 가능하게 됩니다.

## 테스터 추가
애플이 제공하는 ```TestFlight```는 크게 두가지 기능이 있습니다. 자신이 알고 있는 테스터를 추가하는 방법과 공개 URL을 생성하여 이 링크를 배포하는 방법입니다. 우선 테스터를 추가하는 방법에 대해 알아보겠습니다. ```TestFlight```에서 테스트 그룹을 선택하고 ```테스터(0)```옆에 ```+``` 버튼을 선택하고 ```새로운 테스터 추가``` 메뉴를 선택합니다.

![새로운 테스터 추가](/assets/images/category/react-native/ios-testflight/ko-add-new-tester.png)

새로 추가할 테스터의 이메일, 이름을 입력하고 ```추가``` 버튼을 누릅니다. 추가할 테스터의 이메일을 앱 스토어(App Store)에서 앱을 다운로드할 때 사용하는 이메일이여야 합니다.

![새로운 테스터 추가 완료](/assets/images/category/react-native/ios-testflight/ko-added-new-tester.png)

새로운 테스터가 추가되었습니다. 새롭게 추가된 테스테에게는 ```TestFlight``` 메일이 발송됩니다.

![testflight email](/assets/images/category/react-native/ios-testflight/testflight-email.png)

테스터는 앱 스토어(App store)에서 ```TestFlight```를 검색하여 다운로드하여 앱 테스트를 하면 됩니다.

## 공개 링크
공개 링크를 선택해서 작업을 맞치면 공개 링크가 생성됩니다. 그 링크를 복사하여 공유면 테스트 참여가 가능하게 됩니다.

## 완료
이것으로 ```TestFlight```를 활용하는 간단한 방법에 대해서 살펴보았습니다. 다음 블로그에서는 실제 앱을 배포하는 방법에 대해 알아보겠습니다.