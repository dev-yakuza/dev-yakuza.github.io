---
layout: 'post'
permalink: '/react-native/react-native-multidex/'
paginate_path: '/react-native/:num/react-native-multidex/'
lang: 'en'
categories: 'react-native'
comments: true

title: Configure Multidex on React Native
description: Let's see how to configure Multidex on Android in React Naitve project.
image: '/assets/images/category/react-native/2020/react-native-multidex/background.jpg'
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [Gradle setting](#gradle-setting)
- [Java setting](#java-setting)
- [Completed](#completed)

</div>

## Outline

Sometimes, the error message below appeared on React Native.

```bash
Cannot fit requested classes in single dex file
```

To solve this error, we need to set Multidex on React Native project. Let's see how to configure Multidex on React Native project.

## Gradle setting

To configure Multidex for Android on React Native project, open `android/app/build.gradle` file and modify it like below.

```js
android {
    defaultConfig {
        ...
        versionName "1.0"
        multiDexEnabled true
    }
    ...
}

dependencies {
  def multidex_version = "2.0.1"
  implementation 'androidx.multidex:multidex:$multidex_version'
}
```

## Java setting

After modifying Gradle file like above, open `MainApplication.java` file and modify it like below.

```java
import androidx.multidex.MultiDexApplication;

public class MainApplication extends MultiDexApplication implements ReactApplication {
  ...
}
```

## Completed

Done! we've seen how to set Multidex on React Native. After configuration, when you execute the command below, you can see the problem is solved.

```bash
npm run android
```

I hope this blog post is helpful for the developers to develop Android project on React Native.
