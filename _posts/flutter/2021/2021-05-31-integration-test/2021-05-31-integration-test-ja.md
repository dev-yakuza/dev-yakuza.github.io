---
layout: 'post'
permalink: '/flutter/widget/integration-test/'
paginate_path: '/flutter/:num/widget/integration-test/'
lang: 'ja'
categories: 'flutter'
comments: true

title: '[Flutter] 統合テスト(Integration Test)'
description: 今回のブログポストではFlutterで統合テスト(Integration Test)をする方法を説明します。
image: '/assets/images/category/flutter/background.png'
published: false
---

<div id="contents_list" markdown="1">

## 目次

</div>

## 概要

Flutterで開発したアプリの統合テスト(Integration Test)をする方法について説明しようかと思います。Flutterの公式とドキュメントでも使い方が詳しく乗せておりますので、ご参考してみてください。

- 公式ドキュメント: [An introduction to integration testing](https://flutter.dev/docs/cookbook/testing/integration/introduction){:rel="nofollow noreferrer" target="_blank"}

今回のブログポストでは公式ドキュメントの内容を参考して、統合テストするための内容をまとめてみました。ここで紹介するソースコードは下記のリンクで確認できます。

- GitHub: [Integration Test Example](https://github.com/dev-yakuza/study-flutter/tree/main/test/integration_test_example){:rel="nofollow noreferrer" target="_blank"}

## integration_testパッケージインストール

Flutterで統合テストをするためには、`integration_test`パッケージを使う必要があります。Flutter SDKをインストールすると、このパッケージも一緒にインストールされるので、別にインストールする必要はありません。

しかし、このパッケージを使うため`pubspec.yaml`ファイルを次のように修正する必要があります。

```yaml
...
dev_dependencies:
  flutter_test:
    sdk: flutter
  integration_test:
    sdk: flutter
...
```

## 設定

統合テストは、アンドロイドのエミュレーターやiOSのシミュレーター、またはデバイスで実際アプリを起動した後、テストシナリオによってテストを実行します。したがって、`integration_test`パッケージを使ってFlutterで統合テストをするためには、各OSに合った設定をする必要があります。

### アンドロイド設定

次は`integration_test`パッケージを使ってFlutterで統合テストをするため、アンドロイドを設定する方法について説明します。

1. `./android/app/build.gradle`ファイルを開いて下記のように修正します。

  ```js
  ...
  defaultConfig {
      ...
      testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"
  }
  ...
  dependencies {
      ...
      // For integration test
      testImplementation 'junit:junit:4.12'
      // https://developer.android.com/jetpack/androidx/releases/test/#1.2.0
      androidTestImplementation 'androidx.test:runner:1.2.0'
      androidTestImplementation 'androidx.test.espresso:espresso-core:3.2.0'
  }
  ...
  ```

1. `./android/app/src/androidTest/java/com/example/[Project Name]/MainActivityTest.java`ファイルを生成して次のように修正します。(Project Nameの部分を自分のFlutterプロジェクトの名前で変更します。)

  ```java
  package com.example.[Project Name];

  import androidx.test.rule.ActivityTestRule;
  import dev.flutter.plugins.integration_test.FlutterTestRunner;
  import org.junit.Rule;
  import org.junit.runner.RunWith;

  @RunWith(FlutterTestRunner.class)
  public class MainActivityTest {
    @Rule
    public ActivityTestRule<MainActivity> rule = new ActivityTestRule<>(MainActivity.class, true, false);
  }
  ```

{% include in-feed-ads.html %}

### iOSの設定

1. `ios/Runner.xcworkspace`ファイルを実行してXcodeを実行します。(次のコマンドを使ってXcodeを実行することができます。)

  ```bash
  open ./ios/Runner.xcworkspace
  ```

1. `File > New > Target...`を選択します。

  ![Flutter integration test - create new target](/assets/images/category/flutter/2021/integration-test/xcode-target.jpg)

1. `Unit Testing Bundle`を検索して`Next`ボタンを選択します。

  ![Flutter integration test - unit testing bundle](/assets/images/category/flutter/2021/integration-test/unit-testing-bundle.jpg)

1. `Product Name`に`RunnerTests`を入力します。`Organization Identifier`を入力します。`Language`を`Objective-C`で変更します。そして、`Finish`を選択して`Unit Testing Bundle`を生成します。

  ![Flutter integration test - unit testing](/assets/images/category/flutter/2021/integration-test/unit-testing.jpg)

1. `Runner > Info > Configurations`を選択して`Debug/Release/Profile`の項目で`Runner`と`RunnerTests`の設定を同じ値で設定します。

  ![Flutter integration test - info configurations](/assets/images/category/flutter/2021/integration-test/info-configurations.jpg)

1. `Runner > Build Settings`の`iOS Deployment Target`と`RunnerTests > Build Settings`の`iOS Deployment Target`を同じバージョンで合わせます。

  ![Flutter integration test - info configurations](/assets/images/category/flutter/2021/integration-test/ios-deployment-target-runner.jpg)
  ![Flutter integration test - info configurations](/assets/images/category/flutter/2021/integration-test/ios-deployment-target-runner-tests.jpg)

1. `./ios/Podfile`ファイルを開いて下記のように修正します。

  ```rb
  platform :ios, '10.0'
  ...
  target 'Runner' do
    ...
    # For integration test
    target 'RunnerTests' do
      inherit! :search_paths
    end
  end
  ...
  ```

1. 次のコマンドを実行します。

  ```bash
  flutter build ios
  or
  flutter build ios --no-codesign
  ```

1. Xcodeで`RunnerTests.m`ファイルを開いて全ての内容を消して、次の内容を追加します。

  ```swift
  @import XCTest;
  @import integration_test;

  INTEGRATION_TEST_IOS_RUNNER(RunnerTests)
  ```

  ![Flutter integration test - modify RunnerTests.m](/assets/images/category/flutter/2021/integration-test/runnertests.jpg)

1. `Product > Test`を選択してテストを実行してみます。

  ![Flutter integration test - product test](/assets/images/category/flutter/2021/integration-test/product-test.jpg)

  問題なければ、ビルドが成功して、シミュレーターが実行されることが確認できます。

{% include in-feed-ads.html %}

## テストコード作成

各OSでテストをする準備が終わりました。次は実際テストコードを作成してみましょう。

### ドライバー

Flutterで統合テスト(Integration Test)をするためにはドライバー(Driver)が必要です。`./test_driver/integration_test.dart`ファイルを生成して次のように修正します。

```dart
import 'package:integration_test/integration_test_driver.dart';

Future<void> main() => integrationDriver();
```

### テストコード

Flutterで統合テスト(Integration Test)を作成するため、`integration_test`と言うフォルダを生成する必要があり、ユニットテストと同じように`_test.dart`の形式でテストファイルを生成する必要があります。ここではまず、`./integration_test/main_test.dart`ファイルを生成して次と同じように修正します。

```dart
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:integration_test/integration_test.dart';

import 'package:integration_test_example/main.dart' as app;

void main() {
  IntegrationTestWidgetsFlutterBinding.ensureInitialized();

  testWidgets("successful test example", (WidgetTester tester) async {
    app.main();
    await tester.pumpAndSettle();

    expect(find.text('0'), findsOneWidget);

    await tester.tap(find.byType(FloatingActionButton));
    await tester.pumpAndSettle();

    expect(find.text('1'), findsOneWidget);
  });
}
```

## テストコードの実行

次はこのように作成したテストコードを実行してみましょう。

### アンドロイドの統合テスト

アンドロイドで統合テストをするためにはアンドロイドエミュレーターを実行する必要があります。次のコマンドを使って実行可能なアンドロイドのエミュレーターを確認します。

```bash
emulator -list-avds
```

次のコマンドを実行してエミュレーターを実行します。`&`マークはコマンドをバックグラウンドで実行するためのオプションです。

```bash
emulator -avd [Emulator ID] &
```

エミュレーターが実行されたら、次のコマンドを実行して作成した統合テストを実行します。

```bash
flutter test integration_test/
```

そしたら、エミュレーターで私たちが作成した統合テストが実行されることが確認できます。全てのテストが無事成功したら、次のコマンドを実行してエミュレーターを終了します。

```bash
adb emu kill
```

{% include in-feed-ads.html %}

### iOSの統合テスト

次のコマンドを実行して最近実行されたiOSシミュレーターを実行します。

```bash
open -a Simulator.app
```

シミュレーターが実行されたら、次のコマンドを実行して統合テストを実行します。

```bash
flutter test integration_test/
```

作成した統合テストが全て成功したら、次のコマンドを実行して、起動したシミュレーターを終了します。

```bash
killall "iOS Simulator"
```

## 完了

これでFlutterで統合テストをするための準備と統合テストを作成する方法、そして統合テストを実行する方法についてみてみました。今後、皆さんも実際の環境で皆さんのアプリをテストしてみてください。
