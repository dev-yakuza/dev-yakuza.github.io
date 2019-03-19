---
layout: 'post'
permalink: '/react-native/react-native-splash-screen/'
paginate_path: '/react-native/:num/react-native-splash-screen/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'App Splash Screen'
description: let's make Splash screen end at the desired time by using react-native-splash-screen on RN(React Native) project.
image: '/assets/images/category/react-native/react-native-splash-screen.jpg'
---


## Outline
basically, RN(React Native) supports Splash screen. I've introduced how to use ```generator-rn-toolbox``` tool to make Splash image in variety of sizes. you can see it to click the link below.

- [Splash image]({{site.url}}/{{page.categories}}/splash-image/){:target="_blank"}

however, when RN(React Native) is executed, Splash screen quickly ends. in normal app UX, Splash screen shows up and get informations via API in background. after getting informations, Splash screen ends and show the screen with informations. but it's difficult to implement it with Splash screen which RN(React Native) supports basically.

in this blog, we'll introduce how to use ```react-native-splash-screen``` library to end Splash screen when you want.

- react-native-splash-screen official site: [https://github.com/crazycodeboy/react-native-splash-screen](https://github.com/crazycodeboy/react-native-splash-screen){:rel="nofollow noreferrer" target="_blank"}

## Installation
execute the command below to install ```react-native-splash-screen```.

```bash
npm install --save react-native-splash-screen
```

## Link Libarary
execute the command below to link ```react-native-splash-screen``` to RN(React Native) project.

```bash
react-native link react-native-splash-screen
```

### Fail To Link Library
if your environment is in the list below, highly, you would fail to link ```react-native-splash-screen``` to RN(React Native).

1. changed the package name in Android project.
1. use ```Pod``` in iOS.

I used both, so it took a long time to link. if you are in the situation above and fail to link, try to do below.

1. if you changed the package name in Android project.
  change the folder structure according to the package name in Android. for example, if the package name is ```io.github.dev.yakuza.blaboo```, change the folder structure from ```com/blaboo``` to ```io/github/dev/yakuza/blaboo```.
1. if you use ```Pod``` in iOS.
  I use the Git to the version control. below is for using the Git.

  execute the command below to remove ```Pod```.

  ```bash
  # cd ios
  pod deintegrate
  rm Podfile
  ```

  execute the command below to install and link ```react-native-splash-screen``` library to RN(React Native).

  ```bash
  # React Native root directory
  npm install --save react-native-splash-screen
  react-native link react-native-splash-screen
  ```

  after that, execute the command below to restore and reinstall ```Pod```.

  ```bash
  # cd ios
  git checkout -- Podfile
  pod install
  ```

## How To Use
we need to add the source code to Native and JS parts to use ```react-native-splash-screen``` on RN(React Native). the Native parts is to start the Splash screen on Android and iOS. JS part is to end the Splash screen.

### Android
open and modify ```MainActivity.java``` file to use ```react-native-splash-screen``` on Android.

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

also, we need to create Splash screen for Android. create ```android/app/src/main/res/layout/launch_screen.xml``` file and add the code below to it.

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:orientation="vertical" android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@drawable/launch_screen">
</LinearLayout>
```

if you used ```generator-rn-toolbox```([Splash Image]({{site.url}}/{{page.categories}}/splash-image/){:target="_blank"}) to generate the Splash images, Splash images were generated named ```launch_screen.png``` in ```darwable-*```.

therefore, you can use above source code but if you have another name splash image file, you should modify ```launch_screen``` part to your file name in ```android:background="@drawable/launch_screen"```.

### iOS
open and modify ```AppDelegate.m``` file to use ```react-native-splash-screen``` o iOS.

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
add the source code below to end Splash screen we set above.

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

I think you already understand what to do. add ```SplashScreen.hide();``` when you want to end Spalsh screen.


## Completed
I had always the problem that Splash screen ended fastly. after I used ```react-native-splash-screen``` library, I can control Splash screen to make good UX.

in my case, if my app doesn't use the network, I add the code below to keep the Splash screen for a while.

```js
componentDidMount() {
  ...
  setTimeout(() => {
      SplashScreen.hide();
  }, 1000);
}
```

if use the network, I end the Splash screen after getting all information via API.

you can use ```react-native-splash-screen``` to make better UX in your app too!


## Reference
- react-native-splash-screen official site: [https://github.com/crazycodeboy/react-native-splash-screen](https://github.com/crazycodeboy/react-native-splash-screen){:rel="nofollow noreferrer" target="_blank"}