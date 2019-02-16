---
layout: 'post'
permalink: '/kumoncho/development-journal/'
paginate_path: '/kumoncho/:num/development-journal/'
lang: 'ja'
categories: 'kumoncho'
comments: true

title: 'Kumonchoアプリ開発日誌(RN, React Native)'
description: 'RN(React Native)を使ってくもんちょ(Kumoncho)と言う子供向け絵本アプリを作りました。このアプリを開発した時のエピソードをまとめてみました。'
image: '/assets/images/category/kumoncho/background.png'
---

## 概要
以前のプロジェクトでは一人でRN(React Native)を使ってアプリを最初から最後まで作ってみました。今回は別の人と協業してプロジェクトを進めてたいので、以前のプロジェクトで一番時間が掛かったデザインを担当してくれる友達と一緒にプロジェクトを進めてみました。以前のプロジェクトが気になる方は下記のリンクを押して以前のプロジェクトを開発した時のエピソードをみてください。

- [BlaBooアプリ開発日誌(RN, React Native)]({{site.url}}/blaboo/development-journal/){:target="_blank"}


## くもんちょ(Kumoncho)とは?
くもんちょ(Kumoncho)は雲の国のイカロス王子と彼の雲の友達、くもんちょの友情と容器に関する子供向け絵本アプリです。

- Kumoncho紹介ページ: [Kumoncho]( https://dev-yakuza.github.io/app/kumoncho/ko/){:target="_blank"}

下記はアプリのダウンロードリンクです。

<div class="download_link_container">
    <a class="download_link_ios" href="https://itunes.apple.com/app/kumoncho/id1450902241" target="_blank">
        <img src="/assets/images/apple_download.png" alt="子供向け絵本アプリくもんちょiOSダウンロード"/>
    </a>
    <a class="download_link_android" href="https://play.google.com/store/apps/details?id=io.github.dev.yakuza.kumoncho" target="_blank">
        <img src="/assets/images/google play_download.png" alt="子供向け絵本アプリくもんちょアンドロイドダウンロード"/>
    </a>
</div>


## なぜ作るようになったか？
以前のプロジェクトは一人でRN(React Native)でアプリを最初から最後まで開発することを中心にしました。

- [BlaBooアプリ開発日誌(RN, React Native)]({{site.url}}/blaboo/development-journal/){:target="_blank"}

それで今回のプロジェクトは他の人と協業することを焦点にしたかったです。また、以前のプロジェクトで一番時間が掛かったデザインの部分を協業で時間を短縮してもっと早くアプリを作成したかったです。

最後は、漫画家になりたかったけど、その夢を達成できなくってデザイナで仕事してる友達が一人いました。けれど、その才能がもったいないと思ってこのプロジェクトに誘いました。漫画家は数万ページ、数万ストーリーを作らなければならないですが、子供向け絵本は短いテーマで作れるので今の業務をしながら、趣味で作れるじゃない？と言えながら一緒に作ってみようと説得しました。

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/kumoncho/development-journal/profile_shu.png" alt="子供向け絵本作者shuプロフィール">
</div>

- Shu: <a href="mailto:meiki.shuzou@gmail.com">meiki.shuzou@gmail.com</a>


幸いに一緒に作ることになって、この友達が絵とストーリーを、私がプロジェクトのディレクティングと開発を担当して進めることになりました。

このプロジェクトをはじめ、この友達とは続けて子供向けの絵本アプリを作成する予定であり、絵本を出版することを最終目標として設定しました。くもんちょをリリースしながら、既に2番目の子供向け絵本アプリを準備しています。

お互いに仕事してる会社が違うので、フィードバックは主にラインのメッセージでやりとりで、必要な時ランチでテレビ会議をしました。担当してるパートが重ならなくはっきり分かれてるので、協業には大きな問題なく進めることができました。


## アプリの企画
今回のプロジェクトは子供向け絵本アプリですが、作者の友達は絵本のストーリーや絵を書いたことがないし、私も絵本アプリを作ったことなかったです。それで一旦資料調査をはじめました。

最終目標は絵本の出版なので現在の子供向け絵本の基準を調査しました。

子供向け絵本は16、24、48ページの本がありますが、32ページが業界標準です。(もし間違ったらコメントください。)

![子供向け絵本32ページ](/assets/images/category/kumoncho/development-journal/picture_book.jpg)
(写真の出所: [https://taralazar.com](https://taralazar.com/2009/02/22/picture-book-construction-know-your-layout/){:rel="nofollow noreferrer" target="_blank"})

また、私たちは出版する本(本当に出版できるか分からないけど)とアプリの違いを作って、アプリを既に見た方も本を購買出来るように企画しました。それで結論出したページが9ページ。あまり長くも短くもないページを設定しました。(絵本の出版は32ページを想定しています。)

これでページを決定したら作者の友達は簡単にストーリーとイラストのレイアウトを構成することができました。


## ストーリーとイラスト
作者の友達と私は子供向け絵本アプリは初めて作るので、最初のストーリーは無難なストーリーで決定しました。アプリをダウンロードして内容を見たら分かると思いますが、どこかで見た気がする、どこかにある気がする内容を初ストーリーで決定しました。

<div class="download_link_container">
    <a class="download_link_ios" href="https://itunes.apple.com/app/kumoncho/id1450902241" target="_blank">
        <img src="/assets/images/apple_download.png" alt="子供向け絵本アプリくもんちょiOSダウンロード"/>
    </a>
    <a class="download_link_android" href="https://play.google.com/store/apps/details?id=io.github.dev.yakuza.kumoncho" target="_blank">
        <img src="/assets/images/google play_download.png" alt="子供向け絵本アプリくもんちょアンドロイドダウンロード"/>
    </a>
</div>

ストーリーが決まると、作者の友達はスケッチで人物と背景を躯体化しました。

![くもんちょスケッチ](/assets/images/category/kumoncho/development-journal/sketch.png)

そしてストーリーを磨き、そのストーリーと合わせてイラストを描き出しました。

![くもんちょイラスト](/assets/images/category/kumoncho/development-journal/illustration.png)

私の友達だからではなく、本当に絵とストーリーには才能があるのではないかなと思います。


## アプリ開発
アプリ開発はもちろんRN(React Native)を使いました。くもんちょは基本的RN(```React Native```)とタイプスクリプト(```typescript```)を使ってます。

- RN(React Native)インストール方法: [RNインストール]({{site.url}}/react-native/installation/){:target="_blank"}
- RN(React Native)にtypescriptタイプスクリプト適用: [typescript]({{site.url}}/react-native/typescript/){:target="_blank"}

また、RN(React Native)の基本スタイルは```styled-components```を使いました。

- RN(React Navtive)でstyled-components使い方: [styled-components]({{site.url}}/react-native/styled-components/){:target="_blank"}

ページの背景には```react-native-linear-gradient```を使ってグラデーションの効果を入れました。

- RN(React Navtive)でグラデーション(Gradient)を使う方法: [react-native-linear-gradient]({{site.url}}/react-native/react-native-linear-gradient/){:target="_blank"}

初めて開発した時は、ページ転換を下記のようにスクロールを使いました。

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/kumoncho/development-journal/kumoncho_scroll.gif" alt="子供向け絵本くもんちょスクロール">
</div>

しかし、自然なページ転換を演出したくて[react-native-linear-gradient]({{site.url}}/react-native/react-native-linear-gradient/){:target="_blank"}で紹介したグラデーションのアニメーションを適用して背景を変更しました。それと[react-native-animatable]({{site.url}}/react-native/react-native-animatable/){:target="_blank"}のfadein/fadeoutでイメージの登場効果を入れました。

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/kumoncho/development-journal/kumoncho_swipe.gif" alt="子供向け絵本くもんちょスワイプ">
</div>

ページの転換にはユーザのスワイプのイベントを検知するようにしました。

- RN(React Native)でスワイプ検知: [react-native-swipe-gestures]({{site.url}}/react-native/react-native-swipe-gestures/){:target="_blank"}

最後にはアプリの広告と分析のためグーグルのファイアベース(Google Firevase)とグーグルアドモブ(Google Admob)を使ってます。これを実装するため```react-native-firebase```を使ってます。

- react-native-firebase admobの使い方: [react-native-firebase-admob]({{site.url}}/react-native/react-native-firebase-admob/){:target="_blank"}
- react-native-firebase analyticsの使い方: [react-native-firebase-analytics]({{site.url}}/react-native/react-native-firebase-analytics/){:target="_blank"}
- react-native-firebase Crashlyticsの使い方: [firebase-crashlytics]({{site.url}}/react-native/firebase-crashlytics/){:target="_blank"}

下記のリストは付加的な機能を実装するため使ったライブラリです。

- RN(React Native)でメール発信: [react-native-mail]({{site.url}}/react-native/react-native-mail/){:target="_blank"}
- RN(React Native)でレビュー案内: [react-native-rate]({{site.url}}/react-native/react-native-rate/){:target="_blank"}
- RN(React Native)でsplashイメージコントロール: [react-native-splash-screen]({{site.url}}/react-native/react-native-splash-screen/){:target="_blank"}
- RN(React Native)でTTS(Text To Speech)を使う方法: [react-native-tts]({{site.url}}/react-native/react-native-tts/){:target="_blank"}


## アプリ登録
以前のプロジェクトではアプリ登録する時結構大変でした。([BlaBooアプリ開発日誌(RN, React Native)]({{site.url}}/blaboo/development-journal/){:target="_blank"}) その時の経験のお陰で、今回のプロジェクトのアプリ登録は問題なく進めることができました。

iOSは子供のカテゴリーを選べて登録を試しましたが、アプリ中に外部リンクがあって審査はリジェクト(Reject)されました。子供のカテゴリーの場合、Parental Gateの機能で外部リンクを保護する義務がありますが、私のアプリはこれを無視して問題になりました。Parental Gateに関していいライブラリを見つけれなかったので、子供のカテゴリーを放棄して登録申請をして登録しました。

<div class="download_link_container">
    <a class="download_link_ios" href="https://itunes.apple.com/app/kumoncho/id1450902241" target="_blank">
        <img src="/assets/images/apple_download.png" alt="子供向け絵本アプリくもんちょiOSダウンロード"/>
    </a>
    <a class="download_link_android" href="https://play.google.com/store/apps/details?id=io.github.dev.yakuza.kumoncho" target="_blank">
        <img src="/assets/images/google play_download.png" alt="子供向け絵本アプリくもんちょアンドロイドダウンロード"/>
    </a>
</div>


## 最後に
今回の子供向け絵本アプリプロジェクトは企画段階でもっとベンチマーキングと競争社(絵本)を分析するべきでした。私たちはページ数が決定された瞬間ストーリーとイラストに集中したので1ページへ入る内容、つまり文字数を決定しなかったミスをしました。```ストーリーとイラスト```セクションでイラストを見たと思いますが、最初のイラストには絵しかありませんでした。アプリを開発する段階でイラストに関する内容を伝えるため、あとで内容を入れました。そのせいで、イラストの求道とストーリーの伝達力が落ちる問題が発生しました。

また、絵本を基準にして作業したので、アプリで絵本を読む部分、つまりUXを深く考えなかったです。今も途中でアプリを終了してアプリを再起動した場合、いつも最初から全て見ないとダメです。中間ページに飛べる機能もないです。UXに関しては完全に失敗したプロジェクトと思います。

開発にも問題はありました。アプリをリリースした後、作者の友達からタブレットも対応して欲しい話がありました。RN(React Native)はそもそもクロスプラットフォームなので簡単に転換できると思いました。実際以前のプロジェクト([BlaBooアプリ開発日誌(RN, React Native)]({{site.url}}/blaboo/development-journal/){:target="_blank"})は簡単なアプリなので簡単に転換できました。しかし、今回のプロジェクトはイメージが多いし、そのイメージを設定する部分でタブレットを考慮しなくて設計したのでタブレットの転換に失敗しました。時間があったら設計を直してタブレットも対応する予定ですが最初からうまく作るべきでした。

<div class="download_link_container">
    <a class="download_link_ios" href="https://itunes.apple.com/app/kumoncho/id1450902241" target="_blank">
        <img src="/assets/images/apple_download.png" alt="子供向け絵本アプリくもんちょiOSダウンロード"/>
    </a>
    <a class="download_link_android" href="https://play.google.com/store/apps/details?id=io.github.dev.yakuza.kumoncho" target="_blank">
        <img src="/assets/images/google play_download.png" alt="子供向け絵本アプリくもんちょアンドロイドダウンロード"/>
    </a>
</div>

最後の最後ですが、出版業界いらっしゃる方中で私たちのアプリを絵本に出版したい方がいたら連絡してください！！

<a href="mailto:dev.yakuza@gmail.com">dev.yakuza@gmail.com</a>
