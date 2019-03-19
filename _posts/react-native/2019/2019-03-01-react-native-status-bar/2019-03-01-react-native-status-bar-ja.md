---
layout: 'post'
permalink: '/react-native/react-native-status-bar/'
paginate_path: '/react-native/:num/react-native-status-bar/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'StatusBarコントロール'
description: 'RN(React Native)でStatusBarをコントロールする方法について説明します。'
image: '/assets/images/category/react-native/react-native-status-bar/background.jpg'
---


## 概要
最近アプリを開発する時、StatusBarをコントロールする時がありました。このブログでRN(React Native)のアプリでStatusBarをコントロールする方法をまとめます。


## Splashスクリーン
私はRN(React Native)でSplashスクリーンを使うため```react-native-splash-screen```を使ってます。```react-native-splash-screen```について詳しく内容は下記のブログを参考してください。

- [App Splashスクリーン]({{site.url}}/{{page.categories}}/react-native-splash-screen/){:target="_blank"}

何にも設定しないと、Splashスクリーンが表示される時、StatusBarが表示します。下記のように設定するとSplashスクリーンでStatusBarを非表示することができます。

### iOS
SplashスクリーンでStatusBarを日表示するため、```info.plist```を開いて下記のように修正します。

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

### アンドロイド
アンドロイドでSplashスクリーンが表示される時、StatusBarを非表示するためは下記のように```MainActivity.java```を修正します。

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

また、```res/values/styles.xml```を下記のように修正します。

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

### アンドロイドで透明StatusBar
アンドロイドでStatusBarを透明にするためには```js```レベルでソースコードを修正する必要があります。StatusBarを透明にしたいコンポーネント(Component)に下記のようにソースコードを修正します。

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

上のようにRN(React Native)のStatusBarを使って```backgroundColor={'transparent'}```と```translucent={true}```を設定したら透明なStatusBarを使えることができます。


## 完了
今までRN(React Native)を使って開発したアプリ内でStatusBarをコントロールする方法について説明します。上部で調べた内容以外にStatusBarをコントロールしたらこのブログに追加します。
