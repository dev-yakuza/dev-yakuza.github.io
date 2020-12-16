---
layout: 'post'
permalink: '/react-native/react-native-firebase-v6-installation/'
paginate_path: '/react-native/:num/react-native-firebase-v6-installation/'
lang: 'ko'
categories: 'react-native'
comments: true

title: react-native-firebase V6 설치
description: React Native에서 Firebase를 사용하기 위해 react-native-firebase(V6)을 설치하는 방법에 대해서 알아봅시다.
image: '/assets/images/category/react-native/2020/react-native-firebase-v6-installation/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [라이브러리 설치](#라이브러리-설치)
- [Firebase 프로젝트 생성](#firebase-프로젝트-생성)
- [iOS 설정](#ios-설정)
  - [Bundle ID 변경](#bundle-id-변경)
  - [Firbase iOS 프로젝트 설정](#firbase-ios-프로젝트-설정)
- [안드로이드 설정](#안드로이드-설정)
  - [안드로이드 패키지명 수정](#안드로이드-패키지명-수정)
  - [Firbase 안드로이드 프로젝트 설정](#firbase-안드로이드-프로젝트-설정)

</div>

## 개요

React Native 프로젝트에서 [Firebase](https://firebase.google.com/){:rel="nofollow noreferrer" target="_blank"}를 사용하기 위해 `react-native-firebase`를 설치하는 방법에 대해서 알아봅시다.

- react-native-firebase(V6): [https://rnfirebase.io/](https://rnfirebase.io/){:rel="nofollow noreferrer" target="_blank"}

react-native-firebase의 이전 버전(V5)을 사용하는 방법에 대해서는 아래에 블로그 리스트를 참고하시기 바랍니다.

- [Firebase Analytics]({{site.url}}/{{page.categories}}/react-native-firebase-analytics/){:target="_blank"}
- [Firebase Crashlytics]({{site.url}}/{{page.categories}}/firebase-crashlytics/){:target="_blank"}
- [Firebase Admob]({{site.url}}/{{page.categories}}/react-native-firebase-admob/){:target="_blank"}
- [react-native-firebase(V5)를 이용한 Push message]({{site.url}}/{{page.categories}}/react-native-firebase-fcm/){:target="_blank"}

이 블로그는 시리즈로 제작되어있습니다. 다른 내용을 확인하고 싶으신 분들은 아래에 블로그 리스트를 참고하시기 바랍니다.

- react-native-firebase V6 설치
- [react-native-firebase V6 Crashlytics]({{site.url}}/{{page.categories}}/react-native-firebase-v6-crashlytics/){:target="_blank"}
- [react-native-firebase V6 Admob]({{site.url}}/{{page.categories}}/react-native-firebase-v6-admob/){:target="_blank"}

## 라이브러리 설치

아래에 명령어를 사용하여 `react-native-firebase`를 설치합니다.

```bash
npm install --save @react-native-firebase/app
```

아래에 명령어를 사용하여 iOS 프로젝트에 react-native-firebase를 연결합니다.

```bash
cd ios
pod install
```

{% include in-feed-ads.html %}

## Firebase 프로젝트 생성

다음은 구글의 파이어베이스(Google Firebase)에서 프로젝트를 생성할 필요가 있습니다. 아래에 링크를 눌러 구글 파이어베이스(Google Firebase)로 이동합니다.

- 구글 파이어베이스(Google Firebase): [https://firebase.google.com](https://firebase.google.com){:rel="nofollow noreferrer" target="_blank"}

![google firebase](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/google-firebase.jpg)

오른쪽 위에 `SIGN IN` 버튼을 눌러 로그인합니다.

![google firebase after login](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/google-firebase-after-login.jpg)

로그인을 했다면 오른쪽 위에 `GO TO CONSOLE`을 눌러 구글 파이어베이스 콘솔(Google Firebase Console)로 이동합니다.

![google firebase console](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/google-firebase-console.jpg)

구글 파이어베이스 콘솔(Google Firebase Console)에서 `+ Add project`를 눌러 프로젝트를 추가합니다.

![google firebase console add project](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/google-firebase-console-add-project.jpg)

위와 같은 화면에서 `Enter your project name`에 만들고자하는 Firebase 프로젝트 이름을 입력합니다. 입력을 하였다면 하단에 있는 `Continue` 버튼을 눌러 다음으로 진행합니다.

![google firebase console add google analytics](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/google-firebase-console-add-google-analytics.jpg)

프로젝트 명을 입력하였다면, 위와 같이 `Google Analytics`을 연동하는 화면을 볼 수 있습니다. Google Analytics와 연동을 원하지 않는 경우, 왼쪽 하단의 스위치를 선택하여 `Disable`로 변경하고 Firebase 프로젝트를 생성합니다.

Google Analytics와 연동을 원하는 분들은 `Continue`를 눌러 진행합니다.

![google firebase console add integrate google analytics](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/google-firebase-console-integrate-google-analytics.jpg)

Google Analytics 계정을 선택하고, `Create project` 버튼을 눌러 Firebase 프로젝트를 생성합니다.

{% include in-feed-ads.html %}

## iOS 설정

react-native-firebase를 사용하기 위해 iOS를 설정하는 방법에 대해서 알아봅시다.

### Bundle ID 변경

Firebase에 iOS 프로젝트를 생성하기 전에, iOS의 `Bundle ID`를 변경할 필요가 있습니다. `ios/[project name].xcworkspace`를 선택하여 Xcode를 실행합니다.

![change ios bundle id](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/ios-change-bundle-id.jpg)

왼쪽 상단의 프로젝트 명을 선택하고 `General` 탭으로 이동하면, 상단에 `Bundle Identifier`를 확인할 수 있습니다. 이 Bundle ID를 자신의 프로젝트에 맞게 변경해 줍니다.

### Firbase iOS 프로젝트 설정

구글 파이어베이스 콘솔(Google Firebase Console)에서 프로젝트를 선택하면 다음과 같은 화면이 보입니다.

![google firebase console project](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/google-firebase-console-project.jpg)

중앙에 `iOS` 버튼을 눌러 iOS 설정 화면으로 이동합니다.

![google firebase console project ios](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/google-firebase-console-project-ios.jpg)

개발한 앱에 번들 ID(bundle ID)를 입력하고 `Register app` 버튼을 선택합니다.

![GoogleService-Info.plist download](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/googleservice-info-plist-download.jpg)

구글 파이어베이스(Google Firebase)가 생성한 `GoogleService-Info.plist` 파일을 다운로드하여 `info.plist`와 동일한 위치에 추가합니다. `GoogleService-Info.plist` 파일 추가를 완료했다면 `Next` 버튼을 클릭합니다.

![add Firebase SDK](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/add-firebase-sdk-google-analytics.jpg)

화면에 표시된 방식으로 구글 파이어베이스 SDK(Google Firebase SDK)를 React Native 프로젝트에 추가할 필요가 있습니다. `./ios/Podfile` 파일을 열고 아래와 같이 수정합니다.

```ruby
target 'blaboo' do
  ...
  pod 'Firebase/Analytics'
  ...
end
```

Google Analytics를 사용하지 않는 분들은 위와 같이 코드를 수정할 필요가 없습니다.

아래에 명령어를 통해 구글 파이어베이스 SDK(Google Firebase SDK)를 설치합니다.

```bash
pod install
# pod update
```

![edit appdelegate.m for firebase](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/edit-appdelegate.jpg)

React Native 프로젝트의 `AppDelegate.m` 파일에 아래와 같이 코드를 추가합니다.

```js
...
@import Firebase;

@implementation AppDelegate
...
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
  [FIRApp configure];
  ...
  return YES;
}
...
```

구글 파이어베이스 SDK(Google Firebase SDK)를 초기화합니다.

![connect firebase to app](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/connect-firebase-to-app.jpg)

저는 이 부분에서  `Skip this step`을 눌러 이 부분을 건너 뛰었습니다.

{% include in-feed-ads.html %}

## 안드로이드 설정

이제 react-native-firebase를 사용하기 위해 안드로이드를 설정하는 방법에 대해서 알아봅시다.

### 안드로이드 패키지명 수정

- React Native 프로젝트 폴더에서 `android/app/BUCK` 파일 수정

  ```xml
  ...
  android_build_config(
      ...
      package = "package_name",
  )
  ...
  android_resource(
      ...
      package = "package_name",
      ...
  )
  ...
  ```

- React Native 프로젝트 폴더에서 `android/app/src/main/AndroidManifest.xml` 파일 수정

  ```xml
  <manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="package_name">
  ...
  ```

- React Native 프로젝트 폴더에서 `android/app/src/main/java/com/ProjectName/MainActivity.java` 파일 수정

  ```java
  package package_name;
  ...
  ```

- React Native 프로젝트 폴더에서 `android/app/src/main/java/com/ProjectName/MainApplication.java` 파일 수정

  ```java
  package package_name;
  ...
  ```

- React Native 프로젝트 폴더에서 `android/app/build.gradle` 파일 수정

  ```java
  ...
  defaultConfig {
      applicationId package_name
      ...
  }
  ...
  ```

이렇게 패키지명을 변경하였다면, `android/app/src/main/java/com/[App Name]/MainActivity.java`으로 되어 있는 폴더 구조를 `android/app/src/main/java/[Package Name Folder]/MainActivity.java`과 같이 변경해줄 필요가 있습니다.

{% include in-feed-ads.html %}

### Firbase 안드로이드 프로젝트 설정

구글 파이어베이스 콘솔(Google Firebase Console)에서 왼쪽 상단의 `Project Overview`를 선택합니다.

![Google Firebase Console Project Overview](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/firebase-project-overview.jpg)

상단에 `+ Add app` > `안드로이드(Android) 아이콘`을 눌러 안드로이드(Android) 프로젝트 설정으로 이동합니다.

![Google Firebase Android app register](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/register-android.jpg)

안드로이드 패키지명(Android Package Name)을 입력하고 `Register app`을 선택합니다.

![Google Firebase google-services.json setting](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/set-google-services-json.jpg)

구글 파이어베이스(Google Firebase)가 만든 `google-services.json` 파일을 React Native 프로젝트의 `android/app` 폴더에 복사합니다. 그리고 `Next`버튼을 눌러 다음 단계로 진행합니다.

![Google Firebase setting on android](/assets/images/category/react-native/2020/react-native-firebase-v6-installation/setting-android.jpg)

React Native 프로젝트가 있는 폴더에서 `android/build.gradle` 파일을 열고 아래에 코드를 추가합니다.

```js
buildscript {
  repositories {
    google()
    jcenter()
  }
  dependencies {
    classpath("com.android.tools.build:gradle:3.5.2")
    classpath 'com.google.gms:google-services:4.3.3'
  }
}
...
allprojects {
  repositories {
    mavenLocal()
    google()
    jcenter()
    ...
  }
}
```

위와 같이 `repositories`에 `google()`이 포함되어 있어야 하며, `jcenter()`보다 위에 선언되어 있어야 됩니다.

React Native 프로젝트가 있는 폴더에서 `android/app/build.gradle` 파일을 열고 아래에 코드를 추가합니다.

```js
dependencies {
    // under 59 version
    // implementation project(':react-native-firebase')
    ...
    implementation 'com.google.firebase:firebase-analytics:17.2.2'
}
```

Google Analytics를 사용하지 않는 분들은 위 내용을 추가하지 않으셔도 됩니다. 그리고 동일한 파일 제일 하단에 아래에 코드를 추가합니다.

```js
...
apply plugin: 'com.google.gms.google-services'
```

다음은 `./android/build.gradle` 파일을 열고 아래와 같이 수정합니다.

```js
buildscript {
    ext {
        ...
    }
    repositories {
        ...
    }
    dependencies {
        classpath("com.android.tools.build:gradle:3.4.2")
        classpath 'com.google.gms:google-services:4.3.3'
    }
}
```

## 완료

이것으로 React Native에서 Firebase를 사용하기 위해 `react-native-firebae`를 설치하는 방법에 대해서 알아보았습니다. 다른 기능들을 추가하는 방법에 대해서는 아래에 링크를 참고하시기 바랍니다.

- [react-native-firebase V6 Crashlytics]({{site.url}}/{{page.categories}}/react-native-firebase-v6-crashlytics/){:target="_blank"}
- [react-native-firebase V6 Admob]({{site.url}}/{{page.categories}}/react-native-firebase-v6-admob/){:target="_blank"}