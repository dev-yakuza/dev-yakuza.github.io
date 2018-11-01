---
layout: 'post'
permalink: '/git/create-repository/'
paginate_path: '/git/:num/create-repository/'
lang: 'en'
categories: 'git'
comments: true

title: 'create Repository'
description: 'create git repository for using git. git repository is the storage to manage source code version.'
image: '/assets/images/category/git/create-repository.jpg'
---

## outline
we already installed git so let's use git for managing source code. we introduce how to create git repository for managing source code by git at here. git repository is the storage where source code changing hisotries store

## create project folder
we use ```terminal``` for Mac, and ```cmd``` for Windows. create the folder for using git.

```bash
mkdir temp_test_git
```
## create git repository
create git repository for using git in the project folder.

```bash
cd temp_test_git

git
```
execute above command, you can see git command list.

![git clone init](/assets/images/category/git/create-repository/clone_init.png)

you can see ```clone``` and ```init``` command in git command list.

- init: create new git repository.
- clone: clone(copy) new repository from existing git repository.

### git init
if you start new project, you can make new git repository with ```init``` command.

```bash
git init
```

### git clone
if you have existing project(Opensource or project already managed by git), you can clone(copy) the repository from remote repository.

we introduce how to clone(copy) git project using our blog git repository.

- our git repository: [https://github.com/dev-yakuza/dev-yakuza.github.io](https://github.com/dev-yakuza/dev-yakuza.github.io){:rel="nofollow noreferrer" :target="_blank"}

click the above link to go to the our git repository in github.

![git clone blog](/assets/images/category/git/create-repository/clone.png)

click ```Clone or download``` button on right side and copy the url of the git repository.

```bash
 git clone https://github.com/dev-yakuza/dev-yakuza.github.io.git
```

execute the above command to clone our git repository to your local pc. we serve our blog by using ```jekyll``` and github page. if you are interested about how to make a blog with jekyll and github, please check our another blog series([jekyll blog]({{site.url}}/jekyll/){:target="_blank"}).

## check git repository created
execute the below command for checking git repository created.

```bash
# Mac
ls -al

# Windows
dir /ah
```

if you can see ```.git``` folder in folder list, you are succeed to create git repository. ```.git``` folder stores informations about source code edit histories when you use git to manage them. if you delete ```.git``` folder, you delete also all histories and git repository so please be careful not to delete it.

## configure user
add user to new git repository for managing source code version. we can recognize who edit source code if git user is set.

```bash
# git config --global user.name [user name]
git config --global user.name dev.yakuza

# git config --global user.email [user email]
git config --global user.email dev.yakuza@gmail.com
```