---
layout: 'post'
permalink: '/environment/vagrant-install-and-usage/'
paginate_path: '/environment/:num/vagrant-install-and-usage/'
lang: 'en'
categories: 'environment'
comments: true

title: 'vagrant installation and usage'
description: let's see how to install virtualbox, vagrant to create virtual machine in virtual environment and how to usage vagrant to create virtual machine.
image: '/assets/images/category/environment/vagrant-install-and-usage.jpg'
---


## outline
we want to create backend - server development environment same like server. so in here, we will introduce how to use vagrant to make virtual machine.

## install virtualbox
vagrant is virtual machine management tool. in other words, vagrant is a tool to create and manage virtual machine on virtual environment. so to manage virtual environment is not vagrant feature. there are many tools to create and manage virtual environment but we will use virtualbox in here.

click below link to go to virtualbox download site.

- virtualbox: [https://www.virtualbox.org/wiki/Downloads](https://www.virtualbox.org/wiki/Downloads){:rel="nofollow noreferrer" target="_blank"}

when you see below screen, download and install virtualbox to your PC.

![virtualbox donwload page](/assets/images/category/environment/vagrant-install-and-usage/virtualbox_download.png)

to download and install virtualbox is same to download and install normal software so we will skip to talk about downloading and installing.

after installation, you can see below screen since you execute virtualbox.

![virtualbox installed](/assets/images/category/environment/vagrant-install-and-usage/virtualbox_installed.png)

## install vagrant
now we can make virtual environment by virtualbox. let's see how to install vagrant which is helpful to create virtual machine on virtual environment.

click below link to go to vagrant download site.

- vagrant: [https://www.vagrantup.com/downloads.html](https://www.vagrantup.com/downloads.html){:rel="nofollow noreferrer" target="_blank"}

after clicking above link to go to vagrant download site, you can see below screen.

![vagrant download site](/assets/images/category/environment/vagrant-install-and-usage/vagrant_site.png)

select your PC OS installer and download it. we also skip how to download and install vagrant because it's same to download and install normal software.

after installing, execute below command to check vagrant is installed.

```bash
vagrant --version
```

if vagrant is installed, you can see vagrant version like below.

```bash
Vagrant 2.2.1
```

## add box
add box that vagrant will use to make virtual machine. box is a package include OS of virtual machine and softwares in OS. below links are official basic box and vagrant user box site.

- official box site: [https://app.vagrantup.com/boxes/search](https://app.vagrantup.com/boxes/search){:rel="nofollow noreferrer" target="_blank"}
- user box site: [http://www.vagrantbox.es/](http://www.vagrantbox.es/){:rel="nofollow noreferrer" target="_blank"}

execute below vagrant command to add box to your pc.

- add official box

```bash
vagrant box add centos/7
```

- add user box

```bash
vagrant box add centos66  https://github.com/tommy-muehle/puppet-vagrant-boxes/releases/download/1.0.0/centos-6.6-x86_64.box
```

we will use official box that is ```bento/ubuntu-16.04```.

- official ```bento/ubuntu-16.04```:[https://app.vagrantup.com/bento/boxes/ubuntu-16.04](https://app.vagrantup.com/bento/boxes/ubuntu-16.04){:rel="nofollow noreferrer" target="_blank"}

execute below vagrant command to add ```bento/ubuntu-16.04``` box to your PC.

```bash
vagrant box add bento/ubuntu-16.04
```

execute below vagrant command to check added box list.

```bash
vagrant box list
```

if you add wrong box, it's possible to delete it by executing below vagrant command.

```bash
vagrant box remove bento/ubuntu-16.04
```

## create virtual machine
execute below vagrant command to create virtual machine using vagrant and added box.

```bash
# mkdir create your project folder
mkdir temp
cd temp
vagrant init bento/ubuntu-16.04
```

you can see ```Vagrantfile``` in the folder you executed command(temp). below code is contents of ```Vagrantfile```file that we removed comment out(```#```).

```ruby
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-16.04"
end
```

## execute virtual machine
execute below vagrant command to start virtual machine with ```Vagrantfile``` we made above.

```bash
vagrant up
```

execute ```virtualbox``` we downloaded and installed, we can see one virtual machine.

![virtualbox with virtual machine](/assets/images/category/environment/vagrant-install-and-usage/virtualbox-with-machine.png)


execute below vagrant command to access vitual machine.

```bash
vagrant ssh
```

execute below command to come back from virtual machine to local PC.

```bash
exit
```

## stop virtual machine
if you want to stop virtual machine, execute below vagrant command.

```bash
vagrant halt
```

## delete virtual machine
if virtual machine is not needed anymore, execute below vagrant command to delete it.

```bash
vagrant destroy
```

## completed
we saw how to make virtual machine by vagrant. in next blog posts, we will introduce how to configure development environment by editing ```Vagrantfile``` file and how to set development environment in virtual machine.