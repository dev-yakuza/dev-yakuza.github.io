---
layout: 'post'
permalink: '/react-native/ios-testflight/'
paginate_path: '/react-native/:num/ios-testflight/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'iOS TestFlight'
description: 'iOSのTestFlightを使って作ったアプリをテスターに送ってテストしてみましょう。'
image: '/assets/images/category/react-native/ios-testflight.jpg'
---

<div id="contents_list" markdown="1">

## 目次

1. [概要](#概要)
1. [リリース用アプリ生成](#リリース用アプリ生成)
1. [アプリビルド](#アプリビルド)
1. [アプリアップロード](#アプリアップロード)
1. [テストグループ生成](#テストグループ生成)
1. [ビルド追加](#ビルド追加)
1. [テスター追加](#テスター追加)
1. [公開リンク](#公開リンク)
1. [完了](#完了)

</div>

## 概要

iOSは開発したアプリをリリースする前自分のテスターまたはテストバージョンの公開URLを使ってテストができる```TestFlight```システムを持ってます。ここでは```TestFlight```を使って開発したアプリをテストする方法について話します。

このブログはシリーズです。下記のブログも確認してください。

- [iOSデバイステスト]({{site.url}}/{{page.categories}}/ios-test-on-device/){:target="_blank"}
- [iOSビルドやテスト]({{site.url}}/{{page.categories}}/ios-running-on-device/){:target="_blank"}
- [iOS開発者登録]({{site.url}}/{{page.categories}}/ios-enroll-developer-program/){:target="_blank"}
- [iOS証明書(Certification)]({{site.url}}/{{page.categories}}/ios-certification/){:target="_blank"}
- [iOS App store 登録]({{site.url}}/{{page.categories}}/ios-app-store/){:target="_blank"}
- [Fastlaneを使ってアプリのデプロイを自動化する]({{site.url}}/{{page.categories}}/fastlane/){:target="_blank"}

アップル開発者プログラムApple Developer Program)の登録や証明書(Certification)の設定が出来てない方は上のブログを参考してください。

## リリース用アプリ生成

アップルが提供してる```TestFlight```を使ってアプリをテストする場合アプリストアコネクト(Apple Store Connect)にリリース用アプリを生成する必要があります。下記のリンクを押してアプリストアコネクト(App Store Connect)へ移動します。

- アプリストアコネクト(App Store Connect): [https://appstoreconnect.apple.com/](https://appstoreconnect.apple.com/){:rel="nofollow noreferrer" target="_blank"}

![App Store Connect](/assets/images/category/react-native/ios-testflight/app-store-connect.jpg)

アプル開発者プログラム(Apple Developer Program)へ登録した開発者アイディでログインします。アプル開発者プログラム(Apple Developer Program)へ登録してない方は[iOS開発者登録]({{site.url}}/{{page.categories}}/ios-enroll-developer-program/){:target="_blank"}のブログを参考して登録してください。

ログインをしたら下記のような画面が見えます。```マイAppApp```を押してアプリ管理ページへ移動します。

![アプリストアコネクトメイン](/assets/images/category/react-native/ios-testflight/ja-app-store-connect-main.jpg)

左上の```+```ボタンを押して```新規App```メニューを選択します。

![アプリリスト](/assets/images/category/react-native/ios-testflight/ja-app-list.jpg)

アプリ登録画面が出たら、自分のアプリの情報を入力します。よくわからない部分があったら項目の左にある```?```マークを押して内容を確認します。名前とプライマ言語(アプリの多言語で対応してない国からアプリを起動した時表示する言語)は後でも帰れます。

![アプリ生成](/assets/images/category/react-native/ios-testflight/ja-new-app.jpg)

- バンドルID: アプリを開発する時使った```bundle ID```です。これが何か分からない方は[iOSデバイステスト]({{site.url}}/{{page.categories}}/ios-test-on-device/){:target="_blank"}を見てください。
- SKU: App Storeには表示しないアプリユニークIDです。仏はURL形式で作成します。(ex> io.github.dev-yakuza.blaboo)

![アプリメニュー](/assets/images/category/react-native/ios-testflight/ja-app-menu.jpg)

アプリを生成したら上の画面ようにメニューが見えます。メニュー中```TestFlight```メニューを選択します。

開発したアプリを```TestFlight```を使ってテストするためにはリリース用ビルドが必要になりそのビルドがアプリストアコネクト(App Store Connect)へアップロードする必要があります。

{% include in-feed-ads.html %}

## アプリビルド

開発したアプリをビルドしてアプリストアコネクト(App Store Connect)へアップロードする方法について説明します。すでにビルドしたアプリがある方はこの部分はスキップしても大丈夫です。

リアクトネイティブ(React Native)プロジェクトフォルダへ```ios/プロジェクト名.xcodeproj```ファイルを実行します。

![build for production](/assets/images/category/react-native/ios-testflight/build-for-production.jpg)

xcodeが実行されたら上部にあるメニューで```Product``` > ```Archive```を選択します。アプリ開発者プログラム(Apple Developer Program)へ登録されてない方や証明書を連携してない方は以前のブログを確認してください。([iOS開発者登録]({{site.url}}/{{page.categories}}/ios-enroll-developer-program/){:target="_blank"}, [iOS 証明書(Certification)]({{site.url}}/{{page.categories}}/ios-certification/){:target="_blank"})

ビルドが無事に終わったら下のような画面が出ます。

![build for production](/assets/images/category/react-native/ios-testflight/distribute-app.jpg)

## アプリアップロード

ビルド完了後、見える画面を閉じた方やすでにビルドしたファイルを持ってる方はxcodeの上部にあるメニューで```Window``` > ```Organizer```を選択します。

![organizer menu](/assets/images/category/react-native/ios-testflight/organizer-menu.jpg)

メニューまたはビルドを完了したら下の画面が見えます。

![build for production](/assets/images/category/react-native/ios-testflight/distribute-app.jpg)

右にある```Distribute App```を選択します。アプリをリリースするではなくアプリをアプリストアコネクト(App Store Connect)へアップロードする機能です。

![select platfom](/assets/images/category/react-native/ios-testflight/select-platform.jpg)

開発したアプリをリリースするプラットフォームを選択します。私たちは```iOS App Store```を選択します。

![upload or export](/assets/images/category/react-native/ios-testflight/upload-export.jpg)

最後の目的地がアプリストアコネクト(App Store Connect)へアップロードするかipaファイルを出す(export)かを決める画面です。私たちはアプリストアコネクト(App Store Connect)へアップロードする予定ですので```Upload```を選択します。

![options](/assets/images/category/react-native/ios-testflight/options.jpg)

オプション選択画面です。全てのオプションがチェックされてる状態で```Next```を押します。次の画面で生成した証明書とプロビジョニングプロファイル(Provisioning Profile)を選択します。証明書、プロビジョニングプロファイル(Provisioning Profile)生成は以前のブログ([iOS証明書(Certification)]({{site.url}}/{{page.categories}}/ios-certification/){:target="_blank"})を確認してください。

アップロードの準備がおわたら下の画面が見えます。```Upload```ボタンを押して準備出来たファイルをアプリストアコネクト(App Store Connect)へアップロードしてください。

![upload](/assets/images/category/react-native/ios-testflight/upload.jpg)

無事にアプリをアプリストアコネクト(App Store Connect)へアップロードしました。アップロードしたファイルを使える準備が出来たらアップルからメールが来ます。アップロードからメール来る時まだちょっと時間がかかります。

{% include in-feed-ads.html %}

## テストグループ生成

アップルからメールを貰った方はアプリストアコネクト
애플에서 메일을 받으신 분들은 앱 스토어 커넥트(App Store Connect)の ```TestFlight```ページに移動します。

![ビルドファイルリスト](/assets/images/category/react-native/ios-testflight/ja-testflight-build-file-list.jpg)

上のような```TestFlight```画面でアップロードしたファイルが見えます。左下の```新規グループ ＋```を押してテストのためのグループを生成します。

![テストグループ生成](/assets/images/category/react-native/ios-testflight/ja-create-test-group.jpg)

テストグループを生成したら左メニューへ生成する時使ったグループ名が追加されます。そのグループを選択します。

![テストグループ](/assets/images/category/react-native/ios-testflight/ja-test-group.jpg)

テストグループの生成を完了しました。今後はビルドファイル、テスターを追加してテストする方法を紹介します。

## ビルド追加

テストグループを選択した画面で上部にある```ビルド```タブを選択します。

![ビルドタブ選択](/assets/images/category/react-native/ios-testflight/ja-build-tab.jpg)

ビルドタブで```ビルド(0)```の横にある```+```ボタンを押してビルドファイルを選択する画面に移動します。テストしたいビルドを選択した下にある```次へ```ボタンを押します。

![ビルド選択](/assets/images/category/react-native/ios-testflight/ja-select-build.jpg)

テストする時ログイン情報が必要かどうか選択する画面が出ます。アプリをテストするためにログイン情報が必要な場合、```サインインが必要です```を選択してID/PWを入力して```次へ```ボタンを押します。

![ログイン必要](/assets/images/category/react-native/ios-testflight/ja-need-login.jpg)

下の画面でテスターに送りたいメッセージやテストする方ほを作成して```審査へ提出```ボタンを押します。

![テスターメッセージ](/assets/images/category/react-native/ios-testflight/ja-test-message.jpg)

テスターへテストをお願いするための```TestFlight```ですが、基本的簡単な審査をするみたいです。したがった、テスターにすぐにファイルを送ることが出来ないです。審査がおわたらテストができる状態になります。

{% include in-feed-ads.html %}

## テスター追加

アップルが提供してる```TestFlight```は大きく二つ機能があります。自分がしてるテスターを追加する方法と公開URLを生成してこのリンクを配布する方法です。まずテスターを追加する方法について説明します。```TestFlight```メニューでテストグループを押して```テスター(0)```の横にある```+```ボタンを押して```新規テスターを追加```のメニューを選択します。

![新規テスター追加](/assets/images/category/react-native/ios-testflight/ja-add-new-tester.jpg)

新しい追加するテスターのメール、名前を入力して```追加```ボタンを押します。追加するテスターのメールはアプリストア(App Store)でアプリをダウンロードする時使うメールです。

![新規テスター追加完了](/assets/images/category/react-native/ios-testflight/ja-added-new-tester.jpg)

新しテスターが追加されました。新しく追加されたテスターには```TestFlight```からメールが送信されます。

![testflight email](/assets/images/category/react-native/ios-testflight/testflight-email.jpg)

テスターはアプリストア(App store)から```TestFlight```を検索してダウンロードしたらアプリテストができます。

## 公開リンク

公開リンクを選択して登録を完了したら公開リンクが生成されます。そのリンクをコピーして共有したらテストへ参加することができます。

## 完了

これで```TestFlight```を使ってテストする方法を見ました。次のブログでは実際アップリをリリースする方法について紹介します。
