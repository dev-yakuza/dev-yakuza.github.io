---
layout: 'post'
permalink: '/react-native/react-native-status-bar/'
paginate_path: '/react-native/:num/react-native-status-bar/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'Control StatusBar'
description: let's see how to control the StatusBar in RN(React Native)
image: '/assets/images/category/react-native/react-native-status-bar/background.jpg'
---


## Outline
Recently, when I developed the app, I needed to control the StatusBar. in this blog, I'll introduce how to handle the StatusBar in RN(React Native).


## Splash Screen
I use ```react-native-splash-screen``` to handle the Splash screen in RN(React Native). if you want to know more details about how to use ```react-native-splash-screen```, see the blog below.

- [App Splash screen]({{site.url}}/{{page.categories}}/react-native-splash-screen/){:target="_blank"}

if we don't configure anything, the StatusBar will show up on the Splash screen. we can configure the settings below to hide the StatusBar on the Splash screen.

### iOS
modify ```info.plist``` to hide the StatusBar on the Splash screen.

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

### Android
modify ```MainActivity.java``` to hide the StatusBar on the Splash screen.

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

also, modify ```res/values/styles.xml``` like below.

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

### Android Transparent StatusBar
we need to modify the ```js``` level source code to make the StatusBar transparent. modify the component source code in where you want to hide the StatusBar like below.

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
to make the StatusBar transparent, use ```backgroundColor={'transparent'}``` and ```translucent={true}``` options in StatusBar component of RN(React Native) like above.


## Completed
we've talked abouht how to handle the StatusBar in RN(React Native). if I use other way except the way above, I'll add the contents to this blog.
