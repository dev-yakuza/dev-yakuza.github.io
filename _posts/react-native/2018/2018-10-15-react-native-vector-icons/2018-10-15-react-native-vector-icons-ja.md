---
layout: 'post'
permalink: '/react-native/react-native-vector-icons/'
paginate_path: '/react-native/:num/react-native-vector-icons/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'react-native-vector-icons'
description: 'react-native-vector-iconsライブラリを使ってアイコンを表示して見ましょう。'
image: '/assets/images/category/react-native/react-native-vector-icons.jpg'
---

<div id="contents_list" markdown="1">

## 目次

1. [概要](#概要)
1. [ライブラリインストール](#ライブラリインストール)
1. [ライブラリリンク](#ライブラリリンク)
    - [0.59 以下](#059-以下)
    - [0.60 以上](#060-以上)
        - [iOS](#ios)
        - [Android](#android)
1. [使い方](#使い方)
1. [Material icons](#material-icons)
1. [参考](#参考)

</div>

## 概要

リアクトネイティブ(React Native)プロジェクトへベクターアイコンを使うため[react-native-vector-icons](https://github.com/oblador/react-native-vector-icons){:rel="nofollow noreferrer" target="_blank" } ライブラリを使って見ましょう。

## ライブラリインストール

下記のコマンドでreact-native-vector-iconsをインストールします。

```bash
npm install react-native-vector-icons --save
# For Typescript
npm install --save-dev @types/react-native-vector-icons
```

インストールが完了されたら下記のコマンドでライブラリをプロジェクトへリンクします。

## ライブラリリンク

react-native-vector-iconsを使うためインストールしたライブラリをリンクする必要があります。

### 0.59 以下

下記のコマンドを使ってライブラリをリンクします。

```bash
react-native link react-native-vector-icons
```

{% include in-feed-ads.html %}

### 0.60 以上

0.60以上から手動でリンクする必要があります。

#### iOS

iOSでreact-native-vector-iconsをリンクするため`ios/[project].xcworkspace`を選択してXcodeを実行します。

![react-native-vector-iconsインストール方法 - Xcode Fontsグループ追加](/assets/images/category/react-native/2018/react-native-vector-icons/xcode_add_new_group.jpg)

Xcodeが実行されると上のようにプロジェクトを右クリックして`New Group`メニューを選択して、`Fonts`の名前でグループを生成します。

![react-native-vector-iconsインストール方法 - Xcode Fonts path](/assets/images/category/react-native/2018/react-native-vector-icons/react-native-vector-icons_font_path.jpg)

Fontsグループを生成したら、上のように`node_modules/react-native-vector-icons/Fonts/`で移動して下にある全てのフォントをXcodeのFontsグループにドラックします。

![react-native-vector-iconsインストール方法 - Xcode Fonts Copy items if needed](/assets/images/category/react-native/2018/react-native-vector-icons/copy-items-if-needed.jpg)

ドラックしたら上のような画面が見えます。`Copy items if needed`がチェックされた状態で右下の`Finish`ボタンを選択します。

最後に`ios/[project]/Info.plist`ファイルを開いて下記の内容を追加します。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    ...
  <key>UIViewControllerBasedStatusBarAppearance</key>
  <false/>
  <key>UIAppFonts</key>
  <array>
    <string>AntDesign.ttf</string>
    <string>Entypo.ttf</string>
    <string>EvilIcons.ttf</string>
    <string>Feather.ttf</string>
    <string>FontAwesome.ttf</string>
    <string>FontAwesome5_Brands.ttf</string>
    <string>FontAwesome5_Regular.ttf</string>
    <string>FontAwesome5_Solid.ttf</string>
    <string>Foundation.ttf</string>
    <string>Ionicons.ttf</string>
    <string>MaterialCommunityIcons.ttf</string>
    <string>MaterialIcons.ttf</string>
    <string>Octicons.ttf</string>
    <string>SimpleLineIcons.ttf</string>
    <string>Zocial.ttf</string>
    <string>Fontisto.ttf</string>
  </array>
</dict>
```

Xcodeで`cmd + shift + k`を押して`Clean Build Folder`を実行します。

{% include in-feed-ads.html %}

#### Android

アンドロイドはiOSより設定が簡単です。`android/app/build.gradle`ファイルを開いて下記の内容を追加します。

```js
...
apply from: "../../node_modules/react-native/react.gradle"
apply from: "../../node_modules/react-native-vector-icons/fonts.gradle" // add this line
...
```

そして`node_modules/react-native-vector-icons/Fonts/`下にあるフォントファイルを`android/app/src/main/assets/fonts`フォルダへコピーします。(assets/fontsフォルダが無い時はフォルダを生成します。)

最後にアンドロイドプロジェクトをAndroid Studioで開いて自動でGradle syncの実行が終わることを待てます。

アンドロイドプロジェクトをAndroid Studioで開くため下記のコマンドを使うことができます。

```bash
# in RN project root folder
open -a /Applications/Android\\ Studio.app ./android
```

## 使い方

私たちは基本的使ったことがある場合、ブログを作成します。したがってここには私たちが実際使って分かった内容を追加する予定です。

使い方を詳しく知りたい方は公式サイトを見てください。

- 公式サイト: [react-native-vector-icons](https://github.com/oblador/react-native-vector-icons){:rel="nofollow noreferrer" target="_blank" }

{% include in-feed-ads.html %}

## Material icons

Material iconを使う方法

```js
...
import Icon from 'react-native-vector-icons/FontAwesome';
...

export default class Home extends React.Component<Props, State> {
    render() {
        return (
            <View>
                <Icon name="home" size={24} color="#ffffff" />
            </View>
        );
    }
}
```

## 参考

- 公式サイト: [react-native-vector-icons](https://github.com/oblador/react-native-vector-icons){:rel="nofollow noreferrer" target="_blank" }
