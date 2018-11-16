---
layout: 'post'
permalink: '/react-native/ios-running-on-device/'
paginate_path: '/react-native/:num/ios-running-on-device/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'iOS build and test'
description: let's build RN(react native) for production and test it on the device.
image: '/assets/images/category/react-native/ios-running-on-device.jpg'
---


## outline
we introduced how to test RN(react native) project on the device at previous blog.([device test]({{site.url}}/{{page.categories}}/ios-test-on-device/){:target="_blank"})  Did everyone have no problem? we enough to test RN(react native) project so let's build RN(react native) project for production and test it on the device.

in here, we will introduce how to build RN(react native) project and how to test the built file on the device. this blog doesn't include how to upload to Market.

## iOS / Mac
if you don't know how to create developer account and connect the device to Mac, see previous blog.([device test]({{site.url}}/{{page.categories}}/ios-test-on-device/){:target="_blank"}) in here, we will only introduce how to build RN(react native) project for production and how to test the built file on the device.

### prepare to build
we are not English native so your English is better than us. if you don't like our poor English, just see official site([react-native](https://facebook.github.io/react-native/docs/ios-running-on-device#building-your-app-for-production){:rel="nofollow noreferrer" target="_blank"}). there are all details about how to build for production. we will introduce how to build by following that.

#### configure HTTPS protocol
Apple added the feature for security reason. if this is activated, all HTTP requests(not HTTPS requests) are rejected. but when RN(react native) is on development, RN(react native) executes dev-server on Local PC and communicates by HTTP request so RN(react native) basically disabled this feature. however, RN(react native) is built and executed on production, it doesn't communicate with dev-server so we need to delete disable code. find below code at ```/ios/projectname/info.plist``` in RN(react native) project folder and delete them.

```xml
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
    <key>NSExceptionDomains</key>
    <dict>
        <key>localhost</key>
        <dict>
            <key>NSExceptionAllowsInsecureHTTPLoads</key>
            <true/>
        </dict>
    </dict>
</dict>
```

warning: if you develop again, you should restore this code. we already said RN(react native) uses dev-server with HTTP request.

if your app need HTTP requests not HTTPS, just delete ```localhost``` parts like below code.

```xml
<key>NSAppTransportSecurity</key>
<dict>
  <key>NSAllowsArbitraryLoads</key>
      <true/>
</dict>
```

#### change build scheme
we need to change build scheme form ```Debug``` to ```Release``` for RN(react native) production. execute ```ios/projectname.xcodeproj``` file in RN(react native) project.

after xcode is executed, select ```Product``` > ```Scheme``` > ```Edit``` on the top menubar.

![change build scheme](/assets/images/category/react-native/ios-running-on-device/change-scheme.png)

select ```Run``` menu when you see below screen. change ```Build Configuration``` from ```Debug``` to ```Release``` and click ```Close``` button to close the dialog.

![change build scheme to Release from Debug](/assets/images/category/react-native/ios-running-on-device/change-debug-to-release.png)

warning: when you develop again, you should restore ```Build Configuration``` from ```Release``` to ```Debug```.

#### specifying the bundle file
finally, we need to specify the bundle file. RN(react native) uses dev-server(localhost) which serve js(javascript) file on development but on production, RN(react native) creates one bundle file and uses it like ```react``` so we need to set built bundle file. edit code at  ```ios/projectname/AppleDelegate.m``` file in RN(react natie) project folder lie below.

```
#ifdef DEBUG
    jsCodeLocation = [[RCTBundleURLProvider sharedSettings] jsBundleURLForBundleRoot:@"index" fallbackResource:nil];
#else
    jsCodeLocation = [[NSBundle mainBundle] URLForResource:@"main" withExtension:@"jsbundle"];
#endif
```

#### test on the device
completed all settings. let's check the built file on the device. connect the device to Mac and change build target from the simulator to the device and click arrow to execute.

![device test](/assets/images/category/react-native/ios-running-on-device/device-test.png)

it is not necessary that Mac and the device are same Wifi/Network enviroment like device test and doesn't need to connect the device to Mac after installation because RN(react native) uses the bundle file.however, this is not formal installation so the app will not be available after a certain period time.

## reference
- official site: [react native](https://facebook.github.io/react-native/docs/ios-running-on-device){:rel="nofollow noreferrer" target="_blank"}
