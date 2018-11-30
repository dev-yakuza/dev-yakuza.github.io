---
layout: 'post'
permalink: '/environment/install-ansible/'
paginate_path: '/environment/:num/install-ansible/'
lang: 'en'
categories: 'environment'
comments: true

title: 'Ansible installation'
description: 'make the environment can be used Ansible by installing Ansible on virtual machine(guest system) created by Vagrant'
image: '/assets/images/category/environment/install-ansible.jpg'
---


## outline
if we try to explain Ansible, we need to make a book for it. however we don't know Ansible perfectly and our level is not able to explain it. so we can't introduce details about Ansible but we try to explain Ansible by how we use Ansible. simply Ansible is an automation tool for infrastructure. we can do automatically install or deploy by Ansible. in here we introduce how to install Ansible to vagrant.

this blog post is for people who installed virtualbox and vagrant. if you don't install virtualbox and vagrant, see our previous blog - [vagrant installation and usage]({{site.url}}/{{page.categories}}/vagrant-install-and-usage/){:target="_blank"}

## create virtual machine setting
execute below vagrant command to create virtual machine(guest system) setting.

```bash
vagrant init bento/ubuntu-16.04
```

after executing above vagrant command, you can see ```Vagrantfile``` file in the folder you executed it. below code is ```Vagrantfile``` contents without comment out(```#```).

```ruby
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-16.04"
end
```

## create and check virtual machine
execute below vagrant command to create virtual machine(guest syste).

```bash
vagrant up
```

execute below vagrant command to access virtual machine(guest system) after being created it.

```bash
vagrant ssh
```

## configure Ansible installation
if you execute below command in virtual machine(guest system), you can know Ansible is not installed yet.

```bash
ansible --version
```

open and modify ```Vagrantfile``` like below.

```ruby
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-16.04"

  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update
    sudo apt-get install software-properties-common
    sudo apt-add-repository --yes --update ppa:ansible/ansible
    sudo apt-get install ansible --yes
  SHELL
end
```
provision shell makes to upload and execute script in virtual machine(guest system). add Ansible installation script to vagrant provision shell.

## install Ansible
execute below vagrant command in local machine(host systme).

```bash
vagrant provision
```

access virtual machine(guest system) again and check Ansible installed.

```bash
vagrant ssh

ansible --version
```

if Ansible is installed, you can see Ansible version like below.

```bash
ansible 2.7.2
  config file = /etc/ansible/ansible.cfg
  configured module search path = [u'/home/vagrant/.ansible/plugins/modules', u'/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/lib/python2.7/dist-packages/ansible
  executable location = /usr/bin/ansible
  python version = 2.7.12 (default, Dec  4 2017, 14:50:18) [GCC 5.4.0 20160609]
```

above process is we created virtual machine(guest system) without Ansible installation script in provision shell and added Ansible installation script to provision shell and executed vagrant command(```vagrant provision```) to install Ansible.

however, if you configure environment to other PC or reconfigure, you just need to execute ```vagrant up``` because your ```Vagrantfile``` already has Ansible installation script in provision shell.

execute below vagrant command to remove virtual machine(guest system) for test it.

```bash
vagrant destroy
```

execute below vagrant command to create virtual machine(guest system) again.

```bash
vagrant up
```

after creating, execute below vagrant command to access virtual machine(guest system).

```bash
vagrant ssh
```

execute below command to check Ansible is installed.

```bash
ansible --version
```

if Ansible is installed, you can see below on the screen.

```bash
ansible 2.7.2
  config file = /etc/ansible/ansible.cfg
  configured module search path = [u'/home/vagrant/.ansible/plugins/modules', u'/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/lib/python2.7/dist-packages/ansible
  executable location = /usr/bin/ansible
  python version = 2.7.12 (default, Dec  4 2017, 14:50:18) [GCC 5.4.0 20160609]
```

## completed
in here, we introduced how to install Ansible to vagrant by Vagrantfile. if Ansible masters saw this blog, maybe they say why do we need to install Ansible to vagrant? not local PC(host system)? normally people install Ansible to local machine(host system) and they use Ansible to configure the infrastructure for virtual machine(guest system) but windows OS doesn't support Ansible yet so we decided to do above process. next blog, we will introduce how to use Ansible to configure Laravel development environment in virtual machine(guest system).