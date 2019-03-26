---
layout: 'post'
permalink: '/kumoncho/update-review/'
paginate_path: '/kumoncho/:num/update-review/'
lang: 'ja'
categories: 'kumoncho'
comments: true

title: 'Kumonchoアップデート後期(RN, React Native)'
description: 'RN(React Native)を使ってくもんちょ(Kumoncho)と言う絵本アプリを開発してリリースしました。アプリをリリースした後どうんなアップデートをしてるかについて説明します。'
image: '/assets/images/category/kumoncho/background.png'
---

## 概要
RN(React Native)を使ってKumoncho(くもんちょ)と言うアプリを開発してリリースしました。このブログではアプリをリリースした後、Kumonchoはどうんなアップデートをしてか説明します。Kumonchoアプリを開発した時の話は下記のアプリ開発日誌のブログを参考してください。

- [Kumonchoアプリ開発日誌(RN, React Native)]({{site.url}}/kumoncho/development-journal/){:target="_blank"}

本格的に話する前Kumonchoをもう一度簡単に説明します。


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

## 問題点
以前のブログでも説明しましたが、今回のプロジェクトはUXの観点で完全に失敗したプロジェクトです。下記のリンクでアプリ開発日誌で確認できます。

- Kumoncho紹介ページ: [Kumoncho]( https://dev-yakuza.github.io/app/kumoncho/ko/){:target="_blank"}

それで、今回のアップデートではUXを良くする部分に集中しました。また、開発する時タブレットを考えなく設計したのでタブレット対応に失敗しました。今回はリファクタリングをしてアプリがタブレットを対応できるように修正しました。

最後に作者の友達は現在マイクロインタラクション(Micro-interaction)専門家を目指しています。仕事でも使えるし、今回のアプリをもっと効果的に表現するためにアニメーションを追加しました。


## アプリアップデート
Kumoncho v2は下記のような機能を追加しました。

1. タブレット対応
1. アニメーション
1. ページ移動
1. チュートリアル
1. StatusBar

一つ一つ見てみましょう。


### タブレット対応
RN(React Native)はCross Platformを対応してるので、スマホやタブレットを対応するUniversal Appを簡単に作れます。もちろん画面のサイズが色々あるのでそれそれ画面に合せてコーディングする必要はあります。RN(React Native)は基本的に```flexbox```を使ってるので簡単にresponsiveアプリを作ることができます。

しかし、Kumonchoは子供向け絵本アプリです。それで全体の絵をレイヤー(Layer)で分けってその中にイメージを固定して表示しています。最初からタブレットを考えなかったので簡単にResponsiveアプリに展開ができませんでした。

![子供向け絵本アプリKumonchoレイヤー](/assets/images/category/kumoncho/update-review/kumoncho_layer.png)

Kumonchoは上のように背景レイヤー、メインイメージレイヤー、その他イメージレイヤー、説明(Description)レイヤーで分けって管理しています。このように分けったレイヤーを```object```で各ページを管理してReactのコンポーネントを使って簡単に実現しています。

```js
{
    key: 'page1',
    src: ...,
    description: {
        ja: [...],
        ko: [...],
        en: [...],
    },
    color: ...,
    background: [...],
    direction: {
        start: { ... },
        end: { ... },
    },
    width: ...,
    descriptionImage: ...,
    additionalImages: [
        {...},
        {...},
        {...},
        {...},
    ],
},
```

上の```object```は実際使ってるobjectの一部です。見えるようにタブレット(tablet)と関係あるものは一切存在していません。最初はReactコンポーネントでスマホかタブレットか区分してスタイルを適用してみようかと思いましたが根本的な問題の解決にはならないので```object```の部分をリファクタリングすることになりました。

```js
{
    key: 'page1',
    background: {
      color: [...],
      direction: {
        start: { ... },
        end: { ... },
      },
    },
    layers: [
      {
        data: ...,
        ...
        style: {
          phone: { ... },
          tablet: { ... },
        },
      },
      {
        images: [
          {
            src: ...,
            style: {
              phone: {...},
              tablet: {...},
            },
          },
          ...
        ],
      },
    ],
    description: {
      text: {
        ja: [...],
        ko: [...],
        en: [...],
      },
      color: ...,
      image: ...,
      style: {
        container: {
          phone: {...},
          tablet: {...},
        },
        label: {
          phone: {...},
          tablet: {...},
        },
      },
    },
},
```

このようにレイヤーをデータ(アニメーション)とイメージなどを対応するように作成して、スタイルもスマホやタブレットを分けって管理できるようにしました。また、以前は特定スタイル(widthやcolorなど)しか対応出来なかったが、今回のリファクタリングでどうんなスタイルも対応できるように修正しました。これでスマホと関係なくタブレットだけ集中して開発ができるようになりました。


### アニメーション
Kumonchoは子供向け絵本```アプリ```です。シダがって、一般的な紙の本では表現出来ない機能を提供することが出来ます。それの一つがアニメーションの機能です。ユーザ（子供）がもっと絵本を面白く見るようにマイクロインタラクションを入れて見ました。

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/kumoncho/update-review/kumoncho_animation.gif" alt="子供向け絵本アプリKumonchoアニメーション">
</div>

各ページにアニメーションを追加しました。それでもっと面白く絵本を見ることができましたのでぜひ一回見てください。アニメーションは`lottie`を使いました。これに関するブログが下記になります。

- [アフターエフェクト(AEF)]({{site.url}}//react-native/react-native-lottie/){:target="_blank"}


### ページ移動
以前のブログ([Kumonchoアプリ開発日誌(RN, React Native)]({{site.url}}/kumoncho/development-journal/){:target="_blank"})でも説明しましたが、今回のプロジェクトはUXの部分で失敗作です。アプリで絵本を見て途中でアプリを終了したら、また最初から絵本を見なければならないです。今回のアップデートではこの部分を解決して、ページ移動の機能を追加しました。

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/kumoncho/update-review/kumoncho_page_change.gif" alt="子供向け絵本アプリくもんちょスクロール">
</div>

画面をダブルタッチしたら、ページリストが見えてそこで見たいページを選べたらそこのページに移動する機能を追加しました。


### チュートリアル
現在は画面スワイプと画面ダブルタッチでページを移動しています。この部分をユーザがよく分からないかもしれないと思って、アプリを最初実行したらチュートリアル画面が見えるように追加しました。

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/kumoncho/update-review/kumoncho_tutorial.png" alt="子供向け絵本アプリくもんちょチュートリアル">
</div>


### StatusBar
iOSを中心にして開発してるのでアンドロイドをあまり気にしませんでした。iOSはStatusBarが透明なのでもんだいありませんでしたがアプリをリリースしてアンドロイドの方でStatusBarを透明にして欲しいの意見がありました。それでアンドロイドのStatusBarを透明にして、Splashが表示する時はStatusBarを非表示するように修正しました。下記のリンクはこれの説明ブログです。

- [StatusBarコントロール']({{site.url}}/react-native/react-native-status-bar/){:target="_blank"}


## 問題点
やはりアンドロイドで問題が発生します。シミュレーターでは特に問題ありませんでしたが実際デバイスでテストする時`OOM(Out Of Memory)`が発生してアプリがCrashする現象が出ました。デバッグして見たら`lottie`のアニメーション問題でした。

今使ってるアニメーションはPNGタイプのイメージを使ってます。このPNGタイプのイメージをコントロールする方式がiOSとアンドロイドで違うみたいです。現在、PNGのイメージをSVGに変換して適用して見ましたが特に問題なくアニメーションが表示してることを確認しました。

もし皆さんも`lottie`を使ってアニメーションを適用する要諦なったら、PNGのイメージを使わないようにすることをお勧めします。


## 結論
今回のアップデートで完全に失敗したUXの部分を少しよくなるように作ったと思います。また、アニメーションを使ってもっと面白く絵本を見るようにしました。今回作ったアプリをベースにして次の絵本アプリも作る要諦です。もっとこうして欲しいなとかの意見があったら、下にコメントください。
이번 업데이트를 통해 완전 실패했던 UX부분을 조금은 좋게 만들었다고 생각합니다. 또한 애니메이션을 통해 좀 더 재밌게 동화를 즐길 수 있도록 했습니다. 이번 기회를 통해 만든 앱을 베이스로 다음 그림 동화책 앱을 만들 예정입니다. 좀 더 추가했으면 좋겠다는 의견이 있으면 아래 댓글을 남겨주세요!

<div class="download_link_container">
    <a class="download_link_ios" href="https://itunes.apple.com/app/kumoncho/id1450902241" target="_blank">
        <img src="/assets/images/apple_download.png" alt="子供向け絵本アプリくもんちょiOSダウンロード"/>
    </a>
    <a class="download_link_android" href="https://play.google.com/store/apps/details?id=io.github.dev.yakuza.kumoncho" target="_blank">
        <img src="/assets/images/google play_download.png" alt="子供向け絵本アプリくもんちょアンドロイドダウンロード"/>
    </a>
</div>