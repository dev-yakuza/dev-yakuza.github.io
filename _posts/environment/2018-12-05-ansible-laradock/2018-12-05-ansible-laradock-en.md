---
layout: 'post'
permalink: '/environment/ansible-laradock/'
paginate_path: '/environment/:num/ansible-laradock/'
lang: 'en'
categories: 'environment'
comments: true

title: 'Ansible&Laradock'
description: let's make Laravel development environment by using virtual machine(guest system) created by vagrant and Ansible.
image: '/assets/images/category/environment/ansible-laradock.jpg'
---


## outline
in these days, everything is existed in the world. something we thought is already existed and shared in somewhere. Laradock is the project that creates and manages Dockers for Laravel development environment. if you want to know more details, see official repository([https://github.com/laradock/laradock/](https://github.com/laradock/laradock/){:rel="nofollow noreferrer" target="_blank"}). in here, we will introduce how to use Laradock to make Laravel development environment.

this blog is the series of below list. we recommend to read below list for understanding.

- [vagrant installation and usage]({{site.url}}/{{page.categories}}/vagrant-install-and-usage/){:target="_blank"}
- [Ansible installation]({{site.url}}/{{page.categories}}/install-ansible/){:target="_blank"}
- [Ansible Playbook]({{site.url}}/{{page.categories}}/ansible-playbook/){:target="_blank"}
- [Ansible&Docker]({{site.url}}/{{page.categories}}/ansible-docker/){:target="_blank"}


## configure development environment
Laradock provides many Dockers for configuring development environment. so we should decide which Docker we will use for development. we've decided to use below list for configuring development environment.

- nginx
- mysql
- phpmyadmin
- workspace

## modify virtual machine setting
modify ```Vagrantfile``` for virtual machine setting.

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

we set specific name(```laravel-dev```) by ```vb.name``` to display it on virtualbox. this part actually is not related with development environment, just display it for easy understanding.

we used ```config.vm.network "forwarded_port"``` of vagrant features for port-forward betwenn local machine(host system) and virtual machine(guest system). now we can access virtual machine(guest system) ports by local machine(host system) ports. 80 port is for Laravel project and 8080 is for phpmyadmin to acceess.

we can stop virtual machine(guest system) by vagrant command(```vagrant halt```) and restart it by vagrant command(```vagrant up```). however, Ansible Playbook is not executed because it is in Provision shell when virutal machine(guest system) is restarted. and Laradock Dockers is not configured to restart always so when virtual machine(guest system) is restarted, Dockers are not executed. therefore, we modified Vagrantfile like below.

```ruby
config.trigger.after :up do |trigger|
  trigger.name = "trigger Docker after Vagrant Up"
  trigger.run_remote = {inline: "sudo ansible-playbook /vagrant/ansible/playbook.yml --tags 'docker'"}
end
```

this option is executed after we execute ```vagrant up``` command to restart virtual machine(guest system). we configured Ansible Playbook will be executed after virtual machine(guest system) is restarted. Ansible Playbook command in here uses ```--tags 'docker'``` unlike the command in provision shell. if we use this option, we can execute specific commands tagging ```docker```. we will explain more detail in below Ansible Playbook setting again.

## set Laradock in Ansible Playbook
we'll use previous Ansible Playbook setting for configure development environment. until now, folder structure is like below.

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

we create ```laradock/tasks/main.yml``` file to define ```role``` for Laradock.

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

add Laradock ```role``` to Ansible Playbook start point ```playbook.yml```.

```yml
---
- hosts: localhost
  connection: local
  roles:
    - init
    - docker
    - laradock
```

modify ```laradock/tasks/main.yml``` file we added like below.

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

let's see Ansible Playbook ```role``` we added.

```yml
- name: git clone Laradock
  git: repo=https://github.com/Laradock/laradock.git dest=/vagrant/app/laradock/ version=master
```

this is to use Ansible git module to clone Laradock repository.

```yml
- name: copy Laradock environment file
  copy: src=/vagrant/app/laradock/env-example dest=/vagrant/app/laradock/.env
```

copy example environment file(```env-example```) to environment file(```.env```) we can use.

```yml
- name: change mysql version
  replace:
    path: /vagrant/app/laradock/.env
    regexp: 'MYSQL_VERSION=*.*'
    replace: 'MYSQL_VERSION=5.7'
  tags:
    - replace
```

change ```mysql``` version to ```5.7``` in Laradock environment file(```.env```). when we used recent version(```8.0```), we got below error message when we access mysql from Laravel.

```bash
[PDOException]
SQLSTATE[HY000] [2054] The server requested authentication method unknown to the client
```

maybe, Laravel is not supported new password authentication method of recent mysql. there are many solutions for this problem, but if you don't use specific features in mysql 8.0, we recommend just downgrade to 5.7.

```yml
- name: change project folder
  replace:
    path: /vagrant/lib/laradock/.env
    regexp: 'APP_CODE_PATH_HOST=*.*'
    replace: 'APP_CODE_PATH_HOST=/vagrant/app'
  tags:
    - replace
```

Laradock workspace Docker is the environment that Laravel project is executed. this Docker refers```APP_CODE_PATH_HOST``` folder to sync it so workspace Docker is built and executed with this folder. basic option is ```APP_CODE_PATH_HOST=../``` which means upper Laradock folder. we modified this to ```/vagrant/app```. you can modify it to your Laravel project folder or you can change your Laravel project folder name to ```app```.

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

build and execute required Dockers by Ansible Docker Service module. this task uses ```tag``` feature unlike others. if we use ```--tags``` option in executing Ansible Playbook command, we can execute only tagged commands in all commands. if ```--tags``` option is not set, Ansible Playbook executes all commands.

```bash
# execute all commands
sudo ansible-playbook /vagrant/ansible/playbook.yml
# execute commands tagged docker
sudo ansible-playbook /vagrant/ansible/playbook.yml --tags 'docker'
```

## execute Ansible Playbook
completed to configure Laradock ```role``` to Ansible Playbook. let's execute Ansible Playbook to install Laradock.

```bash
# vagrant ssh
sudo ansible-playbook /vagrant/ansible/playbook.yml
```

## check Laradock is installed
execute below Docker command to check Laradock is installed well by Ansible Playbook.

```bash
# vagrant ssh
sudo docker ps
```

also, open ```http://localhost``` on local machine(host system) browser. you can see ```nginx```'s ```404 Not Found``` error screen.

## completed
we prepared Laravel development environment by installing Laradock using Ansible. now we can see ```404 Not Found``` because we've not set Laravel project but Laravel development environment was ready by Laradock. next, we will configure Laravel project on Laradock development environment.

## reference
- [https://laradock.io/documentation/](https://laradock.io/documentation/){:rel="nofollow noreferrer" target="_blank"}
