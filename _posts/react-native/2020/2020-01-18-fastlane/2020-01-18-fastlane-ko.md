---
layout: 'post'
permalink: '/react-native/fastlane/'
paginate_path: '/react-native/:num/fastlane/'
lang: 'ko'
categories: 'react-native'
comments: true

title: 'Fastlane을 통한 앱 자동 배포'
description: 'Fastlane을 사용해서 React native로 만든 앱을 자동으로 배포해 보자'
image: '/assets/images/category/react-native/2020/fastlane/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

1. [개요](#개요)
1. [Fastlane](#fastlane)
1. [설치](#설치)
1. [iOS](#ios)
    - [iOS를 위한 Fastlane 초기화](#ios를-위한-fastlane-초기화)
    - [iOS용 Fastlane 폴더 및 파일](#ios용-fastlane-폴더-및-파일)
    - [iOS용 실행 파일 수정](#ios용-실행-파일-수정)
    - [iOS용 fastlane 실행](#ios용-fastlane-실행)
1. [안드로이드](#안드로이드)
    - [API access를 위한 Service Account 생성](#api-access를-위한-service-account-생성)
    - [안드로이드를 위한 Fastlane 초기화](#안드로이드를-위한-fastlane-초기화)
    - [안드로이드용 Fastlane 폴더 및 파일](#안드로이드용-fastlane-폴더-및-파일)
    - [안드로이드용 실행 파일 수정](#안드로이드용-실행-파일-수정)
    - [안드로이드용 fastlane 실행](#안드로이드용-fastlane-실행)
1. [package.json](#packagejson)
1. [gitignore](#gitignore)
1. [완료](#완료)

</div>

## 개요

React Native를 사용해서 취미로 앱을 개발을 하다보니, 앱이 점점 많아져서 앱을 배포할 때 상단한 시간이 걸리기 시작했습니다.

- 취미로 만든 앱 리스트: [App List]({{site.url}}/app/list/ko){:target="_blank"}

그래서 React Native로 만든 앱을 자동으로 배포하는 방법을 찾다가 `Fastlane`이라는 툴을 발견하게 되었습니다.

- 공식 사이트: [Fastlane](https://docs.fastlane.tools/){:rel="nofollow noreferrer" target="_blank"}

이번 블로그 포스트는 `Fastlane`을 사용해서 React Native로 개발한 앱의 배포를 자동화하는 방법에 대해서 알아봅니다. (React Native로 만든 앱뿐만 아니라 네이티브로 만든 앱에서도 사용이 가능하므로, 네이티브로 개발하시는 분들도 참고해 보시기 바랍니다.)

혹시 React Native의 배포에 관해서 잘 모르시는 분들은 이전 블로그들을 참고하시기 바랍니다.

- iOS
  - [iOS 디바이스 테스트]({{site.url}}/{{page.categories}}/ios-test-on-device/){:target="_blank"}
  - [iOS 빌드 및 테스트]({{site.url}}/{{page.categories}}/ios-running-on-device/){:target="_blank"}
  - [iOS 개발자 등록]({{site.url}}/{{page.categories}}/ios-enroll-developer-program/){:target="_blank"}
  - [iOS 인증서(Certification)]({{site.url}}/{{page.categories}}/ios-certification/){:target="_blank"}
  - [iOS TestFlight]({{site.url}}/{{page.categories}}/ios-testflight/){:target="_blank"}
  - [iOS App store 등록]({{site.url}}/{{page.categories}}/ios-app-store/){:target="_blank"}
- Android
  - [안드로이드 디바이스 테스트]({{site.url}}/{{page.categories}}/android-test-on-device/){:target="_blank"}
  - [안드로이드 빌드 및 테스트]({{site.url}}/{{page.categories}}/android-running-on-device/){:target="_blank"}
  - [안드로이드 개발자 등록]({{site.url}}/{{page.categories}}/android-enroll-google-play-developer/){:target="_blank"}
  - [안드로이드 앱 스토어 등록]({{site.url}}/{{page.categories}}/android-google-play/){:target="_blank"}

## Fastlane

> fastlane is the easiest way to automate beta deployments and releases for your iOS and Android apps. It handles all tedious tasks, like generating screenshots, dealing with code signing, and releasing your application.

Fastlane은 iOS와 안드로이드의 테스트용 배포 또는 릴리스용 배포를 간단하게 자동화해주는 툴입니다. 배포뿐만 아니라, 스크린샷 생성, 코드 사이닝, 앱 스토어 등록 정보 등을 생성, 관리할 수 있습니다.

이번 블로그에서는 스크린샷, 앱 스토어 등록 정보 등은 등록이 되어있다고 가정하고, 테스트용/릴리스용 배포를 자동화하는 부분만을 다룰 예정입니다.

스크린샷, 앱 스토어 등록 정보 생성 등, 다른 기능도 사용하고 싶은 분들은 공식 사이트를 참고하시기 바랍니다.

- 공식 사이트: [Fastlane](https://docs.fastlane.tools/){:rel="nofollow noreferrer" target="_blank"}

{% include in-feed-ads.html %}

## 설치

아래에 명령어를 사용해서 `Fastlane`을 설치할 수 있습니다.

```bash
# Using RubyGems
sudo gem install fastlane -NV

# Alternatively using Homebrew
brew cask install fastlane
```

공식 사이트에서는 `Homebrew`를 사용해서 설치하는 방법과 `RubyGems`을 사용해서 설치하는 방법을 안내하고 있습니다.

저는 처음에 Homebrew를 사용해서 설치하고, 테스트해봤지만 제대로 동작하지 않는 부분이 있었습니다. 따라서 RubyGems을 사용해서 설치하는 것을 권장합니다. 혹시 Homebrew로 제대로 동작하지 않는다면 RubyGems으로 다시 설치하신 후 시도해 보시기 바랍니다.

## iOS

React Native로 개발한 iOS 앱을 Fastlane을 사용해서 iOS의 배포를 자동화 해보도록 하겠습니다.

### iOS를 위한 Fastlane 초기화

아래에 명령어를 사용하여 iOS를 위한 Fastlane을 초기화 합니다.

```bash
cd ios
fastlane init
```

위에 명령어를 실행하면 아래와 같은 화면을 확인할 수 있습니다.

![Fastlane을 사용한 React Native 앱 자동 배포 - iOS 초기화](/assets/images/category/react-native/2020/fastlane/init-ios.jpg)

간편하게 설정을 진행하기 위해서는 Testflight용 배포를 위해 설정인 `2`번이나, 앱 스토어에 배포하기 위한 설정인 `3`을 선택할 수 있습니다.

```bash
2. Automate beta distribution to TestFlight
3. Automate App Store distribution
```

여기에서는 Testflight용 배포를 위한 설정인 `2`번을 선택하여 진행합니다.

![Fastlane을 사용한 React Native 앱 자동 배포 - iOS 프로젝트 선택](/assets/images/category/react-native/2020/fastlane/select-ios-project.jpg)

2번을 선택하고 진행하면 위와 같이 iOS의 프로젝트를 선택하는 화면을 확인할 수 있습니다. tv 앱을 제작하고 계시지 않는다면 `2`번을 선택하여 React Native의 iOS 앱 프로젝트를 선택합니다.

![Fastlane을 사용한 React Native 앱 자동 배포 - Apple 로그인](/assets/images/category/react-native/2020/fastlane/login-apple.jpg)

React Native의 iOS 프로젝트를 선택하였다면, 위와 같이 Apple 로그인을 위한 화면을 확인할 수 있습니다. iOS의 앱 배포를 위해 사용하는 Apple store connect의 로그인 아이디를 입력합니다.

![Fastlane을 사용한 React Native 앱 자동 배포 - iOS 설정 진행](/assets/images/category/react-native/2020/fastlane/enter-ios.jpg)

저는 이미 Fastlane을 사용하여 로그인한 적이 있기 때문에 위와 같은 화면을 확인할 수 있었습니다. 처음 Fastlane을 설정하시는 분들은 이중 인증을 위한 절차를 진행하셔야 됩니다.

위와 같은 화면 이외에도 여러차례 `Continue by pressing Enter`를 입력하는 화면이 나옵니다. Enter 키를 눌러 진행하여 설정을 완료합니다.

{% include in-feed-ads.html %}

### iOS용 Fastlane 폴더 및 파일

iOS의 설정을 완료하면 React Naitve의 ios 폴더 밑에 아래에 폴더 및 파일이 생성되는 것을 확인할 수 있습니다.

```bash
|- fastlane
|  |- Appfile
|  |- Fastfile
|- Gemfile
|- Gemfile.lock
```

각 폴더 및 파일을 자세히 살펴보도록 하겠습니다.

- fastlane 폴더: fastlane의 설정 및 실행 파일들이 들어 있는 폴더
- Gemfile, Gemfile.lock: fastlane은 Ruby로 되어있습니다. fastlane을 실행 시키기 위한 라이브러리 설치 파일입니다.

fastlane을 실행하기 위한 설정 내용이 들어 있는 `fastlane/Appfile` 파일을 주석을 제거하면 아래와 같습니다.

```ruby
app_identifier("io.github.dev-yakuza.kumoncho")
apple_id("dev.yakuza@gmail.com")

itc_team_id("119423059")
team_id("WFDJCJXQZ6")
```

Appfile은 iOS의 자동 배포를 위한 fastlane 설정 파일입니다. 간단한 파일이므로 자세한 설명은 생략하도록 하겠습니다.

그 다음은 실제로 앱을 배포하기 위한 실행 파일인 `fastlane/Fastfile` 파일을 주석을 제거하면 아래와 같습니다.

```ruby
default_platform(:ios)

platform :ios do
  desc "Push a new beta build to TestFlight"
  lane :beta do
    increment_build_number(xcodeproj: "kumoncho.xcodeproj")
    build_app(workspace: "kumoncho.xcworkspace", scheme: "kumoncho")
    upload_to_testflight
  end
end
```

아래에 명령어로 위의 fastlane을 실행할 수 있습니다.

```bash
# cd ios
fastlane beta
```

위와 같이 fastlane을 실행하면 iOS의 build number를 올리고(`increment_build_number`), 앱을 빌드한 다음(`build_app`), Testflight용으로 업로드 합니다.(`upload_to_testflight`)

{% include in-feed-ads.html %}

### iOS용 실행 파일 수정

기본적으로 제공하는 fastlane 파일로는 완벽하게 자동화를 할 수 없습니다. 따라서 iOS용 배포를 자동화하기 위해 `fastlane/Fastfile` 파일을 아래와 같이 수정합니다.

```ruby
default_platform(:ios)

platform :ios do
  def updateVersion(options)
    if options[:version]
      version = options[:version]
    else
      version = prompt(text: "Enter the version type or specific version\n(major, minor, patch or 1.0.0): ")
    end

    re = /\d+.\d+.\d+/
    versionNum = version[re, 0]

    if (versionNum)
      increment_version_number(
        version_number: versionNum
      )
    elsif (version == 'major' || version == 'minor' || version == 'patch')
      increment_version_number(
        bump_type: version
      )
    else
      UI.user_error!("[ERROR] Wrong version!!!!!!")
    end
  end

  desc "Push a new beta build to TestFlight"
  lane :beta do |options|
    cert
    sigh(force: true)
    updateVersion(options)

    increment_build_number(xcodeproj: "kumoncho.xcodeproj")
    build_app(workspace: "kumoncho.xcworkspace", scheme: "kumoncho")
    upload_to_testflight
  end

  desc "Push a new release build to the App Store"
  lane :release do |options|
    cert
    sigh(force: true)
    updateVersion(options)

    increment_build_number(xcodeproj: "kumoncho.xcodeproj")
    build_app(workspace: "kumoncho.xcworkspace", scheme: "kumoncho")
    upload_to_app_store(
      force: true,
      reject_if_possible: true,
      skip_metadata: false,
      skip_screenshots: true,
      languages: ['en-US', 'ja','ko'],
      release_notes: {
        "default" => "bug fixed",
        "en-US" => "bug fixed",
        "ja" => "バグ修正",
        "ko" => "버그 수정"
      },
      submit_for_review: true,
      automatic_release: true,
      submission_information: {
        add_id_info_uses_idfa: true,
        add_id_info_serves_ads: true,
        add_id_info_tracks_install: true,
        add_id_info_tracks_action: false,
        add_id_info_limits_tracking: true,
        export_compliance_encryption_updated: false,
      }
    )
  end
end
```

추가한 내용을 살펴보면 다음과 같습니다.

```ruby
def updateVersion(options)
  if options[:version]
    version = options[:version]
  else
    version = prompt(text: "Enter the version type or specific version\n(major, minor, patch or 1.0.0): ")
  end

  re = /\d+.\d+.\d+/
  versionNum = version[re, 0]

  if (versionNum)
    increment_version_number(
      version_number: versionNum
    )
  elsif (version == 'major' || version == 'minor' || version == 'patch')
    increment_version_number(
      bump_type: version
    )
  else
    UI.user_error!("[ERROR] Wrong version!!!!!!")
  end
end
```

사용자가 입력한 버전 상황에 맞게, 버전을 수정하도록 하는 함수를 정의하였습니다.

```ruby
lane :beta do |options|
  cert
  sigh(force: true)
  updateVersion(options)
  ...
```

fastlane 명령어를 실행할 때 파라메터를 전달하기 위해 `|options|`를 추가하였으며, 해당 options를 새로 정의한 함수의 파라메터로 전달하였습니다. 이렇게 새로 추가한 스크립트를 사용하기 위해서는 아래와 같은 명령어를 실행합니다.

```bash
# fastlane beta version:1.0.0
# fastlane beta version:major
# fastlane beta version:minor
fastlane beta version:patch
```

만약 파라메터를 입력하지 않으면, 사용자 입력을 기다리도록 처리하였습니다.

```ruby
def updateVersion(options)
  if options[:version]
    version = options[:version]
  else
    version = prompt(text: "Enter the version type or specific version\n(major, minor, patch or 1.0.0): ")
  end
...
```

또한 `cert`를 이용해서 인증서를 가져오도록 설정하였으며 `sigh(force: true)`를 통해 프로비저닝 프로파일을 연결하도록 하였습니다.

지금까지는 Testflight용으로 업로드 하는 방법에 대해서 다루었습니다. 실제 배포를 위해서 아래와 같은 내용을 추가하였습니다.

```ruby
desc "Push a new release build to the App Store"
lane :release do |options|
  cert
  sigh(force: true)
  updateVersion(options)

  increment_build_number(xcodeproj: "kumoncho.xcodeproj")
  build_app(workspace: "kumoncho.xcworkspace", scheme: "kumoncho")
  upload_to_app_store(
    force: true,
    reject_if_possible: true,
    skip_metadata: false,
    skip_screenshots: true,
    languages: ['en-US', 'ja','ko'],
    release_notes: {
      "default" => "bug fixed",
      "en-US" => "bug fixed",
      "ja" => "バグ修正",
      "ko" => "버그 수정"
    },
    submit_for_review: true,
    automatic_release: true,
    submission_information: {
      add_id_info_uses_idfa: true,
      add_id_info_serves_ads: true,
      add_id_info_tracks_install: true,
      add_id_info_tracks_action: false,
      add_id_info_limits_tracking: true,
      export_compliance_encryption_updated: false,
    }
  )
end
```

앱을 빌드하는 것까지는 Testflight용과 동일합니다. 빌드된 앱을 앱 스토어에 배포하기 위해 아래와 같은 내용을 추가하였습니다.

```ruby
upload_to_app_store(
  force: true,
  reject_if_possible: true,
  skip_metadata: false,
  skip_screenshots: true,
  languages: ['en-US', 'ja','ko'],
  release_notes: {
    "default" => "bug fixed",
    "en-US" => "bug fixed",
    "ja" => "バグ修正",
    "ko" => "버그 수정"
  },
  submit_for_review: true,
  automatic_release: true,
  submission_information: {
    add_id_info_uses_idfa: true,
    add_id_info_serves_ads: true,
    add_id_info_tracks_install: true,
    add_id_info_tracks_action: false,
    add_id_info_limits_tracking: true,
    export_compliance_encryption_updated: false,
  }
)
```

- force: fastlane가 생성하는 HTML report를 생성하지 않도록 합니다.(true)
- reject_if_possible: 심사 대기중인 버전이 있다면 취소합니다(true)
- skip_metadata: 앱 스토어의 정보를 등록할지 결정합니다. 자동 배포를 할 때, 버전의 수정 내용을 작성해야 하므로 이 정보를 등록하도록 설정해야합니다.(false)
- skip_screenshots: 저는 이미 배포한 앱에 대해서 자동 배포를 적용하고 있습니다. 따라서 스크린 샷을 다시 업로드할 필요가 없습니다(true)
- languages: 현재 스토어에 등록된 앱의 지역화를 설정합니다. 사용 가능한 언어는 `ar-SA, ca, cs, da, de-DE, el, en-AU, en-CA, en-GB, en-US, es-ES, es-MX, fi, fr-CA, fr-FR, he, hi, hr, hu, id, it, ja, ko, ms, nl-NL, no, pl, pt-BR, pt-PT, ro, ru, sk, sv, th, tr, uk, vi, zh-Hans, zh-Hant` 이며 자세한 내용은 공식 홈페이지를 참고하시기 바랍니다([공식 홈페이지](https://docs.fastlane.tools/actions/upload_to_app_store/#available-language-codes){:rel="nofollow noreferrer" target="_blank"})
- release_notes: iOS는 앱을 재배포할 때, Release notes를 꼭 작성해야합니다. 제가 사용하는 스크립트는 3개국어를 지원하는 앱이므로 default와 3개 국어에 해당하는 Release notes를 작성하였습니다.
- submit_for_review: 앱 심사에 제출하도록 합니다.(true)
- automatic_release: 심사후 앱을 자동으로 배포하도록 설정합니다. 이 값이 설정되지 않으면, 앱 심사를 통과한 후 개발자가 수동으로 배포해야 합니다.(true)
- submission_information: 배포전에 암호화, 광고 포함 여부등을 물어보는 옵션을 설정합니다.

이 밖에도 많은 옵션들이 있습니다. 자세한 내용은 공식 홈페이지를 참고하시기 바랍니다.

- 공식 홈페이지: [https://docs.fastlane.tools/actions/upload_to_app_store/](https://docs.fastlane.tools/actions/upload_to_app_store/){:rel="nofollow noreferrer" target="_blank"}
- 예제: [submission_information](https://github.com/artsy/eigen/blob/faa02e2746194d8d7c11899474de9c517435eca4/fastlane/Fastfile#L131-L149){:rel="nofollow noreferrer" target="_blank"}

{% include in-feed-ads.html %}

### iOS용 fastlane 실행

이제 fastlane을 사용하여 iOS에 자동으로 배포할 준비가 끝났습니다. 이제 fastlane을 사용하여 앱을 자동 배포해 봅시다.

아래에 명령어를 사용하여 React Native로 제작한 앱을 Testflight에 배포해 봅니다.

```bash
# cd ios
fastlane beta version:patch
```

배포가 완료될 때까지, 상단한 시간이 걸립니다. 배포가 완료되면 아래와 같은 화면을 확인할 수 있습니다.

![Fastlane을 사용한 React Native 앱 자동 배포 - iOS Testflight 배포](/assets/images/category/react-native/2020/fastlane/ios-testflight.jpg)

물론 App store connect의 Testflight에도 잘 배포된 것을 확인할 수 있습니다.

그럼 이제 아래에 명령어를 실행하여 실제로 배포를 진행해 봅니다.

```bash
# cd ios
fastlane release version:patch
```

배포가 완료되면 아래와 같은 화면을 확인할 수 있습니다.

![Fastlane을 사용한 React Native 앱 자동 배포 - iOS 앱 배포](/assets/images/category/react-native/2020/fastlane/ios-upload-app-store.jpg)

또한 App store connect에도 잘 배포된 것을 확인할 수 있습니다.

{% include in-feed-ads.html %}

## 안드로이드

이제 React Native로 개발한 안드로이드 앱을 Fastlane을 사용해서 안드로이드의 배포를 자동화 해보도록 하겠습니다.

### API access를 위한 Service Account 생성

Fastlane을 통해 안드로이드를 배포할 때, 구글 API를 사용하기 때문에 `Google Developer Service Account`를 생성할 필요가 있습니다.

Google Developer Service Account를 생성하기 위해, 아래의 링크를 통해 구글 플레이 콘솔(Google Play Console)로 이동합니다.

- 구글 플레이 콘솔: [https://play.google.com/apps/publish/](https://play.google.com/apps/publish/){:rel="nofollow noreferrer" target="_blank"}

구글 플레이 콘솔로 이동하면 아래와 같은 화면을 확인할 수 있습니다.

![Fastlane을 사용한 React Native 앱 자동 배포 - 구글 플레이 콘솔](/assets/images/category/react-native/2020/fastlane/google-play-console.jpg)

왼쪽 메뉴의 `Settings`를 선택합니다. 그리고 `Developer account` 하위에 있는 `API access` 메뉴를 선택합니다.

![Fastlane을 사용한 React Native 앱 자동 배포 - 구글 플레이 콘솔 api access 메뉴](/assets/images/category/react-native/2020/fastlane/android-api-access.jpg)

위와 같은 화면이 보인다면, `CREATE NEW PROJECT` 버튼을 눌러, 새로운 프로젝트를 생성합니다.

![Fastlane을 사용한 React Native 앱 자동 배포 - 구글 플레이 콘솔 api access, service account](/assets/images/category/react-native/2020/fastlane/android-api-access-service-account.jpg)

새로운 프로젝트가 생성되면, 위와 같은 화면을 볼 수 있습니다. 하단에 있는 `CREATE SERVICE ACCOUNT` 버튼을 선택하면, 아래와 같은 화면을 확인할 수 있습니다.

![Fastlane을 사용한 React Native 앱 자동 배포 - 구글 플레이 콘솔 api access, how to create service account](/assets/images/category/react-native/2020/fastlane/android-api-access-how-to-create-service-account.jpg)

위와 같은 화면에서 `Google API Console` 링크를 선택합니다. 선택하고 나면, 아래와 같은 화면을 볼 수 있습니다.

![Fastlane을 사용한 React Native 앱 자동 배포 - Google API Console](/assets/images/category/react-native/2020/fastlane/android-google-api-console.jpg)

상단에 있는 `CREATE SERVICE ACCOUNT` 버튼을 선택합니다. 선택하고 나면 아래와 같이 새로운 Service account를 생성하는 화면을 확인할 수 있습니다.

![Fastlane을 사용한 React Native 앱 자동 배포 - Google API Console, service account 생성](/assets/images/category/react-native/2020/fastlane/android-google-api-console-create-service-account.jpg)

위와 같은 화면에서, `Service account name`에 이름을 입력하고, `CREATE` 버튼을 눌러 Service account를 생성합니다.(저는 Service account name에 google-play-fastlane-deployment을 입력하였습니다.)

![Fastlane을 사용한 React Native 앱 자동 배포 - Google API Console, service account 역할 설정](/assets/images/category/react-native/2020/fastlane/android-google-api-console-service-account-role.jpg)

위와 같은 화면이 보이면, `Role`을 선택하고 `Service Account User`를 검색하여 선택합니다. Role에 Service Account User를 설정하였다면, 하단에 있는 `CONTINUE` 버튼을 눌러 다음으로 진행합니다.

![Fastlane을 사용한 React Native 앱 자동 배포 - Google API Console, service account 키 생성](/assets/images/category/react-native/2020/fastlane/android-google-api-console-service-account-create-key.jpg)

위와 같은 화면이 보이면, 하단에 있는 `CREATE KEY`를 선택하고 `JSON`이 선택된 상태에서 `CREATE` 버튼을 눌러 키를 생성합니다.

![Fastlane을 사용한 React Native 앱 자동 배포 - Google API Console, service account JSON 키 생성](/assets/images/category/react-native/2020/fastlane/android-google-api-console-service-account-create-json-key.jpg)

CREATE 버튼을 눌러 키를 생성하면 JSON 형식에 파일이 자동으로 다운로드 됩니다. 이 파일을 React native 프로젝트의 `android` 폴더 하위에 복사합니다. 마지막으로 `DONE` 버튼을 눌러 Service Account를 생성합니다.

그리고 원래 화면으로 돌아와서 오른쪽 하단에 있는 `DONE` 버튼을 눌러 Service Account 생성을 종료합니다.

![Fastlane을 사용한 React Native 앱 자동 배포 - 구글 플레이 콘솔 api access, how to create service account](/assets/images/category/react-native/2020/fastlane/android-api-access-how-to-create-service-account.jpg)

그러면 이전과는 다르게 아래와 같은 화면을 확인할 수 있습니다.

![Fastlane을 사용한 React Native 앱 자동 배포 - 구글 플레이 콘솔 Service Account 생성 완료](/assets/images/category/react-native/2020/fastlane/android-finish-to-create-service-account.jpg)

이제 권한을 부여하기 위해 오른쪽 하단의 `GRANT ACCESS` 버튼을 선택합니다.

![Fastlane을 사용한 React Native 앱 자동 배포 - 구글 플레이 콘솔 Service Account 권한 설정](/assets/images/category/react-native/2020/fastlane/android-service-account-grant-access.jpg)

위와 같은 화면이 나오면 하단으로 스크롤하여 `ADD USER`를 선택하여 사용자를 등록합니다.

{% include in-feed-ads.html %}

### 안드로이드를 위한 Fastlane 초기화

이제 안드로이드용 Fastlane을 생성해 봅시다. 아래에 명령어를 사용하여 안드로이드용 Fastlane을 생성합니다.

```bash
cd android
fastlane init
```

위에 명령어를 실행하면 아래와 같은 화면을 확인할 수 있습니다.

![Fastlane을 사용한 React Native 앱 자동 배포 - 안드로이드 초기화: package name](/assets/images/category/react-native/2020/fastlane/android-package-name.jpg)

안드로이드 프로젝트의 `Package Name`을 입력합니다.(ex> io.github.dev.yakuza.kumoncho) 그러면 다음과 같이 JSON 파일의 경로를 입력하라는 화면을 확인할 수 있습니다.

![Fastlane을 사용한 React Native 앱 자동 배포 - 안드로이드 초기화: JSON path](/assets/images/category/react-native/2020/fastlane/android-json-path.jpg)

Service Account를 생성했을 때, 다운로드한 JSON 파일을 `android` 폴더에 복사하였습니다. 이 파일의 경로를 지정합니다. (ex> `app-xxx.json`)

![Fastlane을 사용한 React Native 앱 자동 배포 - 안드로이드 초기화: 다운로드 metadata](/assets/images/category/react-native/2020/fastlane/android-download-metadata.jpg)

다음으로 안드로이드를 배포할 때, 등록한 스토어 정보(metadata)를 다운로드할 지 물어봅니다. 저는 이미 배포한 앱을 자동화하기 때문에 스토어 정보를 갱신할 필요가 없었습니다. 따라서 n 입력을 입력하여 스토어 정보를 다운로드하지 않았습니다.

위와 같은 화면 이외에도 여러차례 `Continue by pressing Enter`를 입력하는 화면이 나옵니다. Enter 키를 눌러 진행하여 설정을 완료합니다.

{% include in-feed-ads.html %}

### 안드로이드용 Fastlane 폴더 및 파일

안드로이드의 설정을 완료하면 React Naitve의 android 폴더 밑에 아래에 폴더 및 파일이 생성되는 것을 확인할 수 있습니다.

```bash
|- fastlane
|  |- Appfile
|  |- Fastfile
|- Gemfile
|- Gemfile.lock
```

각 폴더 및 파일을 자세히 살펴보도록 하겠습니다.

- fastlane 폴더: fastlane의 설정 및 실행 파일들이 들어 있는 폴더
- Gemfile, Gemfile.lock: fastlane은 Ruby로 되어있습니다. fastlane을 실행 시키기 위한 라이브러리 설치 파일입니다.

fastlane을 실행하기 위한 설정 내용이 들어 있는 `fastlane/Appfile` 파일을 주석을 제거하고 확인하면 아래와 같습니다.

```ruby
json_key_file("api-xxx.json")
package_name("io.github.dev.yakuza.kumoncho")
```

우리가 설정한 Pacakge Name과 JSON 파일 위치가 설정된 것을 확인할 수 있습니다. 그 다음은 실제로 앱을 배포하기 위한 실행 파일인 `fastlane/Fastfile` 파일을 주석을 제거하면 아래와 같습니다.

```ruby
default_platform(:android)

platform :android do
  desc "Runs all the tests"
  lane :test do
    gradle(task: "test")
  end

  desc "Submit a new Beta Build to Crashlytics Beta"
  lane :beta do
    gradle(task: "clean assembleRelease")
    crashlytics
  end

  desc "Deploy a new version to the Google Play"
  lane :deploy do
    gradle(task: "clean assembleRelease")
    upload_to_play_store
  end
end
```

iOS와는 다르게 `beta`와 `deploy`, 두개의 lane이 생성된 것을 확인할 수 있습니다. 위에 Fastlane도 역시 아래와 같은 명령어로 실행할 수 있습니다.

```bash
# cd android
fastlane beta
fastlane deploy
```

하지만 역시 완벽한 자동화를 위해서는 Fastfile을 수정할 필요가 있습니다.

{% include in-feed-ads.html %}

### 안드로이드용 실행 파일 수정

기본적으로 제공하는 fastlane 파일로는 완벽하게 자동화를 할 수 없습니다. 따라서 안드로이용 배포를 자동화하기 위해 `fastlane/Fastfile` 파일을 아래와 같이 수정합니다.

```ruby
default_platform(:android)

platform :android do
  def increment_version_code()
    path = '../app/build.gradle'
    re = /versionCode\s+(\d+)/

    s = File.read(path)
    versionCode = s[re, 1].to_i
    s[re, 1] = (versionCode + 1).to_s

    f = File.new(path, 'w')
    f.write(s)
    f.close
  end

  def increment_version_number(bump_type: nil, version_number: nil)
    path = '../app/build.gradle'
    re = /versionName\s+("\d+.\d+.\d+")/
    s = File.read(path)
    versionName = s[re, 1].gsub!('"','').split('.')

    major = versionName[0].to_i
    minor = versionName[1].to_i
    patch = versionName[2].to_i

    if (bump_type == 'major')
        major += 1
        minor = 0
        patch = 0
    elsif (bump_type == 'minor')
        minor += 1
        patch = 0
    elsif (bump_type == 'patch')
        patch += 1
    end

    if(version_number)
      s[re, 1] = "\"#{version_number}\""
    else
      s[re, 1] = "\"#{major}.#{minor}.#{patch}\""
    end

    f = File.new(path, 'w')
    f.write(s)
    f.close
    increment_version_code()
  end

  def updateVersion(options)
    if options[:version]
      version = options[:version]
    else
      version = prompt(text: "Enter the version type or specific version\n(major, minor, patch or 1.0.0): ")
    end

    re = /\d+.\d+.\d+/
    versionNum = version[re, 0]

    if (versionNum)
      increment_version_number(
        version_number: versionNum
      )
    elsif (version == 'major' || version == 'minor' || version == 'patch')
      increment_version_number(
        bump_type: version
      )
    else
      UI.user_error!("[ERROR] Wrong version!!!!!!")
    end
  end

  desc "Submit a new Beta Build to Crashlytics Beta"
  lane :beta do |options|
    updateVersion(options)

    gradle(task: "clean bundleRelease")
    upload_to_play_store(
      skip_upload_metadata: true,
      skip_upload_changelogs: true,
      skip_upload_screenshots: true,
      skip_upload_images: true,
      skip_upload_apk: true,
      track: 'internal'
    )
  end

  desc "Deploy a new version to the Google Play"
  lane :release do |options|
    updateVersion(options)

    gradle(task: "clean bundleRelease")
    upload_to_play_store(
      skip_upload_metadata: true,
      skip_upload_changelogs: true,
      skip_upload_screenshots: true,
      skip_upload_images: true,
      skip_upload_apk: true
    )
  end
end
```

추가한 내용을 살펴보면 다음과 같습니다.

```ruby
def increment_version_code()
  path = '../app/build.gradle'
  re = /versionCode\s+(\d+)/

  s = File.read(path)
  versionCode = s[re, 1].to_i
  s[re, 1] = (versionCode + 1).to_s

  f = File.new(path, 'w')
  f.write(s)
  f.close
end

def increment_version_number(bump_type: nil, version_number: nil)
  path = '../app/build.gradle'
  re = /versionName\s+("\d+.\d+.\d+")/
  s = File.read(path)
  versionName = s[re, 1].gsub!('"','').split('.')

  major = versionName[0].to_i
  minor = versionName[1].to_i
  patch = versionName[2].to_i

  if (bump_type == 'major')
      major += 1
      minor = 0
      patch = 0
  elsif (bump_type == 'minor')
      minor += 1
      patch = 0
  elsif (bump_type == 'patch')
      patch += 1
  end

  if(version_number)
    s[re, 1] = "\"#{version_number}\""
  else
    s[re, 1] = "\"#{major}.#{minor}.#{patch}\""
  end

  f = File.new(path, 'w')
  f.write(s)
  f.close
  increment_version_code()
end
```

안드로이드는 iOS와 다르게 앱 버전을 업데이트하는 기능을 제공하지 않습니다.(제가 못찾은 걸 수 도 있습니다. 혹시 아시는 분은 피드백 주세요.) 따라서 안드로이드의 versionCode와 versionName을 업데이트하는 기능을 구현하였습니다.

```ruby
def updateVersion(options)
...
```

update 버전은 iOS에서 설명하였으므로 설명을 생략하도록 하겠습니다.

```ruby
lane :beta do |options|
  updateVersion(options)

  gradle(task: "clean bundleRelease")
  upload_to_play_store(
    skip_upload_metadata: true,
    skip_upload_changelogs: true,
    skip_upload_screenshots: true,
    skip_upload_images: true,
    skip_upload_apk: true,
    track: 'internal'
  )
end
```

안드로이드는 gradle의 clean과 bundleRelease로 앱을 빌드하도록 하였습니다.(`assembleRelease`이 아님) 또한, upload_to_play_store의 `track: 'internal'`을 사용하여 internal test용으로 배포하도록 하였습니다.

안드로이드는 iOS와 다르게 Release notes(change log)를 작성할 필요가 없기 때문에 스토어와 관련된 모든 기능은 skip 하도록 설정하였습니다.

마지막으로 bundleRelease를 통해 aab 파일을 생성하고 업로드할 예정이므로 skip_upload_apk를 true로 설정하였습니다.

```ruby
desc "Deploy a new version to the Google Play"
lane :release do |options|
  updateVersion(options)

  gradle(task: "clean bundleRelease")
  upload_to_play_store(
    skip_upload_metadata: true,
    skip_upload_changelogs: true,
    skip_upload_screenshots: true,
    skip_upload_images: true,
    skip_upload_apk: true
  )
end
```

구글 플레이에 배포용 스크립트입니다. iOS와 동일하게 하기 위해 `lane :deploy`를 `lane :release`로 변경하였습니다.

upload_to_play_store의 track 파라메터가 없는 것외에는 beta용과 동일하기 때문에 자세한 설명은 생략하도록 하겠습니다.

{% include in-feed-ads.html %}

### 안드로이드용 fastlane 실행

이제 fastlane을 사용하여 안드로이드를 자동으로 배포할 준비가 끝났습니다. 이제 fastlane을 사용하여 앱을 자동 배포해 봅시다.

아래에 명령어를 사용하여 React Native로 제작한 앱을 internal test에 배포해 봅니다.

```bash
# cd android
fastlane beta version:patch
```

배포가 완료될 때까지, 상단한 시간이 걸립니다. 배포가 완료되면 아래와 같은 화면을 확인할 수 있습니다.

![Fastlane을 사용한 React Native 앱 자동 배포 - 안드로이드 internal test 배포](/assets/images/category/react-native/2020/fastlane/android-fastlane-beta.jpg)

물론 Play store console에서도 internal test에 잘 배포된 것을 확인할 수 있습니다.

그럼 이제 아래에 명령어를 실행하여 실제로 배포를 진행해 봅니다.

```bash
# cd android
fastlane release version:patch
```

배포가 완료되면 아래와 같은 화면을 확인할 수 있습니다.

![Fastlane을 사용한 React Native 앱 자동 배포 - 안드로이드 앱 스토어 배포](/assets/images/category/react-native/2020/fastlane/android-fastlane-release.jpg)

또한 Google Play store에도 잘 배포된 것을 확인할 수 있습니다.

{% include in-feed-ads.html %}

## package.json

저는 이렇게 만든 fastlane을 실행하는 명령어를 아래와 같이 package.json에 작성해서 사용하고 있습니다.

```json
"scripts": {
  ...
  "beta:android": "npm run prebuild-android && cd ./android && bundle exec fastlane beta version:patch",
  "beta:ios": "cd ./ios && bundle exec fastlane beta version:patch",
  "beta": "npm run beta:android && npm run beta:ios",
  "release:android": "npm run prebuild-android && cd ./android && bundle exec fastlane release version:patch",
  "release:ios": "cd ./ios && bundle exec fastlane release version:patch",
  "release": "npm run release:android && npm run release:ios"
},
```

## gitignore

fastlane을 통해 배포를 하면, 그에 따른 파일들이 생성됩니다. git에서 관리하지 않기 위해 `.gitignore` 파일에 아래와 같은 내용을 추가하였습니다.

```bash
...
# fastlane
ios/*.mobileprovision
ios/*.cer
ios/*.dSYM.zip
android/fastlane/README.md
ios/fastlane/README.md
```

## 완료

이것으로 fastlane을 사용해서 React Native로 제작한 앱을 자동으로 배포하는 방법에 대해서 알아보았습니다. 이번 블로그에서 설명한 내용은 물론 Native로 개발된 앱에서도 활용할 수 있으므로 많은 분들께 도움이 되었으면 좋겠네요.

이번 fastlane을 도입함으로써 그동안 쓸때없이 낭비되던 시간을 절약할 수 있게 되어서 너무 편한거 같습니다. 여러분도 꼭 한번 사용해 보시기 바랍니다.
