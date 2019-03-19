---
layout: 'post'
permalink: '/react-native/android-test-on-device/'
paginate_path: '/react-native/:num/android-test-on-device/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'Android device test'
description: let's test RN(react native) project on Android devices
image: '/assets/images/category/react-native/android-test-on-device.jpg'
---


## outline
it's very stressful to develop RN(react native) on Android emulator so let's see how to develop and test RN(react native) project on Android device. if you want to know how to develop and test RN(react native) on iOS device, see previous blog post - [iOS device test]({{site.url}}/{{page.categories}}/ios-test-on-device/){:target="_blank"}.

## prepare
Obviously, We need to prepare below things to test RN(react native) project on Android device.

- Android Studio
- Android device
- RN(react native) project

if you want to knwo how to make RN(react native) development enviroment, see another blog post - [RN installation]({{site.url}}/{{page.categories}}/installation/){:target="_blank"}.

## Android Device test
you can see all details about how to develop and test RN(react native) on Android Device in official site. we just do to follow the manual.

- official site: [https://facebook.github.io/react-native/docs/running-on-device](https://facebook.github.io/react-native/docs/running-on-device){:rel="nofollow noreferrer" target="_blank"}

## configure Android device
we need to activate Developer Options in devices we use. go to ```Settings``` > ```About phone``` and click ```Build number``` several times to activate Developer Options.

after Developer Options is activated, we need to enable ```USB debugging```. click ```Settings``` > ```Developer Options``` > ```USB debugging``` and enable USB debugging.

## connect Android device
connect Android device to PC by USB. you can see USB debugging message on your device. approve it to make testable device.

## execute on Android device
keep connecting Android device to PC and execute Android Studio. click ```Debug app``` button(arrow over bug icon) on the top of the screen. you can see an emulator and your device. select your device and click ```OK``` button. finally, you can see your RN(react native) project is executed on Android device.

warning: this process is for testing on the device. so test server is executed on PC like doing the emulator process. and the device accesses to the server to test RN(react native) project. so the device and PC must be on same Wifi/network for testing.

## Android version lower than 5.0
if test Android device version is lower than 5.0, we need to set additionals. below is about how to test RN(react native) on Android device 4.4.2 we did.

edit ```android/app/build.gradle``` like below in RN(react native) proejct folder.

```xml
defaultConfig {
    ...
    ndk {
        // abiFilters "armeabi-v7a", "x86"
    }
}
```

open Android Studio and click ```sync``` button for ```gradle sync```. after sync, execute RN(react native) project.

```bash
react-native run-android
```

RN(react native) dev-server is executed and the app also is installed but red error screen is shown up.

shake the device to show up Developer Menu. select ```Dev Settings``` > ```Debug server host & port for device``` menu in Developer Menu. you can see the screen for inputting IP address and port. insert your PC IP and 8081 port(ex> 10.0.1.1:8081). go to Developer Menu again and click ```Reload JS``` to restart project.

## compeleted
we introduced how to execute RN(react native) on Android device. now you can test your app on Android device.