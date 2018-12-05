---
layout: 'post'
permalink: '/environment/ansible-playbook/'
paginate_path: '/environment/:num/ansible-playbook/'
lang: 'ja'
categories: 'environment'
comments: true

title: 'アンシブルプレイブック'
description: 'アンシブルプレイブック(Ansible Playbook)を使ってサーバー構築に必要なプログラムのインストールや基本設定をしてみます。'
image: '/assets/images/category/environment/ansible-playbook.jpg'
---


## 概要
以前のブログでインストールしたアンシブル(Ansible)のプレイブック(Playbook)を使ってサーバーを構築します。基本的にサーバー構築へ必要なプログラムインストールや設定をするためアンシブルプレイブック(Ansible Playbook)を使う予定です。このブログでは基本的vagrantを使って仮想マシン(guest system)を作ってその中にアンシブル(Ansible)をインストールして進めます。

- vagrantをインストールする方法については以前のブログの[vagrantインストールや使い方]({{site.url}}/{{page.categories}}/vagrant-install-and-usage/){:target="_blank"}を確認してください。
- vagrantにアンシブル(Ansible)をインストールする方法については[アンシブルインストール]({{site.url}}/{{page.categories}}/install-ansible/){:target="_blank"}を見てください。

このブログは上の2つのブログの内容を実行したと仮定して説明します。

## アンシブルプレイブック生成
現在```Vagrantfile```ファイルが存在するフォルダへ```ansible``の名前でフォルダを作ります。

```bash
|-- ansible
|-- Vagrantfil
```

生成した```ansible```フォルダに```playbook.yml```ファイルを生成します。アンシブル(Ansible)の全ての内容は```ヤムル(yml)```ファイル形式と文法で作ります。だから、```ヤムル(yml)```で使える全てのことが使えます。

```bash
|-- ansible
|    |-- playbook.yml
|-- Vagrantfil
```

生成した```playbook.yml```ファイルはアンシブル(Ansible)のスタート点です。```playbook.yml```を下のように作成します。

```yml
---
- hosts: localhost
  roles:
    - init
```

以前のブログでも紹介したがアンシブル(Ansible)はインフラに関する全般的な自動化ツールです。したがって、ローカルサーバー(local server)以外でもリモートサーバー(remote server)のインフラも管理することが出来ます。```hosts```はアンシブル(Ansible)を使ってインフラを構築する対象、つまりローカル(local server)やリモートサーバー(remote server)を指定することができます。私たちは現在開発サーバーを構築してるので```hosts```には```localhost```を設定します。

アンシブル(Ansible)は１つのプレイブック(playbook)ファイルで全てのインフラ構築内容を定義することもできますが```roles```を使って複数のファイルで管理することも可能です。```roles```下に分離して管理したいフォルダリストを設定します。このブログでは```init```フォルダを1つ生成する予定ですので```- init```を追加しました。

```bash
|-- ansible
|    |-- init
|    |    |-- tasks
|    |    |    |-- main.yml
|    |-- playbook.yml
|-- Vagrantfil
```

上のように```ansible```フォルダ下へ```init/tasks/main.yml```ファイルを生成した下記の内容を追加します。

```yml
---
- name: Make app directory
  file: path=/var/www state=directory mode=0755

- name: Symbolic link
  file: src=/vagrant dest=/var/www/vhosts state=link

- name: Set timezone to Asia/Tokyo
  timezone:
    name: Asia/Tokyo

- name: Update and upgrade apt packages
  become: true
  apt:
    upgrade: yes
    update_cache: yes
    cache_valid_time: 86400

- name: Add python3.6 repo
  apt_repository:
    repo: 'ppa:jonathonf/python-3.6'

- name: Install basic packages
  become: true
  apt:
    pkg:
      - git
      - unzip
      - python3.6
      - python-pip
      - python3-pip
      - fabric
    state: present
    update_cache: yes
```

アンシブル(Ansible)のコマンドを一つ一つ見てみます。

```yml
- name: Make app directory
  file: path=/var/www state=directory mode=0755
```

これがアンシブル(Ansible)の1つのコマンドです。```name```は現在のコマンドを区分するためものでこのコマンドはアンシブル(Ansible)の```file```コマンドを使ってフォルダを生成する部分です。

```yml
- name: Symbolic link
  file: src=/vagrant dest=/var/www/vhosts state=link
```

フォルダを管理をするため```/vagrant```フォルダと```/var/www/vhosts```フォルダを連携します。

```yml
- name: Set timezone to Asia/Tokyo
  timezone:
    name: Asia/Tokyo
```

ローカルサーバーのタイムゾーン(timezone)を設定します。

```yml
- name: Update and upgrade apt packages
  become: true
  apt:
    upgrade: yes
    update_cache: yes
    cache_valid_time: 86400
  tags:
    - packages
```

Linuxのパッケージ管理ツールの```apt-get```をアップデートします。```become: true```で管理者権限(root)でこのアンシブル(Ansible)コマンドを実行します。

```yml
- name: Add python3.6 repo
  apt_repository:
    repo: 'ppa:jonathonf/python-3.6'
```

アンシブル(Ansible)のモジュール中でパイソン(python)に依存するモジュールがあってパイソン(python)をインストールする必要があります。パイソン(python)をインストールするためパイソンのレポジトリ(repository)を追加します。

```yml
- name: Install basic packages
  become: true
  apt:
    pkg:
        - git
        - unzip
        - python3.6
        - python-pip
        - python3-pip
        - fabric
    state: present
    update_cache: yes
```

あとで必要な基本プログラム(git, unzip)とパイソン(python)と関係あるプログラムをインストールします。

## Vagrantfile修正
既存の```Vagrantfile```に下記の内容を追加します。

```ruby
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
 ...

  config.vm.provision "shell", inline: <<-SHELL
    ...
    sudo ansible-playbook /vagrant/ansible/playbook.yml
  SHELL

  config.vm.synced_folder ".", "/vagrant"
end
```

以前のブログで使ったプロビジョンシェル(provision shell)に```ansible-playbook /vagrant/ansible/playbook.yml```を追加しました。今から```vagrant up```または```vagrant provision```コマンドを実行すると私たちが作ったアンシブルプレイブック(Ansible Playbook)が自動に実行されます。

また```config.vm.synced_folder ".", "/vagrant"```コマンドを使ってローカルマシン(host system)のフォルダを仮想マシン(guest system)の```/vagrant```へアップロードして同期化(sync)します。今からはローカルマシン(host system)でファイルを修正したら仮想マシン(guest system)へ自動に反映されます。

## テスト
今まで作ったアンシブルプレイブック(Ansible Playbook)とVagrantfileを使って自動でサーバーを設定してみましょう。既存の仮想マシン(guest system)が起動中だったら下記のvagrantコマンドで仮想マシン(guest system)を削除します。

```bash
vagrant destroy
```

下のvagrantコマンドで仮想マシン(guest system)を生成します。このように生成したら以前と違って私たちが作成したアンシブルプレイブック(Ansible Playbook)が起動してることをコンソール(console)で確認できます。

```bash
vagrant up
```

生成されたら下記のvagrantコマンドで仮想マシン(guest system)へ接続します。

```bash
vagrant ssh
```

下のコマンドでVagrantfileとアンシブルプレイブック(Ansible Playbook)が上手く動作したかを確認します。

```bash
cd /vagrant
ls

git --version
unzip -v
```

## 完了
今回のブログではアンシブルプレイブック(Ansible Playbook)を使って仮想マシン(guest system)へ基本的必要なプログラムをインストールしてみました。これを通じてアンシブルプレイブック(Ansible Playbook)をどうやって使うかもみました。また```Vagrantfile```ファイルを修正して仮想マシン(guest system)を生成する時アンシブルプレイブック(Ansible Playbook)を自動に実行されるように作ったりVagrantfileが実行されたフォルダと仮想マシン(Ansible Playbook)の```/vagrant```フォルダと同期化する方法もみてみました。

アンシブルプレイブック(Ansible Playbook)をもっと上手く使う必要がありますが、私たちは単純に使ってるのでちょっと恥ずかしいですね。下にアンシブルのドキュメント(Ansible Document)サイトのリンクを紹介します。そのドキュメントをみってもっと美しくアンシブル(Ansible)を使ってみてください。

次のブログではdockerの開発環境を追加してみます。



## 参考
- アンシブルドキュメント(Ansible Document): [https://docs.ansible.com/](https://docs.ansible.com/){:rel="nofollow noreferrer" target="_blank"}