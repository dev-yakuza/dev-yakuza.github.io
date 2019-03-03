---
layout: 'post'
permalink: '/react-native/react-native-status-bar/'
paginate_path: '/react-native/:num/react-native-status-bar/'
lang: 'ko'
categories: 'react-native'
comments: true

title: 'StatusBar 다루기'
description: 'RN(React Native)에서 StatusBar를 다루는 방법에 대해서 설명합니다.'
image: '/assets/images/category/react-native/react-native-status-bar/background.jpg'
---


## 개요
최근 앱을 개발할 때, StatusBar를 다루게 되었습니다. 이 블로그에서는 RN(React Native)에서 StatusBar를 다루는 방법에 대해서 정리합니다.


## Splash 스크린
저는 RN(React Native)에서 Splash 스크린을 다루기 위해 ```react-native-splash-screen```을 사용하고 있습니다. ```react-native-splash-screen```에 대한 자세한 내용은 아래의 블로그를 참고하시기 바랍니다.

- [App Splash 스크린]({{site.url}}/{{page.categories}}/react-native-splash-screen/){:target="_blank"}

아무 설정도 하지 않은 경우, Splash 스크린이 표시될 때, StatusBar가 표시됩니다. 아래와 같이 설정하여 Splash 스크린에서 StatusBar가 표시되지 않게 할 수 있습니다.

### iOS
Splash 스크린에서 StatusBar를 감추기 위해, ```info.plist```를 아래와 같이 수정합니다.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    ...
    <key>UIStatusBarHidden</key>
	<true/>
	<key>UIViewControllerBasedStatusBarAppearance</key>
	<false/>
    ...
</dict>
</plist>
```

### 안드로이드
안드로이드에서 Splash 스크린이 표시될 때, StatusBar를 을 감추기 위해서는 아래와 같이 ```MainActivity.java```를 수정합니다.

```java
...
public class MainActivity extends ReactActivity {
...
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        SplashScreen.show(this, true);
        super.onCreate(savedInstanceState);
    }
...
}
```

또한, ```res/values/styles.xml```을 아래와 같이 수정합니다.

```xml
<resources>
    <style name="AppTheme" parent="Theme.AppCompat.NoActionBar">
        <item name="android:windowExitAnimation">@android:anim/fade_out</item>
        <item name="android:windowFullscreen">true</item>
        <item name="windowActionBar">false</item>
        <item name="windowNoTitle">true</item>
    </style>
</resources>
```

### 안드로이드에서 투명 StatusBar
안드로이드에서 StatusBar를 투명하게 만들기 위해서는 ```js``` 레벨에서 소스를 수정해야합니다. StatusBar를 투명하게 만들고자 하는 컴포넌트(Component)에서 아래와 같이 소스를 수정합니다.

```js
...
import {
  ...
  StatusBar,
} from 'react-native';
...
export default class Story extends React.Component<Props, State> {
    ...
    render() {
        ...
        return (
            <React.Fragment>
                <StatusBar barStyle="dark-content" backgroundColor={'transparent'} translucent={true} />
                ...
            </React.Fragment>
        );
    }
    ...
}
```

위와 같이 RN(React Native)의 StatusBar를 사용하여 ```backgroundColor={'transparent'}```와 ```translucent={true}```를 설정하면 투명 배경의 StatusBar를 사용할 수 있습니다.


## 완료
지금까지 RN(React Native)를 사용하여 개발한 앱내에서 StatusBar를 다루는 방법에 대해서 알아보았습니다. 위에서 알아본 내용 이외에도 StatusBar를 다루게 된다면 이 블로그에 추가하도록 하겠습니다.
