---
layout: 'post'
permalink: '/react-native/react-native-image-picker/'
paginate_path: '/react-native/:num/react-native-image-picker/'
lang: 'ko'
categories: 'react-native'
comments: true

title: 'react-native-image-picker'
description: 'react-native-image-picker을 사용해서 사진을 찍거나, 카메라 롤에서 사진을 가져오는 방법에 대해서 알아봅시다.'
image: '/assets/images/category/react-native/2020/react-native-image-picker/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [react-native-image-picker 설치하기](#react-native-image-picker-설치하기)
- [권한 설정](#권한-설정)
  - [iOS 권한 설정](#ios-권한-설정)
  - [안드로이드 권한 설정](#안드로이드-권한-설정)
- [사용법](#사용법)
- [옵션](#옵션)
- [Response 결과](#response-결과)
- [주의 사항](#주의-사항)
- [react-native-image-picker 예제](#react-native-image-picker-예제)
- [완료](#완료)

</div>

## 개요

아래와 같이 React Native에서 카메라를 이용하여 사진을 찍거나, 카메라 롤에 저장된 사진에 접근할 수 있습니다.

<table>
  <thead>
    <tr>
      <th style="width:50%">iOS</th>
      <th style="width:50%">Android</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <img src="/assets/images/category/react-native/2020/react-native-image-picker/ios-image.jpg" alt="react-native-image-picker on iOS"/>
      </td>
      <td>
        <img src="/assets/images/category/react-native/2020/react-native-image-picker/android-image.jpg" alt="react-native-image-picker on Android"/>
      </td>
    </tr>
  </tbody>
</table>
[사진: react-native-image-picker의 공식 사이트]

이와 같은 기능을 구현하기 위해, `react-native-image-picker` 라이브러리를 사용하는 방법에 대해서 알아보려고 합니다.

- 공식 사이트: [react-native-image-picker](https://github.com/react-native-community/react-native-image-picker){:rel="nofollow noreferrer" target="_blank"}

여기서 소개하는 내용은 Github에서 소스코드를 확인할 수 있습니다.

- Github: [react-native-image-picker-example](https://github.com/dev-yakuza/react-native-image-picker-example){:target="_blank"}

여기서 소개한 예제 소스코드는 아래에 내용들이 적용된 상태입니다.

- [typescript]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}
- [ESLint, Prettier, Husky, lint-staged]({{site.url}}/{{page.categories}}/eslint-prettier-husky-lint-staged/){:target="_blank"}
- [styled-components]({{site.url}}/{{page.categories}}/styled-components/){:target="_blank"}
- [root-import]({{site.url}}/{{page.categories}}/root-import/){:target="_blank"}

## react-native-image-picker 설치하기

아래에 명령어를 사용하여 react-native-image-picker를 설치합니다.

```bash
npm install --save react-native-image-picker
```

iOS에서 react-native-image-picker를 사용하기 위해 아래에 명령어를 실행합니다.

```bash
cd ios
pod install
cd ..
```

{% include in-feed-ads.html %}

## 권한 설정

이제 react-native-image-picker를 사용하여 사진 기능을 구현하기 위해서는 권한(Permission)이 필요합니다.

### iOS 권한 설정

iOS에서 react-native-image-picker를 사용하기 위해서는 `ios/[project name]/Info.plist`를 열고 아래와 같이 수정합니다.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  ...
  <key>NSPhotoLibraryUsageDescription</key>
  <string>$(PRODUCT_NAME) would like access to your photo gallery</string>
  <key>NSCameraUsageDescription</key>
  <string>$(PRODUCT_NAME) would like to use your camera</string>
  <key>NSPhotoLibraryAddUsageDescription</key>
  <string>$(PRODUCT_NAME) would like to save photos to your photo gallery</string>
  <key>NSMicrophoneUsageDescription</key>
  <string>$(PRODUCT_NAME) would like to use your microphone (for videos)</string>
</dict>
</plist>
```

### 안드로이드 권한 설정

안드로이드에서 react-native-image-picker를 사용하기 위해서는 `android/app/main/AndroidManifest.xml`를 열고 아래와 같이 수정합니다.

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
  package="com.reactnativeimagepickerexample">
    ...
    <uses-permission android:name="android.permission.CAMERA" />
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
    ...
</manifest>
```

{% include in-feed-ads.html %}

## 사용법

react-native-image-picker를 사용하기 위해서는 우선 아래와 같이 라이브러리를 불러옵니다.

```js
import ImagePicker from 'react-native-image-picker';
```

그리고 아래와 같이 사용할 수 있습니다.

- 사진과 카메라롤, 사용자 정의 버튼 표시

  ```js
  const options = {
    title: 'Load Photo',
    customButtons: [
      { name: 'button_id_1', title: 'CustomButton 1' },
      { name: 'button_id_2', title: 'CustomButton 2' }
    ],
    storageOptions: {
      skipBackup: true,
      path: 'images',
    },
  };
  ...
  ImagePicker.showImagePicker(options, (response) => {
    console.log('Response = ', response);

    if (response.didCancel) {
      console.log('User cancelled image picker');
    } else if (response.error) {
      console.log('ImagePicker Error: ', response.error);
    } else if (response.customButton) {
      console.log('User tapped custom button: ', response.customButton);
      Alert.alert(response.customButton);
    } else {
      // You can also display the image using data:
      // const source = { uri: 'data:image/jpeg;base64,' + response.data };
      setImageSource(response.uri);
    }
  });
  ```

- 카메라 표시

  ```js
  const options = {
    storageOptions: {
      skipBackup: true,
      path: 'images',
    },
  };
  ...
  ImagePicker.launchCamera(options, (response) => {
    if (response.error) {
      console.log('LaunchCamera Error: ', response.error);
    }
    else {
      setImageSource(response.uri);
    }
  });
  ```

- 카메라 롤 표시

  ```js
  const options = {
    storageOptions: {
      skipBackup: true,
      path: 'images',
    },
  };
  ...
  ImagePicker.launchImageLibrary(options, (response) => {
    if (response.error) {
      console.log('LaunchImageLibrary Error: ', response.error);
    }
    else {
      setImageSource(response.uri);
    }
  });
  ```

{% include in-feed-ads.html %}

## 옵션

react-native-image-picker는 아래와 같은 옵션을 사용할 수 있습니다.

| 옵션 | 필수 여부 | 타입 | iOS | 안드로이드 | 설명 |
|------|----------|------|-------------|-------|-------|
| title | X | string | ○ | ○ | ImagePicker의 상단 부분에 표시되는 타이틀 |
| cancelButtonTitle | X | string | ○ | ○ | ImagePicker의 취소 버튼의 타이틀 |
| takePhotoButtonTitle | X | string | ○ | ○ | ImagePicker의 사진 버튼의 타이틀 |
| chooseFromLibraryButtonTitle | X | string | - | ○ | ImagePicker의 카메라 롤 표시 버튼 타이틀 |
| chooseWhichLibraryTitle | X | string | ○ | ○ | 안드로이드에서 카메라 앱이 여러개 설치되어 있는 경우 표시되는 대화상자의 타이틀 |
| customButtons | X | [{name?: string; title?: string;}] | ○ | ○ | 카메라 버튼과 카메라롤 버튼 이외에 사용자 정의 버튼을 추가할 때 사용 |
| cameraType | X | 'front', 'back' | ○ | - | 전면 카메라를 사용할지, 후면 카메라를 사용할지 결정 |
| mediaType | X | 'photo', 'video', 'mixed' | ○ | ○ | 사진만 표시, 비디오만 표시, 사진과 비디오를 표시 |
| maxWidth | X | number | ○ | ○ | 최대 넓이 (Photo  only) |
| maxHeight | X | number | ○ | ○ | 최대 높이 (Photo only) |
| quality | X | number | ○ | ○ | 사진의 퀄리티 (0 to 1, photos only) |
| videoQuality | X | 'low', 'medium', 'high' | ○ | ○ | 비디오의 퀄리티 (iOS: low, medium, high / Android: low, high) |
| durationLimit | X | number | ○ | ○ | 최대 비디오 녹화 시간 (second) |
| rotation | X | number | - | ○ | 사진의 회전 각도 (Photo only, 0 to 360) |
| allowsEditing | X | boolean | ○ | - | 사진을 Resize할지 여부 |
| noData | X | boolean | ○ | ○ | 사진 선택 결과의 base64 데이터를 가져올지 여부. 큰 사진인 경우 true로 설정하면 성능을 향상 시킬 수 있다. |
| tintColor | X | number, string | ○ | - | ImagePicker의 버튼 글자 색상 |
| storageOptions.skipBackup | X | boolean | ○ | - | true로 설정하면 iCloud에 백업을 하지 않는다. |
| storageOptions.path | X | string | ○ | ○ | 이미지 저장 경로 설정 (iOS: Documents/[path]/, Android: Pictures/[path]/) |
| storageOptions.waitUntilSaved | X | boolean | ○ | - | true로 설정하면 사진/비디오가 카메라 롤에 저장될 때까지 기다린다. |
| storageOptions.privateDirectory | X | boolean | - | ○ | true로 설정하면 사진/비디오는 Android/data/your_package/files/Pictures에 저장된다. |
| permissionDenied.title | X | string | - | ○ | 권한 설정창의 제목을 설정한다. (default: Permission denied) |
| permissionDenied.text | X | string | - | ○ | 권한 설정창의 메시지 (default: To be able to take pictures with your camera and choose images from your library.) |
| permissionDenied.reTryTitle | X | string | - | ○ | 다시 시도 버튼의 타이틀 (default: re-try) |
| permissionDenied.okTitle | X | string | - | ○ | 확인 버튼의 타이틀 (default: I'm sure) |

{% include in-feed-ads.html %}

## Response 결과

| 옵션 | 필수 여부 | 타입 | iOS | 안드로이드 | 설명 |
|------|----------|------|-------------|------|------|
| customButton | ○ | string | ○ | ○ | 사용자 정의 버튼을 선택했을 때, 사용자 버튼의 name이 전달된다. |
| didCancel | ○ | boolean | ○ | ○ | ImagePicker에서 Cancel 버튼을 선택했는지 여부 |
| error | ○ | string | ○ | ○ | Error가 발생했을 때, Error 메시지 |
| data | ○ | string | ○ | ○ | 이미지의 Base64 문자열 (Photo only) |
| uri | ○ | string | ○ | ○ | 사진/비디오의 로컬 파일 URI |
| origURL | X | string | ○ | - | 카메라 롤의 사진/비디오 URL |
| isVertical | ○ | boolean | ○ | ○ | 사진/비디오의 Vertical 여부 |
| width | ○ | number | ○ | ○ | 사진의 폭 (Photo only) |
| height | ○ | number | ○ | ○ | 사진의 높이 (Photo only) |
| fileSize | ○ | number | ○ | ○ | 파일의 크기 (Photo only) |
| type | X | string | ○ | ○ | 파일 타입 (Photo only) |
| fileName | X | string | ○ | ○ | 파일의 이름 (iOS: Photo, Video / Android: Photo) |
| path | X | string | - | ○ | 파일 위치 |
| latitude | X | number | ○ | ○ | 사진/비디오의 위도 (정보가 있으면) |
| longitude | X | number | ○ | ○ | 사진/비디오의 경도 (정보가 있으면) |
| timestamp | X | string | ○ | ○ | 사진/비디오의 Metadata Timestamp (ISO8601 UTC format) |

{% include in-feed-ads.html %}

## 주의 사항

iOS 시뮬레이터, 안드로이드 에뮬레이터에서는 사진 촬영 기능을 테스트할 수 없습니다. 이 기능을 테스트하고자 하는 분들은 디바이스에서 테스트하시기를 권장합니다.

## react-native-image-picker 예제

![react-native-image-picker-example](/assets/images/category/react-native/2020/react-native-image-picker/react-native-image-picker-example.jpg)

react-native-image-picker를 사용하는 예제를 만들어 보았습니다. 아래에 링크를 통해 확인할 수 있습니다.

- Github: [react-native-image-picker-example](https://github.com/dev-yakuza/react-native-image-picker-example){:target="_blank"}

## 완료

이것으로 `react-native-image-picker`의 사용 방법을 알아보았습니다. React Native로 사진/카메라 롤 기능을 구현하려는 분들께 조금이 나마 도움이 되면 좋겠네요
