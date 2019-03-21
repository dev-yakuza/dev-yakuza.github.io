---
layout: 'post'
permalink: '/react-native/react-native-sqlite-storage/'
paginate_path: '/react-native/:num/react-native-sqlite-storage/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'How to use sqlite in RN(Reacct Native)'
description: let's see how to use sqlite database in RN(React Native).
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

## Install react-native-sqlite-storage library
execute the command below on the project that you want to use the sqlite.

```bash
npm install --save react-native-sqlite-storage
# for typescript
npm install --save-dev @types/react-native-sqlite-storage
```

and then, execute the command below to bind react-native-sqlite-storage to RN(React Native) project.

```bash
react-native link react-native-sqlite-storage
```

if you use pod, I recommend you to bind it manually. you can see the details on the official site.

- react-native-sqlite-storage official site: [https://github.com/andpor/react-native-sqlite-storage](https://github.com/andpor/react-native-sqlite-storage#step-1a-if-rnpm-link-does-not-work-for-you-you-can-try-manually-linking-according-to-the-instructions-below){:rel="nofollow noreferrer" target="_blank"}

as a result, your project settings to use react-native-sqlite-storage should be like below.

![react-native-sqlite-storage setting completed](/assets/images/category/react-native/2019/react-native-sqlite-storage/setting.png)


## Add DB
we need to add DB which we've made above to each OS.

### iOS
if you want to use sqlite DB that you've made, you should follow the process below.

1. create `ios/[project name]/www` folder and copy the DB on it.
  ![react-native-sqlite-storage create www folder and copy db file](/assets/images/category/react-native/2019/react-native-sqlite-storage/www_folder.png)

1. execute `[project name].xcodeproj` or `[project name].xcworkspace` file to start xcode

1. right-click `[project name]` > `[project name]` folder on the left top and click `Add Files to [project name]`.
  ![react-native-sqlite-storage add db file on xcode](/assets/images/category/react-native/2019/react-native-sqlite-storage/add_file_for_ios.png)

1. when you see the file selection dialog, click `www` folder that we've made on `(1)` section. select `Create folder references` and click `Add` to add it.
  ![react-native-sqlite-storage add DB file to proejct](/assets/images/category/react-native/2019/react-native-sqlite-storage/create_folder_references.png)

### Android
if you want to use sqlite DB that you've made, you should follow the process below.

1. open and modify `android/settings.gradle` file like below.
  ```js
  rootProject.name = 'react_native_sqlite_storage_exercise'
  ...
  include ':react-native-sqlite-storage'
  project(':react-native-sqlite-storage').projectDir = new File(rootProject.projectDir, '../node_modules/react-native-sqlite-storage/src/android')
  ...
  include ':app'
  ```

1. oepn and modify `android/app/build.gradle` file like below.
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

1. open and modify ```MainApplication.java``` file like below.
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

1. create `android/app/src/main/assets/www` folder and copy the sqlite DB which you've made
  ![react-native-sqlite-storage add db file on android](/assets/images/category/react-native/2019/react-native-sqlite-storage/www_folder_android.png)


## How to use DB
when you finished the configuration each OS, you can use sqlite DB by adding the source like below.

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

## Completed
we saw how to use react-native-sqlite-storage library to use the sqlite DB. now, if you want to deploy the app with DB, you can use the sqlite database. let's challenge!

if you want to know full example about how to use react-native-sqlite-storage, please check the git repository below that I've made when I wrote this blog.

- git repository: [react_native_sqlite_storage_exercise](){:rel="nofollow noreferrer" target="_blank"}