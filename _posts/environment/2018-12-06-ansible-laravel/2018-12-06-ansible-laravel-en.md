---
layout: 'post'
permalink: '/environment/ansible-laravel/'
paginate_path: '/environment/:num/ansible-laravel/'
lang: 'en'
categories: 'environment'
comments: true

title: 'Ansible&Laravel'
description: let's make development environment by installing Laravel on virtual machine(guest system) that is configured by Ansible and Laradock.
image: '/assets/images/category/environment/ansible-laravel.jpg'
---


## outline
at previous blog, we installed Laradock by Ansible. to develop Laravel, we will install and create Laravel project.


this blog is the series of below list. we recommend to read below list for understanding.

- [vagrant installation and usage]({{site.url}}/{{page.categories}}/vagrant-install-and-usage/){:target="_blank"}
- [Ansible installation]({{site.url}}/{{page.categories}}/install-ansible/){:target="_blank"}
- [Ansible Playbook]({{site.url}}/{{page.categories}}/ansible-playbook/){:target="_blank"}
- [Ansible&Docker]({{site.url}}/{{page.categories}}/ansible-docker/){:target="_blank"}
- [Ansible&Laradock]({{site.url}}/{{page.categories}}/ansible-laradock/){:target="_blank"}

## configure php and composer
if you installed php and composer in local machine(host system), it's better to skip this section. to create Laravel project, we'll install php and composer on virtual machine(guest system).

add php and composer installation ```role``` to Ansible Playbook folder we've made until now.

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

add new php ```role``` to Ansible Playbook file.

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

modify Ansible Playbook ```role``` file ```php/tasks/main.yml``` like below.

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

let's see ```task``` in ```role``` one by one.

```yml
- name: Add php7.2 repo
  apt_repository:
    repo: 'ppa:ondrej/php'
  tags: php
```

to install php 7.2, add php 7.2 repository to ```apt```.

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

install php 7.2 and php modules for installing and executing Laravel.

```yml
- name: check composer
  stat: path=/usr/local/bin/composer
  register: composer_bin
  tags: php
```

before installing composer, check composer file exists and store the result to ```composer bin``` variable.

```yml
- block:
  ...
  when: not composer_bin.stat.exists
  tags: php
```

enclose multiple ```task``` in a block. also, also, this block is run only when composer file does not exist by checking ```composer_bin```variable.

let's see the block one by one.

```yml
- name: download composer
  get_url:
    url: https://getcomposer.org/installer
    dest: /tmp/installer
```

download composer install script to ```/tmp/installer``` file.

```yml
- name: install composer
    shell: cat /tmp/installer | php -- --install-dir=/usr/local/bin
```

install composer to ```/usr/local/bin``` folder by using composer install script.

```yml
- name: rename composer.phar to composer
  shell: mv /usr/local/bin/composer.phar /usr/local/bin/composer
```

change ```composer.phar``` file name to ```composer```.

```yml
- name: make composer executable
    file:
      path: /usr/local/bin/composer
      mode: a+x
      state: file
```

change the permission so that composer is executable.

```yml
- name: stop apache2
  become: true
  shell: update-rc.d apache2 disable
  tags: php
```

after installing php, we got a problem. when virtual machine(guest system) is restarted, ```apache2``` is started and Docker that uses same port is not executed. so we configure not to start ```apache2``` server when virtual machine(guest system) is restarted.

## install php and composer
execute Ansible Playbook ```role``` we made above to install php and composer. we added php tag to ```role``` for only executing specific ```role```. execute below command to run only ```role``` tagged php.

```bash
#vagrant ssh
sudo ansible-playbook /vagrant/ansible/playbook.yml --tags 'php'
```

execute below command to check php and composer are installed well.

```bash
#vagrant ssh
php --version
composer --version
```

## create Laravel project
execute below command to create Laravel project. if you have your own Laravel project, you can skip below command.

```bash
#vagrant ssh
cd /vagrant
composer create-project laravel/laravel app
```

## configure Laravel project
at previous blog post([Ansible&Laradock]({{site.url}}/{{page.categories}}/ansible-laradock/){:target="_blank"}), we've made Laradock installation ```role``` like below.

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

we've set to sync ```/vagrant/app``` folder to Laradock workspace Docker when created. so we made new project on ```/app``` folder in ```/vagrant``` folder. if you have existing Laravel project, you should copy to ```/vagrant/app``` or you sould modify above part in Laradock ```role```.

## check Laravel project
now, access localhost again. you can see basic Laravel screen.

![laravel first page](/assets/images/category/environment/ansible-laravel/laravel.png)

if Laravel is not configured well, you can see 500 error screen like below.

![laravel 500 error page](/assets/images/category/environment/ansible-laravel/laravel_error.png)

check if missed settings exist during you configure Laravel. if you use ```composer create-project laravel/laravel app``` command to create new Laravel project, below settings is automatically executed.

Did you install required Laravel project libraries?

```bash
composer install
```

Did you create Laravel environment file?

```bash
cp .env.example .env
```

Did you configure Larevel key?

```bash
php artisan key:generate
```


## phpmyadmin
let's access ```phpmyadmin``` to set Database. you can see ```phpmyadmin``` screen when you access ```localhost:8080```

![phpmyadmin login](/assets/images/category/environment/ansible-laravel/phpmyadmin_login.png)

if you didn't configure anything, you can access by below informations.

```
server: mysql
username: root
password: root
```

you can see below screen after login.

![phpmyadmin change password](/assets/images/category/environment/ansible-laravel/phpmyadmin_change_password.png)

click ```Change password``` on the middle of the screen and change password.

![phpmyadmin new password](/assets/images/category/environment/ansible-laravel/phpmyadmin_new_password.png)

click ```Database``` menu on the top of the screen and create database for Laravel.

![phpmyadmin new database](/assets/images/category/environment/ansible-laravel/phpmyadmin_new_database.png)

## configure Laravel DB
we need to connect Laravel project to Database we've made above using ```phpmyadmin```. you can see below when you open Laravel environment file ```.env```.

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

modify this parts like below. insert what you've set up to settings ```DB_DATABASE``` and ```DB_PASSWORD```.

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

if you do so, try to create User Table that Laravel basically provides.

```bash
# vagrant ssh
# sudo docker exec -it laradock_workspace_1 bash
php artisan migrate
```

if you don't use User Table that Laravel basically provides, remove it by Laravel command below.

```bash
php artisan migrate:rollback
```

## completed
we've made Laravel development environment using vagrant, Ansible and Laradock. also, we've seen a little bit how to use Ansible and Docker through creating development environment. if we use Ansible and Docker very well, maybe we can be ```DevOps```.

we will continue to add contents related to building development environment, Docker and Ansible to this [dev environment]({{site.url}}/{{page.categories}}/){:target="_blank"} category. also, we will add contents about Laravel development to [Laravel]({{site.url}}/laravel/){:target="_blank"}, so please see it.

## reference
- [https://laradock.io/documentation/](https://laradock.io/documentation/){:rel="nofollow noreferrer" target="_blank"}