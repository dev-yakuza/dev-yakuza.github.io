---
layout: 'post'
permalink: '/flutter/device-unique-id/'
paginate_path: '/flutter/:num/device-unique-id/'
lang: 'en'
categories: 'flutter'
comments: true

title: '[Flutter] Device Unique ID'
description: Let's see how to get the user device unique ID by using the device_info_plus package in Flutter.
image: '/assets/images/category/flutter/background.png'
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [Install device_info_plus](#install-device_info_plus)
- [Get device unique ID](#get-device-unique-id)
- [Completed](#completed)

</div>

## Outline

When we develop apps in Flutter, sometimes, we need to get the user device unique ID to distinguish the user. In this blog post, I will introduce how to use the `device_info_plus` package to get the user device unique ID in Flutter.

- device_info_plus: [https://pub.dev/packages/device_info_plus](https://pub.dev/packages/device_info_plus){:rel="nofollow noreferrer" target="_blank"}

## Install device_info_plus

To get the user device unique ID, we need to use the `device_info_plus` package. To use the `device_info_plus` package, execute the following command to install the `device_info_plus` package.

```bash
flutter pub add device_info_plus
```

## Get device unique ID

Actuall, the `device_info_plus` package doesn't a feature to get the device unique ID. So, we need to make a function to get the device unique ID with the `device_info_plus` package.

The following code is that I use to get the device unique ID.

```dart
Future<String> getDeviceUniqueId() async {
  var deviceIdentifier = 'unknown';
  var deviceInfo = DeviceInfoPlugin();

  if (Platform.isAndroid) {
    var androidInfo = await deviceInfo.androidInfo;
    deviceIdentifier = androidInfo.androidId!;
  } else if (Platform.isIOS) {
    var iosInfo = await deviceInfo.iosInfo;
    deviceIdentifier = iosInfo.identifierForVendor!;
  } else if (Platform.isLinux) {
    var linuxInfo = await deviceInfo.linuxInfo;
    deviceIdentifier = linuxInfo.machineId!;
  } else if (kIsWeb) {
    var webInfo = await deviceInfo.webBrowserInfo;
    deviceIdentifier = webInfo.vendor! +
        webInfo.userAgent! +
        webInfo.hardwareConcurrency.toString();
  }

  return deviceIdentifier;
}
```

If you use the function above, you can get the device unique ID not only on `iOS` and `Android`, but also on `Linux` and `Web`.

## Completed

Done! we've seen how to use the `device_info_plus` package to get the user device unique ID in Flutter. Please try to use the code above to get the user device unique ID.
