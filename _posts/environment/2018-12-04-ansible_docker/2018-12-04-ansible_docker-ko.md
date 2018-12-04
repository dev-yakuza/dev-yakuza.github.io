---
layout: 'post'
permalink: '/environment/ansible-docker/'
paginate_path: '/environment/:num/ansible-docker/'
lang: 'ko'
categories: 'environment'
comments: true

title: '앤서블&도커'
description: '앤서블 플레이북(Ansible Playbook)을 사용하여 vagrant 가상 머신(guest system)에 도커(Docker)와 도커 컴포즈(Docker Compose)를 설치해 봅시다.'
image: '/assets/images/category/environment/ansible-docker.jpg'
---


## 개요
서버 개발에 이제는 도커(Docker)를 빼놓을 수 없네요. 여기에서 도커(Docker)에 관한 모든 설명을 하는 것은 힘들거 같습니다. 블로그를 작성하면서 필요할 때 조금씩 조금씩 설명하는 것으로 도커(Docker)를 설명하겠습니다. 이 블로그에서는 앤서블 플레이북(Ansible Playbook)을 사용하여 vagrant에 도커(Docker)와 도커 컴포즈(Docker Compose)를 설치하는 방법을 소개하겠습니다.

이 블로그는 이전 블로그를 모두 진행했다고 가정하에 설명합니다.

- [vagrant 설치 및 사용법]({{site.url}}/{{page.categories}}/vagrant-install-and-usage/){:target="_blank"}
- [앤서블 설치]({{site.url}}/{{page.categories}}/install-ansible/){:target="_blank"}
- [앤서블 플레이북]({{site.url}}/{{page.categories}}/ansible-playbook/){:target="_blank"}


## 앤서블 플레이북에 도커 설정
지금까지 만든 vagrant 가상 머신(guest system)을 위한 디렉토리(directory) 구조는 아래와 같습니다.

```bash
|-- ansible
|    |-- init
|    |    |-- tasks
|    |    |    |-- main.yml
|    |-- playbook.yml
|-- Vagrantfile
```

여기에 우리는 도커(Docker) 설치에 관한 ```role```을 정의하고 앤서블 플레이북(Ansible Playbook)에 추가할 예정입니다. 아래와 같이 ```ansible``` 폴더 밑에 ```docker/tasks/main.yml``` 파일을 추가합니다.

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

앤서블 플레이북(Ansible Playbook)의 시작점인 ```playbook.yml``` 파일을 열어 아래와 같이 추가합니다.

```yml
---
- hosts: localhost
  connection: local
  roles:
    - init
    - docker
```

추가한 ```docker/tasks/main.yml``` 파일을 아래와 같이 수정합니다.

```yml
---
- name: Install docker
  shell: curl https://get.docker.com | sh

- name: Modify privilege
  become: true
  shell: usermod -aG docker $USER

- name: Change privilege of docker
  become: true
  command: chmod +x /usr/bin/docker

- name: Install docker-compose
  become: true
  shell: curl -L https://github.com/docker/compose/releases/download/1.18.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose

- name: Change privilege of docker-compose
  become: true
  command: chmod +x /usr/local/bin/docker-compose
```

이제 앤시블(Ansible) 명령어를 하나씩 자세히 보겠습니다.

```yml
- name: Install docker
  shell: curl https://get.docker.com | sh
```

도커(Docker) 설치 스크립트를 사용하여 도커(Docker)를 설치합니다.

```yml
- name: Modify privilege
  become: true
  shell: usermod -aG docker $USER

- name: Change privilege of docker
  become: true
  command: chmod +x /usr/bin/docker
```

도커(Docker)의 사용자와 권한을 변경합니다.

```yml
- name: Install docker-compose
  become: true
  shell: curl -L https://github.com/docker/compose/releases/download/1.18.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
```

도커 컴포즈(Docker Compose)를 설치합니다.

```yml
- name: Change privilege of docker-compose
  become: true
  command: chmod +x /usr/local/bin/docker-compose
```

도커 컴포즈(Docker Compose)의 권한을 변경합니다.

## 앤서블 실행
위에서 앤서블 플레이북(Ansible Playbook)에 추가한 도커(Docker) 설치 ```role```을 실행하기 위해 아래에 앤서블(Ansible) 명령어를 가상 머신(guest system)에서 실행합니다.

```bash
vagrant ssh

sudo ansible-playbook /vagrant/ansible/playbook.yml
```

이미 환경이 구성된 상태에서 진행하였기 때문에 앤서블 플레이북(Ansible Playbook)을 실행시켰습니다. 새로 개발 환경을 구성할 경우 vagrat의 프로비전 쉘(provision shell)에 앤서블 플레이북(Ansible Playbook) 실행 스크립트를 추가하였기 때문에 자동으로 실행됩니다.

확인을 위해 아래에 vagrant 명령어를 로컬 머신(host system)에서 실행합니다.

```bash
vagrant destroy
vagrant up
```

## 도커 설치 확인
도커(Docker)가 앤서블 플레이북(Ansible Playbook)에 의해 가상 머신(guest system)에 잘 설치되었는지 아래에 도커(Docker) 명령어로 확인합니다.

```bash
vagrant ssh

docker --version
docker-compose --version
```

## 완료
앤서블 플레이북(Ansible Playbook)에 도커(Docker)와 도커 컴포즈(Docker Compose)를 추가하여 가상 머신(guest system)에 설치하는 방법을 살펴보았습니다. 이제 도커(Docker)를 통해 원하는 개발 환경을 만들 수 있게 되었습니다. 다음 블로그에서는 도커(Docker)와 도커 컴포즈(Docker Compose)를 이용하여 라라벨(Laravel) 개발 환경을 구성하는 방법에 대해서 살펴보겠습니다.