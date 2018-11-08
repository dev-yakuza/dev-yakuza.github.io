---
layout: 'post'
permalink: '/jekyll/send-email/'
paginate_path: '/jekyll/:num/send-email/'
lang: 'ja'
categories: 'jekyll'
comments: true

title: 'メール送信機能'
description: 'jekyllプロジェクトへformspreeサービスを利用してメール発送機能を追加して見ましょう。'
image: '/assets/images/category/jekyll/send-email.jpg'
---

## 概要
私たちは[github page](https://pages.github.com/){:rel="nofollow noreferrer" :target="_blank"}でブログをサービスしています。jekyllで生成したStaticファイル（html, css, javascript）をgithub pageへアップロードすることでブログをサービスしてます。つまり、サーバーソースの生成や活用してないことです。そのため、一般的にサーバーを通じてメールを送信する簡単な機能もgithubとjekyllを使って作ったサイトでは利用することが不可能です。

[formspreeサービス](https://formspree.io/){:rel="nofollow noreferrer" :target="_blank"}はこのようなStaticページにメール送信機能を無料で使えるように助けてくれるサービスです。このブログポストではformspreeを使ってjekyllでメールを送信する機能を作る方法を紹介します。

## formspreeサービス
formspreeサービスは会員登録しなくても無料で使うことが出来ます。下記のリンクを押してサービスサイトに移動しましょう。
- formspreeサービス: [https://formspree.io/](https://formspree.io/){:rel="nofollow noreferrer" :target="_blank"}

## formspreeサービスを使う
formspreeサービスサイトへ移動したら下の画面が見ます。
![formspree service site](/assets/images/category/jekyll/formspree/homepage.png)

左上の```Try Formspree!```を押します。

![formspree test site](/assets/images/category/jekyll/formspree/test-site.png)

上の画面で```Edit your form here```の部分を修正して実際自分が使うフォームを作成します。

```html
<form method="POST" action="https://formspree.io/YOUREMAILHERE">
```
actionの部分に送信して貰うメールアドレスを入れます。

```html
<form method="POST" action="https://formspree.io/dev.yakuza@gmail.com">
```

そして、右の```Test it here```を通じて実際メールを送信して見ます。

メールを送信した後、formへ入れったメールが実際自分のメールがどうか確認するメールがformspreeから確認メールがきます。メールを開いて自分のメールことを証明します。

formspreeサービスを通じてメール送信機能をjekyllへ入れる準備が終わりました。

## jekyllへformspree 適用する
上記で生成したhtml formソースをコピして```_layout/contact.html```へ入れます。テーマによってレイアウトファイルが違うかもしれないです。下記のコードは実際、私たちが使ってるソースです。

{% include_relative common/email_form.md %}

```html
action="https://formspree.io/{{ site.email }}"
```

formのactionへ```_config.yml```に設定したメールを使うようにします。

```html
<input type="text" name="_gotcha" style="display:none" />
```

上のコードでメールを送信する時、```CAPTCHA```を表示するように設定します。

```html
<input type="hidden" name="_subject" value="블로그에서 새로운 연락이 왔습니다." />
```

メールのタイトルを設定します。

## 完了
全ての設定が終わりました。実際サイトでメールを送信して確認してください。

## 参考
- 公式サイト: [formspreeサービス](https://formspree.io/){:rel="nofollow noreferrer" :target="_blank"}