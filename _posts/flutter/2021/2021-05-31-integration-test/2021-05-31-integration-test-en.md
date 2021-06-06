---
layout: 'post'
permalink: '/flutter/integration-test/'
paginate_path: '/flutter/:num/integration-test/'
lang: 'en'
categories: 'flutter'
comments: true

title: '[Flutter] Integration Test'
description: Let's see how to do the integration test in Flutter.
image: '/assets/images/category/flutter/background.png'
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [Install integration_test package](#install-integration_test-package)
- [Configuration](#configuration)
  - [Android settings](#android-settings)
  - [iOS settings](#ios-settings)
- [Write test code](#write-test-code)
  - [Driver](#driver)
  - [Test code](#test-code)
  - [Scroll](#scroll)
- [Execute test code](#execute-test-code)
  - [Android integration test](#android-integration-test)
  - [iOS integration test](#ios-integration-test)
- [Completed](#completed)

</div>

## Outline

Let's see how to do the integration test to the app which is developed by Flutter. You can see the details about the integration test on the Flutter official document.

- Official document: [An introduction to integration testing](https://flutter.dev/docs/cookbook/testing/integration/introduction){:rel="nofollow noreferrer" target="_blank"}

This blog referenced the contents of the official document, and summarizes the contents for integration testing. You can see the source code of this blog post on the link below.

- GitHub: [Integration Test Example](https://github.com/dev-yakuza/study-flutter/tree/main/test/integration_test_example){:rel="nofollow noreferrer" target="_blank"}

## Install integration_test package

We need to use the `integration_test` package to do the integration test on Flutter. When you install the Flutter SDK, the `integration_test` package is also installed, so we don't need to install it again.

But, we need to modify the `pubspec.yaml` file to use the `integration_test` package like the below.

```yaml
...
dev_dependencies:
  flutter_test:
    sdk: flutter
  integration_test:
    sdk: flutter
...
```

## Configuration

The integration test will install the app on the Android emulator or iOS simulator, or the device, and do test following the test scenario. So, to use the `integration_test` package to do the integration test on Flutter, we need to configure the setting for each OS.

### Android settings

Let's see how to configure the Android settings for `integration_test` to do the integration test on Flutter.

1. open the `./android/app/build.gradle` file and modify it like the below.

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

1. Create the `./android/app/src/androidTest/java/com/example/[Project Name]/MainActivityTest.java` file and modify it like the below. (You should change the `Project Name` part to your Flutter project name.)

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

### iOS settings

1. Execute the `ios/Runner.xcworkspace` file to open Xcode. (You can excute the command below to open Xcode.)

  ```bash
  open ./ios/Runner.xcworkspace
  ```

1. Select `File > New > Target...`.

  ![Flutter integration test - create new target](/assets/images/category/flutter/2021/integration-test/xcode-target.jpg)

1. Search `Unit Testing Bundle` and click `Next` button.

  ![Flutter integration test - unit testing bundle](/assets/images/category/flutter/2021/integration-test/unit-testing-bundle.jpg)

1. Insert `RunnerTests` on `Product Name`. Enter `Organization Identifier`. change `Language` to `Objective-C`. And then, click `Finish` to create `Unit Testing Bundle`.

  ![Flutter integration test - unit testing](/assets/images/category/flutter/2021/integration-test/unit-testing.jpg)

1. Select `Runner > Info > Configurations` and set the same value on `Runner` and `RunnerTests` in the `Debug/Release/Profile` section.

  ![Flutter integration test - info configurations](/assets/images/category/flutter/2021/integration-test/info-configurations.jpg)

1. set the same version on `iOS Deployment Target` in `Runner > Build Settings` and `iOS Deployment Target` in `RunnerTests > Build Settings`.

  ![Flutter integration test - info configurations](/assets/images/category/flutter/2021/integration-test/ios-deployment-target-runner.jpg)
  ![Flutter integration test - info configurations](/assets/images/category/flutter/2021/integration-test/ios-deployment-target-runner-tests.jpg)

1. open the `./ios/Podfile` file and modify it like the below.

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

1. Execute the command below.

  ```bash
  flutter build ios
  or
  flutter build ios --no-codesign
  ```

1. Open the `RunnerTests.m` file via Xcode and remove all code and add the code below to it.

  ```swift
  @import XCTest;
  @import integration_test;

  INTEGRATION_TEST_IOS_RUNNER(RunnerTests)
  ```

  ![Flutter integration test - modify RunnerTests.m](/assets/images/category/flutter/2021/integration-test/runnertests.jpg)

1. Select `Product > Test` to execute the test.

  ![Flutter integration test - product test](/assets/images/category/flutter/2021/integration-test/product-test.jpg)

  If you don't have any problem, you can see the app build is succeeded, and the simulator is executed.

{% include in-feed-ads.html %}

## Write test code

We've configured the setting for each OS. Next, let's write the integration test code.

### Driver

To do the integration test on Flutter, we need to configure Driver. Create the `./test_driver/integration_test.dart` file and modify it like the below.

```dart
import 'package:integration_test/integration_test_driver.dart';

Future<void> main() => integrationDriver();
```

### Test code

To write the integration test code on Flutter, we need to create the `integration_test` folder and the `_test.dart` file in there. In here, create the `./integration_test/main_test.dart` file and modify it like the below.

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

### Scroll

When you do the integration test, if the screen has a scroll and if you click the widget which is outside of the screen, the error occurs. So, in this case, we need to scroll the screen to the widget which you want to click.

You can scoll the screen in the integration test like the below.

```dart
...
await tester.scrollUntilVisible(find.text('Cancel'), -40);
...
```

The above integration test code scrolls by `40px` until the `Cancel` is shown.

## Execute test code

Next, let's execute the integration test.

### Android integration test

To do the integration test on Android, we need to execute the Android emulator. Execute the command below to get the Android emulator list.

```bash
emulator -list-avds
```

And, execute the command below to open the Android emulator. The `&` mark is an option for executing the command in the background.

```bash
emulator -avd [Emulator ID] &
```

After the emulator is executed, execute the command below to do the integration test.

```bash
flutter test integration_test/
```

And then, you can see the integration test is started on the emulator. After the test is done successfully, execute the command below to exit the emulator.

```bash
adb emu kill
```

### iOS integration test

Execute the command below to open the iOS simulator which is used recently.

```bash
open -a Simulator.app
```

After the simulator is opened, execute the command below to do the integration test.

```bash
flutter test integration_test/
```

After the test is done successfully, execute the command below to exit the simulator.

```bash
killall "iOS Simulator"
```

## Completed

Done! we've seen how to prepare the integration test, how to write the integration test code, and how to execute the integration test on Flutter. Now, I encourage you to test your app in a real environment!
