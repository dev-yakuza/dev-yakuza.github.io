---
layout: 'post'
permalink: '/react-native/ios-certification/'
paginate_path: '/react-native/:num/ios-certification/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'iOS 証明書(Certification)'
description: 'アップル開発者プログラム(Apple Developer Program)の登録を完了したら、開発者証明書(Certification)を設定する方法について説明します。'
image: '/assets/images/category/react-native/ios-certification.jpg'
---

<div id="contents_list" markdown="1">

## 目次

1. [概要](#概要)
1. [証明書ダウンロード](#証明書ダウンロード)
1. [証明書生成](#証明書生成)
1. [証明書登録](#証明書登録)
1. [アップル開発者アカウント連携](#アップル開発者アカウント連携)
1. [プロビジョニングプロファイル生成](#プロビジョニングプロファイル生成)
1. [プロビジョニングプロファイル連携](#プロビジョニングプロファイル連携)
1. [完了](#完了)

</div>

## 概要

このブログはアップル開発者プログラム(Apple Developer Program)へすでに登録した開発者のため説明です。アップル開発者プログラム(Apple Developer Program)へまだ登録してない方は前のブログ[iOS開発者登録]({{site.url}}/{{page.categories}}/ios-enroll-developer-program/){:target="_blank"}をみてアップル開発者プログラム(Apple Developer Program)へ登録してください。

このブログはシリーズです。下記のブログも確認してください。

- [iOSデバイステスト]({{site.url}}/{{page.categories}}/ios-test-on-device/){:target="_blank"}
- [iOSビルドやテスト]({{site.url}}/{{page.categories}}/ios-running-on-device/){:target="_blank"}
- [iOS開発者登録]({{site.url}}/{{page.categories}}/ios-enroll-developer-program/){:target="_blank"}
- [iOS TestFlight]({{site.url}}/{{page.categories}}/ios-testflight/){:target="_blank"}
- [iOS App store 登録]({{site.url}}/{{page.categories}}/ios-app-store/){:target="_blank"}
- [Fastlaneを使ってアプリのデプロイを自動化する]({{site.url}}/{{page.categories}}/fastlane/){:target="_blank"}

今から開発者の証明書(Certification)を生成して設定する方法について説明します。

## 証明書ダウンロード

アップル開発者プログラム(Apple Developer Program)を購入して購入完了メールをもらったらアップル開発者サイト([https://developer.apple.com/](https://developer.apple.com/){:rel="nofollow noreferrer" target="_blank"})の```Account```ページへ移動します。

![apple developer site after enrolling](/assets/images/category/react-native/ios-certification/apple-developer-site-after-enrolling.jpg)

アップル開発者プログラム(Apple Developer Program)へ登録する前と画面が少し違います。左上の```Certificates, IDs & Profiles```を選択して証明書(Certification)を発行するページへ移動します。

![download certification](/assets/images/category/react-native/ios-certification/download-certification.jpg)

証明書(Certification)がすでに一個存在します。この証明書(Certification)を選択して```Download```ボタンを押して証明書を好きなところに保存します。証明書が見えない方は下記の証明書生成を見って証明書を新しく生成します。

この証明書は開発用です。この証明書がある方も下記の証明書生成でリリース用の証明書を生成してください。

{% include in-feed-ads.html %}

## 証明書生成

Macで```キーチェーンアクセス```プログラムを実行します。

![キーチェーンアクセス](/assets/images/category/react-native/ios-certification/ja-keychain.jpg)

キージェーンが実行されたら左上の```キーチェーンアクセス```を選択して```証明書アシスタント```で```証明局に証明書を要求...```を選択します。

![キーチェーンアクセス証明書要求](/assets/images/category/react-native/ios-certification/ja-request-certification.jpg)

上のように```証明局に証明書を要求...```を押すと下記のように```証明書アシスタント```ダイアローグが表示します。

![キーチェーンアクセス証明書情報入力](/assets/images/category/react-native/ios-certification/ja-certification-info.jpg)

上の画面で```ユーザのメールアドレス```と```通称```へ情報を入力して```要求の処理```で```ディスクに保存```と```鍵ペア情報を指定```を選択して```続ける```を押します。ファイル保存する画面が出たら好きな場所を選択してファイルを保存します。

![キーチェーンアクセス証明書保存](/assets/images/category/react-native/ios-certification/ja-certification-key.jpg)

キーペア情報を上のように設定して```続ける```を押します。

![キーチェーンアクセス証明書完了](/assets/images/category/react-native/ios-certification/ja-certification-completed.jpg)

ディスクへ証明書が上手く保存しました。

![download certification](/assets/images/category/react-native/ios-certification/download-certification.jpg)

アップル開発者サイト([https://developer.apple.com/](https://developer.apple.com/){:rel="nofollow noreferrer" target="_blank"})の```Account```ページで```Certificates, IDs & Profiles```メニューを押して証明書登録サイトへ移動します。そこで右上にある```+```ボタンを押します。

![certification selection](/assets/images/category/react-native/ios-certification/select-certification.jpg)

証明書選択画面で```iOS App Development```を選択して下にスクロールして```Continue```ボタンを押します。

リリース用証明書を生成する方は```Production```の部分で```App Store and Ad Hoc```を選択してく進んでください。

証明書ファイル(CSR)を作る方法を説明するページが出ます。私たちは上部で```キーチェーンアクセス```ですでに証明書ファイル(CSR)を作りましたのでスクロールして```Continue```ボタンを押します。

![create csr file](/assets/images/category/react-native/ios-certification/create-csr-file.jpg)

生成した証明書ファイルを選択する画面で```Choose File```ボタンを押して上部で作った証明書ファイルを選択して下にある```Continue```ボタンを押します。

![choose csr file](/assets/images/category/react-native/ios-certification/choose-csr-file.jpg)

証明書の生成を完了しました。```Download```ボタンを押して証明書を好きなところへ保存してください。

![complete create certification file](/assets/images/category/react-native/ios-certification/complete-create-certification.jpg)

## 証明書登録

生成した証明書を```キーチェーンアクセス```へ入れる必要があります。```キーチェーンアクセス```を実行します。

![キーチェーンアクセス](/assets/images/category/react-native/ios-certification/ja-keychain.jpg)

下のように```キーチェーンアクセス```が開けたら左下にある```自分の証明書```を押して上部でダウンロードした証明書のファイルをドラッグして追加します。

![キーチェーンアクセス証明書](/assets/images/category/react-native/ios-certification/ja-keychain-certification.jpg)

{% include in-feed-ads.html %}

## アップル開発者アカウント連携

アップル開発者アカウント(Apple Developer)と現在のプロジェクトを連携する必要があります。リアクトネイティブ(React Native)のプロジェクトフォルダで```ios/プロジェクト名.xcodeproj```ファイルを実行します。

xcodeで左上の```プロジェクト名```を選択して```General```タブに移動します。

![xcode certification](/assets/images/category/react-native/ios-certification/xcode-certification.jpg)

上のような画面で```Signing```の部分で```Team```の横にあるドロップダウンメニューを選択します。

![xcode certification add new](/assets/images/category/react-native/ios-certification/xcode-certification-add-new.jpg)

すでにxcodeとアップル開発者アカウント(Apple Developer)が連動されてる方はそのアカウントを選択します。アカウント連動をしてない方は```Add an Account```を選択します。

![xcode certification login](/assets/images/category/react-native/ios-certification/xcode-certification-login.jpg)

アップル開発者アカウント(Appld Developer)でログインします。アップル開発者アカウント(Appld Developer)がない方は[iOS デバイステスト]({{site.url}}/{{page.categories}}/ios-test-on-device/){:target="_blank"}でアップル開発者アカウント生成方法を見って作ってください。ログインを完了したら左上の閉じるボタンを押して画面を閉じます。

![xcode certification add new](/assets/images/category/react-native/ios-certification/xcode-certification-add-new.jpg)

また```Team```の横のドロップダウンメニューを選択したら先ほど追加したアップル開発者アカウントが見えます。そのアカウントを選択します。

同じ方法でTestの部分もアップル開発者アカウント(Apple Developer)と連携します。

![xcode certification add test](/assets/images/category/react-native/ios-certification/xcode-certification-add-test.jpg)

これでアップル開発者アカウントとの連携が終わりました。今からリリース用のビルドへ必要なプロビジョニングプロファイル(Provisioning Profiles)を生成して連携します。

{% include in-feed-ads.html %}

## プロビジョニングプロファイル生成

アップル開発者サイト(Apple Developer)の```Account```ページで下にスクロールしたら```Provisioning Profiles```の項目が見ます

プロビジョニングプロファイル(Provisioning Profiles)も開発用とデプロイ用が必要なので下記のプロセスを開発用とデプロイ用で2回進める必要があります。

![provisioning profiles](/assets/images/category/react-native/ios-certification/provisioning-profiles.jpg)

メニューの```All```を押してプロビジョニングプロファイル(Provisioning Profiles)を登録するページへ遷移します。

![provisioning profiles detail](/assets/images/category/react-native/ios-certification/provisioning-profiles-detail.jpg)

上のような画面が見えたら右上の```+```ボタンを押して新しプロビジョニングプロファイル(Provisioning Profile)を追加します。

![provisioning profiles ios](/assets/images/category/react-native/ios-certification/provisioning-profiles-ios.jpg)

上のような画面で```iOS App Development```を選択して```Continue```ボタンを押して進めます。

リリース用プロビジョニングプロファイル(Provisioning Profiles)は```Distribution```の```App Store```を選択して進めてください。

![provisioning profiles app id](/assets/images/category/react-native/ios-certification/provisioning-profiles-app-id.jpg)

私たちがアプリを開発する時使った```Bundle Identifier```を選択します。```Bundle Identifier```はxcodeで左上の```プロジェクト名```を選択して```General```タブに移動したら一番上の部分で```Identity```項目を確認することが出来ます。

![xcode bundle identifier](/assets/images/category/react-native/ios-certification/xcode-certification.jpg)

選択を完了したら```Continue```を押して進めてください。開発者アカウントとテストするデバイスを選択して次のページへ移動します。

![provisioning profiles name](/assets/images/category/react-native/ios-certification/provisioning-profiles-name.jpg)

最後にプロビジョニングプロファイル(Provisioning Profile)の名前を設定して```Continue```を押して次のページへ移動します。

プロビジョニングプロファイル(Provisioning Profile)の生成が完了しました。```Download```を押してファイルを好きなところに保存してください。

{% include in-feed-ads.html %}

## プロビジョニングプロファイル連携

xcodeでは基本的に自動に```Signing```を管理する設定がされております。(```Signing```項目の```Automatically manage signing```)

![xcode bundle identifier](/assets/images/category/react-native/ios-certification/xcode-certification.jpg)

この状態でプロビジョニングプロファイル(Provisioning Profile)の連携、リリースのビルドする時特に問題ない方はそのまま使っても大丈夫です。（```Signing```の項目へ赤文字エラーがない方）私たちはプロビジョニングプロファイル(Provisioning Profile)との連携が上手く出来なかったので手動で連携してみます。

下記は手動でプロビジョニングプロファイル(Provisioning Profile)を連携する方法です。

![xcode bundle identifier](/assets/images/category/react-native/ios-certification/xcode-certification.jpg)

上のような画面で```Signing```の```Automatically manage signing```を選択してチェックを外します。

![disable automatically manage signing](/assets/images/category/react-native/ios-certification/disable_auto.jpg)

チェックを外したら上の画面ような```Signing(Debug)```と```Signing(Release)```が見えます。二つの```Provision Profile```の横にあるドロップダウンメニューで```Import Profile```を選択して上部で生成してダウンロードしたプロビジョニングプロファイル(Provisioning Profile)を選択します。同じ方法でTestの部分も修正します。

![disable automatically manage signing test](/assets/images/category/react-native/ios-certification/disable_auto_test.jpg)

## 完了

全ての設定が終わりました。証明書を連携したので開発やリリースの準備まで終わりました。次のブログからはリリース準備や```TestFlight```を使う方法、実際のリリースについて説明します。
