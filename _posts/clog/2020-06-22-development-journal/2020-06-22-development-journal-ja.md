---
layout: 'post'
permalink: '/clog/development-journal/'
paginate_path: '/clog/:num/development-journal/'
lang: 'ja'
categories: 'clog'
comments: true

title: '「Clog」サービス開発日誌(React Native, Laravel, Django)'
description: React Native, Laravel, Djangoを使って「Clog」と言うサービスを開発してみましたこのサービスを開発した時、経験した内容をまとめてみました。
image: '/assets/images/category/clog/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [目次](#目次)
- [概要](#概要)
- [Clogとは](#clogとは)
- [なぜ作ることになったか](#なぜ作ることになったか)
- [サービス企画](#サービス企画)
- [デザイン](#デザイン)
- [システム構成](#システム構成)
- [DB設計](#db設計)
- [APIサーバー開発](#apiサーバー開発)
- [クローリングサーバ開発](#クローリングサーバ開発)
- [アプリ開発](#アプリ開発)
- [開発中の問題](#開発中の問題)
  - [Dothomeホスティング](#dothomeホスティング)
  - [ビデオ再生](#ビデオ再生)
  - [Reject](#reject)
- [開発期間](#開発期間)
- [懐古](#懐古)

</div>

## 概要

もう16番目のトーイプロジェクトです。下記のリンクで今まで私が開発したトーイプロジェクトを確認できます。気になる方は下記のリンクで確認してください。

- [JeongHean's App List]({{site.url}}/app/list/){:target="_blank"}

トーイプロジェクトを開発しながら作成した開発日誌もあります。

- [BlaBooアプリ開発日誌(RN, React Native)]({{site.url}}/blaboo/development-journal/){:target="_blank"}
- [Kumonchoアプリ開発日誌(RN, React Native)]({{site.url}}/kumoncho/development-journal/){:target="_blank"}
- [일단공부アプリ開発日誌(RN, React Native)]({{site.url}}/ildangongbu/development-journal/){:target="_blank"}

私は主にFacebookのグループで開発、スタートアッなどの情報を見てます。しかし、Facebookがこのような情報を共有するため生まれたプラットフォームではないので、要らない情報もたくさん持ってます。

それで私に必要な情報だけを集めて見せるアプリがあれば、いいかなと思ってこのようなサービスを企画や開発することになりました。

## Clogとは

Clogは開発、スタートアップやトレンドなどの情報を取得するため、ブログ、検索やFacebookなどで探した不便さを改善するため、1つの場所へ集めて見せるサービスです。（まだ、韓国語版しかないです。）

- Clog紹介ページ: [Clog - 世界の全ての情報をまとめて見る]( https://dev-yakuza.posstree.com/app/clog/){:target="_blank"}

下記はアプリダウンロードリンクです。

<div class="download_link_container">
    <a class="download_link_ios" href="https://apps.apple.com/app/clog/id1513780724" target="_blank">
        <img src="/assets/images/apple_download.png" alt="Clog - 世界の全ての情報をまとめて見る, ios ダウンロード"/>
    </a>
    <a class="download_link_android" href="https://play.google.com/store/apps/details?id=io.github.dev.yakuza.clog" target="_blank">
        <img src="/assets/images/google play_download.png" alt="Clog - 世界の全ての情報をまとめて見る, 안드로이드 ダウンロード"/>
    </a>
</div>

## なぜ作ることになったか

概要でも少し話しましたが、私は開発/スタートアップ/トレンドなどの情報をFacebookのグールプで取得してます。また、MediumやGitHubなどの個人ブログも検索をして探して見てます。

このように必要な情報を取得するため、Facebookを確認したりいいブログを探して見たりすることが大変だし、このような方式は欲しい情報だけ見ることができないです。

それで開発/スタートアップ/トレンドなどの情報を1つの場所でまとめて見るサービスを作成したら役に立てるかなと思ってこのようなサービスを開発することになりました。

![Clog - 世界の全ての情報をまとめて見る](/assets/images/category/clog/background.jpg)


{% include in-feed-ads.html %}

## サービス企画

一旦ネーミングはClogの`C`は`B`logの次のバージョンを意味しております。また、`C`が英語の`See`と発音が似てるので、`See log`、つまり記録を見ると言う意味も持ってます。

ClogのMVP(Minimum Viable Product: 最小機能製品)は下記のように定義しました。

1. 情報収集: 開発/スタートアップ/トレンドなどと関係ある情報、特にブログを集める。
1. 情報提供API: 集めた情報をAPIで提供する。
1. ブログリスト: APIを使ってブログポストリストを取得して見せる。
1. ブログの詳細: リストで詳しくみたいItemを選択すると、そのブログの詳細内容が見れる。

他のアプリを開発した時より、MVPがとてもシンプールでした。`記事を集めて、記事を見せる。`へ集中しました。

## デザイン

私はデザインは私がやるものではないと思って生きて来た開発者です。だからこそ、デザインが一番大変です。小さい会社でフロントエンドを開発するときは開発者がUI/UXもやってるので、ツールを使うことでは慣れてますが、問題を解決する開発とは違って、デザインはセンスの問題なので、多く大変さを感じてます。

そしてもトーイプロジェクトを進める時考えて、失敗してどんどん上手くなってるのかと思います。やはり、練習が一番大事ですね。

![Clog - 世界の全ての情報をまとめて見る. ロゴデザイン](/assets/images/category/clog/development-journal/logo.jpg)


ロゴは`See log`からアイデアを思い出しました。`見る`と言う意味を強調するため`C`を人の`目`の形にデザインしてみました。また、大きいロゴでは目を開いてlogを見るイメージで、眉毛のイメージも追加して瞳もlogの方に近くなるようにデザインしてみました。

メインの色は信頼と安定感を感じる青色系にして、ちょっと新鮮さを出すため明るさを上げました。

![Clog - 世界の全ての情報をまとめて見る。ロゴデザイン](/assets/images/category/clog/development-journal/all_design.jpg)


アプリの全般的なデザインは最初１〜２ページだけでしたが、開発しながらどんどん必要な機能が多くなって上記のようにデザインが増えました。全てのデザインは`sketchapp`で作成しました。

{% include in-feed-ads.html %}

## システム構成

Clogは下記のようなシステで構成されております。

![Clog - 世界の全ての情報をまとめて見る。システム構成図](/assets/images/category/clog/development-journal/system-architecture.jpg)


アプリは`React Native`で開発して、iOS / Android両方使えるようにしました。メインのサーバにあるAPIサーバは`Laravel(php)`で開発して、情報を集めるクローリングサーバは`Django(python)`で開発しました。

本当はクローリングサーバとAPIサーバを1つで開発しても全然大丈夫ですが、私が貧乏な開発なので、AWSとかGCPを維持する余力がなくて、安いホスティングサービスを使うことにしました。韓国の`Dothome`と`heroku`を使って安くサービスを維持するように構成しました。

![Clog - 世界の全ての情報をまとめて見る。Dothome,Herokuホスティング](/assets/images/category/clog/development-journal/dothome_plan.jpg)


Dothomeはドメインを購入するとすると無制限ウェブホスティングを使えることができます。無制限ウェブホスティングは1日`1G`まで基本トラフィックが提供されて、そのあとはウェブサービスの速度が制限されることになります。現在1Gを超えたことがないので、どのぐらい遅くなるかテストはませんでしたが、写真、動画などをサービスしてないので、多く問題はなくサービスを維持するとこができると思いました。ユーザが増えて問題にナルト、500円ダスト無制限トラフィックを使えるので、これでいいかと思ってます。（このブログポストはDothomeとは無関係です。）

詳しい内容は下記のリンクを確認してください。（韓国語です）

- [Dothome - 無制限ホスティング](https://www.dothome.co.kr/web/premium/index.php){:rel="nofollow noreferrer noopener" target="_blank"}

問題はDothomeでは`php`のみサービスをしてます。それでシステムを考える時、`Laravel`を選択しました。また、SSHアクセスもできないので、`crontab`などを使うことができないので、定期的作業するサーバが別に必要になりました。

Herokuは色んな言語をサーポートするクラウドサービスで`無料`で使うことができます。しかし、無料なので、性能の面で良くないことがあったので、DothomeをメインAPIサーバにして、Herokuサーバをクローリングサーバにしました。

Herokuは無料で`550 free dyno hours`を提供しております。dyno hoursで書いてますが結局使える時間を意味します。1日24時間を可動すると22日ほど使うことができます。それでは1ヶ月使うことができないです。しかし、クレジットカードを登録すると追加で`450 dyno hours`を貰えます。そしたら全部で`1000 dyno hours`を使えます。24時間使っても41日使えることができます。つまり1ヶ月使うことができます。

![Clog - 世界の全ての情報をまとめて見る. heroku free plan](/assets/images/category/clog/development-journal/heroku_plan.jpg)


問題はこのように無料で使えますが、30分間何もしないと、スリップモードに入るので、起こす時は時間がかかります。それで、APIサーバでは良くないと思って、定期的作業をすることをしました。

Herokuの無料プランに関して詳しく内容は下記のリンクを参考してください。(このブログポストはHerokuとは無関係です。)

- [Heorku - 無料プラン](https://www.heroku.com/free){:rel="nofollow noreferrer noopener" target="_blank"}

このように完成したシステム図は下記のようです。

![Clog - 世界の全ての情報をまとめて見る。ホスティングシステム構成図](/assets/images/category/clog/development-journal/system-architecture-hosting.jpg)


React Nativeでアプリを開発して、Dothomeが提供するPHPサーバとMysqlをLaravel APIサーバで構成して、最後にはHerokuでDjangoを動かしてクローリングをしております。

今振り替えてみると、HerokuではDjangoまで環境を設定する必要はなかったなと思います。単純にクローリングだけしてるので、なまPythonでも良かったかなと思いますね。

{% include in-feed-ads.html %}

## DB設計

DBはDothomeではMysqlを提供するので、Mysqlを使えなきゃならないです。そして、MySQL Workbenchをつかて下記のようにDBを設計しました。

![Clog - 世界の全ての情報をまとめて見る. DB設計図](/assets/images/category/clog/development-journal/db_erd.jpg)


## APIサーバー開発

APIサーバ開発はLaravelで構成しました。今からPHPフレイムワークで一番良かったなと思えたので、Laravelを使えるようにしました。

単純にDBへある情報を取って送るだけなので開発はそんなに時間は掛からなかったです。

しかし、Dothomeでは`FTP`でデプロイをしなきゃなラナイし、Dothomeが提供するPHPバージョンとMysqlバージョンを考えなきゃならないです。最初からこれを考えなかったので、FTPでファイルをアップロードしてもサーバが起動できませんでした。あ。。。それと何年ぶりのFTPデプロイか。。。しかし、`git-ftp`と言うオープンソースがあったので、簡単にデプロイするようになりました。

- [Git FTPを使ってデプロイする]({{site.url}}/git/git-ftp/){:target="_blank"}

今回のサービスではログイン機能があります。ログイン認証機能には`JWT(Json Web Token)`を使ってます。

- [jwtインストールや設定]({{site.url}}/laravel/jwt/){:target="_blank"}
- [jwt:会員登録]({{site.url}}/laravel/jwt-signup){:target="_blank"}
- [jwt:ログイン]({{site.url}}/laravel/jwt-signin){:target="_blank"}
- [jwt:ユーザ情報]({{site.url}}/laravel/jwt-user-info){:target="_blank"}
- [jwt:トークン更新]({{site.url}}/laravel/jwt-refresh-token){:target="_blank"}
- [jwt:ログアウト]({{site.url}}/laravel/jwt-logout){:target="_blank"}

## クローリングサーバ開発

ウェブにある情報をそのままクローリングすることは法律的色々問題があるので、今回のサービスでは`RSS(Rich Site Summary)`を使ってクローリングサーバを構成しました。

RSS Feedも個人的に購読することを目的にするので、法律的に問題があるかもしれないですが、私のサービスでそんなにトラフィックを取ることもないし、単純にタイトルと、イメージ、本文の一部を見せて、クリックすると、リダイレクトではなく直接サイトをオープンしてるので、そんなに問題ではないと思いました。また、大きく問題になるそうなニュースより、個人のブログやスタトアップの記事を撮ってくるようにしました。（問題になるとやめるしか。。。）

ブログリストは個人的に集めたものと`awesome-devblog`（韓国）のGitHubで持ってきました。

- [https://github.com/sarojaba/awesome-devblog](https://github.com/sarojaba/awesome-devblog){:rel="nofollow noreferrer noopener" target="_blank"}

これ以外にも色んなリソースを使ってクローリングを進めております。

## アプリ開発

アプリはReact Nativeを使ってiOS、アンドロイドを開発/デプロイしました。アプリは単純にAPIを使って必要なデータを取得して、画面へ表示するものなので、そんなに難しい記述を使ってません。

アプリの基本構造はTypescriptとStyled componentsを使っております。

- [typescript]({{site.url}}/react-native/typescript/){:target="_blank"}
- [styled-components]({{site.url}}/react-native/styled-components/){:target="_blank"}
- [RN(React Native)でroot importする]({{site.url}}/react-native/root-import/){:target="_blank"}

アプリのアイコンとSplashイメージ適用はreact-native-makeと言うライブラリを使いました。

- [React NativeでAppアイコン&Splashイメージを作る]({{site.url}}/react-native/react-native-make/){:target="_blank"}
- [App Splashスクリン]({{site.url}}/react-native/react-native-splash-screen/){:target="_blank"}

ナビゲーションはreact-navigation v5を使ってます。

- RN(React Navtive)でreact-navigation v5を使う: [react-navigation V5]({{site.url}}/react-native/react-navigation-v5/){:target="_blank"}

そしてアプリの分析や広告にはreact-native-firebase v6を使ってます。

- [react-native-firebase V6 インストール]({{site.url}}/react-native/react-native-firebase-v6-installation/){:target="_blank"}
- [react-native-firebase V6 Crashlytics]({{site.url}}/react-native/react-native-firebase-v6-crashlytics/){:target="_blank"}
- [react-native-firebase V6 Admob]({{site.url}}/react-native/react-native-firebase-v6-admob/){:target="_blank"}

今回のアプリではバーナ広告ではなく、ネーティブ広告を使ってます。しかしreact-native-firebaseではネーティブ広告をサーポートしてません。ネーティブ広告を使うため今回のアプリではreact-native-admob-native-adsを使ってます。

- [react-nativeでNative Advanced広告を表示する]({{site.url}}/react-native/react-native-admob-native-ads/){:target="_blank"}

最後は、今回のアプリはビデオタブを持ってます、ビデオはYoutube動画を再生しております。これのためreact-native-youtubeと言うライブラリを使ってます。

- [react-nativeでYoutubeを再生する]({{site.url}}/react-native/react-native-youtube/){:target="_blank"}

react-native-videoもやってみましたが、youtubeのダウンロードリンクを作る時、時間がかかることと制限(1つのIPでは6時間間に1回生成可能)などの問題があってreact-native-youtubeライブラリを使うことにしました。詳しい内容は上のリンクを確認してください。

{% include in-feed-ads.html %}

## 開発中の問題

このサービスは単純なので大きい問題はないと思いましたが、下記のような問題が発生しました。

### Dothomeホスティング

上記にも少し話しましたが、最初Laravelで開発したサーバがDothomeホスティングで動かない問題が発生しました。それでDothomeで動くPHPバージョンをローカルにインストールして、それに合うLaravelバージョンをインストールした後、再開発しました。

また、サーバへデプロイするためFTPを利用したことと、Laravelを起動するため`.htaccess`を設定する必要がありました。

### ビデオ再生

アプリで自動でビデオを再生するためreact-native-videoとreact-native-ytdlを使って開発しましたが、同じIPで何回もリンクを生成することで問題があって、アンドロイドではVideoコントローラを実現する時黒しました。

それでreact-native-videoを使うことをヤメって、react-native-youtubeを使うことにしました。react-native-youtubeもiOSでは特に問題がありませんでしたが、アンドロイドでは複数プレイアを同時に表示することができなくって、画面へ表示されたYoutubeの一番最初の動画のみでプレイアを生成して、再生できるようにしました。구성하였습니다.

### Reject

やはり、一番問題はiOSの審査でした。アプリのMVPは下記のようです。

1. ブログリスト: APIを使ってブログポストリストを取得して見せる。
1. ブログの詳細: リストで詳しくみたいItemを選択すると、そのブログの詳細内容が見れる。

この機能を実装してアプリを登録しましたが、単純にウェブの内容を集めて見せてるので、アプリでの意味がないこととネーティブの機能を使ってないのでウェブでサービスした方が良いって言われてRejectされました。これを超えるために下記の機能を追加しました。

1. おすすめ(いいね)機能
1. 共有
1. 最新順/ピックアップ順
1. ブックマーク
1. 作者ファロウ
1. Youtubeビデオ

上の機能を一つづつ開発をして、終わったら審査を投げって、どの機能が追加されたらOKになるか確認してみました。その結果Youtubeのビデオをアプリ内で見ることができるように機能を追加した後、この理由のRejectはもう出ませんでした。

その後はアプリでユーザがアップロードした情報を共有しておりますが、見たくない情報を隠す機能がないのでRejectされました。それで次の機能を追加しました。

1. 該当記事を隠す
1. 該当作者の記事を隠す

それで審査を申請したら、無事にアップストアへ登録することができました。この後、Googleのプレイストアへデプロイしましたが、アンドロイドは特に問題なくデプロイされました。

{% include in-feed-ads.html %}

## 開発期間

全てのサービスを開発した期間は2ヶ月ほとかかりました。リーン（Lean）で開発してるので、正確にどのぐらい掛かったかはっきり言えませんが、ちょっと区分すると下記のようです。

- 企画や調査: 1週間
- デザイン: 1週間
- アプリ開発: 1ヶ月
- クローリングサーバ: 1ヶ月
- APIサーバ: 1ヶ月

上の期間はあまり意味がないです。朝、昼、夜、週末など時間がある時開発したので、実際かかった時間とは関係ないです。またリーンスタイルで開発したので、正確な時間ではないです。

開発は5月からスタートして、6月末へリリースしました。

## 懐古

- 今回のトーイプロジェクトは今まで作ったトーイプロジェクトで初めてサーバを使ったプロジェクです。
- 貧乏な開発者なので、どうすると安くサービスを提供することできるかを悩んだ。
- やはり、作ってみないと、大変さがわからない。(このようなRejectもあるか)
- 開発は面白い。

<div class="download_link_container">
    <a class="download_link_ios" href="https://apps.apple.com/app/clog/id1513780724" target="_blank">
        <img src="/assets/images/apple_download.png" alt="Clog - 世界の全ての情報をまとめて見る, ios ダウンロード"/>
    </a>
    <a class="download_link_android" href="https://play.google.com/store/apps/details?id=io.github.dev.yakuza.clog" target="_blank">
        <img src="/assets/images/google play_download.png" alt="Clog - 世界の全ての情報をまとめて見る, アンドロイドダウンロード"/>
    </a>
</div>
