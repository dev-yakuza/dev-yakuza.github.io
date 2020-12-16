---
layout: 'post'
permalink: '/git/sync-fork-repository/'
paginate_path: '/git/:num/sync-fork-repository/'
lang: 'ja'
categories: 'git'
comments: true

title: 'Forkリポジトリを同期する'
description: Forkしたリポジトリ(Repository)と原本リポジトリ(Repository)を同期(Sync)する方法について説明します。
image: '/assets/images/category/git/2020/sync-fork-repository/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [原本リポジトリ追加](#原本リポジトリ追加)
- [原本リポジトリの内容を取ってくる](#原本リポジトリの内容を取ってくる)
- [Rebase](#rebase)
- [Forkブランチ同期化](#forkブランチ同期化)
- [完了](#完了)

</div>

## 概要

オープンソースへコミット(Commit)する時、会社がソースコードをGitHubで管理してる時、私たちはForkを使って当該リポジトリ(Repository)を自分のリポジトリで持ってきます。このように持ってきたリポジトリのCloneして修正した後、原本リポジトリへPull Requestを送ってMergeすることでソースコードを管理します。

しかし、オープンソすや会社のソースコードは一人だけ使ってないので、私がForkした時点の原本リポジトリのMasterとPull Requestを送る現時点の原本Masterには差があります。

このブログポストではこのように差が発生した場合、原本リポジトリのMasterとForkしたリポジトリのMasterを同期化する方法について説明します。

## 原本リポジトリ追加

原本リポジトリとForkしたリポジトリを同期化(Sync)するためにはまず、原本リポジトリをローカル環境のリモートアドレスへ追加する必要があります。

下記のコマンドを実行して現在追加されたリモートアドレスを確認します。

```bash
git remote -v
```

上のコマンドを実行すると下記のような結果が確認できます。

```bash
origin  https://github.com/USER_NAME/FORK_REPOSITORY.git (fetch)
origin  https://github.com/USER_NAME/FORK_REPOSITORY.git (push)
```

ローカルは当然にForkしたリポジトリをCloneしたので、上のような結果が確認できます。次は下記のコマンドを使って原本リポジトリをローカルのリモートアドレスへ追加します。

```bash
git remote add upstream https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git
```

普通は`upstream`という名前で原本リポジトリを追加しますが、ただの名前なので他の名前にしても大丈夫です。

```bash
git remote add test https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git
```

ここでは`upstream`と言う名前で進めます。下記のコマンドを実行して原本リポジトリがうまく追加されたか確認します。

```bash
git remote -v
```

問題なく追加されたら下記のような結果が確認できます。

```bash
origin    https://github.com/USER_NAME/FORK_REPOSITORY.git (fetch)
origin    https://github.com/USER_NAME/FORK_REPOSITORY.git (push)
upstream  https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git (fetch)
upstream  https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git (push)
```

{% include in-feed-ads.html %}

## 原本リポジトリの内容を取ってくる

ローカルのリモートアドレスへ原本のリポジトリを追加しました。次は`Fetch`を使ってリモートのリポジトリの内容をローカルへ取ってきます。

下記のコマンドを実行してリモートリポジトリの内容を取ってきます。

```bash
git fetch upstream master
```

## Rebase

現在ローカルのMasterブランチはForkしたリポジトリをCloneしたので、ForkしたリポジトリのMasterブランチをBaseにしてます。次は`Rebase`を使ってローカルのMasterブランチが`Fetch`で取ってきた原本リポジトリのMasterブランチをBaseにするように変更します。

下記のコマンドを使ってローカルのMasterブランチのBaseを原本リポジトリのMasterブランチで変更します。

```bash
git rebase upstream/master
```

今、ローカルのMasterブランチのBaseは原本リポジトリのMasterブランチになりました。

## Forkブランチ同期化

Rebasewo使って現在ローカルのMaserブランチは原本リポジトリのMasterブランチで変更された状態です。次は、Forkしたリモートリポジトリも原本リポジトリのMasterブランチで変更する必要があります。

下記のコマンドを使ってForkしたリモートリポジトリのMasterブランチを原本リポジトリのMasterブランチで同期化します。

```bash
git push origin master -f
```

## 完了

業務中で、オープンソースのコミットする時、このように時々リポジトリを同期化することがあります。皆さんもRebasewo使ってForkしたリポジトリを同期化してみてください。
