---
layout: 'post'
permalink: '/environment/nvm/'
paginate_path: '/environment/:num/nvm/'
lang: 'ja'
categories: 'environment'
comments: true

title: (macOS) NVMでNodeのバージョン管理
description: macOSへNVM(Node Version Manager)をインストールしてNodeのバージョンを管理する方法について説明します。
image: '/assets/images/category/environment/2020/nvm/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [外洋](#外洋)
- [NVMインストール](#nvmインストール)
- [NVM設定](#nvm設定)
- [使い方](#使い方)
  - [Nodeのバージョンリスト](#nodeのバージョンリスト)
  - [Nodeインストール](#nodeインストール)
  - [Nodeのバージョン変更](#nodeのバージョン変更)
- [Nodeのバージョン削除](#nodeのバージョン削除)
- [プロジェクト別Nodeのバージョン管理](#プロジェクト別nodeのバージョン管理)
  - [.nvmrc生成](#nvmrc生成)
  - [.nvmrc使い方](#nvmrc使い方)
- [完了](#完了)

</div>

## 外洋

私はMacユーザです。Macで色んなプロジェクトを進めていますが、プロジェクト別でNodeのバージョンを管理する必要がありました。このブログポストでは`NVM(Node Version Manager)`を使ってNodeのバージョンを管理する方法について説明します。

- NVM(Node Version Manager): [公式サイト](https://github.com/nvm-sh/nvm){:rel="nofollow noreferrer" target="_blank"}

ここで紹介する方法はmacOS専用で、macOSには`Homebrew`がインストールされたと思って説明します。

## NVMインストール

下記のコマンドを使ってNVMをインストールします。

```bash
brew install nvm
```

{% include in-feed-ads.html %}

## NVM設定

TerminalでNVMを使うためには`.zshrc`ファイルを修正する必要があります。`.zshrc`ファイルを開いて下記のように修正します。

```bash
# code ~/.zshrc
...
export NVM_DIR=~/.nvm
source $(brew --prefix nvm)/nvm.sh
```

設定が完了されたら、Terminalを再起動して、下記のコマンドを実行してNVMがうまくインストールされてるか確認します。

```bash
nvm --version
```

問題なくインストールしたら、下記のような結果が確認できます。

```bash
0.35.3
```

## 使い方

インストールが完了しました。今からNVMを使ってNodeのバージョンを管理する方法について説明します。

### Nodeのバージョンリスト

下記のコマンドでインストール可能なNodeのバージョンを確認することができます。

```bash
nvm ls-remote
```

### Nodeインストール

バージョンを確認したら、下記のコマンドで使うNodeをインストールします。

- 最新のNodeバージョンインストール

  ```bash
  nvm install node
  ```

- 最新のLTS releaseバージョンインストール

  ```bash
  nvm install --lts
  ```

- 特定したバージョンのNodeインストール

  ```bash
  nvm install 13.12.0
  ```

このようにインストールしたら、下記のコマンドで現在インストールされたNodeバージョンを確認することができます。

```bash
nvm ls
```

{% include in-feed-ads.html %}

### Nodeのバージョン変更

NVMを使って色んなバージョンのNodeをインストールしたら、下記のコマンドを使って、使いたいNodeを選択することができます。

```bash
nvm use 13.12.0
```

下記のコマンドを使ってNodeのバージョンがうまく変更されたか確認します。

```bash
nvm ls
```

うまく変更されたら、下記のような結果が見えます。

```bash
       v8.9.0
       v12.16.1
->     v13.12.0
         system
```

## Nodeのバージョン削除

下記のコマンドを使って要らないNodeのバージョンを削除することができます。

```bash
nvm uninstall 8.9.0
```

削除されたら、下記のような結果が見えます。

```bash
Uninstalled node v8.9.0
```

## プロジェクト別Nodeのバージョン管理

NVMを使ってLocalに色んなバージョンのNodeをインストールして、使う方法について見てみました。次は、各プロジェクト別Nodeのバージョンを管理する方法について説明します。

### .nvmrc生成

各プロジェクト別Nodeのバージョンを管理するためには`.nvmrc`ファイルを生成する必要があります。プロジェクトのRootフォルダへ`.nvmrc`ファイルを生成して下記のように修正します。

```bash
12.16.1
```

{% include in-feed-ads.html %}

### .nvmrc使い方

このように設定したNodeのバージョンを使うため、下記のコマンドを`.nvmrc`ファイルがあるフォルダで実行します。

```bash
nvm use
```

もし、`.nvmrc`ファイルに設定されたNodeのバージョンがLocalの環境に存在する場合は下記のような結果が見えます。

```bash
Found '/projects/.nvmrc' with version <12.16.1>
Now using node v12.16.1 (npm v6.13.4)
```

もし、Localの環境へ存在しない場合は下記のような結果が表示されます。

```bash
Found '/projects/.nvmrc' with version <8.9.0>
N/A: version "8.9.0 -> N/A" is not yet installed.

You need to run "nvm install 8.9.0" to install it before using it.
```

上のように`.nvmrc`ファイルへあるNodeのバージョンがない場合は、下記のコマンドを使ってNodeのバージョンをインストールすることができます。

```bash
nvm install
```

インストールが完了されたら下記のような結果が表示されます。

```bash
...
Checksums matched!
Now using node v8.9.0 (npm v5.5.1)
```

## 完了

このブログポストではNVM(Node Version Manager)を使ってLocalへ色んなバージョンのNodeをインストールする方法と使う方法を見てみました。また、プロジェクト別Nodeのバージョンを管理するため、`.nvmrc`ファイルを生成して、`.nvmrc`ファイルを使ってNodeのバージョンをインストールや使う方法についても見てみました。

今から、.nvmrcファイルを使ってプロジェクト別にNodeのバージョンを管理してみましょう！
