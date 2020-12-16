---
layout: 'post'
permalink: '/git/git-squash/'
paginate_path: '/git/:num/git-squash/'
lang: 'ko'
categories: 'git'
comments: true

title: 'Git squash로 여러 커밋을 하나로 만들기'
description: Git squash를 사용하여 여러 커밋을 하나의 커밋으로 만드는 방법에 대해서 알아봅니다.
image: '/assets/images/category/git/2020/git-squash/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [Git Squash](#git-squash)
  - [Git Log](#git-log)
  - [Git Rebase](#git-rebase)
  - [Git Push](#git-push)
- [완료](#완료)

</div>

## 개요

오픈 소스에 기여(Commit)하거나, 회사가 소스코드를 수정할 때, 보통 하나의 이슈(Issue)를 만들고, 그 이슈를 기준으로 브랜치를 만듭니다. 그리고 이렇게 만든 브랜치에 수정한 내용을 커밋(Commit)합니다. 하지만 보통 커밋 한번에 모든 것을 수정할 수 없을 때가 있습니다. 프론트 사이드 소스 코드 커밋, 서버 사이드 소스 코드 커밋, 테스트 코드 커밋, 코드 리뷰 대응 커밋 등, 한 이슈를 수정하기 위해 여러 커밋이 발생하게 됩니다.

이렇게 생성된 여러 커밋을 그냥 병합(Merge)해도 되지만, 오픈 소스나, 여러 사람이 같이 작업하는 회사 소스코드인 경우, 커밋 이력이 많아지고 복잡해져서, 커밋 이력을 추적하는 것이 힘들어지게 됩니다.

이것을 방지하기 위해, 이번 블로그 포스트에서는 Git의 `Squash` 기능에 대해서 알아봅니다.

## Git Squash

Git Squash는 여러번 커밋한 이력을 하나의 커밋 이력으로 만드는데 사용합니다.

### Git Log

우선 아래에 명령어를 사용하여 커밋한 이력을 확인합니다.

```bash
git log --pretty=oneline
```

그러면 아래와 같은 결과를 볼 수 있습니다.

```bash
1f199b7353e40e3134572c9986837b1b4bfebd13 (HEAD -> squash-test) third commit
0118d468a770c2340bf6d4d47f10984c58ea382b second commit
b91e257ce42d5f501c7bc8242a0580b3c05ef462 first commit
db078dae819cfed46bc6e6ef8c962648f97c22da (origin/master, origin/develop, master, develop) Merge pull request #1 from dev-yakuza/rebase-and-squash
c6bd068ec0ea39ef98e135218dc19375e5d63a68 (origin/rebase-and-squash, rebase-and-squash) add rebase-and-squash
2d33cf05e6352b2fa7e8574d170032b34e3a8959 change master
405d0d71ed50429a169ece18cf984dfd64c088a9 add proejct
```

저는 현재 Master 브랜치에서 `squash-test` 브랜치를 만들고 `first commit`, `second commit`, `third commit`의 커밋을 한 상태입니다.

```bash
1f199b7353e40e3134572c9986837b1b4bfebd13 (HEAD -> squash-test) third commit
0118d468a770c2340bf6d4d47f10984c58ea382b second commit
b91e257ce42d5f501c7bc8242a0580b3c05ef462 first commit

db078dae819cfed46bc6e6ef8c962648f97c22da (origin/master, origin/develop, master, develop) Merge pull request #1 from dev-yakuza/rebase-and-squash
```

{% include in-feed-ads.html %}

### Git Rebase

이제, Git의 Squash 기능으로 `first commit`, `second commit`, `third commit` 커밋을 하나의 커밋으로 만들어 보겠습니다. Squash 기능을 사용하려면 Git의 `Rebase`를 사용해야 합니다.

일단, Git의 로그를 다시 한번 확인하고,

```bash
1f199b7353e40e3134572c9986837b1b4bfebd13 (HEAD -> squash-test) third commit
0118d468a770c2340bf6d4d47f10984c58ea382b second commit
b91e257ce42d5f501c7bc8242a0580b3c05ef462 first commit

# We will rebase on here!!!!!!!!
db078dae819cfed46bc6e6ef8c962648f97c22da (origin/master, origin/develop, master, develop) Merge pull request #1 from dev-yakuza/rebase-and-squash
```

3개의 커밋을 하나의 커밋으로 만들 예정이므로 3개의 커밋을 하기 이전인 `db078dae819cfed46bc6e6ef8c962648f97c22da`으로 Rebase를 합니다.

Squash를 사용하기 위해 아래에 Git의 Rebase 명령어를 사용하여 Rebase합니다.

```bash
git rebase -i db078dae819cfed46bc6e6ef8c962648f97c22da
```

여기서 `-i` 옵션을 사용한 것에 주목해야 합니다. `-i` 옵션을 주었기 때문에, 보통의 Rebase와 다르게 아래와 같은 결과를 얻을 수 있습니다.

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

이 화면은 Rebase를 통해 커밋 이전의 상태로 되돌아 가려고 하는데, 현재와 과거 사이에 남아 있는 커밋을 어떻게 처리하겠냐고, Git이 친절하게 물어봐 주는 화면입니다. 하단의 사용 가능한 Command도 나열되어 있습니다. 우리는 여기서 `s, squash`를 사용할 예정입니다.

```bash
# s, squash <commit> = use commit, but meld into previous commit
```

이번 커밋에는 `first commit`을 남겨두고 `second commit`과 `third commit`을 Squash하도록 하겠습니다. 키보드의 `i` 버튼을 누르고 수정 가능한 상태로 변경한 다음, 아래와 같이 수정합니다.

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

그리고 키보드의 `ESC` 버튼을 누르고 `:wq`를 입력한 다음 `Enter` 키를 눌러 변경한 내용을 저장합니다. 변경이 완료되면 아래와 같은 화면을 볼 수 있습니다

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

이 화면은 Git이 Rebase를 통해 Squash를 할 예정인데, 이전에 작성한 커밋 메시지는 어떻게 할지 물어보는 화면입니다. Git이 모든 메시지를 한 화면에 보여주고 있습니다. 역시 키보드의 `i` 버튼을 누른 다음, 아래와 같이 수정합니다. (메시지는 여러분의 환경에 맞게 변경하시기 바랍니다.)

```bash
# This is a combination of 3 commits.
# This is the 1st commit message:

Fix Squash Task

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
```

메시지 작성이 완료되었다면, 키보드의 `ESC` 버튼을 누르고 `:wq`를 입력하여 저장해 줍니다.

다시 `git log --pretty=oneline`으로 커밋 이력을 확인하면,

```bash
099e6f606b3a46b98f0233d558eb07c143a3ec01 (HEAD -> squash-test) Fix Squash Task
db078dae819cfed46bc6e6ef8c962648f97c22da (origin/master, origin/develop, master, develop) Merge pull request #1 from dev-yakuza/rebase-and-squash
```

Rebase 이전과는 다르게 커밋이 하나만 나오는 것을 확인할 수 있습니다. 또한 메시지 내용도 우리가 Squash할 때, 작성한 메시지가 나오는 것을 확인할 수 있습니다.

{% include in-feed-ads.html %}

### Git Push

이제 이렇게 하나로 만든 커밋을 원격 저장소(Remote Repository)에 `Push`합니다.

```bash
git push origin squash-test
```

이미 이전에 커밋한 내용을 원격 저장소에 Push한적이 있다면, 아래와 같이 `-f`을 통해 강제로 교체하도록 합니다.

```bash
git push origin squash-test -f
```

## 완료

이것으로 Git의 Squash를 사용하여 여러 커밋 이력을 하나의 커밋으로 변경하는 방법에 대해서 알아보았습니다. 정확히 말하면 Git의 Rebase를 통해 Squash를 수행했다고 해야할 거 같네요. 이번 블로그 포스트의 사용한 명령어를 정리해 보았습니다.

```bash
git log --pretty=oneline
git rebase -i [Commit Number]
# Select to pick and squash
# Change commit log
git push origin [Branch] -f
# git push origin [Branch]
```

여러분도 Squash를 통해 예쁜 커밋 이력을 남겨보세요!
