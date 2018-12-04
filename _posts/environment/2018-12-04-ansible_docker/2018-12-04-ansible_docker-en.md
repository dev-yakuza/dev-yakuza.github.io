---
layout: 'post'
permalink: '/environment/ansible-docker/'
paginate_path: '/environment/:num/ansible-docker/'
lang: 'en'
categories: 'environment'
comments: true

title: 'Ansible&Docker'
description: let's install Docker and Docker Compose on vagrant virtual machine(guest system) by Ansible Playbook.
image: '/assets/images/category/environment/ansible-docker.jpg'
---


## outline
we can't talk server development without Docker recently. in here, it's difficult to explain all details about Docker. we will introduce Docker by explain it little by little when we need. we will explain how to install Docker and Docker Compose on vagrant by Ansible Playbook in this blog post.

this blog is based on the assumption that you have done three blogs below.

- [vagrant installation and usage]({{site.url}}/{{page.categories}}/vagrant-install-and-usage/){:target="_blank"}
- [Ansible installation]({{site.url}}/{{page.categories}}/install-ansible/){:target="_blank"}
- [Ansible Playbook]({{site.url}}/{{page.categories}}/ansible-playbook/){:target="_blank"}


## set Docker in Ansible Playbook
below is the directory structure for vagrant virtual machine(guest system) we created until now.

```bash
|-- ansible
|    |-- init
|    |    |-- tasks
|    |    |    |-- main.yml
|    |-- playbook.yml
|-- Vagrantfile
```

we'll define ```role``` about Docker installation and add Ansible Playbook in here. create ```docker/tasks/main.yml``` file in ```ansible``` folder.

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

modify ```playbook.yml``` that is Ansible Playbook's start point like below.

```yml
---
- hosts: localhost
  connection: local
  roles:
    - init
    - docker
```

add below codes to ```docker/tasks/main.yml``` we created.

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

let's see Ansible commands one by one.

```yml
- name: Install docker
  shell: curl https://get.docker.com | sh
```

this command is to install Docker by using Docker install script.

```yml
- name: Modify privilege
  become: true
  shell: usermod -aG docker $USER

- name: Change privilege of docker
  become: true
  command: chmod +x /usr/bin/docker
```

this is to change user and permission of Docker.

```yml
- name: Install docker-compose
  become: true
  shell: curl -L https://github.com/docker/compose/releases/download/1.18.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
```

this command is to install Docker Compose

```yml
- name: Change privilege of docker-compose
  become: true
  command: chmod +x /usr/local/bin/docker-compose
```

this is to change Docker Compose Permission

## execute Ansible
execute below Ansible command in virtual machine(guest system) to execute Docker installation ```role``` we added in Ansible Playbook above.

```bash
vagrant ssh

sudo ansible-playbook /vagrant/ansible/playbook.yml
```
we executed Ansible Playbook because we already have virtual machine(guest system). if we make new environment, Ansible Playbook is automatically executed because we already added provision shell.

execute below vagrant command in local machine(host system) for testing.

```bash
vagrant destroy
vagrant up
```

## check Docker is installed
execute below commands to check Docker is installed well on virtual machine(guest system) by Ansible Playbook.

```bash
vagrant ssh

docker --version
docker-compose --version
```

## completed
we saw how to install Docker and Docker Compose by Ansible Playbook. now, we can make development environment via Docker. next blog post, we will introduce how to configure Laravel development environment by Docker and Docker Compose.