---
layout: 'post'
permalink: '/react-native/install-on-windows/'
paginate_path: '/react-native/:num/install-on-windows/'
lang: 'ko'
categories: 'react-native'
comments: true

title: '윈도우(Windows)에 react native 개발 환경 구축하기'
description: 'react-native로 앱을 개발하기 위해 윈도우(Windows)에 개발 환경을 구축해 보고, react-native로 생성한 프로젝트가 잘 동작하는지 확인해 봅니다.'
image: '/assets/images/category/react-native/2018/install-on-windows/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

1. [개요](#개요)
1. [Chocolatey 설치](#chocolatey-설치)
1. [Nodejs 설치](#nodejs-설치)
1. [Python 설치](#python-설치)
1. [React Native CLI 설치](#react-native-cli-설치)
1. [JDK 설치](#jdk-설치)
1. [안드로이드 스튜디오 설치](#안드로이드-스튜디오-설치)
    - [안드로이드 스튜디오 설정](#안드로이드-스튜디오-설정)
    - [안드로이드 스튜디오 SDK 설정](#안드로이드-스튜디오-sdk-설정)
    - [안드로이드 스튜디오 환경 변수 설정](#안드로이드-스튜디오-환경-변수-설정)
1. [react-native 프로젝트 생성 및 확인](#react-native-프로젝트-생성-및-확인)
    - [안드로이드에서 확인](#안드로이드에서-확인)
1. [완료](#완료)

</div>

## 개요

react-native로 앱을 개발하기 위해 윈도우(Windows)에서 개발 환경을 설정하는 방법에 대해서 알아봅시다. 맥(Mac)에 개발 환경을 설정하는 방법에 대해서는 아래에 블로그를 참고하시길 바랍니다.

- [맥(Mac)에 react native 개발 환경 구축하기]({{site.url}}/react-native/install-on-mac/){:target="_blank"}

윈도우즈(Windows)에서 react-native로 앱을 개발하는 방법으로 `Expo CLI`와 `React Native CLI`가 있습니다.

Expo CLI는 react-native로 앱을 개발할 때 자주 사용되는 네이티브 기능(위치 정보, 카메라 등)을 패키지로 묶어서 제공합니다. 처음 시작은 Expo로 시작하면 편할 수 있지만, 사용하지 않은 네이티브 모듈로 인해, 앱 파일 사이즈가 커지는 문제와 Expo에서 제공하지 않은 네이티브 모듈을 추가할 때, 불편함 등이 있어 이 블로그에서는 Expo 사용을 추천하지 않습니다.

이 블로그 포스트는 React Native CLI를 사용하여 앱을 개발하기 위한 개발 환경 설정에 대해서 설명합니다. 또한 설치한 React Native CLI를 사용하여 프로젝트를 생성해 보고 잘 동작하는지 확인도 해 보도록 하겠습니다.

react-native로 앱을 개발하기 위해서는 Nodejs, Python, Android studio등을 설치해야 합니다. 각 단계를 하나씩 하나씩 자세히 살펴 보도록 하겠습니다.

## Chocolatey 설치

Chocolatey는 윈도우(Windows)에서 필요한 패키지를 설치하고 관리하는 윈도우(Windows)용 패키지 관리자입니다. Chocolatey를 사용하면 윈도우(Windows)에서 간단하게 필요한 패키지를 설치할 수 있습니다.

- Chocolatey: [https://chocolatey.org/](https://chocolatey.org/){:rel="nofollow noreferrer" target="_blank"}

Chocolatey를 설치하기 위해서, 명령 프롬프트(cmd)를 관리자 권한으로 실행하고, 아래에 명령어를 실행합니다.

```bash
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
```

설치가 완료되었다면, 명령 프롬프트(cmd)를 재실행한 후, 아래에 명령어를 실행하여 설치가 잘 되었는지 확인합니다.

```bash
choco –version
```

설치가 잘 되었다면, 다음과 같이 Chocolatey의 버전을 확인할 수 있습니다.

```bash
0.10.15
```

{% include in-feed-ads.html %}

## Nodejs 설치

react-native는 Javascript이므로 Javascript의 런타임인 Nodejs가 필요합니다.

- Nodejs: [https://nodejs.org/](https://nodejs.org/){:rel="nofollow noreferrer" target="_blank"}

명령 프롬프트(cmd)를 관리자 권한으로 실행한 후, 아래의 Chocolatey 명령어를 통해 Nodejs를 설치합니다.

```bash
choco install -y nodejs.install
```

설치가 완료되면, 명령 프롬프트(cmd)를 재실행한 후, 아래의 명령어를 통해 Nodejs가 제대로 설치되었는지 확인합니다.

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

## Python 설치

리액트 네이티브의 빌드 시스템은 파이썬을 사용합니다. 맥(Mac)은 기본적으로 파이썬이 설치되어 있으므로, Python 설치 과정이 필요없지만, 윈도우(Windows)에서는 Python을 설치할 필요가 있습니다.

명령 프롬프트(cmd)를 관리자 권한으로 실행한 후 아래의 Chocolatey 명령어를 실행하여 Python을 설치합니다.

```bash
choco install -y python2
```

설치가 완료되면, Python을 사용하기 위해 컴퓨터를 재부팅해야 합니다. 컴퓨터가 재부팅되었다면, 명령 프롬프트(cmd)에서 아래에 명령어를 실행하여 Python이 잘 설치되었는지 확인합니다.

```bash
python --version
```

Python이 잘 설치되었다면, 아래와 같이 Python의 버전을 확인할 수 있습니다.

```bash
2.7.16
```

## React Native CLI 설치

이제 react-native로 앱을 개발하기 위해 필요한 React Native CLI를 설치해 봅시다. 아래의 npm 명령어를 통해 React Native CLI를 설치합니다.

```bash
npm install -g react-native-cli
```

설치가 완료되었다면, 아래에 명령어를 실행하여 React Native CLI가 잘 설치되었는지 확인합니다.

```bash
react-native --version
```

문제없이 설치되었다면, 아래와 같이 React Native CLI의 버전을 확인할 수 있습니다.

```bash
react-native-cli: 2.0.1
react-native: n/a - not inside a React Native project
```

{% include in-feed-ads.html %}

## JDK 설치

react-native로 안드로이드 앱을 개발하기 위해서는 JDK(Java Development Kit)를 설치할 필요가 있습니다. 명령 프롬프트(cmd)를 관리자 권한으로 실행한 후, 아래에 Chocolatey 명령어를 실행하여 JDK를 설치합니다.

```bash
choco install -y jdk8
```

설치가 완료되었다면, 명령 프롬프트(cmd)를 재실행한 후, 아래에 명령어를 통해 Java가 잘 설치되었는지 확인합니다.

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

다운로드가 완료되면, 설치 파일을 실행하여 안드로이드 스튜디오를 설치를 진행합니다.

### 안드로이드 스튜디오 설정

안드로이드 스튜디오를 실행하면 아래와 같은 화면을 볼 수 있습니다.

![react-native 개발 환경 설정 - 안드로이드 스튜디오 설치](/assets/images/category/react-native/2018/install-on-windows/install_android_studio.jpg)

Next 버튼을 눌러 다음 화면으로 이동합니다. 다음 화면으로 이동하면 아래와 같이 Choose Components 화면이 나옵니다. Android Virtual Device를 선택하고 Next 버튼을 눌러 다음으로 진행합니다.

![react-native 개발 환경 설정 - 안드로이드 스튜디오 컴포넌트 설정](/assets/images/category/react-native/2018/install-on-windows/android_studio_choose_components.jpg)

다음 화면으로 이동하면, 아래와 같이 안드로이드 스튜디오의 설치 위치를 설정하는 화면을 확인할 수 있습니다. 한글 이름이 포함된 폴더가 설치 위치에 지정되지 않도록 주의합니다. 설치 위치에 특별한 이상이 없다면 Next 버튼을 눌러 다음으로 진행합니다.

![react-native 개발 환경 설정 - 안드로이드 스튜디오 설치 위치 설정](/assets/images/category/react-native/2018/install-on-windows/android_studio_install_path.jpg)

다음 화면으로 이동하면, 아래와 같이 시작 메뉴를 설정하는 화면을 확인할 수 있습니다. 특별히 수정할 것 없이, Install 버튼을 눌러 설치를 진행합니다.

![react-native 개발 환경 설정 - 안드로이드 스튜디오 시작 메뉴 설정](/assets/images/category/react-native/2018/install-on-windows/android_studio_start_menu_configuration.jpg)

설치가 완료되면, 아래와 같은 화면을 볼 수 있습니다. Next 버튼을 눌러 설치를 완료합니다.

![react-native 개발 환경 설정 - 안드로이드 스튜디오 설치 완료](/assets/images/category/react-native/2018/install-on-windows/android_studio_install_completed.jpg)

Next 버튼을 눌러 설치를 완료하면, 아래와 같은 화면을 볼 수 있습니다. Start Android Studio가 체크된 상태에서 Finish 버튼을 눌러 안드로이드 스튜디오 설치를 완료합니다.

![react-native 개발 환경 설정 - 안드로이드 스튜디오 설치 및 설정 완료](/assets/images/category/react-native/2018/install-on-windows/android_studio_install_configure_completed.jpg)

Finish 버튼을 눌러 안드로이드 스튜디오 설치를 완료하면, 아래와 같이 안드로이드 스튜디오가 실행됩니다. Do not import settings를 선택하고 OK 버튼을 눌러 안드로이드 스튜디오를 실행합니다.

![react-native 개발 환경 설정 - 안드로이드 스튜디오 실행](/assets/images/category/react-native/2018/install-on-windows/android_studio_start.jpg)

OK 버튼을 눌러 안드로이드 스튜디오를 실행하면, 아래와 같이 안드로이드 스튜디오 설정 위자드 화면을 확인할 수 있습니다. Next 버튼을 눌러 다음으로 진행합니다.

![react-native 개발 환경 설정 - 안드로이드 스튜디오 설정 위자드](/assets/images/category/react-native/2018/install-on-windows/android_studio_setup_wizard.jpg)

다음 화면으로 이동하면 아래와 같이 Install Type을 설정하는 화면이 나옵니다. Custom을 선택하고 Next 버튼을 눌러 다음으로 진행합니다.

![react-native 개발 환경 설정 - 안드로이드 스튜디오 설치 타입 설정](/assets/images/category/react-native/2018/install-on-windows/configure_android_studio_install_type.jpg)

다음 화면으로 이동하면, 아래와 같이 Select UI Theme 화면을 확인할 수 있습니다. 자신이 좋아하는 테마를 선택하고 Next 버튼을 눌러 다음으로 진행합니다.

![react-native 개발 환경 설정 - 안드로이드 스튜디오 테마 설정](/assets/images/category/react-native/2018/install-on-windows/configure_android_studio_select_ui_theme.jpg)

다음 화면으로 이동하면, 아래와 같이 SDK Components Setup 화면을 확인할 수 있습니다. `Performance (Intel ® HAXM)`와 `Android Virtual Device`를 선택하고 Next 버튼을 눌러 설치를 진행합니다.

![react-native 개발 환경 설정 - 안드로이드 스튜디오 sdk 설정](/assets/images/category/react-native/2018/install-on-windows/configure_android_studio_sdk_components_setup.jpg)

다음 화면으로 이동하면 아래와 같이 Emulator Settings 화면을 확인할 수 있습니다. 특별히 수정할 것 없이 Next 버튼을 눌러 다음으로 진행합니다.

![react-native 개발 환경 설정 - 안드로이드 스튜디오 에뮬레이터 설정](/assets/images/category/react-native/2018/install-on-windows/configure_android_studio_emulator_settings.jpg)

다음 화면부터는 일반적인 소프트웨어의 설치 과정이므로 자세한 설명은 생략하도록 하겠습니다. Finish 버튼을 눌러 계속 진행하여 안드로이드 스튜디오의 설정을 완료합니다.

안드로이드 스튜디오의 설치가 완료되면 아래와 같이 안드로이드 스튜디오가 실행되는 것을 확인할 수 있습니다.

![react-native 개발 환경 설정 - 안드로이드 스튜디오 실행](/assets/images/category/react-native/2018/install-on-windows/android_studio.jpg)

{% include in-feed-ads.html %}

### 안드로이드 스튜디오 SDK 설정

오른쪽 하단의 `Configure > SDK Manger`를 선택하여 안드로이드 SDK 설정 화면으로 이동합니다.

![react-native 개발 환경 설정 - 안드로이드 스튜디오 SDK 설정](/assets/images/category/react-native/2018/install-on-windows/android_studio_configure_sdk.jpg)

위와 같은 화면이 보이면, 오른쪽 하단의 `Show Pacakge Details`를 선택합니다. 그리고 리스트에서 아래에 내용을 찾아 선택해 줍니다.

- Android SDK Platform 29
- Intel x86 Atom System Image
- Google APIs Intel x86 Atom System Image
- Google APIs Intel x86 Atom_64 System Image

전부 선택하였다면 오른쪽 하단의 OK 버튼을 눌러 선택한 내용을 설치해 줍니다.

### 안드로이드 스튜디오 환경 변수 설정

이것으로 안드로이드 스튜디오의 설치와 설정이 끝났습니다. 이제 안드로이드 스튜디오를 환경 변수에 등록해 주어야 합니다. 아래에 그림과 같이 내 PC를 우클릭하고 속성 메뉴를 선택합니다.

![react-native 개발 환경 설정 - 안드로이드 스튜디오 환경 변수 설정](/assets/images/category/react-native/2018/install-on-windows/android_studio_configure_environment_variable_menu_ko.jpg)

속성 메뉴를 선택하면, 아래와 같이 시스템 설정 화면을 볼 수 있습니다. 왼쪽에 있는 고급 시스템 설정을 선택합니다.

![react-native 개발 환경 설정 - 안드로이드 스튜디오 환경 변수 설정: 시스템 설정](/assets/images/category/react-native/2018/install-on-windows/android_studio_configure_environment_variable_system_setting_ko.jpg)

고급 시스템 설정을 누르면, 아래와 같이 시스템 속성 화면을 확인할 수 있습니다. 상단에 있는 고급탭을 선택하고, 고급탭 하단에 있는 환경 변수 버튼을 선택합니다.

![react-native 개발 환경 설정 - 안드로이드 스튜디오 환경 변수 설정: 시스템 설정 다이얼로그](/assets/images/category/react-native/2018/install-on-windows/android_studio_configure_environment_variable_system_setting_dialog_ko.jpg)

환경 변수 버튼을 선택하면 아래와 같이 환경 변수를 설정하는 화면을 확인할 수 있습니다. 상단에 있는 사용자 변수 섹션의 새로 만들기 버튼을 선택합니다.

![react-native 개발 환경 설정 - 안드로이드 스튜디오 환경 변수 설정: 새 환경 변수 추가](/assets/images/category/react-native/2018/install-on-windows/android_studio_configure_environment_variable_add_new_ko.jpg)

위와 같이 새 환경 변수 추가 화면이 나오면 변수 이름에는 `ANDROID_HOME`을 입력하고, 변수값에는 자신의 안드로이드 스튜디오의 SDK 위치를 입력합니다. 자신의 안드로이드 SDK 위치가 어디인지 모르는 경우, 아래와 같이 안드로이드 스튜디오 SDK 설정 화면으로 이동합니다. 안드로이드 스튜디오 SDK 설정 화면의 제일 상단을 보면 Android SDK Location 항목에서 자신의 안드로이드 SDK 위치를 확인할 수 있습니다.

![react-native 개발 환경 설정 - 안드로이드 스튜디오 SDK 설정](/assets/images/category/react-native/2018/install-on-windows/android_studio_configure_sdk.jpg)

ANDROID_HOME 환경 변수를 추가하였다면, 안드로이드 스튜디오의 platform-tools를 설정해 주어야 합니다. 사용자 변수 리스트에서 `Path`를 선택하여 환경 변수 편집 화면으로 이동합니다.

![react-native 개발 환경 설정 - 안드로이드 스튜디오 환경 변수 설정: platform-tools 추가](/assets/images/category/react-native/2018/install-on-windows/android_studio_configure_environment_variable_edit_path_ko.jpg)

위와 같이 편집 화면이 보인다면, 하단에 `C:\Users\[사용자 이름]\AppData\Local\Android\Sdk\platform-tools`와 같이 SDK가 설치된 폴더 하위에 있는 platform-tools 폴더를 입력하고 확인 버튼을 눌러 환경 변수를 수정해 줍니다.

이렇게 모든 수정을 완료하였다면, 명령 프롬프트(cmd)를 실행하고 아래에 명령어를 실행합니다.

```bash
adb
```

환경 변수 설정이 잘 되었다면, 아래와 같은 결과를 확인할 수 있습니다.

```bash
Android Debug Bridge version 1.0.41
Version 29.0.1-5644136
Installed as /Users/jeonghean_kim/Library/Android/sdk/platform-tools/adb
```

{% include in-feed-ads.html %}

## react-native 프로젝트 생성 및 확인

이제 아래에 React Native CLI 명령어를 통해 react-native 프로젝트를 생성합니다.

```bash
npx react-native init SampleApp
```

### 안드로이드에서 확인

안드로이드인 경우, 개발자 모드가 활성화된 디바이스를 USB로 연결한 상태 또는 안드로이드 스튜디오를 실행하고 에뮬레이터를 실행한 상태에서 아래에 명령어를 실행합니다.

```bash
cd SampleApp
# react-native run-android
npm run android
```

문제없이 잘 실행되었다면 아래와 같은 화면을 확인할 수 있습니다.

![react-native 개발 환경 설정 - 안드로이드에서 실행](/assets/images/category/react-native/2018/install-on-windows/react_native_on_android.jpg)

## 완료

이것으로 윈도우(Windows)에서 react-native로 앱을 개발하기 위한 개발 환경 설정을 알아보았습니다. 또한 개발 환경 설정을 잘 했는지 확인하기 위해, React Native CLI를 통해 앱을 생성하고 실행해 보았습니다.

이제 react-natie로 앱을 개발할 준비가 끝났습니다. react-native 앱 개발의 세계에 푹 빠져봅시다!
