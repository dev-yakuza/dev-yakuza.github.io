---
layout: 'post'
permalink: '/jekyll/pagination-plugin/'
paginate_path: '/jekyll/:num/pagination-plugin/'
lang: 'ja'
categories: 'jekyll'
comments: true

title: 'paginationプラグイン'
description: 'paginationプラグインを使ってjekyllプロジェクトへページ機能を追加して見ましょう。'
image: '/assets/images/category/jekyll/pagination.jpg'
---

## 概要
jekyllは基本的にpaginationプラグインを提供してますが、私たちは[jekyll-paginate-v2](https://github.com/sverrirs/jekyll-paginate-v2){:rel="nofollow noreferrer" :target="_blank"}を使っています。
このブログはjekyll-paginate-v2の使用法について説明します。

## プラグインのインストールや設定
jekyll-paginate-v2プラグインをインストールしてプレジェクトへ設定します。

### プラグインのインストール
下記のコマンドでjekyll-paginate-v2のプラグインをインストールします。

{% include_relative common/installation.md %}

### プラグインの設定
下記の設定内容を```_config.yml```ファイルへ作成します。

{% include_relative common/config_yml.md %}

- permalink: ページの基本リンクです。このリンクがないとプラグインがうまく動作しません。
- pagination: プラグインの設定オプションです。詳しく内容は公式サイトをご参考してください。([jekyll-paginate-v2:options](https://github.com/sverrirs/jekyll-paginate-v2/blob/master/README-GENERATOR.md){:rel="nofollow noreferrer" :target="_blank"})
- enabled: プラグインを有効化します。
- per_page: ページごとに表示するポスト数です。
- sort_reverse: 逆整列をするかどうかを意味します。私たちは最近順でポストを表示するため```true```で設定します。
- sort field: 整列する時使うフィールドです。私たちは最近順で表示するため```date```フィールドを使ってます。
- title: paginationで生成されたページのタイトルです。```page.title```変数に割り当てられる値を設定します。(ex> :title - page :num)
- trail: 現在選択されたページの前・後へpaginationをどのぐらい表示するかを設定します。

## ページ設定
ページへpaginationを表示するための設定です。paginationを持ってるページとpaginationから呼ばれるページ中に設定します。

### paginationを持ってるページ
paginationを表示するためpaginationを持ってるページ(ex> categoryページ)へ下記のように設定します。

{% include_relative common/page_setting.md %}

- enabled: pagination機能を使います。
- category: このカテゴリのポストをpaginationします。
- permalink: pagination機能で生成されたページのリンクを設定します。(ex> /:num/)

### paginationページから呼ばれるページ
呼ばれるページ(ex> postページ)へ下記のように設定します。

{% include_relative common/called_page_setting.md %}

- paginate_path: paginationから呼ばれる時ページの番号をリンクへ入れるための設定です。

## 参考
- 公式サイト: [jekyll-paginate-v2](https://github.com/sverrirs/jekyll-paginate-v2/blob/master/README-GENERATOR.md){:rel="nofollow noreferrer" :target="_blank"}
- 公式サイトのオプション説明: [jekyll-paginate-v2:options](https://github.com/sverrirs/jekyll-paginate-v2/blob/master/README-GENERATOR.md){:rel="nofollow noreferrer" :target="_blank"}