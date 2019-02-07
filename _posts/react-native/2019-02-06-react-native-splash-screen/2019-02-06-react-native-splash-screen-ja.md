---
layout: 'post'
permalink: '/react-native/react-native-splash-screen/'
paginate_path: '/react-native/:num/react-native-splash-screen/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'App Splash スクリーン'
description: 'RN(React Native)プロジェクトでreact-native-splash-screenを使ってSplashスクリーンを好きな時間に終了するように作ってみましょう。'
image: '/assets/images/category/react-native/react-native-splash-screen.png'
---


## 概要
RN(React Native)は基本的にSplashスクリーンを提供しています。以前のブログでも紹介しましたが、```generator-rn-toolbox```ツールを使ったら簡単に色んなサイズのSplashイメージを作れます。下のリンクは```generator-rn-toolbox```ツールを使ってSplashイメージを作る方法に関するブログです。

- [Splashイメージ]({{site.url}}/{{page.categories}}/splash-image/){:target="_blank"}

しかし、実際アプリを起動したらSplashスクリーンが早く終了されます。普通のアプリではSplashスクリーンを表示して裏で必要な情報をapiで取ってきてSplashスクリーンを終了してその情報を表示する自然なUXを提供するが、RN(React Native)が基本的に提供してるSplashスクリーンでそうゆう感じのUXを提供することは難しです。

このブログでは```react-native-splash-screen```ライブラリを使ってSplashスクリーンを終了する時点をコントロールして自然なUXを提供するように作ってみます。

- react-native-splash-screen公式サイト: [https://github.com/crazycodeboy/react-native-splash-screen](https://github.com/crazycodeboy/react-native-splash-screen){:rel="nofollow noreferrer" target="_blank"}

## インストール
RN(React Native)でSplashスクリンーんを好きな時終了させるため```react-native-splash-screen```ライブラリを下記のコマンドでインストールします。

```bash
npm install --save react-native-splash-screen
```

## ライブラリ連結
RN(React Native)で```react-native-splash-screen```を使うため下記のコマンドで```react-native-splash-screen```ライブラリとRN(React Native)プロジェクトを連結します。

```bash
react-native link react-native-splash-screen
```

### ライブラリ連結失敗
下記のような場合RN(React Native)に```react-native-splash-screen```を連結する時連結がうまくいかなくって失敗する場合があります。

1. アンドロイドプロジェクトのパッケージ(Package)名を変更した場合。
1. iOSで```Pod```を使ってる場合。

私は両方使ってるので連結する時結構大変でした。上のような場合、連結が失敗する方は下記の方法を使ってみてください。

1. アンドロイドプロジェクトのパッケージ(Package)名を変更した場合。
  アンドロイドパッケージ(Package)名に合わせてフォルダーの構造を変更します。例えば、パッケージ名が```io.github.dev.yakuza.blaboo```の場合、```com/blaboo```であるフォルダーの構造を```io/github/dev/yakuza/blaboo```で変更します。
1. iOSで```Pod```を使う場合。
  私はほとんどのプロジェクトギット(git)で管理したます。下記の方法は(git)を使った場合です。

  下のコマンドで```Pod```を削除します。

  ```bash
  # cd ios
  pod deintegrate
  rm Podfile
  ```

  下記のコマンドで```react-native-splash-screen```ライブラリをインストールしてRN(React Native)プロジェクトへ連結します。

  ```bash
  # React Native root directory
  npm install --save react-native-splash-screen
  react-native link react-native-splash-screen
  ```

  その後、下記のコマンドでギット(git)を使って削除した```Pod```を戻して再インストールします。

  ```bash
  # cd ios
  git checkout -- Podfile
  pod install
  ```

## 使い方
RN(React Native)で```react-native-splash-screen```を使うためには大きくネイティブ(Native)部分とJS部分へソースを追加する必要があります。ネイティブ(Native)部分はアンドロイド、iOSでSplashスクリーンを実行するためで、JS部分はネイティブ(Native)で実行したSplashスクリーンを終了するためです。

### アンドロイド
アンドロイドで```react-native-splash-screen```を使うため```MainActivity.java```ファイルを開いて下記のように修正します。

```java
...
import android.os.Bundle; // here
import com.facebook.react.ReactActivity;
import org.devio.rn.splashscreen.SplashScreen; // here
...
public class MainActivity extends ReactActivity {
   @Override
    protected void onCreate(Bundle savedInstanceState) {
        SplashScreen.show(this);
        super.onCreate(savedInstanceState);
    }
    ...
}
```

また、アンドロイドで使うSplashスクリーンを生成する必要があります。```android/app/src/main/res/layout/launch_screen.xml```ファイルを生成して下記のソースコードを追加します。

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:orientation="vertical" android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@drawable/launch_screen">
</LinearLayout>
```

上部で紹介した```generator-rn-toolbox```([Splashイメージ]({{site.url}}/{{page.categories}}/splash-image/){:target="_blank"})を使っでSplashイメージを生成した場合は```drawable-*```フォルダーに```launch_screen.png```ファイルが生成されます。

したがって上のソースコードをコピペして使っても構いませんが、Splashイメージファイル名が違う場合```android:background="@drawable/launch_screen"```の```launch_screen```部分を生成したイメージファイル名で変更して使ってください。

### iOS
iOSで```react-native-splash-screen```を使えため```AppDelegate.m```ファイルを開いて下記のように修正してください。

```swift
...
#import "RNSplashScreen.h"  // here

@implementation AppDelegate

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
    ...
    [RNSplashScreen show];  // here
    return YES;
}

@end
```

### JS
上で設定したSplashスクリーンを終了させるため下記のようにソースを追加します。

```js
...
import SplashScreen from 'react-native-splash-screen'
...
export default class WelcomePage extends Component {

    componentDidMount() {
    	...
      SplashScreen.hide();
    }
}
```

上のソースを見たら分かりますが```SplashScreen.hide();```を使って好きな時Splashスクリーンを終了させることができます。


## 完了
RN(React Native)でプロジェクトを進める時Splashスクリーンがいつも早くなくなって困りました。```react-native-splash-screen```ライブラリを使った後、Splashスクリーンを自由にコントロールすることが出来てもっと良いUXを作ることができました。

私の場合、ネットワークを使ってないアプリは下記のように強制的に時間を入れてSplashスクリーンをもうちょっと維持しています。

```js
componentDidMount() {
  ...
  setTimeout(() => {
      SplashScreen.hide();
  }, 1000);
}
```

ネットワークを使う場合はネットワークから必要な情報を貰ってSplashスクリーンを終了させています。

皆さんも```react-native-splash-screen```を使ってユーザにもっと良い経験を提供してみてください。


## 参考
- react-native-splash-screen 公式サイト: [https://github.com/crazycodeboy/react-native-splash-screen](https://github.com/crazycodeboy/react-native-splash-screen){:rel="nofollow noreferrer" target="_blank"}