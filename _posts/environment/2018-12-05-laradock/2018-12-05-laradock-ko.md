---
published: false
layout: 'post'
permalink: '/environment/laradock/'
paginate_path: '/environment/:num/laradock/'
lang: 'ko'
categories: 'environment'
comments: true

title: '라라독&라라벨'
description: 'vagrant와 앤서블(Ansible)을 이용햐여 만든 가상 머신(guest system)에 라라독(Laradock)을 이용하여 라라벨(Laravel) 개발 환경을 구성해봅시다.'
image: '/assets/images/category/environment/laradock.jpg'
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
  config.vm.hostname = "laravel-dev"
  config.vm.network "forwarded_port", guest: 80, host: 80
  ...
end
```

가상 머신(guest system)에 ```config.vm.hostname```을 사용하여 특정한 이름(```laravel-dev```)를 부여했습니다. 또한 ```config.vm.network "forwarded_port", guest: 80, host: 80```을 사용하여 로컬 머신(host system)의 80 포트을 가상 머신(guest system)의 80 포트로 포트포워드(prot-forward)시켰습니다. 이제 로컬 머신(host system)의 80 포트를 통해 가상 머신(guest system)의 80포트에 접근할 수 있습니다.

## 앤서블 플레이북에 라라독 설정
지난 시간에 이어 계속적으로 앤서블 플레이북(Ansible Playbook)을 사용하여 개발 환경 구성을 진행하겠습니다. 지금까지 구성한 폴더 구조는 아래와 같습니다.

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
  git: repo=https://github.com/Laradock/laradock.git dest=/vagrant/laradock version=master

- name: copy Laradock environment file
  copy: src=/vagrant/laradock/env-example dest=/vagrant/laradock/.env

- name: dokcer compose Laradock(nginx, mysql, phpmyadmin, workspace)
  docker_service:
    debug: true
    state: present
    project_src: /vagrant/laradock
    services:
        - nginx
        - mysql
        - phpmyadmin
        - workspace
```

추가한 앤서블 플레이북(Ansible Playboo)의 ```role```을 살펴보겠습니다.

```yml
- name: git clone Laradock
  git: repo=https://github.com/Laradock/laradock.git dest=/vagrant/laradock version=master
```

앤서블(Ansible)의 git 모듈을 사용하여 라라독(Laradock)의 저장소(repository)를 복사(clone)합니다.

```yml
- name: copy Laradock environment file
  copy: src=/vagrant/laradock/env-example dest=/vagrant/laradock/.env
```

라라독(Laradock)의 예제 설정 파일을 사용 가능한 설정 파일로 복사합니다.

```yml
- name: dokcer compose Laradock(nginx, mysql, phpmyadmin, workspace)
  docker_service:
    debug: true
    state: present
    project_src: /vagrant/laradock
    services:
        - nginx
        - mysql
        - phpmyadmin
        - workspace
```

앤서블(Ansible)의 도커 서비스(Docker Service) 모듈을 사용하여 우리가 필요한 도커(Docker)를 빌드하고 실행시킵니다.

## 앤서블 플레이북 실행
앤서블 플레이북(Ansible Playbook)에 라라독(Laradock)의 ```role``` 설정이 끝났습니다. 이제 앤서블 플레이북(Ansible Playbook)을 실행하여 라라독(Laradock)을 설치해 봅시다.

```bash
# vagrant ssh
sudo ansible-playbook /vagrant/ansible/playbook.yml
```

## 라라독 설치 확인
앤서블 플레이북(Ansible Playbook)에 의해 라라독(Laradock)잘 설치되었는지 아래에 도커(Docker) 명령어를 통해 확인합니다.

```bash
# vagrant ssh
sudo docker ps
```

로컬 머신(host system)에서 ```http://localhost```를 실행하여 라라벨(Laravel)의 기본 화면이 잘 표시되는지 확인합니다.