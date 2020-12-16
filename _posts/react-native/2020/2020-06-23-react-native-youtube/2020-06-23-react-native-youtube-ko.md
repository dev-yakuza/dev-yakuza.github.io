---
layout: 'post'
permalink: '/react-native/react-native-youtube/'
paginate_path: '/react-native/:num/react-native-youtube/'
lang: 'ko'
categories: 'react-native'
comments: true

title: React Native에서 Youtube 재생하기
description: React Native에서 Youtube를 재생하기 위해서 react-native-youtube를 사용하는 방법에 대해서 알아봅시다.
image: '/assets/images/category/react-native/2020/react-native-youtube/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

- [목차](#목차)
- [개요](#개요)
- [react-native-youtube 설치 및 준비](#react-native-youtube-설치-및-준비)
- [react-native-youtube 사용법](#react-native-youtube-사용법)
  - [비디오 재생](#비디오-재생)
  - [FlatList에서 사용하기](#flatlist에서-사용하기)
- [완료](#완료)

</div>

## 개요

React Native로 토이프로젝트를 진행하면서 Youtube 비디오를 재생할 필요가 생겼습니다.

- [「Clog」 서비스 개발기(React Native, Laravel, Django)]({{site.url}}/clog/development-journal/){:target="_blank"}

이번 블로그 포스트에서는 React Native 프로젝트에서 Youtube 비디오를 재생하기 위해서, `react-native-youtube` 라이브러리를 사용하는 방법에 대해서 설명합니다.

- [react-native-youtube](https://github.com/davidohayon669/react-native-youtube){:rel="nofollow noreferrer" target="_blank"}

여기서 사용 소개하는 예제는 GitHub 저장소에서도 확인할 수 있습니다.

- [React Native Youtube Example](https://github.com/dev-yakuza/react-native-youtube-example){:target="_blank"}

## react-native-youtube 설치 및 준비

아래에 명령어를 사용하여 react-native-youtube를 설치합니다.

```bash
npm install --save react-native-youtube
```

iOS에서 사용하기 위해서는 아래에 명령어를 실행합니다.

```bash
cd ios
pod install
```

안드로이드에서 react-native-youtube를 사용하기 위해서는 `Youtube developer API key`가 필요합니다. 아래에 링크를 통해 Youtube developer API key를 생성하시기 바랍니다.

- [Youtube Developer API Key for Android](https://developers.google.com/youtube/android/player/register){:rel="nofollow noreferrer" target="_blank"}

{% include in-feed-ads.html %}

## react-native-youtube 사용법

### 비디오 재생

react-native-youtube를 사용하여 React Native에서 Youtube를 재생하기 위해서 아래와 같이 소스 코드를 추가합니다.

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

### FlatList에서 사용하기

안드로이드에서는 react-native-youtube를 사용하여 여러 Youtube를 한 화면에서 재생할 수 없습니다. 자세한 내용은 아래에 링크를 확인하시기 바랍니다.

- [Multiple Youtube instance on Android](https://github.com/davidohayon669/react-native-youtube#multiple-youtube--instances-on-android){:rel="nofollow noreferrer" target="_blank"}

따라서 안드로이드에서 FlatList를 사용하여 여러 비디오를 표시하고, 자동 재생하기 위해서는 FlatList의`viewabilityConfig`와 `onViewableItemsChanged`를 조합하여 구현할 수 있습니다.

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

위에 소스를 좀 더 자세히 살펴보면,

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

위와 같이 화면에 표시된 아이템이 어느정도 보이면, 화면에 표시되었다고 판단할 수 있도록 기준을 작성합니다.

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

그리고 화면에 표시된 아이템이 변경되면 호출되는 `onViewableItemsChanged`을 통해 현재 표시된 여러 아이템중 첫번째 아이템의 Index를 `useState`를 통해 저장합니다.

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

이렇게 저장한 Index를 비교하셔 첫번째 아이템의 비디오만을 재생하도록 설정할 수 있습니다. 이렇게 하면, 안드로이드에서도 여러 비디오를 자동 재생할 수 있습니다.

## 완료

이것으로 React Native에서 Youtube를 재생하는 방법에 대해서 알아보았습니다. 여기서 소개한 소스코드는 GitHub에서 확인이 가능하니, 전체 소스를 보고 참고하시면 좋을거 같습니다.

- [React Native Youtube Example](https://github.com/dev-yakuza/react-native-youtube-example){:target="_blank"}
