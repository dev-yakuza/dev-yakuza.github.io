---
layout: 'post'
permalink: '/git/create-stage/'
paginate_path: '/git/:num/create-stage/'
lang: 'ja'
categories: 'git'
comments: true

title: 'バージョン生成'
description: 'gitのリポジトリ(Repository)でバージョン管理するためにバージョン(変更履歴)を生成してみましょう。'
image: '/assets/images/category/git/create-stage.jpg'
---

## 概要
以前のブログで([リポジトリ生成]({{site.url}}/{{page.categories}}/create-stage/){:target="_blank"})でgitのリポジトリ(Repository)を生成する方法を勉強しました。今回は生成されたgitのリポジトリ(Repository)へバージョン管理をするためバージョン(変更履歴)を生成する方法に関して勉強してみましょう。

## ファイル追加
gitのリポジトリ(Repository)が存在するフォルダ(```temp_test_git```)へバージョン管理したいファイルをコピーするか生成します。

私たちはテストのため```temp_test_git```フォルダへ```test text```を書いた```test.txt```ファイルを生成しました。

## git status
gitのリポジトリ(Repository)の現在状態を確認するため下の```git status```コマンドを実行します。

```bash
git status
```

上のように```git status```コマンドを実行したら下記のような画面が見えます。

![git status](/assets/images/category/git/create-stage/git-status.png)

- On branch master: 現在のブランチ(branch)はマスター(master)です。gitのブランチ(branch)に関しては別のブログポストで紹介します。
- No commits yet: まだ、コミット(commit)をしてない状態です。コミット(commit)はバージョン(変更履歴)を意味します。まだ、バージョン(変更履歴)を作ってない状態を意味します。
- Untracked files: gitがバージョン(変更履歴)管理をしてないファイルリストです。

私たちはまだgitに```test.txt```ファイルをバージョン(変更履歴)管理するように教えてくれませんでした。そのため、```Untracked files```へ私たちが作った```test.txt```ファイルが存在します。

## git add
私たちが作った新しファイル(```test.txt```)をgitへバージョン(変更履歴)管理対象であることを教える必要があります。```git add```コマンドでgitへ```test.txt```フィルはバージョン(変更履歴)管理対象てあることを教えてみましょう。

```bash
# add single file
git add test.txt

# add multiple files
# git add test.txt test2.txt test3.txt

# add all files
# git add .
```

下記のように```git status```コマンドでgitが新しく追加されたファイルがバージョン(変更履歴)管理対象で認識されてるかを確認します。

```bash
git status
```

下記のように```git status```コマンドを実行したら先の画面とは違う画面が見えます。

![git status after executing git add command](/assets/images/category/git/create-stage/git-status-after-add.png)

- Changes to be committed: gitが次のバージョン(変更履歴)管理をするためのファイルリストです。私たちはファイルを新しく追加したので```new file```で```text.txt```が追加されたことが見えます。

このように```git add```を使ってファイルを追加するプロセスがある理由は今回のバージョン(変更履歴)へ追加したくないファイルが実際のプログラムを作成する時存在するからです。例えば、ビルドされた結果物、DBの情報、ID/PWが保存されてるファイルや臨時でログを表示するため作成したコード(console.log / printなど)が含まれていてバージョン(変更履歴)とは無関係な内容を区分するため使います。

## git commit
私たちはgitにバージョン(変更履歴)へ追加したいファイルを```git addd```コマンドを使って教えてあげました。しかし、実際バージョン(変更履歴)管理はまだ出来てないです。ただgitに新しファイルがあることを教えただけです。実際バージョン(変更履歴)管理をするため```git commit```を使ってバージョン(変更履歴)を生成します。

```bash
git commit
```

このように```git commit``コマンドを実行したらバージョン(変更履歴)を生成する画面が実行されます。

![git commit](/assets/images/category/git/create-stage/git-commit.png)

この画面は```vim```と言うドキュメント編集ツールが実行された画面です。ドキュメントを編集するためキーボードで```i```(insert)を押して変更履歴の内容を作成します。

![git commit with message](/assets/images/category/git/create-stage/git-commit-with-message.png)

作成を完了したらキーボードの```esc```ボタンを押して```:wq```(write-quit)を入力して変更履歴を作成します。

![git completed commit](/assets/images/category/git/create-stage/git-complete-commit.png)

変更履歴が作成されたら上記のようなメッセージが見えます。

## git log
バージョン(変更履歴)が上手く生成されたかを確認するため```git log```コマンドを実行します。

```bash
git log
```
上のように```git log```を実行したら現在作成したバージョン(変更履歴)を確認することができます。

![git log](/assets/images/category/git/create-stage/git-log.png)

- Author: バージョン(変更履歴)を作った人と作成者のメール(git configで登録したユーザー名とメール)
- Date: バージョン(変更履歴)の生成日時
- Dateの下には```git commit```を使って作成したメッセージが見えます。

## ファイル修正の場合
ファイルを修正する場合も上記と同じ方法でします。まず、下のように```git status```コマンドを使って現在の状態を確認します。

```bash
git status
```

まだ何も変更してないので変更内容がないとgitが教えてくれます。

![git status no change](/assets/images/category/git/create-stage/git-status-no-change.png)

じゃ、```test.txt```ファイルの内容を```test text```から```test string```で修正して```git status```を実行してみましょう。

```bash
git status
```

今回は変更の内容があるため下記のような画面が見えます。

![git status with modification](/assets/images/category/git/create-stage/git-status-with-modification.png)

- modified: 修正したファイルを意味します。

今度は```git addd``を使ってgitへ変更した内容があることを教えてあげます。言い換えれバージョン(変更履歴)へ記録するファイルを追加します。

```bash
git add test.txt
```

また```git status```で状態を確認します。

![git status after commit](/assets/images/category/git/create-stage/git-status-after-commit.png)

先とは違って文字も緑で```no changes added to commit (use "git add" and/or "git commit -a")```メッセージもないことが分かります。gitへバージョン(変更履歴)へ```test.txt```ファイルを上手く追加したことが分かります。```git commit```を使ってバージョン(変更履歴)を生成します。バージョンメッセージ(変更履歴メッセージ)には```edit 'text' to 'string'```と入力しました。

```bash
git commit
```

そして```git log```でバージョン(変更履歴)が上手く生成されたかを確認します。

```bash
git log
```

![git log with new version](/assets/images/category/git/create-stage/git-log-with-new-version.png)

上のようにバージョン(変更履歴)が上手く生成されたことが確認できます。

## 要約
バージョン(変更履歴)を生成する方法について勉強しました。全般的に要約すると下記のようです。

1. ファイル追加または変更
1. ```git status```で追加または変更されたフィアるを確認
1. ```git add```でバージョン(変更履歴)へ追加したいファイルを登録
1. ```git status```でバージョン(変更履歴)へ追加したファイルが登録されたかを確認
1. ```git commit```でバージョン(変更履歴)へメッセージを追加して生成
1. ```git log```で生成されたバージョン(変更履歴)を確認

上記のような方法で新しバージョン(変更履歴)を生成します。