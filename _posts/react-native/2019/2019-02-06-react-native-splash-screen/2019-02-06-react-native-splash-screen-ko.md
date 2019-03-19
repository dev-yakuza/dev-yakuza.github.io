---
layout: 'post'
permalink: '/react-native/react-native-splash-screen/'
paginate_path: '/react-native/:num/react-native-splash-screen/'
lang: 'ko'
categories: 'react-native'
comments: true

title: 'App Splash 스크린'
description: 'RN(React Native) 프로젝트에서 react-native-splash-screen를 사용하여 Splash 스크린을 원하는 시간에 종료하도록 만들어 보자.'
image: '/assets/images/category/react-native/react-native-splash-screen.jpg'
---


## 개요
RN(React Native)는 기본적으로 Splash 스크린을 제공합니다. 이전 블로그에서도 소개해 드렸지만 ```generator-rn-toolbox``` 툴을 이용하면 간단하게 다양한 크기에 Splash 이미지를 만들 수 있습니다. 아래에 링크는 ```generator-rn-toolbox``` 툴를 사용하여 Splash 이미지를 만드는 방법에 관한 블로그입니다.

- [Splash 이미지]({{site.url}}/{{page.categories}}/splash-image/){:target="_blank"}

하지만 실제 앱을 구동하면 Splash 스크린이 너무 빨리 종료됩니다. 보통의 앱에서는 Splash 스크린을 표시하고 뒤에서 필요한 정보를 api를 통해 받아 온 후 Splash 스크린을 종료하여 자연스러운 사용자 경험을 제공하지만 RN(React Native)에서 기본으로 제공하는 Splash 스크린은 그런 사용자 경험을 제공하기 어렵습니다.

이번 블로그에서는 ```react-native-splash-screen``` 라이브러리를 사용하여 Splash 스크린 종료 시점을 조절하여 부드러운 사용자 경험을 제공하도록 만들어 보겠습니다.

- react-native-splash-screen 공식 사이트: [https://github.com/crazycodeboy/react-native-splash-screen](https://github.com/crazycodeboy/react-native-splash-screen){:rel="nofollow noreferrer" target="_blank"}

## 설치
RN(React Native)에서 Splash 스크린을 원하는 시점에 종료하기 위해 ```react-native-splash-screen``` 라이브러리를 아래에 명령어를 통해 설치합니다.

```bash
npm install --save react-native-splash-screen
```

## 라이브러리 연결
RN(React Native)에서 ```react-native-splash-screen```를 사용하기 위해 아래에 명령어로 ```react-native-splash-screen``` 라이브러리와 RN(React Native) 프로젝트를 연결합니다.

```bash
react-native link react-native-splash-screen
```

### 라이브러리 연결 실패
아래와 같은 경우 RN(React Native)에 ```react-native-splash-screen```을 연결할 때 연결이 실패하는 경우가 발생합니다.

1. 안드로이드 프로젝트에서 패키지(Package) 명을 변경한 경우.
1. iOS에서 ```Pod```를 사용한 경우.

저는 둘 다 사용하고 있어 연결하는데 꾀 많은 시간을 사용했습니다. 위와 같은 상황에서 연결에 실패하시는 분은 아래에 방법을 사용해 보시기 바랍니다.

1. 안드로이드 프로젝트에서 패키지(Package) 명을 변경한 경우.
  안드로이드 패키지(Package) 명에 맞춰 폴더 구조를 변경합니다. 예를 들어 패키지명이 ```io.github.dev.yakuza.blaboo```인 경우 ```com/blaboo```로 되어있는 폴더 구조를 ```io/github/dev/yakuza/blaboo```로 변경하시기 바랍니다.
1. iOS에서 ```Pod```를 사용한 경우.
  저는 대부분의 프로젝트를 깃(git)으로 관리하고 있습니다. 아래에 방법은 깃(git)을 사용하는 경우에 해당합니다.

  아래에 명령어로 ```Pod``` 제거합니다.

  ```bash
  # cd ios
  pod deintegrate
  rm Podfile
  ```

  아래에 명령어로 ```react-native-splash-screen``` 라이브러리를 설치하고 RN(React Native) 프로젝트에 연결합니다.

  ```bash
  # React Native root directory
  npm install --save react-native-splash-screen
  react-native link react-native-splash-screen
  ```

  그런 다음 아래에 명령어를 통해 깃(git)을 통해 삭제한 ```Pod```을 되돌린 후 다시 설치합니다.

  ```bash
  # cd ios
  git checkout -- Podfile
  pod install
  ```

## 사용 방법
RN(React Native)에서 ```react-native-splash-screen```를 사용하기 위해서는 크게 네이티브(Native) 부분과 JS부분에 소스를 추가해야 합니다. 네이티브(Native) 부분은 안드로이드, iOS에서 Splash 스크린을 실행시키기 위한 부분이며 JS 부분은 네이티브(Native)에서 실행한 Splash 스크린을 종료시키기 위한 처리입니다.

### 안드로이드
안드로이드에서 ```react-native-splash-screen```를 사용하기 위해서 ```MainActivity.java``` 파일을 열고 아래와 같이 수정합니다.

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

또한 안드로이드에서 사용할 Splash 스크린을 생성해야 합니다. ```android/app/src/main/res/layout/launch_screen.xml``` 파일을 생성하고 아래와 같이 소스를 추가합니다.

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:orientation="vertical" android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@drawable/launch_screen">
</LinearLayout>
```

위에서 소개한 ```generator-rn-toolbox```([Splash 이미지]({{site.url}}/{{page.categories}}/splash-image/){:target="_blank"})을 사용하여 Splash 이미지를 생성한 경우 ```drawable-*``` 폴더에 ```launch_screen.png``` 파일들이 생성됩니다.

따라서 위에 코드를 그대로 사용하셔도 되지만 Splash 이미지 파일명이 다른 경우 ```android:background="@drawable/launch_screen"```의 ```launch_screen```부분을 생성하신 이미지 파일명으로 고쳐서 사용하시기 바랍니다.

### iOS
iOS에서 ```react-native-splash-screen```를 사용하기 위해서 ```AppDelegate.m``` 파일을 열고 아래와 같이 수정합니다.

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
위에서 설정한 Splash 스크린을 종료시키기 위해 아래와 같이 소스를 추가합니다.

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

위에서도 알 수 있듯이 ```SplashScreen.hide();```를 사용하면 원하는 시점에 Splash 스크린을 종료시킬 수 있습니다.


## 완료
RN(React Native)로 프로젝트를 진행할 때 Splash 스크린이 항상 빨리 없어져서 문제가 되었습니다. ```react-native-splash-screen``` 라이브러리를 사용한 후, Splash 스크린을 자유롭게 조절할 수 있어 좀 더 좋은 사용자 경험을 줄 수 있게 되었습니다.

저는 네트워크를 사용하지 않는 앱인 경우 아래와 같이 강제적으로 시간을 주어서 좀 더 Splash 스크린을 유지하고 있습니다.

```js
componentDidMount() {
  ...
  setTimeout(() => {
      SplashScreen.hide();
  }, 1000);
}
```

네트워크를 사용하는 경우는 네트워크를 통해 정보를 다 받아온 후 Splash 스크린을 종료하고 있습니다.

여러분도 ```react-native-splash-screen```을 사용하여 사용자에게 좀 더 나은 경험을 제공해 보시기 바랍니다.


## 참고
- react-native-splash-screen 공식 사이트: [https://github.com/crazycodeboy/react-native-splash-screen](https://github.com/crazycodeboy/react-native-splash-screen){:rel="nofollow noreferrer" target="_blank"}