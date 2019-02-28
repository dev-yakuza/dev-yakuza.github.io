---
layout: 'post'
permalink: '/blaboo/update-review/'
paginate_path: '/blaboo/:num/update-review/'
lang: 'ja'
categories: 'blaboo'
comments: true

title: 'BlaBooアップデート後期'
description: 'RN(React Native)を使ってBlaBooと言うアプリを作ってリリースしました。アプリをリリースした後BlaBooはどうんなアップデートをしてるかについて説明します。'
image: '/assets/images/category/blaboo/update-review/app_concept.png'
---


## 概要
RN(React Native)を使ってBlaBooと言うアプリを作成してリリースしました。このブログではアプリをリリースした後BlaBooをどんな感じで管理やアップデートしてるかについて話してみようかともいます。BlaBooをもう一度紹介して本格的な話をしてみます。


## BlaBooとは?
BlaBoo(ブラブー)は英語の```blah blah(ブラブラ)```の単語と赤ちゃんが良く出す```boo(ブー)```の単語を合わせた意味で、赤ちゃん/子供向けの単語アプリです。

- BlaBoo紹介ページ: [BlaBoo]( https://dev-yakuza.github.io/app/blaboo/){:target="_blank"}

下記はBlaBooアプリのダウンロードリンクです。

<div class="download_link_container">
    <a class="download_link_ios" href="https://itunes.apple.com/app/blaboo/id1441741187" target="_blank">
        <img src="/assets/images/apple_download.png" alt="子供向け単語勉強アプリblaboo iOSダウンロード"/>
    </a>
    <a class="download_link_android" href="https://play.google.com/store/apps/details?id=io.github.dev.yakuza.blaboo" target="_blank">
        <img src="/assets/images/google play_download.png" alt="子供向け単語勉強アプリblabooアンドロイドダウンロード"/>
    </a>
</div>

赤ちゃん/子供がイラストを見てそのイラストをタッチしたら音声でその単語を読んでくれるとてもシンプルなアプリです。

![赤ちゃん/子供用単語勉強アプリBlaBoo開発日誌](/assets/images/category/blaboo/development-journal/app_concept.png)

アプリ開発について詳しく内容は以前のブログを参考してください。

- [BlaBooアプリ開発日誌(RN, React Native)]({{site.url}}/react-native/development-journal/){:target="_blank"}


## アプリ管理
最初にBlaBooアプリを企画する時はアプリが本当に簡単なので管理しなくてもいいと思いました。一回作ってリリースしたら、必要な方々がダウンロードしたり、消したりすると思って開発しました。

しかし、アプリをリリースして人たちがダウンロードすることを見たら最初の考えとは違ってしきりに手が行くようになりました。

![子供向け単語勉強アプリBlaBoo開発日誌](/assets/images/category/blaboo/update-review/blaboo_analytics.png)


## アップデート
BlaBooは最初は英語、日本語、韓国語だけ対応してリリースしましたが。一旦自分の目で確認できる言語だけ対象にしたのでコアー機能である単語の音声発音の機能には特に問題ないと思いました。

しかしアプリをリリースした後初ダウンロードは中国から発生して、急いでグーグル翻訳機を使って中国語に翻訳して初アップデートをしました。

- [中国語広報サイト](https://dev-yakuza.github.io/app/blaboo/zh/){:target="_blank"}

![BlaBooアップデート戦略 - 中国語](/assets/images/category/blaboo/update-review/blaboo_zh.png)

グーグル翻訳なので単語を正しく翻訳したかサイトを正しく翻訳したか分からないです。幸いタイワンの友達がいてアプリを少しテストして貰いましたけど、単語は大体合ってるの話があってちょっと安心しましが、その友達も全ての単語を見たわけではないのでまだ心配は残ってます。

それでも少し間違った単語があっても自国語を対応してることがもっと魅力的であるじゃないかなと思ってそれからダウンロードした国家を確認してダウンロードが発生した国家の言語でアプリとサイトを翻訳してアップデートを進めました。

このようにアップデートを進めましたが、ベトナム語を追加する時問題が発生しました。グーグル翻訳機を使って単語を翻訳した後テストをする時ベトナム語を正しく発音しない問題が発生しました。問題の原因を把握した結果、使っているライブラリがベトナム語を対応してないことでした。

BlaBooはTTS(Text To Speech)機能で下記のライブラリを使ってます。

- react-native-tts紹介: [react-native-tts]({{site.url}}/react-native/react-native-tts/){:target="_blank"}

このライブラリは対応してる言語ー国家が決めております。

```js
{language: "ar-SA", id: "com.apple.ttsbundle.Maged-compact", quality: 300, name: "Maged"}
{language: "cs-CZ", id: "com.apple.ttsbundle.Zuzana-compact", quality: 300, name: "Zuzana"}
{language: "da-DK", id: "com.apple.ttsbundle.Sara-compact", quality: 300, name: "Sara"}
{language: "de-DE", id: "com.apple.ttsbundle.Anna-compact", quality: 300, name: "Anna"}
{language: "el-GR", id: "com.apple.ttsbundle.Melina-compact", quality: 300, name: "Melina"}
{language: "en-AU", id: "com.apple.ttsbundle.Karen-compact", quality: 300, name: "Karen"}
{language: "en-GB", id: "com.apple.ttsbundle.Daniel-compact", quality: 300, name: "Daniel"}
{language: "en-IE", id: "com.apple.ttsbundle.Moira-compact", quality: 300, name: "Moira"}
{language: "en-US", id: "com.apple.ttsbundle.Samantha-compact", quality: 300, name: "Samantha"}
{language: "en-ZA", id: "com.apple.ttsbundle.Tessa-compact", quality: 300, name: "Tessa"}
{language: "es-ES", id: "com.apple.ttsbundle.Monica-compact", quality: 300, name: "Monica"}
{language: "es-MX", id: "com.apple.ttsbundle.Paulina-compact", quality: 300, name: "Paulina"}
{language: "fi-FI", id: "com.apple.ttsbundle.Satu-compact", quality: 300, name: "Satu"}
{language: "fr-CA", id: "com.apple.ttsbundle.Amelie-compact", quality: 300, name: "Amelie"}
{language: "fr-FR", id: "com.apple.ttsbundle.Thomas-compact", quality: 300, name: "Thomas"}
{language: "he-IL", id: "com.apple.ttsbundle.Carmit-compact", quality: 300, name: "Carmit"}
{language: "hi-IN", id: "com.apple.ttsbundle.Lekha-compact", quality: 300, name: "Lekha"}
{language: "hu-HU", id: "com.apple.ttsbundle.Mariska-compact", quality: 300, name: "Mariska"}
{language: "id-ID", id: "com.apple.ttsbundle.Damayanti-compact", quality: 300, name: "Damayanti"}
{language: "it-IT", id: "com.apple.ttsbundle.Alice-compact", quality: 300, name: "Alice"}
{language: "ja-JP", id: "com.apple.ttsbundle.Kyoko-compact", quality: 300, name: "Kyoko"}
{language: "ko-KR", id: "com.apple.ttsbundle.Yuna-compact", quality: 300, name: "Yuna"}
{language: "nl-BE", id: "com.apple.ttsbundle.Ellen-compact", quality: 300, name: "Ellen"}
{language: "nl-NL", id: "com.apple.ttsbundle.Xander-compact", quality: 300, name: "Xander"}
{language: "no-NO", id: "com.apple.ttsbundle.Nora-compact", quality: 300, name: "Nora"}
{language: "pl-PL", id: "com.apple.ttsbundle.Zosia-compact", quality: 300, name: "Zosia"}
{language: "pt-BR", id: "com.apple.ttsbundle.Luciana-compact", quality: 300, name: "Luciana"}
{language: "pt-PT", id: "com.apple.ttsbundle.Joana-compact", quality: 300, name: "Joana"}
{language: "ro-RO", id: "com.apple.ttsbundle.Ioana-compact", quality: 300, name: "Ioana"}
{language: "ru-RU", id: "com.apple.ttsbundle.Milena-compact", quality: 300, name: "Milena"}
{language: "sk-SK", id: "com.apple.ttsbundle.Laura-compact", quality: 300, name: "Laura"}
{language: "sv-SE", id: "com.apple.ttsbundle.Alva-compact", quality: 300, name: "Alva"}
{language: "th-TH", id: "com.apple.ttsbundle.Kanya-compact", quality: 300, name: "Kanya"}
{language: "tr-TR", id: "com.apple.ttsbundle.Yelda-compact", quality: 300, name: "Yelda"}
{language: "zh-CN", id: "com.apple.ttsbundle.Ting-Ting-compact", quality: 300, name: "Ting-Ting"}
{language: "zh-HK", id: "com.apple.ttsbundle.Sin-Ji-compact", quality: 300, name: "Sin-Ji"}
{language: "zh-TW", id: "com.apple.ttsbundle.Mei-Jia-compact", quality: 300, name: "Mei-Jia"}
```

私は言語ー国家コードを下記のサイトで確認してます。

- [https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html){:rel="nofollow noreferrer" target="_blank"}

このサイトでベトナム語ーベトナムを探したら```vi-VN```であることを確認できますし、この言語ー国家コードが上のリストにはないことが分かります。```git checkout .```で1時間くらいの作業内容を戻した涙が出る経験をしました。

この後、ダウンロードした国家を確認してダウンロードした国家が今まで追加したことない国家かどうか確認して言語ー国家コードを確認して```react-native-tts```が対応してる言語か確認することになりました。


## アンドロイドバグ
アプリをリリースした後、特に問題ありませんでした。私はアイホンユーザなのでアンドロイドについてあまり気にしませんでした。ところで、友達がアンドロイドでボタンが押せない問題があるとフィードバックをくれました。多分この友達がこのバグを見つけてくれなかったら永遠にクズなアプリでアンドロイドマーケットに残ってあったと思います。

BlaBooではイラストが登場する時、バウンスイン(bounceIn)アニメーションを ```react-native-animatable```と言うライブラリを使って実装してます。

- react-native-animatable使い方: [react-native-animatable]({{site.url}}/react-native/react-native-animatable/){:target="_blank"}

BlaBooアプリで一つのビューでイメージリストを```map```を使って表示してます。ページが変わったらこのイメージリストを更新して新イメージを表示しています。

```js
{pageData.things.map((lineData: Array<IThing>, lineIndex: number) =>
    lineData.map((item: IThing, index: number) => (
        <Animatable.View
            key={`${pageIndex}-${lineIndex}-${index}`}
            animation="bounceIn"
            delay={(index + 2) * 100}
            useNativeDriver={true}>
                <Thing
                    row={item.row}
                    column={item.column}
                    width={this._calculateWidth(pageData.lines[lineIndex])}
                    height={thingHeight}
                    marginRow={item.marginRow}
                    marginColumn={item.marginColumn}
                    src={item.src}
                    locale={locale}
                    text={item[locale]}
                />
        </Animatable.View>
    ))
)}
```

ところで、アンドロイドでこのイメージを更新したら、以前の```Animatable.View```がビューに残って、新イメージの上に表示していました。```react-native-animatable```はアニメーションのパフォーマンス(Performance)のためNative Driverを使えるように```useNativeDriver```オプションを提供しています。上のソースを見たら分かりますが、もちろん、私もパフォーマンスのためこのオプションを使いました。

正確な原因は分かりませんが、このオプションを消したら正確に動作しました。しかし、正確な原因を知らない状態で、すでにリリースした状態でビッグイシューでしたので、```Animatable.View```を削除してアップデートしました。登場アニメーションがなくなってちょっと残念でしたが、明確な原因を知らないでこの機能を使うことはリスクが高いので完全に削除することにしました。もし同じ問題を経験して原因を把握している方がいたら共有してくれたら嬉しいですね。


## アップデート後期
今のアップデートは下記のように単純なプロセスで進めています。

1. ダウンロードが発生した国家を確認
1. すでに翻訳してある国家のか確認
1. 翻訳してない国家の場合言語ー国家コードを確認
1. 言語ー国家コードがライブラリ(```react-native-tts```)から対応してるかどうか確認
1. ライブラリ(```react-native-tts```)が言語ー国家コードを対応してる場合、アプリ、ウェブ、アプリストアーを翻訳
1. テスト
1. iOS、アンドロイドリリース

簡単に見えるかもしれないですが、色々失敗して作ったプロセスです。皆さんもし```react-native-tts```ライブラリを使って多言語を対応するアプリを企画・開発する予定であったらライブラリが対応してる言語を確認することをお勧めします。

今まで初リリース後、アップデートした内容は下記のようです。

1. Splashスクリーンを強制的に1秒間維持して後アプリを起動(使ったライブラリ: [react-native-splash-screen]({{site.url}}/react-native/react-native-splash-screen/){:target="_blank"})
1. アプリのレビューに数字をもっと追加して欲しいのリクエストがあって数字のコンテンツをもっと追加
1. アプリの最初の画面で何を押せばいいか分からないテスターがいて、```start```ボタンにアニメーションを追加して動作を誘導
1. 中国語、イタリア語、ヒンディー語、オランダ語、タイワン語、ドイツ語を追加
1. アプリのレビューを作成するように誘導(使ったライブラリ: [react-native-rate]({{site.url}}/react-native/react-native-rate/){:target="_blank"})
1. タブレット対応
1. バグ修正

アプリダウンロードリンク

<div class="download_link_container">
    <a class="download_link_ios" href="https://itunes.apple.com/app/blaboo/id1441741187" target="_blank">
        <img src="/assets/images/apple_download.png" alt="子供向け単語勉強アプリblaboo iOSダウンロード"/>
    </a>
    <a class="download_link_android" href="https://play.google.com/store/apps/details?id=io.github.dev.yakuza.blaboo" target="_blank">
        <img src="/assets/images/google play_download.png" alt="子供向け単語勉強アプリblabooアンドロイドダウンロード"/>
    </a>
</div>

## 結論
本当はこのブログを書いた一番大きな理由は皆さんの力を借りたいのであります。上でも話しましたが、英語、日本語、韓国語以外はグーグル翻訳を使って翻訳をしました。ウェブやアプリストアーの内容は少し違っても特に問題ないと思いますが、BlaBooアプリは子供や外国語を勉強したい人たちをターゲットにしてるのでアプリ中の単語は間違ったら不味いじゃないかなと思います。しかし、私が全世界の言語を知るわけないし、お金がいっぱいあるわけないので全ての言語を正しく翻訳する状況ではないのでこのように記事を書いています。

もし外国語が得意な方々がいらっしゃったら下記のリポジトリ(Repository)を見て修正してくれたらいいかなと思って、このようにお願いをしてます。

- github: [https://github.com/dev-yakuza/blaboo-translate](https://github.com/dev-yakuza/blaboo-translate){:target="_blank"})

皆さんの助けが一人の開発者に大きな希望であり、たくさんのユーザが正しい単語を勉強できるようにしてくれると思います。