---
layout: 'post'
permalink: '/blaboo/development-journal/'
paginate_path: '/blaboo/:num/development-journal/'
lang: 'ja'
categories: 'blaboo'
comments: true

title: 'BlaBooアプリ開発日誌(RN, React Native)'
description: 'RN(React Native)を使ってBlaBooと言うアプリを開発してみました。このアプリを開発した時のエピソードをまとめてみました。'
image: '/assets/images/category/blaboo/background.png'
---


## 概要
今までRN(React Native)を勉強しましたが、アプリを最初から最後まで開発した経験がありませんでした。それでRN(React Native)を使って可能な限り早くアプリを最初から最後まで開発してみようかと思ってこのプロジェクトを実行しました。

## BlaBooとは?
BlaBoo(ブラブー)は英語の```blah blah(ブラブラ)```の単語と赤ちゃんが良く出す```boo(ブー)```の単語を合わせた意味で、赤ちゃん/子供向けの単語アプリです。

- BlaBoo紹介ページ: [BlaBoo]( https://dev-yakuza.github.io/app/blaboo/){:target="_blank"}

下記はBlaBooアプリのダウンロードリンクです。

- ダウンロード: [アップルアプリストア](https://itunes.apple.com/jp/app/blaboo/id1441741187){:rel="nofollow noreferrer" target="_blank"}
- ダウンロード: [グーグルアプリストア](https://play.google.com/store/apps/details?id=io.github.dev.yakuza.blaboo){:rel="nofollow noreferrer" target="_blank"}

赤ちゃん/子供がイラストを見てそのイラストをタッチしたら音声でその単語を読んでくれるとてもシンプルなアプリです。

![赤ちゃん/子供用単語勉強アプリBlaBoo開発日誌](/assets/images/category/blaboo/development-journal/app_concept.png)

## なぜ作るようになったか？
実際赤ちゃん/子供向けの単語アプリは既にいっぱいあります。このアプリを作った主な目的は下記のようです。

1. 赤ちゃん/子供向けで多言語を勉強できる単語アプリを作る。
1. 今まで勉強したRN(React Naitve)でアプリを開発して正式リリースする。

外国に住んでいるので子供に外国語と母国語を教えたくて色々アプリを探したが、一つのアプリで多言語を勉強できる機能があるアプリがあまりありませんでした。問題も発見したしそれを解決する技術もあるから作ってみようと思って開発することにしました。

## アプリ企画
しかしアプリを自ら全て作ることは時間が十分ありませんでした。それでいった一旦赤ちゃん/子供向けのアプリをベンチマーキングして、MVP(Minimum Vaiable Product: 最小機能製品)を決めました。BlaBooのMVP(Minimum Vaiable Product: 最小機能製品)は下記のようです。

1. 単語のカテゴリー：カテゴリーを定義してその中に該当する単語を表示する。(ex> 車、果物、野菜)
1. 単語をイラストで表示する：単語をイラストで表示して赤ちゃん/子供に興味を誘発させる
1. イラスト選択すると単語の音声を提供：イラストをタッチしたら単語を音声で読んで赤ちゃん/子供が自然にイラストと単語を勉強できるようにする。
1. 多言語対応：多言語を対応して一つの単語を色んな国の言語で勉強できるようにする。

これでMVP(Minimum Vaiable Production: 最小機能製品)を定義して簡単なスケッチでアプリの動線を企画しました。

![赤ちゃん/子供用単語勉強アプリBlaBoo開発日誌 - スケッチ](/assets/images/category/blaboo/development-journal/hand_sketch.png)

スケッチテンプレートは下記のサイトでダウンロードしました。

- [http://sneakpeekit.com/](http://sneakpeekit.com/){:rel="nofollow noreferrer" target="_blank"}

一人でアプリを趣味で作るので企画がそんなすごくしょぼいですね。目標、ターゲット、ビジネスモデル。。。このようなものはいったん折っといておおよその機能とおおよそのスケッチをする程度だけしました。だけど、それなり仮説も立てて、することも一覧で出したり頑張りましたが、これを企画と呼べるかはちょっと恥ずかしですね。

![赤ちゃん/子供用単語勉強アプリBlaBoo開発日誌 - 企画](/assets/images/category/blaboo/development-journal/plan_trello.png)

## アプリデザイン
上で企画した内容をベースで基本的なデザインをしました。やはりデザイン専門家ではないのでデザインがそんなにきれいではないです。それでもデザインを通じてアプリの基本的な色やコンセプトなどを具体化ができました。

基本デザインは[sketchapp](https://www.sketchapp.com/){:rel="nofollow noreferrer" target="_blank"}を使って簡単なデザインをしてイラストは[freepik](https://www.freepik.com/){:rel="nofollow noreferrer" target="_blank"}と言うサイトでダウンロードしました。

![赤ちゃん/子供用単語勉強アプリBlaBoo開発日誌 - デザイン](/assets/images/category/blaboo/development-journal/sketch_design.png)

## アプリ開発
開発はRN(React Native)を使いました。開発者一人でiOS/Androidを同時に開発ができるしjavascriptなので参入障壁もswiftやkotlinより高くありませんでした。BlaBooは基本的RN(```React Native```)とタイプスクリプト(```typescript```)を使ってます。

- RN(React Native)のインストール方法：[RNインストール]({{site.url}}/react-native/installation/){:target="_blank"}
- RN(React Native)にtypescriptを適用する: [typescript]({{site.url}}/react-native/typescript/){:target="_blank"}

また、RN(React Native)の基本UIは```NativeBase```をスタイルは```styled-components```を使ってました。

- RN(React Native)にNativeBaseを適用する：[nativebase]({{site.url}}/react-native/nativebase/){:target="_blank"}
- RN(React Navtive)でstyled-componentsを使う：[styled-components]({{site.url}}/react-native/styled-components/){:target="_blank"}

RN(React Native)は基本的ナビゲーションシステムがありません。BlaBooは```react-navigation```を使ってナビゲーションシステムを実装しました。

- react-navigationの使い方：[react-navigation]({{site.url}}/react-native/react-navigation/){:target="_blank"}

MVP(Minimum Vaiable Product：最小機能製品)の機能中一つである音声機能は```react-native-tts```を使って```tts(Text To Speech)```の機能を実行しました。

- react-native-ttsの使い方：[react-native-tts]({{site.url}}/react-native/react-native-tts/){:target="_blank"}

また、ユーザーの端末の地域情報を使ってアプリと```react-native-tts```の基本言語を設定しています。ユーザーの端末情報を取得するため```react-native-device-info```を使ってます。

- react-native-device-infoの使い方：[react-native-device-info]({{site.url}}/react-native/react-native-device-info/){:target="_blank"}

そしてイラストをタッチするとイラストが動くアニメーションがありますが、```react-native-animatable```を使って実装しました。

- react-native-animatableの使い方: [react-native-animatable]({{site.url}}/react-native/react-native-animatable/){:target="_blank"}

最後にアプリの広告や分析のためあグーグルのファイアベース(Google Firebase)とグーグルのアドモブ(Google Admob)を使ってます。このアプリの実装のため```react-native-firebase```を使ってます。

- react-native-firebase admobの使い方: [react-native-firebase-admob]({{site.url}}/react-native/react-native-firebase-admob/){:target="_blank"}
- react-native-firebase analyticsの使い方: [react-native-firebase-analytics]({{site.url}}/react-native/react-native-firebase-analytics/){:target="_blank"}

こうやってまとめたらほとんどオープンソースを持って来て実装しただけであまりやったものがないに見えますね。素敵なオープンソースを作ってくれてありがとうございます。素敵なオープンソースでメインの機能を開発してRN(React Native)を使って再利用可能なコンポーネント(Component)を使って開発は容易に進めました。ただ、画面へ表示するイラストや音声のための単語をまとめる作業がもっと時間がかかりました。

![赤ちゃん/子供用単語勉強アプリBlaBoo開発日誌 - リソースコード](/assets/images/category/blaboo/development-journal/resource.png)

## アプリ登録
これでBlabooのMVP(Minimun Vaiable Product：最小機能製品)が完成させました。開発が終わったらすぐアプリを登録してダウンロードできると思いましたが、アプリの登録手続きにも結構時間がかかりました。

アップルのアプリ審査(App Review)が結構時間がかかることは事前に知っていましたのでまずiOSアプリを登録してiOSのアプリ登録が完了した時点でアンドロイドの登録手続きを進めました。アップルのアプリ登録は2ヶ月以上かかてアンドロイドは2日かかりました。

アップルはやはり色んな理由でアプリ審査がリジェクト(App Review reject)が多くて時間がかかりました。アンドロイドは赤ちゃん/子供向けのアプリだけど```Designed for Families program```を選択しなかったので一回リジェクト(Reject)されました。

![赤ちゃん/子供用単語勉強アプリBlaBoo開発日誌 - グーグルのアプリ審査リジェクト](/assets/images/category/blaboo/development-journal/google_reject.png)

アプリを登録するためにはアップル開発者プログラム(Apple Developer Program)登録とアンドロイド開発者登録(Google Play Developer)が必要です。

- アップル開発者プログラム登録方法：[iOS開発者登録]({{site.url}}/react-native/ios-enroll-developer-program/){:target="_blank"}
- アンドロイド開発者(Google Play Developer)登録：[アンドロイド開発者登録]({{site.url}}/react-native/android-enroll-google-play-developer/){:target="_blank"}

また、アプリを登録する時色んな情報が必要でした。その情報を作成する時も考えたより時間がかかりました。

- iOSアプリ登録方法：[iOS App store登録]({{site.url}}/react-native/ios-app-store/){:target="_blank"}
- アンドロイドアプリ登録方法：[アンドロイドアプリストア登録]({{site.url}}/react-native/android-google-play/){:target="_blank"}

そしてやはり厳しなアップルのアプリ審査(App Review)。5回くらいアプリ審査(App Review)がリジェクト(Reject)されました。本当に登録をやめったくなりましたね。結局最後のリジェクト(Reject)の理由はアプリがユーザーと適切な相互作用がないからアップルのアプリストアにはいらないアプリですと言いました。

最初は腹立って企画する時ベンチマーキングしたアプリと比較してここよりカテゴリが多いです、ここより単語量が多いです、ここにはない多言語機能がありますとアピールしましたが、簡単に承認してくれませんでした。逆に私が考えて他のアプリがアプリストアの違反されると思ったら申告してくださいと言われました。。。他の開発者が頑張って作ったものをどうやって申告しますかね。。。それで結局最初企画したものとは全然別の機能を追加しました。

![赤ちゃん/子供用単語勉強アプリBlaBoo開発日誌 - 復習機能](/assets/images/category/blaboo/development-journal/add_card_mode.png)

カードタイプでカテゴリで勉強した単語を復習する機能を追加しました。20枚のカードがランダムで表示されてそのカードを左や右に渡し復習する機能です。

最初企画にはなかったもので緊急にアプリ審査(App Review)の承認のため一日でデザインして1日で機能を作ってので前のアプリ機能と合わんない気持ちがあります。今までも一つのアプリに二つのアプリが入ってる気持ちです。だけど、この機能を追加して無事にアプリ審査(App Review)を通過することができました。

最初はアップルのアプリ審査(App Review)が厳しすぎるじゃないと思いましたが、この審査があるおかげでiOSのアプリのUI/UXが用意かなと思いました。また、アップルのアプリ審査(App Reivew)の経験で次のアプリはもっとユーザを考えて作ると思いました。アプルのアプリ審査者(Apple App Reviewer)様だちに本当にありがとございます。

- ダウンロード: [アップルアプリストア](https://itunes.apple.com/jp/app/blaboo/id1441741187){:rel="nofollow noreferrer" target="_blank"}
- ダウンロード: [グーグルアプリストア](https://play.google.com/store/apps/details?id=io.github.dev.yakuza.blaboo){:rel="nofollow noreferrer" target="_blank"}


## アプリの開発の振り返え
色んなことがありましたが、無地に最初のアプリをリリースしました。しょぼいアプリかもしれないですが、このアプリはユーザーをたくさん増えさせて広告の収入を狙えうより自分自身が使うため、それと今まで勉強したRN(React Native)を活用してアプリの登録手続きを確認するため開発しました。

振り返えてみたら、開発よりデザイン、特にイラストをまとめった時間が結構かかりました。開発は一週間ぐらいかな。。。やはりRN(React Native)の開発パフォーマンスを確認しました。(オープンソース開発者たちに心から感謝します。)

アップルの厳しアプリ審査(App Review).そのせいで急なアプリコンセプトの変更、しかしそれのおかげでもっとユーザを考えて開発すると思う心構えを持ってるようになりました。もう一度アップルの審査者(App Review)様に感謝します。

BlaBooで検証したかった無料リソスでアプリの開発が出来る仮説は検証できました。皆さんも無料リソスを活用してアプリを開発してみてください。

## 最後に
やはり```TTS(Text To Speech)```の音声は抵抗感がありました。そして読み間違い時もありました。韓国語で```スパゲティ```は発音できなかったので```パスタ```で変更しました。もし声を寄付してくれう方がいったら大歓迎です。([Contact Us](https://dev-yakuza.github.io/contact/){:target="_blank"})

イラストも無料イラストを使ったので一つのスタイルになってないです。やはり、これも寄付してくれる方がいったら大歓迎です。([Contact Us](https://dev-yakuza.github.io/contact/){:target="_blank"})

多言語は日本語、英語、韓国語を基本提供しましたが、中国とイタリアでアプリダウンロードがあって中国ごとイタリア語を追加しました。しかし中国語、イタリア語はできないので翻訳機を使いました。間違ってる中国、イタリア語があったら、フィドバックお願いします。また、他の言語を寄付してくれる方がいったら大歓迎です。([Contact Us](https://dev-yakuza.github.io/contact/){:target="_blank"})

- ダウンロード: [アップルアプリストア](https://itunes.apple.com/jp/app/blaboo/id1441741187){:rel="nofollow noreferrer" target="_blank"}
- ダウンロード: [グーグルアプリストア](https://play.google.com/store/apps/details?id=io.github.dev.yakuza.blaboo){:rel="nofollow noreferrer" target="_blank"}