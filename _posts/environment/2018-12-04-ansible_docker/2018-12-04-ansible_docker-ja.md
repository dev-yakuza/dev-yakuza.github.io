---
layout: 'post'
permalink: '/environment/ansible-docker/'
paginate_path: '/environment/:num/ansible-docker/'
lang: 'ja'
categories: 'environment'
comments: true

title: 'アンシブル&ドッカー'
description: 'アンシブルプレイブック(Ansible Playbook)を使ってvagrant仮想マシン(guest system)にドッカー(Docker)とドッカーコンポーズ(Docker Compose)をインストールしてみます。'
image: '/assets/images/category/environment/ansible-docker.jpg'
---


## 概要
サーバー開発にドッカー(Docker)は必須になりました。ここでドッカー(Docker)について全ての説明は難しいと思います。ブログを作成しながらちょっとちょっと説明することでドッカー(Docker)を説明します。このブログではアンシブルプレイブック(Ansible Playbook)を使ってvagrantにドッカー(Docker)とドッカーコンポーズ(Docker Compose)をインストールする方法を紹介します。

このブログは下の3つのブログを全て進めたと思って説明します。

- [vagrantインストールや使い方]({{site.url}}/{{page.categories}}/vagrant-install-and-usage/){:target="_blank"}
- [アンシブルインストール]({{site.url}}/{{page.categories}}/install-ansible/){:target="_blank"}
- [アンシブルプレイブック]({{site.url}}/{{page.categories}}/ansible-playbook/){:target="_blank"}


## アンシブルプレイブックにドッカー設定
今まで作ったvagrant仮想マシン(guest system)のためのディレクトリ(directory)構造は下記の通りです。

```bash
|-- ansible
|    |-- init
|    |    |-- tasks
|    |    |    |-- main.yml
|    |-- playbook.yml
|-- Vagrantfile
```

ここに私たちはドッカー(Docker)インストールに関する```role```を定義してアンシブルプレイブック(Ansible Playbook)に追加する予定です。下記のように```ansible```フォルダ下へ```docker/tasks/main.yml```ファイルを追加します。

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

アンシブルプレイブック(Ansible Playbook)のスタートポイントである```playbook.yml```ファイルを下のように追加します。

```yml
---
- hosts: localhost
  connection: local
  roles:
    - init
    - docker
```

追加した```docker/tasks/main.yml```ファイルを下のように修正します。

```yml
---
- name: Install docker
  shell: curl https://get.docker.com | sh

- name: Modify privilege
  become: true
  shell: usermod -aG docker $USER

- name: Change privilege of docker
  become: true
  file: dest=/usr/bin/docker mode=+x

- name: python docker / docker-compse module
  pip:
    name:
        - docker
        - docker-compose
```

今からアンシブル(Ansible)コマンドを1つずつ見ます。

```yml
- name: Install docker
  shell: curl https://get.docker.com | sh
```

ドッカー(Docker)インストールスクリプトを使ってドッカー(Docker)をインストールします。

```yml
- name: Modify privilege
  become: true
  shell: usermod -aG docker $USER

- name: Change privilege of docker
  become: true
  command: chmod +x /usr/bin/docker
```

ドッカー(Docker)のユーザーや権限を変更します。

```yml
- name: python docker / docker-compse module
  pip:
    name:
        - docker
        - docker-compose
```

パイソン(python)のpipを使ってパイソンドッカーモジュール(python docker module)とドッカーコンポーズ(Docker Compose)をインストールします。

## アンシブル実行
上でアンシブルプレイブック(Ansible Playbook)へ追加したドッカー(Docker)インストール```role```を実行するため下のアンシブル(Ansible)コマンドを仮想マシン(guest system)で実行します。

```bash
vagrant ssh

sudo ansible-playbook /vagrant/ansible/playbook.yml
```

すでに環境がある状態で進めるのでアンシブルプレイブック(Ansible Playbook)を実行しました。新しく開発環境を作るときはvagrantのプロビジョンシェル(provision shell)へアンシブルプレイブック(Ansible Playbook)実行スクリプトを追加したので自動に実行されます。

確認するため下記のvagrantコマンドをローカルマシン(host system)で実行します。

```bash
vagrant destroy
vagrant up
```

## ドッカーインストール確認
ドッカー(Docker)がアンシブルプレイブック(Ansible Playbook)で仮想マシン(guest system)に上手くインストールされたかを確認するため下記のドッカー(Docker)コマンドで確認します。

```bash
vagrant ssh

docker --version
docker-compose --version
```

## 完了
アンシブルプレイブック(Ansible Playbook)でドッカー(Docker)とドッカーコンポーズ(Docker Compose)を追加して仮想マシン(guest system)へインストールする方法を見ました。今からはドッカー(Docker)を使って好きな開発環境を作ることができます。次のブログではドッカー(Docker)とドッカーコンポーズ(Docker Compose)を使ってララベル(Laravel)開発環境を作る方法について説明します。