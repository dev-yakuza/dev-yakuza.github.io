---
layout: 'post'
permalink: '/environment/ansible-laradock/'
paginate_path: '/environment/:num/ansible-laradock/'
lang: 'ko'
categories: 'environment'
comments: true

title: '앤서블&라라독'
description: 'vagrant와 앤서블(Ansible)을 이용하여 만든 가상 머신(guest system)에 라라독(Laradock)을 이용하여 라라벨(Laravel) 개발 환경을 구성해봅시다.'
image: '/assets/images/category/environment/ansible-laradock.jpg'
---


## 개요
요즘 세상은 정말 없는게 없는거 같습니다. 우리가 생각하는 것들은 이미 세상 어딘가에 존재하고 공유되고 있네요. 라라독(Laradock)은 라라벨(Laravel)의 개발 환경에 필요한 요소들을 도커(Docker)로 만들고 관리하는 프로젝트입니다. 자세한 내용은 공식 사이트를 참고해주세요([https://github.com/laradock/laradock/](https://github.com/laradock/laradock/){:rel="nofollow noreferrer" target="_blank"}). 이 블로그에서는 라라독(Laradock)을 이용하여 라라벨(laravel) 개발 환경을 구성하는 방법에 대해서 설명하겠습니다.

이 블로그는 아래에 있는 블로그에 연재물입니다. 이해를 돕기 위해 아래에 블로그 리스트를 먼저 진행하시는걸 추천합니다.

- [vagrant 설치 및 사용법]({{site.url}}/{{page.categories}}/vagrant-install-and-usage/){:target="_blank"}
- [앤서블 설치]({{site.url}}/{{page.categories}}/install-ansible/){:target="_blank"}
- [앤서블 플레이북]({{site.url}}/{{page.categories}}/ansible-playbook/){:target="_blank"}
- [앤서블&도커]({{site.url}}/{{page.categories}}/ansible-docker/){:target="_blank"}


## 개발 환경 구성
라라독(Laradock)은 개발 환경을 구성하기 위해 다양한 도커(Docker)를 제공합니다. 따라서 자신이 개발하고자 하는 환경에 맞는 도커(Docker)를 선택하고 설치해야합니다. 우리는 아래에 항목으로 개발 환경을 구성할 예정입니다.

- nginx
- mysql
- phpmyadmin
- workspace

## 가상 머신 설정 수정
가상 머신(guest system) 설정을 수정하기 위해 아래와 같이 ```Vagrantfile```을 수정합니다.

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

가상 머신(guest system)에 virtualbox에서 표시되는 이름을 ```vb.name```을 사용하여 특정한 이름(```laravel-dev```)를 부여했습니다. 이 부분은 실제 개발 환경 구성과는 무관하며 단지 virtualbox에 표시되는 이름을 알기 쉽게 하기 위함입니다.

vagrant의 ```config.vm.network "forwarded_port"```을 사용하여 로컬 머신(host system)의 포트를 가상 머신(guest system)의 포트로 포트포워드(port-forward)시켰습니다. 이제 로컬 머신(host system)의 포트를 통해 가상 머신(guest system)의 포트에 접근할 수 있습니다. 80 포트는 라라벨(Laravel) 프로젝트를 위해, 8080은 phpmyadmin에 접근하기 위해 연결하였습니다.

가상 머신(guest system)을 vagrant 명령어(```vagrant halt```)로 중지 시키고 다시 vagrant 명령어(```vagrant up```)으로 가상 머신(guest system)을 재시작 했을때, 이전 앤서블 플레이북(Ansible Playbook) 실행 스크립트는 프로비전 쉘(provision shell)에 있으므로 실행되지 않습니다. 또한 라라독(Laradock)의 도커(Docker)들은 항상 재시작(restart always)이 설정되어 있지 않아 가상 머신(guest system)이 재시작할시 도커(Docker)가 기동되지 않습니다. 그래서 우리는 Vagrantfile에 아래와 같이 추가하였습니다.

```ruby
config.trigger.after :up do |trigger|
  trigger.name = "trigger Docker after Vagrant Up"
  trigger.run_remote = {inline: "sudo ansible-playbook /vagrant/ansible/playbook.yml --tags 'docker'"}
end
```

이 설정은 우리가 ```vagrant up``` 명령어로 가상 머신(guest system)을 시작한 후, 실행될 내용을 정의합니다. 이곳에 가상 머신(guest system)에서 앤서블 플레이북(Ansible Playbook)을 실행하도록 설정하였습니다. 앤서블 플레이북(Ansible Playbook) 명령어가 프로비전 쉘(provision shell)에 있는 명령어와 다르게 ```--tags 'docker'``` 옵션을 사용하고 있습니다. 이 옵션을 사용하면 ```docker```로 태그(tag)된 명령어만 실행이 됩니다. 자세한 내용은 아래에 앤서블 플레이북(Ansible Playbook) 설정에서 다시 설명하도록 하겠습니다.


## 앤서블 플레이북에 라라독 설정
지난 시간에 이어 앤서블 플레이북(Ansible Playbook)을 사용하여 개발 환경 구성을 진행하겠습니다. 지금까지 구성한 폴더 구조는 아래와 같습니다.

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

여기에 라라독(Laradock)을 위한 ```role```을 정의하기 위해 아래와 같이 ```laradock/tasks/main.yml``` 파일을 추가합니다.

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

앤서블 플레이북(Ansible Playbook)의 시작점인 ```playbook.yml``` 파일을 열고 라라독(Laradock) ```role```을 추가합니다.

```yml
---
- hosts: localhost
  connection: local
  roles:
    - init
    - docker
    - laradock
```

추가한 ```laradock/tasks/main.yml``` 파일을 아래와 같이 수정합니다.

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

추가한 앤서블 플레이북(Ansible Playbook)의 ```role```을 살펴보겠습니다.

```yml
- name: git clone Laradock
  git: repo=https://github.com/Laradock/laradock.git dest=/vagrant/app/laradock/ version=master
```

앤서블(Ansible)의 git 모듈을 사용하여 라라독(Laradock)의 저장소(repository)를 복사(clone)합니다.

```yml
- name: copy Laradock environment file
  copy: src=/vagrant/app/laradock/env-example dest=/vagrant/app/laradock/.env
```

라라독(Laradock)의 예제 설정 파일(```env-example```)을 사용 가능한 설정 파일(```.env```)로 복사합니다.

```yml
- name: change mysql version
  replace:
    path: /vagrant/app/laradock/.env
    regexp: 'MYSQL_VERSION=*.*'
    replace: 'MYSQL_VERSION=5.7'
  tags:
    - replace
```

라라독(Laradock)의 환경 파일인 ```.env```에서 ```mysql``` 버전을 ```5.7```로 변경합니다. 최신 버전(```8.0```)을 사용할 경우 라라벨(Laravel)에서 mysql에 접근시 아래와 같은 에러가 나옵니다.

```bash
[PDOException]
SQLSTATE[HY000] [2054] The server requested authentication method unknown to the client
```

최신 mysql의 암호 인증 방식이 라라벨(Laravel)에서 지원이 안되는 문제가 있어 발생하는거 같습니다. 여러 해결책들이 있지만 mysql 8.0 기능을 딱히 쓰지 않는다면 5.7로 다운그레이드(Downgrade)하여 사용하시길 권장합니다.

```yml
- name: change project folder
  replace:
    path: /vagrant/lib/laradock/.env
    regexp: 'APP_CODE_PATH_HOST=*.*'
    replace: 'APP_CODE_PATH_HOST=/vagrant/app'
  tags:
    - replace
```

라라독(Laradock)의 workspace 도커(Docker)는 우리가 만들 라라벨(Laravel) 프로젝트가 돌아갈 환경입니다. 이 도커(Docker)는 ```APP_CODE_PATH_HOST```를 참고하여 도커(Docker)를 빌드 및 기동시 해당 폴더를 동기화(sync)하여 라라벨(Laravel) 프로젝트를 기동시킵니다. 기본 설정은 ```APP_CODE_PATH_HOST=../```으로 라라독(Laradock)의 상위 폴더를 지칭하고 있습니다. 이 부분을 우리는 ```/vagrant/app``` 부분으로 변경하였습니다. 여러분은 여러분의 라라벨(Laravel) 프로젝트의 폴더의 위치로 변경하거나 여러분의 라라벨(Laravel) 프로젝트의 폴더명을 app으로 변경하여 사용하시면 됩니다.

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

앤서블(Ansible)의 도커 서비스(Docker Service) 모듈을 사용하여 우리가 필요한 도커(Docker)를 빌드하고 실행시킵니다. 또한 다른 명령어들과는 다르게 ```tag``` 기능을 사용하고 있습니다. 앤서블 플레이북(Ansible Playbook)을 실행할때 ```--tags``` 옵션을 사용하여 태그(tag)된 명령어중 실행하고 싶은 명령어들만을 실행할 수 있습니다. ```--tags``` 옵션이 설정이 되지 않은 상태에서 앤서블 플레이북(Ansible Playbook) 명령어를 실행한다면 모든 명령어들이 전부 실행됩니다.

```bash
# 모든 명령어 실행
sudo ansible-playbook /vagrant/ansible/playbook.yml
# docker로 태그(tag)된 명령어만 실행
sudo ansible-playbook /vagrant/ansible/playbook.yml --tags 'docker'
```

## 앤서블 플레이북 실행
앤서블 플레이북(Ansible Playbook)에 라라독(Laradock)의 ```role``` 설정이 끝났습니다. 이제 앤서블 플레이북(Ansible Playbook)을 실행하여 라라독(Laradock)을 설치해 봅시다.

```bash
# vagrant ssh
sudo ansible-playbook /vagrant/ansible/playbook.yml
```

## 라라독 설치 확인
앤서블 플레이북(Ansible Playbook)에 의해 라라독(Laradock)이 잘 설치되었는지 아래에 도커(Docker) 명령어를 통해 확인합니다.

```bash
# vagrant ssh
sudo docker ps
```

또한, 로컬 머신(host system)에서 ```http://localhost```를 실행하여 ```nginx```의 ```404 Not Found``` 에러 화면이 표시됩니다.

## 완료
앤서블(Ansible)을 통해 라라독(Laradock)을 설치하여 라라벨(Laravel) 개발 환경을 준비하였습니다. 지금은 라라벨(Laravel) 프로젝트가 설정이 되어있지 않아 ```404 Not Found``` 화면이 보이지만, 개발 환경은 성공적으로 설정하였습니다. 다음 시간에는 라라독(Laradock) 개발 환경에 라라벨(Laravel) 프로젝트를 설정해 보도록 하겠습니다.

## 참고
- [https://laradock.io/documentation/](https://laradock.io/documentation/){:rel="nofollow noreferrer" target="_blank"}
