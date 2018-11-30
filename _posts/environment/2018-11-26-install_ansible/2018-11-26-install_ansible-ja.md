---
layout: 'post'
permalink: '/environment/install-ansible/'
paginate_path: '/environment/:num/install-ansible/'
lang: 'ja'
categories: 'environment'
comments: true

title: 'アンシブルインストール'
description: 'vagrantで生成した仮想マシン(guest system)へアンシブル(Ansible)をインストールしてアンシブル(Ansible)を使える環境を作ります。'
image: '/assets/images/category/environment/install-ansible.jpg'
---


## 概要
アンシブル(Ansible)を説明すると本一冊が必要です。私たちもそんな詳しく知らなく別の人に説明するレベルでもないので詳しくは説明できないですが私たちが使ってる方法を紹介することでアンシブル(Ansible)を紹介してみようかと思います。アンシブル(Ansible)を簡単に説明したらインフラに関する全般的な自動化ツールです。インストール(installation)やデプロイ(deploy)など様々なことを自動化することができます。このブログではvagrantへアンシブル(Ansible)をインストールする方法に関して説明します。

このブログポストはPCへvirtualbox, vagrantがインストールされた環境を対象にしてます。virtualbox, vagrantをインストールする方法は以前のブログ[vagrantインストールや使い方]({{site.url}}/{{page.categories}}/vagrant-install-and-usage/){:target="_blank"}を確認してください。

## 仮想マシン設定生成
下記のvagrantコマンドで仮想マシン(guest system)を設定します。

```bash
vagrant init bento/ubuntu-16.04
```

vagrantコマンドを実行したフォルダへ```Vagrantfile```ファイルが生成されたことが確認できます。下は```Vagrantfile```でコメントアウト(```#```)を削除した内容です。

```ruby
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-16.04"
end
```

## 仮想マシン生成や確認
下のvagrantコマンドで仮想マシン(guest system)を生成します。

```bash
vagrant up
```

仮想マシン(guest system)が生成されたら下のvagrantコマンドで仮想マシン(guest system)へ接続します。

```bash
vagrant ssh
```

## アンシブルインストール設定
仮想マシン(guest system)中で下のコマンドで実行したらまだアンシブル(Ansible)がインストールされてないことが確認できます。

```bash
ansible --version
```

また```Vagrantfile```ファイルを開いて下記のように修正します。

```ruby
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-16.04"

  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update
    sudo apt-get install software-properties-common
    sudo apt-add-repository --yes --update ppa:ansible/ansible
    sudo apt-get install ansible --yes
  SHELL
end
```

プロビジョンシェル(provision shell)は仮想マシン(guest system)へスクリプトをアップロードして実行できるようにします。vagrantのプロビジョンシェル(provision shell)へアンシブル(Ansible)のインストールスクリプトを追加します。

## アンシブルインストール
下記のvagrantコマンドをローカルマシン(host system)で実行します。

```bash
vagrant provision
```

そしてまた仮想マシン(guest system)に接続した後アンシブル(Ansible)がインストールされたことを確認します。

```bash
vagrant ssh

ansible --version
```

問題なくアンシブル(Ansible)がインストールされたら下記のようにアンシブル(Ansible)のバージョンば確認できます。

```bash
ansible 2.7.2
  config file = /etc/ansible/ansible.cfg
  configured module search path = [u'/home/vagrant/.ansible/plugins/modules', u'/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/lib/python2.7/dist-packages/ansible
  executable location = /usr/bin/ansible
  python version = 2.7.12 (default, Dec  4 2017, 14:50:18) [GCC 5.4.0 20160609]
```

今回はプロビジョンシェル(provision shell)でアンシブル(Ansible)を設定しなくて仮想マシン(guest system)を作った後プロビジョンシェル(provision shell)を入力してvagrantコマンド(```vagrant provision```)でアンシブル(Ansible)をインストールしました。

しかし、別のPCや新しく環境を再構築しする時はさらにプロビジョンシェル(provision shell)が設定された```Vagrantfile```ファイルを利用するので```vagrant up```コマンドを実行するだけでアンシブル(Ansible)がインストールされます。

確認するため下記のvagrantコマンドで仮想マシン(guest system)を削除します。

```bash
vagrant destroy
```

また下のvagrantコマンドで仮想マシン(guest system)を生成します。

```bash
vagrant up
```

生成されたら下記のvagrantコマンドで仮想マシン(guest system)へ接続します。

```bash
vagrant ssh
```

アンシブル(Ansible)がインストールされたか確認するため下のコマンドを実行します。

```bash
ansible --version
```

アンシブル(Ansible)が問題なくインストールされたら下記のような画面をまた見ることができます。

```bash
ansible 2.7.2
  config file = /etc/ansible/ansible.cfg
  configured module search path = [u'/home/vagrant/.ansible/plugins/modules', u'/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/lib/python2.7/dist-packages/ansible
  executable location = /usr/bin/ansible
  python version = 2.7.12 (default, Dec  4 2017, 14:50:18) [GCC 5.4.0 20160609]
```

## 完了
今回のブログではVagrantfileファイルを使ってvagrantへアンシブル(Ansible)をインストールする方法について見ました。アンシブル(Ansible)を上手く使ってる方はなぜこのようにしてるか疑問があると思います。普通はアンシブル(Ansible)をローカルマシン(host system)へインストールして仮想マシン(guest system)へインフラを構築するため使う方が多いと思います。しかし、まだウィンドウズ(Windows)はアンシブル(Ansible)を提供しないので私たちはこのような方法を選べました。次のブログではアンシブル(Ansible)を使ってララベル(Laravel)開発環境を構築する方法を紹介します。