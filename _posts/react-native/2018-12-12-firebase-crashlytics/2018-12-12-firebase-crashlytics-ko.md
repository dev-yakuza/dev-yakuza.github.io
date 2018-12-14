---
layout: 'post'
permalink: '/react-native/firebase-crashlytics/'
paginate_path: '/react-native/:num/firebase-crashlytics/'
lang: 'ko'
categories: 'react-native'
comments: true

title: 'Firebase Crashlytics'
description: 'react-native-firebase를 사용하여 파이어베이스(Firebase)의 Crashlytics로 앱에서 crash가 발생했을 때 내용을 수집해봅시다.'
image: '/assets/images/category/react-native/firebase-crashlytics.jpg'
---


## 개요
이전 블로그([iOS App crash 분석]({{site.url}}/{{page.categories}}/ios-app-crash-debugging/){:target="_blank"})에서 앱 심사 거부(reject)에 첨부된 App crash log를 분석해 보았습니다. 하지만 심사중이 아니라 사용자가 사용하고 있는 환경에서 crash가 발생하면 알수가 없습니다. 그래서 파이어베이스(Firebase)의 Crashlytics를 사용해 앱 crash를 수집하고 분석해 보도록 하겠습니다. 이 블로그에서는 react-native-firebase 라이브러리를 사용할 예정입니다. react-native-firebase 라이브러리 설치 및 설정은 이전 블로그를 확인해 주세요.

- [Firebase Admob]({{site.url}}/{{page.categories}}/react-native-firebase-admob/){:target="_blank"}

## iOS 설정
파이어베이스(Firebase)의 Crashlytics를 사용하기 위해 react-native-firebase를 설정하겠습니다.

### 필요한 라이브러리 설정 및 설치
iOS에 필요한 라이브러리를 아래와 같이 ```Podfile```에 추가합니다.

```ruby
...
pod 'Firebase/Core'
pod 'Firebase/AdMob'
pod 'Fabric'
pod 'Crashlytics'
...
```

추가한 라이브러리를 아래에 ```pod``` 명령어로 설치합니다.

```bash
# cd ios
pod update
```

### Crashlytics 실행 스크립트 추가
파이어베이스(Firebase)의 Crashlytics를 사용하기 위해 Crashlytics 실행 스크립트를 추가해야 합니다.

RN(react native) 프로젝트 폴더에서 ```ios/[AppName].xcworkspace```를 선택하여 Xcode를 실행합니다.

![xcode 실행](/assets/images/category/react-native/firebase-crashlytics/execute_xcode.png)

왼쪽에 있는 파일 탐색기와 ```TARGETS```에서 자신의 프로젝트를 선택합니다. 그리고 위쪽에 메뉴에서 ```Build Phases```를 선택합니다.

![xcode build phases](/assets/images/category/react-native/firebase-crashlytics/build_phases.png)

Build Phases 탭에서 왼쪽 위에 ```+``` 버튼을 누르고 ```New Run Script Phase```를 선택합니다.

![new run script menu on build phases](/assets/images/category/react-native/firebase-crashlytics/new_run_script.png)

아래에 명령어를 ```Run Script```의 ```Shell```하단에 ```# Type a script...```가 있는 입력창에 입력합니다.

```bash
"${PODS_ROOT}/Fabric/run"
```

![add Run Script](/assets/images/category/react-native/firebase-crashlytics/add_run_script.png)

### 테스트
지금까지 설정한 파이어베이스(Firebase)의 Crashlytics를 테스트하기 위해 아래에 코드를 테스트 하고 싶은 위치에 추가합니다.

```js
firebase.crashlytics().crash();
```

이 부분은 강제로 앱을 crash하게 만드는 코드입니다. 앱이 crash가 발생하여 종료되었다면 파이어베이스(Firebase)의 Crashlytics에 보고할 수 있도록 앱을 다시 실행시킵니다.

아래에 명령어 또는 xcode를 사용하여 시뮬레이터를 기동 시킵니다.

```bash
react-native run-ios
```

xcode를 이용하여 시뮬레이터를 기동하신 분들은 xcode를 종료하고 시뮬레이터에서 앱을 선택하여 다시 기동해야 합니다. xcode가 기동된 상태에서 crash가 날 경우 Crashlytics까지 보고가 들어가지 않고 xcode에서 crash를 처리하게 됩니다.

crash가 발생하고 앱을 다시 기동합니다. 조금 시간이 지나면 파이어베이스 콘솔(Firebase Console)의 Crashlytics에서 아래와 같은 내용을 확인할 수 있습니다.

![Firebase Console Crashlytics](/assets/images/category/react-native/firebase-crashlytics/firebase_crashlytics.png)

주의: 테스트 코드(```firebase.crashlytics().crash();```)는 확인이 완료되면 꼭 삭제해 주시기 바랍니다.

## 안드로이드 설정
안드로이드(Android)에서 파이어베이스(Firebase)의 Crashlytics를 사용하기 위해 react-native-firebase를 설정하겠습니다.

### 필요한 라이브러리 설정 및 설치
아래와 같이 ```android/app/build.gradle``` 파일을 수정합니다.

```xml
apply plugin: "com.android.application"
apply plugin: 'io.fabric'
...
dependencies {
  ...
  implementation('com.crashlytics.sdk.android:crashlytics:2.9.5@aar') {
    transitive = true
  }
}
...
```

아래와 같이 ```android/build.gradle``` 파일을 수정합니다.

```xml
...
buildscript {
  ...
  dependencies {
    ...
    classpath 'com.google.gms:google-services:4.0.1'
    classpath 'io.fabric.tools:gradle:1.25.4'
  }
  ...
  repositories {
    ...
    jcenter()
    maven {
        url 'https://maven.fabric.io/public'
    }
  }
  ...
}
...
```

아래와 같이 ```android/app/src/main/java/com/[app name]/MainApplication.java``` 파일을 수정합니다.

```java
...
import io.invertase.firebase.RNFirebasePackage;
import io.invertase.firebase.fabric.crashlytics.RNFirebaseCrashlyticsPackage;
...
    @Override
    protected List<ReactPackage> getPackages() {
      return Arrays.<ReactPackage>asList(
          ...
          new RNFirebasePackage(),
          new RNFirebaseCrashlyticsPackage(),
          ...
      );
    }
...
```

### 테스트
지금까지 설정한 파이어베이스(Firebase)의 Crashlytics를 테스트하기 위해 아래에 코드를 테스트 하고 싶은 위치에 추가합니다.

```js
firebase.crashlytics().crash();
```

안드로이드(Android)에서는 에뮬레이터를 기동하고 ```react-native run-android```로 실행하여 crash를 발생하면 빨간 에러화면이 나와 실제로 crash가 보고되지 않습니다. 그래서 우리는 에뮬레이터에 빌드된 파일을 설치하여 테스트하였습니다. 안드로이드(Android) 빌드 및 테스트에 관해서는 [안드로이드 빌드 및 테스트]({{site.url}}/{{page.categories}}/android-running-on-device/){:target="_blank"}를 참고해 주세요.

```bash
react-native bundle --platform android --dev false --entry-file index.js --bundle-output android/app/src/main/assets/index.android.bundle
```

위에 명령어를 사용하여 javascript를 빌드한 후, 아래에 명령어로 에뮬레이터에 빌드된 파일을 설치합니다.

```bash
react-native run-android --variant=release
```

그리고 테스트하면 아래와 같이 안드로이드(Android)에서도 crash 보고를 받을 수 있습니다.

![Firebase Console Crashlytics android](/assets/images/category/react-native/firebase-crashlytics/firebase_crashlytics_android.png)

주의: 테스트 코드(```firebase.crashlytics().crash();```)는 확인이 완료되면 꼭 삭제해 주시기 바랍니다.

## 참고
- [https://firebase.google.com/docs/crashlytics/get-started](https://firebase.google.com/docs/crashlytics/get-started){:rel="nofollow noreferrer" target="_blank"}
- [https://rnfirebase.io/docs/v5.x.x/crashlytics/ios](https://rnfirebase.io/docs/v5.x.x/crashlytics/ios){:rel="nofollow noreferrer" target="_blank"}