---
layout: 'post'
permalink: '/environment/ansible-laravel/'
paginate_path: '/environment/:num/ansible-laravel/'
lang: 'ko'
categories: 'environment'
comments: true

title: '앤서블&라라벨'
description: '앤서블(Ansible)과 라라독(Laradock)을 사용하여 구성된 개발 환경에 라라벨(Laravel)을 설치하고 개발 환경을 구성해 보도록 하겠습니다.'
image: '/assets/images/category/environment/ansible-laravel.jpg'
---


## 개요
지난 시간에 앤서블(Ansible)을 이용하여 라라독(Laradock)을 설치하였습니다. 이제 라라벨(Laravel)을 개발하기 위해 라라벨(Laravel)을 설치하고 라라벨(Laravel) 프로젝트를 생성해 보겠습니다.

이 블로그는 아래에 있는 블로그에 연재물입니다. 이해를 돕기 위해 아래에 블로그 리스트를 먼저 진행하시는걸 추천합니다.

- [vagrant 설치 및 사용법]({{site.url}}/{{page.categories}}/vagrant-install-and-usage/){:target="_blank"}
- [앤서블 설치]({{site.url}}/{{page.categories}}/install-ansible/){:target="_blank"}
- [앤서블 플레이북]({{site.url}}/{{page.categories}}/ansible-playbook/){:target="_blank"}
- [앤서블&도커]({{site.url}}/{{page.categories}}/ansible-docker/){:target="_blank"}
- [앤서블&라라독]({{site.url}}/{{page.categories}}/ansible-laradock/){:target="_blank"}

## php와 composer 설정
자신의 로컬 머신(host system)에 php와 composer가 설치되어있다면 이 단계는 추가하지 않으셔도 됩니다. 라라벨(Laravel) 프로젝트를 생성하기 위해 php와 composer를 가상 머신(guest system)에 설치할 예정입니다.

지금까지 만든 폴더에 php와 composer를 설치하는 앤서블 플레이북(Ansible Playbook)의 ```role```을 추가합니다.

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

앤서블 플레이북(Ansible Playbook) 파일에도 새롭게 추가한 php의 ```role```을 추가합니다.

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

추가한 앤서블 플레이북(Ansible Playbook)의 ```role``` 파일인 ```php/tasks/main.yml``` 파일을 아래와 같이 수정합니다.

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

추가한 ```role```의 ```task```를 하나하나 살펴봅시다.

```yml
- name: Add php7.2 repo
  apt_repository:
    repo: 'ppa:ondrej/php'
  tags: php
```

php 7.2를 설치하기 위해 ```apt```에 php7.2의 저장소(repository)를 추가합니다.

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

php7.2와 라라벨(Laravel) 설치 및 실행에 필요한 php모듈들을 설치합니다.

```yml
- name: check composer
  stat: path=/usr/local/bin/composer
  register: composer_bin
  tags: php
```

composer 설치에 앞서 composer의 실행 파일이 존재하는지 체크한 후 그 결과를 ```composer_bin```에 저장합니다.

```yml
- block:
  ...
  when: not composer_bin.stat.exists
  tags: php
```

여러 ```task```를 블록(block)으로 묶습니다. 또한 이 블록은 우리가 위에서 저장한 ```composer_bin```이 존재하지 않을 경우에만 실행합니다.

블록(block)안을 하나하나 살펴보겠습니다.

```yml
- name: download composer
  get_url:
    url: https://getcomposer.org/installer
    dest: /tmp/installer
```

composer 설치 스크립트를 ```/tmp/installer``` 파일로 다운로드 합니다.

```yml
- name: install composer
    shell: cat /tmp/installer | php -- --install-dir=/usr/local/bin
```

composer 설치 스크립트를 이용하여 ```/usr/local/bin```에 composer를 설치합니다.

```yml
- name: rename composer.phar to composer
  shell: mv /usr/local/bin/composer.phar /usr/local/bin/composer
```

설치된 composer 파일(```composer.phar```)의 이름을 ```composer```로 변경합니다.

```yml
- name: make composer executable
    file:
      path: /usr/local/bin/composer
      mode: a+x
      state: file
```

composer가 실행 가능하도록 권한을 변경합니다.

```yml
- name: stop apache2
  become: true
  shell: update-rc.d apache2 disable
  tags: php
```

php 설치이후 가상 머신(guest system)을 재시작할시 ```apache2``` 서버가 기동하여 같은 포트(port)를 사용하는 도커(Docker)가 기동되지 않는 문제가 생깁니다. ```apache2``` 서버가 가상 머신(guest system)이 재시작될때 재실행되지 않도록 설정합니다.

## php와 composer 설치
위에서 만든 앤서블 플레이북(Ansible Playbook)의 ```role```을 실행하여 php와 composer를 설치합니다. 우리는 이 ```role```만 실행할 수 있도록 태그(tag)를 지정했으므로 태크(tag) 옵션을 추가한 앤서블 플레이북(Ansible Playbook) 명령어를 아래와 같이 실행합니다.

```bash
#vagrant ssh
sudo ansible-playbook /vagrant/ansible/playbook.yml --tags 'php'
```

아래에 명령어로 설치가 잘 되었는지 확인합니다.

```bash
#vagrant ssh
php --version
composer --version
```

## 라라벨 프로젝트 생성
아래에 명령어로 라라벨(Laravel) 프로젝트를 생성합니다. 기존에 라라벨(Laravel) 프로젝트를 가지고 있는 분들은 이 부분을 건너뛰셔도 좋습니다.

```bash
#vagrant ssh
cd /vagrant
composer create-project laravel/laravel app
```

## 라라벨 프로젝트 설정
우리는 이전 블로그([앤서블&라라독]({{site.url}}/{{page.categories}}/ansible-laradock/){:target="_blank"})에서 라라독(Laradock) 설치 ```role```을 아래와 같이 작성하였습니다.

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

이 부분에서 라라독(Laradock)의 workspace 도커(Docker)가 생성될 때 ```/vagrant/app``` 폴더와 동기화되도록 설정하였습니다. 따라서 우리는 새로운 프로젝트를 ```/vagrant``` 폴더에 ```/app```이라는 폴더명으로 생성하였습니다. 여러분이 기존에 라라벨(Laravel) 프로젝트를 가지고 계신다면 해당 프로젝트를 ```/vagrant/app``` 폴더로 복사하거나 이전 시간에 만든 라라독(Laradock)의 ```role```중에 위에 해당하는 부분을 여러분의 라라벨(Laravel) 프로젝트 폴더로 지정하여 사용하시기 바랍니다.

## 라라벨 프로젝트 확인
이제 다시 localhost에 접속하면 아래와 같이 라라벨(Laravel)의 기본 화면이 보이는 것을 확인할 수 있습니다.

![laravel first page](/assets/images/category/environment/ansible-laravel/laravel.png)

라라벨(Laravel) 설정이 제대로 되지 않았다면 아래와 같은 500 에러 화면이 나옵니다.

![laravel 500 error page](/assets/images/category/environment/ansible-laravel/laravel_error.png)

라라벨(Laravel) 설정중 아래에 항목들을 빼먹었는지 확인해봅니다. ```composer create-project laravel/laravel app``` 명령어로 라라벨(Laravel) 프로젝트를 새로 생성하였다면 아래에 설정은 자동으로 진행됩니다.

라라벨(Laravel) 프로젝트가 필요한 라이브러리를 설치했는가?

```bash
composer install
```

라라벨(Laravel)의 환경 파일을 생성하였는가?

```bash
cp .env.example .env
```

라라벨(Laravel)의 키를 생성하였는가?

```bash
php artisan key:generate
```

## phpmyadmin
데이터베이스를 다루기 위해 설치한 ```phpmyadmin```에 접속해 봅니다. ```localhost:8080```으로 접속하면 ```phpmyadmin```화면이 보입니다.

![phpmyadmin login](/assets/images/category/environment/ansible-laravel/phpmyadmin_login.png)

아무 설정도 하지 않았으므로 아래에 정보를 입력하여 접속합니다.

```
server: mysql
username: root
password: root
```

이렇게 접속한 후 아래와 같은 화면을 볼 수 있습니다.

![phpmyadmin change password](/assets/images/category/environment/ansible-laravel/phpmyadmin_change_password.png)

화면 가운데에 ```Change password```를 눌러 자신이 원하는 패스워드로 변경합니다.

![phpmyadmin new password](/assets/images/category/environment/ansible-laravel/phpmyadmin_new_password.png)

상단 메뉴에서 ```Database```를 눌러 라라벨(Laravel)과 연결하고자 하는 데이터베이스를 생성합니다.

![phpmyadmin new database](/assets/images/category/environment/ansible-laravel/phpmyadmin_new_database.png)

## 라라벨 DB 설정
위에서 ```phpmyadmin```을 사용해 만든 데이터베이스(Database)를 라라벨(Laravel) 프로젝트에 연결할 필요가 있습니다. 라라벨(Laravel) 프로젝트의 환경 파일인 ```.env```를 열면 아래와 같은 내용을 확인할 수 있습니다.

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

이 부분을 아래와 같이 수정합니다. ```DB_DATABASE```와 ```DB_PASSWORD``` 부분은 여러분이 설정한 내용을 입력합니다.

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

이렇게 수정하였다면 아래에 라라벨(Laravel) 명령어를 통해 라라벨(Laravel)이 기본적으로 제공하는 사용자 테이블(User Table)을 생성해 봅니다.

```bash
# vagrant ssh
# sudo docker exec -it laradock_workspace_1 bash
php artisan migrate
```

라라벨(Laravel)이 기본적으로 제공하는 사용자 테이블(User Table)을 사용하지 않을 예정이라면 라라벨(Laravel) 명령어를 통해 생성한 테이블을 제거합니다.

```bash
php artisan migrate:rollback
```

## 완료
vagrant, 앤서블(Ansible), 라라독(Laradock)을 이용하여 라라벨(Laravel) 개발 환경을 구축해보았습니다. 또한 이번 개발 환경 구축을 통해 앤서블(Ansible)과 도커(Docker)를 살짝 맛보았습니다. 앤서블(Ansible)과 도커(Docker)를 잘 활용하면 말로만 듣던 ```DevOps```를 할 수 있는 개발자가 되는게 아닌가 싶습니다.

앞으로도 이 [개발 환경]({{site.url}}/{{page.categories}}/){:target="_blank"} 카테고리에는 개발 환경 구축, 도커(Docker), 앤서블(Ansible)과 관련된 내용을 추가할 예정입니다. 또한 라라벨(Laravel) 개발에 관련한 블로그는 [라라벨]({{site.url}}/laravel/){:target="_blank"} 카테고리에 작성할 예정이니 많이 참고하시기 바랍니다.

## 참고
- [https://laradock.io/documentation/](https://laradock.io/documentation/){:rel="nofollow noreferrer" target="_blank"}