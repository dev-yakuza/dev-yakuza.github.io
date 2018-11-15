---
layout: 'post'
permalink: '/jekyll/jekyll-last-modified-at/'
paginate_path: '/jekyll/:num/jekyll-last-modified-at/'
lang: 'ja'
categories: 'jekyll'
comments: true

title: 'jekyll-last-modified-at'
description: '最後のファイル修正日をsitemap.xmlへ反映してみました。'
image: '/assets/images/category/jekyll/jekyll-last-modified-at.jpg'
---

## 概要
今まで管理してるこのブログの```sitemap.xml```は

```<lastmod>{% raw %}{{ site.time | date: '%Y-%m-%d' }}{% endraw %}</lastmod>```

これを使ってビルドする時点の日付を全てのページへ反映していました。しかし実際更新してないファイルもビルドした時点の時間が入るから全てのファイルを再クローリングして実際更新したファイルのクローリングが遅くなるんじゃないかなと思いました。それで今回```jekyll-last-modified-at```プラグインを使って実際ファイルが修正された場合```sitemap.xml```へ反映するように修正しました。

## プラグイン
下にあるリンクを押して```jekyll-last-modified-at```のサイトへ行ったら全ての説明が詳しくあります。それを見ながらやってみます。

- jekyll-last-modified-at: [https://github.com/gjtorikian/jekyll-last-modified-at](https://github.com/gjtorikian/jekyll-last-modified-at){:rel="nofollow noreferrer" :target="_blank"}

## プラグインインストル
下のコマンドで```jekyll-last-modified-at```ぷログインをインストールします。

```bash
gem install jekyll-last-modified-at
```

## 使い方
ファイルの修正日を表示したい部分で下記のコード中の一つを選べって入れます。

```html
{% raw %}
{% last_modified_at %}

{% last_modified_at %Y:%B:%A:%d:%S:%R %}

{{ page.last_modified_at }}

{{ page.last_modified_at | date: '%Y:%B:%A:%d:%S:%R' }}
{% endraw %}
```
私たちは使ってる```sitemap.xml```を下のように修正しました。

```xml
<!-- <lastmod>{% raw %}{{ site.time | date: '%Y-%m-%d' }}{% endraw %}</lastmod> -->
<lastmod>{% raw %}{{ post.last_modified_at | date: '%Y-%m-%d' }}{% endraw %}</lastmod>
```

## 確認
実際プロジェクトをビルドして入れたコードを確認した結果、実際ファイルを修正した日付が上手く表示してることを確認しました。

```bash
bundle exec jekyll build
```

グーグルのクローリングに影響があるかは分からないけど実際の時間を表示するように修正したのでプログラマー的に上手く仕事したんじゃないかなと思って嬉しいです。