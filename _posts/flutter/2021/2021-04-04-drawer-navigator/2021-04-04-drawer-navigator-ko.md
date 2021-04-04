---
layout: 'post'
permalink: '/flutter/navigator/drawer/'
paginate_path: '/flutter/:num/navigator/drawer/'
lang: 'ko'
categories: 'flutter'
comments: true

title: '[Flutter] 드로어 내비게이션'
description: Flutter를 이용하여 앱을 개발해 봅시다. 이번 블로그 포스트에서는 Flutter로 생성한 프로젝트에서 드로어 내비게이션을 사용하는 방법에 대해서 알아봅니다.
image: '/assets/images/category/flutter/background.jpg'
published: false
---

<div id="contents_list" markdown="1">

## 목차

</div>

## 개요

Flutter를 사용해서 앱을 개발해 보려고 합니다. 앱 개발에서 화면 이동을 위해서는 내비게이션을 사용해야 합니다. 이번 블로그 포스트에서는 Flutter에서 드로어 내비게이션을 사용하여 화면을 이동하는 방법에 대해서 알아봅시다.

![Flutter - drawer](/assets/images/category/flutter/2021/drawer/drawer.jpg)

이 블로그 포스트에서 소개하는 소스 코드는 아래에 링크에서 확인할 수 있습니다.

- GitHub: [https://github.com/dev-yakuza/study-flutter/tree/main/navigator](https://github.com/dev-yakuza/study-flutter/tree/main/navigator){:rel="nofollow noreferrer" target="_blank"}

## 드로어

드로어 내비게이션은 주로 앱의 메뉴에 많이 사용되며, 다음과 같이 화면 위로 슬라이드되어 표시됩니다.

그럼 예제를 통해 드로어 내비게이션을 이해해 봅시다. 다음 명령어를 사용하여 드로어 내비게이션을 위한 프로젝트를 생성합니다.

```bash
flutter create my_app
cd stack
```

{% include in-feed-ads.html %}

그럼 드로어 내비게이션을 구현하기 위해, `main.dart` 파일을 열고 다음과 같이 수정합니다.

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

그럼 이제 소스 코드를 자세히 살펴봅시다.

{% include in-feed-ads.html %}

다음은 기본적으로 앱을 화면에 표시하기 위한 부분입니다.

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

자세한 설명은 생략하도록 하겠습니다. 앱이 실행되면 `Home` 위젯이 화면에 표시되게 됩니다.

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

`Home` 위젯은 `StatelessWidget`을 상속받고, `Scaffold`를 사용하여 화면을 구성하였습니다. 이때, `drawer` 파라메터를 사용하면, 간단하게 드로어 내비게이션을 구현할 수 있습니다.

```dart
drawer: Drawer(
  child: ListView(...),
),
```

`drawer` 파라메터에는 기본적으로 `Drawer` 위젯을 지정해야 합니다. `Darwer` 위젯은 하나의 자식 위젯을 가질 수 있습니다. 이번 예제에서는 `ListView` 위젯을 사용하였습니다.

이번 블로그 포스트는 드로어 내비게이션을 소개하고 있으므로, `ListView` 위젯에 대한 설명은 생략하도록 하겠습니다.

### DrawerHeader

`DrawerHeader` 위젯은 Material 디자인에서 드로어 내비게이션 상단에 표시되는 위젯입니다. 기본적인 디자인만 포함하고 있습니다.

![Flutter - drawer header](/assets/images/category/flutter/2021/drawer/drawer_header.jpg)

`Drawerheader`는 다음과 같이 사용할 수 있으며, `child`에 커스텀 위젯을 제공함으로써, 커스터마이즈할 수 있습니다.

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

`UserAccountsDrawerHeader`는 Material 디자인에서 드로어에 표시되는 사용자 계정 정보를 표시하는데 사용하는 위젯입니다.

![Flutter - user accounts drawer header](/assets/images/category/flutter/2021/drawer/user_accounts_drawer_header.jpg)

`UserAccountsDrawerHeader`는 다음과 같이 사용할 수 있습니다.

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

## 완료

이것으로 Flutter에서 드로어 내비게이션을 사용하는 방법에 대해서 살펴보았습니다. 그리고 드로어 상단에 표시할 수 있는 위젯들을 살펴보았습니다.
