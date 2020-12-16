---
layout: 'post'
permalink: '/jekyll/preview-speed-up/'
paginate_path: '/jekyll/:num/preview-speed-up/'
lang: 'ja'
categories: 'jekyll'
comments: true

title: 'プレビュー'
description: 'ジキル(jekyll)で作成してる記事を早く確認するためプレビューの時間を短縮する方法について説明します。'
image: '/assets/images/category/jekyll/preview-speed-up.jpg'
---

## 問題点
今ジキル(jekyll)で管理してるブログが作成した記事が多くなって、ローカルで作成した記事を確認する時、時間が結構掛かります。私は下のジキル(jekyll)コマンドで記事を公開する前ローカルで作成した記事を確認しています。

```bash
bundle exec jekyll serve
```

しかし、記事の量が多いし、使ってるプラグインが多いので記事を確認するため```209.498985 seconds```を待たなければならない問題が発生しました。配布するためこのぐらい時間が掛かることはいいですが、新記事を確認するたびにこのぐらい時間が掛かることはちょっと勿体無いなと思いました。

## 解決策
たくさんの解決策があるみたいですが私は下記のジキル(jekyll)設定でビルド速度をあげました。

まず、 ```_config.yml```をコピーして```_config-dev.yml```を作りました。。そして、下のコードを追加しました。

```yml
# 多言語を使ってるので3を設定。普通は１で設定
limit_posts: 3
```

そして、作成した記事を確認するため下のジキル(jekyll)コマンドを使ってます。

```bash
bundle exec jekyll serve --config _cong-dev.yml
```

このコードは一つのブログ記事のみビルドするようにします。私はこのジキル(jekyll)設定を使って```74.639 seconds```だけ待ってば記事を確認することが出来るようになりました。また、ジキル(jekyll)プラグイン中で時間が結構掛かる```minify```プラグインを使えないように下記のように設定しました。

```yml
jekyll-minifier:
  remove_spaces_inside_tags: false
  remove_multi_spaces: false
  remove_comments: false
  compress_css: false
  compress_javascript: false
  compress_json: false
```

こんな設定をしたらビルド時間が```50.668 seconds```、20秒くらい早くなりました。

## 完了
上記で説明した方法で200秒から50秒にビルド時間が1/4に減少しました。しかし、まだ50秒くらいかかりますね。これはジキル(jekyll)の大問題点と思います。