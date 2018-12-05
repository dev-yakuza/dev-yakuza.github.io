---
layout: 'post'
permalink: '/environment/ansible-playbook/'
paginate_path: '/environment/:num/ansible-playbook/'
lang: 'en'
categories: 'environment'
comments: true

title: 'Ansible Playbook'
description: let's try to use Ansible Playbook to install server programs and to configure the server.
image: '/assets/images/category/environment/ansible-playbook.jpg'
---


## outline
we try to use Ansilbe Playbook to configure the server. basically, we will use Ansible Playbook to install server programs we need and configure some settings. in this blog, we will make virtual machine(guest system) by vagrant and install Ansible in there.

- if you want to know how to install vagrant, check previous blog post - [vagrant installation and usage]({{site.url}}/{{page.categories}}/vagrant-install-and-usage/){:target="_blank"}.
- if you don't know how to install Ansible, see previous blog post - [Ansible installation]({{site.url}}/{{page.categories}}/install-ansible/){:target="_blank"}.

this blog is based on the assumption that you have done two blogs above.

## create Ansible Playbook
create ```ansible``` folder in ```Vagrantfile``` location.

```bash
|-- ansible
|-- Vagrantfil
```

create ```playbook.yml``` file in ```andible``` folder. Ansible contents are based on ```yml``` file format and grammers. so if we can do ```yml```, we could do in Ansible.

```bash
|-- ansible
|    |-- playbook.yml
|-- Vagrantfil
```

the ```playbook.yml``` file is the start point of the Ansible. modify ```playbook.yml``` like below.

```yml
---
- hosts: localhost
  roles:
    - init
```

we already talked at previous blog, Ansible is an automation tool for infrastructure. so we can manage local server and remote server infrastructure. we can set Ansible infrastructure target - local server or remote server - in ```hosts```. in here, we try to make local development environment so we set ```localhost``` to ```hosts```.

we can't only make and define one Ansible Playbook file to manage all infrastructure features, but also manage it by separate files with ```roles```. set folder list you managed separately under ```roles```. in here, we only use one ```init``` folder, so added ```-init``` under ```roles```.

```bash
|-- ansible
|    |-- init
|    |    |-- tasks
|    |    |    |-- main.yml
|    |-- playbook.yml
|-- Vagrantfil
```

create ```init/tasks/main.yml``` in ```ansible``` folder and modify it like below.

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

- name: Add python3.6 repo
  apt_repository:
    repo: 'ppa:jonathonf/python-3.6'

- name: Install basic packages
  become: true
  apt:
    pkg:
      - git
      - unzip
      - python3.6
      - python-pip
      - python3-pip
      - fabric
    state: present
    update_cache: yes
```

let's see Ansible commands one by one.

```yml
- name: Make app directory
  file: path=/var/www state=directory mode=0755
```

above is one of Ansible commands. ```name```
위에 내용은 앤서블(Ansible)의 명령어를 나타냅니다. ```name``` is the value to distinguish the current command. this command creates the folder by Ansible ```file``` command.

```yml
- name: Symbolic link
  file: src=/vagrant dest=/var/www/vhosts state=link
```

link ```/vagrant``` folder to ```/var/www/vhosts``` folder for management.

```yml
- name: Set timezone to America/New_York
  timezone:
    name: America/New_York
```

set local server timezone.

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

update linux package management tool(```apt-get```). ```become: true``` executes Ansible command by root permission.

```yml
- name: Add python3.6 repo
  apt_repository:
    repo: 'ppa:jonathonf/python-3.6'
```
Ansible has some modules depend on python so we need to install python. add python repository for installing.

```yml
- name: Install basic packages
  become: true
  apt:
    pkg:
        - git
        - unzip
        - python3.6
        - python-pip
        - python3-pip
        - fabric
    state: present
    update_cache: yes
```

install git, unzip programs and python programs for later.

## modify Vagrantfile
add below to ```Vagrantfile```

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

we added ```ansible-playbook /vagrant/ansible/playbook.yml``` in provision shell which we've introduced previous blog. if we execute ```vagrant up``` or ```vagrant provision```, Ansible Playbook we created is automatically executed.

and we added ```config.vm.synced_folder ".", "/vagrant"``` command to sync local machine(host system) folder to virtual machine(guest system) ```/vagrant``` folder. now if we edit files in local machine(host system) folder, automatically upload and sync to virtual machine(guest system).

## test
let's test to configure the server automatically by Ansible Playbook and Vagrantfile. if old virtual machine(guest system) is executing, execute below vagrant command to destroy virtual machine(guest system).

```bash
vagrant destroy
```

execute below vagrant command to create virtual machine(guest system). we can see difference between before and now. we can see Ansible Playbook is executed in console.

```bash
vagrant up
```

after virtual machine(guest system) is created, execute below vagrant command to access to virtual machine(guest system).

```bash
vagrant ssh
```

execute below commands to check Vagrantfile and Ansible Playbook have worked well.

```bash
cd /vagrant
ls

git --version
unzip -v
```

## completed
in this blog post, we installed programs basically required by Ansible Playbook to virtual machine(guest system). we looked briefly Ansible Playbook through this blog. also we modified ```Vagrantfile``` to execute Ansible Playbook automatically when virtual machine(guest system) is started and sync the folder that Vagrantfile was executed to ```/vagrant``` folder in virtual machine(guest system).

we should use Ansible Playbook better than here, we feel shameful because of simple usage. we added Ansible Document site in the bottom. please see that and use Ansible more beautifully.

next we will see how to use docker in virtual machine(guest system).


## reference
- Ansible Document: [https://docs.ansible.com/](https://docs.ansible.com/){:rel="nofollow noreferrer" target="_blank"}