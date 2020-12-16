---
layout: 'post'
permalink: '/react-native/react-native-lottie/'
paginate_path: '/react-native/:num/react-native-lottie/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'use After Effects'
description: let's see how to apply the animation created by Adobe After Effects, to RN(React Native) project.
image: '/assets/images/category/react-native/2019/react-native-lottie/background.jpg'
---

<div id="contents_list" markdown="1">

1. [Outline](#outline)
1. [Installation](#installation)
    - [Upper 0.60](#upper-060)
        - [Connect Library](#connect-library)
    - [Under 0.59](#under-059)
        - [Link Library](#link-library)
1. [How TO Use](#how-to-use)
1. [Animation File with Images](#animation-file-with-images)
    - [Git Repository](#git-repository)
1. [Fix Error](#fix-error)
    - [(0.60 / iOS) ld: warning: Could not find or use auto-linked library](#060--ios-ld-warning-could-not-find-or-use-auto-linked-library)
    - [error: Cycle in dependencies between targets](#error-cycle-in-dependencies-between-targets)
    - [Android Build Error](#android-build-error)
1. [Completed](#completed)
1. [Reference](#reference)autoauto<!-- /TOC -->

</div>

## Outline

recently, many people use Microinteractions to make the app animations. in this blog, we will see how to apply the animation created by Adobe After Effects, to RN(React Native) project by using Airbnb's ```lottie``` library.

- lottie official site: [https://airbnb.design/lottie/](https://airbnb.design/lottie/){:rel="nofollow noreferrer" target="_blank"}

## Installation

execute below command to install ```lottie-react-native``` library to use ```lottie``` library on RN(React Native).

### Upper 0.60

```bash
npm install --save lottie-react-native lottie-ios
```

#### Connect Library

After installing, execute the command below to connect the library on iOS.

```bash
cd ios
pod install
cd ..
```

{% include in-feed-ads.html %}

### Under 0.59

```bash
npm install --save lottie-react-native
```

#### Link Library

after installing ```lottie-react-native``` to use ```lottie``` on RN(React Native), link the library to follow OS specific instruction.

- iOS

execute below command to link ```lottie-react-native``` library to RN(React Native) for using ```lottie``` on iOS.

```bash
react-native link lottie-ios
react-native link lottie-react-native
```

and open ```ios/[project_name].xcodeproj``` or ```ios/[project_name].xcworkspace``` file to execute xcode. and then configure additional settings like below.

![lottie ios additional setting](/assets/images/category/react-native/2019/react-native-lottie/ios-settings.jpg)

1. select the project name on left side menu.
1. select the project name on ```TARGETS```
1. select ```General``` on the top of the screen.
1. scroll down and you can see ```Embedded Binaries``` section. click ```+``` button and search ```Lottie.framework```. select ```ios``` and add.

![lottie ios framework additional settings](/assets/images/category/react-native/2019/react-native-lottie/add-lottie-framework.jpg)

- Android

if you did above ```iOS``` procedure, you don't need to do anything to connect ```lottie``` library for Android. when below command was executed, Android was connected to ```lottie-react-native```.

```bash
react-native link lottie-react-native
```

{% include in-feed-ads.html %}

## How TO Use

we need Adobe After Effects animation file to use lottie on RN(React Native). we won't talk about how to make lottie animation file by Adobe After Effects in this blog. if you want to know how to make lottie animation file by Adobe After Effects, see below link.

- [https://github.com/airbnb/lottie-web](https://github.com/airbnb/lottie-web){:rel="nofollow noreferrer" target="_blank"}

or click below link to search the Microinteractions what you need.

- [https://lottiefiles.com/](https://lottiefiles.com/){:rel="nofollow noreferrer" target="_blank"}

the animation file by Adobe After Effects or you downloaded is ```json``` file type.

below code is how to use lottie on RN(React Native) project for applying Microinteractions

```js
...
import LottieView from 'lottie-react-native';
...
export default class BasicExample extends React.Component {
  render() {
    return (
      <LottieView
        source={require('./animation.json')}
        autoPlay
        loop
      />
    );
  }
}
...
```

## Animation File with Images

when you create the animation using Adobe After Effects, sometimes, you need to export the animation file that includes images.

if you export the animation file that includes images, you can see ```data.json``` like below.

```json
// data.json
{
  ...
  "assets": [
    {
      "id": "image_0",
      "w": 588,
      "h": 792,
      "u": "images/",
      "p": "main_character.jpg",
      "e": 0
    }
  ]
  ...
```

we need to add images in the animation file to the native platforms.

{% include in-feed-ads.html %}

- iOS

execute xcode to select ```ios/[project name].xcworkspace```(or ```ios/xcodeproj```) in RN(React Native) project.

![lottie ios add images](/assets/images/category/react-native/2019/react-native-lottie/lottie_ios_image_add.jpg)

right click ```Resources``` folder below the project name on left side menu, and select ```Add Files to [project name]```

![lottie ios add images - select file](/assets/images/category/react-native/2019/react-native-lottie/lottie_ios_image_add_select_file.jpg)

select image files what you want to add, select ```Copy items if needed``` options on below and add.

if you can't see ```Resources``` folder, right click the project name on left side menu, and select  ```New Group without Folder```. after adding the group, rename it to ```Resources```.

![lottie ios add images - resources add group](/assets/images/category/react-native/2019/react-native-lottie/lottie_ios_image_add_resources_group.jpg)

- Android

Android is more simple than iOS. create the folder that you copy images on ```android/app/src/main/assets``` in RN(React Native) project. in here, I created ```images``` folder. and then, copy images to that folder(```android/app/src/main/assets/images```).

after copying, modify the source code adding ```imageAssetsFolder={'images'}``` like below.

```js
<LottieView
  source={require('./animation.json')}
  autoPlay
  loop
  imageAssetsFolder={'images'}
/>
```

### Git Repository

we created git repository about how to use ```Lottie``` in this case. you can click the link below to check the example.

- git repository: [react_native_lottie_exercise](https://github.com/dev-yakuza/react_native_lottie_exercise){:rel="nofollow noreferrer" target="_blank"}

## Fix Error

### (0.60 / iOS) ld: warning: Could not find or use auto-linked library

When I executed the command below,

```bash
react-native run-ios
```

I got the error message like below.

```bash
ld: warning: Could not find or use auto-linked library ‘swiftCoreFoundation’
ld: warning: Could not find or use auto-linked library ‘swiftCompatibility50’
ld: warning: Could not find or use auto-linked library ‘swiftSwiftOnoneSupport’
ld: warning: Could not find or use auto-linked library ‘swiftObjectiveC’
ld: warning: Could not find or use auto-linked library ‘swiftQuartzCore’
ld: warning: Could not find or use auto-linked library ‘swiftCore’
ld: warning: Could not find or use auto-linked library ‘swiftCoreGraphics’
ld: warning: Could not find or use auto-linked library ‘swiftDispatch’
ld: warning: Could not find or use auto-linked library ‘swiftDarwin’
ld: warning: Could not find or use auto-linked library ‘swiftUIKit’
ld: warning: Could not find or use auto-linked library ‘swiftCompatibilityDynamicReplacements’
ld: warning: Could not find or use auto-linked library ‘swiftCoreImage’
ld: warning: Could not find or use auto-linked library ‘swiftFoundation’
ld: warning: Could not find or use auto-linked library ‘swiftMetal’
```

To solve it, execute `/ios/[project name].xcworkspace` file to open Xcode.

![lottie 0.60, iOS solve build error warning: Could not find or use auto-linked - add new file](/assets/images/category/react-native/2019/react-native-lottie/add-new-file.jpg)

Select `File > New > File...` on the screen like above.

![lottie 0.60, iOS solve build error warning: Could not find or use auto-linked - add Swift file](/assets/images/category/react-native/2019/react-native-lottie/add-swift-file.jpg)

on the screen above, Select `Swift File` and select `Next` button on the right bottom.

![lottie 0.60, iOS solve build error warning: Could not find or use auto-linked - create new file](/assets/images/category/react-native/2019/react-native-lottie/create-new-file.jpg)

Select `Create` button on the create new file screen like above.

![lottie 0.60, iOS solve build error warning: Could not find or use auto-linked - Create Bridging Header](/assets/images/category/react-native/2019/react-native-lottie/create-bridging-header.jpg)

Select `Create Bridging Header` button on the right bottom of the screen like above.

And then, execute the command below to delete the previous project in iOS simulator.

```bash
rm -rf ~/Library/Developer/Xcode/DerivedData/*
```

Lastly, select `Product > Clean Build Folder` on the screen like below.

![lottie 0.60, iOS solve build error warning: Could not find or use auto-linked - Clean Build Folder](/assets/images/category/react-native/2019/react-native-lottie/clean-build-folder.jpg)

Now, execute the command below to excute iOS.

```bash
react-native run-ios
```

{% include in-feed-ads.html %}

### error: Cycle in dependencies between targets

I've used ```react-native-lottie``` well after implementing on RN(React Native), but after installing another library, when I built my RN(React Native) project, I got the error like below.

```bash
Build system information

error: Cycle in dependencies between targets 'LottieLibraryIOS' and 'LottieReactNative'; building could produce unreliable results.
Cycle path: LottieLibraryIOS → LottieReactNative → LottieLibraryIOS
Cycle details:
...
```

I deleted ```Pods``` folder and ```node_modules``` folder, and installed again, but the error was still occured.

below is how to fix the error in my case.  if you have same issue as I have, try to do below.

execute ```ios/[project_name].xcworkspace``` file in RN(React Native) project to open xcode.

![lottie fix build error](/assets/images/category/react-native/2019/react-native-lottie/lottie_fix_error.jpg)

after executing xcode, click ```File > Workspace Settings...``` like above.

![lottie fix build error: change build system](/assets/images/category/react-native/2019/react-native-lottie/change_build_system.jpg)

change the Build System to ```Legacy Build System``` from ```New Build System (Default)```.

in my case, after changing the Build System, I can build successfully. I hope this way is helpful to you.

{% include in-feed-ads.html %}

### Android Build Error

when you build on Android, sometimes, you can see the error like below.

```bash
Execution failed for task ':app:transformClassesWithDexBuilderForDevDebug'.
```

in this case, I modified ```android/app/build.gradle``` file in RN(React Native) project like below.

```xml
android{
    ...
    configurations.all {
        resolutionStrategy {
            force 'com.airbnb.android:lottie:2.5.5'
        }
    }
}
```

- Reference: [Java 8 compilation error version 2.5.6](https://github.com/airbnb/lottie-android/issues/822#issuecomment-401812260){:rel="nofollow noreferrer" target="_blank"}

## Completed

we've done to use lottie on RN(React Native) to show Microinteractions. it's quite simple, isn't it? I think it's more difficult to make the animation than applying it by lottie. I don't know how to use After Effects, so I use [https://lottiefiles.com/](https://lottiefiles.com/){:rel="nofollow noreferrer" target="_blank"} site. I recommend for you to use lottie to use Microinteractions on you project.

## Reference

- lottie official site: [https://airbnb.design/lottie/](https://airbnb.design/lottie/){:rel="nofollow noreferrer" target="_blank"}
