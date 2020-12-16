---
layout: 'post'
permalink: '/git/git-squash/'
paginate_path: '/git/:num/git-squash/'
lang: 'ja'
categories: 'git'
comments: true

title: 'Git squashで複数のコミットを1つでまとめる'
description: Git squashを使って複数のコミットを1つのコミットでまとめる方法について説明します。
image: '/assets/images/category/git/2020/git-squash/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [Git Squash](#git-squash)
  - [Git Log](#git-log)
  - [Git Rebase](#git-rebase)
  - [Git Push](#git-push)
- [完了](#完了)

</div>

## 概要

オープンソースへコミット(Commit)する時や会社のソースコードを修正する時、普通、1つの課題(Issue)を作って、その課題を基準にしてブランチを作ります。そして、このように作ったブランチへ修正内容をコミット(Commit)します。しかし、普通はコミット1つで全ての修正を反映することができないです。フロントサイドの修正コミット、サーバーサイドの修正コミット、テストコードのコミット、コードレビュー対応コミットなど、1つの課題を修正するため、様々なコミットが発生します。

このように生成された様々なコミットをマージ(Merge)してもいいですが、オープンソースや色んな人が一緒に作業する会社のソースコードの場合、コミット履歴が多くって、複雑になって、コミットの履歴を追跡することが難しくなります。

これを避けるため、このブログポストではGitの`Squash`機能について説明します。

## Git Squash

Git Squashは複数のコミット履歴を1つのコミット履歴でまとめる時使います。

### Git Log

まず、下記のコマンドを実行してコミットした履歴を確認します。

```bash
git log --pretty=oneline
```

そしたら、下記のような結果が見えます。

```bash
1f199b7353e40e3134572c9986837b1b4bfebd13 (HEAD -> squash-test) third commit
0118d468a770c2340bf6d4d47f10984c58ea382b second commit
b91e257ce42d5f501c7bc8242a0580b3c05ef462 first commit
db078dae819cfed46bc6e6ef8c962648f97c22da (origin/master, origin/develop, master, develop) Merge pull request #1 from dev-yakuza/rebase-and-squash
c6bd068ec0ea39ef98e135218dc19375e5d63a68 (origin/rebase-and-squash, rebase-and-squash) add rebase-and-squash
2d33cf05e6352b2fa7e8574d170032b34e3a8959 change master
405d0d71ed50429a169ece18cf984dfd64c088a9 add proejct
```

私は現在Masterブランチから`squash-test`ブランチを作って`first commit`, `second commit`, `third commit`のコミットをした状態です。

```bash
1f199b7353e40e3134572c9986837b1b4bfebd13 (HEAD -> squash-test) third commit
0118d468a770c2340bf6d4d47f10984c58ea382b second commit
b91e257ce42d5f501c7bc8242a0580b3c05ef462 first commit

db078dae819cfed46bc6e6ef8c962648f97c22da (origin/master, origin/develop, master, develop) Merge pull request #1 from dev-yakuza/rebase-and-squash
```

{% include in-feed-ads.html %}

### Git Rebase

次は、GitのSquash機能で`first commit`, `second commit`, `third commit`のコミットを1つのコミットに作ってみます。Squash機能を使うためにはGitの`Rebase`を使う必要があります。

まず、Gitのログをもう一回確認して、

```bash
1f199b7353e40e3134572c9986837b1b4bfebd13 (HEAD -> squash-test) third commit
0118d468a770c2340bf6d4d47f10984c58ea382b second commit
b91e257ce42d5f501c7bc8242a0580b3c05ef462 first commit

# We will rebase on here!!!!!!!!
db078dae819cfed46bc6e6ef8c962648f97c22da (origin/master, origin/develop, master, develop) Merge pull request #1 from dev-yakuza/rebase-and-squash
```

3つのコミットを1つのコミットで作る予定なので、3つのコミットをする以前である`db078dae819cfed46bc6e6ef8c962648f97c22da`へRebaseをします。

Squashを使うため、下記のGitのRebaseコマンドを使ってRebaseをします。

```bash
git rebase -i db078dae819cfed46bc6e6ef8c962648f97c22da
```

ここで`-i`をオプションを使ってことを注目してください。`-i`オプションを使ってので、普通のRebaseとは違って、下記のような結果が見えます。

```bash
pick b91e257 first commit
pick 0118d46 second commit
pick 1f199b7 third commit

# Rebase db078da..1f199b7 onto db078da (3 commands)
#
# Commands:
# p, pick <commit> = use commit
# r, reword <commit> = use commit, but edit the commit message
# e, edit <commit> = use commit, but stop for amending
# s, squash <commit> = use commit, but meld into previous commit
# f, fixup <commit> = like "squash", but discard this commit's log messag
```

この画面はRebaseを使ってコミット以前の状態に戻るようにしてるが、現在と過去の間に残ってるコミットをどう処理するかをGitが親切に質問してくれる画面です。下に使えるCommandのリストもあります。私たちはここで、`s, squash`を使う予定です。

```bash
# s, squash <commit> = use commit, but meld into previous commit
```

このコミットには`first commit`を残して`second commit`と`third commit`をSquashしてみます。キーボードの`i`ボタンを押して、修正できる状態に変更した後、下記のように修正します。

```bash
pick b91e257 first commit
s 0118d46 second commit
s 1f199b7 third commit

# Rebase db078da..1f199b7 onto db078da (3 commands)
#
# Commands:
# p, pick <commit> = use commit
# r, reword <commit> = use commit, but edit the commit message
# e, edit <commit> = use commit, but stop for amending
# s, squash <commit> = use commit, but meld into previous commit
# f, fixup <commit> = like "squash", but discard this commit's log messag
```

そしてキーボードの`ESC`ボタンを押して`:wq`を入力した後、`Enter`キーを押して変更した内容を保存します。変更が完了されたら下記のような画面が見えます。

```bash
# This is a combination of 3 commits.
# This is the 1st commit message:

first commit

# This is the commit message #2:

second commit

# This is the commit message #3:

third commit

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
#
# Date:      Mon Apr 20 14:42:26 2020 +0900
#
# interactive rebase in progress; onto db078da
# Last commands done (3 commands done):
#    squash 0118d46 second commit
```

この画面はGitがRebaseを使ってSquashをする予定だけど、以前作成したコミットメッセージをどうするか聞いてくれる画面です。Gitが全てのメッセージを1つの画面で見せています。キーボードの`i`ボタンを押して、下記のように修正します。（メッセージは皆さんの環境に合わせて変更してください。）

```bash
# This is a combination of 3 commits.
# This is the 1st commit message:

Fix Squash Task

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
```

メッセージの作成が完了されたら、キーボードの`ESC`ボタンを押して`:wq`を入力して保存します。

また、`git log --pretty=oneline`でコミット履歴を確認すると、

```bash
099e6f606b3a46b98f0233d558eb07c143a3ec01 (HEAD -> squash-test) Fix Squash Task
db078dae819cfed46bc6e6ef8c962648f97c22da (origin/master, origin/develop, master, develop) Merge pull request #1 from dev-yakuza/rebase-and-squash
```

Rebase以前とは違って、コミットが1つしか表示されないことが確認できます。また、メッセージの内容も私たちがSquashする時、作成した内容が表示されることが確認できます。

{% include in-feed-ads.html %}

### Git Push

次は、このように1つにしたコミットをリモートリポジトリ(Remote Repository)へ`Push`します。

```bash
git push origin squash-test
```

すでにコミットした内容をリモートリポジトリへPushしたことがある場合、下記のように`-f`オプションを使って強制的変更します。

```bash
git push origin squash-test -f
```

## 完了

これでGitのSquashを使ってたくさんのコミット履歴を1つのコミットに変更する方法について見てみました。明確にはGitのRebaseを使ってSquashを実行したと言いますね。今回のブログポストで使ってコマンドをまとめてみました。

```bash
git log --pretty=oneline
git rebase -i [Commit Number]
# Select to pick and squash
# Change commit log
git push origin [Branch] -f
# git push origin [Branch]
```

皆さんもSquashを使って綺麗なコミット履歴を残してみてください！
여러분도 Squash를 통해 예쁜 커밋 이력을 남겨보세요!
