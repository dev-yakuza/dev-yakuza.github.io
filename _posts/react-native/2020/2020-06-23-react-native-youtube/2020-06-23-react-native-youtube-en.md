---
layout: 'post'
permalink: '/react-native/react-native-youtube/'
paginate_path: '/react-native/:num/react-native-youtube/'
lang: 'en'
categories: 'react-native'
comments: true

title: Play Youtube on React Native
description: To play Youtube video on React Native, let's see how to use react-native-youtube!
image: '/assets/images/category/react-native/2020/react-native-youtube/background.jpg'
---

<div id="contents_list" markdown="1">

## Contents

- [Contents](#contents)
- [Outline](#outline)
- [Install and prepare react-native-youtube](#install-and-prepare-react-native-youtube)
- [How to use react-native-youtube](#how-to-use-react-native-youtube)
  - [Play video](#play-video)
  - [Play Video with FlatList](#play-video-with-flatlist)
- [Completed](#completed)

</div>

## Outline

when I made a toy-project with React Native, I needed to play Youtube on it.

- [「Clog」 Service Development Journal(React Native, Laravel, Django)]({{site.url}}/clog/development-journal/){:target="_blank"}

In this blog post, I will show you how to use `react-native-youtube` to show and play Youtube video.

- [react-native-youtube](https://github.com/davidohayon669/react-native-youtube){:rel="nofollow noreferrer" target="_blank"}

You can see the example source code on GitHub.

- [React Native Youtube Example](https://github.com/dev-yakuza/react-native-youtube-example){:target="_blank"}

## Install and prepare react-native-youtube

Execute the command below to install react-native-youtube.

```bash
npm install --save react-native-youtube
```

Execute the command below to use it on iOS.

```bash
cd ios
pod install
```

You need `Youtube developer API key` to play Youtube on Android. See the link below to make Youtube developer API key.

- [Youtube Developer API Key for Android](https://developers.google.com/youtube/android/player/register){:rel="nofollow noreferrer" target="_blank"}

{% include in-feed-ads.html %}

## How to use react-native-youtube

### Play video

Use the source code below to play Youtube via react-native-youtube.

```js
{% raw %}
import YouTube from 'react-native-youtube';
...
const App = () => {
  return (
    <SafeAreaView style={styles.container}>
      <YouTube
        videoId="KVZ-P-ZI6W4"
        apiKey="YOUR_YOUTUBE_DEVELOPER_API_KEY_FOR_ANDROID"
        play={true}
        fullscreen={false}
        loop={false}
        onReady={(e) => console.log('onReady')}
        onChangeState={(e) => console.log('onChangeState:', e.state)}
        onChangeQuality={(e) => console.log('onChangeQuality: ', e.quality)}
        onError={(e) => console.log('onError: ', e.error)}
        style={{width: '100%', height: 300}}
      />
    </SafeAreaView>
  );
};
{% endraw %}
```

### Play Video with FlatList

We can not show and play many Youtube videos via react-native-youtube on Android. See the link below about the details of this issue.

- [Multiple Youtube instance on Android](https://github.com/davidohayon669/react-native-youtube#multiple-youtube--instances-on-android){:rel="nofollow noreferrer" target="_blank"}

So, to show and auto-play with FlatList, we should use FlatList's `viewabilityConfig` and `onViewableItemsChanged`.

```js
{% raw %}
...
import YouTube from 'react-native-youtube';

...

const Placeholder = () => {
  return (
    <View style={styles.item}>
      <ActivityIndicator size="large" color="white" />
    </View>
  );
};

const ListVideo = () => {
  const [visablePostIndex, setVisablePostIndex] = useState(0);

  const onViewRef = useRef(({viewableItems}) => {
    if (viewableItems && viewableItems[0]) {
      const index = viewableItems[0].index;
      if (typeof index === 'number') {
        setVisablePostIndex(index);
      }
    } else {
      setVisablePostIndex(-1);
    }
  });
  const viewConfigRef = useRef({viewAreaCoveragePercentThreshold: 80});

  return (
    <View style={styles.container}>
      <FlatList
        data={VIDEO_LIST}
        viewabilityConfig={viewConfigRef.current}
        onViewableItemsChanged={onViewRef.current}
        keyExtractor={(item, index) => `${index}`}
        renderItem={({item, index}) =>
          index === visablePostIndex ? (
            <YouTube
              videoId={item}
              apiKey="YOUR_YOUTUBE_DEVELOPER_API_KEY_FOR_ANDROID"
              play={true}
              fullscreen={false}
              loop={false}
              onReady={(e) => console.log('onReady')}
              onChangeState={(e) => console.log('onChangeState:', e.state)}
              onChangeQuality={(e) =>
                console.log('onChangeQuality: ', e.quality)
              }
              onError={(e) => console.log('onError: ', e.error)}
              style={{width: '100%', height: 300}}
            />
          ) : (
            <Placeholder />
          )
        }
      />
    </View>
  );
};
...
{% endraw %}
```

{% include in-feed-ads.html %}

Let's see the details.

```js
{% raw %}
...
const viewConfigRef = useRef({viewAreaCoveragePercentThreshold: 80});
...
<FlatList
  viewabilityConfig={viewConfigRef.current}
...
{% endraw %}
```

By using `viewabilityConfig`, we can set the criterion for which items displayed or not.

```js
{% raw %}
...
const onViewRef = useRef(({viewableItems}) => {
    if (viewableItems && viewableItems[0]) {
      const index = viewableItems[0].index;
      if (typeof index === 'number') {
        setVisablePostIndex(index);
      }
    } else {
      setVisablePostIndex(-1);
    }
  });
...
<FlatList
  onViewableItemsChanged={onViewRef.current}
...
{% endraw %}
```

And, by using `onViewableItemsChanged` called when the displayed items are changed, set the Index of items by using `useState`.

```js
{% raw %}
<FlatList
  ...
 renderItem={({item, index}) =>
    index === visablePostIndex ? (
      <YouTube
        videoId={item}
        apiKey="YOUR_YOUTUBE_DEVELOPER_API_KEY_FOR_ANDROID"
        play={true}
        fullscreen={false}
        loop={false}
        onReady={(e) => console.log('onReady')}
        onChangeState={(e) => console.log('onChangeState:', e.state)}
        onChangeQuality={(e) =>
          console.log('onChangeQuality: ', e.quality)
        }
        onError={(e) => console.log('onError: ', e.error)}
        style={{width: '100%', height: 300}}
      />
    ) : (
      <Placeholder />
    )
  }
...
{% endraw %}
```

by using and comparing this Index, we can show and play first video of the displayed items. If you use this structure, you can play videos automatically on Android.

## Completed

We've seen how to play Youtube video on React Native. You can see the full example source code on GitHub.

- [React Native Youtube Example](https://github.com/dev-yakuza/react-native-youtube-example){:target="_blank"}
