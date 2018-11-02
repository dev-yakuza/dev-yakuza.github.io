---
layout: 'post'
permalink: '/git/create-stage/'
paginate_path: '/git/:num/create-stage/'
lang: 'en'
categories: 'git'
comments: true

title: 'create version(editing history)'
description: 'we should create the version(editing history) to manage source code on git repository. we introduce how to create version(editing history).'
image: '/assets/images/category/git/create-stage.jpg'
---

## outline
we introduced how to create git repository in the previous blog post.([create Repository]({{site.url}}/{{page.categories}}/create-stage/){:target="_blank"}) in here, we will show how to create version(editing history) to use git version control.

## add new file
copy or create new file on the folder(```temp_test_git```) which has git repository.

we created ```text.txt``` file written ```test text``` in ```temp_test_git``` folder for testing.

## git status
execute ```git status``` command for checking current status of git repository.

```bash
git status
```

you can see below screen after executing ```git status``` command.

![git status](/assets/images/category/git/create-stage/git-status.png)

- On branch master: current Branch is Master branch. we will introduce git Branch at another blog post.
- No commits yet: our status is before committing. commit means version(editing history). No commits yet means we didn't create version(editing history).
- Untracked files: the list of not managing files by git.

we didn't mention it to git that we want to manage ```test.txt``` file to version(editing history). so we can see ```test.txt``` file with ```Untracked files```.

## git add
we need to tell git that new file(```test.txt```) is version(editing history) management target. execute ```git add``` command for helping git recognize new file(```test.txt```) is version(editing history) management target.

```bash
# add single file
git add test.txt

# add multiple files
# git add test.txt test2.txt test3.txt

# add all files
# git add .
```

execute ```git status``` command for checking that git recognized new file well.

```bash
git status
```

after executing ```git status``` command, you can see different screen before.

![git status after executing git add command](/assets/images/category/git/create-stage/git-status-after-add.png)

- Changes to be committed: next version(editing history) file list. we added new file so we can see ```text.txt``` with ```new file```.


the reason of existing adding file process by ```git add``` command is that files is existed that we don't want to include in version(editing history) when we develop real products. for example, it is used to distinguish between the version (history of change) and irrelevant contents like result files after building, DB information files, ID/PW configuration files or temporally edited files for logging with log code(console.log / print, etc)

## git commit
we informed git with ```git add``` command which file we want to add to the version(editing history). but version(editing history) is not managed yet. just we told git that we have new files. now, we create version(editing history) by executing ```git commit```.

```bash
git commit
```

when you execute ```git commit``` command, you can see the create version(editing history) screen.

![git commit](/assets/images/category/git/create-stage/git-commit.png)

this screen is ```vim``` that is a text editor. we need to push ```i```(insert) for editing the document. and type messages about changes.

![git commit with message](/assets/images/category/git/create-stage/git-commit-with-message.png)

when you finish to write messages, push ```esc``` button on the keyboard and type ```:wq```(write-quit) and pusy ```enter``` button for saving.

![git completed commit](/assets/images/category/git/create-stage/git-complete-commit.png)

you can see above messages when you finish to write change history.

## git log
execute ```git log``` to check version(editing history) created well.

```bash
git log
```

after executing ```git log```, you can see current version(editing history) you wrote.

![git log](/assets/images/category/git/create-stage/git-log.png)

- Author: version(editing history) creator's name and email(we registered before with ```git config``` command.)
- Date: version(editing history) create date.
- you can see messages you wrote when you executed ```git commit``` command under the Date section.

## if modify files
if files are modified, use the same process as above. execute ```git status``` command to check current status like below.

```bash
git status
```

git tells us there are no changes because we did not do anything.

![git status no change](/assets/images/category/git/create-stage/git-status-no-change.png)

now we change ```test text``` to ```test string``` in ```test.txt``` file and execute ```git status``` again.

```bash
git status
```

we have changed the file so we can see different screen before

![git status with modification](/assets/images/category/git/create-stage/git-status-with-modification.png)

- modified: modified file list.

tell git that we have change history with ```git add``` command. in other words, add the file to version(editing history).

```bash
git add test.txt
```

execute ```git status``` again to check the status.

![git status after commit](/assets/images/category/git/create-stage/git-status-after-commit.png)

we can see differences that text color was changed green and ```no changes added to commit (use "git add" and/or "git commit -a")``` message was alos gone. now we can know ```test.txt``` file added to git version(editing history) well. create version(editing history) to use ```git commit``` command. write ```edit 'text' to 'string'``` to version message(editing history message).

```bash
git commit
```

and then execute ```git log``` to check version(editing history) created well.

```bash
git log
```

![git log with new version](/assets/images/category/git/create-stage/git-log-with-new-version.png)

we can see version(editing history) created well as above.

## summary
we saw about how to create version(editing history). the summary is as below.

1. cretae or edit files.
1. check created or added files with ```git status``` command.
1. execute ```git add``` command to add files to version(editing history).
1. check registered files well with ```git status``` command.
1. create version(editing history) with messages by ```git commit``` command.
1. check created version(editing history) with ```git log``` command.

we can make new version(editing history) as above.