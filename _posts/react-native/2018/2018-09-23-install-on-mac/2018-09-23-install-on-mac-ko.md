---
layout: 'post'
permalink: '/react-native/install-on-mac/'
paginate_path: '/react-native/:num/install-on-mac/'
lang: 'ko'
categories: 'react-native'
comments: true

title: '맥(Mac)에 react native 개발 환경 구축하기'
description: 'react-native로 앱을 개발하기 위해 맥(Mac)에 개발 환경을 구축해 보고, react-native로 생성한 프로젝트가 잘 동작하는지 확인해 봅니다.'
image: '/assets/images/category/react-native/2018/install-on-mac/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

1. [개요](#개요)
1. [Homebrew 설치](#homebrew-설치)
1. [Nodejs 설치](#nodejs-설치)
1. [Watchman 설치](#watchman-설치)
1. [React Native CLI 설치](#react-native-cli-설치)
1. [Xcode 설치](#xcode-설치)
    - [Cocoapods 설치](#cocoapods-설치)
1. [JDK 설치](#jdk-설치)
1. [안드로이드 스튜디오 설치](#안드로이드-스튜디오-설치)
    - [안드로이드 스튜디오 설정](#안드로이드-스튜디오-설정)
    - [안드로이드 스튜디오 SDK 설정](#안드로이드-스튜디오-sdk-설정)
    - [안드로이드 스튜디오 환경 변수 설정](#안드로이드-스튜디오-환경-변수-설정)
1. [react-native 프로젝트 생성 및 확인](#react-native-프로젝트-생성-및-확인)
    - [iOS에서 확인](#ios에서-확인)
    - [안드로이드에서 확인](#안드로이드에서-확인)
1. [완료](#완료)

</div>

## 개요

react-native로 앱을 개발하기 위해 맥(Mac)에서 개발 환경을 설정하는 방법에 대해서 알아봅시다. 윈도우(Windows)에 개발 환경을 설정하는 방법에 대해서는 아래에 블로그를 참고하시길 바랍니다.

- [윈도우(Windows)에 react native 개발 환경 구축하기]({{site.url}}/react-native/install-on-windows/){:target="_blank"}

맥(Mac)에서 react-native로 앱을 개발하는 방법으로 `Expo CLI`와 `React Native CLI`가 있습니다.

Expo CLI는 react-native로 앱을 개발할 때 자주 사용되는 네이티브 기능(위치 정보, 카메라 등)을 패키지로 묶어서 제공합니다. 처음 시작은 Expo로 시작하면 편할 수 있지만, 사용하지 않은 네이티브 모듈로 인해, 앱 파일 사이즈가 커지는 문제와 Expo에서 제공하지 않은 네이티브 모듈을 추가할 때, 불편함 등이 있어 이 블로그에서는 Expo 사용을 추천하지 않습니다.

이 블로그 포스트는 React Native CLI를 사용하여 앱을 개발하기 위한 개발 환경 설정에 대해서 설명합니다. 또한 설치한 React Native CLI를 사용하여 프로젝트를 생성해 보고 잘 동작하는지 확인도 해 보도록 하겠습니다.

react-native로 앱을 개발하기 위해서는 Nodejs, Watchman, Xcode등을 설치해야 합니다. 각 단계를 하나씩 하나씩 자세히 살펴 보도록 하겠습니다.

## Homebrew 설치

Homebrew는 맥(Mac)에서 필요한 패키지를 설치하고 관리하는 맥(Mac)용 패키지 관리자입니다. Homebrew를 사용하면 맥(Mac)에서 간단하게 필요한 패키지를 설치할 수 있습니다.

- Homebrew: [https://brew.sh/](https://brew.sh/){:rel="nofollow noreferrer" target="_blank"}

우선, 아래에 명령어를 통해 맥(Mac)에 Homebrew가 설치되었는지 확인합니다.

```bash
brew --version
```

만약, Homebrew가 설치되어있다면 아래와 같이 Homebrew의 버전을 확인할 수 있습니다.

```bash
homebrew 2.1.7
homebrew/homebrew-core (git revision f487; last commit 2019-07-20)
```

Homebrew의 버전이 표시되지 않는다면, 아래에 명령어를 실행하여 Homebrew를 설치합니다.

```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

설치가 완료되었다면, 아래에 명령어를 실행하여 설치가 잘 되었는지 확인합니다.

```bash
brew --version
```

설치가 잘 되었다면, 다음과 같이 Homebrew의 버전을 확인할 수 있습니다.

```bash
homebrew 2.1.7
homebrew/homebrew-core (git revision f487; last commit 2019-07-20)
```

{% include in-feed-ads.html %}

## Nodejs 설치

react-native는 Javascript이므로 Javascript의 런타임인 Nodejs가 필요합니다.

- Nodejs: [https://nodejs.org/](https://nodejs.org/){:rel="nofollow noreferrer" target="_blank"}

아래의 Homebrew 명령어를 통해 Nodejs를 설치합니다.

```bash
brew install node
```

설치가 완료되면, 아래의 명령어를 통해 Nodejs가 제대로 설치되었는지 확인합니다.

```bash
node -–version
```

Nodejs가 문제없이 설치되었다면, 아래와 같이 Nodejs의 버전을 확인할 수 있습니다.

```bash
v12.6.0
```

Nodejs를 설치하면, 기본적으로 Nodejs 패키지 매니저인 npm(Node Package Manager)도 같이 설치됩니다. npm도 잘 설치가 되었는지 확인하기 위해 아래의 명령어를 실행합니다.

```bash
npm --version
```

npm도 문제없이 잘 설치되었다면, 아래와 같이 npm의 버전을 확인할 수 있습니다.

```bash
6.9.0
```

## Watchman 설치

Watchman은 특정 폴더나 파일을 감시하다가 변화가 생기면, 특정 동작을 실행하도록 설정하는 역할을 합니다. react-native에서는 소스코드의 추가, 변경이 발생하면 다시 빌드하기 위해 Watchman을 사용하고 있습니다.

- Watchman: [https://facebook.github.io/watchman/](https://facebook.github.io/watchman/){:rel="nofollow noreferrer" target="_blank"}

Watchman을 설치하기 위해 아래의 Homebrew 명령어를 실행합니다.

```bash
brew install watchman
```

설치가 완료되었다면, 아래의 명령어를 실행하여 Watchman이 잘 설치되었는지 확인합니다.

```bash
watchman –version
```

Watchman이 문제없이 잘 설치되었다면, 아래와 같이 Watchman의 버전을 확인할 수 있습니다.

```bash
4.9.0
```

{% include in-feed-ads.html %}

## React Native CLI 설치

이제 react-native로 앱을 개발하기 위해 필요한 React Native CLI를 설치해 봅시다. 아래의 npm 명령어를 통해 React Native CLI를 설치합니다.

```bash
npm install -g react-native-cli
```

설치가 완료되었다면, 아래에 명령어를 실행하여 React Native CLI가 잘 설치되었는지 확인합니다.

```bash
npx react-native --version
```

문제없이 설치되었다면, 아래와 같이 React Native CLI의 버전을 확인할 수 있습니다.

```bash
react-native-cli: 2.0.1
react-native: n/a - not inside a React Native project
```

## Xcode 설치

react-native로 iOS 앱을 개발하기 위해서는 iOS 개발 툴인 Xcode가 필요합니다. 아래에 링크를 통해 앱 스토어에서 Xcode를 다운로드 합니다.

- Xcode 다운로드 링크: [https://apps.apple.com/us/app/xcode/id497799835?mt=12](https://apps.apple.com/us/app/xcode/id497799835?mt=12){:rel="nofollow noreferrer" target="_blank"}

Xcode 설치가 완료되면, Command Line Tools를 설정할 필요가 있습니다. Xcode를 실행하고 상단 메뉴에서 `Xcode > Preferences... > Locations`로 이동하여 아래와 같이 Command Line Tools가 잘 설정되었는지 확인합니다.

![react-native 개발 환경 설정 - Command Line Tools 설정](/assets/images/category/react-native/2018/install-on-mac/configure_command_line_tools.jpg)

만약 위와 같이 설정되어 있지 않다면, dropdown 메뉴를 선택하여 가장 최신의 Command Line Tool을 선택해 줍니다.

### Cocoapods 설치

Cocoapods는 iOS 개발에 사용되는 의존성 관리자입니다.

- Cocoapods: [https://cocoapods.org/](https://cocoapods.org/){:rel="nofollow noreferrer" target="_blank"}

react-native로 iOS 앱을 개발하려면 꼭 필요하므로 아래에 명령어를 사용하여 Cocoapods를 설치합니다.

```bash
sudo gem install cocoapods
```

설치가 완료되면, 아래에 명령어를 통해 Cocoapods가 잘 설치되었는지 확인합니다.

```bash
pod --version
```

문제없이 설치되었다면, 아래와 같이 Cocoapods의 버전을 확인할 수 있습니다.

```bash
1.7.5
```

{% include in-feed-ads.html %}

## JDK 설치

react-native로 안드로이드 앱을 개발하기 위해서는 JDK(Java Development Kit)를 설치할 필요가 있습니다. 아래에 Homebrew 명령어를 실행하여 JDK를 설치합니다.

```bash
brew tap AdoptOpenJDK/openjdk
brew cask install adoptopenjdk8
```

설치가 완료되었다면, 아래에 명령어를 통해 Java가 잘 설치되었는지 확인합니다.

```bash
java -version
```

JDK를 통해 Java가 잘 설치되었다면 아래와 같이 Java의 버전을 확인할 수 있습니다.

```bash
openjdk version "1.8.0_222"
OpenJDK Runtime Environment (AdoptOpenJDK)(build 1.8.0_222-b10)
OpenJDK 64-Bit Server VM (AdoptOpenJDK)(build 25.222-b10, mixed mode)
```

JDK를 설치하면 Java 컴파일러도 같이 설치됩니다. 아래의 명령어를 통해 Java 컴파일러도 잘 설치되었는지 확인합니다.

```bash
javac -version
```

JDK를 통해 Java 컴파일러도 잘 설치되었다면, 아래와 같이 Java 컴파일러의 버전을 확인할 수 있습니다.

```bash
javac 1.8.0_222
```

## 안드로이드 스튜디오 설치

react-native로 안드로이드 앱을 개발하려면 안드로이드 스튜디오를 설치해야 합니다. 아래에 링크를 통해 안드로이드 스튜디오 사이트로 이동하고, 설치 파일을 다운로드 합니다.

- 안드로이드 스튜디오: [https://developer.android.com/studio](https://developer.android.com/studio){:rel="nofollow noreferrer" target="_blank"}

다운로드가 완료되면, 설치 파일을 실행하여 안드로이드 스튜디오를 실행합니다.

### 안드로이드 스튜디오 설정

안드로이드 스튜디오를 실행하면 아래와 같은 화면을 볼 수 있습니다.

![react-native 개발 환경 설정 - 안드로이드 스튜디오 설정](/assets/images/category/react-native/2018/install-on-mac/configure_android_studio.jpg)

Next 버튼을 눌러 다음 화면으로 이동합니다. 다음 화면으로 이동하면 아래와 같이 Install Type을 설정하는 화면이 나옵니다. Custom을 선택하고 Next 버튼을 눌러 다음으로 진행합니다.

![react-native 개발 환경 설정 - 안드로이드 스튜디오 설치 타입 설정](/assets/images/category/react-native/2018/install-on-mac/configure_android_studio_install_type.jpg)

다음 화면으로 이동하면, 아래와 같이 Select UI Theme 화면을 확인할 수 있습니다. 자신이 좋아하는 테마를 선택하고 Next 버튼을 눌러 다음으로 진행합니다.

![react-native 개발 환경 설정 - 안드로이드 스튜디오 테마 설정](/assets/images/category/react-native/2018/install-on-mac/configure_android_studio_select_ui_theme.jpg)

다음 화면으로 이동하면, 아래와 같이 SDK Components Setup 화면을 확인할 수 있습니다. `Performance (Intel ® HAXM)`와 `Android Virtual Device`를 선택하고 Next 버튼을 눌러 설치를 진행합니다.

![react-native 개발 환경 설정 - 안드로이드 스튜디오 sdk 설정](/assets/images/category/react-native/2018/install-on-mac/configure_android_studio_sdk_components_setup.jpg)

다음 화면으로 이동하면 아래와 같이 Emulator Settings 화면을 확인할 수 있습니다. 특별히 수정할 것 없이 Next 버튼을 눌러 다음으로 진행합니다.

![react-native 개발 환경 설정 - 안드로이드 스튜디오 에뮬레이터 설정](/assets/images/category/react-native/2018/install-on-mac/configure_android_studio_emulator_settings.jpg)

다음 화면부터는 일반적인 소프트웨어의 설치 과정이므로 자세한 설명은 생략하도록 하겠습니다. Finish 버튼을 눌러 계속 진행하여 안드로이드 스튜디오의 설정을 완료합니다.

안드로이드 스튜디오의 설치가 완료되면 아래와 같이 안드로이드 스튜디오가 실행되는 것을 확인할 수 있습니다.

![react-native 개발 환경 설정 - 안드로이드 스튜디오 실행](/assets/images/category/react-native/2018/install-on-mac/android_studio.jpg)

{% include in-feed-ads.html %}

### 안드로이드 스튜디오 SDK 설정

오른쪽 하단의 `Configure > SDK Manger`를 선택하여 안드로이드 SDK 설정 화면으로 이동합니다.

![react-native 개발 환경 설정 - 안드로이드 스튜디오 SDK 설정](/assets/images/category/react-native/2018/install-on-mac/android_studio_configure_sdk.jpg)

위와 같은 화면이 보이면, 오른쪽 하단의 `Show Pacakge Details`를 선택합니다. 그리고 리스트에서 아래에 내용을 찾아 선택해 줍니다.

- Android SDK Platform 29
- Intel x86 Atom System Image
- Google APIs Intel x86 Atom System Image
- Google APIs Intel x86 Atom_64 System Image

전부 선택하였다면 오른쪽 하단의 OK 버튼을 눌러 선택한 내용을 설치해 줍니다.

### 안드로이드 스튜디오 환경 변수 설정

이것으로 안드로이드 스튜디오의 설치와 설정이 끝났습니다. 이제 안드로이드 스튜디오를 환경 변수에 등록해 주어야 합니다. 환경 변수를 추가하기 위해 `~/.bash_profile` 파일 또는 `~/.zshrc` 파일을 열고 아래와 같이 수정합니다.

```bash
# export ANDROID_HOME=$HOME/Library/Android/sdk
export ANDROID_HOME=자신의 안드로이드SDK 위치/Android/sdk
export PATH=$PATH:$ANDROID_HOME/emulator
export PATH=$PATH:$ANDROID_HOME/tools
export PATH=$PATH:$ANDROID_HOME/tools/bin
export PATH=$PATH:$ANDROID_HOME/platform-tools
```

만약 `.bash_profile`을 사용하시는 경우 아래에 명령어를 실행하시기 바랍니다.

```bash
source ~/.bash_profile
# or
source ~/.zshrc
```

위에 코드에서 자신의 안드로이드 SDK 위치를 자신의 환경에 맞춰 변경해 줍니다. 자신의 안드로이드 SDK 위치가 어디인지 모르는 경우, 안드로이드 스튜디오 SDK 설정 화면으로 이동합니다.

![react-native 개발 환경 설정 - 안드로이드 스튜디오 SDK 설정](/assets/images/category/react-native/2018/install-on-mac/android_studio_configure_sdk.jpg)

안드로이드 스튜디오 SDK 설정 화면 제일 상단을 보면 Android SDK Location 항목에서 자신의 안드로이드 SDK 위치를 확인할 수 있습니다.

이렇게 환경 변수를 설정하였다면 터미널을 다시 실행한 후 아래에 명령어를 실행해 봅니다.

```bash
adb
```

환경 변수에 안드로이드 SDK가 잘 설정되었다면, 아래와 같은 결과를 확인할 수 있습니다.

```bash
Android Debug Bridge version 1.0.41
Version 29.0.1-5644136
Installed as /자신의 안드로이드SDK 위치/platform-tools/adb
```

{% include in-feed-ads.html %}

## react-native 프로젝트 생성 및 확인

이제 아래에 React Native CLI 명령어를 통해 react-native 프로젝트를 생성합니다.

```bash
npx react-native init SampleApp
```

### iOS에서 확인

생성이 완료되면 아래에 명령어를 통해 react-native 앱을 iOS에서 구동시켜 봅니다.

```bash
cd SampleApp
# react-native run-ios
npm run ios
```

실행이 잘 되지 않는 경우, `ios/SampleApp.xcworkspace` 파일을 실행하고 왼쪽 상단의 시뮬레이터를 설정하고 화살표 버튼을 눌러 시뮬레이터를 실행합니다.

잘 실행이 되었다면, 아래와 같은 화면을 확인할 수 있습니다.

![react-native 개발 환경 설정 - iOS에서 실행](/assets/images/category/react-native/2018/install-on-mac/react_native_on_ios.jpg)

### 안드로이드에서 확인

안드로이드인 경우, 개발자 모드가 활성화된 디바이스를 USB로 연결한 상태 또는 안드로이드 스튜디오를 실행하고 에뮬레이터를 실행한 상태에서 아래에 명령어를 실행합니다.

```bash
cd SampleApp
# react-native run-android
npm run android
```

문제없이 잘 실행되었다면 아래와 같은 화면을 확인할 수 있습니다.

![react-native 개발 환경 설정 - 안드로이드에서 실행](/assets/images/category/react-native/2018/install-on-mac/react_native_on_android.jpg)

## 완료

이것으로 맥(Mac)에서 react-native로 앱을 개발하기 위한 개발 환경 설정을 알아보았습니다. 또한 개발 환경 설정을 잘 했는지 확인하기 위해, React Native CLI를 통해 앱을 생성하고 실행해 보았습니다.

이제 react-natie로 앱을 개발할 준비가 끝났습니다. react-native 앱 개발의 세계에 푹 빠져봅시다!
