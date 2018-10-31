---
layout: 'post'
permalink: '/git/installation/'
paginate_path: '/git/:num/installation/'
lang: 'ja'
categories: 'git'
comments: true

title: 'gitインストール'
description: 'ソースコードのバージョン管理のためgitを使ってみましょう。gitを使うためgitをインストールします。'
image: '/assets/images/category/git/installation.jpg'
---

## ソースコードバージョン管理
gitはソースコードのバージョンを管理します。バージョンを管理の意味はソースコードの変更履歴を保存して管理することを意味します。ソースコードの変更が間違って戻りたい時どこをどうやって変更したか覚えれなくて困った時ありましたか？gitようなソースコードバージョン管理ツールはこのような状況のため作られました。しかし、```ctrl + z```のように特別なキーを押したらソースコードが変更前へ戻ることのような魔法的なツールではないです。

ソースコードのバージョン管理ツールは開発者がソースコードを変更した後、ソースコードのバージョン管理ツールを使って変更履歴とソースを別のところ(Repository)へ保存します。そして、ソースコードを変更前に戻りたいときは変更履歴を保存した別のところ(Repository)から前のソースを読んできます。このようにソースコードのバージョンを管理します。

gitはソースコードのバージョン管理ツールとして色々たくさんの機能を持ってます。私たちもその機能中一部だけ使ってるし、本当は他の機能が何があるかよく知らないからこのブログを始めました。今後はgitを勉強した内容を記録します。皆さんにも助けになったらいいですね。

## gitインストール
gitを使うためにはまずgitをPCへインストールする必要があります。OSへ合うインストール方法でインストールしてください。

## gitをMacへインストール
gitをMacへインストールするため下記のリンクを押してインストールファイルをダウンロードします。

- ダウンロードリンク: [https://git-scm.com/download/mac](https://git-scm.com/download/mac){:rel="nofollow noreferrer" :target="_blank"}

自動にダウンロードが始めれない方は画面にある```click here to download manually```のリンクを押してダウンロードしてください。

![git download for mac](/assets/images/category/git/installation/download_mac.png)

ファイルダウンロードが終わったらファイルを選択してインストールします。インストール方法は一般的にWebからダウンロードしたファイルをインストールする方法と同じです。セキュリティーのメッセージがでったらMacの設定で確認してインストールします。

インストールが終わったら```termial```を実行して下記のコマンドでgitがインストールされたかを確認します。

```bash
git --version
```

## gitをWindowsへインストール
gitをWindowsへインストールするため下のリンクを押してインストールファイルをダウンロードします。

- ダウンロードリンク: [https://gitforwindows.org/](https://gitforwindows.org/){:rel="nofollow noreferrer" :target="_blank"}

![git download for windows](/assets/images/category/git/installation/download_windows.png)

ダウンロードが終わったら一般的にプログラムをインストールする方法と同じ感じでインストールします。

インストールが終わったら```コマンドプロンプト(cmd)```を実行して下記のコードでgitがインストールされたか確認します。

```bash
git --version
```
コマンドプロンプトは```windowsキー + r```を押して```cmd```を入力してエンターを押して実行することもできます。

## 完了
gitインストールが終わりました。今後はgitを使ってソースコードのバージョン管理について勉強してみましょう。