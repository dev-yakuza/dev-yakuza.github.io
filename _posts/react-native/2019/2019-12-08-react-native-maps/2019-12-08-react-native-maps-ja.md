---
layout: 'post'
permalink: '/react-native/react-native-maps/'
paginate_path: '/react-native/:num/react-native-maps/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'React Nativeへ地図を表示する方法'
description: 'react-native-mapsライブラリを使ってReact Nativeへ地図を使う方法について調べてみます。'
image: '/assets/images/category/react-native/2019/react-native-maps/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

1. [概要](#概要)
1. [react-native-mapsインストール](#react-native-mapsインストール)
1. [ライブラリの連結](#ライブラリの連結)
    - [0.60以上](#060以上)
    - [0.59以下](#059以下)
1. [iOSでグーグルマップを使う方法](#iosでグーグルマップを使う方法)
1. [使い方](#使い方)
    - [Appleマップ](#appleマップ)
    - [Googleマップ](#googleマップ)
    - [地図の初期位置設定](#地図の初期位置設定)
    - [地図へマーカー(Marker)を表示](#地図へマーカーmarkerを表示)
    - [地図の位置を追跡する](#地図の位置を追跡する)
    - [ユーザーの現在位置を表示](#ユーザーの現在位置を表示)
    - [ユーザの位置情報の追跡表示](#ユーザの位置情報の追跡表示)
    - [その他の機能](#その他の機能)
1. [完了](#完了)

</div>

## 概要

React Nativeで地図を表示して、現在の位置情報を表示する方法について調べてみようかと思っています。React Nativeで地図をコントロールするためにはReact Nativeコミュニティーの[react-native-maps](https://github.com/react-native-community/react-native-maps){:rel="nofollow noreferrer" target="_blank"}ライブラリを良く使っています。

今回のブログでは`react-native-maps`を使ってReact Nativeで地図を表示して、現在の位置情報を地図の上に表示する方法について調べてみます。

このブログで紹介するソースコードはgithubで確認することができます。。

- github: [react-native-map-example](https://github.com/dev-yakuza/react-native-map-example){:target="_blank"}

例題ソースコードは下記の内容が適用されています。もっと詳しく知りたい方は下記のリンクを参考してください。

- [typescript]({{site.url}}/react-native/typescript/){:target="_blank"}
- [styled-components]({{site.url}}/react-native/styled-components/){:target="_blank"}
- [root-import]({{site.url}}/react-native/root-import/){:target="_blank"}
- [React Nativeで現在位置情報を取得する方法]({{site.url}}/react-native/react-native-geolocation-service/){:target="_blank"}

{% include in-feed-ads.html %}

## react-native-mapsインストール

下記のコマンドでreact-native-mapsをインストールします。

```bash
npm install --save react-native-maps
```

## ライブラリの連結

インストールしたライブラリをReact Nativeプロジェクトに連結する必要があります。

### 0.60以上

下記のコマンドでreact-native-mapsをReact Nativeプロジェクトへ連結します。

```bash
cd ios
pod install
cd ..
```

### 0.59以下

下記のコマンドでreact-native-mapsをReact Nativeプロジェクトへ連結します。

```bash
react-native link react-native-maps
```

手動で連結する方法については公式サイトを参考してください。

- [iOS - Using CocoaPods (React Native 0.59 and lower)](https://github.com/react-native-community/react-native-maps/blob/master/docs/installation.md#using-cocoapods-react-native-059-and-lower){:rel="nofollow noreferrer" target="_blank"}
- [Build configuration on Android](https://github.com/react-native-community/react-native-maps/blob/master/docs/installation.md#build-configuration-on-android){:rel="nofollow noreferrer" target="_blank"}

## iOSでグーグルマップを使う方法

0.60以上のバージョンでは、iOSでグーグルマップを使うため、`ios/[project name]/AppDelegate.m`ファイルを開いて下記のように修正します。

```swift
#import <GoogleMaps/GoogleMaps.h>

@implementation AppDelegate
...

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
+  [GMSServices provideAPIKey:@"_YOUR_API_KEY_"]; // add this line using the api key obtained from Google Console
...
```

そして`ios/Podfile`を開いて下記のように修正します。

```ruby
...
pod 'Folly', :podspec => '../node_modules/react-native/third-party-podspecs/Folly.podspec'

# react-native-maps dependencies
pod 'react-native-maps', path: '../node_modules/react-native-maps'
  pod 'react-native-google-maps', path: '../node_modules/react-native-maps'  # Remove this line if you don't want to support GoogleMaps on iOS
pod 'GoogleMaps'  # Remove this line if you don't want to support GoogleMaps on iOS
pod 'Google-Maps-iOS-Utils' # Remove this line if you don't want to support GoogleMaps on iOS

target 'ReactNativeMapExampleTests' do
...
```

最後に下記のコマンドを実行してiOSに必要なライブラリをインストールします。

```bash
cd ios
pod install
cd ..
```

0.59以下バージョンを使っている方は公式サイトを参考してください。

- [Enabling Google Maps on iOS (React Native all versions)](https://github.com/react-native-community/react-native-maps/blob/master/docs/installation.md#enabling-google-maps-on-ios-react-native-all-versions){:rel="nofollow noreferrer" target="_blank"}

{% include in-feed-ads.html %}

## 使い方

react-native-mapsを使って地図を表示したいところに下記のように修正します。

### Appleマップ

Appleマップを使って地図を表示するためには、下記のように修正します。

```js
{% raw %}
import React from 'react';
import Styled from 'styled-components/native';
import MapView from 'react-native-maps';

const Container = Styled.View`
    flex: 1;
`;

const AppleMap = () => {
  return (
    <Container>
      <MapView style={{flex: 1}} />
    </Container>
  );
};

export default AppleMap;
{% endraw %}
```

下記のコマンドでReact Nativeを実行すると

```bash
npm run ios
# android
# npm run android
```

下記のような結果画面を見ることができます。

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2019/react-native-maps/apple-map.jpg" alt="React Nativeでreact-native-mapsを使って地図を表示する - Appleマップ">
</div>

### Googleマップ

グーグルマップを使うためには下記のように修正します。

```js
{% raw %}
import React from 'react';
import Styled from 'styled-components/native';
import MapView, {PROVIDER_GOOGLE} from 'react-native-maps';

const Container = Styled.View`
    flex: 1;
`;

const GoogleMap = () => {
  return (
    <Container>
      <MapView style={{flex: 1}} provider={PROVIDER_GOOGLE} />
    </Container>
  );
};

export default GoogleMap;
{% endraw %}
```

下記のコマンドでReact Nativeプロジェクトを実行すると

```bash
npm run ios
# android
# npm run android
```

下記のような結果画面を見ることができます。

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2019/react-native-maps/google-map.jpg" alt="React Nativeでreact-native-mapsを使って地図を表示する - Google マップ">
</div>

(ここでグーグルマップが表示されない理由は、例題にある`provideAPIKey`を使ったためです。皆さんが正しいprovideAPIKeyを使うとグーグルマップが表示されることが確認できます。)

{% include in-feed-ads.html %}

### 地図の初期位置設定

下記のように修正すると、地図の初期位置を設定することができます。

```js
{% raw %}
import React from 'react';
import Styled from 'styled-components/native';
import MapView from 'react-native-maps';

const Container = Styled.View`
    flex: 1;
`;

const InitialLocation = () => {
  return (
    <Container>
      <MapView
        style={{flex: 1}}
        initialRegion={{
          latitude: 37.78825,
          longitude: -122.4324,
          latitudeDelta: 0.0922,
          longitudeDelta: 0.0421,
        }}
      />
    </Container>
  );
};

export default InitialLocation;
{% endraw %}
```

### 地図へマーカー(Marker)を表示

下記のように修正すると、地図の上にマーカー(Marker)を表示することができます。

```js
{% raw %}
import React from 'react';
import Styled from 'styled-components/native';
import MapView, {Marker} from 'react-native-maps';

const Container = Styled.View`
    flex: 1;
`;

const MarkerOnMap = () => {
  return (
    <Container>
      <MapView
        style={{flex: 1}}
        initialRegion={{
          latitude: 37.78825,
          longitude: -122.4324,
          latitudeDelta: 0.0922,
          longitudeDelta: 0.0421,
        }}>
        <Marker
          coordinate={{latitude: 37.78825, longitude: -122.4324}}
          title="this is a marker"
          description="this is a marker example"
        />
      </MapView>
    </Container>
  );
};

export default MarkerOnMap;
{% endraw %}
```

{% include in-feed-ads.html %}

### 地図の位置を追跡する

MapViewの`onRegionChange`と`onRegionChangeComplete`を使えば、地図の位置が変更されたことを追跡できます。

```js
{% raw %}
<MapView
  onRegionChange={region => {
    setLocation({
      latitude: region.latitude,
      longitude: region.longitude,
    });
  }}
  onRegionChangeComplete={region => {
    setLocation({
      latitude: region.latitude,
      longitude: region.longitude,
    });
  }}
>
{% endraw %}
```

下記のソースコードは、ユーザが地図の初期位置から他のところに移動させる時、当該位置を追跡（トラッキング）して地図のセンターへマーカーを表示する方法です。

```js
{% raw %}
import React, {useState} from 'react';
import Styled from 'styled-components/native';
import MapView, {Marker} from 'react-native-maps';

const Container = Styled.View`
    flex: 1;
`;

interface IGeolocation {
  latitude: number;
  longitude: number;
}

const TrackingMapWithMarker = () => {
  const [location, setLocation] = useState<IGeolocation>({
    latitude: 37.78825,
    longitude: -122.4324,
  });
  return (
    <Container>
      <MapView
        style={{flex: 1}}
        initialRegion={{
          latitude: location.latitude,
          longitude: location.longitude,
          latitudeDelta: 0.0922,
          longitudeDelta: 0.0421,
        }}
        onRegionChange={region => {
          setLocation({
            latitude: region.latitude,
            longitude: region.longitude,
          });
        }}
        onRegionChangeComplete={region => {
          setLocation({
            latitude: region.latitude,
            longitude: region.longitude,
          });
        }}>
        <Marker
          coordinate={{
            latitude: location.latitude,
            longitude: location.longitude,
          }}
          title="this is a marker"
          description="this is a marker example"
        />
      </MapView>
    </Container>
  );
};

export default TrackingMapWithMarker;
{% endraw %}
```

{% include in-feed-ads.html %}

### ユーザーの現在位置を表示

ユーザの現在位置を表示するためには、ユーザの現在位置を取得する必要があります。ユーザの現在位置を取得する方法については下記のブログを参考してください。

- [React Nativeで現在位置情報を取得する方法]({{site.url}}/react-native/react-native-geolocation-service/){:target="_blank"}

このように取ってきたユーザデータを表示するため下記のソースコードを使います。

```js
{% raw %}
import React, {useState, useEffect} from 'react';
import Styled from 'styled-components/native';
import MapView, {Marker} from 'react-native-maps';
import Geolocation from 'react-native-geolocation-service';

const Container = Styled.View`
    flex: 1;
`;

interface ILocation {
  latitude: number;
  longitude: number;
}

const UserLocation = () => {
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
      {location && (
        <MapView
          style={{flex: 1}}
          initialRegion={{
            latitude: location.latitude,
            longitude: location.longitude,
            latitudeDelta: 0.0922,
            longitudeDelta: 0.0421,
          }}>
          <Marker
            coordinate={{
              latitude: location.latitude,
              longitude: location.longitude,
            }}
          />
        </MapView>
      )}
    </Container>
  );
};

export default UserLocation;
{% endraw %}
```

結果画面は下記のようです。

![react-native-maps ユーザの現在位置](/assets/images/category/react-native/2019/react-native-maps/user-location.jpg)

{% include in-feed-ads.html %}

### ユーザの位置情報の追跡表示

位置情報ライブラリである`react-native-geolocation-service`を使うと、ユーザの位置情報を追跡することができます。`react-native-geolocation-service`ライブラリに関しては下記のリンクを参考してください。

- [React Nativeで現在位置情報を取得する方法]({{site.url}}/react-native/react-native-geolocation-service/){:target="_blank"}

ユーザの位置情報を追跡してマーカー(Marker)を表示する例題は下記のようです。

```js
{% raw %}
import React, {useState, useEffect} from 'react';
import Styled from 'styled-components/native';
import MapView, {Marker} from 'react-native-maps';
import Geolocation from 'react-native-geolocation-service';

const Container = Styled.View`
    flex: 1;
`;

interface ILocation {
  latitude: number;
  longitude: number;
}

const TrackUserLocation = () => {
  const [locations, setLocations] = useState<Array<ILocation>>([]);
  let _watchId: number;

  useEffect(() => {
    _watchId = Geolocation.watchPosition(
      position => {
        const {latitude, longitude} = position.coords;
        setLocations([...locations, {latitude, longitude}]);
      },
      error => {
        console.log(error);
      },
      {
        enableHighAccuracy: true,
        distanceFilter: 100,
        interval: 5000,
        fastestInterval: 2000,
      },
    );
  }, [locations]);

  useEffect(() => {
    return () => {
      if (_watchId !== null) {
        Geolocation.clearWatch(_watchId);
      }
    };
  }, []);

  return (
    <Container>
      {locations.length > 0 && (
        <MapView
          style={{flex: 1}}
          initialRegion={{
            latitude: locations[0].latitude,
            longitude: locations[0].longitude,
            latitudeDelta: 0.0922,
            longitudeDelta: 0.0421,
          }}>
          {locations.map((location: ILocation, index: number) => (
            <Marker
              key={`location-${index}`}
              coordinate={{
                latitude: location.latitude,
                longitude: location.longitude,
              }}
            />
          ))}
        </MapView>
      )}
    </Container>
  );
};

export default TrackUserLocation;
{% endraw %}
```

ユーザの位置追跡の結果画面は下記のようです。

![react-native-maps ユーザ位置情報追跡](/assets/images/category/react-native/2019/react-native-maps/track-user-location.jpg)

{% include in-feed-ads.html %}

### その他の機能

地図の初期位置設定やマーカー(Marker)表示以外にも沢山の機能を提供しています。下記のリンクで公式サイトを参考してください。

- [Rendering a Marker with a custom view](https://github.com/react-native-community/react-native-maps#rendering-a-marker-with-a-custom-view){:rel="nofollow noreferrer" target="_blank"}
- [Rendering a Marker with a custom image](https://github.com/react-native-community/react-native-maps#rendering-a-marker-with-a-custom-image){:rel="nofollow noreferrer" target="_blank"}
- [Rendering a custom Marker with a custom Callout](https://github.com/react-native-community/react-native-maps#rendering-a-custom-marker-with-a-custom-callout){:rel="nofollow noreferrer" target="_blank"}
- [Draggable Markers](https://github.com/react-native-community/react-native-maps#draggable-markers){:rel="nofollow noreferrer" target="_blank"}
- [Using a custom Tile Overlay](https://github.com/react-native-community/react-native-maps#using-a-custom-tile-overlay){:rel="nofollow noreferrer" target="_blank"}
- [Overlaying other components on the map](https://github.com/react-native-community/react-native-maps#overlaying-other-components-on-the-map){:rel="nofollow noreferrer" target="_blank"}
- [Customizing the map style](https://github.com/react-native-community/react-native-maps#customizing-the-map-style){:rel="nofollow noreferrer" target="_blank"}
- [Animated Region](https://github.com/react-native-community/react-native-maps#animated-region){:rel="nofollow noreferrer" target="_blank"}
- [Animated Marker Position](https://github.com/react-native-community/react-native-maps#animated-marker-position){:rel="nofollow noreferrer" target="_blank"}
- [Take Snapshot of map](https://github.com/react-native-community/react-native-maps#take-snapshot-of-map){:rel="nofollow noreferrer" target="_blank"}
- [Zoom to Specified Markers](https://github.com/react-native-community/react-native-maps#zoom-to-specified-markers){:rel="nofollow noreferrer" target="_blank"}

## 完了

これでReact Nativeで地図を表示する方法についてみてみました。このライブラリを使うと地図の上にマーカーを表示するだけではなく、ポリゴン(Polygon)やポリライン(Polyline)も表示することができます。

地図を持ってるサービスを準備中である方はこのライブラリを使ってみることをおすすめします。
