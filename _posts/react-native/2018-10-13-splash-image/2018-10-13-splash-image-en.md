---
layout: 'post'
permalink: '/react-native/splash-image/'
paginate_path: '/react-native/:num/splash-image/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'Splash image'
description: 'generate and apply splash image by using generator-rn-toolbox'
image: '/assets/images/category/react-native/splash-image.jpg'
---


## outline
we introduce how to generate splash images created by [generator-rn-toolbox](https://github.com/bamlab/generator-rn-toolbox){:rel="nofollow noreferrer" target="_blank" } on mac osx.

## libaray installation
if you want to know how to install generator-rn-toolbox library, see previous blog post [App icon]({{site.url}}/{{page.categories}}/app-icon/){:target="_blank"}.

## prepare splash image
prepare 2208x2208px size ```psd``` file not png, jpg for generating splash images.

### export psd from sketchapp
we use sketchapp for design but it is impossible to export psd file from sketchapp. however if you follow below, you can make psd file from sketchapp.

1. design splash image by sketchapp.
1. export splash image to pdf on sketchapp.
1. search 'pdf to psd converter' on the internet for converting the file.(we use this [site](https://www.pdfconvertonline.com/pdf-to-psd-online.html){:rel="nofollow noreferrer" target="_blank" })

## set splash image
create and set splash image by below code on cmd.

{% include_relative common/usage.md %}

## check it out
splash image is created and applied to the project. let's check splash image is applied by running the project.

{% include_relative common/start_project.md %}

if splash image is not showing up, remove your app from the simulator or phone and do again.

## reference
- official site: [generator-rn-toolbox](https://github.com/bamlab/generator-rn-toolbox){:rel="nofollow noreferrer" target="_blank" }