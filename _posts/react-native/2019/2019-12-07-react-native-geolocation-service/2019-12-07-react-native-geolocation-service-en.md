---
layout: 'post'
permalink: '/react-native/react-native-geolocation-service/'
paginate_path: '/react-native/:num/react-native-geolocation-service/'
lang: 'en'
categories: 'react-native'
comments: true

title: Geolocation in React Native
description: Let's see how to get user current geolocation to use react-native-geolocation-service library in React Native.
image: '/assets/images/category/react-native/2019/react-native-geolocation-service/background.jpg'
---

<div id="contents_list" markdown="1">

## Content

1. [Outline](#outline)
1. [How to install react-native-geolocation-service](#how-to-install-react-native-geolocation-service)
1. [Link the library](#link-the-library)
    - [Version >= 0.60](#version--060)
    - [Version <= 0.59](#version--059)
1. [Configure Permission](#configure-permission)
    - [Configure iOS Permission](#configure-ios-permission)
    - [Configure Android Permission](#configure-android-permission)
1. [How to use](#how-to-use)
    - [How to get current geolocation](#how-to-get-current-geolocation)
    - [How to track user geolocation](#how-to-track-user-geolocation)
1. [Completed](#completed)

</div>

## Outline

In this blog post, we'll see how to get current geolocation in React Native. To get location information, we'll use `react-native-geolocation-service` library. You can see the detail about react-native-geolocation-service library via the link below.

- [react-native-geolocation-service](https://github.com/Agontuk/react-native-geolocation-service){:rel="nofollow noreferrer" target="_blank"}

There is a source code about this blog post. If you want to see the source code, check the link below.

- github: [react-native-geolocation-service-example](https://github.com/dev-yakuza/react-native-geolocation-service-example){:target="_blank"}

The example source code is based on the libraries below. If you want to know the details, check the links below.

- [typescript]({{site.url}}/react-native/typescript/){:target="_blank"}
- [styled-components]({{site.url}}/react-native/styled-components/){:target="_blank"}
- [root-import]({{site.url}}/react-native/root-import/){:target="_blank"}

{% include in-feed-ads.html %}

## How to install react-native-geolocation-service

Execute the link below to install react-native-geolocation-service.

```bash
npm install --save react-native-geolocation-service
```

## Link the library

we need to link the library to React Native project.

### Version >= 0.60

Execute the commend below to link the library on iOS.

```bash
cd ios
pod install
```

To use react-native-geolocation-service You need to make iOS project to suppoert Swift. To make Swift supported, execute `ios/[proejct name]xcworkspace` file to open Xcode.

![react-native-geolocation-service enable swift support](/assets/images/category/react-native/2019/react-native-geolocation-service/enable_swift_support_create_file.jpg)


After Xcode is executed, right-click the folder on the top left, and click `New File...` menu.

![react-native-geolocation-service select swift file](/assets/images/category/react-native/2019/react-native-geolocation-service/enable_swift_support_select_swift.jpg)


On the screen above, click `Swift File` and click `Next` on the right bottom.

![react-native-geolocation-service select file name](/assets/images/category/react-native/2019/react-native-geolocation-service/enable_swift_support_create.jpg)


Insert the file name whatever you want, and click `Create` button on the right bottom.

![react-native-geolocation-service select create bridging header](/assets/images/category/react-native/2019/react-native-geolocation-service/enable_swift_support_create_bridging_header.jpg)


On the screen above, click `Create Bridging Header` on the right bottom to make Swift supported.

### Version <= 0.59

If you use React Native version <= 0.59, see the official site links below.

- [Manually link the library on iOS](https://github.com/Agontuk/react-native-geolocation-service#manually-link-the-library-on-ios){:rel="nofollow noreferrer" target="_blank"}
- [Manually link the library on Android](https://github.com/Agontuk/react-native-geolocation-service#android){:rel="nofollow noreferrer" target="_blank"}

## Configure Permission

### Configure iOS Permission

To use the geolocation information on iOS, we need to configure the permissions like below in `ios/[Project Name]/info.plist` file.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  ...
  <key>NSLocationWhenInUseUsageDescription</key>
  <string>Program requires GPS to track cars and job orders</string>
  <key>NSLocationAlwaysUsageDescription</key>
  <string>Program requires GPS to track cars and job orders</string>
  <key>NSLocationAlwaysAndWhenInUseUsageDescription</key>
  <string>Program requires GPS to track cars and job orders</string>
  ...
</dict>
</plist>
```

If your app uses the geolocation on the foreground only, you need to set `NSLocationWhenInUseUsageDescription` only.

If your app needs to get the gelocation on the background, you also need to configure `NSLocationAlwaysUsageDescription` and `NSLocationAlwaysAndWhenInUseUsageDescription`, and set `Location updates` on `Background Modes` like below.

To get the geolocation on the background, open Xcode and click `+ Capability` like below.

![react-native-geolocation-service select capability for location updates background modes](/assets/images/category/react-native/2019/react-native-geolocation-service/select-capability.jpg)

When the `Capability` search screen is shown up, search `Background Modes` and double-click the result to add it.

![react-native-geolocation-service search background modes for location updates background modes](/assets/images/category/react-native/2019/react-native-geolocation-service/search-background-modes.jpg)

After adding `Background Modes`, click `Location updates` on the `Background Modes`.

![react-native-geolocation-service search background modes for location updates background modes](/assets/images/category/react-native/2019/react-native-geolocation-service/add-location-updates.jpg)


After configuration, you should use the code below to get the permission.

```js
import {Platform} from 'react-native';
import Geolocation from 'react-native-geolocation-service';
...
useEffect(() => {
  if (Platform.OS === 'ios') {
    Geolocation.requestAuthorization('always');
  }
}, []);
...
```

### Configure Android Permission

Open `android/app/src/main/AndroidManifest.xml` file and modify it like below to get user location information on Android.

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
  package="com.reactnativegeolocationserviceexample">

    ...
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
    ...

    <application
```

{% include in-feed-ads.html %}

## How to use

we can get the geolocation to use react-native-geolocation library like below.

### How to get current geolocation

The code below is about how to get current geolocation.

```js
Geolocation.getCurrentPosition(
    (position) => {
        console.log(position);
    },
    (error) => {
        // See error code charts below.
        console.log(error.code, error.message);
    },
    { enableHighAccuracy: true, timeout: 15000, maximumAge: 10000 }
);
```

The example below is the full source code about how to get current geolocation.

```js
import React, {useState, useEffect} from 'react';
import Styled from 'styled-components/native';
import Geolocation from 'react-native-geolocation-service';

const Container = Styled.View`
    flex: 1;
    justify-content: center;
    align-items: center;
`;

const Label = Styled.Text`
    font-size: 24px;
`;

interface ILocation {
  latitude: number;
  longitude: number;
}

const CurrentPosition = () => {
  const [location, setLocation] = useState<ILocation | undefined>(undefined);

  useEffect(() => {
    Geolocation.getCurrentPosition(
      position => {
        const {latitude, longitude} = position.coords;
        setLocation({
          latitude,
          longitude,
        });
      },
      error => {
        console.log(error.code, error.message);
      },
      {enableHighAccuracy: true, timeout: 15000, maximumAge: 10000},
    );
  }, []);

  return (
    <Container>
      {location ? (
        <>
          <Label>Latitude: {location.latitude}</Label>
          <Label>Latitude: {location.longitude}</Label>
        </>
      ) : (
        <Label>Loading...</Label>
      )}
    </Container>
  );
};

export default CurrentPosition;
```

You can see the result like below if use the source code above.

![react-native-geolocation-service user current location](/assets/images/category/react-native/2019/react-native-geolocation-service/react-native-geolocation-current-position.jpg)

{% include in-feed-ads.html %}

### How to track user geolocation

We can not only get user current location, but also track user geolocation by react-native-geolocation-service.

The source code below is about how to track user gelocation.

```js
_watchId = Geolocation.watchPosition(
  position => {
    const {latitude, longitude} = position.coords;
    setLocation({latitude, longitude});
  },
  error => {
    console.log(error);
  },
  {
    enableHighAccuracy: true,
    distanceFilter: 0,
    interval: 5000,
    fastestInterval: 2000,
  },
);
```

After tracking, we can stop it by the code below.

```js
if (_watchId !== null) {
  Geolocation.clearWatch(_watchId);
}
```

The example below is the full source code about how to track user geolocation.

```js
import React, {useState, useEffect} from 'react';
import Styled from 'styled-components/native';
import Geolocation from 'react-native-geolocation-service';

const Container = Styled.View`
    flex: 1;
    justify-content: center;
    align-items: center;
`;

const Label = Styled.Text`
    font-size: 24px;
`;

interface ILocation {
  latitude: number;
  longitude: number;
}

const WatchLocation = () => {
  const [location, setLocation] = useState<ILocation | undefined>(undefined);

  useEffect(() => {
    const _watchId = Geolocation.watchPosition(
      position => {
        const {latitude, longitude} = position.coords;
        setLocation({latitude, longitude});
      },
      error => {
        console.log(error);
      },
      {
        enableHighAccuracy: true,
        distanceFilter: 0,
        interval: 5000,
        fastestInterval: 2000,
      },
    );

    return () => {
      if (_watchId) {
        Geolocation.clearWatch(_watchId);
      }
    };
  }, []);

  return (
    <Container>
      {location ? (
        <>
          <Label>Latitude: {location.latitude}</Label>
          <Label>Latitude: {location.longitude}</Label>
        </>
      ) : (
        <Label>Loading...</Label>
      )}
    </Container>
  );
};

export default WatchLocation;
```

You can use the simulator for testing to track user location information. Open `Debug > Location` menu and choose one of `City Run, City Bicycle Ride, Freeway Drive` menu like the screen below. You can see the location changed.

![react-native-geolocation-service tracking user location](/assets/images/category/react-native/2019/react-native-geolocation-service/react-native-geolocation-watch-position.jpg)

## Completed

We've seen how to get user location information by react-native-geolocation-service. Also, we've seen how to track user geolocation by `watchPosition`.
