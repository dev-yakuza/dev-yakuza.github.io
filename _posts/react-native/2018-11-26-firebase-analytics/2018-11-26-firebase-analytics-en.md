---
layout: 'post'
permalink: '/react-native/react-native-firebase-analytics/'
paginate_path: '/react-native/:num/react-native-firebase-analytics/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'Firebase Analytics'
description: 'react-native-firebase 라이브러리를 사용하여 좀 더 자세하게 앱을 분석해 보자'
image: '/assets/images/category/react-native/react-native-firebase-analytics.jpg'
---


## outline
we introduced how to set ```react-native-firebase``` at previous blog post - [Firebase Admob]({{site.url}}/{{page.categories}}/react-native-firebase-admob/){:target="_blank"}. we mentioned at previous blog post that Firebase Analytics automatically is started by configuring ```react-native-firebase```. however, when we saw results created Firebase Analytics automatically, we felt that's not enough, so we write this blog post.

in here we will introduce how to make Firebase Analytics results more detail by using ```react-native-firebase```.

## configure library
this blog post is for how to use ```react-native-firebase``` for Firebase Analytics. so we need to set ```react-native-firebase``` basically. if you don't know how to set ```react-native-firebase```, see our preivous blog post - [Firebase Admob]({{site.url}}/{{page.categories}}/react-native-firebase-admob/){:target="_blank"}. in this blog post, we skip to install and configure ```react-native-firebase```.

## DebugView
Firebase Analytics gathers app event logs for about one hour and upload them. so if we want to see analytics result data, we should wait for about one hour. however, we can't wait for one hour to develop or test. so Firebase Analytics provides ```DebugView``` which we can debug analytics events. if we use DebugView, we can see almost real time analytics results.

first, we configure DebugView so that we can immediately see Firebase Analytics results after adding ```react-native-firebase``` library features.

### iOS
configure below to iOS for using Firebase Analytics DebugView feature.

- click ```ios/[project].xcworkspace``` file in RN(react native) project folder to execute xcode
- select ```Product``` > ```Scheme``` > ```Edit Scheme...``` menu on the top of the screen.
    ![xcode edit scheme](/assets/images/category/react-native/react-native-firebase-analytics/edit-scheme.png)
- select ```Run``` menu on the left of ```Edit scheme...``` dialog and click ```Arguments``` tab on right side.
    ![edit scheme arguments](/assets/images/category/react-native/react-native-firebase-analytics/edit-scheme-arguments.png)
- click ```+``` button in ```Arguments Passed On Launch``` session on ```Arguments``` tab and insert below code(include ```-``` )
    ```bash
    -FIRDebugEnabled
    ```
    ![edit scheme arguments FIRDebugEnabled](/assets/images/category/react-native/react-native-firebase-analytics/edit-scheme-FIRDebugEnabled.png)

### Android
Android is more simple than iOS. execute Android Emulator or Device and execute below code.

```bash
adb shell setprop debug.firebase.analytics.app <package_name>
```

if you want to stop ```DebugView``` of Firebase Analytics, execute below code.

```bash
adb shell setprop debug.firebase.analytics.app .none.
```

### test
go to ```DebugView``` menu in Firebase Analytics on Firebase Console.

![firebase analytics debugview](/assets/images/category/react-native/react-native-firebase-analytics/firebase-analytics-debugview.png)

we didn't execute any iOS, Android so ```DebugView``` is wait status. now, execute iOS or Android.

![firebase analytics debugview analytics](/assets/images/category/react-native/react-native-firebase-analytics/debugview-analytics.png)

after a while, you can see almost real time analytics results.

## analyze screens
Firebase Analytics has ```screen_view``` Event to analyze what screens users saw.

click ```Events``` menu in ```Analytics``` on Firebase Console. you can see below screen.

![google firebase console Analytics Events menu](/assets/images/category/react-native/react-native-firebase-analytics/analytics-events.png)

select ```screen_view``` in ```Event``` list.

![Firebase Analytics Events screen_view](/assets/images/category/react-native/react-native-firebase-analytics/analytics-events-screen_view.png)

scroll down a little bit, you can see ```User engagement``` > ```Screen class```.

![Firebase Analytics Events screen_view screen class to screen name](/assets/images/category/react-native/react-native-firebase-analytics/screen_view-class-to-name.png)

change ```Screen class``` to ```Screen name``` in User engagement.

![Firebase Analytics Events screen name no data](/assets/images/category/react-native/react-native-firebase-analytics/screen_name-no-data.png)

if you check up to here, you might feel it's not enough. we can see only basic class in ```Screen class``` and there are no data in ```Screen name```, so we can't analyze which screens users have seen more.

so we decided to use ```setCurrentScreen``` in ```react-native-firebase``` feature to analyze screens users have seen.

add below code to screens you want to analyze.

```js
render() {
    firebase.analytics().setCurrentScreen('HOME');
    ...
    return (
        ...
    );
}
```

insert App screen name to ```setCurrentScreen``` of react-native-firebase feature.

and after testing, we can see App screen name which we inserted to ```setCurrentScreen```.

![Firebase Analytics Events screen name with data](/assets/images/category/react-native/react-native-firebase-analytics/screen_name-with-data.png)

you can see real time analytics results in ```DebugView``` on Firebase Analytics.

![Firebase Analytics Events screen name on debug view](/assets/images/category/react-native/react-native-firebase-analytics/screen_name-on-debugview.png)

DebugView에서 해당 이벤트(screen_view)를 선택하면 위와 같이 상세 화면을 볼 수 있습니다.

## analyze Custom Event
we could analyze which screen users have seen more by using ```setCurrentScreen``` but we don't still know what actions users have done in screens. so let's see how to use ```logEvent``` to add Custom Event in Firebase Analytics.

we added below code to analyze Custom Event in Firebase Analytics.

```js
private _onSpeech = (Tts, text: string) => {
    firebase.analytics().logEvent('onPressSoundButton', { target: text });
    ...
}
```

logEvent first parameter only supports 100 english character and underbar(_).(```up to 100 characters is the maximum character length supported for event parameters.```) but our app is multi-language app and we want to know which actions in which languages. so we use second parameter for adding Custom Parameter to Custom Event. second parameter is Object type so we can make any parameters we want.

if you set Custom Parameter to Custom Event like above, you need to add to Firebase Console too.

![Firebase Analytics Events custom event](/assets/images/category/react-native/react-native-firebase-analytics/custom-event-custom-parameter.png)

go to ```Analytics``` > ```Events``` menu, mousehover to Custom Event you added in Event list.

![Firebase Analytics custom parameter menu](/assets/images/category/react-native/react-native-firebase-analytics/custom-parameter-menu.png)

if you mousehover, you can see ```...``` button. click it and select ```Edit parameter reporting```.

![Firebase Analytics custom parameter edit parameter reporting](/assets/images/category/react-native/react-native-firebase-analytics/custom-parameter-edit-parameter-reporting.png)

insert Custom Parameter of Custom Event to searchbar on the left side and click ```ADD``` button to add Custom parameter.

![Firebase Analytics add custom parameter](/assets/images/category/react-native/react-native-firebase-analytics/add-custom-parameter.png)

do test after adding. after some data are accumulating(almost one day), select Custom Event you added in ```Events``` menu.

![Firebase Analytics custom parameter](/assets/images/category/react-native/react-native-firebase-analytics/custom-parameter.png)

scroll down a little bit, you can see Custom Parameter analytics data you added.

![Firebase Analytics custom parameter result](/assets/images/category/react-native/react-native-firebase-analytics/custom-parameter-result.png)

of course, you can see almost real time analytics results in Firebase Analytics ```DebugView```.

![Firebase Analytics Events custom event on debug view](/assets/images/category/react-native/react-native-firebase-analytics/custom_event-on-debugview.png)

if you select Custom Event in DebugView, you can see details with Custom Parameter.

## reference
- firebase debugging event: [https://firebase.google.com/docs/analytics/debugview](https://firebase.google.com/docs/analytics/debugview){:rel="nofollow noreferrer" target="_blank"}
- react-native-firebase: [https://rnfirebase.io/docs/v5.x.x/analytics/reference/analytics](https://rnfirebase.io/docs/v5.x.x/analytics/reference/analytics){:rel="nofollow noreferrer" target="_blank"}