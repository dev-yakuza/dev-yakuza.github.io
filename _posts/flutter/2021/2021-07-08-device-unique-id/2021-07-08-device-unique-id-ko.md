---
layout: 'post'
permalink: '/flutter/device-unique-id/'
paginate_path: '/flutter/:num/device-unique-id/'
lang: 'ko'
categories: 'flutter'
comments: true

title: '[Flutter] Device Unique ID'
description: Flutter에서 사용자 단말기의 고유 식별 ID를 얻기 위해, device_info_plus 패키지를 사용하는 방법에 대해서 알아봅시다.
image: '/assets/images/category/flutter/background.png'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [device_info_plus 설치](#device_info_plus-설치)
- [Device unique ID 가져오기](#device-unique-id-가져오기)
- [완료](#완료)

</div>

## 개요

앱을 개발하다보면, 사용자의 디바이스를 구별하기 위해, 사용자 디바이스의 고유 식별 ID(Device Unique ID)가 필요할 때가 있습니다. 이번 블로그 포스트에서는 `device_info_plus` 패키지를 사용하여 사용자의 디바이스 고유 식별 ID를 가져오는 방법에 대해서 설명합니다.

- device_info_plus: [https://pub.dev/packages/device_info_plus](https://pub.dev/packages/device_info_plus){:rel="nofollow noreferrer" target="_blank"}

## device_info_plus 설치

사용자 디바이스의 고유 식별 ID를 가져오기 위해서는 `device_info_plus` 패키지를 사용할 필요가 있습니다. `device_info_plus` 패키지를 사용하기 위해, 다음 명령어를 실행하여 `device_info_plus` 패키지를 설치합니다.

```bash
flutter pub add device_info_plus
```

## Device unique ID 가져오기

`device_info_plus` 패키지는 디바이스의 고유 식별 ID를 반환하는 기능을 가지고 있지 않습니다. 따라서, 우리는 `device_info_plus` 패키지의 기능을 사용하여 사용자의 디바이스 고유 식별 ID를 생성하는 함수를 제작할 필요가 있습니다.

다음은 사용자의 디바이스 고유 식별 ID를 얻기 위해 제가 사용하는 코드입니다.

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

위 함수를 사용하면 `iOS`와 `Android`뿐만 아니라 `Linux`와 `Web`에서도 사용할 수 있습니다.

## 완료

이것으로 Flutter에서 `device_info_plus` 패키지를 사용하여 사용자 디바이스의 고유 식별 ID(Device Unique ID)를 가져올 수 있는 방법에 대해서 알아보았습니다. 여러분도 위에 코드를 사용하여 사용자의 디바이스 고유 식별 ID를 습득하여 사용해 보시기 바랍니다.
