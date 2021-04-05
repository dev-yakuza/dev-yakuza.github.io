---
layout: 'post'
permalink: '/flutter/build-context/'
paginate_path: '/flutter/:num/build-context/'
lang: 'ko'
categories: 'flutter'
comments: true

title: '[Flutter] BuildContext'
description: Flutter를 이용하여 앱을 개발해 봅시다. 이번 블로그 포스트에서는 Flutter로 생성한 프로젝트를 살펴보고, Flutter의 위젯에 관해 배워보겠습니다.
image: '/assets/images/category/flutter/background.png'
published: false
---

<div id="contents_list" markdown="1">

## 목차

</div>

## 개요

future => promise

async-await

```dart
import 'dart:io';

void main() {
  showData();
}

void showData() async {
  startTask();
  String account = await accessData();
  fetchData(account);
};

void startTask() {
  print('Start task');
};

Future<String> accessData() async {
  String account = '';

  // sleep(Duration(second: 3));
  await Future.delay(Duration(second: 3), () {
    print('Access data');
    account = 'Dev Yakuza';
  });

  return account;
};

void fetchData(String account) {
  print('Fetch data');
  print('Account: $account');
};
```


위젯 앞의 const를 붙이면 rebuild될 때, 다시 빌드하지 않는다. Text나 Image같이 다시 빌드될 필요가 없을 때 사용된다.

const Text('test')

하지만 변수를 함께 표시할 때에는 `const`를 사용하면 안된다.

FutureBuilder 데이터가 없을 때, 있을 때를 표시할 때 사용

```dart
FutureBuilder(
  future: data,
  build: (context, snapshot) {
    if(snapshot.hasData) {
      return Text('Data: $data');
    } else if(snapshot.hasError) {
      return Text('Error: ${snapshot.error}');
    }

    return CircularProgressIndicator();
  }
)
```

https://github.com/icodingchef/future_json



