---
layout: 'post'
permalink: '/react-native/firebase-crashlytics/'
paginate_path: '/react-native/:num/firebase-crashlytics/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'Firebase Crashlytics'
description: let's see how to use react-native-firebase to gather crash logs on Filebase Crashlytics.
image: '/assets/images/category/react-native/firebase-crashlytics.jpg'
---


## outline
we've introduced how to analyze App crash Log from App review rejection at previous blog([iOS App crash analysis]({{site.url}}/{{page.categories}}/ios-app-crash-debugging/){:target="_blank"}). however, if App is in user environment not review status and crashed, we can't know App is crashed. so we'll explain how to gather and analyze App crash on Firebase Crashlytics. in this blog, we will use react-native-firebase library. if you didn't set react-native-firebase, see our previous blog about how to install and set the library.

- [Firebase Admob]({{site.url}}/{{page.categories}}/react-native-firebase-admob/){:target="_blank"}

## configure iOS
let's see how to configure react-native-firebase on iOS to use Firebase Crashlytics.

### set and install required libraries
add required libraries to ```Podfile``` like below.

```ruby
...
pod 'Firebase/Core'
pod 'Firebase/AdMob'
pod 'Fabric'
pod 'Crashlytics'
...
```

use below ```pod``` command to install added libraries.

```bash
# cd ios
pod install
# pod update
```

### add Crashlytics executing script
we need to add Crashlytics executing script to use Firebase Crashlytics.

execute Xcode to select ```ios/[AppName].xcworkspace``` on RN(react native) project folder.

![execute xcode](/assets/images/category/react-native/firebase-crashlytics/execute_xcode.png)

select own your project on left file explorer and ```TARGETS```. adn select ```Build Phases``` on the top menu.

![xcode build phases](/assets/images/category/react-native/firebase-crashlytics/build_phases.png)

click ```+``` button on Build Phases tab and select ```New Run Script Phase```.

![new run script menu on build phases](/assets/images/category/react-native/firebase-crashlytics/new_run_script.png)

insert below command to ```# Type a script...``` under ```Shell``` on ```Run Script```;

```bash
"${PODS_ROOT}/Fabric/run"
```

![add Run Script](/assets/images/category/react-native/firebase-crashlytics/add_run_script.png)

### test
insert below code to where you want to test Firebase Crashlytics.

```js
firebase.crashlytics().crash();
```

this code forcely makes App crash. if App is crashed and exited, execute App again to report to Firebase Crashlytics.

execute below command or xcode to start the simulator.

```bash
react-native run-ios
```

if you use xcode to start the simulator, you should close xcode and execute App again. if xcode is executed and App is crashed, xcode treats the crash, not to report to Crashlytics.

after crashing, execute App again. after a while, you can see crash report at Firebase Console Crashlytics like below.

![Firebase Console Crashlytics](/assets/images/category/react-native/firebase-crashlytics/firebase_crashlytics.png)

wraning: remove test code (```firebase.crashlytics().crash();```) after test.

## configure Android
configure react-native-firebase on Android to use Firebase Crashlytics.

### set and install required libraries
modify ```android/app/build.gradle``` file like below.

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

modify ```android/build.gradle``` file like below.

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

modify ```android/app/src/main/java/com/[app name]/MainApplication.java``` file like below.

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

### test
add below code to where you want to test Firebase Crashlytics.

```js
firebase.crashlytics().crash();
```

when we started Android emulator and execute ```react-native run-android``` to make App crash,  red error screen was appeared so App crash was not reported. so we tested to install built file on the emulator. if you don't know how to build and test on Android, see our previous blog - [Android build and test]({{site.url}}/{{page.categories}}/android-running-on-device/){:target="_blank"}.

```bash
react-native bundle --platform android --dev false --entry-file index.js --bundle-output android/app/src/main/assets/index.android.bundle
```

build javascript by above command, and execute below command to install on the emulator.

```bash
react-native run-android --variant=release
```

and then test, we can see App crash report like below.

![Firebase Console Crashlytics android](/assets/images/category/react-native/firebase-crashlytics/firebase_crashlytics_android.png)

warning: remove test code (```firebase.crashlytics().crash();```) after test.

## reference
- [https://firebase.google.com/docs/crashlytics/get-started](https://firebase.google.com/docs/crashlytics/get-started){:rel="nofollow noreferrer" target="_blank"}
- [https://rnfirebase.io/docs/v5.x.x/crashlytics/ios](https://rnfirebase.io/docs/v5.x.x/crashlytics/ios){:rel="nofollow noreferrer" target="_blank"}