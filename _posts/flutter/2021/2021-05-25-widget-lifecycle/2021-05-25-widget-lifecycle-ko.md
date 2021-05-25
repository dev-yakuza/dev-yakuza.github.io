---
layout: 'post'
permalink: '/flutter/widget/lifecycle/'
paginate_path: '/flutter/:num/widget/lifecycle/'
lang: 'ko'
categories: 'flutter'
comments: true

title: '[Flutter] 라이프사이클'
description: 이번 블로그 포스트에서는 Flutter에서 위젯의 라이프사이클(lifecycle)에 대해서 알아봅시다.
image: '/assets/images/category/flutter/background.png'
published: false
---

<div id="contents_list" markdown="1">

## 목차

</div>

## 개요

단순히 화면을 구성하는 Stateless 위젯과는 다르게, Stateful 위젯은 `라이프사이클(lifecycle - 생명주기)`을 가지고 있습니다. 이번 블로그 포스트에서는 Statefule 위젯의 라이프사이클에 대해서 살펴봅니다.

Flutter의 라이프사이클 함수의 이해를 돕기 위해 예제 소스를 제작하였다. 아래에 링크를 통해 소스 코드를 확인할 수 있다.

- GitHub: [AnimatedContainer](https://github.com/dev-yakuza/study-flutter/tree/main/widget/lifecycle){:rel="nofollow noreferrer" target="_blank"}

## Stateless 위젯

Stateless 위젯은 단순히 화면을 구성하는 위젯이므로, 복잡한 라이프사이클을 가지고 있지 않습니다. 그럼 Stateless 위젯에서 라이프사이클 함수에 대해 알아봅시다.

### Stateless 위젯의 Constructor

Flutter에서 위젯은 기본적으로 클래스를 사용하여 생성합니다. 위젯이 기본적으로 클래스로 구성이 되어있기 때문에, 당연히 클래스의 `생성자(Constructor)`를 사용할 수 있습니다.

위젯의 생성자는 클래스의 생성자와 동일한 역할을 하며, 위젯(클래스)안에서 사용될 변수를 초기화할 때 사용됩니다.

```dart
import 'package:flutter/material.dart';

class Home extends StatelessWidget {
  final String title;

  Home({required this.title});

  ...
}
```

### Stateless 위젯의 build

위젯의 `Build` 함수는 화면에 표시될 내용을 작성합니다. 이는 `React`의 `render` 함수와 동일한 역할을 하며, 화면에 표시될 위젯들을 반환합니다.

```dart
import 'package:flutter/material.dart';

class Home extends StatelessWidget {
  ...
  @override
  Widget build(BuildContext context) {
    return Center(
      child: Text('Setting Screen'),
    );
  }
}
```

Stateless 위젯은 자체적으로 상태(State)를 가지고 있지 않습니다. 따라서 부모 위젯으로부터 전달받은 값이 변경이 되면 위젯이 `rebuild`되어 화면을 갱신하게 됩니다. 이때, `Constructor`와 `build`가 다시 실행되게 됩니다.

{% include in-feed-ads.html %}

## Stateful 위젯

Stateful 위젯은 Stateless 위젯과는 다르게 위젯 자체가 상태(State)를 가지고 있기 때문에 위젯의 라이프사이클이 조금 더 복잡합니다. 그럼 Stateful 위젯의 라이프사이클 함수를 살펴보도록 합시다.

### Stateful 위젯의 Constructor

Stateful 위젯의 생성자(Constructor)도 Stateless 위젯의 생성자와 동일한 역할을 합니다. 위젯 클래스로 인스턴스를 생성할 때, 생성자가 제일 먼저 호출되게 되며, 부모 위젯으로부터 파라메터를 전달받을 때 사용됩니다.

```dart
class CounterContainer extends StatefulWidget {
  final int count;

  CounterContainer({required this.count})

  @override
  _CounterContainerState createState() => _CounterContainerState(count: count);
}

class _CounterContainerState extends State<CounterContainer> {
  int count;
  _CounterContainerState({required this.count})
  ...
}
```

### initState

Stateful 위젯이 생성될 때, `한번만` 호출되는 함수로써, 상태(State)값을 초기화할 때 사용됩니다.

```dart
class _CounterContainerState extends State<CounterContainer> {
  late int count;

  @override
  void initState() {
    super.initState();
    count = 0;
  }
  ...
}
```

### didChangeDependencies

이 함수는 위젯이 생성될 때, `initState` 함수가 호출된 직 후, 한번만 호출되게 된다. 또한 [InheritedWidget](https://api.flutter.dev/flutter/widgets/InheritedWidget-class.html){:rel="nofollow noreferrer" target="_blank"}이나 [Provider]({{site.url}}/{{page.categories}}/provider/){:target="_blank"}를 사용하는 경우, InheritedWidget이나 Provider의 내용이 변경될 때, 호출되게 된다.

즉, 부모 위젯이나, 자기 자신의 상태가 변경될 때는 호출되지 않지만, 해당 위젯이 참조(Depedency)하는 위젯(InheritedWidget이나 Provider)이 변경되면 `didChangeDependencies` 함수가 호출되게 된다.

### didUpdateWidget

이 함수는 부모 위젯에 의해 `rebuild`가 필요한 경우, `build` 함수 호출 직전에 호출된다. 보통 부모 위젯의 변경으로 인해, 애니메이션을 다시 실행할 필요가 있을 때, 자주 사용됩니다.

```dart
@override
void didUpdateWidget(MyWidget oldWidget) {
  super.didUpdateWidget(oldWidget);
  if (widget.value != oldWidget.value) {
    // TODO: start a transition between the previous and new value
  }
}
```

또한 부모 위젯에 변경에 따라 상태값을 초기화할 필요가 있다면, 이 함수안에서 `setState`을 통해 상태값을 다시 초기화 할 수 있습니다.

### Stateful 위젯의 build

Stateless 위젯의 build와 동일한 역할을 합니다. 화면에 표시될 위젯들을 반환할 때 사용됩니다. `setState`를 사용하여 Stateful 위젯의 상태(State)가 변경될 때, 다시 호출되여 화면을 갱신합니다.

{% include in-feed-ads.html %}

### deactivate

Stateful 위젯은 Stateless 위젯과는 다르게 상태(State) 객체를 가지고 있습니다. 이 상태 객체가 변경(dirty)되면, 변경된 상태 객체를 사용하여 Stateful 위젯을 `rebuild`하게 됩니다.

`deactivate` 함수는 상태(State) 객체가 트리에서 제거될 때, 호출되게 됩니다. Flutter에서는 때때로 상태 객체만 제거되고 다시 추가되는 경우가 있는데, 예를 들어 `GlobalKey`를 사용하여 현재 위젯을 위젯 트리에 특정 위치로 이동시키면, 해당 위젯의 상태 객체가 변경되므로 `deactivate`가 실행되게 됩니다.

자세한 사항은 공식 문서를 참고하시기 바랍니다.

- 공식 문서: [deactivate](https://api.flutter.dev/flutter/widgets/State/deactivate.html){:rel="nofollow noreferrer" target="_blank"}

### dispose

위젯 객체가 위젯 트리에서 영구적으로 제거될 때, 호출됩니다. 위젯 트리가 완전히 제거는 상황에서는, 상태 객체도 함께 제거되므로 `deactivate` 가 먼저 호출되어 상태 객체가 제거되었음을 알리고, 이후 `dispose`가 호출되어 위젯 객체가 삭제되었음을 알립니다.

`dispose` 호출은 위젯 객체가 영구적으로 제거되었음을 의미하므로, `setState`를 사용하여 해당 위젯의 `rebuild` 할 수 없습니다.

### 호출 순서

- Stateful 위젯이 생성될 때: `Constructor` > `initState` > `didChangeDependencies` > `build`
- setState가 호출되었을 때: `build`
- InheritedWidget 또는 Provider의 값이 변경되었을 때: `didChangeDependencies` > `build`
- 부모 위젯으로부터 전달받는 값이 변경되었을 때: `didUpdateWidget` > `build`
- 상태 객체가 제거되었을 때: `deactivate` > `build`
- 위젯 객체가 제거될 때: `deactivate` > `dispose`

## 완료

이것으로 Flutter에서 위젯의 생명주기(lifecycle)을 확인해 보았습니다. 잘못된 라이프사이클 함수 사용은, 앱의 성능을 크게 저하시키거나 무한 루프에 빠질 수 있는 위험이 있으므로 주의해서 사용해야 합니다. 또한, 위젯의 라이프사이클은 `setState`나 특정 함수의 호출 시기를 결정하거나 애니메이션의 실행 시점에 중요한 역할을 하므로 이번 기회에 잘 공부해 두는게 좋을거 같습니다.
