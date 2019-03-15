---
layout: 'post'
permalink: '/react-native/react-native-firebase-admob/'
paginate_path: '/react-native/:num/react-native-firebase-admob/'
lang: 'ko'
categories: 'react-native'
comments: true

title: 'Firebase Admob'
description: 'react-native-firebase 라이브러리를 사용하여 Google Admob을 표시해보자.'
image: '/assets/images/category/react-native/react-native-firebase-admob.jpg'
---


## 개요
우리는 구글 애드몹(Google Admob)을 사용하여 앱에 광고를 표시하고 있습니다. 이전에는 react-native-admob이라는 라이브러리를 사용했지만 구글 애드몹(Google Admob)이외에도 애널리틱스(Analytics)등 여러 기능을 사용하게 되어 통합적으로 사용할 수 있는 라이브러리를 찾다가 react-native-firebase라는 유용한 라이브러리를 찾게 되었습니다.

여기에서는 구글 파이어베이스(google firebase)를 사용하여 무료로 구글 애드몹(Google Admob), 애널리틱스(Analytics)를 사용하는 방법에 대해서 알아보겠습니다.

간단하게 구글 애드몹(Google Admob)만을 사용하고 싶으신 분은 이전 블로그인 [구글 애드몹(Google Admob)]({{site.url}}/{{page.categories}}/react-native-admob/){:target="_blank"}을 참고하시기 바랍니다.

아래에 링크는 react-native-firebase 라이브러리의 공식 페이지입니다. 자세한 내용은 공식 사이트에서 확인해 주세요.

- 공식 사이트: [react-native-firebase](https://github.com/invertase/react-native-firebase){:rel="nofollow noreferrer" target="_blank"}

## 라이브러리 설치
아래에 명령어를 사용하여 react-native-firebase 라이브러리를 설치합니다.

```bash
npm install --save react-native-firebase
```

## 라이브러리 링크
아래에 명령어를 사용하여 react-native-firebase 라이브러리를 RN(react native) 프로젝트에 연결합니다.

```bash
react-native link react-native-firebase
```

## firebase 프로젝트 생성
다음은 구글의 파이어베이스(Google Firebase)에서 프로젝트를 생성할 필요가 있습니다. 아래에 링크를 눌러 구글 파이어베이스(Google Firebase)로 이동합니다.

- 구글 파이어베이스(Google Firebase): [https://firebase.google.com](https://firebase.google.com){:rel="nofollow noreferrer" target="_blank"}

![google firebase](/assets/images/category/react-native/react-native-firebase-admob/google-firebase.png)

오른쪽 위에 ```SIGN IN``` 버튼을 눌러 로그인합니다.

![google firebase after login](/assets/images/category/react-native/react-native-firebase-admob/google-firebase-after-login.png)

로그인을 했다면 오른쪽 위에 ```GO TO CONSOLE```을 눌러 구글 파이어베이스 콘솔(Google Firebase Console)로 이동합니다.

![google firebase console](/assets/images/category/react-native/react-native-firebase-admob/google-firebase-console.png)

구글 파이어베이스 콘솔(Google Firebase Console)에서 ```+ Add project```를 눌러 프로젝트를 추가합니다.

![google firebase console add project](/assets/images/category/react-native/react-native-firebase-admob/google-firebase-console-add-project.png)

프로젝트 정보를 추가한 다음 ```Create project``` 버튼을 눌러 프로젝트를 생성합니다.

## 구글 애드몹 설정
구글 애드몹(Google Admob)에 광고를 설정해야 합니다. 구글 파이어베이스 콘솔(Google Firebas Console)의 ```Grow``` > ```Admob```을 선택하면 아래와 같은 화면을 볼 수 있습니다.

![google firebase console admob](/assets/images/category/react-native/react-native-firebase-admob/google-firebase-console-admob.png)

화면 중앙 하단에 ```linking your apps in AdMob.``` 링크를 누르면 구글 애드몹(Google Admob) 페이지로 이동됩니다.

구글 애드몹(Google Admob)에 광고를 설정하는 방법은 [구글 애드몹(Google Admob)]({{site.url}}/{{page.categories}}/react-native-admob/){:target="_blank"} 블로그를 참고하여 설정해 주시기 바랍니다.

## firebase iOS 설정
구글 파이어베이스 콘솔(Google Firebase Console)에서 프로젝트를 선택하면 다음과 같은 화면이 보입니다.

![google firebase console project](/assets/images/category/react-native/react-native-firebase-admob/google-firebase-console-project.png)

중앙에 ```iOS``` 버튼을 눌러 iOS 설정 화면으로 이동합니다.

![google firebase console project ios](/assets/images/category/react-native/react-native-firebase-admob/google-firebase-console-project-ios.png)

개발한 앱에 번들 ID(bundle ID)를 입력하고 ```Register app``` 버튼을 선택합니다.

![GoogleService-Info.plist download](/assets/images/category/react-native/react-native-firebase-admob/googleservice-info-plist-download.png)

구글 파이어베이스(Google Firebase)가 생성한 ```GoogleService-Info.plist``` 파일을 다운로드하여 ```info.plist```와 동일한 위치에 추가합니다. ```GoogleService-Info.plist``` 파일 추가를 완료했다면 ```Next``` 버튼을 클릭합니다.

![add Firebase SDK](/assets/images/category/react-native/react-native-firebase-admob/add-firebase-sdk.png)

화면에 표시된 방식으로 구글 파이어베이스 SDK(Google Firebase SDK)를 RN(react native) 프로젝트에 추가합니다.

```bash
pod init
```

구글 파이어베이스 SDK(Google Firebase SDK)를 ```Podfile```에 추가합니다.

```ruby
target 'blaboo' do
  # Uncomment the next line if you're using Swift or would like to use dynamic frameworks
  # use_frameworks!

  # Pods for blaboo
  pod 'Firebase/Core'
  pod 'Firebase/AdMob'

#  target 'blaboo-tvOS' do
#    inherit! :search_paths
#    # Pods for testing
#  end

  target 'blabooTests' do
    inherit! :search_paths
    # Pods for testing
  end

end
```

구글 파이어베이스 SDK(Google Firebase SDK) 설치를 설치합니다.

```bash
pod install
# pod update
```

![edit appdelegate.m for firebase](/assets/images/category/react-native/react-native-firebase-admob/edit-appdelegate.png)

RN(react native) 프로젝트의 ```AppDelegate.m``` 파일에 위와 같이 코드를 추가합니다.

```js
...
@import Firebase;
...
```

구글 파이어베이스 SDK(Google Firebase SDK)를 임포트합니다.

```js
...
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
...
[FIRApp configure];
...
RCTRootView *rootView = [[RCTRootView alloc] initWithBundleURL:jsCodeLocation
...
[GADMobileAds configureWithApplicationID:@"ca-app-pub-7987914246691031~8295071692"];
return YES;
...
```

구글 파이어베이스 SDK(Google Firebase SDK)를 초기화합니다. 그 다음 구글 애드몹(Google Admob)의 앱 ID(App ID)를 입력하여 구글 애드몹(Google Admobe)을 초기화합니다. 구글 애드몹의 앱 ID(App ID)를 얻는 방법은 이전 블로그인 [구글 애드몹(Google Admob)]({{site.url}}/{{page.categories}}/react-native-admob/){:target="_blank"}를 참고하시기 바랍니다.

![connect firebase to app](/assets/images/category/react-native/react-native-firebase-admob/connect-firebase-to-app.png)

우리는 이 부분에서  ```Skip this step```을 눌러 이 부분을 건너 뛰었습니다.

## firebase 안드로이드(Android) 설정
구글 파이어베이스 콘솔(Google Firebase Console)에서 왼쪽 상단의 ```Project Overview```를 선택합니다.

![Google Firebase Console Project Overview](/assets/images/category/react-native/react-native-firebase-admob/firebase-project-overview.png)

상단에 ```+ Add app``` > ```안드로이드(Android) 아이콘```을 눌러 안드로이드(Android) 프로젝트 설정으로 이동합니다.

![Google Firebase Android app register](/assets/images/category/react-native/react-native-firebase-admob/register-android.png)

안드로이드 패키지명(Android Package Name)을 입력하고 ```Register app```을 선택합니다.

RN(react native)에서 안드로이드 패키지명을 수정하고 싶으신 분은 아래에 항목을 진행해 주세요.

### 안드로이드 패키지명 수정
- RN(react native) 프로젝트 폴더에서 ```android/app/BUCK``` 파일 수정

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

- RN(react native) 프로젝트 폴더에서 ```android/app/src/main/AndroindManifest.xml``` 파일 수정

  ```xml
  <manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="package_name">
  ...
  ```

- RN(react native) 프로젝트 폴더에서 ```android/app/src/main/java/com/ProjectName/MainActivity.java``` 파일 수정

  ```java
  package package_name;
  ...
  ```

- RN(react native) 프로젝트 폴더에서 ```android/app/src/main/java/com/ProjectName/MainApplication.java``` 파일 수정

  ```java
  package package_name;
  ...
  ```

- RN(react native) 프로젝트 폴더에서 ```android/app/src/bundle.gradle``` 파일 수정

  ```java
  ...
  defaultConfig {
      applicationId package_name
      ...
  }
  ...
  ```

![Google Firebase google-services.json setting](/assets/images/category/react-native/react-native-firebase-admob/set-google-services-json.png)

구글 파이어베이스(Google Firebase)가 만든 ```google-services.json``` 파일을 RN(react native) 프로젝트의 ```android/app``` 폴더에 복사합니다. 그리고 ```Next```버튼을 눌러 다음 단계로 진행합니다.

![Google Firebase setting on android](/assets/images/category/react-native/react-native-firebase-admob/setting-android.png)

RN(react native) 프로젝트가 있는 폴더에서 ```android/build.gradle``` 파일을 열고 아래에 코드를 추가합니다.

```js
buildscript {
  repositories {
    google()
    jcenter()
  }
  dependencies {
    // Add this line
    classpath 'com.google.gms:google-services:4.0.1'
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

위와 같이 ```repositories```에 ```google()```이 포함되어 있어야 하며, ```jcenter()```보다 위에 선언되어 있어야 됩니다.

RN(react native) 프로젝트가 있는 폴더에서 ```android/app/build.gradle``` 파일을 열고 아래에 코드를 추가합니다.

```js
dependencies {
    implementation project(':react-native-firebase')
    ...
    implementation "com.google.android.gms:play-services-base:16.0.1"
    implementation 'com.google.firebase:firebase-core:16.0.4'
    implementation "com.google.firebase:firebase-ads:16.0.1"
}
```

그리고 동일한 파일 제일 하단에 아래에 코드를 추가합니다.

```js
...
apply plugin: 'com.google.gms.google-services'
com.google.gms.googleservices.GoogleServicesPlugin.config.disableVersionCheck = true
```

마지막으로 ```android/app/src/main/java/com/[app name]/MainApplication.java``` 파일에 아래와 같이 소스를 추가합니다.

```java
import io.invertase.firebase.RNFirebasePackage;
import io.invertase.firebase.admob.RNFirebaseAdMobPackage;
import io.invertase.firebase.analytics.RNFirebaseAnalyticsPackage;
import com.google.android.gms.ads.MobileAds;

@Override
protected List<ReactPackage> getPackages() {
  return Arrays.<ReactPackage>asList(
    ...
    new RNFirebasePackage(),
    new RNFirebaseAdMobPackage(),
    new RNFirebaseAnalyticsPackage(),
    ...
  );
}

@Override
public void onCreate() {
  super.onCreate();
  MobileAds.initialize(this, "ca-app-pub-7987914246691031~9800293270");
  ...
}
```

위에 소스에서 ```MobileAds.initialize(this, "ad app id");``` 부분에 구글 애드몹(Google Admob)에서 생성한 앱 아이디(App ID)를 추가합니다. 구글 애드몹(Google Admob)의 앱 아이디(App ID)를 생성하는 방법은 이전 블로그인 [구글 애드몹(Google Admob)]({{site.url}}/{{page.categories}}/react-native-admob/){:target="_blank"}을 참고하시기 바랍니다.

안드로이드 스튜디오(Android Studio)를 열면 ```Gradle```을 동기화할지 물어봅니다. ```Sync now```를 눌러 동기화 해줍니다.

## 소스 추가
react-native-firebase의 설정을 완료했습니다. 이제 RN(react native)의 코드를 수정하여 구글 애드몹(Google Admob)이 잘 표시되도록 합니다.

아래의 소스는 react-native-firebase를 사용하여 banner를 표시하는 예제입니다.

```js
...
import firebase from 'react-native-firebase';
...
```

react-native-firebase를 로딩합니다.

### 배너
아래의 소스코드는 ```react-native-firebase```의 애드몹(Admob)을 사용하여 광고 형식(AD Unit)이 배너(Banner)인 광고를 표시하는 예제입니다.

```js
import { Platform } from 'react-native';
...
render() {
    const Banner = firebase.admob.Banner;
    const AdRequest = firebase.admob.AdRequest;
    const request = new AdRequest();

    const unitId =
      Platform.OS === 'ios'
        ? 'ca-app-pub-7987914246691031/4248107679'
        : 'ca-app-pub-7987914246691031/5729668166';
    ...
    return (
        ...
        <Banner
          unitId={unitId}
          size={'SMART_BANNER'}
          request={request.build()}
          onAdLoaded={() => {
            console.log('Advert loaded');
          }}
        />
    );
```

위와 같이 소스를 추가하고 RN(react native) 프로젝트를 실행하면 배너가 잘 표시되는 것을 확인할 수 있습니다.

### 삽입 광고
아래의 소스코드는 ```react-native-firebase```의 애드몹(Admob)을 사용하여 광고 형식(AD Unit)이 삽입 광고(Interstitial, 전체페이지 광고)인 광고를 표시하는 예제입니다.

```js
import { Platform } from 'react-native';
...
componentDidMount() {
  ...
  const unitId =
    Platform.OS === 'ios'
      ? 'ca-app-pub-7987914246691031/4248107679'
      : 'ca-app-pub-7987914246691031/5729668166';
  const advert = firebase.admob().interstitial(unitId);
  const AdRequest = firebase.admob.AdRequest;
  const request = new AdRequest();
  advert.loadAd(request.build());

  advert.on('onAdLoaded', () => {
    console.log('Advert ready to show.');
    advert.show();
  });
  ...
}
...
```

위에 소스에서 알수 있듯이 ```react-native-firebase```의 애드몹(Admob)의 삽입 광고(Interstitial, 전체페이지 광고)를 표시하고 싶을 때 ```advert.show()```함수를 호출합니다. 호출하기 전에 항상 ```advert.isLoaded()``` 함수를 사용하여 광고가 준비되었는지 확인하시기 바랍니다.

```js
setTimeout(() => {
  if (advert.isLoaded()) {
    advert.show();
  } else {
    // Unable to show interstitial - not loaded yet.
  }
}, 1000);
```

## 완료
RN(react native) 프로젝트에 react-native-firebase 라이브러리를 사용하여 구글 애드몹(Google Admobe)을 적용하는 법을 살펴보았습니다. 이렇게 react-native-firebase를 설정하면 애널리틱스(Analytics)는 자동으로 설정되어 분석이 가능하게 됩니다.

구글 파이어베이스 콘솔(Google Firebase Console)의 메뉴에서 ```Analytics``` > ```Dashboard```를 선택하면, 분석을 하고 있는 것을 확인할 수 있습니다.

![react native firebase analytics](/assets/images/category/react-native/react-native-firebase-admob/react-native-firebase-analytics.png)