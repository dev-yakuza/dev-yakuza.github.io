---
layout: 'post'
permalink: '/git/sync-fork-repository/'
paginate_path: '/git/:num/sync-fork-repository/'
lang: 'en'
categories: 'git'
comments: true

title: 'Sync Fork repository'
description: Let's see how to sync Fork repository to Original repository.
image: '/assets/images/category/git/2020/sync-fork-repository/background.jpg'
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [Add original repository](#add-original-repository)
- [Get original repository contents](#get-original-repository-contents)
- [Rebase](#rebase)
- [Sync Fork branch](#sync-fork-branch)
- [Completed](#completed)

</div>

## Outline

If you commit the opensource, or your company uses GitHub, you fork the repository to your repository. And then, you clone and modify the source code from the forked repository, and send Pull request for the merge.

However, the opensource and company source is not managed by only one person, it occurs difference between your fork repository and the original repository when you send Pull request.

In this blog post, we will see how to sync the forked repository Master branch and the original repository Master branch.

## Add original repository

To sync the original repository and Fork repository, we need to add the original repository to the local remote address.

Execute the command below to check the current added remote address.

```bash
git remote -v
```

After executing, you can see the result like below.

```bash
origin  https://github.com/USER_NAME/FORK_REPOSITORY.git (fetch)
origin  https://github.com/USER_NAME/FORK_REPOSITORY.git (push)
```

Of course, we cloned the Fork repository to the local, so we got the result like above. Next, execute the command below to add the original repository to the local remote address.

```bash
git remote add upstream https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git
```

Nomally, people use `upstream` name for the original repository, but it is just the name, so you can use other names like below.

```bash
git remote add test https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git
```

In here, we use `upstream`. Execute the command below to check the original repository added well on the remote address.

```bash
git remote -v
```

If the original repository is added well, you can see the result like below.

```bash
origin    https://github.com/USER_NAME/FORK_REPOSITORY.git (fetch)
origin    https://github.com/USER_NAME/FORK_REPOSITORY.git (push)
upstream  https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git (fetch)
upstream  https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git (push)
```

{% include in-feed-ads.html %}

## Get original repository contents

We've added the original repository to the remote address. Next, we'll get the original repository contents on the local by `Fetch`.

Execute the command below to get the original repostiory contents.

```bash
git fetch upstream master
```

## Rebase

Currently, the local Master branch's `Base` is the Fork repository Master branch, because we've cloned the Fork repository. Next, we'll change the local Master branch Base to the original Master branch Base that we've gotten via `Fetch`.

Execute the command below to change the local Master branch Base to the original repository Master branch.

```bash
git rebase upstream/master
```

Now, the local Master branch Base is the original Master branch.

## Sync Fork branch

The local Master branch Base was changed the original Master branch by Rebase. Next, we need to change the Fork repository Master branch Base to the original repository Master branch, too.

Execute the command below to sync the Fork repository Master branch and the original repository Master branch.

```bash
git push origin master -f
```

## Completed

In working or committing the open-source, sometimes we need to sync the repositories. Now, you know how to sync the repositories, so sync the Fork repository and the original repository via Rebase.
