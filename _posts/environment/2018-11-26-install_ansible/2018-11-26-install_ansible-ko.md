---
published: false
layout: 'post'
permalink: '/environment/install-ansible/'
paginate_path: '/environment/:num/install-ansible/'
lang: 'ko'
categories: 'environment'
comments: true

title: '앤서블 설치'
description: 'vagrant로 생성한 가상 머신에 앤서블(ansible)을 설치하여 앤서블(ansible)을 사용할 수 있는 환경을 만듭니다.'
image: '/assets/images/category/environment/install-ansible.jpg'
---


## 개요
앤서블(ansible)을 설명하자면 책 한권이 필요합니다. 우리도 아직 잘 모르고 남들에게 설명할 정도에 레벨이 아니므로 자세한 설명을 할 수 없지만 우리가 사용하고 있는 방법을 소개하는 것으로 앤서블(ansible)을 소개하려 합니다. 앤서블(ansible)을 간단히 설명하자면 인프라에 관련된 전반적인 자동화툴입니다. 설치(installation) 및 배포(deploy) 등 수 많은 것을 자동화 할 수 있습니다. 이 블로그에서는 vagrant에 앤서블(ansible)을 설치하는 방법에 대해서 알아봅니다.

이 블로그 포스트는 PC에 virtualbox, vagrant가 설치되어 있는 환경을 대상으로 하며 virtualbox, vagarnt에 설치 방법은 이전 블로그인 [vagrant 설치 및 사용법]({{site.url}}/{{page.categories}}/vagrant-install-and-usage/){:target="_blank"}를 확인해 주세요.

## 가상 머신 생성
아래에 vagrant 명령어를 통해 가상 머신을 생성합니다.