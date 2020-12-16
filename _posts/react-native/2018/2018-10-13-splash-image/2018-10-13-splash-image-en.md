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

<div id="contents_list" markdown="1">

## Contents

1. [Deprecated](#deprecated)
1. [outline](#outline)
1. [libaray installation](#libaray-installation)
1. [prepare splash image](#prepare-splash-image)
    - [export psd from sketchapp](#export-psd-from-sketchapp)
1. [set splash image](#set-splash-image)
1. [check it out](#check-it-out)
1. [error](#error)
    - [Can't Generate Images](#cant-generate-images)
1. [Control Splash screen](#control-splash-screen)
1. [reference](#reference)

</div>

## Deprecated

generator-rn-toolbox is `Deprecated`, so this blog post is not managed any more.If you want to make App icon easily, I recommend to use `react-native-make` that is a new library of generator-rn-toolbox.

If you want to know more, see the blog below.

- [react-native-make]({{site.url}}/{{page.categories}}/react-native-make/){:target="_blank"}

## outline

we introduce how to generate splash images created by [generator-rn-toolbox](https://github.com/bamlab/generator-rn-toolbox){:rel="nofollow noreferrer" target="_blank" } on mac osx.

## libaray installation

if you want to know how to install generator-rn-toolbox library, see previous blog post [App icon]({{site.url}}/{{page.categories}}/app-icon/){:target="_blank"}.

## prepare splash image

prepare 2208x2208px size ```psd``` file not png, jpg for generating splash images.

### export psd from sketchapp

we use sketchapp for design but it is impossible to export psd file from sketchapp. however if you follow below, you can make psd file from sketchapp.

1. design splash image by sketchapp.
1. export splash image to png on sketchapp.
1. search 'png to psd converter' on the internet for converting the file.(we use this [site](https://www.photopea.com/){:rel="nofollow noreferrer" target="_blank" })

{% include in-feed-ads.html %}

## set splash image

create and set splash image by below code on cmd.

{% include_relative common/usage.md %}

## check it out

splash image is created and applied to the project. let's check splash image is applied by running the project.

{% include_relative common/start_project.md %}

if splash image is not showing up, remove your app from the simulator or phone and do again.

## error

we got the problem not to show Splash image up full size. so we've modified ```android/app/src/main/res/drawable/launch_screen_bitmap.xml``` file like below.

```xml
<bitmap
    android:src="@drawable/launch_screen"
    android:gravity="fill_horizontal|fill_vertical"/>
```

### Can't Generate Images

I got the erro below and couldn't generate the images.

```bash
Error: Command failed: identify: FailedToExecuteCommand `'gs'
```

execute the command below to install ```ghostscript```.

```bash
brew install ghostscript
```

and execute the commands below, you can see that the images are generated.

{% include_relative common/usage.md %}

{% include in-feed-ads.html %}

## Control Splash screen

somtimes, we need to control Splash Screen. for example, you want to check login or download the data in showing Splash screen. if you are in this case, see the blog post below to control Splash screen.

- [App Splash Screen]({{site.url}}/{{page.categories}}/react-native-splash-screen/){:target="_blank"}

## reference

- official site: [generator-rn-toolbox](https://github.com/bamlab/generator-rn-toolbox){:rel="nofollow noreferrer" target="_blank" }
