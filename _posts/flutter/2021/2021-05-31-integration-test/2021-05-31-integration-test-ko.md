---
layout: 'post'
permalink: '/flutter/widget/integration-test/'
paginate_path: '/flutter/:num/widget/integration-test/'
lang: 'ko'
categories: 'flutter'
comments: true

title: '[Flutter] 통합 테스트(Integration Test)'
description: 이번 블로그 포스트에서는 Flutter에서 통합 테스트(Integration Test)를 하는 방법에 대해서 알아봅시다.
image: '/assets/images/category/flutter/background.png'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [integration_test 패키지 설치](#integration_test-패키지-설치)
- [설정](#설정)
  - [안드로이드 설정](#안드로이드-설정)
  - [iOS 설정](#ios-설정)
- [테스트 코드 작성](#테스트-코드-작성)
  - [드라이버](#드라이버)
  - [테스트 코드](#테스트-코드)
  - [스크롤](#스크롤)
- [테스트 코드 실행](#테스트-코드-실행)
  - [안드로이드 통합 테스트](#안드로이드-통합-테스트)
  - [iOS 통합 테스트](#ios-통합-테스트)
- [완료](#완료)

</div>

## 개요

Flutter에서 개발한 앱의 통합 테스트(Integration Test)를 하는 방법에 대해서 알아보려고 합니다. Flutter의 공식 문서에서도 사용법이 자세히 나와 있으니 참고하시기 바랍니다.

- 공식 문서: [An introduction to integration testing](https://flutter.dev/docs/cookbook/testing/integration/introduction){:rel="nofollow noreferrer" target="_blank"}

이번 블로그는 공식 문서의 내용을 참고하였으며, 통합 테스트를 하기 위한 내용을 정리하였습니다. 이곳에서 소개하는 소스코드는 아래에 링크에서 확인할 수 있습니다.

- GitHub: [Integration Test Example](https://github.com/dev-yakuza/study-flutter/tree/main/test/integration_test_example){:rel="nofollow noreferrer" target="_blank"}

## integration_test 패키지 설치

Flutter에서 통합 테스트를 하기 위해서는 `integration_test` 패키지를 사용할 필요가 있습니다. Flutter SDK를 설치하면 해당 패키지도 같이 설치되므로 따로 설치를 할 필요는 없습니다.

다만, 해당 패키지를 사용하기 위해 `pubspec.yaml` 파일을 다음과 같이 수정할 필요가 있습니다.

```yaml
...
dev_dependencies:
  flutter_test:
    sdk: flutter
  integration_test:
    sdk: flutter
...
```

## 설정

통합 테스트는, 안드로이드의 에뮬레이터나 iOS의 시뮬레이터, 또는 디바이스에서 실제로 앱을 실행시킨 후, 테스트 시나리오대로 테스트를 진행하게 됩니다. 따라서 `integration_test` 패키지를 사용하여 Flutter에서 통합 테스트를 하기 위해서는, 각 OS에 맞는 설정을 할 필요가 있습니다.

### 안드로이드 설정

이제 `integration_test` 패키지를 사용하여 Flutter에서 통합 테스트를 하기 위해 안드로이드를 설정하는 방법에 대해서 알아봅시다.

1. `./android/app/build.gradle` 파일을 열고 다음과 같이 수정합니다.

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

1. `./android/app/src/androidTest/java/com/example/[Project Name]/MainActivityTest.java` 파일을 생성하고 다음과 같이 수정합니다.(`Project Name` 부분을 자신의 Flutter 프로젝트 이름으로 변경합니다.)

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

### iOS 설정

1. `ios/Runner.xcworkspace` 파일을 실행하여 Xcode를 실행합니다. (다음 명령어를 실행하여 Xcode를 실행할 수 있습니다.)

  ```bash
  open ./ios/Runner.xcworkspace
  ```

1. `File > New > Target...`을 선택합니다.

  ![Flutter integration test - create new target](/assets/images/category/flutter/2021/integration-test/xcode-target.jpg)

1. `Unit Testing Bundle` 검색하고 `Next` 버튼을 클릭합니다.

  ![Flutter integration test - unit testing bundle](/assets/images/category/flutter/2021/integration-test/unit-testing-bundle.jpg)

1. `Product Name`에 `RunnerTests`를 입력합니다. `Organization Identifier`를 입력합니다. `Language`를 `Objective-C`를 변경합니다. 그리고 `Finish`를 선택하여 `Unit Testing Bundle`을 생성합니다.

  ![Flutter integration test - unit testing](/assets/images/category/flutter/2021/integration-test/unit-testing.jpg)

1. `Runner > Info > Configurations`를 선택하고 `Debug/Release/Profile` 항목에서 `Runner`와 `RunnerTests`의 설정값을 동일한 값으로 맞춰줍니다.

  ![Flutter integration test - info configurations](/assets/images/category/flutter/2021/integration-test/info-configurations.jpg)

1. `Runner > Build Settings`의 `iOS Deployment Target`과 `RunnerTests > Build Settings`의 `iOS Deployment Target`을 동일한 버전으로 맞춰줍니다.

  ![Flutter integration test - info configurations](/assets/images/category/flutter/2021/integration-test/ios-deployment-target-runner.jpg)
  ![Flutter integration test - info configurations](/assets/images/category/flutter/2021/integration-test/ios-deployment-target-runner-tests.jpg)

1. `./ios/Podfile` 파일을 열고 다음과 같이 수정합니다.

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

1. 다음 명령어를 실행합니다.

  ```bash
  flutter build ios
  or
  flutter build ios --no-codesign
  ```

1. Xcode에서 `RunnerTests.m` 파일을 열고 모든 내용을 지우고, 다음의 내용을 추가합니다.

  ```swift
  @import XCTest;
  @import integration_test;

  INTEGRATION_TEST_IOS_RUNNER(RunnerTests)
  ```

  ![Flutter integration test - modify RunnerTests.m](/assets/images/category/flutter/2021/integration-test/runnertests.jpg)

1. `Product > Test`를 선택하여 테스트를 실행해 봅니다.

  ![Flutter integration test - product test](/assets/images/category/flutter/2021/integration-test/product-test.jpg)

  문제가 없다면, 빌드가 성공하는 것을 확인할 수 있으며 시뮬레이터가 실행되는 것을 확인할 수 있습니다.

{% include in-feed-ads.html %}

## 테스트 코드 작성

이제 각 OS에서 테스트할 준비가 끝났습니다. 이제 실제로 테스트 코드를 작성해 보도록 합시다.

### 드라이버

Flutter에서 통합 테스트(Integration Test)를 하기 위해서는 드라이버(Driver)가 필요합니다. `./test_driver/integration_test.dart` 파일을 생성하고 다음과 같이 수정합니다.

```dart
import 'package:integration_test/integration_test_driver.dart';

Future<void> main() => integrationDriver();
```

### 테스트 코드

Flutter에서 통합 테스트(Integration Test)를 작성하기 위해서는 `integration_test`라는 폴더를 생성할 필요가 있으며, 유닛 테스트와 마찬가지로 `_test.dart` 형식으로 테스트 파일을 생성할 필요가 있습니다. 여기서는 우선 `./integration_test/main_test.dart` 파일을 생성하고 다음과 같이 수정하였습니다.

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

### 스크롤

스크롤이 있는 화면에서 통합 테스트를 할 때, 화면에 보이지 않는 위젯을 누르면, 에러가 발생합니다. 따라서 해당 위젯이 화면에 보일 때까지, 화면을 스크롤할 필요가 있습니다.

통합 테스트에서 화면을 스크롤할 때, 다음과 같은 코드를 사용합니다.

```dart
...
await tester.scrollUntilVisible(find.text('Cancel'), -40);
...
```

위의 통합 테스트 코드는 `Cancel`이라는 글자가 보일때까지, 스크롤을 `40px`씩 이동시킵니다.

## 테스트 코드 실행

그럼 이렇게 작성한 테스트 코드를 실행해 봅시다.

### 안드로이드 통합 테스트

안드로이드 통합 테스트를 하기 위해서는 안드로이드 에뮬레이터를 실행할 필요가 있습니다. 다음 명령어를 사용하여 실행 가능한 안드로이드 에뮬레이터를 확인합니다.

```bash
emulator -list-avds
```

다음 명령어를 사용하여 에뮬레이터를 실행합니다. `&` 마크는 명령어를 백그라운드에서 실행하기 위한 옵션입니다.

```bash
emulator -avd [Emulator ID] &
```

에뮬레이터가 실행되었다면, 다음 명령어를 실행하여 작성한 통합 테스트를 실행합니다.

```bash
flutter test integration_test/
```

그럼 에뮬레이터에서 우리가 작성한 통합 테스트가 실행되는 것을 확인할 수 있습니다. 모든 테스트가 무사히 성공하였다면, 다음 명령어를 실행하여 에뮬레이터를 종료시킵니다.

```bash
adb emu kill
```

### iOS 통합 테스트

다음 명령어를 실행하여 최근 실행한 iOS 시뮬레이터를 실행합니다.

```bash
open -a Simulator.app
```

시뮬레이터가 실행되었다면, 다음 명령어를 실행하여 통합 테스트를 실행합니다.

```bash
flutter test integration_test/
```

작성한 통합 테스트가 모두 성공하였다면, 다음 명령어를 실행하여, 실행중인 시뮬레이터를 종료시킵니다.

```bash
killall "iOS Simulator"
```

## 완료

이것으로 Flutter에서 통합 테스트를 하기 위한 준비와, 통합 테스트를 작성하는 방법, 그리고 통합 테스트를 실행하는 방법에 대해서 알아보았습니다. 이제 여러분도 실제 환경에서 여러분의 앱을 테스트해 보시기 바랍니다.
