---
layout: 'post'
permalink: '/git/create-stage/'
paginate_path: '/git/:num/create-stage/'
lang: 'ko'
categories: 'git'
comments: true

title: '버전(변경이력) 생성'
description: 'git의 저장소(Repository)로 버전 관리를 하기 위해 버전(변경 이력)을 생성하는 방법에 대해서 알아봅니다.'
image: '/assets/images/category/git/create-stage.jpg'
---

## 개요
이전 블로그([저장소(Repository) 생성]({{site.url}}/{{page.categories}}/create-stage/){:target="_blank"})에서 git의 저장소(Repository)를 생성하는 방법에 대해서 살펴보았습니다. 이번에는 생성된 git 저장소(Repository)에 버전 관리를 위해 버전(변경 이력)을 생성하는 방법에 대해서 알아봅시다.

## 파일 추가
git 저장소(Repository)가 존재하는 폴더(```temp_test_git```)에 버전 관리를 하고 싶은 파일을 복사하거나 새롭게 만듭니다.

우리는 테스트를 위해 ```temp_test_git``` 폴더에 ```test text```라고 기록한 ```test.txt``` 파일을 생성하였습니다.

## git status
git 저장소(Repository)의 현재 상태를 확인하기 위해 아래에 ```git status``` 명령어를 실행시킵니다.

```bash
git status
```

위와 같이 ```git status``` 명령어를 실행하면 아래와 같은 화면을 볼 수 있습니다.

![git status](/assets/images/category/git/create-stage/git-status.png)

- On branch master: 현재 해당하는 브랜치(branch)는 마스터(master)입니다. git 브랜치(branch)에 관해서는 이후에 다른 블로그 포스트에서 설명합니다.
- No commits yet: 아직 커밋(commit)을 하지 않은 상태입니다. 커밋(commit)은 버전(변경 이력)을 의미합니다. 아직 버전(변경 이력)을 만들지 않은 상태를 의미합니다.
- Untracked files: git가 버전(변경 이력) 관리를 하고 있지 않는 파일 리스트입니다.

우리는 아직 git에게 ```test.txt``` 파일을 버전(변경 이력)으로 관리하라고 알려주지 않았습니다. 그렇기 때문에 ```Untracked files```에 우리가 만든 ```test.txt``` 파일이 존재하는 것을 확인할 수 있습니다.

## git add
우리는 새로 만든 파일(```test.txt```)을 git에게 버전(변경 이력) 관리 대상임을 알려줘야 합니다. ```git add``` 명령어로 git에게 ```test.txt``` 파일은 버전(변경 이력) 관리 대상임을 알려 줍니다.

```bash
# add single file
git add test.txt

# add multiple files
# git add test.txt test2.txt test3.txt

# add all files
# git add .
```

아래와 같이 ```git status``` 명령어로 git이 새롭게 추가된 파일을 잘 인식하는지 확인합니다.

```bash
git status
```

아래와 같이 ```git status``` 명령어를 실행하면 아까와는 다른 화면을 볼 수 있습니다.

![git status after executing git add command](/assets/images/category/git/create-stage/git-status-after-add.png)

- Changes to be committed: git이 다음에 버전(변경 이력) 관리를 하기 위한 파일 리스트입니다. 우리는 파일을 새롭게 추가했기 때문에 ```new file```에 ```text.txt```가 추가된 것을 볼 수 있습니다.

이렇게 ```git add```를 통해 파일을 추가하는 과정이 있는 이유는 이번 버전(변경 이력)에 추가하고 싶지 않은 파일들이 실제 프로그램을 작성할 때 존재하기 때문입니다. 예를 들어 빌드된 결과물, DB정보, ID/PW가 저장된 설정 파일이나 임시로 로그를 표시하기 위해 작성한 코드(console.log / print)가 포함되어 있어 버전(변경 이력)과 무관한 내용을 구별하기 위해 사용합니다.

## git commit
우리는 git에게 버전(변경 이력)에 추가하고 싶은 파일을 ```git add``` 명령어로 알려줬습니다. 하지만 실제 버전(변경 이력) 관리는 이뤄지지 않았습니다. 단지 git에게 새로운 파일이 있음을 알려준 것입니다. 이제 실제 버전(변경 이력) 관리를 위해 ```git commit```을 이용하여 버전(변경 이력)을 생성합니다.

```bash
git commit
```

이렇게 ```git commit```명령어를 실행하면 버전(변경 이력)을 생성할 수 있는 화면이 실행됩니다.

![git commit](/assets/images/category/git/create-stage/git-commit.png)

이 화면은 ```vim```이라는 문서 편집 툴이 실행된 화면입니다. 문서를 편집하기 위해 키보드에서 ```i```(insert)를 입력하고 이 변경 이력에 내용이 무엇인지 작성합니다.

![git commit with message](/assets/images/category/git/create-stage/git-commit-with-message.png)

작성이 완료되면 키보드의 ```esc``` 버튼을 누르고 ```:wq```(write-quit)을 입력하여 변경 이력을 작성합니다.

![git completed commit](/assets/images/category/git/create-stage/git-complete-commit.png)

변경 이력 작성이 완료되면 위와 같은 메세지를 볼 수 있습니다.

## git log
버전(변경 이력)이 잘 생성되었는지 확인하기 위해 ```git log```명령어를 실행시킵니다.

```bash
git log
```

위와 같이 ```git log```를 실행하면 현재 작성한 버전(변경 이력)을 확인할 수 있습니다.

![git log](/assets/images/category/git/create-stage/git-log.png)

- Author: 버전(변경 이력) 작성자 및 작성자 이메일(git config로 등록한 사용자명과 이메일)
- Date: 버전(변경 이력)의 생성일자
- Date 하단에 ```git commit```을 사용하여 작성한 메세지를 확인할 수 있습니다.

## 파일 수정인 경우
파일을 수정한 경우도 위와 동일한 방식을 취합니다. 아래와 같이 ```git status``` 명령어로 현재 상태를 확인합니다.

```bash
git status
```

아직 아무 변경도 하지 않았기 때문에 변경 사항이 없다고 git이 알려줍니다.

![git status no change](/assets/images/category/git/create-stage/git-status-no-change.png)

이제 ```test.txt``` 파일의 내용을 ```test text```에서 ```test string```으로 수정한 후 ```git status```를 실행 시킵니다.

```bash
git status
```

이번에는 수정 사항이 있기 때문에 아래와 같은 화면을 볼 수 있습니다.

![git status with modification](/assets/images/category/git/create-stage/git-status-with-modification.png)

- modified: 수정된 파일을 나타냅니다.

이제 ```git add```를 통해 git에게 변경된 이력이 있음 알려줍니다. 다른 말로 버전(변경 이력)에 기록할 파일을 추가합니다.

```bash
git add test.txt
```

다시 ```git status```로 상태를 확인합니다.

![git status after commit](/assets/images/category/git/create-stage/git-status-after-commit.png)

아까와는 다르게 글자도 녹색으로 변경 되었으며 ```no changes added to commit (use "git add" and/or "git commit -a")``` 메세지도 없는 것을 확인 할 수 있습니다. git이 버전(변경 이력)에 ```test.txt``` 파일을 잘 추가하였음을 알 수 있습니다. ```git commit```을 이용하여 버전(변경 이력)을 생성합니다. 버전 메세지(변경 이력 메세지)에는 ```edit 'text' to 'string'```을 입력했습니다.

```bash
git commit
```

그리고 ```git log```를 사용하여 버전(변경 이력)이 잘 생성되었는지 확인합니다.

```bash
git log
```

![git log with new version](/assets/images/category/git/create-stage/git-log-with-new-version.png)

위와 같이 버전(변경 이력)이 잘 생성 된 것을 확인할 수 있습니다.

## 요약
버전(변경 이력)을 생성하는 방법에 대해서 알아봤습니다. 전체적으로 요약하면 아래와 같습니다.

1. 파일 추가 또는 수정
1. ```git status```로 추가 또는 변경된 파일 확인
1. ```git add```로 버전(변경 이력)에 추가하고 싶은 파일 등록
1. ```git status```로 버전(변경 이력)에 추가한 파일이 등록되었는지 확인
1. ```git commit```으로 버전(변경 이력)에 메세지를 추가하여 생성
1. ```git log```로 생성된 버전(변경 이력) 확인

위와 같은 방법으로 새로운 버전(변경 이력)을 생성하면 됩니다.