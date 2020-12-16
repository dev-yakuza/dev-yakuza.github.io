---
layout: 'post'
permalink: '/react-native/install-on-windows/'
paginate_path: '/react-native/:num/install-on-windows/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'How to install React Native on Windows'
description: Let's see how to install and configure react-native development environment on Windows, and create react native project to check the environment is set well.
image: '/assets/images/category/react-native/2018/install-on-windows/background.jpg'
---

<div id="contents_list" markdown="1">

## Contents

1. [Outline](#outline)
1. [Chocolatey](#chocolatey)
1. [Nodejs](#nodejs)
1. [Python](#python)
1. [React Native CLI](#react-native-cli)
1. [JDK](#jdk)
1. [Android Studio](#android-studio)
    - [Android Studio Configuration](#android-studio-configuration)
    - [Android Studio SDK Configuration](#android-studio-sdk-configuration)
    - [Configure Android Studio Environment Variable](#configure-android-studio-environment-variable)
1. [Create & Check react-native Project](#create--check-react-native-project)
    - [Check on Android](#check-on-android)
1. [Completed](#completed)

</div>

## Outline

let's see how to install and configure react-native development environment on Windows. If you want to know how to install react-native on Mac, see the blog post below.

- [How to install React Native on Mac]({{site.url}}/react-native/install-on-mac/){:target="_blank"}

you can use `Expo CLI` and `React Native CLI` to develop react-native app on Windows.

Expo CLI is the package includes many native features(geolocation, camera, etc) when you develop the app with react-native. At the first time, when you develop the react native with Expo CLI, you can feel easy and comfortable. However, this pacakge includes many native features those you don't use, and that makes the app build size bigger. Also, if you want to integrate the native feature which Expo CLI doesn't include, it's hard to make it. Therefore, this blog post doesn't recommend to use Expo CLI.

This blog post is about how to install and configure React Native CLI environment. Also, we'll create react-native project by React Native CLI and check it works well.

We need to install Nodejs, Watchman, Xcode, etc to develop the app by react-native. let's see how to install them one by one.

## Chocolatey

Chocolatey is a package manager on Windows to install and manage packages. We can install packages simply on Windows via Chocolatey.

- Chocolatey: [https://chocolatey.org/](https://chocolatey.org/){:rel="nofollow noreferrer" target="_blank"}

For installing Chocolatey, open Command Prompt(cmd) as Administrator, and execute the command below.

```bash
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
```

After installing, reopen Command Prompt(cmd), and execute the command below to check Chocolatey is installed well.

```bash
choco –version
```

If Chocolatey is installed well, you can see Chocolatey version on the screen.

```bash
0.10.15
```

{% include in-feed-ads.html %}

## Nodejs

react-native is Javascript, so we need to install Nodejs that is Javascript runtime.

- Nodejs: [https://nodejs.org/](https://nodejs.org/){:rel="nofollow noreferrer" target="_blank"}

Open Command Prompt(cmd) as Administrator, and execute Chocolatey command below to install Nodejs.

```bash
choco install -y nodejs.install
```

After installing, reopen Command Prompt(cmd), and execute the command below to check Nodejs is installed well.

```bash
node -–version
```

If Nodejs is installed well, you can see Nodejs version like below.

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

## Python

React Native build system uses Python. Python is basically installed on Mac, so this procedure is not required, but on Windows, this is required.

Open Command Prompt(cmd) as Administrator, and execute Chocolatey command below to install Python

```bash
choco install -y python2
```

After installing, we need to reboot the computer to use Python. After rebooting, open Command Prompt(cmd), and execute the command below to check Python is installed well.

```bash
python --version
```

If Python is installed well, you can see Python version like below.

```bash
2.7.16
```

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

{% include in-feed-ads.html %}

## JDK

We need to install JDK(Java Development Kit) to develop Android app with react-native. open Command Prompt(cmd) as Administrator, and Execute Chocolatey command below to install JDK.

```bash
choco install -y jdk8
```

After installing, reopen Command Prompt(cmd), and execute the command below to check Java is installed well.

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

After downloading, execute the installation file to install Android Studio.

### Android Studio Configuration

you can see the screen like below after executing Android Studio installation file.

![react-native development environment setting - Android studio install](/assets/images/category/react-native/2018/install-on-windows/install_android_studio.jpg)

Click Next button to go to next screen. When you go to next screen, you can see Choose Components screen like below. Select Android Virtual Device and click Next button to go to next screen.

![react-native development environment setting - Android studio Choose Components](/assets/images/category/react-native/2018/install-on-windows/android_studio_choose_components.jpg)

When you go to next screen, you can see Android Studio Install Path screen like below. set Install Path or keep default, click Next button to go to next screen.

![react-native development environment setting - Android studio Install Path setting](/assets/images/category/react-native/2018/install-on-windows/android_studio_install_path.jpg)

When you go to next screen, you can see Start Menu setting screen like below. Just click Install button to install.

![react-native development environment setting - Android studio Start Menu setting](/assets/images/category/react-native/2018/install-on-windows/android_studio_start_menu_configuration.jpg)

After installing, you can see the screen like below. Click Next button to complete Android Studio installation.

![react-native development environment setting - Android studio installation complete](/assets/images/category/react-native/2018/install-on-windows/android_studio_install_completed.jpg)

When you click Next button to complete the installation, you can see the screen like below. Check Start Android Studio and click Finish button to finish Android Studio installation.

![react-native development environment setting - Android studio installation and configuration complete](/assets/images/category/react-native/2018/install-on-windows/android_studio_install_configure_completed.jpg)

When you click Finish button, you can see Android Studio is executed like below. Select Do not import settings, and click OK button to execute Android Studio.

![react-native development environment setting - Android studio excute](/assets/images/category/react-native/2018/install-on-windows/android_studio_start.jpg)

When you click OK button to execute Android Studio, you can see Android Studio Setup Wizard like below. Click Next button to go to next screen.

![react-native development environment setting - Android studio Setup Wizard](/assets/images/category/react-native/2018/install-on-windows/android_studio_setup_wizard.jpg)

When you go to next screen, you can see Install Type screen like below. Select Custom and click Next button to go to next screen.

![react-native development environment setting - Android studio Install Type setting](/assets/images/category/react-native/2018/install-on-windows/configure_android_studio_install_type.jpg)

When you go to next screen, you can see Select UI Theme screen like below. Select the theme which you like, and click Next button to go to the next screen.

![react-native development environment setting - Android studio Select UI Theme](/assets/images/category/react-native/2018/install-on-windows/configure_android_studio_select_ui_theme.jpg)

When you go to the next screen, you can see SDK Components Setup screen like below. Select `Performance (Intel ® HAXM)` option and `Android Virtual Device` option, and clic Next button.

![react-native development environment setting - Android studio sdk configuration](/assets/images/category/react-native/2018/install-on-windows/configure_android_studio_sdk_components_setup.jpg)

on the next screen, you can see Emulator Settings screen like below. Click Next button without any changing especially.

![react-native development environment setting - Android studio emulator setting](/assets/images/category/react-native/2018/install-on-windows/configure_android_studio_emulator_settings.jpg)

the next process is just normal program installation, so I don't explain the detail. Just click Finish button to continue Android studio installation to complete it.

After Android studio installation, you can see Android studio is executed like below.

![react-native development environment setting - Android studio excute](/assets/images/category/react-native/2018/install-on-windows/android_studio.jpg)

{% include in-feed-ads.html %}

### Android Studio SDK Configuration

Click `Configure > SDK Manger` menu on the right botton to go to Android SDK configuration.

![react-native development environment setting - Android studio SDK setting](/assets/images/category/react-native/2018/install-on-windows/android_studio_configure_sdk.jpg)

When the screen is shown up like below, select `Show Pacakge Details` option on the right bottom. find and select the options below on the list.

- Android SDK Platform 28
- Intel x86 Atom System Image
- Google APIs Intel x86 Atom System Image
- Google APIs Intel x86 Atom_64 System Image

If you select all options above, click OK button on the right bottom to install them.

### Configure Android Studio Environment Variable

Android studio installation and configuration are done. Now, we need to set the environment variables. Right-click This PC and click Properties menu like below.

![react-native development environment setting - Android studio environment variable](/assets/images/category/react-native/2018/install-on-windows/android_studio_configure_environment_variable_menu_en.jpg)

When you click Properties menu, you can see System and Security screen. Click Advanced System settings on the left menu list.

![react-native development environment setting - Android studio environment variable: System and Security](/assets/images/category/react-native/2018/install-on-windows/android_studio_configure_environment_variable_system_setting_en.jpg)

When you click Advanced System settings menu, you can see System properties screen like below. Click Advanced tab, and select Environment Varialbes button on the bottom of Advaced tab.

![react-native development environment setting - Android studio environment variable: System properties dailog](/assets/images/category/react-native/2018/install-on-windows/android_studio_configure_environment_variable_system_setting_dialog_en.jpg)

When you click Environment Variables button, you can see the dialog like below. Click New button on User variables for your name section.

![react-native development environment setting - Android studio environment variable: add new variable](/assets/images/category/react-native/2018/install-on-windows/android_studio_configure_environment_variable_add_new_en.jpg)

When you see the dialog like above, insert `ANDROID_HOME` to Variable name, and your Android Studio SDK path to Variable value. If you don't know your Android Studio SDK path, execute ANdroid Studio SDK confiruation screen like below. you can see Android Studio SDK location on the top of the Android Studio SDK configuration screen.

![react-native development environment setting - Android studio SDK configuration](/assets/images/category/react-native/2018/install-on-windows/android_studio_configure_sdk.jpg)

When you've added ANDROID_HOME environment variable, you need to set Android Studio platform-tools path. Click `Path` variable on User variables for your name list to go to the edit dialog.

![react-native development environment setting - Android studio environment variable: add platform-tools](/assets/images/category/react-native/2018/install-on-windows/android_studio_configure_environment_variable_edit_path_en.jpg)

When you can see the screen like above, insert platform-tools folder paht in Android SDK path like `C:\Users\[user name]\AppData\Local\Android\Sdk\platform-tools` to the bottom of the list and click OK button.

After that, open Command Prompt(cmd) and execute the command below.

```bash
adb
```

If the environment variables are configured well, you can see the result like below.

```bash
Android Debug Bridge version 1.0.41
Version 29.0.1-5644136
Installed as /Users/jeonghean_kim/Library/Android/sdk/platform-tools/adb
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

### Check on Android

In Android, execute the command below after connecting the device that the developer mode is activated via USB or executing Android studio emulator.

```bash
cd SampleApp
# react-native run-android
npm run android
```

If you don't have any problen, you can see the screen like below.

![react-native development environment setting - 안드로이드에서 실행](/assets/images/category/react-native/2018/install-on-windows/react_native_on_android.jpg)

## Completed

We've seen how to install and configure react-native to develop the app on Windows. Also, We've created the app by React Native CLI and executed it to check the environment is configured well.

Now, we are ready to develop the app with react-native. Let's dive to the react-native development world!