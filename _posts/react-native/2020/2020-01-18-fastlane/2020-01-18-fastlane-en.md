---
layout: 'post'
permalink: '/react-native/fastlane/'
paginate_path: '/react-native/:num/fastlane/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'Deploy automatically applications via Fastlane'
description: Let's see how to deploy automatically React Native application via Fastlane
image: '/assets/images/category/react-native/2020/fastlane/background.jpg'
---

<div id="contents_list" markdown="1">

## Content

1. [Outline](#outline)
1. [Fastlane](#fastlane)
1. [Installation](#installation)
1. [iOS](#ios)
    - [Initialization of Faslane for iOS](#initialization-of-faslane-for-ios)
    - [iOS Fastlane folders and files](#ios-fastlane-folders-and-files)
    - [Modify the executing file for iOS](#modify-the-executing-file-for-ios)
    - [Excute iOS Fastlane](#excute-ios-fastlane)
1. [Android](#android)
    - [Create Service Account for API access](#create-service-account-for-api-access)
    - [Initialization of Faslane for Android](#initialization-of-faslane-for-android)
    - [Android Fastlane folders and files](#android-fastlane-folders-and-files)
    - [Modify the executing file for Android](#modify-the-executing-file-for-android)
    - [Execute Android Fastlane](#execute-android-fastlane)
1. [package.json](#packagejson)
1. [gitignore](#gitignore)
1. [Completed](#completed)

</div>

## Outline

My hobby is developing applications with React Native, so I have many applications and take much time when I deploy the applications.

- My hobby application list: [App List]({{site.url}}/app/list/en){:target="_blank"}

So, I searched about how to deploy automatically the applications and finally, I found `Fastlane` tool.

- Official site: [Fastlane](https://docs.fastlane.tools/){:rel="nofollow noreferrer" target="_blank"}

In this blog post, you can see how to deploy automatically an application, which is developed by React Native, via `Fastlane` (Not only React Native apps but also Native app can be deployed, so If you're Native application developer, it's also helpful.)

If you don't know details about React Native deployment, see the previous blog posts.

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

## Fastlane

> fastlane is the easiest way to automate beta deployments and releases for your iOS and Android apps. It handles all tedious tasks, like generating screenshots, dealing with code signing, and releasing your application.

You can simply make automatically deployment scripts of test and release for iOS and Android. Not only deployment but also screenshots, code signing and app store info can be changed via Fastlane.

This blog post will only cover the beta/release deployment part not include screenshots and app store info.

If you want to know how to make screenshots and register app store info, see the official stie.

- Official site: [Fastlane](https://docs.fastlane.tools/){:rel="nofollow noreferrer" target="_blank"}

{% include in-feed-ads.html %}

## Installation

You can install `Fastlane` via executing the command below.

```bash
# Using RubyGems
sudo gem install fastlane -NV

# Alternatively using Homebrew
brew cask install fastlane
```

The official site introduces the installation via `Homebrew` and `RubyGems`.

In my case, I installed via Homebrew and tested it, but not working well. So, I re-installed via RubyGems and working well. Therefore, I recommend you to install via RubyGems. If you try to install via Homebrew and not working well, try to re-install via RubyGems.

## iOS

Let's make automatic deployment of the application developed by React Native via Fastlane

### Initialization of Faslane for iOS

execute the command below to initialize Fastlane for iOS.

```bash
cd ios
fastlane init
```

After executing, you can see the screen like below.

![deploy automatically React Native app via Fastlane - iOS initialization](/assets/images/category/react-native/2020/fastlane/init-ios.jpg)

You can simply select `2` for Testflight deployment and `3` for App store deployment.

```bash
2. Automate beta distribution to TestFlight
3. Automate App Store distribution
```

In here, I selected `2`.

![deploy automatically React Native app via Fastlane - select iOS project](/assets/images/category/react-native/2020/fastlane/select-ios-project.jpg)

After selecting 2, you can see the screen like below to select iOS project. If you don't develop TV app, select `2` for React Native iOS project.

![deploy automatically React Native app via Fastlane - Apple login](/assets/images/category/react-native/2020/fastlane/login-apple.jpg)

After selecting React Native iOS project, you can see the Apple login screen like above. Insert your login ID when you login Apple store connect.

![deploy automatically React Native app via Fastlane - iOS setting](/assets/images/category/react-native/2020/fastlane/enter-ios.jpg)

In my case, I've already logged in, so I can see the screen like above. If you login at the first time, you can see Two-factor authentication process. Just follow instructions to finish it.

After it, you can see `Continue by pressing Enter` on the screen many times. Press Enter key to finish the configuration.

{% include in-feed-ads.html %}

### iOS Fastlane folders and files

After the configuration, you can see the folders and files in React Native ios folder like below.

```bash
|- fastlane
|  |- Appfile
|  |- Fastfile
|- Gemfile
|- Gemfile.lock
```

Let's see the details about them.

- fastlane folder: the folder includes Fastlane configuration file and executing file.
- Gemfile, Gemfile.lock: Fastlane is made of Ruby. These files are the library installation files for executing Fastlane.

The `fastlane/Appfile` file is the configuration file to execute Fastlane. You can see the contents like below after removing the comment out.

```ruby
app_identifier("io.github.dev-yakuza.kumoncho")
apple_id("dev.yakuza@gmail.com")

itc_team_id("119423059")
team_id("WFDJCJXQZ6")
```

Appfile is the Fastlane configuration file for iOS depoyment. this is a very simple file, so I just skip to introduce this file.

The `fastlane/Fastfile` file is the executing file for deploying the app. After removing the comment out, you can see the contents like below.

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

You can execute the file via the command below.

```bash
# cd ios
fastlane beta
```

If you execute the command like above to execute Fastlane, Fastlane will update iOS app build number(`increment_build_number`), build the app(`build_app`) and upload it to Testflight(`upload_to_testflight`).

{% include in-feed-ads.html %}

### Modify the executing file for iOS

We can not automatically deploy perfectly the app by the basically provided file. so, modify `fastlane/Fastfile` like below.

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

Let's see the details about it.

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

I defined the function that makes the user insert the app version.

```ruby
lane :beta do |options|
  cert
  sigh(force: true)
  updateVersion(options)
  ...
```

Added `|options|` to get the parameters when the user executes the command and send it to the function we defined above.

You can execute the new script to execute the command like below.

```bash
# fastlane beta version:1.0.0
# fastlane beta version:major
# fastlane beta version:minor
fastlane beta version:patch
```

If you don't insert the version, the script will wait for user input.

```ruby
def updateVersion(options)
  if options[:version]
    version = options[:version]
  else
    version = prompt(text: "Enter the version type or specific version\n(major, minor, patch or 1.0.0): ")
  end
...
```

Also, I used `cert` to get the certification and `sigh(force: true)` to connect the provisioning profile.

Until now, we talked about Testflight deployment. Let's see the details about the release deployment.

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

It's the same until the build app that we've seen in Testflight script. I added the script below to upload the built app to App store.

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

- force: make Fastlane not to generate HTML report(true)
- reject_if_possible: if the app is already waiting for the review and not reviewing yet, cancel it(true)
- skip_metadata: skip modifying App store info(metadata). We need to insert the release note, so we need to set it modifiable(false)
- skip_screenshots: I already have the deployed app and make an automatic deployment script for it, so I don't need to upload the screenshots.(true)
- languages: the localization of the app store info. You can use the languages like `ar-SA, ca, cs, da, de-DE, el, en-AU, en-CA, en-GB, en-US, es-ES, es-MX, fi, fr-CA, fr-FR, he, hi, hr, hu, id, it, ja, ko, ms, nl-NL, no, pl, pt-BR, pt-PT, ro, ru, sk, sv, th, tr, uk, vi, zh-Hans, zh-Hant`. you can see more details on the offical site.([official site](https://docs.fastlane.tools/actions/upload_to_app_store/#available-language-codes){:rel="nofollow noreferrer" target="_blank"})
- release_notes: we must insert Release notes when we deploy iOS app. My app store localized by 3 languages, so the Release notes includes the default and 3 languages.
- submit_for_review: submit the app for review.(true)
- automatic_release: After reviewing, deploy automatically. If you don't set this value, after reviewing, the developer will deploy manually it via the app store connect.(true)
- submission_information: it's the answer to the encryption and advertising questions.

There are many options. You can see other options in the official site.

- Officail stie: [https://docs.fastlane.tools/actions/upload_to_app_store/](https://docs.fastlane.tools/actions/upload_to_app_store/){:rel="nofollow noreferrer" target="_blank"}
- Exmaple: [submission_information](https://github.com/artsy/eigen/blob/faa02e2746194d8d7c11899474de9c517435eca4/fastlane/Fastfile#L131-L149){:rel="nofollow noreferrer" target="_blank"}

{% include in-feed-ads.html %}

### Excute iOS Fastlane

We're ready to deploy iOS via Fastlane. Let's deploy automatically the app via Fastlane.

Execute the command below to deploy the React Native app to Testflight.

```bash
# cd ios
fastlane beta version:patch
```

It takes a long time to finish the deployment. After deploying, you can see the screen like below.

![deploy automatically React Native app via Fastlane - iOS Testflight deployment](/assets/images/category/react-native/2020/fastlane/ios-testflight.jpg)

Of course, you can see the deployed well to Testflight on the App store connect.

Let's execute the command below to deploy to App store.

```bash
# cd ios
fastlane release version:patch
```

You can see the screen like below after deploying.

![deploy automatically React Native app via Fastlane - iOS app deployment](/assets/images/category/react-native/2020/fastlane/ios-upload-app-store.jpg)

Also, you can see the deployed well on App store connect.

{% include in-feed-ads.html %}

## Android

Let's make Fastlane deploy automatically the React Native Android app.

### Create Service Account for API access

When we deploy Android app via Fastlane, Fastlane uses Google API, so we need to create `Google Developer Service Account`.

For createing Google Developer Service Account, click the link below to go to Google Play Console.

- Google Play Console: [https://play.google.com/apps/publish/](https://play.google.com/apps/publish/){:rel="nofollow noreferrer" target="_blank"}

You can see the screen like below when you go to Google Play Console.

![deploy automatically React Native app via Fastlane - Google Play Console](/assets/images/category/react-native/2020/fastlane/google-play-console.jpg)

Select `Settings` menu on the left. And then, select `API access` menu under `Developer account`.

![deploy automatically React Native app via Fastlane - Google Play Console api access menu](/assets/images/category/react-native/2020/fastlane/android-api-access.jpg)

If you can see the screen like above, click `CREATE NEW PROJECT` button to create new project.

![deploy automatically React Native app via Fastlane - Google Play Console api access, service account](/assets/images/category/react-native/2020/fastlane/android-api-access-service-account.jpg)

After creating new project, you can see the screen like above. When you click `CREATE SERVICE ACCOUNT` button on the bottom, you can see the screen like below.

![deploy automatically React Native app via Fastlane - Google Play Console api access, how to create service account](/assets/images/category/react-native/2020/fastlane/android-api-access-how-to-create-service-account.jpg)

Click `Google API Console` link on the screen above. After it, you can see the screen like below.

![deploy automatically React Native app via Fastlane - Google API Console](/assets/images/category/react-native/2020/fastlane/android-google-api-console.jpg)

Click `CREATE SERVICE ACCOUNT` button on the top. After selecting, you can see the screen of createing Service account like below.

![deploy automatically React Native app via Fastlane - Google API Console, create service account](/assets/images/category/react-native/2020/fastlane/android-google-api-console-create-service-account.jpg)

on the screen above, insert `Service account name` and click `CREATE` button to create Service account.(In my case, I inserted google-play-fastlane-deployment to Service account name)

![deploy automatically React Native app via Fastlane - Google API Console, set service account role](/assets/images/category/react-native/2020/fastlane/android-google-api-console-service-account-role.jpg)

When you see the screen above, click `Role` and search `Service Account User`. After setting Service Account User to Role, click `CONTINUE` button.

![deploy automatically React Native app via Fastlane - Google API Console, create service account key](/assets/images/category/react-native/2020/fastlane/android-google-api-console-service-account-create-key.jpg)

If you see the screen like above, click `CREATE KEY` on the bottom. check `JSON` and click `CREATE` button to create the key.

![deploy automatically React Native app via Fastlane - Google API Console, create service account JSON key](/assets/images/category/react-native/2020/fastlane/android-google-api-console-service-account-create-json-key.jpg)

After clicking CREATE button to create the ky, JSON file is donwloaded automatically. Copy this file to React Native project `android` folder. And then, click `DONE` button to create Service Account.

And then, come back to the original screen, and clcik `DONE` button on the right bottom to finish to create Service Account.

![deploy automatically React Native app via Fastlane - Google Play Console api access, how to create service account](/assets/images/category/react-native/2020/fastlane/android-api-access-how-to-create-service-account.jpg)

After it, you can see the different screen like below.

![deploy automatically React Native app via Fastlane - Google Play Console completed to create Service Account](/assets/images/category/react-native/2020/fastlane/android-finish-to-create-service-account.jpg)

Click `GRANT ACCESS` button on the right bottom for granting permissions.

![deploy automatically React Native app via Fastlane - Google Play Console Service Account permission setting](/assets/images/category/react-native/2020/fastlane/android-service-account-grant-access.jpg)

On the screen liek above, scroll to the bottom and select `ADD USER` to register the user.

{% include in-feed-ads.html %}

### Initialization of Faslane for Android

Let's create Fastlane for Android. Execute the command below to create Fastlane for Android.

```bash
cd android
fastlane init
```

After executing, you can see the screen like below.

![deploy automatically React Native app via Fastlane - initialization of Android fastlnae: package name](/assets/images/category/react-native/2020/fastlane/android-package-name.jpg)

Insert `Pacakage Name` of Android project.(ex> io.github.dev.yakuza.kumoncho) After then, you can see the JSON file path screen like below.

![deploy automatically React Native app via Fastlane - initialization of Android fastlnae: JSON path](/assets/images/category/react-native/2020/fastlane/android-json-path.jpg)

we downloaded JSON file and copied it to `android` folder when we created Service Account. insert this file path.(ex> `app-xxx.json`)

![deploy automatically React Native app via Fastlane - initialization of Android fastlnae: download metadata](/assets/images/category/react-native/2020/fastlane/android-download-metadata.jpg)

Next, Fastlane asks you to download Store info(metadata). I have already the deployed app and just make automatic deployment, so I don't need to update Store info. Therefore, insert `n` to skip downloading the store info.

After it, you can see the `Continue by pressing Enter` screen many times. Just press Enter key to complete the configuration.

{% include in-feed-ads.html %}

### Android Fastlane folders and files

After the configuration, you can see the folders and files in React Native android folder like below.

```bash
|- fastlane
|  |- Appfile
|  |- Fastfile
|- Gemfile
|- Gemfile.lock
```

Let's see the details about them.

- fastlane folder: the folder includes Fastlane configuration file and executing file.
- Gemfile, Gemfile.lock: Fastlane is made of Ruby. These files are the library installation files for executing Fastlane.

The `fastlane/Appfile` file is the configuration file to execute Fastlane. You can see the contents like below after removing the comment out.

```ruby
json_key_file("api-xxx.json")
package_name("io.github.dev.yakuza.kumoncho")
```

We can see the Package Name and JSON file path what we configured before.

The `fastlane/Fastfile` file is the executing file for deploying the app. After removing the comment out, you can see the contents like below.

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

we can see `beta` and `deploy`, two lanes different from iOS. Of course, you can execute Fastlane by executing the command below.

```bash
# cd android
fastlane beta
fastlane deploy
```

However, we need to modify Fastfile for the perfect automatic deployment.

{% include in-feed-ads.html %}

### Modify the executing file for Android

We can not automatically deploy perfectly the app by the basically provided file. so, modify `fastlane/Fastfile` like below.

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

Let's see the details about it.

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

Fastlane doesn't provide the update feature of the version unlike iOS.(Maybe I didn't find it. If you find or know it, please give me feedback.) So I implement the function to update Android versionCode and versionName.

```ruby
def updateVersion(options)
...
```

I already mentioned about updateVersion function on the iOS part, so I skip to explain it again.

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

use gradle clean and bundleRelease to build the app on Android.(it's not `assembleRelease`) Also, set `track: 'internal'` in upload_to_play_store to deploy the app to internal test.

We don't need to write Release notes(change log) on Android unlike iOS, so I set to skip all features.

Lastly, I'll make aab file via bundleRelease and upload it, so I set true to skip_upload_apk.

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

It's deployment script for Google Play store. To make same with iOS, modify `lane :deploy` to `lane :release`.

it's same with beta script except no track parameter in upload_to_play_store, so I skip to explain.

{% include in-feed-ads.html %}

### Execute Android Fastlane

We're ready to deploy Android via Fastlane. Let's deploy automatically the app via Fastlane.

Execute the command below to deploy the React Native app to internal test.

```bash
# cd android
fastlane beta version:patch
```

It takes a long time to finish the deployment. After deploying, you can see the screen like below.

![deploy automatically React Native app via Fastlane - Android internal test deployment](/assets/images/category/react-native/2020/fastlane/android-fastlane-beta.jpg)

Of course, you can see the deployed well to internal test on the Play store console

Let's execute the command below to deploy to release.

```bash
# cd android
fastlane release version:patch
```

You can see the screen like below after deploying.

![deploy automatically React Native app via Fastlane - Android app store release](/assets/images/category/react-native/2020/fastlane/android-fastlane-release.jpg)

Also, you can see the deployed well on Google Play store.

{% include in-feed-ads.html %}

## package.json

I make the scripts in package.json like below to use Fastlane what I made.

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

After deploying via Fastlane, some files are generated. Add the contents below to `.gitignore` not to manage them by git.

```bash
...
# fastlane
ios/*.mobileprovision
ios/*.cer
ios/*.dSYM.zip
android/fastlane/README.md
ios/fastlane/README.md
```

## Completed

We've seen about how to use Fastlane to deploy automatically React Native apps. You can use this blog post content for the Native app, too. So I hope this blog post helps many developers.

I can save wasted time and the deployment is simple! so I recommend you guys use Fastlane!
