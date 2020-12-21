---
layout: 'post'
permalink: '/react-native/github-actions-fastlane/'
paginate_path: '/react-native/:num/github-actions-fastlane/'
lang: 'ja'
categories: 'react-native'
comments: true

title: GitHub ActionsとFastlaneを使ってReact Nativeアプリをデプロイする
description: GitHub ActionsとFastlaneを使ってReact Nativeで開発したアプリを自動でデプロイする
image: '/assets/images/category/react-native/2020/github-actions-fastlane/background.jpg'
published: false
---

<div id="contents_list" markdown="1">

## 目次

</div>

## 概要

React Nativeを使って趣味でアプリを開発してますが、アプリがどんどん多くなってアプリをデプロイする時、時間がかかる問題が発生しました。

- 趣味で作ったアプリリスト: [App List]({{site.url}}/app/list/){:target="_blank"}

それでReact Nativeで作ったアプリを自動でデプロイする方法で`Fastlane`と言うツールを使ってデプロイしています。

- [Fastlaneを使ってアプリのデプロイを自動化する]({{site.url}}/{{page.categories}}/fastlane/){:target="_blank"}

しかし、ローカルマシンで`Fastlane`でアプリを一つデプロイするには30分ほどかかって、アプリが20個なので、ローカルでデプロイをするにも、時間がかかりすぎました。

それでこのようなデプロイを効率的するため、`GitHub Actions`を使ってデプロイシステムを考えてみました。

- [GitHub Actions](https://github.com/features/actions){:rel="nofollow noreferrer" target="_blank"}

このブログポストではGitHub ActionsとFastlaneを使ってデプロイする方法について説明します。

もし、React Nativeのデプロイに関してよく知らない方は以前のブログポストを参考してください。

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
- [Fastlaneを使ってアプリのデプロイを自動化する]({{site.url}}/{{page.categories}}/fastlane/){:target="_blank"}

{% include in-feed-ads.html %}

## Fastlane準備

まず、以前のブログを参考してFastlaneでデプロイする準備をします。

- [Fastlaneを使ってアプリのデプロイを自動化する]({{site.url}}/{{page.categories}}/fastlane/){:target="_blank"}

しかし、以前のブログポストで使ったFastlaneはすぐ使えないです。なぜなら、以前のFastlaneはアプリのバージョンを上げって、上ったバージョンをGitHubで管理をしなきゃならないですが、GitHub Actionsサーバで変更した内容をコミットして保存することが難しいです。

したがって、バージョンはローカルで上げって、GitHub Actionsを使ってサーバで単純にデプロイだけ実行するようにFastlaneを修正する必要があります。

### アンドロイドFastlane準備

アンドロイドのFastlaneは単純です。すでに認証キーを使ってデプロイをしてるので、特に設定することがありません。ただし、既存のFastlaneをバージョンを更新するFastlaneとGitHub Actionsで使うFastlaneで分ける必要があります。

- 既存のFastlane

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

- 追加したFastlane

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

既存のFastlaeはローカルでデプロイする場合もあるので、そのままにして、当該のFastlaneの機能を`version`と`github`というFastlaneを分けて追加しました。

GitHub Actionsを使う前にローカルでFastlaneの`version`を使ってバージョンを更新した後、GitHub Actionsでは`github`と言うFastlaneでアプリをデプロイする予定です。

{% include in-feed-ads.html %}

### iOS Fastlane準備

iOSでFastlaneは証明書、2FA認証など少し複雑です。

### Certificate

一旦、ローカルで使ってる証明書をサーバでも使えるようにする必要があります。`Keychain Access`を開いて現在使ってる証明書でマウス右クリックをして`Export`メニューを選択します。

![Export Certificate](/assets/images/category/react-native/2020/github-actions-fastlane/certificate.jpg)

メニューを選択してパスワードを入力する画面がでます。そのパスワードは後で、Fastlaneにも設定する必要があるので、覚えておきます。

このように保存したファイルをReact Nativeのプロジェクトの`ios`フォルダへコピーします。私は分かりやすくするため、ファイルの名前を`distribution.p12`に変更しました。

### Provisioning profile

サーバでiOSアプリをデプロイするためには`Provisioning profile`が必要です。Provisioning profileファイルをダウンロードするため、アップル開発サイトへ移動します。

- [https://developer.apple.com/account/resources/profiles/list](https://developer.apple.com/account/resources/profiles/list){:rel="nofollow noreferrer" target="_blank"}

そしてGitHub Actionsを使ってデプロイしようと思ってるアプリのProvisioning profileファイルをダウンロードします。

![Export Certificate](/assets/images/category/react-native/2020/github-actions-fastlane/provisioning_profile.jpg)

このように保存したファイルをReact Nativeプロジェクトの`ios`フォルダへコピーします。私は分かりやすくするためファイル名を`distribution.mobileprovision`にして保存しました。

{% include in-feed-ads.html %}

### Signing & Capabilities

GitHub Actionsを使ってアプリをデプロイするためダウンロードした`Provisioning profile`を設定して`Automatically manage signing`を解除する必要があります。`ios/[Your project name].xcworkspace`ファイルを実行してxcodeを実行します。

![signing and capabilities](/assets/images/category/react-native/2020/github-actions-fastlane/signing_and_capabilities.jpg)

そして`Signing & Capabilities`へ移動して、`Automatically manage signing`をアンチェックします。あと、上でダウンロードしたProvisioning profileファイルを設定するため`Provisioning Profile`の項目の横にあるドロップダウンメニューを押して`Import Profile...`を選択して上でダウンロードしたファイルを設定します。

### API key

Fastlaneでアプリをデプロイする時、アップルIDでログインして色んなことを実行します。しかし、アップル開発アカウントは`2FA`が設定されてサーバ(CI)を使ってデプロイする場合、ログインできない問題が発生します。

アップルはこの2FA認証の代わりで使える`API Key`を提供してます。API Keyを生成するためAppstoreconnectの`Users and Access`ページへ移動します。

- [https://appstoreconnect.apple.com/access/api](https://appstoreconnect.apple.com/access/api){:rel="nofollow noreferrer" target="_blank"}

このページで追加ボタンを押してAPI Keyを生成します。色んな質問が出ますが、読んで答えると問題なく生成することができます。

このように生成したAPI Keyで`Issuer ID`、`Key ID`そしてダウンロードしたキーファイルは後でFastLaneで設定して使います。ここでダウンロードしたファイルはReact Nativeプロジェクトの`ios`フォルダへコピーします。私は分かりやすくするためファイル名を`distribution.p8`で変更して保存しました。

{% include in-feed-ads.html %}

### iOS Fastlane

デプロイをするため必要なファイルは全て準備しました。ここからFastlaneファイルを修正してデプロイを準備してみます。

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

アンドロイドと同じようにバージョンを更新するFastlaneとデプロイをするためのFastlaneで分けました。しかし、アンドロイドとは違ってデプロイするためのFastlaneを少し修正する必要があります。

まず、iOSアプリをデプロイするため`Certificate`を設定する必要があります。

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

Keychain Accessでダウンロードした`distribution.p12`ファイルを設定して、Exportする時入力したパスワードを設定します。`create_keychain`の`password`と `import_certificate`の`keychain_password`はCertificateをExportする時使ったパスワードとは関係ないですが、二つのパスワードに同じパスワードを設定してもいいです。

```ruby
install_provisioning_profile(path: 'distribution.mobileprovision')
update_project_provisioning(
  xcodeproj: '[Your Project Name].xcodeproj',
  target_filter: 'github',
  profile: 'distribution.mobileprovision',
  build_configuration: 'Release'
)
```

そして上のように`Provisioning profile`ファイルを設定します。そして次のようにAPI Keyを使うため`app_store_connect_api_key`関数を呼び出してその結果を`api_key`変数へ入れます。

```ruby
api_key = app_store_connect_api_key(
  key_id: 'XXXXXXXXXXXXx',
  issuer_id: 'XXXXXXX-XXXXXXXXXXXXX-XXXXXXXXXXX',
  key_filepath: 'distribution.p8'
)
```

最後に以前作ったFastlaneを使ってアプリをデプロイするように設定します。ただし、API Keyを使ってデプロイするため`upload_to_app_store`を次のように修正して設定する必要があります。

```ruby
upload_to_app_store(
  ...
  precheck_include_in_app_purchases: false,
  ...
  api_key: api_key
)
```

上で作って貰った`api_key`変数を設定して`precheck_include_in_app_purchases`は`false`で設定します。`precheck_include_in_app_purchases`を設定しない場合デプロイする時エラーが発生します。

{% include in-feed-ads.html %}

## GitHub Actions

そしたら次は`GitHub Actions`を使うためGtiHub Actionsへ必要な設定ファイルを生成する必要があります。React Nativeプロジェクトフォルへ`.github/workflows/main.yml`ファイルを生成して下記のように修正します。

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

まず、GitHub Actionsの名前を設定していつGitHub Actionsを実行するか設定します。

```yaml
name: Publish iOS and Android App to App Store and Play Store
on:
  push:
    tags:
      - "v*"
```

私は`v`で始まるタグが`push`されるとGitHub Actionsが実行されるように設定しました。

```yaml
jobs:
  release-ios:
  release-android:
```

そして実際実行されるコマンドをアンドロイドとiOSを分けて設定しました。

{% include in-feed-ads.html %}

### iOS GitHub Actions

GitHub ActionsでiOSへ使うコマンドをみてみましょう。

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

まずiOSは`runs-on: macos-latest`を使ってマックOSでコマンドを実行するように設定します。

```yaml
- uses: actions/checkout@v2
```

そして現在のRepositoryのソースコードを持ってきた後、

```yaml
- uses: actions/setup-node@v1
  with:
    node-version: "10.x"
- uses: actions/setup-ruby@v1
  with:
    ruby-version: "2.x"
```

ノードとルビをインストールします。

```yml
- name: Install Fastlane
  run: cd ios && bundle install && cd ..
- name: Install packages
  run: yarn install
- name: Install pods
  run: cd ios && pod install && cd ..
```

その後、Fastlane、ノードパッケージ、そしてPodライブラリをインストールします。

```yml
- name: Execute Fastlane command
  run: cd ios && fastlane github
```

最後に私たちが作ったFastlaneのgithubを実行します。

{% include in-feed-ads.html %}

### アンドロイドGitHub Actions

GitHub Actionsでアンドロイドで使うコマンドをみてみましょう。

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

まず、アンドロイドは`runs-on: ubuntu-latest`を使ってubuntuサーバでコマンドを実行するように設定します。

```yaml
- uses: actions/checkout@v2
```

そして現在のRepositoryのソースコードを持ってきて、

```yaml
- uses: actions/setup-node@v1
  with:
    node-version: "10.x"
- uses: actions/setup-ruby@v1
  with:
    ruby-version: "2.x"
```

ノードとルビをインストールします。

```yaml
- name: Install Fastlane
  run: cd ios && bundle install && cd ..
- name: Install packages
  run: yarn install
```

その後、Fastlaneとノードパッケージをインストールします。

```yaml
- name: Prebuild
  run: npm run prebuild-android
```

そしてアンドロイドデプロイファイルを生成するため`prebuild-android`を実行します。このコマンドは私が個人的に`package.json`の`scripts`へ設定したコマンドで下記のようです。

```json
...
"scripts": {
  ...
  "prebuild-android": "npx jetify && react-native bundle --platform android --dev false --entry-file index.js --bundle-output android/app/src/main/assets/index.android.bundle",
  ...
}
...
```

最後に私たちが作ったFastlaneのgithubを実行します。

```yaml
- name: Execute Fastlane command
  run: cd android && fastlane github
```

{% include in-feed-ads.html %}

## スクリプト

このように作ったFastlaneとGitHub Actionsを使うために下記のようなコマンドを使います。

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

アンドロイドフォルダとiOSフォルダへ移動して上で作ったFastlaneのversionを使ってローカルでデプロイするアプリのバージョンを変更します。

```bash
cd android
fastlane version version:$VERSION
cd ..
cd ios
fastlane version version:$VERSION
cd ..
```

このように変更したバージョンをGitで管理するためCommitとPushをやっておきます。

```bash
git add .
git commit -m 'update version'
git push origin main
```

最後にTagを設定してPushをしてGitHub Actionsを実行します。

```bash
git tag -a v$VERSION -m 'add verstion tag' -f
git push origin v$VERSION -f
```

このように作ったスクリプトファイルをReact Nativeプロジェクトフォルダへ`release.sh`名前で保存します。そしてGitHub Actionsを使ってアプリをデプロイしたい時下記のようにコマンドを実行します。

```bash
# sh ./release.sh 3.3.1
# sh ./release.sh major
# sh ./release.sh minor
sh ./release.sh patch
```

## 完了

これでGitHub ActionsとFastlaneを使ってアプリをデプロイする方法についてみてみました。資料があまりなくって作る時結構くろしました。この資料が誰かに少しても役に立てたら嬉しいです。

私はiOSで色んなエラーがでって結構くろしました。また無料ユーザはGitHub Actionsを使う時間が1ヶ月で2,000分でマックOSを使うとLinuxサーバを使う時間より10倍で計算する問題があります。普通のiOSアプリを1つデプロイするには30分ぐらいがかかるので1回デプロイすると300分の時間を使うことになります。したがって、無料で1ヶ月にデプロイする回数は8回ぐらいですね。アンドロイドは10分しかかからなくてLinuxサーバなので、10分、そのまま計算されますので、問題ないですが、マックOSは少し気になります。もし他のGitHub Actionsを使ってる方はこの時間に注意する必要があります。

今度は、皆さんもGitHub Actionsを使って効率的アプリをデプロイしてみてください。
