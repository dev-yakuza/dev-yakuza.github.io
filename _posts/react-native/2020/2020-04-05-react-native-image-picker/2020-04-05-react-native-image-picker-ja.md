---
layout: 'post'
permalink: '/react-native/react-native-image-picker/'
paginate_path: '/react-native/:num/react-native-image-picker/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'react-native-image-picker'
description: 'react-native-image-pickerを使って写真を取ったり、カメラロールから写真を取得する方法について説明します。'
image: '/assets/images/category/react-native/2020/react-native-image-picker/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [react-native-image-pickerのインストール](#react-native-image-pickerのインストール)
- [権限の設定](#権限の設定)
  - [iOSの権限設定](#iosの権限設定)
  - [アンドロイドの権限設定](#アンドロイドの権限設定)
- [使い方](#使い方)
- [オプション](#オプション)
- [Response結果](#response結果)
- [注意事項](#注意事項)
- [react-native-image-pickerの例題](#react-native-image-pickerの例題)
- [完了](#完了)

</div>

## 概要

下記のようにReact Nativeでカメラを使って写真を取ったり、カメラロールから保存された写真にアクセスすることができます。

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
[写真: react-native-image-pickerの公式サイト]

このような機能を実現するため、`react-native-image-picker`のライブラリを使う方法について説明します。

- 公式サイト: [react-native-image-picker](https://github.com/react-native-community/react-native-image-picker){:rel="nofollow noreferrer" target="_blank"}

ここで紹介する内容はGithubでソースコードを確認することができます。

- Github: [react-native-image-picker-example](https://github.com/dev-yakuza/react-native-image-picker-example){:target="_blank"}

ここで紹介する例題ソースコードは下記の内容が適用された状態です。

- [typescript]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}
- [ESLint, Prettier, Husky, lint-staged]({{site.url}}/{{page.categories}}/eslint-prettier-husky-lint-staged/){:target="_blank"}
- [styled-components]({{site.url}}/{{page.categories}}/styled-components/){:target="_blank"}
- [root-import]({{site.url}}/{{page.categories}}/root-import/){:target="_blank"}

## react-native-image-pickerのインストール

下記のコマンドを使ってreact-native-image-pickerをインストールします。

```bash
npm install --save react-native-image-picker
```

iOSではreact-native-image-pickerを使うため下記のコマンドを実行します。

```bash
cd ios
pod install
cd ..
```

{% include in-feed-ads.html %}

## 権限の設定

次は、react-native-image-pickerを使って写真の機能を実現するためには権限(Permission)が必要です。

### iOSの権限設定

iOSでreact-native-image-pickerを使うためには`ios/[project name]/Info.plist`を開いて下記のように修正します。

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

### アンドロイドの権限設定

アンドロイドでreact-native-image-pickerを使うためには`android/app/main/AndroidManifest.xml`を開いて下記のように修正します。

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

## 使い方

react-native-image-pickerを使うためにはまず、下記のようにライブラリをインポートします。

```js
import ImagePicker from 'react-native-image-picker';
```

そして、下記のように使うことができます。

- 写真とカメラロール、カスタムボタンを表示

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

- カメラ表示

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

- カメラロール表示

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

## オプション

react-native-image-pickerは下記のようなオプションを使うことができます。

| オプジョン | 必須 | タイプ | iOS | アンドロイド | 説明 |
|------|----------|------|-------------|
| title | X | string | ○ | ○ | ImagePickerの上に表示されるタイトル |
| cancelButtonTitle | X | string | ○ | ○ | ImagePickerのチャンセルボタンのタイトル |
| takePhotoButtonTitle | X | string | ○ | ○ | ImagePickerの写真ボタンのタイトル |
| chooseFromLibraryButtonTitle | X | string | - | ○ | ImagePickerのカメラロール表示ボタンのタイトル |
| chooseWhichLibraryTitle | X | string | ○ | ○ | アンドロイドでカメラアプリが複数インストールされた場合、表示されるダイアログのタイトル |
| customButtons | X | [{name?: string; title?: string;}] | ○ | ○ | カメラボタンとカメラロールボタン以外にカスタムボタンを追加するとき使う |
| cameraType | X | 'front', 'back' | ○ | - | 前のカメラを使うか、後ろのカメラを使うか決める |
| mediaType | X | 'photo', 'video', 'mixed' | ○ | ○ | 写真のみ表示、ビデオのみ表示、写真とビデオを表示 |
| maxWidth | X | number | ○ | ○ | 最大広さ (Photo  only) |
| maxHeight | X | number | ○ | ○ | 最大高さ (Photo only) |
| quality | X | number | ○ | ○ | 写真のクオリティ (0 to 1, photos only) |
| videoQuality | X | 'low', 'medium', 'high' | ○ | ○ | ビデオのクオリティ (iOS: low, medium, high / Android: low, high) |
| durationLimit | X | number | ○ | ○ | 最大ビデオの録画時間 (second) |
| rotation | X | number | - | ○ | 写真の回転角度 (Photo only, 0 to 360) |
| allowsEditing | X | boolean | ○ | - | 写真をResizeするかどうか |
| noData | X | boolean | ○ | ○ | 写真選択の結果でbase64のデータを取得するかどうか。大きい写真の場合、trueで設定すると性能をあげることができます。 |
| tintColor | X | number, string | ○ | - | ImagePickerのボタンのタキストの色 |
| storageOptions.skipBackup | X | boolean | ○ | - | trueを設定すると、iCloudへバックアップをしない。 |
| storageOptions.path | X | string | ○ | ○ | イメージの保存場所を設定 (iOS: Documents/[path]/, Android: Pictures/[path]/) |
| storageOptions.waitUntilSaved | X | boolean | ○ | - | trueで設定すると、写真/ビデオがカメラロールへ保存されるまで待ってる。 |
| storageOptions.privateDirectory | X | boolean | - | ○ | trueで設定すると写真/ビデオはAndroid/data/your_package/files/Picturesへ保存される。 |
| permissionDenied.title | X | string | - | ○ | 権限の設定ダイアログのタイトルを設定する。 (default: Permission denied) |
| permissionDenied.text | X | string | - | ○ | 権限の設定ダイアログのメッセージ (default: To be able to take pictures with your camera and choose images from your library.) |
| permissionDenied.reTryTitle | X | string | - | ○ | 再試しのボタンのタイトル (default: re-try) |
| permissionDenied.okTitle | X | string | - | ○ | 確認ボタンのタイトル (default: I'm sure) |

{% include in-feed-ads.html %}

## Response結果

| オプション | 必須 | タイプ | iOS | アンドロイド | 説明 |
|------|----------|------|-------------|
| customButton | ○ | string | ○ | ○ | カスタムボタンを選択した時、カスタムボタンのnameが帰ってくる |
| didCancel | ○ | boolean | ○ | ○ | ImagePickerでCancelボタンをおしたかどうか |
| error | ○ | string | ○ | ○ | Errorが発生した時のErrorメッセージ |
| data | ○ | string | ○ | ○ | イメージのBase64文字列 (Photo only) |
| uri | ○ | string | ○ | ○ | 写真/ビデオのローカルファイルURI |
| origURL | X | string | ○ | - | カメラロールの写真/ビデオのURL |
| isVertical | ○ | boolean | ○ | ○ | 写真/ビデオがVerticalかどうか |
| width | ○ | number | ○ | ○ | 写真の広さ (Photo only) |
| height | ○ | number | ○ | ○ | 写真の高さ (Photo only) |
| fileSize | ○ | number | ○ | ○ | ファイルのサイズ (Photo only) |
| type | X | string | ○ | ○ | ファイルのタイプ (Photo only) |
| fileName | X | string | ○ | ○ | ファイルの名前 (iOS: Photo, Video / Android: Photo) |
| path | X | string | - | ○ | ファイルパス |
| latitude | X | number | ○ | ○ | 写真/ビデオの緯度 (情報がある場合) |
| longitude | X | number | ○ | ○ | 写真/ビデオの軽度 (情報がある場合) |
| timestamp | X | string | ○ | ○ | 写真/ビデオのMetadata Timestamp (ISO8601 UTC format) |

{% include in-feed-ads.html %}

## 注意事項

iOSのシミュレータ、アンドロイドのエミュレータではカメラで写真を取る機能はテストできません。この機能をテストしたい方はデバイスでテストしてください。

## react-native-image-pickerの例題

![react-native-image-picker-example](/assets/images/category/react-native/2020/react-native-image-picker/react-native-image-picker-example.jpg)

react-native-image-pickerを使った例題を作ってみました。下記のリンクを使って確認してください。

- Github: [react-native-image-picker-example](https://github.com/dev-yakuza/react-native-image-picker-example){:target="_blank"}

## 完了

これで`react-native-image-picker`を使う方法について確認しました。このブログポストがReact Nativeで写真/カメラロール機能を実装する方に少しでも役に立って欲しいです。
