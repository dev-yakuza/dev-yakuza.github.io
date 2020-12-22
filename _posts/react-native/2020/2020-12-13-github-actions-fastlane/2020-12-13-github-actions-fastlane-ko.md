---
layout: 'post'
permalink: '/react-native/github-actions-fastlane/'
paginate_path: '/react-native/:num/github-actions-fastlane/'
lang: 'ko'
categories: 'react-native'
comments: true

title: GitHub Actions와 Fastlane을 사용해서 React Native 앱 배포하기
description: GitHub Actions와 Fastlane을 사용해서 React Native로 개발한 앱을 자동으로 배포해 봅시다.
image: '/assets/images/category/react-native/2020/github-actions-fastlane/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [Fastlane 준비](#fastlane-준비)
  - [안드로이드 Fastlane 준비](#안드로이드-fastlane-준비)
  - [iOS Fastlane 준비](#ios-fastlane-준비)
  - [Certificate](#certificate)
  - [Provisioning profile](#provisioning-profile)
  - [Signing & Capabilities](#signing--capabilities)
  - [API key](#api-key)
  - [iOS Fastlane](#ios-fastlane)
- [GitHub Actions](#github-actions)
  - [iOS GitHub Actions](#ios-github-actions)
  - [안드로이드 GitHub Actions](#안드로이드-github-actions)
- [스크립트](#스크립트)
- [완료](#완료)

</div>

## 개요

React Native를 사용해서 취미로 앱을 개발을 하다보니, 앱이 점점 많아져서 앱을 배포할 때 상단한 시간이 걸리기 시작했습니다.

- 취미로 만든 앱 리스트: [App List]({{site.url}}/app/list/ko){:target="_blank"}

그래서 React Native로 만든 앱을 자동으로 배포하는 방법으로 `Fastlane`이라는 툴을 사용하여 자동으로 배포하고 있습니다.

- [Fastlane을 통한 앱 자동 배포]({{site.url}}/{{page.categories}}/fastlane/){:target="_blank"}

하지만, 로컬 머신에서 `Fastlane`으로 앱을 하나씩 배포하는데 30분 정도 걸리고, 앱이 20개가 넘어가면서 로컬에서만 배포를 시도하는데도, 하나의 앱이 다 배포되고 나서 다음 앱이 배포됨으로 여전히 시간이 많이 걸리고 있습니다.

그래서 이런 배포 과정을 좀 더 효율적으로 하기 위해, `GitHub Actions`를 사용하여 배포하도록 시스템을 구성해 보았습니다.

- [GitHub Actions](https://github.com/features/actions){:rel="nofollow noreferrer" target="_blank"}

이번 블로그 포스트에서는 GitHub Actions와 Fastlane을 사용하여 배포하는 방법에 대해서 알아보겠습니다.

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
- [Fastlane을 통한 앱 자동 배포]({{site.url}}/{{page.categories}}/fastlane/){:target="_blank"}

{% include in-feed-ads.html %}

## Fastlane 준비

우선 이전 블로그 포스트를 참고하여 Fastlane으로 배포할 준비를 합니다.

- [Fastlane을 통한 앱 자동 배포]({{site.url}}/{{page.categories}}/fastlane/){:target="_blank"}

하지만 이전 블로그 포스트에서 준비한 Fastlane은 바로 사용할 수 없습니다. 왜냐하면, 이전 Fastlane은 앱 버전을 올리며, 올린 버전을 GitHub에서 관리해야하는데, GitHub Actions 서버에서는 변경 사항을 커밋하고 저장하기 어렵기 때문입니다.

따라서, 버전은 로컬에서 올리고, GitHub Actions를 사용하여 서버에서는 단순히 배포만 진행하도록 Fastlane을 수정해야 합니다.

### 안드로이드 Fastlane 준비

안드로이드 Fastlane은 단순합니다. 이미 인증키를 사용해서 배포를 했기 때문에, 특별한 설정을 추가로 해 줄 필요가 없습니다. 다만 기존의 Fastlane을 버전을 업로드하는 Fastlane과 GitHub Actions에서 사용할 Fastlane으로 나눌 필요가 있습니다.

- 기존의 Fastlane

```ruby
desc 'Deploy a new version to the Google Play'
lane :release do |options|
  updateVersion(options)

  gradle(task: 'clean bundleRelease')
  upload_to_play_store(
    skip_upload_metadata: true,
    skip_upload_changelogs: true,
    skip_upload_screenshots: true,
    skip_upload_images: true,
    skip_upload_apk: true
  )
end
```

- 추가한 Fastlane

```ruby
desc 'GitHub actions release'
lane :version do |options|
  updateVersion(options)
end

lane :github do |_options|
  gradle(task: 'clean bundleRelease')
  upload_to_play_store(
    skip_upload_metadata: true,
    skip_upload_changelogs: true,
    skip_upload_screenshots: true,
    skip_upload_images: true,
    skip_upload_apk: true
  )
end
```

기존의 Fastlane은 로컬에서도 배포할 경우가 생길 수 있으므로 그대로 유지하고, 해당 Fastlane의 기능을 `version`과 `github`이라는 Fastlane으로 나누어 추가하였습니다.

GitHub Actions를 사용하기 전에 로컬에서 Fastlane의 `version`을 사용하여 버전을 업로드하고 GitHub Actions에서는 `github`이라는 Fastlane으로 앱을 배포할 예정입니다.

{% include in-feed-ads.html %}

### iOS Fastlane 준비

iOS에서 Fastlane은 인증서, 2FA 인증 등으로 인해 조금 복잡합니다.

### Certificate

일단 로컬에서 배포에 사용하는 인증서를 서버에서도 사용할 수 있게 해야합니다. `Keychain Access`를 열고 현재 사용하고 있는 인증서에서 마우스 오른쪽 클릭을 하고, `Export` 메뉴를 선택합니다.

![Export Certificate](/assets/images/category/react-native/2020/github-actions-fastlane/certificate.jpg)

메뉴를 선택하면 암호를 입력하는 화면이 나옵니다. 해당 암호는 나중에 Fastlane에도 설정을 해야함으로 잘 기억해 둡니다.

이렇게 저장한 파일을 React Native 프로젝트의 `ios` 폴더에 복사합니다. 저는 알기 쉽게 하기 위해 파일명을 `distribution.p12`으로 변경하여 저장하였습니다.

### Provisioning profile

서버에서 iOS 앱을 배포하기 위해서는 `Provisioning profile`가 필요합니다. Provisioning profile 파일을 다운로드받기 위해 애플 개발자 사이트로 이동합니다.

- [https://developer.apple.com/account/resources/profiles/list](https://developer.apple.com/account/resources/profiles/list){:rel="nofollow noreferrer" target="_blank"}

그리고 GitHub Actions를 통해 배포하려는 앱의 Provisioning profile 파일을 다운로드받습니다.

![Export Certificate](/assets/images/category/react-native/2020/github-actions-fastlane/provisioning_profile.jpg)

이렇게 저장한 파일을 React Native 프로젝트의 `ios` 폴더에 복사합니다. 저는 알기 쉽게 하기 위해 파일명을 `distribution.mobileprovision`으로 변경하여 저장하였습니다.

{% include in-feed-ads.html %}

### Signing & Capabilities

GitHub Actions를 사용하여 앱을 배포하기 위에서 다운로드한 `Provisioning profile`을 설정하고 `Automatically manage signing`을 해제할 필요가 있습니다. `ios/[Your project name].xcworkspace` 파일을 실행하여 xcode를 실행합니다.

![signing and capabilities](/assets/images/category/react-native/2020/github-actions-fastlane/signing_and_capabilities.jpg)

그리고 `Signing & Capabilities`로 이동한 후, `Automatically manage signing`를 사용하지 않기 위해 체크를 해제합니다. 또한 앞에서 다운로드한 Provisioning profile 파일을 설정하기 위해 `Provisioning Profile` 항목 옆에 드롭 다운 메뉴를 선택한 후 `Import Profile...`를 선택하여 위에서 다운로드한 파일을 설정합니다.

### API key

Fastlane으로 앱을 배포할 때, 애플 아이디로 로그인을 하고 여러 동작을 수행하게 됩니다. 하지만 애플 개발자 계정에는 `2FA`가 설정되어 있어 서버(CI)를 통해 배포할 경우, 로그인을 할 수 없어 문제가 발생합니다.

애플에서는 이 2FA 인증을 대신하기 위한 `API Key`를 제공하고 있습니다. API Key를 생성하기 위해서 Appstoreconnect의 `Users and Access` 페이지로 이동합니다.

- [https://appstoreconnect.apple.com/access/api](https://appstoreconnect.apple.com/access/api){:rel="nofollow noreferrer" target="_blank"}

해당 페이지에서 추가 버튼을 눌러 API Key를 생성합니다. 여러 질문들이 나오는데 잘 읽어보고 대답하면 큰 문제없이 생성할 수 있습니다.

이렇게 생성한 API Key에서 `Issuer ID`, `Key ID` 그리고 다운로드한 키 파일은 추후 FastLane에 설정하여 사용하게 됩니다. 여기서 다운로드 한 파일은 React Native 프로젝트의 `ios` 폴더에 복사합니다. 저는 알기 쉽게 하기 위해 파일명을 `distribution.p8`로 변경하여 저장하였습니다.

{% include in-feed-ads.html %}

### iOS Fastlane

배포를 위해 필요한 파일들은 모두 준비되었습니다. 이제 Fastlane 파일을 수정하여 배포 준비를 합니다.

```ruby
desc 'GitHub actions release'
lane :version do |options|
  updateVersion(options)
  increment_build_number(xcodeproj: '[Your Project Name].xcodeproj')
end

lane :github do |_options|
  create_keychain(
    name: 'ios_app_keychain',
    password: 'XXXXXXXXX',
    timeout: 1800,
    default_keychain: true,
    unlock: true,
    lock_when_sleeps: false
  )
  import_certificate(
    certificate_path: 'distribution.p12',
    certificate_password: 'XXXXXXXXXXX',
    keychain_name: 'ios_app_keychain',
    keychain_password: 'XXXXXXXXX'
  )
  install_provisioning_profile(path: 'distribution.mobileprovision')
  update_project_provisioning(
    xcodeproj: '[Your Project Name].xcodeproj',
    target_filter: 'github',
    profile: 'distribution.mobileprovision',
    build_configuration: 'Release'
  )
  api_key = app_store_connect_api_key(
    key_id: 'XXXXXXXXXXXXx',
    issuer_id: 'XXXXXXX-XXXXXXXXXXXXX-XXXXXXXXXXX',
    key_filepath: 'distribution.p8'
  )

  build_app(workspace: '[Your Project Name].xcworkspace', scheme: '[Your Project Name]')
  upload_to_app_store(
    force: true,
    reject_if_possible: true,
    skip_metadata: false,
    skip_screenshots: true,
    languages: ['ko'],
    release_notes: {
      'default' => 'bug fixed',
      'ko' => 'bug fixed'
    },
    submit_for_review: true,
    precheck_include_in_app_purchases: false,
    automatic_release: true,
    submission_information: {
      add_id_info_uses_idfa: true,
      add_id_info_serves_ads: true,
      add_id_info_tracks_install: true,
      add_id_info_tracks_action: false,
      add_id_info_limits_tracking: true,
      export_compliance_encryption_updated: false
    },
    api_key: api_key
  )
end
```

안드로이드와 마찬가지로 버전을 올리는 Fastlane과 배포를 위한 Fastlane을 나누었습니다. 하지만, 안드로이드와 다르게 배포를 위한 Fastlane을 조금 수정해야 합니다.

우선 iOS 앱 배포를 위한 `Certificate`를 설정할 필요가 있습니다.

```ruby
create_keychain(
  name: 'ios_app_keychain',
  password: 'XXXXXXXXX',
  timeout: 1800,
  default_keychain: true,
  unlock: true,
  lock_when_sleeps: false
)
import_certificate(
  certificate_path: 'distribution.p12',
  certificate_password: 'XXXXXXXXXXX',
  keychain_name: 'ios_app_keychain',
  keychain_password: 'XXXXXXXXX'
)
```

Keychain Access에서 다운로드한 `distribution.p12` 파일을 설정하고, 내보낼 때 사용한 패스워드를 설정합니다. `create_keychain`의 `password`와 `import_certificate`의 `keychain_password`는 Certificate를 내보낼 때 사용한 패스워드와 관계가 없으며, 두 패스워드에는 같은 패스워드를 설정하면 됩니다.

```ruby
install_provisioning_profile(path: 'distribution.mobileprovision')
update_project_provisioning(
  xcodeproj: '[Your Project Name].xcodeproj',
  target_filter: 'github',
  profile: 'distribution.mobileprovision',
  build_configuration: 'Release'
)
```

그리고 위와 같이 `Provisioning profile` 파일을 설정합니다. 그리고 다음과 같이 API Key를 사용하기 위해 `app_store_connect_api_key` 함수를 호출하고 결과를 `api_key` 변수에 할당합니다.

```ruby
api_key = app_store_connect_api_key(
  key_id: 'XXXXXXXXXXXXx',
  issuer_id: 'XXXXXXX-XXXXXXXXXXXXX-XXXXXXXXXXX',
  key_filepath: 'distribution.p8'
)
```

마지막으로 이전에 만든 Fastlane을 사용하여 앱을 배포하도록 설정합니다. 다만 API Key를 사용해 배포함으로 `upload_to_app_store`에서 다음과 같이 설정을 수정해야 합니다.

```ruby
upload_to_app_store(
  ...
  precheck_include_in_app_purchases: false,
  ...
  api_key: api_key
)
```

앞에서 할당한 `api_key`를 설정하고 `precheck_include_in_app_purchases`를 `false`로 설정합니다. `precheck_include_in_app_purchases`을 설정하지 않으면 배포 도중에 에러가 발생합니다.

{% include in-feed-ads.html %}

## GitHub Actions

그럼 이제 `GitHub Actions`를 사용하기 위해서, GtiHub Actions에 필요한 설정 파일을 생성할 필요가 있습니다. React Native 프로젝트 폴더에 `.github/workflows/main.yml` 파일을 생성하고 다음과 같이 수정합니다.

```yaml
name: Publish iOS and Android App to App Store and Play Store
on:
  push:
    tags:
      - "v*"
jobs:
  release-ios:
    name: Build and release iOS app
    runs-on: macos-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-node@v1
        with:
          node-version: "10.x"
      - uses: actions/setup-ruby@v1
        with:
          ruby-version: "2.x"
      - name: Install Fastlane
        run: cd ios && bundle install && cd ..
      - name: Install packages
        run: yarn install
      - name: Install pods
        run: cd ios && pod install && cd ..
      - name: Execute Fastlane command
        run: cd ios && fastlane github
  release-android:
    name: Build and release Android app
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-node@v1
        with:
          node-version: "10.x"
      - uses: actions/setup-ruby@v1
        with:
          ruby-version: "2.x"
      - name: Install Fastlane
        run: cd android && bundle install && cd ..
      - name: Install packages
        run: yarn install
      - name: Prebuild
        run: npm run prebuild-android
      - name: Execute Fastlane command
        run: cd android && fastlane github
```

우선 GitHub Actions의 이름을 설정하고 언제 GitHub Actions를 실행할지 설정합니다.

```yaml
name: Publish iOS and Android App to App Store and Play Store
on:
  push:
    tags:
      - "v*"
```

저는 `v`로 시작하는 태그가 `push`되면 GitHub Actions가 실행되게 설정하였습니다.

```yaml
jobs:
  release-ios:
  release-android:
```

그리고 실제로 실행될 명령어들을 안드로이드와 iOS를 구별해서 설정하였습니다.

{% include in-feed-ads.html %}

### iOS GitHub Actions

GitHub Actions에서 iOS에 사용하는 명령어들을 살펴봅시다.

```yaml
jobs:
  release-ios:
    name: Build and release iOS app
    runs-on: macos-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-node@v1
        with:
          node-version: "10.x"
      - uses: actions/setup-ruby@v1
        with:
          ruby-version: "2.x"
      - name: Install Fastlane
        run: cd ios && bundle install && cd ..
      - name: Install packages
        run: yarn install
      - name: Install pods
        run: cd ios && pod install && cd ..
      - name: Execute Fastlane command
        run: cd ios && fastlane github
```

우선 iOS는 `runs-on: macos-latest`를 통해 맥OS에서 명령어들이 실행될 수 있도록 설정하였습니다.

```yaml
- uses: actions/checkout@v2
```

그리고 현재 Repository의 소스 코드를 가져온 후,

```yaml
- uses: actions/setup-node@v1
  with:
    node-version: "10.x"
- uses: actions/setup-ruby@v1
  with:
    ruby-version: "2.x"
```

노드와 루비를 설치합니다.

```yml
- name: Install Fastlane
  run: cd ios && bundle install && cd ..
- name: Install packages
  run: yarn install
- name: Install pods
  run: cd ios && pod install && cd ..
```

그 후, Fastlane, 노드 패키지, 그리고 Pod 라이브러리를 설치합니다.

```yml
- name: Execute Fastlane command
  run: cd ios && fastlane github
```

마지막으로 우리가 만든 Fastlane의 github를 실행합니다.

{% include in-feed-ads.html %}

### 안드로이드 GitHub Actions

GitHub Actions에서 안드로이드에 사용하는 명령어들을 살펴봅시다.

```yaml
jobs:
  release-android:
    name: Build and release Android app
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-node@v1
        with:
          node-version: "10.x"
      - uses: actions/setup-ruby@v1
        with:
          ruby-version: "2.x"
      - name: Install Fastlane
        run: cd android && bundle install && cd ..
      - name: Install packages
        run: yarn install
      - name: Prebuild
        run: npm run prebuild-android
      - name: Execute Fastlane command
        run: cd android && fastlane github
```

우선 안드로이드는 `runs-on: ubuntu-latest`를 통해 ubuntu 서버에서 명령어들이 실행될 수 있도록 설정하였습니다.

```yaml
- uses: actions/checkout@v2
```

그리고 현재 Repository의 소스 코드를 가져온 후,

```yaml
- uses: actions/setup-node@v1
  with:
    node-version: "10.x"
- uses: actions/setup-ruby@v1
  with:
    ruby-version: "2.x"
```

노드와 루비를 설치합니다.

```yaml
- name: Install Fastlane
  run: cd ios && bundle install && cd ..
- name: Install packages
  run: yarn install
```

그 후, Fastlane 그리고 노드 패키지를 설치합니다.

```yaml
- name: Prebuild
  run: npm run prebuild-android
```

그리고 안드로이드 배포 파일을 생성하기 위해 `prebuild-android`를 실행합니다. 이 명령어는 제가 개인적으로 `package.json`의 `scripts`에 설정한 명령어로 다음과 같습니다.

```json
...
"scripts": {
  ...
  "prebuild-android": "npx jetify && react-native bundle --platform android --dev false --entry-file index.js --bundle-output android/app/src/main/assets/index.android.bundle",
  ...
}
...
```

마지막으로 우리가 만든 Fastlane의 github를 실행합니다.

```yaml
- name: Execute Fastlane command
  run: cd android && fastlane github
```

{% include in-feed-ads.html %}

## 스크립트

이제 이렇게 만든 Fastlane과 GitHub Actions를 사용하기 위해 다음과 같은 명령어를 사용합니다.

```bash
VERSION=$1

cd android
fastlane version version:$VERSION
cd ..
cd ios
fastlane version version:$VERSION
cd ..

git add .
git commit -m 'update version'
git push origin main

git tag -a v$VERSION -m 'add verstion tag' -f
git push origin v$VERSION -f
```

안드로이드 폴더와 iOS 폴더로 이동하여 앞에서 만든 Fastlane의 version을 사용하여 로컬에서 배포할 앱의 버전을 변경합니다.

```bash
cd android
fastlane version version:$VERSION
cd ..
cd ios
fastlane version version:$VERSION
cd ..
```

이렇게 변경한 버전을 Git에서 관리하기 위해 Commit과 Push를 해둡니다.

```bash
git add .
git commit -m 'update version'
git push origin main
```

마지막으로 Tag를 설정하고 Push해서 GitHub Actions를 실행합니다.

```bash
git tag -a v$VERSION -m 'add verstion tag' -f
git push origin v$VERSION -f
```

이렇게 만든 파일을 React Native 프로젝트 폴더에 `release.sh` 이름으로 저장합니다. 그리고 GitHub Actions를 통해 앱을 배포하고 싶을 때 다음과 같은 명령어를 실행합니다.

```bash
# sh ./release.sh 3.3.1
# sh ./release.sh major
# sh ./release.sh minor
sh ./release.sh patch
```

## 완료

이것으로 GitHub Actions와 Fastlane을 사용하여 앱을 배포하는 방법에 대해서 알아보았습니다. 자료가 많이 없어 구축하는데 고생을 했습니다. 이 자료가 다른 분들께도 조금이라도 도움이 되면 좋겠습니다.

저는 iOS에서 많은 에러가 발생하여 굉장히 고생했습니다. 또한 무료 사용자는 GitHub Actions를 사용할 수 있는 시간이 한달에 2,000분이고 맥OS를 사용하는 경우, 리눅스 서버보다 사용 시간을 10배로 계산하는 문제가 있습니다. 보통 iOS 앱 하나를 배포하는데 30분 정도가 걸리니깐, 한 번 배포에 300분의 시간을 사용하는 것으로 계산됩니다. 따라서 무료로 한 달에 배포할 수 있는 회수는 8번 정도 밖에 안되겠네요. 안드로이드는 10분정도만 걸리고 리눅스이므로 10분, 그대로 계산되므로 큰 문제가 없는데, 맥OS는 좀 많이 신경이 쓰이네요. 혹시 다른 GitHub Actions들과 사용하신다면, 이 사용 시간에 주의할 필요가 있습니다.

이제 여러분도 GitHub Actions을 사용해서 효율적으로 앱을 배포해 보시기 바랍니다.
