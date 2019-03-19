---
published: false
layout: 'post'
permalink: '/react-native/react-native-sqlite-storage/'
paginate_path: '/react-native/:num/react-native-sqlite-storage/'
lang: 'ko'
categories: 'react-native'
comments: true

title: 'RN(Reacct Native)에서 sqlite 사용하기'
description: 'RN(React Native) 프로젝트에서 sqlite 데이터베이스를 사용하는 방법에 대해서 알아봅시다.'
image: '/assets/images/category/react-native/2019/react-native-sqlite-storage/background.jpg'
---


## 개요
RN(React Native)로 앱을 개발하다보면 로컬 데이터베이스(DB)를 사용할 경우가 있습니다. 예를 들어 제가 개발한 단어장 앱([일단공부(일본어 단어 공부) - JLPT 단어 공부](){})은 단어를 서버에서 받아오는게 아니라 앱과 함께 배포하고 있습니다. 이 블로그에서는 이렇게 앱내에서 데이터베이스(DB)를 사용하는 방법에 대해서 알아보겠습니다.

여기에서 소개할 DB는 sqlite이며, RN(React Native)에서 [react-native-sqlite-storage](https://github.com/andpor/react-native-sqlite-storage){:rel="nofollow noreferrer" target="_blank"} 라이브러리로 DB를 사용하는 방법에 대해서 살펴보겠습니다.

- react-native-sqlite-storage 공식 홈페이지: [https://github.com/andpor/react-native-sqlite-storage](https://github.com/andpor/react-native-sqlite-storage){:rel="nofollow noreferrer" target="_blank"}


## DB 준비
RN(React Native)에서 사용할 DB를 준비합니다. 여기서는 샘플 DB를 제작하는 방법을 설명합니다. 이미 Sqlite DB를 가지고 계신분들은 이 섹션을 건너뛰셔도 됩니다.

아래는 제가 사용하고 있는 sqlite 툴의 링크입니다. 링크를 눌러 OS에 맞는 툴을 다운로드합니다.

- sqlite 툴 다운로드: [https://sqlitebrowser.org/dl/](https://sqlitebrowser.org/dl/){:rel="nofollow noreferrer" target="_blank"}

다운로드 및 설치가 끝나면 툴을 실행합니다.

![RN(react-native) sqlite 툴](/assets/images/category/react-native/2019/react-native-sqlite-storage/sqlite-tool.png)

왼쪽 위에 `New Database`를 선택하여 새로운 `TestDB`라는 이름으로 데이터베이스를 생성합니다.

![RN(react-native) sqlite 툴 - DB 생성](/assets/images/category/react-native/2019/react-native-sqlite-storage/sqlite-tool-create-db.png)

아래와 같이 `test`라는 이름의 테이블을 생성하고 `id`, `name`, `age`, `email` 필드를 추가합니다.

![RN(react-native) sqlite 툴 - DB 테이블 생성](/assets/images/category/react-native/2019/react-native-sqlite-storage/sqlite-tool-create-db-table.png)

아래에 sql문으로 더미 데이터를 추가합니다.

```sql
INSERT INTO
	test
	(name, age, email)
VALUES
	("aaa",  20, "aaa@aaa.aaa"),
	("bbb",  25, "bbb@bbb.bbb"),
	("ccc",  30, "ccc@ccc.ccc")
```

![RN(react-native) sqlite 툴 - DB 데이터 추가](/assets/images/category/react-native/2019/react-native-sqlite-storage/sqlite-insert-data.png)

데이터가 잘 추가되었는지 아래에 sql문으로 확인합니다.

```sql
SELECT * FROM test
```

![RN(react-native) sqlite 툴 - DB 데이터 확인](/assets/images/category/react-native/2019/react-native-sqlite-storage/sqlite-check-data.png)

이제 데이터베이스가 준비되었습니다. RN(React Native)에서 사용해 봅시다.

## react-native-sqlite-storage 라이브러리 설치
sqlite를 사용하고 싶은 RN(React Native) 프로젝트에서 아래에 명령어로 react-native-sqlite-storage를 설치합니다.

```bash
npm install --save react-native-sqlite-storage
```

그리고 아래에 명령어를 통해 설치한 react-native-sqlite-storage를 RN(React Native) 프로젝트와 연결합니다.

```bash
react-native link react-native-sqlite-storage
```

