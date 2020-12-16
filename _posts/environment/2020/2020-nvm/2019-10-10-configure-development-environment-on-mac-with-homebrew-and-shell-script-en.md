---
layout: 'post'
permalink: '/environment/nvm/'
paginate_path: '/environment/:num/nvm/'
lang: 'en'
categories: 'environment'
comments: true

title: (macOS) Manage Node versions via NVM
description: Let's see how to install NVM(Node Version Manager) on macOS and how to manage Node versions.
image: '/assets/images/category/environment/2020/nvm/background.jpg'
---

<div id="contents_list" markdown="1">

## Content

- [Outline](#outline)
- [Install NVM](#install-nvm)
- [Configure NVM](#configure-nvm)
- [How to use](#how-to-use)
  - [Node version list](#node-version-list)
  - [Install Node](#install-node)
  - [Change Node version](#change-node-version)
- [Delete Node version](#delete-node-version)
- [Manage Node version by project](#manage-node-version-by-project)
  - [Create .nvmrc](#create-nvmrc)
  - [How to use .nvmrc](#how-to-use-nvmrc)
- [Completed](#completed)

</div>

## Outline

I'm a Mac user. I'm developing many projects on Mac, so I need to manage Node versions. In this blog post, I will show how to manage Node versions by using `NVM(Node Version Manager)`.

- NVM(Node Version Manager): [Official site](https://github.com/nvm-sh/nvm){:rel="nofollow noreferrer" target="_blank"}

This blog post is for the macOS only and for Mac that `Homebrew` was installed on.

## Install NVM

Execute the command below to install NVM.

```bash
brew install nvm
```

{% include in-feed-ads.html %}

## Configure NVM

You need to configure `.zshrc` file to use NVM on the Terminal. Open `.zshrc` file and modify it like below.

```bash
# code ~/.zshrc
...
export NVM_DIR=~/.nvm
source $(brew --prefix nvm)/nvm.sh
```

After setting, restart the Terminal, and execute the command below to check NVM was installed well.

```bash
nvm --version
```

If you install and set well, you can see the result like below.

```bash
0.35.3
```

## How to use

We've installed, so Let's see how to use NVM to manage Node versions.

### Node version list

You can see the Node version list that you can install by executing the command below.

```bash
nvm ls-remote
```

### Install Node

After checking the versions, You can install the Node version by executing the commands below.

- Install newest Node version

  ```bash
  nvm install node
  ```

- Install LTS release Node version

  ```bash
  nvm install --lts
  ```

- Install specific Node version

  ```bash
  nvm install 13.12.0
  ```

After installing, you can see the installed Node versions by executing the command below.

```bash
nvm ls
```

{% include in-feed-ads.html %}

### Change Node version

If you installed various Node versions via NVM, you can change the Node version by executing the command below.

```bash
nvm use 13.12.0
```

Execute the command below to check the Node version is changed well.

```bash
nvm ls
```

If the version is changed well, you can see the result like below.

```bash
       v8.9.0
       v12.16.1
->     v13.12.0
         system
```

## Delete Node version

Execute the command below to delete the Node version which you want to delete.

```bash
nvm uninstall 8.9.0
```

After deleting, you can see the result like below.

```bash
Uninstalled node v8.9.0
```

## Manage Node version by project

We've seen how to install Node versions via NVM and how to use the Node version via NVM. Next, let's see how to manage the Node version by project.

### Create .nvmrc

To manage the Node version by project, You need to create `.nvmrc` file. Create `.nvmrc` file on the root folder of the project, and modify it like below.

```bash
12.16.1
```

{% include in-feed-ads.html %}

### How to use .nvmrc

To use this Node version, execute the command below on the folder which `.nvmrc` exists.

```bash
nvm use
```

If the Node version in `.nvmrc` file was installed on Local, you can see the result like below.

```bash
Found '/projects/.nvmrc' with version <12.16.1>
Now using node v12.16.1 (npm v6.13.4)
```

If the Node version didn't exist on Local, you can see the result like below.

```bash
Found '/projects/.nvmrc' with version <8.9.0>
N/A: version "8.9.0 -> N/A" is not yet installed.

You need to run "nvm install 8.9.0" to install it before using it.
```

If you don't have the Node version in `.nvmrc` file like above, you can install the Node version by executing the command below.

```bash
nvm install
```

After installing, you can see the result like below.

```bash
...
Checksums matched!
Now using node v8.9.0 (npm v5.5.1)
```

## Completed

In this blog post, we've seen how to install various Node versions on Local by NVM(Node Version Manager) and how to use it. Also, we've seen how to create `.nvmrc` file to manage the Node versions by projects, and how to use or install the Node version by using `.nvmrc` file.

Now, Let's manage the Node versions by projects via NVM!
