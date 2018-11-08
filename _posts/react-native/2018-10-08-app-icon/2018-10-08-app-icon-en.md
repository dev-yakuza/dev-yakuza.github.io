---
layout: 'post'
permalink: '/react-native/app-icon/'
paginate_path: '/react-native/:num/app-icon/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'App icon'
description: 'try to make app icon by using generator-rn-toolbox'
image: '/assets/images/category/react-native/app-icon.jpg'
---


## outline
this blog introduces how to make app icon by using [generator-rn-toolbox](https://github.com/bamlab/generator-rn-toolbox){:rel="nofollow noreferrer" :target="_blank" } on Mac osx

## prepare app icon image
prepare 1024x1024px size png image for app icon.

## install libraries
install reuqired libraries using below code.

{% include_relative common/installation.md %}

- generator-rn-toolbox: this is tools for support RN projects. if you want to know details, see official site.(official site: [generator-rn-toolbox](https://github.com/bamlab/generator-rn-toolbox){:rel="nofollow noreferrer" :target="_blank" })
- yo: this is a library for executing generator-rn-toolbox library.

you should install ```imagemagick``` for creating app icons.

{% include_relative common/imagemagick_installation.md %}

## how to use
- execute below code for creating app icons.

{% include_relative common/usage.md %}

done! app icons were created and applied to the project. let's check it by executing RN project

{% include_relative common/start_project.md %}

if app icons is not applied, remove your app from the simulator or phone and try again.

## reference
- official site: [react-navigation](https://reactnavigation.org/docs){:rel="nofollow noreferrer" :target="_blank" }