---
layout: 'post'
permalink: '/environment/ansible-playbook/'
paginate_path: '/environment/:num/ansible-playbook/'
lang: 'ko'
categories: 'environment'
comments: true

title: '앤서블 플레이북'
description: '앤서블 플레이북(Ansible Playbook)을 사용하여 서버 구축에 필요한 프로그램 설치와 기초 설정들을 진행해 보자.'
image: '/assets/images/category/environment/ansible-playbook.jpg'
---


## 개요
이전 블로그에서 설치한 앤서블(Ansible)의 플레이북(Playbook)을 활용하여 서버를 구축하려고 합니다. 기본적으로 서버 구축에 필요한 프로그램과 설정을 위해 앤서블 플레이북(Ansible Playbook)을 사용할 예정입니다. 이 블로그는 기본적으로 vagrant를 사용하여 가상 머신(guest system)을 만들고 그 안에 앤서블(Ansible)을 설치하여 진행합니다.

- vagrant를 설치하는 방법에 대해서는 이전 블로그인 [vagrant 설치 및 사용법]({{site.url}}/{{page.categories}}/vagrant-install-and-usage/){:target="_blank"}을 확인해 주세요.
- vagrant에 앤서블(Ansible)을 설치하는 방법은 [앤서블 설치]({{site.url}}/{{page.categories}}/install-ansible/){:target="_blank"}을 확인해 주세요.

이 블로그는 위에 두 블로그 내용을 진행하였다는 가정하에 설명합니다.

## 앤서블 플레이북 생성
현재 ```Vagrantfile``` 파일이 존재하는 폴더에 ```ansible```이라는 이름의 폴더를 만듭니다.

```bash
|-- ansible
|-- Vagrantfil
```

생성한 ```ansible``` 폴더에 ```playbook.yml``` 파일을 생성합니다. 앤서블(Ansible)에 모든 내용은 ```야믈(yml)``` 파일 형식과 문법을 따릅니다. 그러므로 ```야믈(yml)```에서 사용가능한 모든 것을 사용할 수 있습니다.

```bash
|-- ansible
|    |-- playbook.yml
|-- Vagrantfil
```

생성한 ```playbook.yml``` 파일은 앤서블(Ansible)의 시작점입니다. ```playbook.yml```를 아래와 같이 작성합니다.

```yml
---
- hosts: localhost
  roles:
    - init
```

이전 블로그에서 소개해 드렸지만 앤서블(Ansible)은 인프라에 관련된 전반적인 자동화툴입니다. 따라서 로컬 서버(local server) 이외에도 원격 서버(remote server)의 인프라도 관리할 수 있습니다. ```hosts```는 앤서블(Ansible)을 이용하여 인프라 구축할 대상, 즉 로컬 서버(local server)나 원격 서버(remote server)을 지정할 수 있습니다. 우리는 현재 개발 서버를 구축하는 단계임으로 ```hosts```에는 ```localhost```를 입력합니다.

앤서블(Ansible)이 하나에 플레이북(playbook) 파일로 모든 인프라 구축 내용을 정의할 수 있지만, ```roles```를 이용하여 여러 파일로 분리하여 관리할 수 있습니다. ```roles``` 하단에 분리하여 관리할 폴더 리스트를 지정합니다. 이 블로그에서는 ```init```이라는 하나의 폴더만을 생성할 예정임으로 ```- init```이라고 입력합니다.

```bash
|-- ansible
|    |-- init
|    |    |-- tasks
|    |    |    |-- main.yml
|    |-- playbook.yml
|-- Vagrantfil
```

위와 같이 ```ansible``` 폴더 하위에 ```init/tasks/main.yml``` 파일을 생성하고 아래에 내용을 추가합니다.

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

- name: Install basic packages
  become: true
  apt:
    pkg:
        - git
        - unzip
    state: present
    update_cache: yes
```

앤서블(Ansible)의 명령어를 하나하나 자세히 보도록 하겠습니다.

```yml
- name: Make app directory
  file: path=/var/www state=directory mode=0755
```

위에 내용은 앤서블(Ansible)의 명령어를 나타냅니다. ```name```은 현재 명령어를 구분하기 위한 값이며 이 명령어는 앤서블(Ansible)의 ```file``` 명령어를 통해 폴더를 생성하는 부분입니다.

```yml
- name: Symbolic link
  file: src=/vagrant dest=/var/www/vhosts state=link
```

폴더 관리를 편하게 하기 위해 ```/vagrant``` 폴더와 ```/var/www/vhosts``` 폴더를 연결합니다.

```yml
- name: Set timezone to Asia/Seoul
  timezone:
    name: Asia/Seoul
```

로컬 서버의 타임존(timezone)을 설정합니다.

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

리눅스 팩키지 관리 도구인 ```apt-get```을 최신 상태로 업데이트 합니다. ```become: true```를 통해 관리자(root) 권한으로 이 앤서블(Ansible) 명령어를 실행합니다.

```yml
- name: Install basic packages
  become: true
  apt:
    pkg:
        - git
        - unzip
    state: present
    update_cache: yes
```

앞으로 필요한 기본 프로그램(git, unzip)을 설치합니다.

## Vagrantfile 수정
기존의 ```Vagrantfile```에 아래에 내용을 추가합니다.

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

이전 블로그에서 활용한 프로비전 쉘(provision shell)에 ```ansible-playbook /vagrant/ansible/playbook.yml```을 추가하였습니다. 이제 ```vagrat up``` 또는 ```vagrant provision```을 실행하면 우리가 만든 앤서블 플레이북(Ansible Playbook)이 자동으로 실행됩니다.

또한 ```config.vm.synced_folder ".", "/vagrant"``` 명령어를 통해 로컬 머신(host system)의 폴더를 가상 머신(guest system)의 ```/vagrant```에 업로드하고 동기화(sync)합니다. 이제 로컬 머신(host system)에서 파일을 수정하면 가상 머신(guest system)에 자동으로 반영됩니다.

## 테스트
그럼 지금까지 만든 앤서블 플레이북(Ansible Playbook)과 Vagrantfile를 이용하여 자동으로 서버를 설정해봅시다. 기존에 가상 머신(guest system)이 구동중이라면 아래의 vagrant 명령어를 통해 가상 머신(guest system)을 제거합니다.

```bash
vagrant destroy
```

아래에 vagrant 명령어를 통해 가상 머신(guest system)을 생성합니다. 이렇게 생성하면 이전과는 다르게 우리가 작성한 앤서블 플레이북(Ansible)이 동작하는 것을 콘솔(console)에서 확인할 수 있습니다.

```bash
vagrant up
```

생성이 완료되면 아래에 vagrant 명령어를 통해 가상 머신(guest system)에 접속합니다.

```bash
vagrant ssh
```

아래에 명령어들을 통해 Vagrantfile과 앤서블 플레이북(Ansible Playbook)이 잘 동작하였는지 확인합니다.

```bash
cd /vagrant
ls

git --version
unzip -v
```

## 완료
이번 블로그에서는 앤서블 플레이북(Ansible Playbook)을 통해 가상 머신(guest system)에 기본적으로 필요한 프로그램들을 설치해 보았습니다. 이를 통해 앤서블 플레이북(Ansible Playbook)을 어떻게 사용하는지도 간단하게 살펴보았습니다. 또한 ```Vagrantfile``` 파일을 수정하여 가상 머신(guest system) 생성시 앤서블 플레이북(Ansible Playbook)이 자동으로 실행되게 만들었으며 Vagrantfile이 실행된 폴더와 가상 머신(guest system)의 ```/vagrant``` 폴더를 동기화 하는 방법도 살펴보았습니다.

앤서블 플레이북(Ansible Playbook)을 더 잘 사용해야 하지만, 저희는 아주 단순하게만 사용하고 있어 조금 부끄럽네요. 아래에 앤서블 문서(Ansible Document) 사이트 링크를 첨부했습니다. 문서를 확인하시고 더 아름답게 앤서블(Ansible)을 사용해 보세요.

다음 블로그에서는 docker 개발 환경을 추가해 보도록 하겠습니다.


## 참고
- 앤서블 문서(Ansible Document): [https://docs.ansible.com/](https://docs.ansible.com/){:rel="nofollow noreferrer" target="_blank"}