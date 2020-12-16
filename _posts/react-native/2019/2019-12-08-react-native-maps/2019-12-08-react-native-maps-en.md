---
layout: 'post'
permalink: '/react-native/react-native-maps/'
paginate_path: '/react-native/:num/react-native-maps/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'Show Map on React Native'
description: Let's see how to use react-native-maps to display a map on React Native
image: '/assets/images/category/react-native/2019/react-native-maps/background.jpg'
---

<div id="contents_list" markdown="1">

## Content

1. [Outline](#outline)
1. [How to install react-native-maps](#how-to-install-react-native-maps)
1. [How to link the library](#how-to-link-the-library)
    - [Version >= 0.60](#version--060)
    - [Version <= 0.59](#version--059)
1. [How to use Google map on iOS](#how-to-use-google-map-on-ios)
1. [How to use](#how-to-use)
    - [Apple map](#apple-map)
    - [Google map](#google-map)
    - [Configure map initial location](#configure-map-initial-location)
    - [Display a marker on the map](#display-a-marker-on-the-map)
    - [Tracking the map with a marker](#tracking-the-map-with-a-marker)
    - [Display user location](#display-user-location)
    - [Track and display user location](#track-and-display-user-location)
    - [Other features](#other-features)
1. [Completed](#completed)

</div>

## Outline

In this blog post, we'll see how to show a map on React Native. For displaying a map on React Native, React Native community's [react-native-maps](https://github.com/react-native-community/react-native-maps){:rel="nofollow noreferrer" target="_blank"} library is used normally.

In here, we'll see how to get user location and show user location on the map with `react-native-map` library.

You can see the full source code about this blog post on Github.

- github: [react-native-map-example](https://github.com/dev-yakuza/react-native-map-example){:target="_blank"}

The example source code is based on the list below. If you want to know details, see the links below.

- [typescript]({{site.url}}/react-native/typescript/){:target="_blank"}
- [styled-components]({{site.url}}/react-native/styled-components/){:target="_blank"}
- [root-import]({{site.url}}/react-native/root-import/){:target="_blank"}
- [Geolocation in React Native]({{site.url}}/react-native/react-native-geolocation-service/){:target="_blank"}

{% include in-feed-ads.html %}

## How to install react-native-maps

execute the command below to install react-native-maps.

```bash
npm install --save react-native-maps
```

## How to link the library

We need to link the library to React Native project.

### Version >= 0.60

execute the commands below to link react-native-maps to React Native project.

```bash
cd ios
pod install
cd ..
```

### Version <= 0.59

execute the commands below to link react-native-maps to React Native project.

```bash
react-native link react-native-maps
```

If you need to link manually, see the links below.

- [iOS - Using CocoaPods (React Native 0.59 and lower)](https://github.com/react-native-community/react-native-maps/blob/master/docs/installation.md#using-cocoapods-react-native-059-and-lower){:rel="nofollow noreferrer" target="_blank"}
- [Build configuration on Android](https://github.com/react-native-community/react-native-maps/blob/master/docs/installation.md#build-configuration-on-android){:rel="nofollow noreferrer" target="_blank"}

## How to use Google map on iOS

Over than 0.60 version, for using Google map, open `ios/[project name]/AppDelegate.m` file and modify it like below.

```swift
#import <GoogleMaps/GoogleMaps.h>

@implementation AppDelegate
...

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
+  [GMSServices provideAPIKey:@"_YOUR_API_KEY_"]; // add this line using the api key obtained from Google Console
...
```

And the, open `ios/Podfile` file and modify it like below.

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

Lastly, execute the commands below to install required libraries on iOS.

```bash
cd ios
pod install
cd ..
```

Under than 0.59 version, see the official site links below.

- [Enabling Google Maps on iOS (React Native all versions)](https://github.com/react-native-community/react-native-maps/blob/master/docs/installation.md#enabling-google-maps-on-ios-react-native-all-versions){:rel="nofollow noreferrer" target="_blank"}

{% include in-feed-ads.html %}

## How to use

Modify the source code in which you want to display a map by react-native-maps like below.

### Apple map

Modify like below to show Apple map.

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

Execute the command below to start React Native project,

```bash
npm run ios
# android
# npm run android
```

You can see the result screen like below.

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2019/react-native-maps/apple-map.jpg" alt="on React Native, display a map by react-native-maps - Apple map">
</div>

### Google map

Modify like below to use Google map.

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

Execute the command below to start React Native project,

```bash
npm run ios
# android
# npm run android
```

You can see the result screen like below.

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2019/react-native-maps/google-map.jpg" alt="on React Native how to use react-native-maps to display a map - Google map">
</div>

(In here, Google map is not shown up, because I use example `provideAPIKey`. If you use your own provideAPIKey, you can see Google map is displayed)

{% include in-feed-ads.html %}

### Configure map initial location

Modify like below, you can set initial location of the map.

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

### Display a marker on the map

Modify like below, you can display a marker on the map.

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

### Tracking the map with a marker

You can track the map location changed with `onRegionChange` and `onRegionChangeComplete` of MapView.

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

the source code below is about how to track the map that the user moves from the initial location, and display the marker on the center of the map.

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

### Display user location

To display user location, we need to get current user location. If you want to know how to get current user location, see the link below.

- [Geolocation in React Native]({{site.url}}/react-native/react-native-geolocation-service/){:target="_blank"}

To display user data, modify like below.

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

The result is like below.

![react-native-maps user current location](/assets/images/category/react-native/2019/react-native-maps/user-location.jpg)

{% include in-feed-ads.html %}

### Track and display user location

If you use `react-native-geolocation-service` library to use get user location, you can track user location. If you want to know how to use `react-native-geolocation-service` library, see the link below.

- [Geolocation in React Native]({{site.url}}/react-native/react-native-geolocation-service/){:target="_blank"}

To track user location and display markers on the map, modify like below.

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

The result screen is like below.

![react-native-maps track user location](/assets/images/category/react-native/2019/react-native-maps/track-user-location.jpg)

{% include in-feed-ads.html %}

### Other features

In additional to set initial location and display markers, there are many features. If you want to know details, see the links below.

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

## Completed

We've seen how to display a map on React Native. If you use this library, you can display Polygon and Polyline, in additional to markers.

If you prepare the service which has a map, I recommend using this library!
