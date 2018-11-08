---
layout: 'post'
permalink: '/react-native/installation/'
paginate_path: '/react-native/:num/installation/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'RN installation'
description: 'install react-native and check how to make a project.'
image: '/assets/images/category/react-native/installation.jpg'
---


## installation
install react-native(RN) and check how to make a project.

when make a react-native project, you can use [create-react-native-app](https://github.com/react-community/create-react-native-app){:rel="nofollow noreferrer" :target="_blank"}, but we introduce how to make react-native project via using [react-native-cli](https://github.com/facebook/react-native#readme){:rel="nofollow noreferrer" :target="_blank"}.

you can see more detail about installation at [react-native](https://facebook.github.io/react-native/docs/getting-started){:rel="nofollow noreferrer" :target="_blank"}.

## before installing react-native
before installing react-native, you have to install (Mac)Node, Watchman / (Windows)Node, python2. you need to install xcode for developing iOS and Android Studio for developing Android.

we will introduce the installation using xcode for Mac and using Android studio for Windows.

### Mac
- install Node, Watchman using [Homebrew](https://brew.sh/){:rel="nofollow noreferrer" :target="_blank"} on Mac.

{% include_relative common/install_node_watchman_mac.md %}

- download and install xcode: [App store](https://itunes.apple.com/us/app/xcode/id497799835?mt=12){:rel="nofollow noreferrer" :target="_blank"}

### Windows
- install Node, puthon2 using [Chocolatey](https://chocolatey.org/){:rel="nofollow noreferrer" :target="_blank"} on Windows.

{% include_relative common/install_node_watchman_windows.md %}

- donwload and install Android studio: [Download](https://developer.android.com/studio/){:rel="nofollow noreferrer" :target="_blank"}
- when you install it, select "Custom" and check below list for installing.

{% include_relative common/install_custom_android.md %}

- need to install Android SDK ```Android 8.0 (Oreo)``` version.

{% include_relative common/install_android_sdk.md %}

- add ANDROID_HOME to environment variables.

{% include_relative common/android_enviroment_valiable.md %}

- create Android virtual device: see [managing-avds](https://developer.android.com/studio/run/managing-avds){:rel="nofollow noreferrer" :target="_blank"}

{% include_relative common/android_avd.md %}

## install react-native
install react-native-cli using npm.

{% include_relative common/install_react_native_cli.md %}

## create new project

{% include react-native/create_new_project.md %}

## check new project

{% include_relative common/check_project.md %}
