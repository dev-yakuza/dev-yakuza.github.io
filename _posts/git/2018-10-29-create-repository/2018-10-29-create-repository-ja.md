---
layout: 'post'
permalink: '/git/create-repository/'
paginate_path: '/git/:num/create-repository/'
lang: 'ja'
categories: 'git'
comments: true

title: 'リポジトリ生成'
description: 'gitを使うためにgitのリポジトリ(Repository)を生成します。gitのリポジトリ(Repository)はソースコードのバージョンを管理するためソースコードの編集履歴を情報を保存する場所です。'
image: '/assets/images/category/git/create-repository.jpg'
---

## 概要
gitをインストールしたので今からはgitを使ってソースコードのバージョンを管理する方法を勉強します。ここにはgitでソースコードを管理するためリポジトリ(Repository)を生成する方法について勉強します。gitのリポジトリ(Repository)はソースコードのバージョンに関する履歴を保存するための場所です。

## プロジェクトフォールだ生成
Macは```terminal```、Windowsは```cmd```を使って説明します。gitを使うためのフォルダを作ります。

```bash
mkdir temp_test_git
```
## gitのリポジトリ(Repository)生成
gitを使うために生成したフォルダへgitのリポジトリ(Repository)を生成する必要があります。

```bash
cd temp_test_git

git
```
上のコマンドでgitで使えるコマンドリストを確認します。

![git clone init](/assets/images/category/git/create-repository/clone_init.png)

gitのコマンドを確認したら上の画像ようにgitのリポジトリ(Repository)を```clone```をするか```init```をするか選択するコマンドがあります。

- init: 新しgitのリポジトリ(Repository)を生成します。
- clone: 既存のgitのリポジトリ(Repository)をコピーして生成します。

### git init
新しプロジェクトを始める場合、```init```コマンドを使ってgitのリポジトリ(Repository)を生成します。

```bash
git init
```

### git clone
既存に存在してるプロジェクト(Opensourceや既存gitでバージョン管理をしてるプロジェクト)がある場合、外部リポジトリ(Remote Repository)から```clone```コマンドでリポジトリ(Repository)をコピーして持ってきます。

下記は私たちのブログのgitリポジトリ(Repository)をcloneすることで説明します。

- gitリポジトリ(Repository): [https://github.com/dev-yakuza/dev-yakuza.github.io](https://github.com/dev-yakuza/dev-yakuza.github.io){:rel="nofollow noreferrer" :target="_blank"}

上のリンクを押してgithubで保存している私たちのgitリポジトリ(Repository)へ移動します。

![git clone blog](/assets/images/category/git/create-repository/clone.png)

右へある```Clone or donwload```ボタンを押してgitリポジトリ(Repository)のURLをコピーします。

```bash
 git clone https://github.com/dev-yakuza/dev-yakuza.github.io.git
```

上のコマンドを実行したら私たちのgitリポジトリ(Repository)がLocal PCへコピーされます。参考ですが私たちのブログは```jekyll```を使って無料でサービスしてます。興味があるかたは[jekyll blog]({{site.url}}/jekyll/){:target="_blank"}を参考してください。

## gitリポジトリ(Repository)生成確認
gitのリポジトリ(Repository)が上手く生成されたかを下記のコマンドで確認します。

```bash
# Mac
ls -al

# Windows
dir /ah
```

表示してるリストへ```.git```フォルダが見えたらgitリポジトリ(Repository)の生成が成功したことを意味します。```.git```フォルダはgitを使ってソースコードバージョンを管理したらそこに関する情報が保存される場所です。```.git```フォルダを削除したらgitのリポジトリ(Repository)へ保存した内容が全部削除されるので削除しないように気をつけてください。