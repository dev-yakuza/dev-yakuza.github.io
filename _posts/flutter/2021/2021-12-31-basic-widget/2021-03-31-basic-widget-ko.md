---
layout: 'post'
permalink: '/flutter/layout/'
paginate_path: '/flutter/:num/layout/'
lang: 'ko'
categories: 'flutter'
comments: true

title: '[Flutter] 레이아웃'
description: Flutter를 이용하여 앱을 개발해 봅시다. 이번 블로그 포스트에서는 Flutter로 생성한 프로젝트를 살펴보고, Flutter의 위젯에 관해 배워보겠습니다.
image: '/assets/images/category/flutter/background.jpg'
published: false
---

<div id="contents_list" markdown="1">

## 목차

</div>

## 개요

Flutter를 사용해서 앱을 개발해 보려고 합니다. 이번 블로그 포스트에서는 Flutter로 앱을 개발하기 위해 생성한 Flutter 프로젝트의 폴더 및 주요 파일을 살펴보고, Flutter의 기본 요소인 위젯(Widget)에 관해 살펴보도록 하겠습니다.

## 개발 환경

Flutter로 앱을 개발하기 위해서는 Flutter SDK를 설치해야 합니다. Flutter의 개발 환경 설정에 관해서는 이전 블로그 포스트를 참고해 주시기 바랍니다.

- [[MacOS] Flutter 설치]({{site.url}}/{{page.categories}}/installation/){:target="_blank"}

## Dart

Flutter로 앱을 개발하기 위해서는 `Dart`라는 언어를 사용해야합니다. Dart에 대해 잘 모르시는 분들은 Dart에 관한 블로그 시리즈를 참고하시기 바랍니다.

- [[Flutter] Dart에서 변수]({{site.url}}/{{page.categories}}/dart/variable/){:target="_blank"}
- [[Flutter] Dart에서 연산자]({{site.url}}/{{page.categories}}/dart/operator/){:target="_blank"}
- [[Flutter] Dart에서 Statement]({{site.url}}/{{page.categories}}/dart/statement/){:target="_blank"}
- [[Flutter] Dart에서 함수]({{site.url}}/{{page.categories}}/dart/function/){:target="_blank"}
- [[Flutter] Dart에서 클래스]({{site.url}}/{{page.categories}}/dart/class/){:target="_blank"}

{% include in-feed-ads.html %}

## 프로젝트 생성

그럼 이제 Flutter의 새로운 프로젝트를 생성해 봅시다. 다음 명령어를 사용하여 Flutter의 새로운 프로젝트를 생성합니다.

```bash
# flutter create [Project Name]
flutter create first_app
```

프로젝트명은 소문자와 `_`를 사용하는 `스네이크 케이스(Snake case)`를 사용해야 합니다.

## 주요 폴더 및 파일

그럼 이렇게 생성된 Flutter 프로젝트의 주요 폴더 및 파일을 확인해 봅시다.

### pubspec.yaml

Flutter의 새로운 프로젝트를 살펴보면, `pubspec.yaml` 파일을 확인할 수 있습니다. 이 파일은 Flutter 프로젝트의 메타 데이터를 정의하고 관리하는 파일로써, Node의 `package.json`과 비슷한 역할을 합니다.

Flutter에서는 이 파일을 사용해서 프로젝트의 버전을 관리하고, 서드파티 라이브러리나 디펜던시를 관리합니다.

### iOS/Android/Web 폴더

Flutter는 크로스플랫폼 개발 플랫폼으로써, 다양한 플랫폼을 하나의 코드베이스로 개발하는 것을 목표로 하고 있습니다. Flutter를 사용면 React Native와 마찬가지로 `iOS`와 `Android` 앱을 동시에 개발할 수 있으며, 이 때, 각 플랫폼과 관련된 프로젝트와 파일들이 `iOS` 폴더와 `Android` 폴더에 저장되어 있습니다.

우리는 Flutter로 앱을 개발할 때, 이 폴더안에 내용을 수정할 일이 없지만, 앱을 배포할 때에는 이 폴더안에 내용들을 수정하게 됩니다.

최근에는 Flutter가 Web 플랫폼도 지원하게 되었으며, Web 플랫폼을 지원하기 위한 파일, 폴더들은 `Web`이라는 폴더에 저장되어 있습니다.

### lib 폴더

Flutter는 하나의 코드베이스로 `iOS`와 `Android` 앱을 동시에 개발할 수 있습니다. 여기서 하나의 Flutter 코드 베이스를 저장하는 폴더가 바로 `lib` 폴더입니다.

우리는 앞으로 이 폴더안에 Dart를 사용해서 코딩을 하여 앱을 개발할 예정입니다. 이 폴더안에 있는 `main.dart` 파일이 Flutter 프로젝트의 시작 파일입니다. Flutter는 이 파일을 기준으로 앱을 빌드하고 실행합니다.

### test 폴더

test 폴더는 `lib` 폴더에 Dart를 사용하여 작성한 Flutter 앱을 테스트하기 위한 코드를 저장하는 폴더입니다.

이것으로 새롭게 생성된 Flutter 프로젝트의 주요 폴더와 파일을 살펴보았습니다. 이제 Flutter의 가장 기본 요소인 `위젯`에 관해 살펴보도록 하겠습니다.

{% include in-feed-ads.html %}

## 위젯

Flutter는 위젯으로 시작해서 위젯으로 끝납니다. Flutter에서 화면에 표시된 모든 요소가 위젯이며, 눈에 보이지 않지만 화면을 구성하는 레이아웃(Layout)도 위젯입니다.

따라서 Flutter로 앱을 개발하기 위해서는 위젯을 이해할 필요가 있습니다.

위젯은 크게 두 가지로 분류할 수 있습니다.

- Stateful Widget
- Stateless Widget

그럼 이제 각각의 위젯을 자세히 살펴보도록 합시다.

### Stateful Widget

Flutter에서 `Stateful Widget`은 어떤 상태값을 가지고 있으며, 해당 상태값에 의해 화면에 움직임이나 변화를 표현할 때 사용합니다. Stateful Widget은 상태값을 가지고 있으며, 해당 상태값을 지속적으로 추적하고 관리합니다.

- 예: 텍스트 필드, 버튼, 서버에서 전달받은 값을 화면에 표시하는 위젯 등

위와 같이 Stateful Widget은 사용자의 인터렉션의 의해 모양이나 형태를 변경할 때 사용합니다. Stateful Widget은 `StatefulWidget`을 상속받아 생성합니다.

### Stateless Widget

`Stateless Widget`은 Stateful Widget과는 반대로, 어떠한 상태도 가지고 있지 않은 정적인 위젯입니다. 어떠한 상태값도 가지고 있지 않기 때문에 Stateless Widget은 화면에서 어떠한 움직임이나 변화가 없습니다. 즉, 화면상에는 존재하지만 어떠한 것도 하지 않는 위젯입니다.

- 예: 텍스트, 이미지 등.

위와 같이 Stateless Widget은 화면에는 표시되지만, 사용자와 어떠한 인터렉션도 하지않으며, 어떠한 움직임이나 변화를 가지고 있지 않습니다. Stateless Widget은 `StatelessWidget`을 상속하여 생성합니다.

### Widget tree

기본적으로 Flutter는 위젯을 사용하여 개발을 하게 됩니다. 한 위젯은 여러 위젯을 포함할 수 있으며, 모든 위젯은 부모-자식 관게를 가지게 됩니다. 이렇게 부모-자식 관계를 가지게 되면, 이를 `Tree` 계층 구조로 표현할 수 있으며, 관리할 수 있습니다.

예를 들어 설명하면, 웹이 브라우저에 표시될 때, 브라우저는 HTML 요소들을 DOM 트리로 생성하고 관리합니다. 이것과 마찬가지로 Flutter는 위젯을 Widget 트리로 생성하고 관리합니다.

모든 위젯은 부모 위젯과 자식 위젯으로 구성되며 부모 위젯은 `Parent Widget`이라고도 하지만, `Widget Container`라고도 합니다.

{% include in-feed-ads.html %}

## 코딩

그럼 이제 간단하게 코딩을 하면서 위젯을 이해해 보도록 하겠습니다. `lib/main.dart` 파일을 열고 다음과 같이 수정합니다.

```dart
import 'package:flutter/material.dart';

void main() => runApp(FistAppWidget());

class FistAppWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: HomeWidget(),
    );
  }
}

class HomeWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('HOME'),
      ),
      body: Center(
        child: Text('Hello world'),
      ),
    );
  }
}
```

그럼 이제 소스 코드를 하나씩 자세히 살펴보도록 하겠습니다.

```dart
import 'package:flutter/material.dart';
```

우선 우리는 Flutter에서 제공하는 `material` 디자인을 따라 프로그램을 작성할 예정입니다.

```dart
void main() => runApp(FistAppWidget());
```

Dart를 공부하셨다면, `main` 함수는 친숙할 것입니다. `main` 함수는 Dart의 프로그램을 시작하기 위한 함수이며, Flutter에서는 이 함수에서 `runApp` 함수를 호출한 결과값을 반환해야 합니다.

`runApp` 함수는 하나의 위젯을 파라메터로 전달받으며, 여기서 전달받은 위젯이 우리가 만들 Flutter 앱을 구성하는 시작점이 됩니다. 이 위젯은 위젯 트리의 최상단에 위치하게 됩니다.

```dart
class FistAppWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: HomeWidget(),
    );
  }
}
```

`FistAppWidget`은 우리가 만든 커스텀 위젯입니다. 위젯의 이름은 어떤걸 사용해도 되지만, 여기서는 `FistAppWidget`이라고 지정하였으며, 이 위젯은 `StatelessWidget`을 상속하였습니다. 즉, 이 위젯은 어떠한 동적 상태값을 가지고 있지 않습니다.

모든 위젯은 기본적으로 `build` 함수를 가지고 있으며, 이 빌드 함수는 또 다른 위젯을 반환하는 구조를 가지게 됩니다. 이렇게 위젯안에 위젯을 포함하며, 부모-자식 관계가 형성되며, 위젯 트리를 생성하게 됩니다.

이번 예제에서는 `flutter/material.dart`가 제공하는 `MaterialApp` 위젯을 사용하여 앱을 구성하였습니다. `MaterialApp`에는 `home`이라는 Named 파라메터를 가지고 있습니다.

이 `home`은 앱이 실행되고 처음으로 표시되는 화면을 뜻하며, 이 파라메터로 전달된 위젯이 첫 화면에 표시되게 됩니다.

{% include in-feed-ads.html %}

그럼 앱의 첫 화면에 표시되는 `HomeWidget`을 살펴보도록 합시다. `HomeWidget`은 FirstAppWidget과 같이 `StatelessWidget`을 상속받아 만든 커스텀 위젯이며, 역시 어떠한 이름을 사용해도 되지만, 여기서는 HomeWidget이라고 지정하였습니다.

```dart
class HomeWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('HOME'),
      ),
      body: Center(
        child: Text('Hello world'),
      ),
    );
  }
}
```

HomeWidget은 `flutter/material.dart`가 제공하는 `Scaffold`라는 위젯을 반환하고 있습니다. Scaffold 위젯은 `material`으로 앱을 구성할 때, 기본적으로 사용되는 위젯이며, `appBar`와 `body` 등과 같이 화면 구성을 쉽게 할 수 있도록 도와주는 위젯입니다.

```dart
Scaffold(
  appBar: AppBar(
    title: Text('HOME'),
  ),
  ...,
);
```

이번 예제에서는 이 Scaffold를 사용하여 앱 상단 바를 표시하였습니다. appBar 파라메터에는 `AppBar` 위젯을 파라메터로 전달하였으며, AppBar 위젯에는 title 파라메터에 `Text` 위젯을 사용하여 `HOME`이라는 글자를 표시하도록 하였습니다.

```dart
Scaffold(
  ...,
  body: Center(
    child: Text('Hello world'),
  ),
);
```

앱의 `body`에는 `Center`라는 위젯을 통해, 화면에 표시될 위젯을 가운데 정렬 시켰으며, `Text` 위젯을 통해 `Hello world`라는 글자를 표시하도록 하였습니다.

{% include in-feed-ads.html %}

## Closing Label

지금까지 예제를 코딩하다보면, 다음과 같이 우리가 추가하지 않았지만, 자동으로 추가되는 주석을 확인할 수 있습니다.

![Flutter - Closing Label](/assets/images/category/flutter/2021/widget/closing_label.jpg)

Flutter는 수많은 위젯을 중첩해서 앱을 작성하게 됩니다. 이렇게 수많은 위젯과 수많은 코드때문에, 정확히 위젯이 어디서부터 어디까지인지 구별하기가 힘들때가 있습니다. 이를 해결하기 위해서 Flutter는 `Closing Label`을 사용하여 위젯이 끝나는 부분에 자동으로 주석을 추가하게 됩니다.

이 주석은 우리가 추가할 수도, 수정할 수도 없습니다.

## 확인

이것으로 간단한 코딩을 통해 Flutter 앱의 화면 구성 방법에 대해서 알아보았습니다. 코드를 확인해 보면 알 수 있듯이, 앱을 구성하는 모든 요소가 위젯인 것을 알 수 있었습니다.

그럼 이제 이렇게 수정한 앱을 실행해 보도록 하겠습니다.

다음 명령어를 통해 iOS 시뮬레이터를 실행합니다.

```bash
open -a Simulator
```

또는 다음 명령어를 실행하여 안드로이드 에뮬레이터를 실행합니다.

```bash
emulator -list-avds
emulator -avd @name-of-your-emulator
```

iOS 시뮬레이터 또는 에뮬레이터가 실행되었다면, 다음 명령어를 통해 우리가 만든 Flutter 앱을 실행합니다.

```bash
flutter run
```

이렇게 앱을 실행하고 나면 다음과 같이 우리가 만든 앱이 화면에 표시되는 것을 확인할 수 있습니다.

![Flutter - First App](/assets/images/category/flutter/2021/widget/first_app.jpg)

## 완료

이것으로 Flutter를 사용하여 새로운 프로젝트를 생성해 보고, 간단한 예제를 통해 Flutter의 주요 요소인 위젯에 대해서 자세히 살펴보았습니다. Flutter는 이 위젯을 사용하여 모든 앱을 구성하므로, 잘 기억해 두시기 바랍니다.
