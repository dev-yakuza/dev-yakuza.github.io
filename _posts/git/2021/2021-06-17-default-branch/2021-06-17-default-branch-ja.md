---
layout: 'post'
permalink: '/git/default-branch/'
paginate_path: '/git/:num/default-branch/'
lang: 'ja'
categories: 'git'
comments: true

title: "[Git] デフォルトブランチをmasterからmainに設定する方法"
description: Gitを使う時、基本ブランチをmasterからmainに変更する方法について説明します。
image: '/assets/images/category/git/2021/default-branch/background.jpg'
published: false
---

<div id="contents_list" markdown="1">

## 目次


</div>

## 概要

Gitの基本ブランチ名である`master`と言う単語が色々問題になって、たくさんのサービスで`master`の名前を使わなくなりました。

- GitHub [Renaming the default branch from master](https://github.com/github/renaming){:rel="nofollow noreferrer noopener" target="_blank"}

しかし、まだローカルでGitを使うと`master`が基本ブランチで生成される不便さがあります。今回のブログポストではローカルでGitを使う時、基本的`master`ではなく`main`でブランチが生成されるようにする方法を紹介します。

## Git config

`git config`のコマンドを使うとGitに関する色んな設定を修正することができます。もちろん、基本ブランチ名を変更するときもこのコマンドを使います。そしたら、次のコマンドを実行してGitの基本ブランチ名を`master`から`main`で変更します。

```bash
git config --global init.defaultBranch main
```

このコマンドを実行した後、次のコマンドを使ってGitを初期化すると、`master`ブランチではなく`main`ブランチが生成されることが確認できます。

```bash
git init
```

## 完了

これでGitの基本ブランチ名を`master`から`main`に変更する方法について説明しました。皆さんもこの設定を使ってGitのデフォルトブランチ名を変更してみてください。
