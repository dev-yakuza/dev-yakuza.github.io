---
layout: 'post'
permalink: '/react-native/android-running-on-device/'
paginate_path: '/react-native/:num/android-running-on-device/'
lang: 'ko'
categories: 'react-native'
comments: true

title: '안드로이드 빌드 및 테스트'
description: 'RN(react native)로 개발한 프로젝트를 안드로이드(Android)용으로 빌드하고 디바이스에서 테스트해봅시다.'
image: '/assets/images/category/react-native/android-running-on-device.jpg'
---


## 개요
지금까지 개발한 RN(react native)를 안드로이드(Android)용으로 빌드하여 디바이스에 올리고 테스트하는 방법을 소개하겠습니다. 여기에서는 Mac(맥)에서 안드로이드(Android)용 서명 키(Signing Key)를 생성하고 빌드할 예정입니다. 이 블로그는 RN(react native)의 공식 사이트를 참고하였으며 상세한 설명은 공식 사이트를 참고하시기 바랍니다.

- 공식 사이트: [https://facebook.github.io/react-native/docs/signed-apk-android](https://facebook.github.io/react-native/docs/signed-apk-android){:rel="nofollow noreferrer" target="_blank"}

## 안드로이드 서명 키 생성
Mac에서 ```터미널``` 프로그램을 열고 RN(react native) 프로젝트 폴더에 ```android/app``` 폴더로 이동합니다.

```bash
cd [your path]/android/app
```

아래에 명령어를 통해 안드로이드(Android)용 서명 키(Signing Key)를 발급합니다.

```bash
# keytool -genkey -v -keystore my-release-key.keystore -alias my-key-alias -keyalg RSA -keysize 2048 -validity 10000

keytool -genkey -v -keystore [key-name].keystore -alias [key alias] -keyalg RSA -keysize 2048 -validity 10000

Enter keystore password:
Re-enter new password:
What is your first and last name?
  [Unknown]:
What is the name of your organizational unit?
  [Unknown]:
What is the name of your organization?
  [Unknown]:
What is the name of your City or Locality?
  [Unknown]:
What is the name of your State or Province?
  [Unknown]:
What is the two-letter country code for this unit?
  [Unknown]:
Is CN=*****, OU=Unknown, O=Unknown, L=*****, ST=*****, C=***** correct?
  [no]:

Enter key password for <my-key-alias>
    (RETURN if same as keystore password):
```

전부 입력을 하고 나면 RN(react native) 프로젝트 폴더 하위에 ```android/app``` 폴더에 ```my-release-key.keystore``` 파일이 생성된 것을 확인할 수 있습니다.

## 서명 키 설정
서명 키(Signing Key)가 생성되면 ```gradle```에 키를 설정해야합니다. ```android/gradle.properties``` 파일을 열고 아래에 코드를 추가합니다.

```xml
MYAPP_RELEASE_STORE_FILE=my-release-key.keystore
MYAPP_RELEASE_KEY_ALIAS=my-key-alias
MYAPP_RELEASE_STORE_PASSWORD=*****
MYAPP_RELEASE_KEY_PASSWORD=*****
```

아래에 코드를 ```android/app/build.gradle``` 파일에 추가합니다.

```xml
...
android {
    ...
    defaultConfig { ... }
    signingConfigs {
        release {
            if (project.hasProperty('MYAPP_RELEASE_STORE_FILE')) {
                storeFile file(MYAPP_RELEASE_STORE_FILE)
                storePassword MYAPP_RELEASE_STORE_PASSWORD
                keyAlias MYAPP_RELEASE_KEY_ALIAS
                keyPassword MYAPP_RELEASE_KEY_PASSWORD
            }
        }
    }
    buildTypes {
        release {
            ...
            signingConfig signingConfigs.release
        }
    }
}
...
```

## 빌드
RN(react native)가 있는 프로젝트 폴더에서 ```android``` 폴더로 이동한 후 아래에 명령어로 빌드합니다.

```bash
./gradlew assembleRelease
```

빌드된 파일은 아래에 경로에 생성됩니다.

```bash
android/app/build/outputs/apk/release/app-release.apk
```

우리는 이 부분에서 아래와 같은 에러가 발생했습니다.

```bash
...
Execution failed for task ':app:lintVitalRelease'.
> Lint found fatal errors while assembling a release target.
...
```

좋은 방법은 아니지만, 우리는 ```android/app/build.gradle``` 파일에 아래에 내용을 추가하여 이 부분을 해결했습니다.

```xml
...
android {
  ...
  lintOptions {
      checkReleaseBuilds false
      // Or, if you prefer, you can continue to check for errors in release builds,
      // but continue the build even when errors are found:
      abortOnError false
  }
  ...
}
...
```


## 빌드된 파일 테스트
안드로이드 디바이스(Android Device)에 기존에 설치된 앱을 삭제하고 아래에 명령어를 실행하여 빌드 파일을 위한 테스트를 진행하세요.

```bash
react-native run-android --variant=release
```

## 에러 대응
공식 사이트에 내용을 통해 위와 같이 진행했지만 우리는 실제로 아래와 명령어를 통해 빌드 파일을 생성할 때와

```bash
./gradlew assembleRelease
```

아래에 명령어로 직접 디바이스에서 테스할 때,

```bash
react-native run-android --variant=release
```

아래와 같은 에러가 발생하였습니다.

```bash
java.lang.RuntimeException: Unable to load script from assets 'index.android.bundle'. Make sure your bundle is packaged correctly or you're running a packager server.
```

해결 방법으로 아래의 명령어를 먼저 입력하여 ```index.android.bundle```을 생성한 후

```bash
react-native bundle --platform android --dev false --entry-file index.js --bundle-output android/app/src/main/assets/index.android.bundle
```

빌드를 하거나

```bash
./gradlew assembleRelease
```

직접 디바이스에 올려 테스트했습니다.

```bash
react-native run-android --variant=release
```