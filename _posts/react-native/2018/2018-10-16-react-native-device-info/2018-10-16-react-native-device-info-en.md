---
layout: 'post'
permalink: '/react-native/react-native-device-info/'
paginate_path: '/react-native/:num/react-native-device-info/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'react-native-device-info'
description: use react-native-device-info for getting user's device informations.
image: '/assets/images/category/react-native/react-native-device-info.jpg'
---

<div id="contents_list" markdown="1">

## Contents

- [outline](#outline)
- [react-native-device-info library installation](#react-native-device-info-library-installation)
- [how to use](#how-to-use)
- [device locale](#device-locale)
- [Unique ID](#unique-id)
- [Device Identification](#device-identification)
- [fix errors](#fix-errors)
- [reference](#reference)

</div>

## outline

we apply [react-native-device-info](https://github.com/rebeccahughes/react-native-device-info){:rel="nofollow noreferrer" target="_blank" } library to RN project for getting user's device informations.

## react-native-device-info library installation

install react-native-device-info with below code.

```bash
npm install --save react-native-device-info
```

finish to install, link react-native-device-info library to the project with below code.

```bash
cd ios
pod install
```

{% include in-feed-ads.html %}

## how to use

we only write a blog post if we have used libraries. so we will add contents to here when we use.

if you want to knwo how to use, see official site.

- official site: [react-native-device-info](https://github.com/rebeccahughes/react-native-device-info){:rel="nofollow noreferrer" target="_blank" }

## Unique ID

the code below is about how to get App's Unique ID.

```js
...
import DeviceInfo from 'react-native-device-info';
...

export default class Home extends React.Component<Props, State> {
    render() {
        const uniqueID = DeviceInfo.getUniqueID();
        // E98948E4-498D-447B-A750-D632C30461A3
        ...
    }
}
```

## Device Identification

if you want to know whether the app is running on the smartphone or tablet, use the code below.

```js
...
import DeviceInfo from 'react-native-device-info';
...

export default class Home extends React.Component<Props, State> {
    render() {
        const isTablet = DeviceInfo.isTablet();
        // tablet: true / phone: false
        ...
    }
}
```

{% include in-feed-ads.html %}

## fix errors

suddenly, occur App crash randomly and show below error message up on the simulator.

```bash
RCTBridge required dispatch_sync to load RCTDevLoadingView. This may lead to deadlocks
```

we've move ```libRNDeviceInfo.a``` to last line and fixed the error.

![RCTBridge required dispatch_sync to load RCTDevLoadingView. error](/assets/images/category/react-native/react-native-device-info/error.jpg)

we referred below link to fix the error.

- [github issue](https://github.com/rebeccahughes/react-native-device-info/issues/260#issuecomment-366835600){:rel="nofollow noreferrer" target="_blank" }

## reference

- official site: [react-native-device-info](https://github.com/rebeccahughes/react-native-device-info){:rel="nofollow noreferrer" target="_blank" }
