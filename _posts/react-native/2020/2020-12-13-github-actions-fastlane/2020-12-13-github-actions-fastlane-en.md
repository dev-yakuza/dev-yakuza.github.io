---
layout: 'post'
permalink: '/react-native/github-actions-fastlane/'
paginate_path: '/react-native/:num/github-actions-fastlane/'
lang: 'en'
categories: 'react-native'
comments: true

title: GitHub Actions and Fastlane for deploying React Native App
description: Let's see how to deploy React Native App with GitHub Actions and Fastlane.
image: '/assets/images/category/react-native/2020/github-actions-fastlane/background.jpg'
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [Prepare Fastlane](#prepare-fastlane)
  - [Prepare Fastlane for Android](#prepare-fastlane-for-android)
  - [Prepare Fastlane for iOS](#prepare-fastlane-for-ios)
  - [Certificate](#certificate)
  - [Provisioning profile](#provisioning-profile)
  - [Signing & Capabilities](#signing--capabilities)
  - [API key](#api-key)
  - [iOS Fastlane](#ios-fastlane)
- [GitHub Actions](#github-actions)
  - [iOS GitHub Actions](#ios-github-actions)
  - [Android GitHub Actions](#android-github-actions)
- [Scripts](#scripts)
- [Completed](#completed)

</div>

## Outline

I have a hobby to develop Apps with React Native, and I already have some apps. When I deploy them, it takes much times.

- App list: [App List]({{site.url}}/app/list/en){:target="_blank"}

So I use `Fastlane` tool to deploy React Native App automatically to save the time.

- [Deploy automatically applications via Fastlane]({{site.url}}/{{page.categories}}/fastlane/){:target="_blank"}

However, the deployment with `Fastlane` takes 30 min for a app on local, and I have apps more than 20, so the deployment still takes too much time because the apps are deployed one by one.

So, to make the deployment efficiently,, I try to make a system with `GitHub Actions`.

- [GitHub Actions](https://github.com/features/actions){:rel="nofollow noreferrer" target="_blank"}

In this blog post, we will see how to use GitHub Actions and Fastlane to deploy React Native App.

If you don't know React Native deployment, see the previous blog posts.

- iOS
  - [iOS build and test]({{site.url}}/{{page.categories}}/ios-running-on-device/){:target="_blank"}
  - [iOS device test]({{site.url}}/{{page.categories}}/ios-test-on-device/){:target="_blank"}
  - [enroll iOS developer]({{site.url}}/{{page.categories}}/ios-enroll-developer-program/){:target="_blank"}
  - [iOS Certification]({{site.url}}/{{page.categories}}/ios-certification/){:target="_blank"}
  - [iOS TestFlight]({{site.url}}/{{page.categories}}/ios-testflight/){:target="_blank"}
  - [register iOS App store]({{site.url}}/{{page.categories}}/ios-app-store/){:target="_blank"}
- Android
  - [Android device test]({{site.url}}/{{page.categories}}/android-test-on-device/){:target="_blank"}
  - [Android build and test]({{site.url}}/{{page.categories}}/android-running-on-device/){:target="_blank"}
  - [enroll Android developer]({{site.url}}/{{page.categories}}/android-enroll-google-play-developer/){:target="_blank"}
  - [register Android App store]({{site.url}}/{{page.categories}}/android-google-play/){:target="_blank"}
- [Deploy automatically applications via Fastlane]({{site.url}}/{{page.categories}}/fastlane/){:target="_blank"}

{% include in-feed-ads.html %}

## Prepare Fastlane

First, prepare Fastlane by seeing the previous blog post.

- [Deploy automatically applications via Fastlane]({{site.url}}/{{page.categories}}/fastlane/){:target="_blank"}

But we can't use the previous Fastlane from the previous blog post. Because, the previous Fastlane is updating the app versions, and we controlled that version on GitHub. However, it's difficult to commit and push on GitHub Actions server.

So, we need to make a new Fastlane to update the version on local and only deploy with GitHub Actions.

### Prepare Fastlane for Android

Android Fastlane is very simple. We already deployed wit the authentication key, so we don't need to set any configuration. Just, we need to separate the previous Fastlane to the Fastlane updating the version and Fastlane used on GitHub Acitions.

- Previous Fastlane

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

- New Fastlane

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

In my case, I also need to deploy on local, so I keep the previous Fastlane. I just added new `version` and `github` lanes to Fastlane.

Before using GitHub Actions to deploy the app, we'll use `version` lane on local to update the app version and commits it on Git, and use `github` lane to deploy the app on GitHub Actions.

{% include in-feed-ads.html %}

### Prepare Fastlane for iOS

iOS is a little bit complicated because of the certification and 2FA.

### Certificate

We need to make the certification on local can be used on the server. Open `Keychain Access` and right-click the current certification, and click `Export` menu.

![Export Certificate](/assets/images/category/react-native/2020/github-actions-fastlane/certificate.jpg)

When you click the menu, you'll see the modal to insert a password. this password will be used on Fastlane, so remember it.

Copy the certification file downloaded to `ios` folder in React Native project. I renamed the file name to `distribution.p12` to recognize it easily.

### Provisioning profile

We need `Provisioning profile` to deploy the iOS app on the server. To download the Provisioning profile, go to the Apple developer site.

- [https://developer.apple.com/account/resources/profiles/list](https://developer.apple.com/account/resources/profiles/list){:rel="nofollow noreferrer" target="_blank"}

And then download the Provisioning profile that you want to deploy the app via GitHub Actions.

![Export Certificate](/assets/images/category/react-native/2020/github-actions-fastlane/provisioning_profile.jpg)

And copy the downloaded file to `ios` folder in React Native project. I renamed the file to `distribution.mobileprovision` to recognize it easily.

{% include in-feed-ads.html %}

### Signing & Capabilities

Next, we need to configure `Provisioning profile` that we downloaded above, and uncheck `Automatically manage signing`. Open `ios/[Your project name].xcworkspace` to execute the Xcode.

![signing and capabilities](/assets/images/category/react-native/2020/github-actions-fastlane/signing_and_capabilities.jpg)

And go to `Signing & Capabilities`, uncheck `Automatically manage signing`. Also, click `Provisioning Profile` dropdown, and click `Import Profile...` and select the Provisioning profile that we downloaded above.

### API key

When we deploy the app with Fastlane, Fastlane logs in with Apple developer ID and deploys it. However, the Apple developer account has `2FA`, so we can't use it on the server(CI) because can't login.

So, Apple provides `API Key` for the 2FA. To create API Key, go to `Users and Access` page on Appstoreconnect

- [https://appstoreconnect.apple.com/access/api](https://appstoreconnect.apple.com/access/api){:rel="nofollow noreferrer" target="_blank"}

Click the plus(+) button to create API Key. You'll see some questions in the modal, just read and answer correctly to create it.

After creating the API Key, copy `Issuer ID`, `Key ID` and download the key file. We'll use them on Fastlane. the key file need to be copied to `ios` folder in React Native Project. I renamed it to `distribution.p8` to recognize it easily.

{% include in-feed-ads.html %}

### iOS Fastlane

We've prepared all files. Let's see how to make a new lane in Fastlane.

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

Like Android, I made two lanes that one is for updating the app version and another is for deploying on GitHub Actions. However, unlike Android, we need to modify the deployment lane.

First, we need to configure `Certificate` to deploy the app.

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

set the `distribution.p12` from Keychain Access, and set the password that you use when you export the file. The `password` in `create_keychain` and `keychain_password` in `import_certificate` is not related to the password when you export the file, so you can set anything. (I just set same password)

```ruby
install_provisioning_profile(path: 'distribution.mobileprovision')
update_project_provisioning(
  xcodeproj: '[Your Project Name].xcodeproj',
  target_filter: 'github',
  profile: 'distribution.mobileprovision',
  build_configuration: 'Release'
)
```

And then, configure `Provisioning profile` file like above. And assign `api_key` variable to call `app_store_connect_api_key` to use the API Key like below.

```ruby
api_key = app_store_connect_api_key(
  key_id: 'XXXXXXXXXXXXx',
  issuer_id: 'XXXXXXX-XXXXXXXXXXXXX-XXXXXXXXXXX',
  key_filepath: 'distribution.p8'
)
```

Lastly, use `upload_to_app_store` to deploy the app. At this time, we need to set the API Key like below.

```ruby
upload_to_app_store(
  ...
  precheck_include_in_app_purchases: false,
  ...
  api_key: api_key
)
```

set the `api_key` assigned above, and `false` to `precheck_include_in_app_purchases`. If you don't set `precheck_include_in_app_purchases`, you'll get the error when you deploy the app.

{% include in-feed-ads.html %}

## GitHub Actions

To use `GitHub Actions`, we need to create the configuration file for GitHub Actions. Create `.github/workflows/main.yml` file in React Native project and modify it like below.

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

First, set the name of GitHub Actions, and configure the trigger of GitHub Actions.

```yaml
name: Publish iOS and Android App to App Store and Play Store
on:
  push:
    tags:
      - "v*"
```

In my case, I set when the tag started with `v` is `push`ed to GitHub, GitHub Actions is executed.

```yaml
jobs:
  release-ios:
  release-android:
```

And configure both of Android and iOS separately.

{% include in-feed-ads.html %}

### iOS GitHub Actions

Let's see the GitHub Actions command list for iOS.

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

First, configure `runs-on: macos-latest` to execute the commands on macOS for iOS.

```yaml
- uses: actions/checkout@v2
```

And get the source code of the repository.

```yaml
- uses: actions/setup-node@v1
  with:
    node-version: "10.x"
- uses: actions/setup-ruby@v1
  with:
    ruby-version: "2.x"
```

Install Node and Ruby.

```yml
- name: Install Fastlane
  run: cd ios && bundle install && cd ..
- name: Install packages
  run: yarn install
- name: Install pods
  run: cd ios && pod install && cd ..
```

after it, install Fastlane, Node Packages, and Pod libraries.

```yml
- name: Execute Fastlane command
  run: cd ios && fastlane github
```

Lastly, execute the github lane in Fastlane that we created above.

{% include in-feed-ads.html %}

### Android GitHub Actions

Let's see the GitHub Actions commands for Android.

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

First, configure `runs-on: ubuntu-latest` to execute the command list on the ubuntu server for Android.

```yaml
- uses: actions/checkout@v2
```

And then, get the source code of the current repository.

```yaml
- uses: actions/setup-node@v1
  with:
    node-version: "10.x"
- uses: actions/setup-ruby@v1
  with:
    ruby-version: "2.x"
```

And install Node and Ruby.

```yaml
- name: Install Fastlane
  run: cd ios && bundle install && cd ..
- name: Install packages
  run: yarn install
```

After it, install Fastlane and Node packages.

```yaml
- name: Prebuild
  run: npm run prebuild-android
```

And then, run `prebuild-android` command to build the Android deployment file. This command is that I made on `scripts` in `package.json` personally. The command is like below.

```json
...
"scripts": {
  ...
  "prebuild-android": "npx jetify && react-native bundle --platform android --dev false --entry-file index.js --bundle-output android/app/src/main/assets/index.android.bundle",
  ...
}
...
```

Lastly, execute the github lane of Fastlane that we made above.

```yaml
- name: Execute Fastlane command
  run: cd android && fastlane github
```

{% include in-feed-ads.html %}

## Scripts

I use the commands like below that I execute the Fastlane and GitHub Actions.

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

Go to Android folder and iOS folder, and execute the version lane of the Fastlane to update the app version on local.

```bash
cd android
fastlane version version:$VERSION
cd ..
cd ios
fastlane version version:$VERSION
cd ..
```

And then, commit and push the changed version on Git.

```bash
git add .
git commit -m 'update version'
git push origin main
```

Lastly, set the Tag and push it to execute GitHub Actions.

```bash
git tag -a v$VERSION -m 'add verstion tag' -f
git push origin v$VERSION -f
```

I created `release.sh` includes scripts above in the root folder of React Native project. And if I want to deploy, I use the command like below.

```bash
# sh ./release.sh 3.3.1
# sh ./release.sh major
# sh ./release.sh minor
sh ./release.sh patch
```

## Completed

We've seen how to use GitHub Actions and Fastlane to deploy the app. I had a hard time to make this system because there are not many contents about this. I hope this blog post helps someone to build it!

I got many errors on iOS. Also, I am a free user of GitHub, so I can use 2,000 min for GitHub Actions. If we use macOS, it counts 10 times of the usage time than the Linux server. one iOS app takes 30 min to deploy, so it counts 300 min for one deployment. So we can deploy 8 times per month for free. Android takes 10 min to deploy and it is executed on Linux, so it's not a problem. If you already use other GitHub Actions, take care about this time limit.

Now, try to deploy the app via GitHub Actions for saving the time!
