---
layout: 'post'
permalink: '/react-native/react-native-sqlite-storage/'
paginate_path: '/react-native/:num/react-native-sqlite-storage/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'RN(Reacct Native)でsqliteを使う方法'
description: 'RN(React Native)プロジェクトでsqliteデータベースを使う方法について説明します。'
image: '/assets/images/category/react-native/2019/react-native-sqlite-storage/background.jpg'
---

## 概要
RN(React Native)でアプリを開発する時、ローカルデータベース(DB)を使う場合があります。例えば、私が開発した韓国人向けの日本語単語勉強アプリ([일단공부(일본어 단어 공부) - JLPT 단어 공부](https://dev-yakuza.github.io/app/blaboo/en/){:target="_blank"})は単語をサーバから貰うじゃなく、アプリと一緒に配布してます。このブログではこのようにアプリ内でデータベース(DB)を使う方法について説明します。

ここで紹介するDBはsqliteです。RN(React Native)で`react-native-sqlite-storage`ライブラリでDBを使う方法について説明します。

- react-native-sqlite-storage公式サイト: [https://github.com/andpor/react-native-sqlite-storage](https://github.com/andpor/react-native-sqlite-storage){:rel="nofollow noreferrer" target="_blank"}


## DB準備
RN(React Native)で使うDBを準備します。ここにはサンプルDBを作成する方法も説明します。すでにSqlite DBを持っている方はこのセクションをスキップして構いません。

下記は私が使ってるsqliteツールのリンクです。リンクを押して自分のOSに合うツールをダウンロードします。

- sqliteツールダウンロード: [https://sqlitebrowser.org/dl/](https://sqlitebrowser.org/dl/){:rel="nofollow noreferrer" target="_blank"}

ダウンロードやインストールが終わったらツールを実行します。

![RN(react-native) sqliteツール](/assets/images/category/react-native/2019/react-native-sqlite-storage/sqlite-tool.png)

左上の`New Database`を選択して新しい`TestDB`と言う名前のデータベースを生成します。

![RN(react-native) sqliteツール - DB生成](/assets/images/category/react-native/2019/react-native-sqlite-storage/sqlite-tool-create-db.png)

下記のように`test`と言う名前でテーブルを生成して`id`, `name`, `age`, `email`フィルドを追加します。

![RN(react-native) sqliteツール - DBテーブル生成](/assets/images/category/react-native/2019/react-native-sqlite-storage/sqlite-tool-create-db-table.png)

下のsqlでダミーデータを追加します。

```sql
INSERT INTO
	test
	(name, age, email)
VALUES
	("aaa",  20, "aaa@aaa.aaa"),
	("bbb",  25, "bbb@bbb.bbb"),
	("ccc",  30, "ccc@ccc.ccc")
```

![RN(react-native) sqliteツール - DBデータ追加](/assets/images/category/react-native/2019/react-native-sqlite-storage/sqlite-insert-data.png)

データが上手く追加されたか下記のsqlで確認します。

```sql
SELECT * FROM test
```

![RN(react-native) sqliteツール - DBデータ確認](/assets/images/category/react-native/2019/react-native-sqlite-storage/sqlite-check-data.png)

データベースが用意できました。RN(React Native)で使ってみましょう。

## react-native-sqlite-storageライブラリインストール
sqliteを使いたいRN(React Native)プロジェクトで下記のコマンドでreact-native-sqlite-storageをインストールします。

```bash
npm install --save react-native-sqlite-storage
# for typescript
npm install --save-dev @types/react-native-sqlite-storage
```

そして、下記のコマンドでインストールしたreact-native-sqlite-storageをRN(React Native)プロジェクトと連結します。

```bash
react-native link react-native-sqlite-storage
```

podを使っている方は手動でライブラリを連結することをお勧めします。手動でライブラリを連携する方法は公式サイトを参考してください。

- react-native-sqlite-storage公式サイト: [https://github.com/andpor/react-native-sqlite-storage](https://github.com/andpor/react-native-sqlite-storage#step-1a-if-rnpm-link-does-not-work-for-you-you-can-try-manually-linking-according-to-the-instructions-below){:rel="nofollow noreferrer" target="_blank"}

結果的には下記のような設定ができたらreact-native-sqlite-storageライブラリを使えます。

![react-native-sqlite-storage設定完了](/assets/images/category/react-native/2019/react-native-sqlite-storage/setting.png)


## DB追加
上で作ったDBをアプリ中で使えように角OSに合わせてDBを追加します。

### iOS
iOSですでに作ったsqlite DBを使えたい時、下記の手続きをする必要があります。

1. `ios/[project name]/www`のフォルダを作って持っているsqlite DBをコピーします。

![react-native-sqlite-storage wwwフォルダ生成やファイルコピー](/assets/images/category/react-native/2019/react-native-sqlite-storage/www_folder.png)

1. `[project name].xcodeproj`または`[project name].xcworkspace`ファイルを実行してxcodeを実行します。

1. 左上の`[project name]`の下にある`[project name]`フォルダを右クリックして、`Add Files to [project name]`を選択します。

![react-native-sqlite-storage xcode에 DB 파일 추가](/assets/images/category/react-native/2019/react-native-sqlite-storage/add_file_to.png)

1. ファイル選択ダイアローグが表示されたら`(1)`で作った`www`フォルダを選択して`Create folder references`を選択した後`Add`のボタンを押して追加します。

![react-native-sqlite-storage xcode에 DB 파일 추가](/assets/images/category/react-native/2019/react-native-sqlite-storage/create_folder_references.png)

### アンドロイド
アンドロイドではすでに作ったsqlite DBを使うために下記の手続きをする必要があります。

1. `android/settings.gradle`ファイルを開いて下記のように修正します。(react-native link react-native-sqlite-storageですでに修正された可能性があります。)

```js
rootProject.name = 'react_native_sqlite_storage_exercise'
...
include ':react-native-sqlite-storage'
project(':react-native-sqlite-storage').projectDir = new File(rootProject.projectDir, '../node_modules/react-native-sqlite-storage/src/android')
...
include ':app'
```

1. `android/app/build.gradle`ファイルを開いて下記のように修正します。(react-native link react-native-sqlite-storageですでに修正された可能性があります。)

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

1. ```MainApplication.java```ファイルを開いて下記のように修正します。(react-native link react-native-sqlite-storageですでに修正された可能性があります。)

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

1. `android/app/src/main/assets//www`フォルダを作ってすでに生成したsqlite DBをコピーします。

![react-native-sqlite-storage android에 DBファイル追加](/assets/images/category/react-native/2019/react-native-sqlite-storage/www_folder_android.png)


## DBを使う方法
角OSの設定が終わったら、sqlite DBを使うために下記のようにソースを修正します。

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

## 完了
これでreact-native-sqlite-storageライブラリを使ってsqlite DBを使う方法について説明しました。皆さんもDBを一緒に配布するアプリを作成する場合、sqliteを使うことを検討したらどうでしょうか？下記のリンクは上で説明した内容のソースのgitレポジトリ(repository)です。ソースが木になる方は下のリンクを参考してください。

- gitレポジトリ(repository): [react_native_sqlite_storage_exercise](){:rel="nofollow noreferrer" target="_blank"}