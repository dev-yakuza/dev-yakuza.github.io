---
layout: 'post'
permalink: '/react-native/test-on-device/'
paginate_path: '/react-native/:num/test-on-device/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'device test'
description: let's test RN(react native) project on devices
image: '/assets/images/category/react-native/test-on-device.jpg'
---


## outline
it is slow and annoyed to test on the simulator, isn't it? let's start to test RN(react native) on devices not the simulator.

## iOS / Mac
we absolutely need Mac to test RN(react native) project on iPhone. we need to prepare iPhone, Mac and RN(react native) project you want to test.

![prepare iphone mac](/assets/images/category/react-native/test-on-device/mac-iphone.jpg)

### create developer account
we need Apple developer account to test on devices. this is not enrolling developer program so it is free to create Apple developer account. if you have Apple developer account, it is better to skip this section.

click below link to go to the Apple developer account site.

- Apple developer account site: [https://developer.apple.com/](https://developer.apple.com/){:rel="nofollow noreferrer" :target="_blank"}

![apple developer site](/assets/images/category/react-native/test-on-device/apple-developer-site.png)

click ```account``` menu on the right top.

![apple developer site login](/assets/images/category/react-native/test-on-device/apple-developer-site-login.png)

if you have Apple account, you can login. if you don't have Apple account, click ```Create Apple ID``` for creating. this account is Apple account that you use on iPhone for downloading App, not Apple developer account.

![agreement](/assets/images/category/react-native/test-on-device/agreement.png)

after login, you can see agreement. click ```By checking this box I confirm that I have read and agree to be bound by the Agreement above.```for agreeing and ```Submit```.

![completed to create developer account](/assets/images/category/react-native/test-on-device/completed-create-account.png)

completed to create Apple developer account.

### test on deveices
your English is definitely better than us so you can see everything on official site([react native](https://facebook.github.io/react-native/docs/running-on-device){:rel="nofollow noreferrer" :target="_blank"}). we do just following it.

1. connect the device to Mac using USB.
1. got to RN(react native) project folder and execute ```ios/[project name].xcodeproj``` file.
1. after xcode is executed, click project name on left top and click ```General``` tab on right side. scroll down a little bit, you can see ```Signing``` section. click ```Add an Account...``` button beside ```Team```.

    ![signing in xcode](/assets/images/category/react-native/test-on-device/signing.png)

    insert Apple developer account ID / PW created upside and click ```Next``` button.

    ![login signing in xcode](/assets/images/category/react-native/test-on-device/signing-login.png)

    after login, click ```Download Manual Profiles``` on the bottom of the window. and close the window.
    now you can see dropdown menu beside ```Team```. select your Apple developer account.

    ![signing error in xcode](/assets/images/category/react-native/test-on-device/signing-error.png)

    if you have same error above, scroll up and change ```Bundle Identifier``` on ```Identity``` section.

    ![signing error solve in xcode](/assets/images/category/react-native/test-on-device/signing-error-solve.png)

    select ```(project name)Tests``` on ```Targets``` section. select your Apple developer account again on the dropdown menu beside ```Team``` for ```signing```.

    ![signing test target in xcode](/assets/images/category/react-native/test-on-device/signing-target-test.png)
1. change build target to the device on left top and click the arrow for starting the project.

    ![device test in xcode](/assets/images/category/react-native/test-on-device/device-test.png)

    warning: this process is for testing on the device. so test server is executed on PC like doing the simulator process. and the device accesses to the server to test RN(react native) project. so the device and PC must be on same Wifi/network for testing.

1. you can see below message when build is succeeded.

    ![security error](/assets/images/category/react-native/test-on-device/security-error.png)

    there are details what to do. just follow it.

## Android
if we test on Android, we write contents in here.

## reference
- official site: [react native](https://facebook.github.io/react-native/docs/running-on-device){:rel="nofollow noreferrer" :target="_blank"}
