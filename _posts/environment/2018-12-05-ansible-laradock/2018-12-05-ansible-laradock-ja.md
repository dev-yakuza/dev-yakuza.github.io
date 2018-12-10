---
layout: 'post'
permalink: '/environment/ansible-laradock/'
paginate_path: '/environment/:num/ansible-laradock/'
lang: 'ja'
categories: 'environment'
comments: true

title: 'アンシブル&Laradock'
description: 'vagrantとアンシブル(Ansible)を使って作った仮想マシン(guest system)にLaradockを使ってララベル(Laravel)開発環境を作ってみます。'
image: '/assets/images/category/environment/ansible-laradock.jpg'
---


## 概要
最近世の中は本当にないものがないです。私たちが考えてることはすでに世の中どこか存在して共有されています。Laradockはララベル(Laravel)の開発環境へ必要な物をドッカー(Docker)で作って管理するプロジェクトです。もっと詳しく内容は公式サイトを参考してください。([https://github.com/laradock/laradock/](https://github.com/laradock/laradock/){:rel="nofollow noreferrer" target="_blank"}). このブログではLaradockを使ってララベル(Laravel)開発環境を作る方法について説明します。

このブログは下記のブログのシリーズです。理解のため下記のブログを先見ることをお勧めします。

- [vagrantインストールや使い方]({{site.url}}/{{page.categories}}/vagrant-install-and-usage/){:target="_blank"}
- [アンシブルインストール]({{site.url}}/{{page.categories}}/install-ansible/){:target="_blank"}
- [アンシブルプレイブック]({{site.url}}/{{page.categories}}/ansible-playbook/){:target="_blank"}
- [アンシブル&ドッカー]({{site.url}}/{{page.categories}}/ansible-docker/){:target="_blank"}


## 開発環境構成
Laradockは開発環境を構成のため色んなドッカー(Docker)を提供してます。したがって、自分が開発したい環境に合わせてドッカー(Docker)を選択してインストールする必要があります。私たちは下記の項目で開発環境を構成する要諦です。

- nginx
- mysql
- phpmyadmin
- workspace

## 仮想マシン設定修正
仮想マシンの(guest system)の設定を修正するため下記のように```Vagrantfile```を修正します。

```ruby
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  ...
  config.vm.provider :virtualbox do |vb|
    vb.name = "laravel-dev"
  end
  config.vm.network "forwarded_port", guest: 80, host: 80
  config.vm.network "forwarded_port", guest: 8080, host: 8080
  ...
  config.trigger.after :up do |trigger|
    trigger.name = "trigger Docker after Vagrant Up"
    trigger.run_remote = {inline: "sudo ansible-playbook /vagrant/ansible/playbook.yml --tags 'docker'"}
  end
end
```

仮想マシン(guest system)がvirtualboxで表示される名前を```vb.name```を使って特定な名前(```laravel-dev```)を設定しました。この部分は実際開発環境構成とは関係ありません。ただ、virtualboxに表示される名前を分かりやすくするためです。

vagrantの```config.vm.network "forwarded_port"```を使ってローカルマシン(host system)のポートを仮想マシン(guest system)のポートに連結(port-forward)させました。今からローカルマシン(host system)のポートを使って仮想マシン(guest system)のポートに接続ができます。80ポートはララベル(Laravel)プロジェクトのため、8080はphpmyadminへ接続するため連結しました。

仮想マシン(guest system)をvagrantコマンド(```vagrant halt```)で中止させてまたvagrantコマンド(```vagrant up```)で仮想マシン(guest system)を再起動したら、以前アンシブルプレイブック(Ansible Playbook)実行スクリプトはプロビジョンシェル(provision shell)中にあるので実行れないです。さらに、Laradockのドッカー(Docker)はいつも再起動(restart always)が設定されてないので仮想マシンが(guest system)が再起動する時ドッカー(Docker)が起動されないです。だから、私たちはVagrantfileに下のように追加しました。

```ruby
config.trigger.after :up do |trigger|
  trigger.name = "trigger Docker after Vagrant Up"
  trigger.run_remote = {inline: "sudo ansible-playbook /vagrant/ansible/playbook.yml --tags 'docker'"}
end
```

この設定は私たちが```vagrant up```コマンドで仮想マシン(guest system)を実行した後、実行される内容を定義します。この仮想マシン(guest system)にアンシブルプレイブック(Ansible Playbook)を実行するように設定します。アンシブルプレイブック(Ansible Playbook)コマンドがプロビジョンシェル(provision shell)にあるコマンドと違って```--tags 'docker'```が入っています。このオプションを使ったら```docker```とタグ(tag)されたコマンドだけ実行することができます。もっと詳しく内容は下のアンシブルプレイブック(Ansible Playbook)設定でもう一度説明します。

## アンシブルプレイブックへLaradock設定
以前のブログに続いてアンシブルプレイブック(Ansible Playbook)を使って開発環境構成を進めます。今まで構成したフォルダ構造は下記のようです。

```bash
|-- ansible
|    |-- init
|    |    |-- tasks
|    |    |    |-- main.yml
|    |-- docker
|    |    |-- tasks
|    |    |    |-- main.yml
|    |-- playbook.yml
|-- Vagrantfile
```

ここにLaradockのための```role```を定義するため下のように```laradock/tasks/main.yml```ファイルを追加します。

```bash
|-- ansible
|    |-- init
|    |    |-- tasks
|    |    |    |-- main.yml
|    |-- docker
|    |    |-- tasks
|    |    |    |-- main.yml
|    |-- laradock
|    |    |-- tasks
|    |    |    |-- main.yml
|    |-- playbook.yml
|-- Vagrantfile
```

アンシブルプレイブック(Ansible Playbook)のスタートポイントである```playbook.yml```ファイルにLaradockの```role```を追加します。

```yml
---
- hosts: localhost
  connection: local
  roles:
    - init
    - docker
    - laradock
```

追加した```laradock/tasks/main.yml```ファイルを下記のように修正します。

```yml
---
- name: git clone Laradock
  git: repo=https://github.com/Laradock/laradock.git dest=/vagrant/app/laradock/ version=master

- name: copy Laradock environment file
  copy: src=/vagrant/app/laradock/env-example dest=/vagrant/app/laradock/.env

- name: change mysql version
  replace:
    path: /vagrant/app/laradock/.env
    regexp: 'MYSQL_VERSION=*.*'
    replace: 'MYSQL_VERSION=5.7'
  tags:
    - replace

- name: change project folder
  replace:
    path: /vagrant/lib/laradock/.env
    regexp: 'APP_CODE_PATH_HOST=*.*'
    replace: 'APP_CODE_PATH_HOST=/vagrant/app'
  tags:
    - replace

- name: dokcer compose Laradock(nginx, mysql, phpmyadmin, workspace)
  docker_service:
    state: present
    project_src: /vagrant/app/laradock
    services:
        - nginx
        - mysql
        - phpmyadmin
        - workspace
  tags:
    - docker
```

追加したアンシブルプレイブック(Ansible Playook)の```role```をみてみましょう。

```yml
- name: git clone Laradock
  git: repo=https://github.com/Laradock/laradock.git dest=/vagrant/app/laradock/ version=master
```

アンシブル(Ansible)のgitモジュールを使ってLaradockのリポジトリ(repository)をコピー(clone)します。

```yml
- name: copy Laradock environment file
  copy: src=/vagrant/app/laradock/env-example dest=/vagrant/app/laradock/.env
```

Laradockの設定ファイルの例(```env-example```)を使える設定ファイル(```.env```)にコピーします。

```yml
- name: change mysql version
  replace:
    path: /vagrant/app/laradock/.env
    regexp: 'MYSQL_VERSION=*.*'
    replace: 'MYSQL_VERSION=5.7'
  tags:
    - replace
```

Laradockの環境ファイルである```.env```に```mysql```バージョンを```5.7```で変更します。最新のバージョン(```8.0```)は使った場合ララベル(Laravel)からmysqlへ接続すると下記のようなエラーが発生します。

```bash
[PDOException]
SQLSTATE[HY000] [2054] The server requested authentication method unknown to the client
```

最新のmysqlの暗号認証方式がララベル(Laravel)から提供しなくて問題が発生してるみたいです。色んな解決方法がありますがmysql 8.0の機能をあまり使ってない場合、5.7でダウングレード(Downgrade)して使うことをお勧めします。

```yml
- name: change project folder
  replace:
    path: /vagrant/lib/laradock/.env
    regexp: 'APP_CODE_PATH_HOST=*.*'
    replace: 'APP_CODE_PATH_HOST=/vagrant/app'
  tags:
    - replace
```

Laradockのworkspaceドッカー(Docker)は私たちが作るララベル(Laravel)プロジェクトが入る環境です。このドッカー(Docker)は```APP_CODE_PATH_HOST```を参考してドッカー(Docker)をビルドや起動する時、ここに設定されたフォルダを同期化(synce)してララベル(Laravel)プロジェクトを起動します。基本設定は```APP_CODE_PATH_HOST=../```なのでLaradockの上位フォルダを指定しています。この部分を私たちは```/vagrant/app```で変更して使ってます。皆さんは皆さんのララベル(Laravel)プロジェクトのフォルダの位置で変更するか皆さんのララベル(Laravel)プロジェクトのフォルダ名をappで変更して使ったらいいと思います

```yml
- name: dokcer compose Laradock(nginx, mysql, phpmyadmin, workspace)
  docker_service:
    debug: true
    state: present
    restarted: true
    project_src: /vagrant/app/laradock
    services:
        - nginx
        - mysql
        - phpmyadmin
        - workspace
  tags:
    - docker
```

アンシブル(Ansible)のドッカーサービス(Docker Service)モジュールを使って私たちが必要なドッカー(Docker)をビルドして実行します。また、別のコマンドと違って```tag```機能を使っています。アンシブルプレイブック(Ansible Playbook)を実行する時```--tags```オプションを使ってタグ(tag)されたコマンド中で実行したいコマンドだけ実行することが可能です。```--tags```オプションが設定されてないアンシブルプレイブック(Ansible Playboo)を実行すると全てのコマンドが実行されます。

```bash
# 全てのコマンド実行
sudo ansible-playbook /vagrant/ansible/playbook.yml
# dockerでタグ(tag)されたコマンドだけ実行
sudo ansible-playbook /vagrant/ansible/playbook.yml --tags 'docker'
```

## アンシブルプレイブック実行
アンシブルプレイブック(Ansible Playbook)でLaradockの```role```設定は終わりました。アンシブルプレイブック(Ansible Playbook)を実行してLaradockをインストールしてみましょう。

```bash
# vagrant ssh
sudo ansible-playbook /vagrant/ansible/playbook.yml
```

## Laradockインストール確認
アンシブルプレイブック(Ansible Playbook)でLaradockが上手くインストールされたか下記のドッカー(Docker)コマンドで確認します。

```bash
# vagrant ssh
sudo docker ps
```

また、ローカルマシン(host system)で```http://localhost```を実行して```nginx```の```404 Not Foud```エラー画面が表示されます。

## 完了
アンシブル(Ansible)を使ってLaradockをインストールしてララベル(Laravel)開発環境を準備しました。今はララベル(Laravel)プロジェクトが設定されてないので```404 Not Found```エラーが見えますが、開発環境は上手くインストールされました。次はLaradock開発環境にララベル(Laravel)プロジェクトを設定してみます。

## 参考
- [https://laradock.io/documentation/](https://laradock.io/documentation/){:rel="nofollow noreferrer" target="_blank"}
