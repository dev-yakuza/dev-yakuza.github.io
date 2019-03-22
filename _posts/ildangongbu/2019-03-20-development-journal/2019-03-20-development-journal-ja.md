---
layout: 'post'
permalink: '/ildangongbu/development-journal/'
paginate_path: '/ildangongbu/:num/development-journal/'
lang: 'ja'
categories: 'ildangongbu'
comments: true

title: '「일단공부(イルタンコンブ)」アプリ開発日誌(RN, React Native)'
description: 'RN(React Native)を使って「일단공부(イルタンコンブ)」と言うJLPT日本語単語勉強アプリを開発してみました。このアプリを開発した時のエピソードをまとめてみました。'
image: '/assets/images/category/ildangongbu/background.png'
---

## 概要
RN(React Native)を使って開発したアプリがもう3番目ですね。下記は以前のアプリを作る時作成した開発日誌です。以前のアプリが気になる方は下記のリンクをクリックして確認してください。

- [BlaBooアプリ開発日誌(RN, React Native)]({{site.url}}/blaboo/development-journal/){:target="_blank"}
- [Kumonchoアプリ開発日誌(RN, React Native)]({{site.url}}/kumoncho/development-journal/){:target="_blank"}

このアプリは韓国人向けの日本語単語アプリですのでアプリダウンロードしても無駄になると思いますので、この記事だけ面白く見て貰ったら嬉しいです。


## 일단공부(イルタンコンブ)とは?
JLPT日本語単語をレベル別で勉強が出来るし、毎日勉強出来る量と復習昨日で単語の勉強をサポートするアプリです。

- 일단공부(イルタンコンブ)の紹介ページ: [일단공부(イルタンコンブ)](https://dev-yakuza.github.io/app/ildangongbu/){:target="_blank"}

下はアプリダウンロードリンクです。

<div class="download_link_container">
    <a class="download_link_ios" href="https://itunes.apple.com/app/id1456091125" target="_blank">
        <img src="/assets/images/apple_download.png" alt="JLPT日本語単語アプリ、일단공부(イルタンコンブ)iosダウンロード"/>
    </a>
    <a class="download_link_android" href="https://play.google.com/store/apps/details?id=io.github.dev.yakuza.ildangongbu" target="_blank">
        <img src="/assets/images/google play_download.png" alt="JLPT日本語単語アプリ、일단공부(イルタンコンブ)アンドロイドダウンロード"/>
    </a>
</div>


## なぜ作るようになったか？
私は韓国人で日本で仕事してます。日本語の単語本を持って出勤する時勉強してますが、日本の出勤電車（地獄電車）で勉強することは結構大変でした。それと単語の本は単語と意味が一緒に表示されて、意識して意味を見ないようにするがちょこちょこ意味が見えるので実際単語の勉強がよくできなかったんです。最後は単語はやはり反復して見なきゃなので、復習したら本の前だけ勉強しじゃうんですね。この問題を解決して見ようかと思って簡単なJLPT単語アプリを作成することにしました。

![JLPT日本語単語アプリ、 일단공부(イルタンコンブ)](/assets/images/category/ildangongbu/background.png)


## アプリ企画
일단공부(イルタンコンブ)のMVP(Minimum Vaiable Product：最小機能製品)は下記となります。

1. JLPT日本語の単語をレベル別で見える。
1. 毎日勉強出来る量(15単語)で単語が見える。
1. 日本語の単語が意味が見ない状態でリストで見える。
1. 意味を見るボタンを押したら読み方(ひらがな/カタカナ)と意味が見える。
1. 読み方を選択すると発音が出る。
1. 勉強した単語をテストで復習出来る。
1. テストする時間違った単語をリストで表示する。
1. レベル別や全ての単語を復習出来る機能を追加する。
1. 復習機能に良く間違う単語をもっと見せるようにする。

このようにまとめたら、結構機能があるように見えますね。シンプルに作るようにしましたが、やはり自分が使い安いアプリを作りたくって色々機能が追加されました。本当はもっと機能を追加したかったけど、まずはMVP、 MVP!


## デザイン
は。。やっぱりデザインセンスはゼロです。。どのデザインがいいか色んなパータンを作って色んな色を入れて挑戦したが。。。まだ、デザインは難しいですね。

![JLPT日本語単語アプリ、일단공부(イルタンコンブ)のデザイン](/assets/images/category/ildangongbu/development-journal/ildangongbu-design.png)

デザインは`sketchapp`で作成しました。色んなデザインパータン中で一番シンプルのデザインを選択しました。また、要らない画面も無くして最終デザインは下記のようにしました。

![JLPT日本語単語アプリ、일단공부(イルタンコンブ)のデザイン](/assets/images/category/ildangongbu/development-journal/ildangongbu-final-design.png)

デザイナーさんリスペクトします。


## アプリ開発
開発はもちろん、RN(React Native)を使いました。일단공부(イルタンコンブ)は本的RN(```React Native```)とタイプスクリプト(```typescript```)を使ってます。

- RN(React Native)のインストール方法：[RNインストール]({{site.url}}/react-native/installation/){:target="_blank"}
- RN(React Native)にtypescriptを適用する: [typescript]({{site.url}}/react-native/typescript/){:target="_blank"}

また、RN(React Native)の基本UIは```NativeBase```をスタイルは```styled-components```を使ってました。

- RN(React Native)にNativeBaseを適用する：[nativebase]({{site.url}}/react-native/nativebase/){:target="_blank"}
- RN(React Navtive)でstyled-componentsを使う：[styled-components]({{site.url}}/react-native/styled-components/){:target="_blank"}

일단공부(イルタンコンブ)は基本ナビゲーションシステムで```react-navigation```を使ってます。

- react-navigationの使い方：[react-navigation]({{site.url}}/react-native/react-navigation/){:target="_blank"}

MVP(Minimum Vaiable Product：最小機能製品)の機能中一つである音声機能は```react-native-tts```を使って```tts(Text To Speech)```の機能を実行しました。

- react-native-ttsの使い方：[react-native-tts]({{site.url}}/react-native/react-native-tts/){:target="_blank"}

일단공부(イルタンコンブ)アプリ中で使う単語をsqliteに入れてアプリと一緒に配布してます。アプリでsqliteを使う方法は下のリンクを確認してください。

- react-native-sqlite-storage使う方法: [react-native-sqlite-storage]({{site.url}}/react-native/react-native-sqlite-storage/){:target="_blank"}

最後にアプリの広告や分析のためあグーグルのファイアベース(Google Firebase)とグーグルのアドモブ(Google Admob)を使ってます。このアプリの実装のため```react-native-firebase```を使ってます。

- react-native-firebase admobの使い方: [react-native-firebase-admob]({{site.url}}/react-native/react-native-firebase-admob/){:target="_blank"}
- react-native-firebase analyticsの使い方: [react-native-firebase-analytics]({{site.url}}/react-native/react-native-firebase-analytics/){:target="_blank"}
- react-native-firebase Crasylyticsの使い方: [firebase-crashlytics]({{site.url}}/react-native/firebase-crashlytics/){:target="_blank"}


## 最後に
今回のアプリは単純に単語を見せるアプリです。やはりデザインで一番時間がかかりました。また、`react-native-sqlite-storage`がアンドロイドでパフォーマンス問題があるみたいです。ローカルからデータを読んでくるがサーバーで貰ってくる感じで時間がかかります。私の作りが悪かったかも。。。もう一度SQLをチューニングして見て出来なかったらライブラリのソースもちょっと見る必要があるかもしれないです。

韓国人向けなので。。。ダウンロードはお勧めしませんが。。。アプリをダウンロードして動きを確認してみたらどうでしょうかね。。。

<div class="download_link_container">
    <a class="download_link_ios" href="https://itunes.apple.com/app/id1456091125" target="_blank">
        <img src="/assets/images/apple_download.png" alt="JLPT日本語単語アプリ、일단공부(イルタンコンブ)iosダウンロード"/>
    </a>
    <a class="download_link_android" href="https://play.google.com/store/apps/details?id=io.github.dev.yakuza.ildangongbu" target="_blank">
        <img src="/assets/images/google play_download.png" alt="JLPT日本語単語アプリ、일단공부(イルタンコンブ)アンドロイドダウンロード"/>
    </a>
</div>