---
layout: 'post'
permalink: '/flutter/installation/'
paginate_path: '/flutter/:num/installation/'
lang: 'en'
categories: 'flutter'
comments: true

title: '[MacOS] Flutter installation'
description: Let's see how to install Flutter on MacOS.
image: '/assets/images/category/flutter/background.png'
---

<div id="contents_list" markdown="1">

## Content

- [Outline](#outline)
- [VScode](#vscode)
- [Xcode](#xcode)
- [Android Studio](#android-studio)
- [Flutter SDK installation](#flutter-sdk-installation)
- [Configure Path](#configure-path)
- [Install dependency](#install-dependency)
- [Check](#check)
- [Complete](#complete)

</div>

## Outline

Flutter is a cross-platform mobile app development platform like React Native. We can develop iOS app and Android app with single code base. Recently, Flutter supports the web and they extend the support devices more and more.

- Flutter: [Official site](https://flutter.dev/){:rel="nofollow noreferrer" target="_blank"}

In this blog post, we'll see how to install Flutter on Mac to develop the app with it. If you use other OS, please see the official document on the link below.

- Officail site: [https://flutter.dev/docs/get-started/install](https://flutter.dev/docs/get-started/install){:rel="nofollow noreferrer" target="_blank"}

## VScode

Normally, I use VSCode to deveolp the app with Flutter. If you don't use specific tools, I recommend to use VSCode. Execute the command below to install VSCode.

```bash
brew cask install visual-studio-code
sudo xattr -dr com.apple.quarantine /Applications/Visual\ Studio\ Code.app
```

And then, execute the command below to install the Flutter extension.

```bash
code --install-extension dart-code.flutter
```

## Xcode

Flutter is a cross-platform mobile app development platform, so we can develop iOS app wit it. when we develop iOS app with Flutter, we'll use iOS simulators and deploy the app via Xcode. So, we need to install Xcode to develop the app with Flutter.

- Xcode: [Web](https://developer.apple.com/xcode/){:rel="nofollow noreferrer" target="_blank"}
- Xcode: [Mac App Store](https://itunes.apple.com/us/app/xcode/id497799835){:rel="nofollow noreferrer" target="_blank"}

Install Xcode via the link above, and execute the command below to configure Xcode after installing.

```bash
sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer
sudo xcodebuild -runFirstLaunch
sudo xcodebuild -license
sudo gem install cocoapods
```

## Android Studio

Also, we can develop Android app with Flutter. But, we need Android emulators and Android Studio to deploy the app.

Download and install Android Studio via the link below.

- [Android Studio](https://developer.android.com/studio){:rel="nofollow noreferrer" target="_blank"}

{% include in-feed-ads.html %}

## Flutter SDK installation

We need to install Flutter SDK to develop the app with Flutter. First, create a folder for downloading Flutter SDK.

```bash
mkdir ~/development
cd ~/development
```

After creating the folder, execute the command below to clone the Flutter SDK.

```bash
git clone https://github.com/flutter/flutter.git -b stable
```

Or, you can download the Flutter SDK via the [web](https://flutter.dev/docs/get-started/install/macos#get-sdk){:rel="nofollow noreferrer" target="_blank"}.

```bash
curl -O https://storage.googleapis.com/flutter_infra/releases/stable/macos/flutter_macos_2.0.3-stable.zip
unzip flutter_macos_2.0.3-stable.zip
```

## Configure Path

Next, we need to configure the Flutter SDK path to use it. Execute the command below to open the configuration file for adding the path.

```bash
code ~/.zshrc
```

And then, add the below to the end of the file.

```bash
...
export PATH=$HOME/development/flutter/bin:$PATH
```

{% include in-feed-ads.html %}

## Install dependency

Now, we need to install the dependency SDK and Tools to develop the app with Flutter. Execute the command below to install the dependency for Flutter.

```bash
flutter doctor
```

If you download the Flutter SDK via `git clone`, Flutter SDK will be built, so it takes time. If you download the SDK via the web, the built is included, so the process will be faster.

After executing, you can see the result like below.

```bash
[✓] Flutter (Channel stable, 2.0.3, on macOS 11.2.3 20D91 darwin-x64, locale en)
[!] Android toolchain - develop for Android devices (Android SDK version 29.0.3)
    ! Some Android licenses not accepted.  To resolve this, run: flutter doctor --android-licenses
[✓] Xcode - develop for iOS and macOS
[✓] Chrome - develop for the web
[✓] Android Studio (version 3.6)
[✓] VS Code (version 1.54.2)
[✓] Connected device (1 available)
```

I have an error on `Android toolchain`. The error message shows the solution to configure `Android toolchain`, so execute it like below.

```bash
flutter doctor --android-licenses
```

And then, execute the `flutter doctor` again, we can see all installations succeed.

```bash
Doctor summary (to see all details, run flutter doctor -v):
[✓] Flutter (Channel stable, 2.0.3, on macOS 11.2.3 20D91 darwin-x64, locale en)
[✓] Android toolchain - develop for Android devices (Android SDK version 29.0.3)
[✓] Xcode - develop for iOS and macOS
[✓] Chrome - develop for the web
[✓] Android Studio (version 3.6)
[✓] VS Code (version 1.54.2)
[✓] Connected device (1 available)
```

So, `flutter doctor` helps us to install the required SDK or tools for Flutter.

## Check

After all installations, create a Flutter app simply and check the app is executed well. Execute the command below to create an app wit Flutter.

```bash
flutter create my_app
```

After it, open the Android emulator or iOS simulator. And then, execute the command below.

```bash
cd my_app
flutter run
```

You can open the iOS simulator with the command below.

```bash
open -a Simulator
```

You can open the Android simulator with the command below.

```bash
emulator -list-avds
emulator -avd @name-of-your-emulator
```

## Complete

Now, we're ready to develop an app with Flutter. Next, let's study Dart and develop the app with Flutter!
