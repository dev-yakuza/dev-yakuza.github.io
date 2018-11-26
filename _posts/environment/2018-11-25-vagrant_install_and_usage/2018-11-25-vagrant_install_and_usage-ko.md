---
layout: 'post'
permalink: '/environment/vagrant-install-and-usage/'
paginate_path: '/environment/:num/vagrant-install-and-usage/'
lang: 'ko'
categories: 'environment'
comments: true

title: 'vagrant 설치 및 사용법'
description: '가상 머신을 사용하여 개발 환경을 구축하기 위해 virtualbox, vagrant를 설치하는 방법을 알아보고 가상 머신을 만들기 위해 vagrant를 사용하는 방법에 대해서 알아봅니다.'
image: '/assets/images/category/environment/vagrant-install-and-usage.jpg'
---


## 개요
백엔드(backend) - 서버를 개발하기 위해서 서버와 동일한 환경을 구축하려고 합니다. 여기에서는 vagrant를 사용하여 가상 머신을 만드는 방법을 소개합니다.

## virtualbox 설치
vagrant는 가상 머신을 쉽게 만들고 관리해주는 툴입니다. 다시말해, 가상 환경위에 가상 머신을 설치하고 관리해주는 툴입니다. 따라서 가상 머신을 돌릴 가상 환경은 vagrant의 관리밖입니다. 가상 환경을 만들어주는 여러 툴이 있지만 여기에서는 virtualbox를 활용하겠습니다.

아래에 링크를 눌러 virtualbox의 다운로드 페이지로 이동합니다.

- virtualbox: [https://www.virtualbox.org/wiki/Downloads](https://www.virtualbox.org/wiki/Downloads){:rel="nofollow noreferrer" target="_blank"}

아래와 같은 화면에서 자신의 PC에 해당하는 다운로드 파일을 다운로드받아 설치합니다.

![virtualbox donwload page](/assets/images/category/environment/vagrant-install-and-usage/virtualbox_download.png)

virtualbox 다운로드 및 설치 과정은 일반적인 소프트웨어를 설치하는 것과 동일하기 때문에 자세한 설명은 생략하겠습니다.

설치가 완료하고 virtualbox를 실행하면 아래와 같은 화면을 볼수 있습니다.

![virtualbox installed](/assets/images/category/environment/vagrant-install-and-usage/virtualbox_installed.png)

## vagrant 설치
virtualbox 설치로 이제 가상 환경을 만들 수 있습니다. 이제 가상 환경에서 돌아갈 가상 머신을 쉽고 간단하게 만들 수 있게 도와주는 vagrant의 설치 방법에 대해서 알아봅니다.

아래에 링크를 눌러 vagrant 다운로드 사이트로 이동합니다.

- vagrant: [https://www.vagrantup.com/downloads.html](https://www.vagrantup.com/downloads.html){:rel="nofollow noreferrer" target="_blank"}

위에 링크를 눌러 vagrant 다운로드 사이트로 이동하면 아래와 같은 화면을 볼 수 있습니다.

![vagrant download site](/assets/images/category/environment/vagrant-install-and-usage/vagrant_site.png)

자신의 PC의 OS에 맞는 설치 파일을 선택하여 다운로드합니다. 역시 vagrant의 다운로드 및 설치 방법은 일반적인 소프트웨어를 다운로드하고 설치하는 방법과 동일하기 때문에 설명을 생략하겠습니다.

설치가 완료되면 아래에 명령어를 실행하여 vagrant가 잘 설치되었는지 확인합니다.

```bash
vagrant --version
```

vagrant가 잘 설치되었다면 아래와 같이 설치된 vagrant의 버전을 확인할 수 있습니다.

```bash
Vagrant 2.2.1
```

## box 추가
vagrant가 가상 머신을 만들기 위해 사용할 box를 추가합니다. box는 가상 머신이 될 OS와 OS에 포함된 소프트웨어들을 모아둔 패키지입니다. 아래는 기본이 되는 공식 box와 vagrant 유저들이 만든 box의 사이트입니다.

- 공식 box 사이트: [https://app.vagrantup.com/boxes/search](https://app.vagrantup.com/boxes/search){:rel="nofollow noreferrer" target="_blank"}
- 유저 box 사이트: [http://www.vagrantbox.es/](http://www.vagrantbox.es/){:rel="nofollow noreferrer" target="_blank"}

아래에 vagrant 명령어를 통해 box를 자신의 PC에 추가합니다.

- 공식 box 추가

```bash
vagrant box add centos/7
```

- 유저 box 추가

```bash
vagrant box add centos66  https://github.com/tommy-muehle/puppet-vagrant-boxes/releases/download/1.0.0/centos-6.6-x86_64.box
```

우리는 공식 box인 ```bento/ubuntu-16.04```를 사용할 예정입니다

- 공식 ```bento/ubuntu-16.04```:[https://app.vagrantup.com/bento/boxes/ubuntu-16.04](https://app.vagrantup.com/bento/boxes/ubuntu-16.04){:rel="nofollow noreferrer" target="_blank"}

아래에 vagrant 명령어를 통해 ```bento/ubuntu-16.04``` box를 자신의 PC에 추가합니다.

```bash
vagrant box add bento/ubuntu-16.04
```

아래에 vagrant 명령어로 추가된 box 리스트를 확인할 수 있습니다.

```bash
vagrant box list
```

만약 잘못된 box를 추가하였다면 아래에 vagrant 명령어로 추가된 box를 제거할 수 있습니다.

```bash
vagrant box remove bento/ubuntu-16.04
```

## 가상 머신 생성
아래에 vagrant 명령어를 통해 vagrant와 추가한 box를 이용하여 가상 머신을 생성합니다.

```bash
# mkdir create your project folder
mkdir temp
cd temp
vagrant init bento/ubuntu-16.04
```

명령어를 실행한 폴더(temp)에 ```Vagrantfile``` 파일이 생성된 것을 확인할 수 있습니다. 아래는 주석 처리(```#```)가 된 부분을 제외한 ```Vagrantfile```의 내용입니다.

```ruby
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-16.04"
end
```

## 가상 머신 실행
위에서 생성한 ```Vagrantfile```를 아래에 vagrant 명령어로 vagrant를 사용하여 가상 머신을 실행합니다.

```bash
vagrant up
```

우리가 다운로드하고 설치한 ```virtualbox```를 실행해 보면 가상 머신이 생성된 것을 확인할 수 있습니다.

![virtualbox with virtual machine](/assets/images/category/environment/vagrant-install-and-usage/virtualbox-with-machine.png)

아래에 vagrant 명령어를 통해 가상 머신에 접근합니다.

```bash
vagrant ssh
```

아래에 명령어를 통해 가상 머신에서 로컬 PC 환경으로 나옵니다.

```bash
exit
```

## 가상 머신 중지
가상 머신에 사용을 중지하고 싶을 때, 아래에 vagrant 명령어를 실행합니다.

```bash
vagrant halt
```

## 가상 머신 삭제
가상 머신이 더 이상 필요하지 않을 때, 아래에 vagrant 명령어로 가상 머신을 삭제합니다.

```bash
vagrant destroy
```

## 완료
이것으로 vagrant를 이용한 가상 머신을 만드는 방법을 살펴보았습니다. 앞으로는 ```Vagrantfile``` 파일을 수정하거나 가상 머신안에 개발 환경을 구축하는 방법에 대해 소개할 예정입니다.