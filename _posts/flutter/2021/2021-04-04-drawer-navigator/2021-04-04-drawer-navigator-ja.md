---
layout: 'post'
permalink: '/flutter/navigator/drawer/'
paginate_path: '/flutter/:num/navigator/drawer/'
lang: 'ja'
categories: 'flutter'
comments: true

title: '[Flutter] Drawerナビゲーション'
description: Flutterを使ってアプリを開発してみましょう。今回のブログポストではFlutterで作ったプロジェクトでドロワーナビゲーションを使う方法について説明します。
image: '/assets/images/category/flutter/background.png'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [ドロワー](#ドロワー)
  - [DrawerHeader](#drawerheader)
  - [UserAccountsDrawerHeader](#useraccountsdrawerheader)
- [完了](#完了)

</div>

## 概要

Flutterを使ってアプリを開発してみようかと思います。アプリを開発する時画面の移動をするためにはナビゲーションを使います。今回のブログポストではFlutterでドロワーナビゲーションを使って画面を移動する方法について説明します。

このブログポストで紹介するソースコードは下記のリンクで確認できます。

- GitHub: [https://github.com/dev-yakuza/study-flutter/tree/main/navigator](https://github.com/dev-yakuza/study-flutter/tree/main/navigator){:rel="nofollow noreferrer" target="_blank"}

## ドロワー

ドロワーナビゲーションは主にアプリのメニューでよく使えますし、次のように画面の上にスライドされ表示されます。

![Flutter - drawer](/assets/images/category/flutter/2021/drawer/drawer.jpg)

それじゃ、例題を使ってドロワーナビゲーションを理解してみましょう。次のコマンドを実行してドロワーナビゲーションのためプロジェクトを生成します。

```bash
flutter create my_app
cd stack
```

{% include in-feed-ads.html %}

次はドロワーナビゲーションを実装するため、`main.dart`ファイルを開いて下記のように修正します。

```dart
import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      debugShowCheckedModeBanner: false,
      home: Home(),
    );
  }
}

class Home extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Drawer')),
      body: Center(child: Text('My Page!')),
      drawer: Drawer(
        child: ListView(
          padding: EdgeInsets.zero,
          children: [
            DrawerHeader(
              child: Text('Drawer Header'),
              decoration: BoxDecoration(
                color: Colors.blue,
              ),
            ),
            ListTile(
              title: Text('Item 1'),
              onTap: () {
                Navigator.pop(context);
              },
            ),
            ListTile(
              title: Text('Item 2'),
              onTap: () {
                Navigator.pop(context);
              },
            ),
          ],
        ),
      ),
    );
  }
}
```

じゃ、ソースコードを詳しくみてみましょう。

{% include in-feed-ads.html %}

下記は基本的アプリを画面へ表示するための部分です。

```dart
import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      debugShowCheckedModeBanner: false,
      home: Home(),
    );
  }
}
```

詳しく説明は省略します。このコードでアプリが実行すると`Home`ウィジェットが画面に表示されます。

```dart
class Home extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Drawer')),
      body: Center(child: Text('My Page!')),
      drawer: Drawer(
        child: ListView(...),
      ),
    );
  }
}
```

`Home`ウィジェットは`StatelessWidget`を継承して、`Scaffold`を使って画面を構成しました。この時、`drawer`パラメーターを使って、簡単なドロワーナビゲーションを実装することができます。

```dart
drawer: Drawer(
  child: ListView(...),
),
```

`drawer`パラメータには基本的`Drawer`ウィジェットを指定します。`Darwer`ウィジェットは1つのチャイルドウィジェットを持つことができます。今回の例題では`ListView`ウィジェットを使いました。

今回のブログポストではドロワーナビゲーションを紹介していますので、`ListView`ウィジェットについて詳しく説明は省略します。

### DrawerHeader

`DrawerHeader`ウィジェットはMaterialデザインでドロワーナビゲーションのヘッダーに表示されるウィジェットです。`DrawerHeader`ウィジェットは基本的Materialのデザインを含めております。

![Flutter - drawer header](/assets/images/category/flutter/2021/drawer/drawer_header.jpg)

`Drawerheader`は次のように使うことができますし、`child`にカスタムウィジェットを提供してカスタマイズすることができます。

```dart
DrawerHeader(
  child: Text('Drawer Header'),
  decoration: BoxDecoration(
    color: Colors.blue,
  ),
)
```

{% include in-feed-ads.html %}

### UserAccountsDrawerHeader

`UserAccountsDrawerHeader`はMaterialデザインでドロワーに表示されるユーザアカウント情報を表示するため使うウィジェットです。

![Flutter - user accounts drawer header](/assets/images/category/flutter/2021/drawer/user_accounts_drawer_header.jpg)

`UserAccountsDrawerHeader`は次のように使います。

```dart
UserAccountsDrawerHeader(
  currentAccountPicture: CircleAvatar(
    backgroundImage: AssetImage('assets/bunny.gif'),
  ),
  otherAccountsPictures: [
    CircleAvatar(
      backgroundImage: AssetImage('assets/profile.png'),
    )
  ],
  accountEmail: Text('dev.yakkuza@gmail.com'),
  accountName: Text('Dev Yakuza'),
  onDetailsPressed: () {
    print('press details');
  },
  decoration: BoxDecoration(
      color: Colors.blue[300],
      borderRadius: BorderRadius.only(
        bottomLeft: Radius.circular(40),
        bottomRight: Radius.circular(40),
      )),
),
```

## 完了

これでFlutterでドロワーナビゲーションを使う方法について説明しました。そしてドロワーのヘッダーに表示できるウィジェットを説明しました。
