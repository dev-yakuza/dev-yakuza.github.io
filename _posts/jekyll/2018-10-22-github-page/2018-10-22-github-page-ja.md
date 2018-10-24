---
layout: 'post'
permalink: '/jekyll/github-page/'
paginate_path: '/jekyll/:num/github-page/'
lang: 'ja'
categories: 'jekyll'
comments: true

title: 'github page'
description: '今まで作ったjekyllのプロジェクトをgithub pagedへアップロードしてブログサービスを始めてみましょう。'
image: '/assets/images/category/jekyll/github-page.jpg'
---

## 概要
今まで作ったjekyllプロジェクトをgithub pageへアップロードしてブログを始めてみましょう。基本ソースは[bitbucket](https://bitbucket.org/){:rel="nofollow noreferrer" :target="_blank"}で管理する予定でjekyllからbuildされたstaticページを[github](https://github.com/){:rel="nofollow noreferrer" :target="_blank"}へアップロードしてサービスする予定です。

jekyllを使ってプロジェクトを作る方法をよく知らない方は以前のブログを確認してください。

### jekyllプロジェクト生成
- [jekyllインストール]({{site.url}}/{{page.categories}}/installation/){:target="_blank"}
- [テーマ設定]({{site.url}}/{{page.categories}}/theme/){:target="_blank"}
- [フォルダ構造]({{site.url}}/{{page.categories}}/directory_structure/){:target="_blank"}
- [jekyll設定]({{site.url}}/{{page.categories}}/configuration/){:target="_blank"}

### jekyllプロジェクトオプション
- [多言語プラグイン]({{site.url}}/{{page.categories}}/multi-languages-plugin/){:target="_blank"}
- [SEO対応]({{site.url}}/{{page.categories}}/seo/){:target="_blank"}
- [paginationプラグイン]({{site.url}}/{{page.categories}}/pagination-plugin/){:target="_blank"}
- [Disqusコメント]({{site.url}}/{{page.categories}}/disqus/){:target="_blank"}
- [メール送信機能]({{site.url}}/{{page.categories}}/send-email/){:target="_blank"}
- [googleサービス]({{site.url}}/{{page.categories}}/google-service/){:target="_blank"}

## bitbucket
bitbucketもgithubのようにrepositoryを管理するツールです。機能がたくさんありますが、ここではgithub pageへアップロードするソースを管理用で説明します。自分のソースが公開されても良い方はここはスキップしても構わないです。

下記のリンクを押してbitbucketへ移動します。

- bitbucket: [https://bitbucket.org/](https://bitbucket.org/){:rel="nofollow noreferrer" :target="_blank"}

### 会員登録とログイン
会員登録とログインの説明は省略します。一般的サービスと同じ手順ですので会員登録とログインをしてください。

![bitbucket login](/assets/images/category/jekyll/github-page/bitbucket-login.png)

### Repository生成
ログイン後、下のメニューが見えたら```+````ボタンを押します。

![bitbucket menu](/assets/images/category/jekyll/github-page/bitbucket-menu.png){:class="narrow-image"}

下のメニューが見えたら```Repository```を押して新しいrepositoryを生成します。

![bitbucket menu repository](/assets/images/category/jekyll/github-page/bitbucket-menu-repository.png){:class="narrow-image"}

repositoryの情報を入力します。

![bitbucket menu repository information](/assets/images/category/jekyll/github-page/bitbucket-menu-repository-information.png)

repositoryの生成が完了しました。

### PCへRepository連動
開発で使うPCへ生成したrepositoryを連動してソースコードを管理します。gitのインストールや使い方をよく知らない方はgitに関するブログを参考してください。([git]({{site.url}}/git/){:target="_blank"})

![bitbucket git clone](/assets/images/category/jekyll/github-page/bitbucket-git-clone.png)

repositoryが生成されたら上の画面が見えます。PCとの連動について詳しく説明が表示してます。一緒にやってみましょう。

{% include_relative common/git-clone.md %}

上記のコマンドでPCへrepositoryをcloneします。生成されたフォルダへjekyllプロジェクトをコピします。（または、jekyllプロジェクトを生成します。）

{% include_relative common/git-add-push.md %}

上のコマンドでlocal(pc)にあるソースをbitbucketへあるrepositoryへアップロードします。

[bitbucketサイト](https://bitbucket.org/){:rel="nofollow noreferrer" :target="_blank"}で移動して自分が追加したjekyllプロジェクトのソースがあるかどうか確認します。

## github page連動
github pageにはjekyllがビルドしたstaticファイルをアップロードしてブログサービスを始まります。

### 会員登録とログイン
下記のサイトで移動して会員登録とログインをします。会員登録とログインは一般的サービスと同じですので説明は省略します。

注意；会員登録する時```ユーザ名```には注意してください。```https://ユーザ名.github.io```でgithub pageを作る予定です。

- githubサイト: [https://github.com/](https://github.com/){:rel="nofollow noreferrer" :target="_blank"}

![github login](/assets/images/category/jekyll/github-page/github-login.png)

### Repository生成
ログインをしたら、下の画面が見えます。```Start a project```を押して新しいプロジェクトを生成します。

![github repository](/assets/images/category/jekyll/github-page/github-repository.png)

Repository nameにgithubへ会員登録した時作った```ユーザ名 + github.io```を入力して```Create repository```ボタンを押してrepositoryを生成します。

![github crete repository](/assets/images/category/jekyll/github-page/github-create-repository.png)

### PCへRepository連動
repositoryを生成したらやはり親切に説明があるページが表示します。しかし、私たちはすでにbitbucketとlocalを連動してるので少し別の方法で進めます。もしbitbucketを連動してない方はページの内容で進めてください。

![github clone repository](/assets/images/category/jekyll/github-page/github-clone-repository.png)

私たちはすでにbitbucketと連動してあるので、下記のコマンドでremote repositoryを追加します。

{% include_relative common/add-remote.md %}

連動が終わりました。下記のコマンドでjekyllからビルドして貰ったソースをrepositoryへアップロードします。

{% include_relative common/push-subtree.md %}

ジキルでビルドしてない方はビルドを先にしてください。

{% include jekyll/build_command.md %}

github pagesで画面が表示するかどうか確認しましょう。

```
https://dev-yakuza.github.io
```

## 完了
現在ソースをgithub, bitbucketと連動する方法を見ました。build前のソースをbitbucketへ、build後のstaticファイルをgithub pageへアップロードしてブログサービスができるようにやってみました。今から皆さんも自分のブログを始めて見てください。