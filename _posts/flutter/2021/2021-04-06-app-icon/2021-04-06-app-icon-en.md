---
layout: 'post'
permalink: '/flutter/app-icon/'
paginate_path: '/flutter/:num/app-icon/'
lang: 'en'
categories: 'flutter'
comments: true

title: '[Flutter] App icon'
description: Let's see how to change the App icons in Flutter.
image: '/assets/images/category/flutter/background.png'
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [Prepare image file](#prepare-image-file)
- [Install flutter_launcher_icons](#install-flutter_launcher_icons)
- [Configure App icon](#configure-app-icon)
- [Generate App icon](#generate-app-icon)
- [Check](#check)
- [Completed](#completed)

</div>

## Outline

I try to develop an anpp with Flutter. In this blog post, I will show you how to change the App icons in Flutter.

To change the App icons, we need to generate the images for the Android and iOS, and configure them to each OS. However, if we use the `flutter_launcher_icons` package, we can configure the App icon more simply.

- [flutter_launcher_icons](https://pub.dev/packages/flutter_launcher_icons){:rel="nofollow noreferrer" target="_blank"}

## Prepare image file

First, we need to prepare an image for the App icons. The image should meet the following conditions.

- PNG file
- more than 1024px x 1024px size
- 1024KB maximum file size

Store the prepared image to `assets/app-icon.png`.

## Install flutter_launcher_icons

To use the flutter_launcher_icons package, of course, we need to install the flutter_launcher_icons package.

Execute the command below to install the flutter_launcher_icons package.

```bash
flutter pub add flutter_launcher_icons --dev
```

## Configure App icon

Next, we need to configure the image for the App icons. Open the `pubspec.yaml` file, and add the code below to the bottom of the file.

```yaml
...
flutter_icons:
  android: "launcher_icon"
  ios: true
  image_path: "assets/app-icon.png"
```

## Generate App icon

Execute the command below to generate the App icons via the flutter_launcher_icons package.

```bash
flutter pub run flutter_launcher_icons:main
```

## Check

When you restart your Flutter project, you can see the App icon changed well like below.

![Flutter - App icon](/assets/images/category/flutter/2021/app-icon/app-icon.jpg)

## Completed

Done! we've seen how to change the App icons in Flutter. You can change them simply when you use the `flutter_launcher_icons` package!
