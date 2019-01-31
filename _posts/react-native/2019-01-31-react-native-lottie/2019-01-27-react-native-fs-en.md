---
layout: 'post'
permalink: '/react-native/react-native-lottie/'
paginate_path: '/react-native/:num/react-native-lottie/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'use After Effects'
description: let's see how to apply the animation created by Adobe After Effects, to RN(React Native) project.
image: '/assets/images/category/react-native/react-native-lottie.jpg'
---


## Outline
recently, many people use Microinteractions to make the app animations. in this blog, we will see how to apply the animation created by Adobe After Effects, to RN(React Native) project by using Airbnb's ```lottie``` library.

- lottie official site: [https://airbnb.design/lottie/](https://airbnb.design/lottie/){:rel="nofollow noreferrer" target="_blank"}

## Installation
execute below command to install ```lottie-react-native``` library to use ```lottie``` library on RN(React Native).

```bash
npm install --save lottie-react-native
```

## Link Library
after installing ```lottie-react-native``` to use ```lottie``` on RN(React Native), link the library to follow OS specific instruction.

### iOS
execute below command to link ```lottie-react-native``` library to RN(React Native) for using ```lottie``` on iOS.

```bash
react-native link lottie-ios
react-native link lottie-react-native
```

and open ```ios/[project_name].xcodeproj``` or ```ios/[project_name].xcworkspace``` file to execute xcode. and then configure additional settings like below.

![lottie ios additional setting](/assets/images/category/react-native/react-native-lottie/ios-settings.png)

1. select the project name on left side menu.
1. select the project name on ```TARGETS```
1. select ```General``` on the top of the screen.
1. scroll down and you can see ```Embedded Binaries``` section. click ```+``` button and search ```Lottie.framework```. select ```ios``` and add.

![lottie ios framework additional settings](/assets/images/category/react-native/react-native-lottie/add-lottie-framework.png)

### Android
if you did above ```iOS``` procedure, you don't need to do anything to connect ```lottie``` library for Android. when below command was executed, Android was connected to ```lottie-react-native```.

```bash
react-native link lottie-react-native
```

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

## Completed
we've done to use lottie on RN(React Native) to show Microinteractions. it's quite simple, isn't it? I think it's more difficult to make the animation than applying it by lottie. I don't know how to use After Effects, so I use [https://lottiefiles.com/](https://lottiefiles.com/){:rel="nofollow noreferrer" target="_blank"} site. I recommend for you to use lottie to use Microinteractions on you project.


## Reference
- lottie official site: [https://airbnb.design/lottie/](https://airbnb.design/lottie/){:rel="nofollow noreferrer" target="_blank"}