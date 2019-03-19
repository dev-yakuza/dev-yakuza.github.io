---
layout: 'post'
permalink: '/react-native/react-native-firebase-analytics/'
paginate_path: '/react-native/:num/react-native-firebase-analytics/'
lang: 'ko'
categories: 'react-native'
comments: true

title: 'Firebase Analytics'
description: 'react-native-firebase 라이브러리를 사용하여 좀 더 자세하게 앱을 분석해 보자'
image: '/assets/images/category/react-native/react-native-firebase-analytics.jpg'
---


## 개요
이전 블로그인 [Firebase Admob]({{site.url}}/{{page.categories}}/react-native-firebase-admob/){:target="_blank"}에서 ```react-native-firebase```를 설정하는 방법을 설명하였습니다. 이전 블로그에서도 이야기 했지만 파이어베이스 애널리틱스(Firebase Analytics)는 ```react-native-firebase```를 설정만 하는 것으로 자동으로 분석을 시작해 줍니다. 하지만 우리가 실제로 파이어베이스 애널리틱스(Firebase Analytics)에서 분석한 내용을 본 결과, 자동으로 해주는 분석만으로는 부족한 부분이 많아 이번 블로그를 작성하게 되었습니다.

이번 블로그에서는 ```react-native-firebase```를 사용하여 파이어베이스 애널리틱스(Firebase Analytics)로 좀 더 상세하게 분석하기 위한 방법에 대해서 설명합니다.

## 라이브러리 설정
여기서 설명할 내용은 ```react-native-firebase``` 라이브러리를 사용한 파이어베이스 애널리틱스(Firebase Analytics)입니다. 따라서 기본적으로 ```react-native-firebase```를 설정할 필요가 있습니다. ```react-native-firebase```를 설정하는 방법은 이전 블로그인 [Firebase Admob]({{site.url}}/{{page.categories}}/react-native-firebase-admob/){:target="_blank"}를 참고하여 설정하여 주시기 바랍니다. 이번 블로그에서는 ```react-native-firebase``` 라이브러리 설정에 관해서는 생략하도록 하겠습니다.

## 디버그뷰(DebugView)
파이어베이스 애널리틱스(Firebase Analytics)는 앱이 기록하는 이벤트를 약 1시간 동안 취합한 후 일괄 업로드합니다. 따라서 분석된 데이터를 보기 위해서는 약 1시간이라는 시간을 기다려야 합니다. 하지만 개발하거나 테스트할 때는 이렇게 기다릴 수 없습니다. 그래서 파이어베이스 애널리틱스(Firebase Analytics)는 디버깅이 가능한 디버그뷰(DebugView)를 지원합니다. 디버그뷰(DebugView)를 이용하면 취합한 데이터의 업로드 시간을 최소화하여 거의 실시간으로 분석을 진행할 수 있습니다.

앞으로 ```react-native-firebase``` 라이브러리의 기능을 사용하여 파이어베이스 애널리틱스(Firebase Analytics)에 추가할 분석 기능들을 바로 확인 가능하도록 디버그뷰(DebugView)를 설정하고 진행하겠습니다.

### iOS
파이어베이스 애널리틱스(Firebase Analytics)에 디버그뷰(DebugView) 기능을 사용하기 위해 iOS에 아래와 같이 설정합니다.

- RN(react native) 프로젝트 폴더에서 ```ios/[project].xcworkspace``` 파일을 선택하여 xcode를 실행합니다.
- 상단 메뉴에서 ```Product``` > ```Scheme``` > ```Edit Scheme...```를 선택합니다.
    ![xcode edit scheme](/assets/images/category/react-native/react-native-firebase-analytics/edit-scheme.png)
- 활성화된 ```Edit schema...``` 창 왼쪽 메뉴에서 ```Run```을 선택하고 오른쪽에 ```Arguments``` 탭을 선택합니다.
    ![edit scheme arguments](/assets/images/category/react-native/react-native-firebase-analytics/edit-scheme-arguments.png)
- 선택한 ```Arguments``` 탭에 ```Arguments Passed On Launch```에 ```+```버튼을 눌러 아래에 내용을 추가합니다.(마이너스(```-```) 부호도 같이 복사 붙여넣습니다.)
    ```bash
    -FIRDebugEnabled
    ```
    ![edit scheme arguments FIRDebugEnabled](/assets/images/category/react-native/react-native-firebase-analytics/edit-scheme-FIRDebugEnabled.png)

### Android
안드로이드는 iOS보다 간단합니다. 안드로이드 에뮬레이터(Android Emulator)나 디바이스(Device)를 기동하고 아래에 명령어를 입력합니다.

```bash
adb shell setprop debug.firebase.analytics.app <package_name>
```

파이어베이스 애널리틱스(Firebase Analytics)의 ```DebugView```를 중단하고 싶을 땐 아래에 명령어를 입력합니다.

```bash
adb shell setprop debug.firebase.analytics.app .none.
```

### 테스트
이제 파이어베이스 콘솔(Firebase Console)에 파이어베이스 애널리틱스(Firebase Analytics) ```DebugView``` 메뉴로 이동합니다.

![firebase analytics debugview](/assets/images/category/react-native/react-native-firebase-analytics/firebase-analytics-debugview.png)

현재는 iOS, Android 둘 다 기동하지 않은 상태임으로 ```DebugView```가 대기 상태에 있습니다. 이제 iOS나 Android를 기동합니다.

![firebase analytics debugview analytics](/assets/images/category/react-native/react-native-firebase-analytics/debugview-analytics.png)

잠시후 위와 같이 거의 실시간으로 분석되는 화면을 볼 수 있습니다.

## 화면 분석
파이어베이스 애널리틱스(Firebase Analytics)에서 사용자가 어떤 화면을 봤는지 기록해 주는 ```screen_view```라는 이벤트(Event)가 있습니다.

파이어베이스 콘솔(Firebase Console)에서 ```Analytics```의 ```Events```라는 메뉴를 선택하면 아래와 같은 화면을 볼 수 있습니다.

![google firebase console Analytics Events menu](/assets/images/category/react-native/react-native-firebase-analytics/analytics-events.png)

화면에 보이는 ```Event``` 리스트에서 ```screen_view```를 선택합니다.

![Firebase Analytics Events screen_view](/assets/images/category/react-native/react-native-firebase-analytics/analytics-events-screen_view.png)

조금 스크롤을 해서 하단으로 이동하면 ```User engagement``` > ```Screen class```라는 항목이 보입니다.

![Firebase Analytics Events screen_view screen class to screen name](/assets/images/category/react-native/react-native-firebase-analytics/screen_view-class-to-name.png)

User engagement를 ```Screen class```에서 ```Screen name```으로 변경합니다.

![Firebase Analytics Events screen name no data](/assets/images/category/react-native/react-native-firebase-analytics/screen_name-no-data.png)

여기까지 확인하면 무언가 부족함을 느끼셨을 겁니다. ```Screen class```에서는 정말 기본이 되는 class만 확인이 되고 ```Screen name```에는 아무 데이터가 없어 사용자가 어떤 화면을 많이 봤는지 분석이 되지 않습니다.

그래서 우리는 ```react-native-firebase```가 제공하는 ```setCurrentScreen```함수를 사용하여 사용자가 본 화면을 분석하기로 했습니다.

우리는 분석하고자 하는 앱(App)의 화면에 아래와 같이 코드를 추가하였습니다.

```js
render() {
    firebase.analytics().setCurrentScreen('HOME');
    ...
    return (
        ...
    );
}
```

react-native-firebase가 제공하는 ```setCurrentScreen``` 함수에 앱(App)의 화면 이름을 입력해 줍니다.

그리고 테스트하여 분석이 끝나면 아래와 같이 우리가 ```setCurrentScreen``` 함수에 입력한 앱(App)의 화면 이름을 확인 할 수 있습니다.

![Firebase Analytics Events screen name with data](/assets/images/category/react-native/react-native-firebase-analytics/screen_name-with-data.png)

파이어베이스 애널리틱스(Firebase Analytics)의 ```DebugView```에서도 실시간으로 분석이 되는 것을 확인할 수 있습니다.

![Firebase Analytics Events screen name on debug view](/assets/images/category/react-native/react-native-firebase-analytics/screen_name-on-debugview.png)

DebugView에서 해당 이벤트(screen_view)를 선택하면 위와 같이 상세 화면을 볼 수 있습니다.

## 커스텀 이벤트 분석
위에서 소개한 ```setCurrentScreen``` 함수로 사용자가 본 화면은 분석이 가능했지만 실제 그 화면에서 어떤 액션을 취했는지는 알수가 없습니다. 이번에는 ```logEvent```를 사용하여 파이어베이스 애널리틱스(Firebase Analytics)에서 커스텀 이벤트(Custom Event)를 분석하는 방법에 대해서 알아보겠습니다.

우리는 파이어베이스 애널리틱스(Firebase Analytics)에서 분석하고 싶은 커스텀 이벤트(Custom Event)를 아래에 코드를 통해 추가하였습니다.

```js
private _onSpeech = (Tts, text: string) => {
    firebase.analytics().logEvent('onPressSoundButton', { target: text });
    ...
}
```

logEvent의 첫번째 파라미터는 알파벳 100자와 특수문자는 언더바(_)만 지원합니다.(```up to 100 characters is the maximum character length supported for event parameters.```) 하지만 우리는 다국어를 지원하는 앱이고 어떤 언어로 어떤 액션을 했는지 분석하고 싶었습니다. 그래서 두번째 파라미터를 사용하여 커스텀 이벤트(Custom Event)에 커스텀 파라미터(Custom Parameter)를 추가하였습니다. 두번째 파라미터는 오브젝트(Object) 타입이므로 자유롭게 커스텀 파라미터(Custom Parameter)를 만들어 분석에 활용할 수 있습니다.

위와 같이 커스텀 이벤트(Custom Event)에 커스텀 파라미터(Custom Parameter)를 추가하였다면 파이어베이스 콘솔(Firebase Console)에도 추가해야 합니다.

![Firebase Analytics Events custom event](/assets/images/category/react-native/react-native-firebase-analytics/custom-event-custom-parameter.png)

위와 같이 ```Analytics``` 메뉴의 ```Events```로 이동한 후 이벤트(Event) 리스트에서 추가한 커스텀 이벤트(Custom Event)에 마우스를 이동합니다.

![Firebase Analytics custom parameter menu](/assets/images/category/react-native/react-native-firebase-analytics/custom-parameter-menu.png)

마우스를 이동하면 해당 항목 오른쪽에 ```...``` 버튼이 활성화됩니다. 해당 버튼을 눌러 보이는 메뉴에서 ```Edit parameter reporting```을 선택합니다.

![Firebase Analytics custom parameter edit parameter reporting](/assets/images/category/react-native/react-native-firebase-analytics/custom-parameter-edit-parameter-reporting.png)

왼쪽 검색바에 분석하고 싶은 커스텀 이벤트(Custom Event)의 커스텀 파라미터(Custom Parameter)를 입력하고 ```ADD```를 눌러 커스텀 파라미터(Custom Parameter) 추가합니다.

![Firebase Analytics add custom parameter](/assets/images/category/react-native/react-native-firebase-analytics/add-custom-parameter.png)

추가 완료후 테스트를 진행합니다. 데이터가 쌓이고(하루정도 지나고), ```Events``` 메뉴에 추가한 커스텀 이벤트(Custom Event)를 선택합니다.

![Firebase Analytics custom parameter](/assets/images/category/react-native/react-native-firebase-analytics/custom-parameter.png)

조금 스크롤하여 하단으로 이동하면 우리가 추가한 커스텀 파라미터(Custom Parameter)의 분석 결과를 확인할 수 있습니다.

![Firebase Analytics custom parameter result](/assets/images/category/react-native/react-native-firebase-analytics/custom-parameter-result.png)

파이어베이스 애널리틱스(Firebase Analytics)의 ```DebugView```에서도 실시간으로 분석이 되는 것을 확인할 수 있습니다.

![Firebase Analytics Events custom event on debug view](/assets/images/category/react-native/react-native-firebase-analytics/custom_event-on-debugview.png)

DebugView에서 해당 커스텀 이벤트(Custom Event)를 선택하면 위와 같이 추가한 커스텀 파라미터(Custom Parameter)가 함께 보이는 상세 화면을 볼 수 있습니다.

## 참고
- 파이어베이스 디버깅 이벤트: [https://firebase.google.com/docs/analytics/debugview](https://firebase.google.com/docs/analytics/debugview){:rel="nofollow noreferrer" target="_blank"}
- react-native-firebase: [https://rnfirebase.io/docs/v5.x.x/analytics/reference/analytics](https://rnfirebase.io/docs/v5.x.x/analytics/reference/analytics){:rel="nofollow noreferrer" target="_blank"}