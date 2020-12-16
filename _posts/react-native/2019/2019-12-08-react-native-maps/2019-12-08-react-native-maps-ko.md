---
layout: 'post'
permalink: '/react-native/react-native-maps/'
paginate_path: '/react-native/:num/react-native-maps/'
lang: 'ko'
categories: 'react-native'
comments: true

title: 'React Native에서 지도 표시하기'
description: 'react-native-maps 라이브러리를 이용하여 React Native에서 지도를 사용하는 방법에 대해서 알아봅시다.'
image: '/assets/images/category/react-native/2019/react-native-maps/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

1. [개요](#개요)
1. [react-native-maps 설치](#react-native-maps-설치)
1. [라이브러리 연결](#라이브러리-연결)
    - [0.60 이상](#060-이상)
    - [0.59 이하](#059-이하)
1. [iOS에서 구글맵 사용 설정](#ios에서-구글맵-사용-설정)
1. [사용법](#사용법)
    - [애플 맵](#애플-맵)
    - [구글 맵](#구글-맵)
    - [지도의 초기 위치 설정](#지도의-초기-위치-설정)
    - [지도의 마커(Marker) 표시](#지도의-마커marker-표시)
    - [지도 위치 추적하기](#지도-위치-추적하기)
    - [사용자의 현재 위치 표시](#사용자의-현재-위치-표시)
    - [사용자 위치 추적 표시](#사용자-위치-추적-표시)
    - [그밖에 기능들](#그밖에-기능들)
1. [네이버 지도](#네이버-지도)
1. [완료](#완료)

</div>

## 개요

React Native에서 지도를 표시하고 현재 위치를 표시하는 방법에 대해서 알아보려고 합니다. React Native에서 지도를 다루기 위해서는 React Native 커뮤니케이션의 [react-native-maps](https://github.com/react-native-community/react-native-maps){:rel="nofollow noreferrer" target="_blank"} 라이브러리를 많이 사용합니다.

이번 블로그에서는 `react-native-maps`를 통해 React Native에 지도를 표시하고 현재 위치를 가져와 지도 위에 표시하는 방법에 대해서 알아봅니다.

이 블로그 포스트에서 소개 되는 소스코드는 github에서 확인할 수 있습니다.

- github: [react-native-map-example](https://github.com/dev-yakuza/react-native-map-example){:target="_blank"}

예제 소스코드는 아래에 내용이 적용되어 있으니, 궁금하신 분들은 아래에 내용도 참고하시기 바랍니다.

- [typescript]({{site.url}}/react-native/typescript/){:target="_blank"}
- [styled-components]({{site.url}}/react-native/styled-components/){:target="_blank"}
- [root-import]({{site.url}}/react-native/root-import/){:target="_blank"}
- [React Native에서 현재 위치 정보 가져오기]({{site.url}}/react-native/react-native-geolocation-service/){:target="_blank"}

{% include in-feed-ads.html %}

## react-native-maps 설치

아래에 명령어를 사용하여 react-native-maps를 설치합니다.

```bash
npm install --save react-native-maps
```

## 라이브러리 연결

설치한 라이브러리를 React Native 프로젝트에 연결할 필요가 있습니다.

### 0.60 이상

아래에 명령어로 react-native-maps를 React Native 프로젝트에 연결합니다.

```bash
cd ios
pod install
cd ..
```

### 0.59 이하

아래에 명령어로 react-native-maps를 React Native 프로젝트에 연결합니다.

```bash
react-native link react-native-maps
```

수동 연결에 관해서는 공식 사이트를 참고하시기 바랍니다.

- [iOS - Using CocoaPods (React Native 0.59 and lower)](https://github.com/react-native-community/react-native-maps/blob/master/docs/installation.md#using-cocoapods-react-native-059-and-lower){:rel="nofollow noreferrer" target="_blank"}
- [Build configuration on Android](https://github.com/react-native-community/react-native-maps/blob/master/docs/installation.md#build-configuration-on-android){:rel="nofollow noreferrer" target="_blank"}

## iOS에서 구글맵 사용 설정

0.60 버전에서 구글 맵을 사용하기 위해, `ios/[project name]/AppDelegate.m` 파일을 열고 아래와 같이 수정합니다.

```swift
#import <GoogleMaps/GoogleMaps.h>

@implementation AppDelegate
...

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
+  [GMSServices provideAPIKey:@"_YOUR_API_KEY_"]; // add this line using the api key obtained from Google Console
...
```

그리고 `ios/Podfile`을 열고 아래와 같이 수정합니다.

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

마지막으로 아래에 명령어를 실행하여 iOS에 필요한 라이브러리를 설치합니다.

```bash
cd ios
pod install
cd ..
```

0.59 이하 버전을 사용하시는 분들은 공식 사이트를 참고하시기 바랍니다.

- [Enabling Google Maps on iOS (React Native all versions)](https://github.com/react-native-community/react-native-maps/blob/master/docs/installation.md#enabling-google-maps-on-ios-react-native-all-versions){:rel="nofollow noreferrer" target="_blank"}

{% include in-feed-ads.html %}

## 사용법

react-native-maps을 이용하여 지도를 표시하고 싶은 부분에 아래와 같이 수정합니다.

### 애플 맵

애플 맵을 사용하여 지도를 표시하기 위해서는 아래와 같이 수정합니다.

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

아래에 명령어로 React Native 프로젝트를 실행하면

```bash
npm run ios
# android
# npm run android
```

아래와 같은 결과 화면을 볼 수 있습니다.

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2019/react-native-maps/apple-map.jpg" alt="React Native에서 react-native-maps을 사용하여 지도 표시하기 - 애플 맵">
</div>

### 구글 맵

구글 맵을 사용하기 위해서는 아래와 같이 수정합니다.

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

아래에 명령어로 React Native 프로젝트를 실행하면

```bash
npm run ios
# android
# npm run android
```

아래와 같은 결과 화면을 볼 수 있습니다.

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2019/react-native-maps/google-map.jpg" alt="React Native에서 react-native-maps을 사용하여 지도 표시하기 - 구글 맵">
</div>

(여기 구글 맵이 표시되지 않는 이유는, 예제에 있는 `provideAPIKey`를 사용했기 때문입니다. 여러분이 정확한 provideAPIKey를 사용하신다면 구글 맵이 표시되는 것을 확인할 수 있습니다.)

{% include in-feed-ads.html %}

### 지도의 초기 위치 설정

아래와 같이 수정하면, 지도의 초기 위치를 설정할 수 있습니다.

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

### 지도의 마커(Marker) 표시

아래와 같이 수정하면, 지도위에 마커(Marker)를 표시할 수 있습니다.

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

### 지도 위치 추적하기

MapView의 `onRegionChange`와 `onRegionChangeComplete`을 사용하면 지도의 위치가 변경된 것을 추적할 수 있습니다.

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

아래의 소스코드는, 사용자가 지도의 초기 위치에서 다른 곳으로 이동할 때, 해당 위치를 추적(트래킹)하고 지도의 가운데에 마커를 찍는 방법입니다.

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

### 사용자의 현재 위치 표시

사용자의 현재 위치를 표시하기 위해서는 사용자의 현재 위치를 가져올 필요가 있습니다. 사용자의 위치 정보를 가져오는 방법에 대해서는 아래에 블로그를 참고하시기 바랍니다.

- [React Native에서 현재 위치 정보 가져오기]({{site.url}}/react-native/react-native-geolocation-service/){:target="_blank"}

이렇게 가져온 사용자 데이터를 표시하기 위해 아래에 소스코드를 이용합니다.

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

결과 화면은 아래와 같습니다.

![react-native-maps 사용자 현재 위치](/assets/images/category/react-native/2019/react-native-maps/user-location.jpg)

{% include in-feed-ads.html %}

### 사용자 위치 추적 표시

위치 정보 라이브러리인 `react-native-geolocation-service`를 사용하면, 사용자의 위치 정보를 추적할 수 있습니다. `react-native-geolocation-service` 라이브러리에 관해서는 아래에 링크를 참고하시기 바랍니다.

- [React Native에서 현재 위치 정보 가져오기]({{site.url}}/react-native/react-native-geolocation-service/){:target="_blank"}

사용자 위치 정보를 추적하여 마커(Marker)로 표시하는 예제는 아래와 같습니다.

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

사용자 위치 추적의 결과 화면은 아래와 같습니다.

![react-native-maps 사용자 위치 추적](/assets/images/category/react-native/2019/react-native-maps/track-user-location.jpg)

{% include in-feed-ads.html %}

### 그밖에 기능들

지도의 초기 위치 설정 및 마커(Marker) 표시 이외에도 다양한 기능을 제공하고 있습니다. 아래에 링크를 통해 공식 사이트를 참고하시기 바랍니다.

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

## 네이버 지도

한국에서는 네이버 지도을 사용하고 싶은 분들이 많을거 같습니다. 여기서 소개한 라이브러리는 핸드폰에서 기본적으로 제공하는 지도(구글, 애플)를 사용합니다. 네이버 지도를 사용하고 싶은 분들은 아래에 라이브러리를 참고하시기 바랍니다.

- [react-native-naver-map](https://github.com/QuadFlask/react-native-naver-map){:rel="nofollow noreferrer" target="_blank"}

## 완료

이것으로 React Native에서 지도를 사용하는 방법에 대해서 알아보았습니다. 이 라이브러리를 사용하면 지도 위에 마커뿐만 아니라, 폴리곤(Polygon)이나 폴리라인(Polyline)도 그릴 수 있습니다.

지도를 가지고 서비스를 준비중이신 분들은 이 라이브러리를 사용해 보시는 걸 추천합니다.
