---
layout: 'post'
permalink: '/environment/install-ansible/'
paginate_path: '/environment/:num/install-ansible/'
lang: 'ko'
categories: 'environment'
comments: true

title: '앤서블 설치'
description: 'vagrant로 생성한 가상 머신(guest system)에 앤서블(Ansible)을 설치하여 앤서블(Ansible)을 사용할 수 있는 환경을 만듭니다.'
image: '/assets/images/category/environment/install-ansible.jpg'
---


## 개요
앤서블(Ansible)을 설명하자면 책 한권이 필요합니다. 우리도 아직 잘 모르고 남들에게 설명할 정도에 레벨이 아니므로 자세한 설명을 할 수 없지만 우리가 사용하고 있는 방법을 소개하는 것으로 앤서블(Ansible)을 소개하려 합니다. 앤서블(Ansible)을 간단히 설명하자면 인프라에 관련된 전반적인 자동화툴입니다. 설치(installation) 및 배포(deploy) 등 수 많은 것을 자동화 할 수 있습니다. 이 블로그에서는 vagrant에 앤서블(Ansible)을 설치하는 방법에 대해서 알아봅니다.

이 블로그 포스트는 PC에 virtualbox, vagrant가 설치되어 있는 환경을 대상으로 하며 virtualbox, vagarnt에 설치 방법은 이전 블로그인 [vagrant 설치 및 사용법]({{site.url}}/{{page.categories}}/vagrant-install-and-usage/){:target="_blank"}를 확인해 주세요.

## 가상 머신 설정 생성
아래에 vagrant 명령어를 통해 가상 머신(guest system)을 설정 생성합니다.

```bash
vagrant init bento/ubuntu-16.04
```

vagrant 명령어를 실행한 폴더에 ```Vagrantfile``` 파일이 생성된 것을 확인할 수 있습니다. 아래는 주석 처리(```#```)가 된 부분을 제외한 ```Vagrantfile```의 내용입니다.

```ruby
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-16.04"
end
```

## 가상 머신 생성 및 확인
아래에 vagrant 명령어를 통해 가상 머신(guest system)을 생성합니다

```bash
vagrant up
```

가상 머신(guest system)이 생성되었다면 아래에 vagrant 명령어로 가상 머신(guest system)에 접속합니다.

```bash
vagrant ssh
```

## 앤서블 설치 설정
가상 머신(guest system)안에서 아래에 명령어를 실행해 보면 아직 앤서블(Ansible)이 설치되지 않았음을 확인할 수 있습니다.

```bash
ansible --version
```

다시 ```Vagrantfile``` 파일을 열어 아래와 같이 수정합니다.

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

프로비전 쉘(provision shell)은 가상 머신(guest system)에 스크립트를 업로드하고 실행할 수 있게 해줍니다. vagrant의 프로비전 쉘(provision shell)에 앤서블(Ansible) 설치 스크립트를 추가합니다.

## 앤서블 설치
아래에 vagrant 명령어를 로컬 머신(host system)에서 실행합니다.

```bash
vagrant provision
```

그리고 다시 가상 머신(guest system)에 접속한 후 앤서블(Ansible)이 설치되었는지 확인합니다.

```bash
vagrant ssh

ansible --version
```

문제없이 앤서블(Ansible)이 설치되었다면 아래와 같이 앤서블(Ansible)의 버전을 확인할 수 있습니다.

```bash
ansible 2.7.2
  config file = /etc/ansible/ansible.cfg
  configured module search path = [u'/home/vagrant/.ansible/plugins/modules', u'/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/lib/python2.7/dist-packages/ansible
  executable location = /usr/bin/ansible
  python version = 2.7.12 (default, Dec  4 2017, 14:50:18) [GCC 5.4.0 20160609]
```

지금은 프로비전 쉘(provision shell)에 앤서블(Ansible)을 설정하지 않은 상태에서 가상 머신(guest system)을 만든 후 프로비전 쉘(provision shell)을 입력하고 vagrant 명령어(```vagrant provision```)으로 앤서블(Ansible)을 설치했습니다.

하지만 다른 PC 또는 새롭게 환경을 재구성할 때에는 이미 프로비전 쉘(provision shell)이 설정된 ```Vagrantfile``` 파일을 이용하므로 ```vagrant up``` 명령어를 실행하는 것만으로 앤서블(Ansible)이 설치됩니다.

확인을 위해 아래에 vagrant 명령어로 가상 머신(guest system)을 제거합니다.

```bash
vagrant destroy
```

다시 아래에 vagrant 명령어로 가상 머신(guest system)을 생성합니다.

```bash
vagrant up
```

생성이 완료되면 아래에 vagrant 명령어로 가상 머신(guest system)에 접속합니다.

```bash
vagrant ssh
```

앤서블(Ansible)이 설치되었는지 확인하기 위해 아래에 명령어를 입력합니다.

```bash
ansible --version
```

앤서블(Ansible)이 문제없이 설치되었다면 아래와 같은 화면을 다시 볼 수 있습니다.

```bash
ansible 2.7.2
  config file = /etc/ansible/ansible.cfg
  configured module search path = [u'/home/vagrant/.ansible/plugins/modules', u'/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/lib/python2.7/dist-packages/ansible
  executable location = /usr/bin/ansible
  python version = 2.7.12 (default, Dec  4 2017, 14:50:18) [GCC 5.4.0 20160609]
```

## 완료
이번 블로그에서는 Vagrantfile 파일을 이용하여 vagrant에 앤서블(Ansible)을 설치하는 방법에 대해 살펴보았습니다. 앤서블(Ansible)을 잘 사용하고 계신 분들은 왜 이렇게 하는지 의아해 하실 수 있습니다. 보통 앤서블(Ansible)을 로컬 머신(host system)에 설치하고 가상 머신(guest system)에 인프라 구축을 위해 사용을 하시는 분들이 많습니다. 하지만 아직 윈도우즈(Windows)에서 앤서블(Ansible)을 지원하지 않기 때문에 저희는 위와 같은 방법을 선택했습니다. 다음 블로그에서는 앤서블(Ansible)을 활용하여 라라벨(Laravel) 개발 환경을 구축하는 방법을 살펴보겠습니다.