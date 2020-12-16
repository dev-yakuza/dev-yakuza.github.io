---
layout: 'post'
permalink: '/react-native/fastlane/'
paginate_path: '/react-native/:num/fastlane/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'Fastlaneを使ってアプリのデプロイを自動化する'
description: 'Fastlaneを使ってReact nativeで作ったアプリをを自動でデプロイしてみましょう。'
image: '/assets/images/category/react-native/2020/fastlane/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

1. [概要](#概要)
1. [Fastlane](#fastlane)
1. [インストール](#インストール)
1. [iOS](#ios)
    - [iOSのためFastlaneの初期化](#iosのためfastlaneの初期化)
    - [iOS用Fastlaneフォルダやファイル](#ios用fastlaneフォルダやファイル)
    - [iOS用実行ファイル修正](#ios用実行ファイル修正)
    - [iOS用fastlaneを実行](#ios用fastlaneを実行)
1. [アンドロイド](#アンドロイド)
    - [API accessのためService Account生成](#api-accessのためservice-account生成)
    - [アンドロイドのためFastlane初期化](#アンドロイドのためfastlane初期化)
    - [アンドロイド用のFastlaneフォルダやファイル](#アンドロイド用のfastlaneフォルダやファイル)
    - [アンドロイド用実行ファイル修正](#アンドロイド用実行ファイル修正)
    - [アンドロイドのfastlane実行](#アンドロイドのfastlane実行)
1. [package.json](#packagejson)
1. [gitignore](#gitignore)
1. [完了](#完了)

</div>

## 概要

React Nativeを使って趣味でアプリを開発していますが、アプリがどんどん多くなってアプリをアップデートする時、結構な時間が掛かってしまいました。

- 趣味で作ったアプリリスト: [App List]({{site.url}}/app/list){:target="_blank"}

それでReact Nativeで作ったアプリを自動で配布する方法を探して、`Fastlane`と言うツールを見つけました。

- 公式サイト: [Fastlane](https://docs.fastlane.tools/){:rel="nofollow noreferrer" target="_blank"}

このブログポストは`Fastlane`を使ってReact Nativeで開発したアプリのデプロイを自動化する方法について説明します。 (React Nativeで作ったアプリ以外にもネーティブで作ったアプリも使うことができますので、ネーティブで開発した方もご参考してください。)

もしReact Nativeのデプロイについて良く知らない方は以前のブログを参考してください。

- iOS
  - [iOSビルドやテスト]({{site.url}}/{{page.categories}}/ios-running-on-device/){:target="_blank"}
  - [iOSデバイステスト]({{site.url}}/{{page.categories}}/ios-test-on-device/){:target="_blank"}
  - [iOS開発者登録]({{site.url}}/{{page.categories}}/ios-enroll-developer-program/){:target="_blank"}
  - [iOS証明書(Certification)]({{site.url}}/{{page.categories}}/ios-certification/){:target="_blank"}
  - [iOS TestFlight]({{site.url}}/{{page.categories}}/ios-testflight/){:target="_blank"}
  - [iOS App store 登録]({{site.url}}/{{page.categories}}/ios-app-store/){:target="_blank"}
- Android
  - [アンドロイドデバイステスト]({{site.url}}/{{page.categories}}/android-test-on-device/){:target="_blank"}
  - [アンドロイドビルドやテスト]({{site.url}}/{{page.categories}}/android-running-on-device/){:target="_blank"}
  - [アンドロイド開発者登録]({{site.url}}/{{page.categories}}/android-enroll-google-play-developer/){:target="_blank"}
  - [アンドロイドアプリストア登録]({{site.url}}/{{page.categories}}/android-google-play/){:target="_blank"}

## Fastlane

> fastlane is the easiest way to automate beta deployments and releases for your iOS and Android apps. It handles all tedious tasks, like generating screenshots, dealing with code signing, and releasing your application.

FastlaneはiOSとアンドロイドのテスト用やリリース用のデプロイを簡単に自動化してくれるツールです。デプロイ以外にも、スクリンショット、コードサイニング、アプリストアーの情報などを生成、管理することもできます。

このブログではスクリンショット、アプリストアー登録情報などは既に登録したと思って、テスト用/リリース用のデプロイを自動化する部分だけ説明する予定です。

スクリンショット、アプリストアー登録情報の生成など、他の機能を使ってみたい方は公式サイトを参考してください。

- 公式サイト: [Fastlane](https://docs.fastlane.tools/){:rel="nofollow noreferrer" target="_blank"}

{% include in-feed-ads.html %}

## インストール

下記のコマンドで`Fastlane`をインストールすることができます。

```bash
# Using RubyGems
sudo gem install fastlane -NV

# Alternatively using Homebrew
brew cask install fastlane
```

公式サイトでは`Homebrew`を使ってインストールする方法と`RubyGems`を使ってインストールする方法を案内しています。

私は最初はHomebrewを使ってインストールして、テストしましたが、上手く行かない部分がありました。したがって、RubyGemsを使ってインストールすることをおすすめします。もし、Homebrewで上手く行かない方はRubyGemsで再インストールして試してみてください。

## iOS

React Nativeで開発したアプリをFastlaneを使ってiOSのデプロイを自動化してみます。

### iOSのためFastlaneの初期化

下記のコマンドを使ってiOSのため、Fastlaneを初期化します。

```bash
cd ios
fastlane init
```

上のコマンドを実行すると下記の画面が見えます。

![Fastlaneを使ってReact Nativeアプリ自動配布 - iOSの初期化](/assets/images/category/react-native/2020/fastlane/init-ios.jpg)

基本設定をするためTestflight用のデプロイ設定である`2`やアプリストアへのデプロイ設定である`3`を選択します。

```bash
2. Automate beta distribution to TestFlight
3. Automate App Store distribution
```

ここではTestflight用のデプロイ設定である`2`を選んで進めます。

![Fastlaneを使ってReact Nativeアプリ自動配布 - iOSのプロジェクト選択](/assets/images/category/react-native/2020/fastlane/select-ios-project.jpg)

2を選択して進めると上のようにiOSのプロジェクトを選択する画面が確認できます。tvアプリを開発していない場合`2`を選択してReact NativeのiOSアプリプロジェクトを選べます。

![Fastlaneを使ってReact Nativeアプリ自動配布 - Appleログイン](/assets/images/category/react-native/2020/fastlane/login-apple.jpg)

React NativeのiOSプロジェクトを選択したら、上のようにAppleログインをする画面がでます。iOSのアプリ配布のため使ってるApple store connectのログインIDを入力します。

![Fastlaneを使ってReact Nativeアプリ自動配布 - iOS設定](/assets/images/category/react-native/2020/fastlane/enter-ios.jpg)

私はすでにFastlaneを使ってログインしたことがあるので、上のような画面が確認できます。最初Fastlaneを設定する方は二重認証の手続きが出るので、その手続き通りやってください。

上のような画面以外にも何回も`Continue by pressing Enter`を入力する画面がでます。Enterキーを押して進めて設定を完了します。

{% include in-feed-ads.html %}

### iOS用Fastlaneフォルダやファイル

iOSの設定を完了したらReact Naitveのiosフォルダ下へ下記のようなフォルダやファイルが生成されることが確認できます。

```bash
|- fastlane
|  |- Appfile
|  |- Fastfile
|- Gemfile
|- Gemfile.lock
```

各フォルダやファイルを詳しくみてみましょう。

- fastlane フォルダ: fastlaneの設定ファイルや実行ファイルが入っているフォルダ
- Gemfile, Gemfile.lock: fastlaneはRubyでできてるのでfastlaneを実行するためのライブラリインストールファイルです。

fastlanewお実行するための設定内容が入ってる`fastlane/Appfile`ファイルのコメントアウトを消して見ると下記のようです。

```ruby
app_identifier("io.github.dev-yakuza.kumoncho")
apple_id("dev.yakuza@gmail.com")

itc_team_id("119423059")
team_id("WFDJCJXQZ6")
```

AppfileはiOSの自動配布のためfastlaneの設定ファイルです。簡単なファイルですので、詳しく説明は省略します。

その次は実際アプリをデプロイする時、実行するファイルである`fastlane/Fastfile`ファイルをコメントアウトを消して見ると下記のようです。

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

下記のコマンドで上のfastlaneを実行することができます。

```bash
# cd ios
fastlane beta
```

上のようにfastlaneを実行するとiOSのbuild numberを上げて(`increment_build_number`)、アプリをビルドして(`build_app`)、Testflight用でアップロードします。(`upload_to_testflight`)

{% include in-feed-ads.html %}

### iOS用実行ファイル修正

基本でき提供するfastlaneファイルでは完璧に自動化ができません。したがってiOS用のデプロイ自動化のため`fastlane/Fastfile`を下記のように修正します。

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

追加した内容を見ると下記のようです。

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

ユーザーが入力したバージョンに合わせて、バージョンを修正する関数を定義しました。

```ruby
lane :beta do |options|
  cert
  sigh(force: true)
  updateVersion(options)
  ...
```

fastlaneのコマンドで実行する時、パラメーターを使うため`|options|`を追加して、該当optionを新しく定義した関数のパラメーターへ入れました。このように新しく追加したスクリプトを使うためには下記のようなコマンドを実行します。

```bash
# fastlane beta version:1.0.0
# fastlane beta version:major
# fastlane beta version:minor
fastlane beta version:patch
```

もし、パラメーターを入力しなかった場合、ユーザーの入力を待てるようにしました。

```ruby
def updateVersion(options)
  if options[:version]
    version = options[:version]
  else
    version = prompt(text: "Enter the version type or specific version\n(major, minor, patch or 1.0.0): ")
  end
...
```

また、`cert`を使って証明書を持ってくるように設定して、`sigh(force: true)`を使ってProvisioning profileと連携するようにしました。

今まではTestflight用でアップロードする方法について説明しました。実際デプロイのため下記のような内容を追加します。

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

アプリをビルドするところまではTestflight用と同じです。ビルドされたアプリをアプリストアーへ配布するために下記のような内容を追加しました。

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

- force: fastlaneが生成するHTML reportを生成されないようにします。(true)
- reject_if_possible: アプリ審査を待ってるバージョンがある時、その審査をキャンセルします。(true)
- skip_metadata: アプリストアの情報を登録するかを設定します。自動配布する時、バージョンの修正内容を作成する必要があるので、この情報を登録できるように設定します。(false)
- skip_screenshots: 私は既に配布されたアプリについて自動配布を適用しています。したがって、スクリンショットを再アップロードする必要がありません。(true)
- languages: 現在ストアへ登録されたアプリのローカライゼーションを設定します。使える言語は `ar-SA, ca, cs, da, de-DE, el, en-AU, en-CA, en-GB, en-US, es-ES, es-MX, fi, fr-CA, fr-FR, he, hi, hr, hu, id, it, ja, ko, ms, nl-NL, no, pl, pt-BR, pt-PT, ro, ru, sk, sv, th, tr, uk, vi, zh-Hans, zh-Hant`で、詳しく内容は公式サイトを参考してください。([公式サイト](https://docs.fastlane.tools/actions/upload_to_app_store/#available-language-codes){:rel="nofollow noreferrer" target="_blank"})
- release_notes: iOSはアプリを再配布する時、Release notesを必ず作成します。私が使ってるスクリプトは3国語を提供してるアプリなので、defaultと와 3国語に該当するRelease notesを作成しました。
- submit_for_review: アプリ審査へ提出するようにします。(true)
- automatic_release: 審査が終わったらアプリを自動でデプロイするように設定します。これを設定しないとアプリ審査が終わった後、開発者が手動でデプロイする必要があります。(true)
- submission_information: デプロイ前、暗号化や広告が含まれたかをチェックするオプションです。

これ意外にもたくさんのオプションがあります。詳しく内容は公式サイトを参考してください。

- 公式サイト: [https://docs.fastlane.tools/actions/upload_to_app_store/](https://docs.fastlane.tools/actions/upload_to_app_store/){:rel="nofollow noreferrer" target="_blank"}
- 例題: [submission_information](https://github.com/artsy/eigen/blob/faa02e2746194d8d7c11899474de9c517435eca4/fastlane/Fastfile#L131-L149){:rel="nofollow noreferrer" target="_blank"}

{% include in-feed-ads.html %}

### iOS用fastlaneを実行

これでfastlaneを使ってiOSへの自動デプロイ準備は終わりました。これからfastlaneを使ってアプリを自動デプロイしてみます。

下記のコマンドを使ってReact Nativeで作ったアプリをTestflightへデプロイしてみます。

```bash
# cd ios
fastlane beta version:patch
```

デプロイが終わるまで、結構な時間がかかります。デプロイが終わったら下記のような画面が確認できます。

![Fastlaneを使ってReact Nativeのアプリを自動配布 - iOS Testflightデプロイ](/assets/images/category/react-native/2020/fastlane/ios-testflight.jpg)

もちろん、App store connectのTestflightへも上手くデプロイされたことが確認できます。

じゃ、今回は下記のコマンド使って実際デプロイしてみましょう。

```bash
# cd ios
fastlane release version:patch
```

デプロイが終わったら下記のような画面が確認できます。

![Fastlaneを使ってReact Nativeアプリ自動配布 - iOSアプリデプロイ](/assets/images/category/react-native/2020/fastlane/ios-upload-app-store.jpg)

また、App store connectにも上手くデプロイが出来たことが確認出来ます。

{% include in-feed-ads.html %}

## アンドロイド

今回はReact Nativeで開発したアンドロイドアプリをFastlaneを使ってアンドロイドのデプロイを自動化してみます。

### API accessのためService Account生成

Fastlaneを使ってアンドロイドをデプロイする時、グーグルのAPIを使うため、`Google Developer Service Account`を生成する必要があります。

Google Developer Service Accountを生成するため、下記のリンクを使ってグーグルコンソール(Google Play Console)に行きます。

- グーグルプレイコンソール: [https://play.google.com/apps/publish/](https://play.google.com/apps/publish/){:rel="nofollow noreferrer" target="_blank"}

グーグルプレイコンソールに移動したら、下記の画面が確認できます。

![Fastlaneを使ってReact Nativeのアプリを自動配布 - グーグルプレイコンソール](/assets/images/category/react-native/2020/fastlane/google-play-console.jpg)

左メニューの`Settings`を選択します。そして`Developer account`下にある`API access`メニューを選択します。

![Fastlaneを使ってReact Nativeのアプリを自動配布 - グーグルプレイコンソールapi accessメニュー](/assets/images/category/react-native/2020/fastlane/android-api-access.jpg)

上のような画面が見えたら、`CREATE NEW PROJECT`ボタンを押して、新しプロジェクトを生成します。

![Fastlaneを使ってReact Nativeのアプリを自動配布 - グーグルプレイコンソールapi access, service account](/assets/images/category/react-native/2020/fastlane/android-api-access-service-account.jpg)

新しプロジェクトが生成されると、上のような画面が確認できます。下にある`CREATE SERVICE ACCOUNT`ボタンを選択したら、下記のような画面が確認できます。

![Fastlaneを使ってReact Nativeのアプリを自動配布 - グーグルプレイコンソールapi access, how to create service account](/assets/images/category/react-native/2020/fastlane/android-api-access-how-to-create-service-account.jpg)

上のような画面で`Google API Console`リンクを選択します。選択したら、下記のような画面が確認できます。

![Fastlaneを使ってReact Nativeのアプリを自動配布 - Google API Console](/assets/images/category/react-native/2020/fastlane/android-google-api-console.jpg)

上にある`CREATE SERVICE ACCOUNT`ボタンを選択します。選択したら、下記のように新しService accountを生成する画面が確認できます。

![Fastlaneを使ってReact Nativeのアプリを自動配布 - Google API Console, service account生成](/assets/images/category/react-native/2020/fastlane/android-google-api-console-create-service-account.jpg)

上のような画面で、`Service account name`へ名前を入力して、`CREATE`ボタンを押してService accountを生成します。(私はService account nameへgoogle-play-fastlane-deploymentを入力しました。)

![Fastlaneを使ってReact Nativeのアプリを自動配布 - Google API Console, service account役割設定](/assets/images/category/react-native/2020/fastlane/android-google-api-console-service-account-role.jpg)

上のような画面が見えたら、`Role`を選択して`Service Account User`を検索して選択します。RoleにService Account Userを設定したら、下にある`CONTINUE`ボタンを押して進めます。

![Fastlaneを使ってReact Nativeのアプリを自動配布 - Google API Console, service accountキー生成](/assets/images/category/react-native/2020/fastlane/android-google-api-console-service-account-create-key.jpg)

上のような画面が見えたら、下にある`CREATE KEY`を選択して`JSON`が選択された状態で`CREATE`を押してキーを生成します。

![Fastlaneを使ってReact Nativeのアプリを自動配布 - Google API Console, service account JSONキー生成](/assets/images/category/react-native/2020/fastlane/android-google-api-console-service-account-create-json-key.jpg)

CREATEボタンを押してキーを生成したら、JSON形式のファイルが自動でダウンロードされます。このファイルをReact Nativeプロジェクトの`android`フォルダー下にコピーします。最後に`DONE`ボタンを押してService Accountを生成します。

そして現在画面へ戻って、右下にある`DONE`ボタンを押してService Account生成を終了します。

![Fastlaneを使ってReact Nativeのアプリを自動配布 - グーグルプレイコンソールapi access, how to create service account](/assets/images/category/react-native/2020/fastlane/android-api-access-how-to-create-service-account.jpg)

そしたら以前と違って下記のような画面が確認できます。

![Fastlaneを使ってReact Nativeのアプリを自動配布 - グーグルプレイコンソールService Account生成完了](/assets/images/category/react-native/2020/fastlane/android-finish-to-create-service-account.jpg)

そしたら、権限を設定するため、右下の`GRANT ACCESS`ボタンを選択します。

![Fastlaneを使ってReact Nativeのアプリを自動配布 - グーグルプレイコンソールService Account権限設定](/assets/images/category/react-native/2020/fastlane/android-service-account-grant-access.jpg)

上の画面が表示されたら、スクロールして`ADD USER`を選択してユーザーを登録します。

{% include in-feed-ads.html %}

### アンドロイドのためFastlane初期化

今からアンドロイド用のFastlaneを生成してみましょう。下記のコマンドを使ってアンドロイド用のFastlaneを生成します。

```bash
cd android
fastlane init
```

上のコマンドを実行すると下記のような画面が確認できます。

![Fastlaneを使ってReact Nativeのアプリを自動配布 - アンドロイド初期化: package name](/assets/images/category/react-native/2020/fastlane/android-package-name.jpg)

アンドロイドプロジェクトの`Package Name`を入力します。(ex> io.github.dev.yakuza.kumoncho)そしたら、下記のようにJSONファイルのpathを入力する画面が確認できます。

![Fastlaneを使ってReact Nativeのアプリを自動配布 - アンドロイド初期化: JSON path](/assets/images/category/react-native/2020/fastlane/android-json-path.jpg)

Service Accountを生成した時、ダウンロードしたJSONファイルを`android`フォルダーへコピーしました。このファイルのpathを指定します。(ex> `app-xxx.json`)

![Fastlaneを使ってReact Nativeのアプリを自動配布 - アンドロイド初期化:ダウンロードmetadata](/assets/images/category/react-native/2020/fastlane/android-download-metadata.jpg)

次はアンドロイドをデプロイする時、登録したストアー情報(metadata)をダウンロードするかどうか設定します。私は既にデプロイしたアプリを自動化してるのでストアー情報を更新する必要がありません。したがって、nを入力してストアー情報をダウンロードしないようにしました。

上のような画面以外にも何回にも`Continue by pressing Enter`を入力する画面がでます。Enterキーを押して進めて設定を完了します。

{% include in-feed-ads.html %}

### アンドロイド用のFastlaneフォルダやファイル

アンドロイドの設定を完了したら、React Naitveのandroidフォルダ下へ下記のようなフォルダやファイルが生成されたことが確認できます。

```bash
|- fastlane
|  |- Appfile
|  |- Fastfile
|- Gemfile
|- Gemfile.lock
```

各フォルダやファイルを詳しく説明します。

- fastlaneフォルダ: fastlaneの設定や実行するファイルが入ってるフォルダ
- Gemfile, Gemfile.lock: fastlaneはRubyでできてるので、fastlaneを実行するためのライブラリのインストールファイルです。

fastlaneを実行する設定内容が入ってる`fastlane/Appfile`ファイルのコメントアウトを消して見ると下記のようです。

```ruby
json_key_file("api-xxx.json")
package_name("io.github.dev.yakuza.kumoncho")
```

私たちが設定したPacakge NameとJSONファイルのいちが設定されたことが確認できます。その次、実際アプリをデプロイする時実行されるファイルである`fastlane/Fastfile`ファイルのコメントアウトを消して見ると下記のようです。

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

iOSとは違って`beta`と`deploy`,2つのlaneが生成されることが確認できます。上のFastlaneももちろん下記のコマンドで実行することができます。

```bash
# cd android
fastlane beta
fastlane deploy
```

しかし、完璧な自動化をするため、Fastfileを修正する必要があります。

{% include in-feed-ads.html %}

### アンドロイド用実行ファイル修正

基本的提供されるfastlaneファイルでは完璧に自動化ができません。したがって、アンドロイド用のデプロイを自動化するため`fastlane/Fastfile`ファイルを下記のように修正します。

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

追加した内容を詳しく見ると下記のようです。

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

アンドロイドはiOSと違ってアプリのバージョンをアップデートする機能が提供されていません。(私が探せなかったかも知れないです。もし、分かる方はフィドバックお願いします。)したがって、アンドロイドのversionCodeとversionNameをアップデートする機能を実装しました。

```ruby
def updateVersion(options)
...
```

updateバージョンの部分はiOSで説明したので省略します。

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

アンドロイドはgradleのcleanとbundleReleaseでアプリをビルドするようにしました。(`assembleRelease`ではありません。)また、upload_to_play_storeの`track: 'internal'`を使ってinternal test用でデプロイするようにしました。

アンドロイドはiOSとは違ってRelease notes(change log)を作成する必要がありません。だから、ストアーと関係ある全ての機能はskipするように設定しました。

最後にbundleReleaseをを使ってaabファイルを生成してアップロードする予定なので、skip_upload_apkをtrueで設定しました。

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

グーグルプレイにデプロイするスクリプトです。iOSと同じようにするため`lane :deploy`を`lane :release`で変更しました。

upload_to_play_storeのtrackパレメーターが無いこと以外はbeta用と同じなので詳しく説明は省略します。

{% include in-feed-ads.html %}

### アンドロイドのfastlane実行

fastlaneを使ってアンドロイドを自動デプロイする準備が終わりました。今からfastlaneを使ってアプリを自動デプロイしてみます。

下記のコマンドを使ってReact Nativeで作成したアプリをinternal testへデプロイしてみます。

```bash
# cd android
fastlane beta version:patch
```

デプロイが終わるまで、結構な時間がかかります。デプロイが終わったら下記のような画面が確認できます。

![Fastlaneを使ってReact Nativeのアプリを自動配布 - アンドロイドinternal testデプロイ](/assets/images/category/react-native/2020/fastlane/android-fastlane-beta.jpg)

もちろんPlay store consoleでもinternal testへ上手くデプロイされたことが確認できます。

じゃ、今から下記のコマンドを使って実際デプロイをやってみます。

```bash
# cd android
fastlane release version:patch
```

デプロイが完了されたら、下記のような画面が確認できます。

![Fastlaneを使ってReact Nativeのアプリを自動配布 - アンドロイドアプリストアーデプロイ](/assets/images/category/react-native/2020/fastlane/android-fastlane-release.jpg)

また、グーグルプレイストアにも上手くデプロイされたことが確認できます。

{% include in-feed-ads.html %}

## package.json

私はこのように作ったfastlaneを実行するコマンドを下記のようにpackage.jsonへ作成して使っています。

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

fastlaneを使ってデプロイすると、それによるファイルだちが生成されます。gitで管理しないようにするため`.gitignore`ファイルへ下記の内容を追加します。

```bash
...
# fastlane
ios/*.mobileprovision
ios/*.cer
ios/*.dSYM.zip
android/fastlane/README.md
ios/fastlane/README.md
```

## 完了

これでfastlaneを使ってReact Nativeを作成したアプリを自動デプロイする方法についてみてみました。このブログで説明した内容はもちろんNativeで開発したアプリでも活用できるので、たくさんの方にやくにたてらいいかと思います。

このfastlaneを導入して時間を節約できたし、楽になって嬉しいです。皆さんもぜひ使ってみてください。
