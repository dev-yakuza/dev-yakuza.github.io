---
layout: 'post'
permalink: '/react-native/installation/'
paginate_path: '/react-native/:num/installation/'
lang: 'ko'
categories: 'react-native'
comments: true

title: 'RN 설치'
description: 'react-native를 설치하고 프로젝트가 동작하는지 확인한다.'
image: '/assets/images/category/react-native/installation.jpg'
---


## 설치
react-native(RN)을 설치하고 프로젝트가 동작하는지 확인합니다.

[create-react-native-app](https://github.com/react-community/create-react-native-app){:rel="nofollow noreferrer" target="_blank"}을 사용해서 프로젝트를 진행할 수 있지만, [react-native-cli](https://github.com/facebook/react-native#readme){:rel="nofollow noreferrer" target="_blank"}을 통해서 진행하도록 하겠습니다.

[react-native](https://facebook.github.io/react-native/docs/getting-started){:rel="nofollow noreferrer" target="_blank"} 공식 사이트에 설치 방법들이 자세히 나와 있으니 참고하시기 바랍니다.

## react-native 설치전에
react-native 설치전에 (Mac)Node, Watchman / (Windows)Node, python2 jdk8을 설치해야 합니다. 또한  iOS개발을 위해 xcode와 Android 개발을 위해 Android studio를 설치해야 합니다.

여기서는 Mac은 xcode로 Windows는 Android studio로 진행하겠습니다.

### Mac
- Mac은 [Homebrew](https://brew.sh/){:rel="nofollow noreferrer" target="_blank"}를 통해 설치합니다.

{% include_relative common/install_node_watchman_mac.md %}

- xcode 다운로드 및 설치: [App store](https://itunes.apple.com/us/app/xcode/id497799835?mt=12){:rel="nofollow noreferrer" target="_blank"}

### Windows
- Windows는 [Chocolatey](https://chocolatey.org/){:rel="nofollow noreferrer" target="_blank"}를 통해 설치합니다.

{% include_relative common/install_node_watchman_windows.md %}

- Android studio 다운로드 및 설치: [Download](https://developer.android.com/studio/){:rel="nofollow noreferrer" target="_blank"}
- 설치시 Custom을 선택하고 아래에 항목을 체크한 후 설치해 주세요.

{% include_relative common/install_custom_android.md %}

- Android SDK ```Android 8.0 (Oreo)```버전을 설치해 주세요.

{% include_relative common/install_android_sdk.md %}

- ANDROID_HOME을 환경 변수에 추가

{% include_relative common/android_enviroment_valiable.md %}

- Android 가상 디바이스 생성: [managing-avds](https://developer.android.com/studio/run/managing-avds){:rel="nofollow noreferrer" target="_blank"} 참고

{% include_relative common/android_avd.md %}

## react-native 설치
npm을 이용하여 react-native-cli를 설치합니다.

{% include_relative common/install_react_native_cli.md %}

## 프로젝트 생성

{% include react-native/create_new_project.md %}

## 프로젝트 확인

{% include_relative common/check_project.md %}
