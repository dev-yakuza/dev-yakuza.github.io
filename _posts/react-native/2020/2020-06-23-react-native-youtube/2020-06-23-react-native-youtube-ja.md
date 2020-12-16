---
layout: 'post'
permalink: '/react-native/react-native-youtube/'
paginate_path: '/react-native/:num/react-native-youtube/'
lang: 'ja'
categories: 'react-native'
comments: true

title: React NativeでYoutubeを表示する
description: React NativeでYoutubeを表示するため、react-native-youtubeを使う方法について説明します。
image: '/assets/images/category/react-native/2020/react-native-youtube/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [目次](#目次)
- [概要](#概要)
- [react-native-youtubeインストールや準備](#react-native-youtubeインストールや準備)
- [react-native-youtube使い方](#react-native-youtube使い方)
  - [ビデオ再生](#ビデオ再生)
  - [FlatListで使う方法](#flatlistで使う方法)
- [完了](#完了)

</div>

## 概要

React Nativeでトーイプロジェクトを作る時、Youtubeビデオを表示する必要がありました。

- [「Clog」 サービス開発日誌(React Native, Laravel, Django)]({{site.url}}/clog/development-journal/){:target="_blank"}

このブログポストではReact NativeプロジェクトでYoutubeビデオを表示するため、`react-native-youtube`ライブラリを使う方法について説明します。

- [react-native-youtube](https://github.com/davidohayon669/react-native-youtube){:rel="nofollow noreferrer" target="_blank"}

ここで紹介するソースコードはGitHubで確認できます。

- [React Native Youtube Example](https://github.com/dev-yakuza/react-native-youtube-example){:target="_blank"}

## react-native-youtubeインストールや準備

下記のコマンドを使ってreact-native-youtubeをインストールします。

```bash
npm install --save react-native-youtube
```

iOSで使うため、下記のコマンドを実行します。

```bash
cd ios
pod install
```

アンドロイドではreact-native-youtubeを使うためには`Youtube developer API key`が必要です。下記のリンクを使ってYoutube developer API keyを生成します。

- [Youtube Developer API Key for Android](https://developers.google.com/youtube/android/player/register){:rel="nofollow noreferrer" target="_blank"}

{% include in-feed-ads.html %}

## react-native-youtube使い方

### ビデオ再生

react-native-youtubeを使ってReact NativeでYoutubeを再生するためには下記のようにソースコードを追加します。

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

### FlatListで使う方法

アンドロイドではreact-native-youtubeを使って複数のYoutubeを同じ画面で表示や再生することができません。このIssueについて詳しくは下記のリンクを参考してください。

- [Multiple Youtube instance on Android](https://github.com/davidohayon669/react-native-youtube#multiple-youtube--instances-on-android){:rel="nofollow noreferrer" target="_blank"}

したがって、アンドロイドFlatListを使って複数のビデオを表示して、自動再生するためにはFlatListの`viewabilityConfig`と`onViewableItemsChanged`を使って実装することができます。

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

上のソースコードをもっと詳しく見ると、

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

上のように画面へ表示されたItemがどのぐらい見えると、画面へ表示されたかを判断できるような基準を作成します。

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

そして画面へ表示されたItemが変更される時Callされる`onViewableItemsChanged`を使って現在表示された複数のItem中で一番最初のItemのIndexを`useState`を使って保存します。

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

このように保存したIndexを比較して最初のItemのビデオだけ表示して再生するように設定することができます。このように修正すると、複数のビデオの自動再生することができます。

## 完了

これでReact NativeでYoutubeを再生する方法について見てみました。ここで紹介したソースコードはGitHubで確認できますので、全てのソースコードを見て、参考しても良いかと思います。

- [React Native Youtube Example](https://github.com/dev-yakuza/react-native-youtube-example){:target="_blank"}
