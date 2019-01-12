---
published: false
layout: 'post'
permalink: '/react-native/android-google-playstore/'
paginate_path: '/react-native/:num/android-google-playstore/'
lang: 'ko'
categories: 'react-native'
comments: true

title: '안드로이드 App store등록'
description: 'RN(React Native)로 개발한 안드로이드 앱(Android App)을 안드로이드 App store(Google Playstore)에 등록해 봅시다.'
image: '/assets/images/category/react-native/android-google-playstore.jpg'
---


## 개요
RN(React Native)로 개발한 안드로이드 앱(Android App)을 구글 플레이스토어(Google Playstore)에 등록하려고 합니다. 안드로이드 앱(Android App)을 구글 플레이스토어(Google Playstore)에 등록하기 위해서는 안드로이드 개발자 등록(구글 플레이 개발자 등록)이 필요합니다. 안드로이드 개발자 등록(구글 플레이 개발자 등록)을 하지 않으신 분은 이전 블로그를 참고하여 등록하시기 바랍니다.

- [안드로읻 개발자 등록]({{site.url}}/{{page.categories}}/android-enroll-google-play-developer/){:target="_blank"}

## 준비
RN(React Native)로 개발한 안드로이드 앱(Android App)을 구글 플레이스토어(Google Playstore)에 등록하기 위해서는 RN(React Native)를 안드로이드용으로 빌드할 필요가 있습니다. RN(React Native)에 안드로이드 서명키(Android Signing Key)를 등록하고 안드로이드용으로 빌드하는 방법에 대해서는 이전 블로그를 참고하시기 바랍니다.

- [안드로이드 빌드 및 테스트]({{site.url}}/{{page.categories}}/android-running-on-device/){:target="_blank"}

## 빌드 파일 사이즈 최적화
이전 블로그인 [안드로이드 빌드 및 테스트]({{site.url}}/{{page.categories}}/android-running-on-device/){:target="_blank"}에서 안드로이드용으로 빌드된 파일은 파일 사이즈의 최적화가 되어있지 않습니다. RN(React Native)로 개발한 안드로이드 앱(Android App)을 구글 플레이스토어(Google Playstore)에 업로드하기 위해서 빌드 파일 사이즈를 최적화할 필요가 있습니다.

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

![구글 플레이 콘솔 홈](/assets/images/category/react-native/android-google-playstore/google-play-console-home.png)

화면 상단에 보이는 ```PUBLISH AN ANDROID APP ON GOOGLE PLAY``` 버튼을 선택합니다.

![구글 플레이 콘솔 앱 타이틀](/assets/images/category/react-native/android-google-playstore/app-title.png)

구글 플레이스토어(Google Playstore)에 표시될 이름과 기본 언어를 선택합니다.

![구글 플레이 콘솔 앱 정보](/assets/images/category/react-native/android-google-playstore/app-info.png)

구글 플레이스토어(Google Playsotre)에 표시될 정보들을 입력합니다.

- 제목(title): 50자
- 요약 설명(short description): 80자
- 전체 설명(full description): 4000자
- 앱 이미지(Screenshots)
- 앱 아이콘(App icon): 512x512(32-bit PNG, alpha), 1024x500(JPG or 24-bit PNG), 180x120(JPG or 24-bit PNG), 1280x720(JPG or 24-bit PNG), 4096x4096(JPG or 24-bit PNG)
- 프로모션 비디오(Promo Video)
- 앱 카테고리(Category)
- 개발자 연락처(Contact details)
- 개인 정보 정책(Privacy Policy)