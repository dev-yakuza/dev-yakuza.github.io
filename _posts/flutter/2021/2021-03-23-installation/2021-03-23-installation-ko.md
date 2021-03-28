---
layout: 'post'
permalink: '/flutter/installation/'
paginate_path: '/flutter/:num/installation/'
lang: 'ko'
categories: 'flutter'
comments: true

title: '[MacOS] Flutter 설치'
description: MacOS에 Flutter를 설치하는 방법에 대해서 알아봅시다.
image: '/assets/images/category/flutter/background.png'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [VScode](#vscode)
- [Xcode](#xcode)
- [Android Studio](#android-studio)
- [Flutter SDK 설치](#flutter-sdk-설치)
- [경로 설정](#경로-설정)
- [의존성 설치](#의존성-설치)
- [확인](#확인)
- [완료](#완료)

</div>

## 개요

Flutter는 React Native와 같이 하나에 언어로 iOS와 안드로이드 앱, 모두를 개발할 수 있는 크로스 플랫폼 모바일 앱 개발 플랫폼입니다. 최근에는 웹까지 확장되면서 점점 그 영역을 확대해 나가고 있습니다.

- Flutter: [공식 홈페이지](https://flutter.dev/){:rel="nofollow noreferrer" target="_blank"}

이번 블로그 포스트에서는 맥에서 Flutter로 앱을 개발하기 위해서, Flutter를 맥에 설치하는 방법에 대해서 알아보려고 합니다. 다른 OS에 Flutter를 설치하는 방법은 공식 홈페이지를 참고하시기 바랍니다.

- 공식 홈페이지: [https://flutter.dev/docs/get-started/install](https://flutter.dev/docs/get-started/install){:rel="nofollow noreferrer" target="_blank"}

## VScode

저는 Flutter를 개발할 때, VSCode를 사용합니다. 혹시 다른 툴을 사용하고 계시지 않는다면, VSCode를 사용하시기를 추천합니다. 다음 명령어를 사용하여 VSCode를 설치합니다.

```bash
brew cask install visual-studio-code
sudo xattr -dr com.apple.quarantine /Applications/Visual\ Studio\ Code.app
```

그리고 다음 명령어를 사용하여 Flutter 개발에 필요한 Extension을 설치합니다.

```bash
code --install-extension dart-code.flutter
```

## Xcode

Flutter는 크로스 플랫폼 모바일 앱 개발 플랫폼이므로 iOS 앱을 개발할 수 있습니다. iOS 앱을 개발할 때에는 iOS의 시뮬레이터를 사용하며, 배포할 때에는 Xcode를 사용해야 합니다. 따라서 Flutter로 앱을 개발할 때에도 Xcode는 설치해야합니다

- Xcode: [Web](https://developer.apple.com/xcode/){:rel="nofollow noreferrer" target="_blank"}
- Xcode: [Mac App Store](https://itunes.apple.com/us/app/xcode/id497799835){:rel="nofollow noreferrer" target="_blank"}

위에 링크를 통해 Xcod를 설치하였다면, 아래 명령어를 실행하여 Xcode를 설정합니다.

```bash
sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer
sudo xcodebuild -runFirstLaunch
sudo xcodebuild -license
sudo gem install cocoapods
```

## Android Studio

역시 Flutter로 안드로이드 앱을 개발할 수 있습니다. 하지만, 안드로이드 에뮬레이터를 사용하고 앱을 배포하기 위해서는 Android Studio가 필요합니다.

다음 링크를 통해 Android Studio를 다운로드 받고, 설치합니다.

- [Android Studio](https://developer.android.com/studio){:rel="nofollow noreferrer" target="_blank"}

{% include in-feed-ads.html %}

## Flutter SDK 설치

Flutter로 앱을 개발하기 위해서는 Flutter의 SDK를 설치할 필요가 있습니다. 우선 다음 명령어를 사용하여 Flutter SDK를 다운로드할 폴더를 생성합니다.

```bash
mkdir ~/development
cd ~/development
```

이렇게 Flutter SDK를 다운로드할 폴더를 생성하였다면, 아래에 명령어를 사용하여 Flutter SDK를 Clone합니다.

```bash
git clone https://github.com/flutter/flutter.git -b stable
```

또는, 다음 명령어를 사용하여 웹을 통해 배포하는 Flutter SDK를 다운로드 할 수 있습니다.

```bash
curl -O https://storage.googleapis.com/flutter_infra/releases/stable/macos/flutter_macos_2.0.3-stable.zip
unzip flutter_macos_2.0.3-stable.zip
```

## 경로 설정

Flutter SDK를 사용하기 위해서는 Flutter SDK의 경로를 설정할 필요가 있습니다. 다음 명령어를 사용하여 경로를 추가하기 위한 파일을 수정합니다.

```bash
code ~/.zshrc
```

그리고 파일의 제일 하단에 다음의 내용을 추가합니다.

```bash
...
export PATH=$HOME/development/flutter/bin:$PATH
```

{% include in-feed-ads.html %}

## 의존성 설치

이제 Flutter로 앱을 개발하기 위해 필요한 SDK 및 Tool을 설치해야 합니다. 다음 명령어를 실행하여 Flutter로 앱을 개발하기 위해 필요한 것들을 설치합니다.

```bash
flutter doctor
```

Flutter SDK를 `git clone`으로 복사한 경우 SDK를 빌드하므로 많은 시간이 소요됩니다. SDK를 웹에서 다운로드한 경우, 빌드된 내용도 포함되어 있으므로 조금 더 빠르게 진행할 수 있습니다.

실행이 완료되면 다음과 같은 결과를 확인할 수 있습니다.

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

저는 `Android toolchain`에서 실패하였네요. 실패와 함께 표시된 명령어를 실행하여 `Android toolchain`을 설정합니다.

```bash
flutter doctor --android-licenses
```

그리고 다시 `flutter doctor`를 실행하면 다음과 같이 모두 잘 설치된 것을 확인할 수 있습니다.

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

이렇게 `flutter doctor`는 Flutter 앱 개발에 필요한 SDK나 툴을 설치할 수 있게 해줍니다.

## 확인

이렇게 모든 설치가 완료되었다면, 간단하게 Flutter 앱을 생성해 보고, 앱이 잘 실행되는지 확인해 봅시다. 다음 명령어를 실행하여 Flutter로 통해 개발할 앱을 생성합니다.

```bash
flutter create my_app
```

그리고 안드로이드 애뮬레이터나 iOS 시뮬레이터를 실행시킨 다음 명령어를 통해 생성된 앱을 실행합니다.

```bash
cd my_app
flutter run
```

iOS 시뮬레이터는 다음 명령어로 실행할 수 있습니다.

```bash
open -a Simulator
```

아래 명령어로 안드로이드 애뮬레이터를 실행할 수 있습니다.

```bash
emulator -list-avds
emulator -avd @name-of-your-emulator
```

## 완료

이것으로 Flutter로 앱을 개발하기 위한 준비가 완료되었습니다. 이제 Dart를 배워보고 Flutter로 앱을 개발해 봅시다.
