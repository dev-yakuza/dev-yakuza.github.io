---
layout: 'post'
permalink: '/react-native/react-native-firebase-admob/'
paginate_path: '/react-native/:num/react-native-firebase-admob/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'Firebase Admob'
description: let's use react-native-firebase library to display Google Admob.
image: '/assets/images/category/react-native/react-native-firebase-admob.jpg'
---


## outline
we used Google Admob to display advertisements. we've used react-native-admob library before, now we use react-native firebase because we wanted to use features like Google Admob, Analytics and so on.

in here, we introduce how to use freely Google Firebase for Google Admob and Analytics.

if you want to use simply Google admob only, see previous blog post - [Google Admob]({{site.url}}/{{page.categories}}/react-native-admob/){:target="_blank"} and check how to use react-native-admob library for Google Admob.

below link is react-native-firebase official page. you can see every details in official site.

- official site: [react-native-firebase](https://github.com/invertase/react-native-firebase){:rel="nofollow noreferrer" target="_blank"}

## isntall library
execute below command to install react-native-firebase library.

```bash
npm install --save react-native-firebase
```

## link library
execute below command to link react-native-firebase library to RN(react native) project.

```bash
react-native link react-native-firebase
```

## create firebase project.
next, we need to create the project in Google Firebase. click below link to go to Google Firebase site.

- Google Firebase: [https://firebase.google.com](https://firebase.google.com){:rel="nofollow noreferrer" target="_blank"}

![google firebase](/assets/images/category/react-native/react-native-firebase-admob/google-firebase.png)

click ```SIGN IN``` button on the right top of the page to login.

![google firebase after login](/assets/images/category/react-native/react-native-firebase-admob/google-firebase-after-login.png)

after login, click ```GO TO CONSOLE``` on the right top of the page to go to Google Firebase Console.

![google firebase console](/assets/images/category/react-native/react-native-firebase-admob/google-firebase-console.png)

click ```+ Add project``` button in Google Firebase Console to add a project.

![google firebase console add project](/assets/images/category/react-native/react-native-firebase-admob/google-firebase-console-add-project.png)

insert the project informations and click ```Create project``` button to create the project.

## configure Google Admob
we need to configure advertisements in Google Admob. click ```Grow``` > ```Admob``` menu in Google Firebase Console. you can see below screen.

![google firebase console admob](/assets/images/category/react-native/react-native-firebase-admob/google-firebase-console-admob.png)

click ```linking your apps in Admob``` on the bottom middle of the page to go to Google Admob Page.

if you want to know how to set an advertisement in Google Admob, see [Google Admob]({{site.url}}/{{page.categories}}/react-native-admob/){:target="_blank"} blog and configure the advertisement.

## set firebase in iOS
when you select the project in Google Firebase Console, you can see below screen.

![google firebase console project](/assets/images/category/react-native/react-native-firebase-admob/google-firebase-console-project.png)

click ```iOS``` button on the center of the screen to go to iOS configuration page.

![google firebase console project ios](/assets/images/category/react-native/react-native-firebase-admob/google-firebase-console-project-ios.png)

insert your app bundle ID and click ```Register app``` button.

![GoogleService-Info.plist download](/assets/images/category/react-native/react-native-firebase-admob/googleservice-info-plist-download.png)

download ```GoogleService-Info.plist``` file created by Google Firebase and copy to same location  of the ```info.plist```. after copying ```GoogleService-Info.plist```, click ```Next``` button.

![add Firebase SDK](/assets/images/category/react-native/react-native-firebase-admob/add-firebase-sdk.png)

add Google Firebase SDK to RN(react native) project followed the manual shown on the screen.

```bash
pod init
```

add Google Firebase SDK to ```Podfile```.

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

install Google Firebase SDK.

```bash
pod install
# pod update
```

![edit appdelegate.m for firebase](/assets/images/category/react-native/react-native-firebase-admob/edit-appdelegate.png)

add codes like below to ```AppDelegate.m``` file in RN(react native)

```js
...
@import Firebase;
...
```

import Google Firebase SDK.

```js
...
[FIRApp configure];
[GADMobileAds configureWithApplicationID:@"ca-app-pub-7987914246691031~8295071692"];
...
```

initialize Google Firebase SDK. and then, initialize Google Admob with App ID from Google Admob. if you don't know how to get App ID from Google Admob, see [Google Admob]({{site.url}}/{{page.categories}}/react-native-admob/){:target="_blank"} blog.

![connect firebase to app](/assets/images/category/react-native/react-native-firebase-admob/connect-firebase-to-app.png)

we clicked ```Skip this step``` in here.

## configure firebase in Android
click ```Project Overview``` on the left top of Google Firebase Console.

![Google Firebase Console Project Overview](/assets/images/category/react-native/react-native-firebase-admob/firebase-project-overview.png)

click ```+ Add app``` > ```Android icon``` to go to Android project configuration.

![Google Firebase Android app register](/assets/images/category/react-native/react-native-firebase-admob/register-android.png)

insert Nadroid Package Name and click ```Register app```.

if you want to change Android package name in RN(react native), do following section.

### change Android Package name
- modify ```android/app/BUCK``` file

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

- modify ```android/app/src/main/AndroindManifest.xml``` file

  ```xml
  <manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="package_name">
  ...
  ```

- modify ```android/app/src/main/java/com/ProjectName/MainActivity.java``` file

  ```java
  package package_name;
  ...
  ```

- modify ```android/app/src/main/java/com/ProjectName/MainApplication.java``` file

  ```java
  package package_name;
  ...
  ```

- modify  ```android/app/src/bundle.gradle``` file

  ```java
  ...
  defaultConfig {
      applicationId package_name
      ...
  }
  ...
  ```

![Google Firebase google-services.json setting](/assets/images/category/react-native/react-native-firebase-admob/set-google-services-json.png)

download ```google-services.json``` created by Google Firebase and copy it to RN(react native) ```android/app``` folder. and then, click ```Next``` button to go to next step.

![Google Firebase setting on android](/assets/images/category/react-native/react-native-firebase-admob/setting-android.png)

open ```android/build.gradle``` in RN(react native) folder and add below code.

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

check ```google()``` is above ```jcenter()``` in ```repositories```.

open ```android/app/build.gradle``` in RN(react native) project and add below code.

```js
dependencies {
    implementation project(':react-native-firebase')
    ...
    implementation "com.google.android.gms:play-services-base:16.0.1"
    implementation 'com.google.firebase:firebase-core:16.0.4'
    implementation "com.google.firebase:firebase-ads:16.0.1"
}
```

and add below code in the bottom of same file.

```js
...
apply plugin: 'com.google.gms.google-services'
com.google.gms.googleservices.GoogleServicesPlugin.config.disableVersionCheck = true
```

last, add below source to ```android/app/src/main/java/com/[app name]/MainApplication.java```.

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

set your App ID created in Google Admob to ```MobileAds.initialize(this, "ad app id");```. if you don't know how to create App ID in Google Admob, see [Google Admob]({{site.url}}/{{page.categories}}/react-native-admob/){:target="_blank"} blog.

open Android Studio and you can see ```Gradle``` sync question. click ```Sync now```.

## add source
completed to set react-native-firebase. now let's modify RN(react native) source to show Google Admob.

below source is react-native-firebase banner example.

```js
...
import firebase from 'react-native-firebase';
...
```

load react-native-firebase.

```js
render() {
    const Banner = firebase.admob.Banner;
    const AdRequest = firebase.admob.AdRequest;
    const request = new AdRequest();
    ...
    return (
        ...
        <Banner
          unitId="ca-app-pub-7987914246691031/7659403606"
          size={'SMART_BANNER'}
          request={request.build()}
          onAdLoaded={() => {
            console.log('Advert loaded');
          }}
        />
    );
```

add above source and execute RN(react native) project. you can see the Google Admob banner.

## completed
we introduced how to display Google Admob using react-native-firebase library in RN(react native) project. when you set react-native-firebase, Analytics is automatically configured.

click ```Analytics``` > ```Dashboard``` menu in Google Firebase Console. you can see Google Firebase analyzation.

![react native firebase analytics](/assets/images/category/react-native/react-native-firebase-admob/react-native-firebase-analytics.png)