---
layout: 'post'
permalink: '/git/default-branch/'
paginate_path: '/git/:num/default-branch/'
lang: 'en'
categories: 'git'
comments: true

title: "[Git] Configure default branch from master to main"
description: Let's how to configure the default branch of Git from master to main.
image: '/assets/images/category/git/2021/default-branch/background.jpg'
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [Git config](#git-config)
- [Completed](#completed)

</div>

## Outline

There are many arguments about the `master` name of the default branch in Git. So, many services decide to drop `master` for the name of the branch.

- GitHub [Renaming the default branch from master](https://github.com/github/renaming){:rel="nofollow noreferrer noopener" target="_blank"}

However, when we use Gith on Local, the `master` branch is still the default branch. So, when we create a new Git repository on local, the branch name is `master`. And then, we should change it to `main`. In this blog post, I will show you how to change the default branch to `main` from `master` to solve this inconvenience.

## Git config

You can configure almost all of the Git settings with the `git config` command. Of course, you can change the default branch name by this command. Execute the command below to change the default branch name from `master` to `main`.

```bash
git config --global init.defaultBranch main
```

After executing this command, when you execute the following command to create a new Git repository, you can see the default branch name is `main` instead of `master`.

```bash
git init
```

## Completed

Done! we've seen how to change the default branch from `master` to `main`. It's very easy, so I hope you configure this and you join this movement.
