---
layout: 'post'
permalink: '/react-native/install-on-mac/'
paginate_path: '/react-native/:num/install-on-mac/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'How to install React Native on Mac'
description: Let's see how to install and configure react-native development environment on Mac, and create react native project to check the environment is set well.
image: '/assets/images/category/react-native/2018/install-on-mac/background.jpg'
---

<div id="contents_list" markdown="1">

## Contents

1. [Outline](#outline)
1. [Homebrew](#homebrew)
1. [Nodejs](#nodejs)
1. [Watchman](#watchman)
1. [React Native CLI](#react-native-cli)
1. [Xcode](#xcode)
    - [Install Cocoapods](#nstall-Cocoapods)
1. [JDK](#jdk)
1. [Android Studio](#android-studio)
    - [Android Studio Configuration](#android-studio-configuration)
    - [Android Studio SDK Configuration](#android-studio-sdk-configuration)
    - [Configure Android Studio Environment Variable](#configure-android-studio-Eevironemt-variable)
1. [Create & Check react-native Project](#create--check-react-native-project)
    - [Check on iOS](#check-on-ios)
    - [Check on Android](#check-on-android)
1. [Completed](#completed)

</div>

## Outline

let's see how to install and configure react-native development environment on Mac. If you want to know how to install react-native on Windows, see the blog post below.

- [How to install React Native on Windows]({{site.url}}/react-native/install-on-windows/){:target="_blank"}

you can use `Expo CLI` and `React Native CLI` to develop react-native app on Mac.

Expo CLI is the package includes many native features(geolocation, camera, etc) when you develop the app with react-native. At the first time, when you develop the react native with Expo CLI, you can feel easy and comfortable. However, this pacakge includes many native features those you don't use, and that makes the app build size bigger. Also, if you want to integrate the native feature which Expo CLI doesn't include, it's hard to make it. Therefore, this blog post doesn't recommend to use Expo CLI.

This blog post is about how to install and configure React Native CLI environment. Also, we'll create react-native project by React Native CLI and check it works well.

We need to install Nodejs, Watchman, Xcode, etc to develop the app by react-native. let's see how to install them one by one.

## Homebrew

Homebrew is a package manager on Mac to install and manage packages. We can install packages simply on Mac via Homebrew.

- Homebrew: [https://brew.sh/](https://brew.sh/){:rel="nofollow noreferrer" target="_blank"}

First, execute the command below to check Homebrew is installed on Mac.

```bash
brew --version
```

If Homebrew is installed, you can see Homebrew version like below.

```bash
homebrew 2.1.7
homebrew/homebrew-core (git revision f487; last commit 2019-07-20)
```

If Homebrew version is not shown, you can install Homebrew via the command below.

```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

After installing, execute the command below to check Homebrew is installed well.

```bash
brew --version
```

If Homebrew is installed well, you can see Homebrew version like below.

```bash
homebrew 2.1.7
homebrew/homebrew-core (git revision f487; last commit 2019-07-20)
```

{% include in-feed-ads.html %}

## Nodejs

react-native is Javascript, so we need to install Nodejs that is Javascript runtime.

- Nodejs: [https://nodejs.org/](https://nodejs.org/){:rel="nofollow noreferrer" target="_blank"}

execute Homebrew command below to install Nodejs.

```bash
brew install node
```

After installing, execute the command below to check Nodejs is installed well.

```bash
node -–version
```

If Nodejs is installed well, you can see Nodejs version on the screen.

```bash
v12.6.0
```

When Nodejs is installed, basically, npm (Node Package Manager) is also installed. Execute the command below to check npm is installed well.

```bash
npm --version
```

If npm is installed well, you can see npm version like below.

```bash
6.9.0
```

## Watchman

Watchman is to watch specific folders or files, and if they is changed, Watchman can trigger some actions. In react-native, Watchman watches the source codes and if they are added or changed, Watchman rebuilds them.

- Watchman: [https://facebook.github.io/watchman/](https://facebook.github.io/watchman/){:rel="nofollow noreferrer" target="_blank"}

Execute Homebrew command below to install Watchman.

```bash
brew install watchman
```

After installing, execute the command below to check Watchman is installed well.

```bash
watchman –version
```

If Watchman is installed well, Watchman version would be shown up.

```bash
4.9.0
```

{% include in-feed-ads.html %}

## React Native CLI

Let's install React Native CLI to develop the app by react-native. Execute npm command below to install React Native CLI globally.

```bash
npm install -g react-native-cli
```

After installing, execute the command below to check React Native CLI is installed well.

```bash
react-native --version
```

If React Native CLI is installed well, you can see React Native CLI version like below.

```bash
react-native-cli: 2.0.1
react-native: n/a - not inside a React Native project
```

## Xcode

We need Xcode to develop iOS app by react-native. Click the link below to install Xcode via App store.

- Xcode download link: [https://apps.apple.com/us/app/xcode/id497799835?mt=12](https://apps.apple.com/us/app/xcode/id497799835?mt=12){:rel="nofollow noreferrer" target="_blank"}

After Xcode is installed, we need to configure Command Line Tools. Execute Xcode and click `Xcode > Preferences... > Locations` on the top menu. When you click it, you can see Command Line Tools setting like below.

![react-native development envirionment setting - Command Line Tools configuration](/assets/images/category/react-native/2018/install-on-mac/configure_command_line_tools.jpg)

If the setting is not like above, click the dropdown menu and select last version of Command Line Tool.

### Install Cocoapods

Cocoapods is the dependency manager on iOS development.

- Cocoapods: [https://cocoapods.org/](https://cocoapods.org/){:rel="nofollow noreferrer" target="_blank"}

Cocoapods is necessary to develop an app by react-native. Execute the command below to install Cocoapods.

```bash
sudo gem install cocoapods
```

After installing, execute the command below to check Cocoapods is installed well.

```bash
pod --version
```

If Cocoapods is installed well, you can see Cocoapods version like below.

```bash
1.7.5
```

{% include in-feed-ads.html %}

## JDK

We need to install JDK(Java Development Kit) to develop Android app with react-native. Execute the command below to install JDK.

```bash
brew tap AdoptOpenJDK/openjdk
brew cask install adoptopenjdk8
```

After installing, Execute the command below to check Java is installed well.

```bash
java -version
```

If Java is installed well via installing JDK, you can see Java version like below.

```bash
openjdk version "1.8.0_222"
OpenJDK Runtime Environment (AdoptOpenJDK)(build 1.8.0_222-b10)
OpenJDK 64-Bit Server VM (AdoptOpenJDK)(build 25.222-b10, mixed mode)
```

When JDK is installed, Java compiler is alo installed. Execute the command below to check Java compiler is also installed well.

```bash
javac -version
```

If Java compiler is installed well via installing JDK, Java compiler version is shown up like below.

```bash
javac 1.8.0_222
```

## Android Studio

We need to install Android Studio to develop Android app with react-native. Click the link below to go to Android Studio site and download the installation file.

- Android Studio: [https://developer.android.com/studio](https://developer.android.com/studio){:rel="nofollow noreferrer" target="_blank"}

After downloading, execute the installation file to execute Android Studio.

### Android Studio Configuration

you can see the screen like below after executing Android Studio.

![react-native development environment setting - Android studio configuration](/assets/images/category/react-native/2018/install-on-mac/configure_android_studio.jpg)

Click Next button to go to next screen. When you go to the next screen, you can see Install Type configuration screen. Select Custom option and click next button to go to next screen.

![react-native development environment setting - Android studio install taype configuration](/assets/images/category/react-native/2018/install-on-mac/configure_android_studio_install_type.jpg)

When you go to the next screen, you can see Select UI Theme screen like below. Select the theme which you like, and click Next button to go to the next screen.

![react-native development environment setting - Android studio theme configuration](/assets/images/category/react-native/2018/install-on-mac/configure_android_studio_select_ui_theme.jpg)

When you go to the next screen, you can see SDK Components Setup screen like below. Select `Performance (Intel ® HAXM)` option and `Android Virtual Device` option, and clic Next button.

![react-native development environment setting - Android Studio SDK Configuration](/assets/images/category/react-native/2018/install-on-mac/configure_android_studio_sdk_components_setup.jpg)

on the next screen, you can see Emulator Settings screen like below. Click Next button without any changing especially.

![react-native development environment setting - Android studio emulator configuration](/assets/images/category/react-native/2018/install-on-mac/configure_android_studio_emulator_settings.jpg)

the next process is just normal program installation, so I don't explain the detail. Just click Finish button to continue Android studio installation to complete it.

After Android studio installation, you can see Android studio is executed like below.

![react-native development environment setting - execute Android studio](/assets/images/category/react-native/2018/install-on-mac/android_studio.jpg)

{% include in-feed-ads.html %}

### Android Studio SDK Configuration

Click `Configure > SDK Manger` menu on the right botton to go to Android SDK configuration.

![react-native development environment setting - Android studio SDK configuration](/assets/images/category/react-native/2018/install-on-mac/android_studio_configure_sdk.jpg)

When the screen is shown up like below, select `Show Pacakge Details` option on the right bottom. find and select the options below on the list.

- Android SDK Platform 28
- Intel x86 Atom System Image
- Google APIs Intel x86 Atom System Image
- Google APIs Intel x86 Atom_64 System Image

If you select all options above, click OK button on the right bottom to install them.

### Configure Android Studio Environment Variable

Android studio installation and configuration are done. Now, we need to set the environment variables. open `~/.bash_profile` file or `~/.zshrc` file and add the code below to them to add the environment variables.

```bash
# export ANDROID_HOME=$HOME/Library/Android/sdk
export ANDROID_HOME=Android SDK directory location/Android/sdk
export PATH=$PATH:$ANDROID_HOME/emulator
export PATH=$PATH:$ANDROID_HOME/tools
export PATH=$PATH:$ANDROID_HOME/tools/bin
export PATH=$PATH:$ANDROID_HOME/platform-tools
```

If you use `.bash_profile`, execute the command below.

```bash
source ~/.bash_profile
```

on the code above, you should modify Android SDK directory location to your location. If you don't know where your Android SDK location, go to the Android Studio SDK configuration.

![react-native development environment setting - Android studio SDK configuration](/assets/images/category/react-native/2018/install-on-mac/android_studio_configure_sdk.jpg)

you can find your Android SDK directory location at Android SDK Location section on the top of the Android studio SDK configuration screen.

After configuration, re-start the terminal and execute the command below.

```bash
adb
```

If the environment variables are configured well, you can see the result like below.

```bash
Android Debug Bridge version 1.0.41
Version 29.0.1-5644136
Installed as /Your Android SDK Directory Location/platform-tools/adb
```

{% include in-feed-ads.html %}

## Create & Check react-native Project

Sometimes, the react-native app is not working or can't be built after updating the version. Therefore, it's recommended to execute the npm command below to lock the version when you develop the app with react-native.

```bash
npm config set save-exact=true
```

execute React Native CLI command below to create react-native project.

```bash
react-native init SampleApp
```

### Check on iOS

After creating, execute the command below to execute the react-native app on iOS.

```bash
cd SampleApp
# react-native run-ios
npm run ios
```

If you can't execute well, execute `ios/SampleApp.xcworkspace` file and select the simulator on the top of Xcode screen, and click the arrow button to execute the simulator.

If the react-native app is executed well, you can see the screen like below.

![react-native development environment setting - Check on iOS](/assets/images/category/react-native/2018/install-on-mac/react_native_on_ios.jpg)

### Check on Android

In Android, execute the command below after connecting the device that the developer mode is activated via USB or executing Android studio emulator.

```bash
cd SampleApp
# react-native run-android
npm run android
```

If you don't have any problen, you can see the screen like below.

![react-native development environment setting - check on Android](/assets/images/category/react-native/2018/install-on-mac/react_native_on_android.jpg)

## Completed

We've seen how to install and configure react-native to develop the app on Mac. Also, We've created the app by React Native CLI and executed it to check the environment is configured well.

Now, we are ready to develop the app with react-native. Let's dive to the react-native development world!
