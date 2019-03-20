---
layout: 'post'
permalink: '/react-native/react-native-sqlite-storage/'
paginate_path: '/react-native/:num/react-native-sqlite-storage/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'How to use sqlite in RN(Reacct Native)'
description: 'RN(React Native) 프로젝트에서 sqlite 데이터베이스를 사용하는 방법에 대해서 알아봅시다.'
image: '/assets/images/category/react-native/2019/react-native-sqlite-storage/background.jpg'
---

## Outline
when we develop apps with RN(React Native), sometimes we need to use local database. for example, the the Japanese words app which I developed for Korean([일단공부(일본어 단어 공부) - JLPT 단어 공부](https://dev-yakuza.github.io/app/blaboo/en/){:target="_blank"}) is not to download the words, just use the local database. in this blog, I will introduce how to use the database in the app.

in here, I will introduce sqlite DB, and how to use it by `react-native-sqlite-storage` library in RN(React Native).

- react-native-sqlite-storage official site: [https://github.com/andpor/react-native-sqlite-storage](https://github.com/andpor/react-native-sqlite-storage){:rel="nofollow noreferrer" target="_blank"}


## Prepare DB
let's prepare the DB to use in RN(React Native). in here, we will make the sample database. if you have the sqlite database, please skip this section.

the link below is the sqlite tool which I use. click the link and download for your OS.

- download sqlite tool: [https://sqlitebrowser.org/dl/](https://sqlitebrowser.org/dl/){:rel="nofollow noreferrer" target="_blank"}

after downloading and installing, execute the tool.

![RN(react-native) sqlite tool](/assets/images/category/react-native/2019/react-native-sqlite-storage/sqlite-tool.png)

click `New Database` on the left top, and create the database named `TestDB`.

![RN(react-native) sqlite tool - create DB](/assets/images/category/react-native/2019/react-native-sqlite-storage/sqlite-tool-create-db.png)

create `test` table like below, and add `id`, `name`, `age`, `email` fields.

![RN(react-native) sqlite tool - create DB table](/assets/images/category/react-native/2019/react-native-sqlite-storage/sqlite-tool-create-db-table.png)

execute the sql below to add dummy data.

```sql
INSERT INTO
	test
	(name, age, email)
VALUES
	("aaa",  20, "aaa@aaa.aaa"),
	("bbb",  25, "bbb@bbb.bbb"),
	("ccc",  30, "ccc@ccc.ccc")
```

![RN(react-native) sqlite tool - add data to DB ](/assets/images/category/react-native/2019/react-native-sqlite-storage/sqlite-insert-data.png)

execute the sql below to check data is inserted well.

```sql
SELECT * FROM test
```

![RN(react-native) sqlite tool - check data in DB](/assets/images/category/react-native/2019/react-native-sqlite-storage/sqlite-check-data.png)

now, we prepared the database. let's use it on RN(React Native).

## react-native-sqlite-storage 라이브러리 설치
sqlite를 사용하고 싶은 RN(React Native) 프로젝트에서 아래에 명령어로 react-native-sqlite-storage를 설치합니다.

```bash
npm install --save react-native-sqlite-storage
# for typescript
npm install --save-dev @types/react-native-sqlite-storage
```

그리고 아래에 명령어를 통해 설치한 react-native-sqlite-storage를 RN(React Native) 프로젝트와 연결합니다.

```bash
react-native link react-native-sqlite-storage
```

pod을 이용하시는 분들은 수동으로 라이브러리를 연결하는 걸 권장합니다. 수동으로 라이브러리를 연결하는 방법은 공식 홈페이지를 참고해 주세요.

- react-native-sqlite-storage 공식 홈페이지: [https://github.com/andpor/react-native-sqlite-storage](https://github.com/andpor/react-native-sqlite-storage#step-1a-if-rnpm-link-does-not-work-for-you-you-can-try-manually-linking-according-to-the-instructions-below){:rel="nofollow noreferrer" target="_blank"}

결과적으로 아래와 같이 설정이 되면 react-native-sqlite-storage 라이브러리를 사용할 수 있습니다.

![react-native-sqlite-storage 설정 완료](/assets/images/category/react-native/2019/react-native-sqlite-storage/setting.png)


## DB 추가
위에서 작성한 DB를 앱안에 사용할 수 있도록 각 OS에 맞게 DB를 추가합니다.

### iOS
iOS에서 미리 만든 sqlite DB를 사용하기 위해서는 아래와 같은 절차를 따라야 합니다.

1. `ios/[project name]/www` 폴더를 만들고 미리 생성한 sqlite DB를 복사합니다.

![react-native-sqlite-storage www 폴더 생성 및 파일 복사](/assets/images/category/react-native/2019/react-native-sqlite-storage/www_folder.png)

1. `[project name].xcodeproj` 또는 `[project name].xcworkspace` 파일을 실행하여 xcode를 실행합니다.

1. 왼쪽 상단에 `[project name]` 하단의 `[project name]` 폴더를 우클릭하고, `Add Files to [project name]`을 선택합니다.

![react-native-sqlite-storage xcode에 DB 파일 추가](/assets/images/category/react-native/2019/react-native-sqlite-storage/add_file_to.png)

1. 파일 선택 대화창이 나오면 `(1)`에서 만든 `www` 폴더를 선택하고 `Create folder references`를 선택한 후 `Add` 버튼을 눌러 추가합니다.

![react-native-sqlite-storage xcode에 DB 파일 추가](/assets/images/category/react-native/2019/react-native-sqlite-storage/create_folder_references.png)

### 안드로이드
안드로이드에서 미리 만든 sqlite DB를 사용하기 위해서는 아래와 같은 절차를 따라야 합니다.

1. `android/settings.gradle` 파일을 열고 아래와 같이 수정합니다.(react-native link react-native-sqlite-storage로 벌써 수정이 되어있을 수 있음)

```js
rootProject.name = 'react_native_sqlite_storage_exercise'
...
include ':react-native-sqlite-storage'
project(':react-native-sqlite-storage').projectDir = new File(rootProject.projectDir, '../node_modules/react-native-sqlite-storage/src/android')
...
include ':app'
```

1. `android/app/build.gradle` 파일을 열고 아래와 같이 수정합니다.(react-native link react-native-sqlite-storage로 벌써 수정이 되어있을 수 있음)

```js
...
dependencies {
    implementation fileTree(dir: "libs", include: ["*.jar"])
    implementation "com.android.support:appcompat-v7:${rootProject.ext.supportLibVersion}"
    implementation "com.facebook.react:react-native:+"  // From node_modules
	...
    implementation project(':react-native-sqlite-storage')
}
...
```

1. ```MainApplication.java``` 파일을 열고 아래와 같이 수정합니다.(react-native link react-native-sqlite-storage로 벌써 수정이 되어있을 수 있음)

```java
...
import org.pgsqlite.SQLitePluginPackage;
...
public class MainApplication extends Application implements ReactApplication {
	...

	...
	@Override
	protected List<ReactPackage> getPackages() {
		return Arrays.<ReactPackage>asList(
			...
			new SQLitePluginPackage(),
			...
			new MainReactPackage()
		);
	}
}
```

1. `android/app/src/main/assets//www` 폴더를 만들고 미리 생성한 sqlite DB를 복사합니다.

![react-native-sqlite-storage android에 DB 파일 추가](/assets/images/category/react-native/2019/react-native-sqlite-storage/www_folder_android.png)


## DB 사용하기
각 OS 설정이 끝났다면, 이제 sqlite DB를 사용하기 위해 아래와 같이 소스를 추가합니다.

```js
import * as React from 'react';
import Styled from 'styled-components/native';
import SQLite from 'react-native-sqlite-storage';

const Container = Styled.View`
  flex: 1;
  justify-content: center;
  align-items: center;
  background-color: #F5FCFF;
`;
const UserContainer = Styled.View`
  flex-direction: row;
`;
const UserInfo = Styled.Text`
  padding: 8px;
`;

interface Props {}
interface State {
  db: SQLite.SQLiteDatabase;
  users: Array<IUser>;
}

export default class App extends React.Component<Props, State> {
  constructor(props: Props) {
    super(props);

    const db = SQLite.openDatabase(
      {
        name: 'TestDB.db',
        location: 'default',
        createFromLocation: '~www/TestDB.db',
      },
      () => {},
      error => {
        console.log(error);
      }
    );

    this.state = {
      db,
      users: [],
    };
  }

  render() {
    const { users } = this.state;
    return (
      <Container>
        {users.map((user: IUser, index: number) => (
          <UserContainer key={`user-info${index}`}>
            <UserInfo>{user.id}</UserInfo>
            <UserInfo>{user.name}</UserInfo>
            <UserInfo>{user.age}</UserInfo>
            <UserInfo>{user.email}</UserInfo>
          </UserContainer>
        ))}
      </Container>
    );
  }

  componentDidMount() {
    const { db } = this.state;

    db.transaction(tx => {
      tx.executeSql('SELECT * FROM test;', [], (tx, results) => {
        const rows = results.rows;
        let users = [];

        for (let i = 0; i < rows.length; i++) {
          users.push({
            ...rows.item(i),
          });
        }

        this.setState({ users });
      });
    });
  }

  componentWillUnmount() {
    const { db } = this.state;

    db.close();
  }
}
```

## 완료
이로써 react-native-sqlite-storage 라이브러리를 사용하여 sqlite DB를 사용하는 방법에 대해서 알아보았습니다. 여러분도 DB를 함께 배포하는 앱을 제작할 경우 sqlite를 사용하는 것을 고려해 보시는 건 어떨까요? 아래는 위에 내용을 이용하여 만든 git 저장소(repository)입니다. 소스가 궁금하신 분들은 아래에 링크를 참고하세요

- git 저장소(repository): [react_native_sqlite_storage_exercise](){:rel="nofollow noreferrer" target="_blank"}