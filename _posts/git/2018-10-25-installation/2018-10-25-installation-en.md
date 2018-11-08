---
layout: 'post'
permalink: '/git/installation/'
paginate_path: '/git/:num/installation/'
lang: 'en'
categories: 'git'
comments: true

title: 'git installation'
description: we use git for source code version control tool. before using git, let's install git first.
image: '/assets/images/category/git/installation.jpg'
---

## source code version controls
git can manage the version of the source code. managing version's mean is storing and managing the editing history of the source code. you wanted to go before editing the source code but you didn't remember where you edit. you were in trouble, weren't you? if you use source code version control like git, you can solve this kind of situation. however git is not a magic tool like we push ```ctrl + z``` keys for going back to change text.

source code version control is that developer edits the source code and stores them to another space(Repository) with editing histories. and then if developer want to go back to the before editing, developer pulls the source code which is before editing from another space(Repository) via the source code version control like git.

git is the one of the source code version control and has many features. we use the parts of them, and actually we don't know exactly what it is so we start to this blog. we hope this blog helpful for you too.

## git installation
before using git, let's install git to PC. install git by following the installation instructions for your OS.

## intsll git on Mac
click the below link for downloading git installation file for Mac.

- download link: [https://git-scm.com/download/mac](https://git-scm.com/download/mac){:rel="nofollow noreferrer" :target="_blank"}

if downloading is not started automatically, click the ```click here to download manually``` link on the site.

![git download for mac](/assets/images/category/git/installation/download_mac.png)

if downloading is finished, click the file for installing. installing is same processing when you download and install other programs via Web. if you see security warning, go to the settings of the Mac and confirm it for installing.

if installation is finished, execute the below code on ```terminal``` for check to finish installing on Mac.

```bash
git --version
```

## install git to Windows
click the below link for downloading git installation file for Windows.

- download link: [https://gitforwindows.org/](https://gitforwindows.org/){:rel="nofollow noreferrer" :target="_blank"}

![git download for windows](/assets/images/category/git/installation/download_windows.png)

if downloading is completed, you can install it on Windows like other programs.

when installation is finished, execute the below code on ```commands``` for checking to complete the installation.

```bash
git --version
```

you can open ```commands``` by pressing ```windows key + r``` and typing ```cmd``` and pressing ```enter```.

## completed
completed to install. now we can use git on PC.