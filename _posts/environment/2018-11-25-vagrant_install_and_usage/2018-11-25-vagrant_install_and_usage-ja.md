---
layout: 'post'
permalink: '/environment/vagrant-install-and-usage/'
paginate_path: '/environment/:num/vagrant-install-and-usage/'
lang: 'ja'
categories: 'environment'
comments: true

title: 'vagrantインストールや使い方'
description: '仮想マシンを使って開発環境を構築するためvirtualbox, vagrantをインストールする方法や仮想マシンを作るためvagrantを使う方法について紹介します。'
image: '/assets/images/category/environment/vagrant-install-and-usage.jpg'
---


## 概要
バックエンド(backend) - サーバーを開発するためサーバーは同一な環境を構築しようとします。ここにはvagrantを使って仮想マシンを作る方法を紹介します。

## virtualboxインストール
vagrantは仮想マシンを簡単に作って管理してくれるツールです。つまり、仮想環境の上に仮想マシンをインストールして管理してくれるツールです。したがって、仮想マシンを実行する仮想環境はvagrantの管理外です。仮想環境を作ってくれる色んなツールがありますがここではvirtualboxを使って紹介します。

下のリンクを押してvirtualboxのダウンロードページへ移動します。

- virtualbox: [https://www.virtualbox.org/wiki/Downloads](https://www.virtualbox.org/wiki/Downloads){:rel="nofollow noreferrer" target="_blank"}

下記のような画面で自分のPCにダウンロードファイルをダウンロードしてインストールします。

![virtualbox donwload page](/assets/images/category/environment/vagrant-install-and-usage/virtualbox_download.png)

virtaulboxダウンロードやインストールするプロセスは一般的なソフトをインストールする方法と同じなのでここでは説明を省略します。

インストールを完了してvirtualboxを実行したら下記のような画面が見えます。

![virtualbox installed](/assets/images/category/environment/vagrant-install-and-usage/virtualbox_installed.png)

## vagrantインストール
virtualboxインストールで今からは仮想環境を作ることが可能になりました。今度は仮想環境で実行される仮想マシンを簡単に作ってくれるvagrantのインストール方法を紹介します。

下のリンクを押してvagrantダウンロードサイトへ移動します。

- vagrant: [https://www.vagrantup.com/downloads.html](https://www.vagrantup.com/downloads.html){:rel="nofollow noreferrer" target="_blank"}

上のリンクを押してvagrantダウンロードサイトへ移動したら下記のような画面が見えます。

![vagrant download site](/assets/images/category/environment/vagrant-install-and-usage/vagrant_site.png)

自分のPCのOSに合うインストールファイルを選択してダウンロードします。今回もvagrantのダウンロードやインストール方法は一般的ソフトをダウンロドしてインストールする方法と同じなので説明を省略します。

インストールが終わったら下記のコマンドを実行してvagrantがインストールされたかを確認します。

```bash
vagrant --version
```

vagrantがインストールされたら下のようにvagratのバージョンの確認が出来ます。

```bash
Vagrant 2.2.1
```

## box追加
vagrantが仮想マシンを作るために使うboxを追加します。boxは仮想マシンになるOSやOSへ含めてるソフトを集めたパッケージです。下記は基本になる公式boxとvagrantユーザーたちが作ったboxのサイトです。

- 公式boxサイト: [https://app.vagrantup.com/boxes/search](https://app.vagrantup.com/boxes/search){:rel="nofollow noreferrer" target="_blank"}
- ユーザーboxサイト: [http://www.vagrantbox.es/](http://www.vagrantbox.es/){:rel="nofollow noreferrer" target="_blank"}

下のvagrantコマンドでboxを自分のPCへ追加します。

- 公式box追加

```bash
vagrant box add centos/7
```

- ユーザーbox追加

```bash
vagrant box add centos66  https://github.com/tommy-muehle/puppet-vagrant-boxes/releases/download/1.0.0/centos-6.6-x86_64.box
```

私たちは公式boxの```bento/ubuntu-16.04```を使う予定です。

- 公式```bento/ubuntu-16.04```:[https://app.vagrantup.com/bento/boxes/ubuntu-16.04](https://app.vagrantup.com/bento/boxes/ubuntu-16.04){:rel="nofollow noreferrer" target="_blank"}

下のvagrantコマンドで```bento/ubuntu-16.04```boxを自分のPCへ追加します。

```bash
vagrant box add bento/ubuntu-16.04
```

下のvagrantコマンドで追加されたboxのリストを確認することが出来ます。

```bash
vagrant box list
```

もしboxを間違って追加したら下記のvagrantコマンドで追加されたboxを消すことが出来ます。

```bash
vagrant box remove bento/ubuntu-16.04
```

## 仮想マシン設定生成
下記のvagrantコマンドでvagrantと追加したboxを使って仮想マシンを設定生成します。

```bash
# mkdir create your project folder
mkdir temp
cd temp
vagrant init bento/ubuntu-16.04
```

コマンドを実行したフォルダ(temp)へ```Vagrantfile```ファイルが生成されたことを確認出来ます。下記はコメントアウト(```#```)を消した```Vagrantfile```の内容です。

```ruby
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-16.04"
end
```

## 仮想マシン生成
上で作った```Vagrantfile```を下のvagrantコマンドでvagrantを使って仮想マシンを生成します。

```bash
vagrant up
```

私たちがインストール下```virtualbox```を実行して見たら仮想マシンが生成されたことが確認出来ます。

![virtualbox with virtual machine](/assets/images/category/environment/vagrant-install-and-usage/virtualbox-with-machine.png)

下記のvagrantコマンドで仮想マシンへ接続が出来ます。

```bash
vagrant ssh
```

下のコマンドで仮想マシンからローカルPC環境に戻ることも可能です。

```bash
exit
```

## 仮想マシン中止
仮想マシンを中止したい時は、下記のvagrantコマンドを実行します。

```bash
vagrant halt
```

## 仮想マシン削除
仮想マシンがもういらない時、下記のvagrantコマンドで仮想マシンを削除します。

```bash
vagrant destroy
```

## 完了
これでvagrantを使って仮想マシンを生成する方法を見てみました。今後は```Vagrantfile```ファイルを修正したら仮想マシン中へ開発環境を構築する方法を紹介する要諦です。