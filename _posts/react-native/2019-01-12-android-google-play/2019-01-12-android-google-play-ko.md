---
layout: 'post'
permalink: '/react-native/android-google-play/'
paginate_path: '/react-native/:num/android-google-play/'
lang: 'ko'
categories: 'react-native'
comments: true

title: '안드로이드 앱 스토어 등록'
description: 'RN(React Native)로 개발한 안드로이드 앱(Android App)을 안드로이드 앱 스토어(Google Play)에 등록해 봅시다.'
image: '/assets/images/category/react-native/android-google-play.jpg'
---


## 개요
RN(React Native)로 개발한 안드로이드 앱(Android App)을 안드로이드 앱 스토어(Google Play)에 등록하려고 합니다. 안드로이드 앱(Android App)을 안드로이드 앱 스토어(Google Play)에 등록하기 위해서는 안드로이드 개발자 등록(구글 플레이 개발자 등록)이 필요합니다. 안드로이드 개발자 등록(구글 플레이 개발자 등록)을 하지 않으신 분은 이전 블로그를 참고하여 등록하시기 바랍니다.

- [안드로이드 개발자 등록]({{site.url}}/{{page.categories}}/android-enroll-google-play-developer/){:target="_blank"}

## 준비
RN(React Native)로 개발한 안드로이드 앱(Android App)을 안드로이드 앱 스토어(Google Play)에 등록하기 위해서는 RN(React Native)를 안드로이드용으로 빌드할 필요가 있습니다. RN(React Native)에 안드로이드 서명키(Android Signing Key)를 등록하고 안드로이드용으로 빌드하는 방법에 대해서는 이전 블로그를 참고하시기 바랍니다.

- [안드로이드 빌드 및 테스트]({{site.url}}/{{page.categories}}/android-running-on-device/){:target="_blank"}

## 빌드 파일 사이즈 최적화
이전 블로그인 [안드로이드 빌드 및 테스트]({{site.url}}/{{page.categories}}/android-running-on-device/){:target="_blank"}에서 안드로이드용으로 빌드된 파일은 파일 사이즈의 최적화가 되어있지 않습니다. RN(React Native)로 개발한 안드로이드 앱(Android App)을 안드로이드 앱 스토어(Google Play)에 업로드하기 위해서 빌드 파일 사이즈를 최적화할 필요가 있습니다.

RN(React Native) 프로젝트 폴더에서 ```android/app/build.gradle```을 열고 아래와 같이 수정합니다.

```
...
defaultConfig {
    ...
    // ndk {
    //     abiFilters "armeabi-v7a", "x86"
    // }
}
...
def enableSeparateBuildPerCPUArchitecture = true
```

그리고 아래의 명령어를 통해 RN(React Native)를 안드로이드용으로 빌드합니다.

```bash
# react-native bundle --platform android --dev false --entry-file index.js --bundle-output android/app/src/main/assets/index.android.bundle
# cd android
./gradlew assembleRelease
```

빌드된 파일은 아래의 경로에서 확인할 수 있습니다.

```bash
android/app/build/outputs/apk/release/app-armeabi-v7a-release.apk
android/app/build/outputs/apk/release/app-x86-release.apk
```

## 앱 등록
아래의 링크를 선택하여 구글 플레이 콘솔(Google Play Console)로 이동합니다.

- 구글 플레이 콘솔(Google Play Console): [https://play.google.com/apps/publish/](https://play.google.com/apps/publish/){:rel="nofollow noreferrer" target="_blank"}

구글 플레이 콘솔(Google Play Console)에 이동하면 아래와 같은 화면을 볼 수 있습니다.

![구글 플레이 콘솔 홈](/assets/images/category/react-native/android-google-play/google-play-console-home.png)

화면 상단에 보이는 ```PUBLISH AN ANDROID APP ON GOOGLE PLAY``` 버튼을 선택합니다.

![구글 플레이 콘솔 앱 타이틀](/assets/images/category/react-native/android-google-play/app-title.png)

안드로이드 앱 스토어(Google Play)에 표시될 이름과 기본 언어를 선택합니다.

![구글 플레이 콘솔 앱 정보](/assets/images/category/react-native/android-google-play/app-info.png)

안드로이드 앱 스토어(Google Play)에 표시될 정보들을 입력합니다.

- 제목(title): 50자
- 요약 설명(short description): 80자
- 전체 설명(full description): 4000자
- 앱 이미지(Screenshots)
- 앱 아이콘(App icon): 512x512(32-bit PNG, alpha), 1024x500(JPG or 24-bit PNG), 180x120(JPG or 24-bit PNG), 1280x720(JPG or 24-bit PNG), 4096x4096(JPG or 24-bit PNG)
- 프로모션 비디오(Promo Video)
- 앱 카테고리(Category)
- 개발자 연락처(Contact details)
- 개인 정보 정책(Privacy Policy)

모든 정보 입력이 끝났다면 이제 apk 파일을 등록하는 방법에 대해서 알아보겠습니다.

왼쪽 위에 ```App release``` 메뉴를 선택하면 아래와 같은 화면을 볼 수 있습니다.

![구글 플레이 앱 등록](/assets/images/category/react-native/android-google-play/app-register.png)

화면에서 보이는 ```Production track```의 ```Production``` 항목의 ```MANAGE```를 선택합니다.

![구글 플레이 앱 production 생성](/assets/images/category/react-native/android-google-play/app-production.png)

위와 같은 화면이 보이면 하단의 ```CREATE RELEASE```를 선택합니다.

![구글 플레이 앱 서명키 등록](/assets/images/category/react-native/android-google-play/register-signing-key.png)

구글 플레이(Google Play)를 이용하여 앱 서명(App Signing)을 하기 위해 ```FINISH``` 버튼을 선택합니다.

![구글 플레이 약관 동의](/assets/images/category/react-native/android-google-play/accept-agreement.png)

위와 같이 약관이 표시되면 하단의 ```ACCEPT``` 버튼을 눌러 동의합니다.

![구글 플레이 apk 업로드](/assets/images/category/react-native/android-google-play/app_apk.png)

위에서 빌드한 RN(React Native)의 ```apk``` 파일을 업로드합니다.

![구글 플레이 apk 릴리스 노트](/assets/images/category/react-native/android-google-play/app_release_note.png)

앱의 배포 이름(Release Name)과 배포 노트(Relase Note)를 작성하고 오른쪽 하단의 ```SAVE``` 버튼을 누릅니다. 그러면 오른쪽의 ```REVIEW``` 버튼이 활성화됩니다. 활성화된 ```REVIEW``` 버튼을 누릅니다.

![구글 플레이 등록 불가](/assets/images/category/react-native/android-google-play/not_yet.png)

앱 등록에 필요한 절차가 끝나지 않았기 때문에 오른쪽 하단의 ```START ROLLOUT TO PRODUCTION``` 버튼이 활성화되지 않았습니다. 왼쪽 메뉴의 ```Content rating```을 선택합니다.

![구글 플레이 콘텐츠 등급](/assets/images/category/react-native/android-google-play/app_content_rating.png)

콘텐츠 등급(Content Rating)을 설정하는 화면입니다. ```CONTINUE```를 선택합니다

![구글 플레이 콘텐츠 등급 정보 입력](/assets/images/category/react-native/android-google-play/app_content_rating_insert_info.png)

이메일 정보와 앱의 카테고리를 선택합니다.

![구글 플레이 콘텐츠 등급 정보 동의](/assets/images/category/react-native/android-google-play/app_content_rating_agreement.png)

앱에 콘텐츠 등급을 정하기 위한 정보를 선택합니다. 전부 선택하였다면 하단의 ```SAVE QUESTIONNAIRE``` 버튼을 선택하고 활성화된 ```CALCULATE RATING```을 선택합니다.

![구글 플레이 콘텐츠 등급 정보 선택 완료](/assets/images/category/react-native/android-google-play/app_content_rating_completed.png)

입력한 정보에 의해 콘텐츠 등급이 계산되어 나옵니다. 내용을 확인하고 하단의 ```APPLYING RATING```을 선택합니다.

![구글 플레이 콘텐츠 등급 완료](/assets/images/category/react-native/android-google-play/calculated_content_rating.png)

콘텐츠 등급 입력이 완료되었습니다. 콘텐츠 등급에 영향이 있는 업데이트가 있다면 콘텐츠 등급을 다시 계산하여 등록하셔야합니다.

![구글 플레이 콘텐츠 등급](/assets/images/category/react-native/android-google-play/content_rating.png)

이제 마지막 절차인 가격 설정으로 이동합니다. 왼쪽 메뉴의 ```Pricing & distribution```을 선택합니다.

![구글 플레이 앱 가격 정보](/assets/images/category/react-native/android-google-play/app_price_info.png)

앱의 가격을 설정하는 화면입니다. 우리는 무료로 앱을 제공할 예정이므로 ```FREE```를 설정하고 진행합니다. 또한 어린이 대상인지, 앱에 광고가 포함되었는지 등 정보를 입력합니다. 필수 항목을 전부 진행하였다면 하단의 ```SAVE DRAFT```를 선택합니다.

## 앱 심사 신청
드디어 앱 심사(App Review)를 위한 준비가 끝났습니다. 다시 메뉴의 ```App release```를 선택합니다.

![구글 플레이 앱 심사](/assets/images/category/react-native/android-google-play/app_review.png)

위에서 작성한 ```Production``` 항목 옆에 ```EDIT RELEASE``` 버튼을 선택합니다.

![구글 플레이 앱 심사 정보](/assets/images/category/react-native/android-google-play/app_review_info.png)

위에서 작성한 내용이 보입니다. 스크롤하여 하단으로 이동한 후, ```REVIEW``` 버튼을 선택합니다.

![구글 플레이 앱 심사 신청](/assets/images/category/react-native/android-google-play/apply_app_review_info.png)

위와 같은 화면이 보인다면 스크롤하여 하단으로 이동한 후 ```START ROLLOUT TO PRODUCTION``` 버튼을 선택합니다.

![구글 플레이 앱 등록](/assets/images/category/react-native/android-google-play/register_app.png)

앱 심사 준비가 끝났다면 ```CONFIRM``` 버튼을 눌러 앱 심사를 신청합니다.

## 완료
안드로이드 앱 스토어(Google Play)에 앱 등록을 위한 모든 절차가 끝났습니다. 앱 심사는 2~3시간 정도 걸리며 앱 심사가 끝나면 등록 신청을 한 앱을 안드로이드 앱 스토어(Google Play)에서 검색 및 다운로드 할 수 있습니다.