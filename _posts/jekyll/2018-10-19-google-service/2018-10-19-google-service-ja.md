---
layout: 'post'
permalink: '/jekyll/google-service/'
paginate_path: '/jekyll/:num/google-service/'
lang: 'ja'
categories: 'jekyll'
comments: true

title: 'googleサービス'
description: 'google search console / analytics / adsenseを連動する方法を調べてみます'
image: '/assets/images/category/jekyll/google-service.jpg'
---

## 概要
自分のブログで収益やインサイトを貰うためにはやはりグーグルサービスと連動が重要と思います。ここにはブログをもっと上手く活用するためにグーグルサービスとの連携する方法を紹介します。

私たちが連携するグーグルサービスは下記のようです。
- Google Analytics: [https://analytics.google.com/analytics/web/](https://analytics.google.com/analytics/web/){:rel="nofollow noreferrer" :target="_blank"}
- Google Search Console: [https://search.google.com/search-console/about](https://search.google.com/search-console/about){:rel="nofollow noreferrer" :target="_blank"}
- Google Adsense: [https://www.google.com/adsense/start/](https://www.google.com/adsense/start/){:rel="nofollow noreferrer" :target="_blank"}

## Google Analytics
サイトの分析するためには基本的Google Analyticsを使います。下のリンクを押してGoogle Analyticsサイトに移動してグーグルアカウントでログインします。

- Google Analytics: [https://analytics.google.com/analytics/web/](https://analytics.google.com/analytics/web/){:rel="nofollow noreferrer" :target="_blank"}

ログインをすると下の画面が見えます。```sign up```を押して進んでください。

![google analytics signup](/assets/images/category/jekyll/google/analytics/signup.png)

下記のようなフォームへサイトの情報を入力して```Get Tracking ID```を押してトラッキングコードを発行してもらいます。

![google analytics register site](/assets/images/category/jekyll/google/analytics/register-site.png)

トラッキングコードが発行されたら```Global Site Tag (gtag.js)```にあるコードを```_include/head.html```へコピペします。テーマによってレイアウトファイルが違うかもしれないです。

![google analytics tracking code](/assets/images/category/jekyll/google/analytics/tracking-code.png)

注意: 上に見えるコードはテスト用の私たちのコードです。それをコピペしじゃタメです。自分のコードをコピペしてください。

Google Analyticsとの連動が終わりました。今からはデータを見ながらブログを管理してみてください。

## Google Search Console
Google Search Consoleはグーグル検索エンジンへ自分のサイトを登録してグーグルに自分のサイトが検索できるようにします。下記のリンクを押してGoogle Search Consoleへ移動します。

- Google Search Console: [https://search.google.com/search-console/about](https://search.google.com/search-console/about){:rel="nofollow noreferrer" :target="_blank"}

下の画面が出たら、```Start now```を押してGoogle Search Consoleを始めます。

![google search console start](/assets/images/category/jekyll/google/search-console/start.png)

自分のサイトURLを入力してGoogle Search Consoleへサイトを登録します。
![google search console start](/assets/images/category/jekyll/google/search-console/register.png)

下記の画面が出たら```Google Analytics```を押して```VERIFY```を押して自分のサイトであることを証明します。

![google search console verify](/assets/images/category/jekyll/google/search-console/verify.png)

自分のサイトのサイトマップを登録してグーグルボットがサイトをクローリングできるようにします。

![google search console sitemap](/assets/images/category/jekyll/google/search-console/sitemap.png)

Google Search Consoleとの連携が終わりました。今からグーグルボットがサイトをクルーリングしてサイトがGoogleから検索できるようにしてくれます。私たちは待つことしかできないです。

グーグルボットがサイトをクローリングをしないとか時間が結構かかる時直接クローリングを要求することもできます。

![google search console request](/assets/images/category/jekyll/google/search-console/request.png)

一番上部にある検索バーへクローリングを要求したいURLを入力して検索します。上の画面が見えたら```REQUEST INDEXING```を押してクローリングを要求してください。

Google Search Consoleとの連動が終わりました。今からグーグルボットがクローリングして私たちのサイトがグーグルで検索できるようになります。

## Google Adsense
私たちがブログでお金持ちにはならないと思いますがGoogle Adsenseの連動練習もお金のためにもjekyllへGoogle Adsenseを連動してみましょう。

下記のリンクを押してGoogle Adsenseサイトに行きます。

- Google Adsense: [https://www.google.com/adsense/start/](https://www.google.com/adsense/start/){:rel="nofollow noreferrer" :target="_blank"}

Google Adsenseサイトで```sign up```を押して会員登録します。

![google adsense signup](/assets/images/category/jekyll/google/adsense/signup.png)

サイト登録が終わったらpaymentを登録する必要があります。Google Adsenseからお金を貰う人の情報を入力します。

![google adsense payment](/assets/images/category/jekyll/google/adsense/payment.png)

そしたらGoogle Adsenseが許可する時まで待ちます。普通は一日で登録してくれますが、私たちのブログは2~3週かかりました。多分最初ブログを作る時登録したのでコンテンツ（ページ）があまりないから登録してくれなかったと思います。登録がながっくなる方はコンテンツ（ページ）をもっと作ってみてください。

![google adsense get](/assets/images/category/jekyll/google/adsense/get.png)

たくさんのユーザーがページを見たり広告を押したら上の画面みたいにGoogle Adsenseからお金が入ります。実際自分の口座におろすためには一定量（¥8,000）越える必要があります。私たちが口座へおろす時が来たらどうやっておろすかをブログへ記録します。

## 参考
- Google Analytics: [https://analytics.google.com/analytics/web/](https://analytics.google.com/analytics/web/){:rel="nofollow noreferrer" :target="_blank"}
- Google Search Console: [https://search.google.com/search-console/about](https://search.google.com/search-console/about){:rel="nofollow noreferrer" :target="_blank"}
- Google Adsense: [https://www.google.com/adsense/start/](https://www.google.com/adsense/start/){:rel="nofollow noreferrer" :target="_blank"}