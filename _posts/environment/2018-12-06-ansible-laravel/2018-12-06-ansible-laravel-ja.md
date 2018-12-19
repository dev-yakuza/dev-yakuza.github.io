---
layout: 'post'
permalink: '/environment/ansible-laravel/'
paginate_path: '/environment/:num/ansible-laravel/'
lang: 'ja'
categories: 'environment'
comments: true

title: 'アンシブル&ララベル'
description: 'アンシブル(Ansible)とLaradockで作った開発環境にララベル(Laravel)をインストールして開発環境を構成してみます。'
image: '/assets/images/category/environment/ansible-laravel.jpg'
---


## 概要
以前のブログでアンシブル(Ansible)を使ってLaradockをインストールしました。今回はララベル(Laravel)を開発するためララベル(Laravel)をインストールしてララベル(Laravel)プロジェクトを生成してみます。

このブログは下記のブログのシリーズです。理解のため下記のブログを先見ることをお勧めします。

- [vagrantインストールや使い方]({{site.url}}/{{page.categories}}/vagrant-install-and-usage/){:target="_blank"}
- [アンシブルインストール]({{site.url}}/{{page.categories}}/install-ansible/){:target="_blank"}
- [アンシブルプレイブック]({{site.url}}/{{page.categories}}/ansible-playbook/){:target="_blank"}
- [アンシブル&ドッカー]({{site.url}}/{{page.categories}}/ansible-docker/){:target="_blank"}
- [アンシブル&Laradock]({{site.url}}/{{page.categories}}/ansible-laradock/){:target="_blank"}

## phpとcomposer設定
自分のローカルマシン(host system)にphpとcomposerがインストールされたらこの段階はスキップしてもいいです。ララベル(Laravel)プロジェクトを生成するためphpとcomposerを仮想マシン(guest system)にインストールする予定です。

今まで作ったフォルダにphpとcomposerをインストールするアンシブルプレイブック(Ansible Playbook)の```role```を追加します。

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
|    |-- php
|    |    |-- tasks
|    |    |    |-- main.yml
|    |-- playbook.yml
|-- Vagrantfile
```

アンシブルプレイブック(Ansible Playbook)ファイルにも新しく追加したphpの```role```を追加します。

```yml
---
- hosts: localhost
  connection: local
  roles:
    - init
    - docker
    - laradock
    - php
```

追加したアンシブルプレイブック(Ansible Playbook)の```role```ファイルである```php/tasks/main.yml```ファイルを下記のように修正します。

```yml
---
- name: Add php7.2 repo
  apt_repository:
    repo: 'ppa:ondrej/php'
  tags: php

- name: Install php
  become: true
  apt:
    pkg:
      - php7.2
      - php7.2-mbstring
      - php7.2-xml
    state: present
    update_cache: yes
  tags: php

- name: check composer
  stat: path=/usr/local/bin/composer
  register: composer_bin
  tags: php

- block:
  - name: download composer
    get_url:
      url: https://getcomposer.org/installer
      dest: /tmp/installer

  - name: install composer
    shell: cat /tmp/installer | php -- --install-dir=/usr/local/bin

  - name: rename composer.phar to composer
    shell: mv /usr/local/bin/composer.phar /usr/local/bin/composer

  - name: make composer executable
    file:
      path: /usr/local/bin/composer
      mode: a+x
      state: file

  when: not composer_bin.stat.exists
  tags: php

- name: stop apache2
  become: true
  shell: update-rc.d apache2 disable
  tags: php
```

追加した```role```の```task```を一つずつみてみます。

```yml
- name: Add php7.2 repo
  apt_repository:
    repo: 'ppa:ondrej/php'
  tags: php
```

php 7.2をインストールするため```apt```へphp7.2のリポジトリ(repository)を追加します。

```yml
- name: Install php
  become: true
  apt:
    pkg:
      - php7.2
      - php7.2-mbstring
      - php7.2-xml
    state: present
    update_cache: yes
  tags: php
```

php7.2とララベル(Laravel)インストールや実行に必要なphpモジュールをインストールします。

```yml
- name: check composer
  stat: path=/usr/local/bin/composer
  register: composer_bin
  tags: php
```

composerのインストールする前composerの実行ファイルが存在するかチェックしてその結果を```composer_bin```に保存します。

```yml
- block:
  ...
  when: not composer_bin.stat.exists
  tags: php
```

色んな```task```をブロック(block)で囲みます。また、このブロックは私たちが上記で保存した```composer_bin```が存在しない場合のみで実行します。

ブロック(block)中を一つずつみてみます。

```yml
- name: download composer
  get_url:
    url: https://getcomposer.org/installer
    dest: /tmp/installer
```

composerインストールスクリプトを```/tmp/instller```ファイルにダウンロードします。

```yml
- name: install composer
    shell: cat /tmp/installer | php -- --install-dir=/usr/local/bin
```

composerインストールスクリプトを使って```/usr/local/bin```にcomposerをインストールします。

```yml
- name: rename composer.phar to composer
  shell: mv /usr/local/bin/composer.phar /usr/local/bin/composer
```

インストールされたcomposerファイルを(```composer.phar```)の名前を```composer```に変更します。

```yml
- name: make composer executable
    file:
      path: /usr/local/bin/composer
      mode: a+x
      state: file
```

composerが実行ができるように権限を変更します。

```yml
- name: stop apache2
  become: true
  shell: update-rc.d apache2 disable
  tags: php
```

phpをインストールした後、仮想マシン(guest system)を再起動すると```apache2```サーバが起動されて同じポート(port)を使ってるドッカー(Docker)が起動されない問題があります。```apache2```サーバが仮想マシン(guest syste)が再起動する時再起動されないように設定します。

## phpとcomposerインストール
上記で作ったアンシブルプレイブック(Ansible Playbook)の```role```を実行してphpとcomposerをインストールします。私たちはこの```role```だけ実行できるようにタグ(tag)を指定したのでタグ(tag)オプションを追加したアンシブルプレイブック(Ansible Playbook)コマンドを下記のように実行します。

```bash
#vagrant ssh
sudo ansible-playbook /vagrant/ansible/playbook.yml --tags 'php'
```

下にあるコマンドでインストールがうまくできたか確認します。

```bash
#vagrant ssh
php --version
composer --version
```

## ララベルプロジェクト生成
下記のコマンドでララベル(Laravel)プロジェクトを生成します。既存のララベル(Laravel)プロジェクトを持ってる方はこの部分はスキップしてもいいです。

```bash
#vagrant ssh
cd /vagrant
composer create-project laravel/laravel app
```

## ララベルプロジェクト設定
私たちは以前のブログ([アンシブル&Laradock]({{site.url}}/{{page.categories}}/ansible-laradock/){:target="_blank"})でLaradockのインストール```role```を下記のように作成しました。

```yml
...
- name: change project folder
  replace:
    path: /vagrant/lib/laradock/.env
    regexp: 'APP_CODE_PATH_HOST=*.*'
    replace: 'APP_CODE_PATH_HOST=/vagrant/app'
  tags:
    - replace
...
```

この部分でLaradockのworkspaceドッカー(Docker)が実行される時```/vagrant/appp```フォルダと同期化するように設定しました。したがって、私たちは新しプロジェクトを```/vagrant```フォルダに```/app```のフォルダ名で生成しました。皆さんが既存のララベル(Laravel)プロジェクトを持ってるだったら```/vagrant/appp```フォルダにコピーするか以前のブログで作ったLaradockの```role```中で上記の部分を皆さんのララベル(Laravel)プロジェクトフォルダで指定して使ってください。

## ララベルプロジェクト確認
また、localhostに接続したら下記のようにララベル(Laravel)の基本画面が見えます。

![laravel first page](/assets/images/category/environment/ansible-laravel/laravel.png)

ララベル(Laravel)設定がよく出来てない時は下記のように500エラー画面が出ます。

![laravel 500 error page](/assets/images/category/environment/ansible-laravel/laravel_error.png)

ララベル(Laravel)設定中で下記の部分を全て実行したか確認します。```composer create-project laravel/laravel app```コマンドでララベル(Laravel)プロジェクトを新しく生成し場合、下記の設定は自動で実行されます。

ララベル(Laravel)プロジェクトに必要なライブラリはインストルしたか？

```bash
composer install
```

ララベル(Laravel)の環境ファイルは生成したか？

```bash
cp .env.example .env
```

ララベル(Laravel)のキーは生成したか？

```bash
php artisan key:generate
```

## phpmyadmin
データベースを触るためインストールした```phpmyadmin```に接続してみます。```localhost:8080```で接続したら```phpmyadmin```の画面が見えます。

![phpmyadmin login](/assets/images/category/environment/ansible-laravel/phpmyadmin_login.png)

何も設定してなかったら下の情報を入力して接続します。

```
server: mysql
username: root
password: root
```

このように接続した後下記のような画面が見えます。

![phpmyadmin change password](/assets/images/category/environment/ansible-laravel/phpmyadmin_change_password.png)

画面の真ん中にある```Change password```を押してパスワードを変更します。

![phpmyadmin new password](/assets/images/category/environment/ansible-laravel/phpmyadmin_new_password.png)

上部にあるメニュー中で```Database```を押してララベル(Laravel)と連結するデータベースを生成します。

![phpmyadmin new database](/assets/images/category/environment/ansible-laravel/phpmyadmin_new_database.png)

## ララベルDB設定
上記で```phpmyadmin```を使って作ったデータベース(Database)をララベル(Laravel)プロジェクトに連結する必要があります。ララベル(Laravel)プロジェクトの環境ファイルである```.env```を開いたら下のように内容を確認することができます。

```bash
...
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=homestead
DB_USERNAME=homestead
DB_PASSWORD=secret
...
```

この部分を下記のように修正します。```DB_DATABASE```と```DB_PASSWORD```の部分は皆さんが設定した内容を入力します。

```bash
...
DB_CONNECTION=mysql
DB_HOST=mysql
DB_PORT=3306
DB_DATABASE=app
DB_USERNAME=root
DB_PASSWORD=*******
...
```

このように修正したら下記のララベル(Laravel)コマンドでララベル(Laravel)が基本的提供してるユーザーテーブル(User Table)を生成してみます。

```bash
# vagrant ssh
# sudo docker exec -it laradock_workspace_1 bash
php artisan migrate
```

ララベル(Laravel)が基本的提供してるユーザーテーブル(User Table)を使わない予定ならララベル(Laravel)コマンドを使って生成したテーブルを削除します。

```bash
php artisan migrate:rollback
```

## 完了
vagrant、アンシブル(Ansible)、Laradockを使ってララベル(Laravel)開発環境を構築してみました。また、この開発環境構築を通じてアンシブル(Ansible)とドッカー(Docker)を少しみてみました。アンシブル(Ansible)とドッカー(Docker)を上手く使えばよく聞こえる```Devops```ができる開発者になれるんじゃないかなと思います。

今後はこの[開発環境]({{site.url}}/{{page.categories}}/){:target="_blank"}カテゴリには開発構築、ドッカー(Docker)、アンシブル(Ansible)と関係ある内容を追加する予定です。また、ララベル(Laravel)開発と関係あるブログは[ララベル]({{site.url}}/laravel/){:target="_blank"}カテゴリに作成する予定なのでご参考してください。

今まで作ったララベル(Laravel)開発環境を下記のレポジトリ(Repository)で確認できます。
- [https://github.com/dev-yakuza/laravel-devtool](https://github.com/dev-yakuza/laravel-devtool){:rel="nofollow noreferrer" target="_blank"}

## 参考
- [https://laradock.io/documentation/](https://laradock.io/documentation/){:rel="nofollow noreferrer" target="_blank"}