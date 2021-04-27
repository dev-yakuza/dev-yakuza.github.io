---
layout: 'post'
permalink: '/flutter/widget/textfield/'
paginate_path: '/flutter/:num/widget/textfield/'
lang: 'ja'
categories: 'flutter'
comments: true

title: '[Flutter] Textfieldウィジェット'
description: 今回のブログポストではFlutterでユーザの入力をもらえるTextfieldウィジェットを使う方法について説明します。
image: '/assets/images/category/flutter/background.png'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [Flutterプロジェクト生成](#flutterプロジェクト生成)
- [Textfield](#textfield)
- [InputDecoration](#inputdecoration)
- [SingleChildScrollView](#singlechildscrollview)
- [GestureDetectorとFocusScope](#gesturedetectorとfocusscope)
- [Textfieldの値を使う方法](#textfieldの値を使う方法)
  - [onChanged](#onchanged)
  - [TextEditingController](#texteditingcontroller)
- [完了](#完了)

</div>

## 概要

Flutterを使ってアプリを開発してみようかと思います。今回のブログポストではFlutterでユーザの入力を受ける方法について説明します。

このブログポストで紹介するソースコードは下記のリンクで確認できます。

- GitHub: [https://github.com/dev-yakuza/study-flutter/tree/main/widget](https://github.com/dev-yakuza/study-flutter/tree/main/widget){:rel="nofollow noreferrer" target="_blank"}

## Flutterプロジェクト生成

Flutterでユーザの入力を貰うためには`Textfield`ウィジェットを使います。TextFieldウィジェットを使うためまず、Flutterのプロジェクトを生成します。

```bash
flutter create my_app
cd my_app
```

{% include in-feed-ads.html %}

## Textfield

プロジェクトを生成したら、`main.dart`ファイルを次のように修正して`Textfield`を表示します。

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      debugShowCheckedModeBanner: false,
      home: Home(),
    );
  }
}

class Home extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('TextField'),
      ),
      body: Center(
        child: Padding(
          child: TextField(
            decoration: InputDecoration(
              labelText: 'Input',
            ),
          ),
          padding: EdgeInsets.all(20.0),
        ),
      ),
    );
  }
}
```

上のようにコードをセク生すると次のような画面が確認できます。

![Flutter - textfield](/assets/images/category/flutter/2021/textfield/textfield.jpg)

`Textfield`を表示する部分を詳しくみてみましょう。

```dart
TextField(
  decoration: InputDecoration(
    labelText: 'Input',
  ),
)
```

上のようにTextfieldを表示することができるし、`decration`パラメーターで`InputDecoration`を使って色んな設定ができます。

{% include in-feed-ads.html %}

## InputDecoration

`InputDecoration`を使うと色んな形の`Textfield`ウィジェットが使えます。

```dart
TextField(
  decoration: InputDecoration(
    labelText: 'Email',
    hintText: 'Enter your email',
    labelStyle: TextStyle(color: Colors.redAccent),
    focusedBorder: OutlineInputBorder(
      borderRadius: BorderRadius.all(Radius.circular(10.0)),
      borderSide: BorderSide(width: 1, color: Colors.redAccent),
    ),
    enabledBorder: OutlineInputBorder(
      borderRadius: BorderRadius.all(Radius.circular(10.0)),
      borderSide: BorderSide(width: 1, color: Colors.redAccent),
    ),
    border: OutlineInputBorder(
      borderRadius: BorderRadius.all(Radius.circular(10.0)),
    ),
  ),
  keyboardType: TextInputType.emailAddress,
)
```

このように`InputDecoration`を使うと下記のように色んなデザインを適用することができます。

![Flutter - Textfield InputDecoration](/assets/images/category/flutter/2021/textfield/input_decoration.jpg)

{% include in-feed-ads.html %}

## SingleChildScrollView

`Textfield`を使うとキーボードが出た時、下記のように特に問題はないです。

![Flutter - Textfield keyboard](/assets/images/category/flutter/2021/textfield/textfield_keyboard.jpg)

しかし、普通デザインのため`Column`ウィジェットと`Textfield`を使います。

![Flutter - Textfield column](/assets/images/category/flutter/2021/textfield/textfield_column.jpg)

この時、Columnのエリアの上にキーボードが表示されると下記のようなワーニングがでます。

![Flutter - Textfield column](/assets/images/category/flutter/2021/textfield/textfield_column_warning.jpg)

このワーニングを解決するため、使えるものが`SingleChildScrollView`ウィジェットです。

{% include in-feed-ads.html %}

`SingleChildScrollView`ウィジェットを次のように使うと上の問題を解決することができます。

```dart
SingleChildScrollView(
  child: Column(
    children: [
      Container(
        width: 300,
        height: 300,
        margin: EdgeInsets.all(40.0),
        color: Colors.lightBlue,
      ),
      Padding(
        padding: EdgeInsets.fromLTRB(20.0, 0.0, 20.0, 10.0),
        child: TextField(
          decoration: InputDecoration(
            labelText: 'Email',
            hintText: 'Enter your email',
            labelStyle: TextStyle(color: Colors.redAccent),
            focusedBorder: OutlineInputBorder(
              borderRadius: BorderRadius.all(Radius.circular(10.0)),
              borderSide: BorderSide(width: 1, color: Colors.redAccent),
            ),
            enabledBorder: OutlineInputBorder(
              borderRadius: BorderRadius.all(Radius.circular(10.0)),
              borderSide: BorderSide(width: 1, color: Colors.redAccent),
            ),
            border: OutlineInputBorder(
              borderRadius: BorderRadius.all(Radius.circular(10.0)),
            ),
          ),
          keyboardType: TextInputType.emailAddress,
        ),
      ),
    ],
  ),
)
```

`SingleChildScrollView`を使うと、Textfieldでキーボードがアクティブされた時、画面がスクロールできる状態になって発生した問題が解決されます。

![Flutter - Textfield SingleChildScrollView](/assets/images/category/flutter/2021/textfield/textfield_with_single_child_scroll_view.jpg)

{% include in-feed-ads.html %}

## GestureDetectorとFocusScope

現在キーボードがアクティブになると、キーボードの`done`ボタンを押さないとキーボードは消えません。つまり、Textfieldが`Focus`の状態になると、キーボードがアクティブになり、`done`キーを押してTextfieldが`UnFocus`の状態になるとキーボードが消えます。

普通のアプリのUXはキーボードがアクティブになると、キーボード以外のエリアをタッチすると、キーボードが消えます。このようにキーボード以外のエリアをタッチした時、キーボードが消えるようにするため`GestureDetector`ウィジェットと`FocusScope`ウィジェットを使います。

それじゃ、キーボード以外のエリアをタッチした時、キーボードを消すため、`main.dart`ファイルを次のように修正します。

```dart
GestureDetector(
  onTap: () => FocusScope.of(context).unfocus(),
  child: SingleChildScrollView(...),
),
```

`SingleChildScrollView`ウィジェット中は上で説明したコードなので省略しました。まず、ユーザのイベントを検知するため`GestureDetector`を使いました。この時、ユーザが画面をタッチした場合、キーボードから`Focus`を消すため、`FocusScope`ウィジェットの`unfocus`関数を使いました。

このように`GestureDetector`と`FocusScope`を使うと、キーボードを消す機能を使えます。

## Textfieldの値を使う方法

Textfieldを使う理由はユーザから値を入力して貰って、入力した貰った値を使うためです。それじゃ、Textfieldの値を使う方法について説明します。

### onChanged

ユーザがTextfieldに値を入れるとTextfieldウィジェットの`onChanged`関数がコールされます。この関数がコールされる時、パラメーターで渡されるtextの値を`setState`を使って保存すれば良いです。

```dart
class Home extends StatefulWidget {
  @override
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {
  String inputText = '';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('TextField'),
      ),
      body: Center(
        child: GestureDetector(
          onTap: () => FocusScope.of(context).unfocus(),
          child: SingleChildScrollView(
            child: Column(
              children: [
                Text('$inputText'),
                Padding(
                  padding: EdgeInsets.fromLTRB(20.0, 0.0, 20.0, 10.0),
                  child: TextField(
                    onChanged: (text) {
                      setState(() {
                        inputText = text;
                      });
                    },
                    decoration: InputDecoration(
                      labelText: 'Email',
                      hintText: 'Enter your email',
                      labelStyle: TextStyle(color: Colors.redAccent),
                      focusedBorder: OutlineInputBorder(
                        borderRadius: BorderRadius.all(Radius.circular(10.0)),
                        borderSide:
                            BorderSide(width: 1, color: Colors.redAccent),
                      ),
                      enabledBorder: OutlineInputBorder(
                        borderRadius: BorderRadius.all(Radius.circular(10.0)),
                        borderSide:
                            BorderSide(width: 1, color: Colors.redAccent),
                      ),
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.all(Radius.circular(10.0)),
                      ),
                    ),
                    keyboardType: TextInputType.emailAddress,
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
```

値が変更される部分だけもっと詳しく見ると。

```dart
...
String inputText = '';
...
Text('$inputText')
...
TextField(
  onChanged: (text) {
    setState(() {
      inputText = text;
    });
  },
  ...,
)
...
```

変更された値を保存するため、`StatefulWidget`を生成しました。そして、ユーザの入力を保存するためString変数を定義しました。このように生成したString変数を`Text`ウィジェットを使って画面へ表示しました。

そして`Textfield`ウィジェットの`onChanged`関数を使ってユーザが入力した値を`setState`を使って宣言した変数を変更しました。

今から、Textfieldの値を入力すると、次のようにTextfeildの上に入力した内容が出力されることが確認できます。

![Flutter - Textfield SingleChildScrollView](/assets/images/category/flutter/2021/textfield/textfield_on_changed.jpg)

{% include in-feed-ads.html %}

### TextEditingController

上のようにリアルタイムでデータを更新することもできますが、特定なイベントが発生した時、現在入力された値にアクセスしたい時もあります。この時、使うものた`TextEditingController`です。

`TextEditingController`は次のように使えます。

```dart
class _HomeState extends State<Home> {
  TextEditingController inputController = TextEditingController();
  String inputText = '';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('TextField'),
      ),
      body: Center(
        child: GestureDetector(
          onTap: () => FocusScope.of(context).unfocus(),
          child: SingleChildScrollView(
            child: Column(
              children: [
                Text('$inputText'),
                Padding(
                  padding: EdgeInsets.fromLTRB(20.0, 0.0, 20.0, 10.0),
                  child: TextField(
                    controller: inputController,
                    decoration: InputDecoration(
                      labelText: 'Email',
                      hintText: 'Enter your email',
                      labelStyle: TextStyle(color: Colors.redAccent),
                      focusedBorder: OutlineInputBorder(
                        borderRadius: BorderRadius.all(Radius.circular(10.0)),
                        borderSide:
                            BorderSide(width: 1, color: Colors.redAccent),
                      ),
                      enabledBorder: OutlineInputBorder(
                        borderRadius: BorderRadius.all(Radius.circular(10.0)),
                        borderSide:
                            BorderSide(width: 1, color: Colors.redAccent),
                      ),
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.all(Radius.circular(10.0)),
                      ),
                    ),
                    keyboardType: TextInputType.emailAddress,
                  ),
                ),
                ElevatedButton(
                  onPressed: () {
                    setState(() {
                      inputText = inputController.text;
                    });
                  },
                  child: Text('Update'),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
```

{% include in-feed-ads.html %}

そしたら、`TextEditingController`を使って入力した値を画面に表示する部分だけみてみましょう。

```dart
TextEditingController inputController = TextEditingController();
String inputText = '';
...
Text('$inputText'),
...
TextField(
  controller: inputController,
  ...,
),
...
ElevatedButton(
  onPressed: () {
    setState(() {
      inputText = inputController.text;
    });
  },
  child: Text('Update'),
),
...
```

まず`TextEditingController`を宣言した後、`TextField`ウィジェットの`controller`パラメーターに渡します。そして、`ElevatedButton`ボタンが押せた時、`setState`を使って変数をアップデートします。この時、`inputController.text`のようにTextfieldウィジェットの入力値にアクセスすることができます。

この方法は主にサーバへデータを送るとき使います。

## 完了

これで`Textfield`ウィジェットを使ってユーザが入力した値にアクセスして使う方法についてみてみました。
