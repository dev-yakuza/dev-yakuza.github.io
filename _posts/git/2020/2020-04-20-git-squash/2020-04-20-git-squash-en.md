---
layout: 'post'
permalink: '/git/git-squash/'
paginate_path: '/git/:num/git-squash/'
lang: 'en'
categories: 'git'
comments: true

title: 'Make many commits to one commit via Git squash'
description: Let's see how to make many commits to one commit via Git squash.
image: '/assets/images/category/git/2020/git-squash/background.jpg'
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [Git Squash](#git-squash)
  - [Git Log](#git-log)
  - [Git Rebase](#git-rebase)
  - [Git Push](#git-push)
- [Completed](#completed)

</div>

## Outline

When you commit the open-source, or modify your company source code, normally, make an Issue, and make a branch based on the Issue. And then, we modify this branch and commit it. However, we can't modify all by one commit. We need to commit Front side, Server side, Test code, and Code reviews, so many commits occur.

Of course, we can simply merge these commits, but the open-source or the company source code which many people develop, commit history is too complicated and difficult to track it in this case.

To prevent this problem, we'll see how to use Git `Squash` feature in this blog post.

## Git Squash

Git Squash can compress various commit logs to one commit log.

### Git Log

First, execute the command below to see the commit history.

```bash
git log --pretty=oneline
```

And then, you can see the result like below.

```bash
1f199b7353e40e3134572c9986837b1b4bfebd13 (HEAD -> squash-test) third commit
0118d468a770c2340bf6d4d47f10984c58ea382b second commit
b91e257ce42d5f501c7bc8242a0580b3c05ef462 first commit
db078dae819cfed46bc6e6ef8c962648f97c22da (origin/master, origin/develop, master, develop) Merge pull request #1 from dev-yakuza/rebase-and-squash
c6bd068ec0ea39ef98e135218dc19375e5d63a68 (origin/rebase-and-squash, rebase-and-squash) add rebase-and-squash
2d33cf05e6352b2fa7e8574d170032b34e3a8959 change master
405d0d71ed50429a169ece18cf984dfd64c088a9 add proejct
```

In my case, I've made `squash-test` branch from Master branch, and commit three times(`first commit`, `second commit`, `third commit`).

```bash
1f199b7353e40e3134572c9986837b1b4bfebd13 (HEAD -> squash-test) third commit
0118d468a770c2340bf6d4d47f10984c58ea382b second commit
b91e257ce42d5f501c7bc8242a0580b3c05ef462 first commit

db078dae819cfed46bc6e6ef8c962648f97c22da (origin/master, origin/develop, master, develop) Merge pull request #1 from dev-yakuza/rebase-and-squash
```

{% include in-feed-ads.html %}

### Git Rebase

Next, we'll make `first commit`, `second commit`, `third commit` commits to one simple commit by Git Squash. To use Squash, we need to use Git `Rebase`.

Check Git log again,

```bash
1f199b7353e40e3134572c9986837b1b4bfebd13 (HEAD -> squash-test) third commit
0118d468a770c2340bf6d4d47f10984c58ea382b second commit
b91e257ce42d5f501c7bc8242a0580b3c05ef462 first commit

# We will rebase on here!!!!!!!!
db078dae819cfed46bc6e6ef8c962648f97c22da (origin/master, origin/develop, master, develop) Merge pull request #1 from dev-yakuza/rebase-and-squash
```

I want to compress three commits to one commit, so I'll Rebase on `db078dae819cfed46bc6e6ef8c962648f97c22da` that is before I committed three times.

Execute the Git Rebase command like below to use Squash.

```bash
git rebase -i db078dae819cfed46bc6e6ef8c962648f97c22da
```

You should notice that I used `-i` option. we use `-i` option, we can get the result like below.

```bash
pick b91e257 first commit
pick 0118d46 second commit
pick 1f199b7 third commit

# Rebase db078da..1f199b7 onto db078da (3 commands)
#
# Commands:
# p, pick <commit> = use commit
# r, reword <commit> = use commit, but edit the commit message
# e, edit <commit> = use commit, but stop for amending
# s, squash <commit> = use commit, but meld into previous commit
# f, fixup <commit> = like "squash", but discard this commit's log messag
```

This scene is that Git tries to go to the past, but there are commits between the current and past, so Git asks us what to do kindly. There is Command list on the bottom. We'll use `s, squash` in here.

```bash
# s, squash <commit> = use commit, but meld into previous commit
```

In my case, I will leave `first commit` commit, and Squash `second commit` and `third commit` to it. Press `i` button on the keyboard to make the modification status, and then modify it like below.

```bash
pick b91e257 first commit
s 0118d46 second commit
s 1f199b7 third commit

# Rebase db078da..1f199b7 onto db078da (3 commands)
#
# Commands:
# p, pick <commit> = use commit
# r, reword <commit> = use commit, but edit the commit message
# e, edit <commit> = use commit, but stop for amending
# s, squash <commit> = use commit, but meld into previous commit
# f, fixup <commit> = like "squash", but discard this commit's log messag
```

After it, press `ESC` button on the keyboard, and insert `:wq` and press `Enter` key to save it. After saving, you can see the screen like below.

```bash
# This is a combination of 3 commits.
# This is the 1st commit message:

first commit

# This is the commit message #2:

second commit

# This is the commit message #3:

third commit

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
#
# Date:      Mon Apr 20 14:42:26 2020 +0900
#
# interactive rebase in progress; onto db078da
# Last commands done (3 commands done):
#    squash 0118d46 second commit
```

In this screen, Git will Squash via Rebase, so Git asks you about the commit messages. Git shows all commit messages on one screen. Press `i` button, and then modify it like below. (You should modify it on your situation.)

```bash
# This is a combination of 3 commits.
# This is the 1st commit message:

Fix Squash Task

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
```

After finishing to write the message, press `ESC` button on the keyboard and insert `:wq` to save it.

Again, execute `git log --pretty=oneline` command to check the history,

```bash
099e6f606b3a46b98f0233d558eb07c143a3ec01 (HEAD -> squash-test) Fix Squash Task
db078dae819cfed46bc6e6ef8c962648f97c22da (origin/master, origin/develop, master, develop) Merge pull request #1 from dev-yakuza/rebase-and-squash
```

You can see one commit history like above unlike before Rebase. Also, you can see the message that we've written on Squash.

{% include in-feed-ads.html %}

### Git Push

Now, we need to `Push` this commit to Remote Repository.

```bash
git push origin squash-test
```

If you pushed the commits before, you should use `-f` option like below to push forcely.

```bash
git push origin squash-test -f
```

## Completed

We've seen how to compress many commits to one commit via Git Squash. Actually, we've worked by Git Rebase to squash. Here is the command list on thie blog post.

```bash
git log --pretty=oneline
git rebase -i [Commit Number]
# Select to pick and squash
# Change commit log
git push origin [Branch] -f
# git push origin [Branch]
```

Let's make pretty commit logs via Squash!
