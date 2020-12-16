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

<div id="contents_list" markdown="1">

1. [outline](#outline)
1. [isntall library](#isntall-library)
1. [link library](#link-library)
    - [Upper 0.60](#upper-060)
    - [Under 0.59](#under-059)
1. [create firebase project](#create-firebase-project)
1. [configure Google Admob](#configure-google-admob)
1. [set firebase in iOS](#set-firebase-in-ios)
1. [configure firebase in Android](#configure-firebase-in-android)
    - [change Android Package name](#change-android-package-name)
1. [add source](#add-source)
    - [Banner](#banner)
    - [Interstitial](#interstitial)
1. [Fix Error](#fix-error)
    - [admob/error-code-no-fill](#admoberror-code-no-fill)
1. [completed](#completed)

</div>

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

{% include in-feed-ads.html %}

## link library

We need to link react-native-firebase library to use it.

### Upper 0.60

execute below command to link react-native-firebase library to RN(react native) project.

```bash
cd ios
pod install
cd ..
```

### Under 0.59

execute below command to link react-native-firebase library to RN(react native) project.

```bash
react-native link react-native-firebase
```

## create firebase project

next, we need to create the project in Google Firebase. click below link to go to Google Firebase site.

- Google Firebase: [https://firebase.google.com](https://firebase.google.com){:rel="nofollow noreferrer" target="_blank"}

![google firebase](/assets/images/category/react-native/react-native-firebase-admob/google-firebase.jpg)

click ```SIGN IN``` button on the right top of the page to login.

![google firebase after login](/assets/images/category/react-native/react-native-firebase-admob/google-firebase-after-login.jpg)

after login, click ```GO TO CONSOLE``` on the right top of the page to go to Google Firebase Console.

![google firebase console](/assets/images/category/react-native/react-native-firebase-admob/google-firebase-console.jpg)

click ```+ Add project``` button in Google Firebase Console to add a project.

![google firebase console add project](/assets/images/category/react-native/react-native-firebase-admob/google-firebase-console-add-project.jpg)

insert the project informations and click ```Create project``` button to create the project.

## configure Google Admob

we need to configure advertisements in Google Admob. click ```Grow``` > ```Admob``` menu in Google Firebase Console. you can see below screen.

![google firebase console admob](/assets/images/category/react-native/react-native-firebase-admob/google-firebase-console-admob.jpg)

click ```linking your apps in Admob``` on the bottom middle of the page to go to Google Admob Page.

if you want to know how to set an advertisement in Google Admob, see [Google Admob]({{site.url}}/{{page.categories}}/react-native-admob/){:target="_blank"} blog and configure the advertisement.

{% include in-feed-ads.html %}

## set firebase in iOS

when you select the project in Google Firebase Console, you can see below screen.

![google firebase console project](/assets/images/category/react-native/react-native-firebase-admob/google-firebase-console-project.jpg)

click ```iOS``` button on the center of the screen to go to iOS configuration page.

![google firebase console project ios](/assets/images/category/react-native/react-native-firebase-admob/google-firebase-console-project-ios.jpg)

insert your app bundle ID and click ```Register app``` button.

![GoogleService-Info.plist download](/assets/images/category/react-native/react-native-firebase-admob/googleservice-info-plist-download.jpg)

download ```GoogleService-Info.plist``` file created by Google Firebase and copy to same location  of the ```info.plist```. after copying ```GoogleService-Info.plist```, click ```Next``` button.

![add Firebase SDK](/assets/images/category/react-native/react-native-firebase-admob/add-firebase-sdk.jpg)

add Google Firebase SDK to RN(react native) project followed the manual shown on the screen.

If React Native version is under 0.59, execute the command below.

```bash
pod init
```

add Google Firebase SDK to ```Podfile```.

```ruby
target 'blaboo' do
  ...
  pod 'Firebase/Core'
  pod 'Firebase/Analytics' // if you use Analytics
  pod 'Firebase/AdMob'
  ...
end
```

install Google Firebase SDK.

```bash
pod install
# pod update
```

![edit appdelegate.m for firebase](/assets/images/category/react-native/react-native-firebase-admob/edit-appdelegate.jpg)

add codes like below to ```AppDelegate.m``` file in RN(react native)

```js
...
@import Firebase;
...
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
  [FIRApp configure];
  ...
  return YES;
}
...
```

initialize Google Firebase SDK. And then, open `Info.plist` file and modify it like below.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	...
	<key>GADIsAdManagerApp</key>
	<true/>
	<key>GADApplicationIdentifier</key>
  <string>ca-app-pub-7987914246691031~8295071692</string>
</dict>
</plist>
```

Initialize Google Admob with App ID from Google Admob. if you don't know how to get App ID from Google Admob, see [Google Admob]({{site.url}}/{{page.categories}}/react-native-admob/){:target="_blank"} blog.

![connect firebase to app](/assets/images/category/react-native/react-native-firebase-admob/connect-firebase-to-app.jpg)

I clicked ```Skip this step``` in here.

{% include in-feed-ads.html %}

## configure firebase in Android

click ```Project Overview``` on the left top of Google Firebase Console.

![Google Firebase Console Project Overview](/assets/images/category/react-native/react-native-firebase-admob/firebase-project-overview.jpg)

click ```+ Add app``` > ```Android icon``` to go to Android project configuration.

![Google Firebase Android app register](/assets/images/category/react-native/react-native-firebase-admob/register-android.jpg)

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

- modify ```android/app/src/main/AndroidManifest.xml``` file

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

- modify  ```android/app/build.gradle``` file

  ```java
  ...
  defaultConfig {
      applicationId package_name
      ...
  }
  ...
  ```

![Google Firebase google-services.json setting](/assets/images/category/react-native/react-native-firebase-admob/set-google-services-json.jpg)

download ```google-services.json``` created by Google Firebase and copy it to RN(react native) ```android/app``` folder. and then, click ```Next``` button to go to next step.

![Google Firebase setting on android](/assets/images/category/react-native/react-native-firebase-admob/setting-android.jpg)

open ```android/build.gradle``` in RN(react native) folder and add below code.

```js
buildscript {
  repositories {
    google()
    jcenter()
  }
  dependencies {
    // Add this line
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

check ```google()``` is above ```jcenter()``` in ```repositories```.

open ```android/app/build.gradle``` in RN(react native) project and add below code.

```js
dependencies {
    implementation project(':react-native-firebase') // under 59 version
    ...
    implementation "com.google.android.gms:play-services-base:16.1.0"
    implementation 'com.google.firebase:firebase-core:16.0.9'
    implementation 'com.google.firebase:firebase-analytics:17.2.2' // if you use analytics
    implementation "com.google.firebase:firebase-ads:17.2.1"
}
```

and add below code in the bottom of same file.

```js
...
apply plugin: 'com.google.gms.google-services'
```

- Upper 0.60

Open ```android/app/src/main/java/com/[app name]/MainApplication.java``` file and modify it like below.

```java
import io.invertase.firebase.RNFirebasePackage;
import io.invertase.firebase.admob.RNFirebaseAdMobPackage;
import io.invertase.firebase.analytics.RNFirebaseAnalyticsPackage;
...
@Override
protected List<ReactPackage> getPackages() {
  @SuppressWarnings("UnnecessaryLocalVariable")
  List<ReactPackage> packages = new PackageList(this).getPackages();
  // Packages that cannot be autolinked yet can be added manually here, for example:
  // packages.add(new MyReactNativePackage());
  packages.add(new RNFirebaseAnalyticsPackage());
  packages.add(new RNFirebaseAdMobPackage());
  packages.add(new RNFirebaseCrashlyticsPackage());
  return packages;
}
...
```

Open ```android/app/src/AndroidManifest.xml``` file and modify it like below.

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
  package="io.github.dev.yakuza.blaboo">
    ...
    <application
      android:name=".MainApplication"
      android:label="@string/app_name"
      android:icon="@mipmap/ic_launcher"
      android:allowBackup="false"
      android:theme="@style/AppTheme">
      <meta-data
        android:name="com.google.android.gms.ads.APPLICATION_ID"
        android:value="ca-app-pub-7987914246691031~9800293270"/>
      ...
    </application>

</manifest>
```

- Under 0.59

Open ```android/app/src/main/java/com/[app name]/MainApplication.java``` file and modify it like below.

```java
import io.invertase.firebase.RNFirebasePackage;
import io.invertase.firebase.admob.RNFirebaseAdMobPackage;
import io.invertase.firebase.analytics.RNFirebaseAnalyticsPackage;
import com.google.android.gms.ads.MobileAds;
...

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

{% include in-feed-ads.html %}

## add source

completed to set react-native-firebase. now let's modify RN(react native) source to show Google Admob.

below source is react-native-firebase banner example.

```js
...
import firebase from 'react-native-firebase';
...
```

load react-native-firebase.

### Banner

below source code is the example about how to show Banner type advertisement(AD Unit is Banner) by ```react-native-firebase``` Admob.

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

add above source and execute RN(react native) project. you can see the Google Admob banner.

### Interstitial

below source code is the example about how to show Interstitial type advertisement(AD Unit is Interstitial) by ```react-native-firebase``` Admob.

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

you can use ```advert.show()``` function when you show Interstitial advertisement like below. you should call ```advert.isLoaded()``` to check the Interstitial advertisement is ready.

```js
setTimeout(() => {
  if (advert.isLoaded()) {
    advert.show();
  } else {
    // Unable to show interstitial - not loaded yet.
  }
}, 1000);
```

{% include in-feed-ads.html %}

## Fix Error

in here, I'll introduce my solution about the errors.

### admob/error-code-no-fill

finally, I got this message. suddenly my app didn't display the ads. when I debugged, I saw `admob/error-code-no-fill` message.

when I got `admob/error-code-no-fill` message, my payment status was $40(we can withdraw money at $80). at that time, I didn't register my payment way. after registering it, the ads showed up! maybe, google didn't have my payment information so, they can't pay money to me, so they adjusted the ads rating.

so, if you get `admob/error-code-no-fill` error message and you didn't give the payment information, insert it on the Admob settings.

{% include in-feed-ads.html %}

## completed

we introduced how to display Google Admob using react-native-firebase library in RN(react native) project. when you set react-native-firebase, Analytics is automatically configured.

click ```Analytics``` > ```Dashboard``` menu in Google Firebase Console. you can see Google Firebase analyzation.

![react native firebase analytics](/assets/images/category/react-native/react-native-firebase-admob/react-native-firebase-analytics.jpg)

