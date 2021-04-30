---
layout: 'post'
permalink: '/flutter/splash-screen/'
paginate_path: '/flutter/:num/splash-screen/'
lang: 'en'
categories: 'flutter'
comments: true

title: '[Flutter] Splash Screen'
description: Let's see how to change the Splash screen on Flutter.
image: '/assets/images/category/flutter/background.png'
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [Prepare imaage](#prepare-imaage)
- [Install flutter_native_splash](#install-flutter_native_splash)
- [Configure Splash image](#configure-splash-image)
- [flutter_native_splash package options](#flutter_native_splash-package-options)
- [Generate Splash images](#generate-splash-images)
- [Tip](#tip)
  - [Initial data](#initial-data)
  - [Status bar](#status-bar)
- [Completed](#completed)

</div>

## Outline

I try to develop an app with Flutter. In this blog post, I will introduce how to change the Splash screen in Flutter.

To apply a Splash screen, normally we need to create each image for Android and iOS and configure the images to each platform.

- [Adding a splash screen to your mobile app](https://flutter.dev/docs/development/ui/advanced/splash-screen){:rel="nofollow noreferrer" target="_blank"}

However, if you use the `flutter_native_splash` package, you can change it more simply.

- [flutter_native_splash](https://pub.dev/packages/flutter_native_splash){:rel="nofollow noreferrer" target="_blank"}

## Prepare imaage

There is no limitaion of the image file on the official document. However, I used the image file like the condition below.

- PNG file
- bigger than 3000px X 3000px

Store the file to `assets/splash.png`.

## Install flutter_native_splash

To use the flutter_native_splash package, we need to install the flutter_native_splash pacakge. Execute the command below to install the flutter_native_splash pageckage.

```bash
flutter pub add flutter_native_splash
```

## Configure Splash image

Next, we need to configure an image for the Splash screen. Open the `pubspec.yaml` file and add the code below to the bottom of the file.

```yaml
...
flutter_native_splash:
  color: "#FFFFFF"
  image: assets/splash.png
  fullscreen: true
```

## flutter_native_splash package options

The flutter_native_splash package has some options.

- color: Splash screen background color
- background_image: Splash screen background image
- image: Splash screen image
- color_dark: background color when the device is the dark-mode
- background_image_dark: background image when the device is the dark-mode
- image_dark: Splash screen image when the device is the dark-mode
- android_gravity: Splash image position on Android. (bottom, center, center_horizontal, center_vertical, clip_horizontal, clip_vertical, end, fill, fill_horizontal, fill_vertical, left, right, start, top)
- ios_content_mode: Splash image position on iOS. (scaleToFill, scaleAspectFit, scaleAspectFill, center, top, bottom, left, right, topLeft, topRight, bottomLeft, bottomRight)
- web_image_mode: Splash image position on Web. (center, contain, stretch, cover)
- fullscreen: show the splash screen to full screen (true, false)
- info_plist_files: if the info.plist file name is changed, set this option for it.

## Generate Splash images

If you finish to configure the flutter_native_splash options, execute the command below to generate the Splash images.

```bash
flutter pub run flutter_native_splash:create
```

{% include in-feed-ads.html %}

## Tip

If you use the flutter_native_splash package to create the Splash images, you don't need any modifiction to show the Splash screen.

You can use the Splash screen with the tips below.

### Initial data

Normally, we show the Splash screen and get the initial data. At this time, we can use `Future` and `async-await` to get the data under the Splash screen.

```dart
import 'package:flutter/material.dart';

Future<void> main() async {
  bool data = await fetchData();
  print(data);

  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Home(),
    );
  }
}

Future<bool> fetchData() async {
  bool data = false;

  // Change to API call
  await Future.delayed(Duration(seconds: 3), () {
    data = true;
  });

  return data;
}
...
```

Change the `main` funciton to `async-await`, and get the data before starting the app with `runApp`. As this structure, we can get the data when the Splash screen is shwoing.

### Status bar

In this blog post, I configured the `fullscreen: true` in the `pubspec.yaml` file to create the Splash images. I'm not sure this is the flutter_native_splash package bug, when the app is stared on iOS, the Status bar is not shown up. So I use the codeb below to display the Status bar.

```dart
...
import 'package:flutter/services.dart';
...
class Home extends StatelessWidget {
  Home() {
    SystemChrome.setEnabledSystemUIOverlays(SystemUiOverlay.values);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Home'),
      ),
      body: Center(
        child: Text('Hello world!'),
      ),
    );
  }
}
```

## Completed

Done! we've seen how to change the Splash screen on Flutter. Like this blog post, if you use the `flutter_native_splash` package, you can change the App Splash screen simply on Flutter.
