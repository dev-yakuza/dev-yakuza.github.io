---
layout: 'post'
permalink: '/react-native/react-native-lottie/'
paginate_path: '/react-native/:num/react-native-lottie/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'アフターエフェクト(AEF)'
description: 'リアクトネイティブ(React Native)プロジェクトでアドビのアフターエフェクト(Adobe After Effects)で作ったアニメーションを適用してみましょう'
image: '/assets/images/category/react-native/2019/react-native-lottie/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

1. [概要](#概要)
1. [インストール](#インストール)
    - [0.60 以上](#060-以上)
        - [ライブラリ連動](#ライブラリ連動)
    - [0.59 以下](#059-以下)
        - [ライブラリ連結](#ライブラリ連結)
1. [使い方](#使い方)
1. [アニメーションファイルへイメージがある場合](#アニメーションファイルへイメージがある場合)
    - [Git リポジトリ](#git-リポジトリ)
1. [エラー対応](#エラー対応)
    - [(0.60 / iOS) ld: warning: Could not find or use auto-linked library](#060--ios-ld-warning-could-not-find-or-use-auto-linked-library)
    - [error: Cycle in dependencies between targets](#error-cycle-in-dependencies-between-targets)
    - [アンドロイドビルドエラー](#アンドロイドビルドエラー)
1. [完了](#完了)
1. [参考](#参考)

</div>

## 概要

最近アプリに躍動感を入れるためマイクロインタラクション(Microinteractions)をたくさん使っています。このブログでは```アドビのアフターエフェクト(Adobe After Effects)```で作ったアニメーションをAirbnbが作った```lottie```ライブラリを使ってリアクトネイティブ(React Native)に適用する方法について説明します。

- lottie公式サイト: [https://airbnb.design/lottie/](https://airbnb.design/lottie/){:rel="nofollow noreferrer" target="_blank"}

## インストール

リアクトネイティブ(React Native)で```lottie```ライブラリを使うため下のコマンドを実行して```lottie-react-native```ライブラリをインストールします。

### 0.60 以上

```bash
npm install --save lottie-react-native lottie-ios
```

#### ライブラリ連動

インストールが完了したら、下記のコマンドを実行してiOSに必要なライブラリを連動します。

```bash
cd ios
pod install
cd ..
```

{% include in-feed-ads.html %}

### 0.59 以下

```bash
npm install --save lottie-react-native
```

#### ライブラリ連結

リアクトネイティブ(React Native)で```lottie```ライブラリを使うため```lottie-react-native```ライブラリをインストールを完了したら下記の方法でOSに合わせてライブラリを接続します。

- iOS

リアクトネイティブ(React Native)で```lottie```ライブラリをiOSで使うため下記のように```lottie-react-native```ライブラリをリアクトネイティブ(React Native)プロジェクトと連結します。

```bash
react-native link lottie-ios
react-native link lottie-react-native
```

そして```ios/[project_name].xcodeproj```か```ios/[project_name].xcworkspace```ファイルを開いてxcodeを実行します。その後、下のように追加設定をしてください。

![lottie ios追加設定](/assets/images/category/react-native/2019/react-native-lottie/ios-settings.jpg)

1. 下のメニューでプロジェクト名を選択
1. ```TARGETS```でプロジェクト名を選択
1. 上部にあるメニューで```General```を選択
1. スクロールして下に行くと```Embedded Binaries```項目が見える。```+```ボタンを押して```Lottie.framework```を検索、```ios```用を選択して追加します。

![lottie ios framework追加設定](/assets/images/category/react-native/2019/react-native-lottie/add-lottie-framework.jpg)

- アンドロイド

上のように```iOS```を連結したら```lottie```ライブラリをアンドロイドで使うため他にすることはありません。下記のコマンドが実行された時、アンドロイドは```lottie-react-native```と連結されました。

```bash
react-native link lottie-react-native
```

{% include in-feed-ads.html %}

## 使い方

リアクトネイティブ(React Native)でlottieを使うためにはアドビのアフターエフェクト(Adobe After Effects)で作ったアニメーションファイルが必要になりますアドビのアフターエフェクト(Adobe After Effects)でlottieに必要なアニメーションファイルを作る方法についてはこのブログでは説明しません。下記のリンクを参考してアドビのアフターエフェクト(Adobe After Effects)からlottieのアニメーションファイルを生成してください。

- [https://github.com/airbnb/lottie-web](https://github.com/airbnb/lottie-web){:rel="nofollow noreferrer" target="_blank"}

または下記のサイトで必要なマイクロインタラクション(Microinteractions)ファイルを検索してください。

- [https://lottiefiles.com/](https://lottiefiles.com/){:rel="nofollow noreferrer" target="_blank"}

アドビのアフターエフェクト(Adobe After Effects)や上のサイトからダウンロードしたファイルは```json```形式になっております。

リアクトネイティブ(React Native)でlottieを利用してマイクロインタラクション(Microinteractions)を適用するため下記のようにコードを作成します。

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

## アニメーションファイルへイメージがある場合

アドビのアフターエフェクト(AEF)を使ってアニメーションを作る際、アニメーションへイメージを含める場合が発生します。

イメージを含めたアニメーションをlottie用でエクスポートしたら、下記のようにイメージが含めてある```data.json```を確認することができます。

```json
// data.json
{
  ...
  "assets": [
    {
      "id": "image_0",
      "w": 588,
      "h": 792,
      "u": "images/",
      "p": "main_character.jpg",
      "e": 0
    }
  ]
  ...
```

イメージを含めてるアニメーションファイルは普通のファイルと違ってイメージを追加する作業が必要になります。

{% include in-feed-ads.html %}

- iOS

リアクトネイティブ(React Native)プロジェクトフォルダで```ios/[project name].xcworkspace```(または```ios/xcodeproj```)を選択してxcodeを実行します。

![lottie ios イメージ追加](/assets/images/category/react-native/2019/react-native-lottie/lottie_ios_image_add.jpg)

上のように左でプロジェクトを選択して```Resources```フォルダを右クリくして```Add Files to [project name]```を選択します。

![lottie ios イメージ追加 - ファイル選択](/assets/images/category/react-native/2019/react-native-lottie/lottie_ios_image_add_select_file.jpg)

追加したいファイルを選択して、下にある```Copy items if needed```オプションを選択して追加します。

上記のように```Resources```フォルダが見えない場合、左メニューでプロジェクト名を右クリくして```New Group without Folder```を洗濯した後、追加されたグループ名を```Resources```で修正します。

![lottie ios イメージ追加 - resources グループ追加](/assets/images/category/react-native/2019/react-native-lottie/lottie_ios_image_add_resources_group.jpg)

- アンドロイド

アンドロイドはiOSより簡単です。リアクトネイティブ(React Native)プロジェクトの```android/app/src/main/assets```へアニメーションに含めてるイメージを入れるフォルダを生成します。ここでは```images```フォルダを生成しました。そしてそのフォルダにイメージをコピーします。(```android/app/src/main/assets/images```)

コピーが完了したら、下のようにソースコードへ```imageAssetsFolder={'images'}```を追加します。

```js
<LottieView
  source={require('./animation.json')}
  autoPlay
  loop
  imageAssetsFolder={'images'}
/>
```

### Git リポジトリ

アニメーションへイメージが含まれてある場合、```Lottie```を使う方法についてgitリポジトリ(Repository)を作りました。下記のリンクで例題を確認することができます。

- git リポジトリ: [react_native_lottie_exercise](https://github.com/dev-yakuza/react_native_lottie_exercise){:rel="nofollow noreferrer" target="_blank"}

## エラー対応

### (0.60 / iOS) ld: warning: Could not find or use auto-linked library

0.60に下記のコマンドでiOSを実行すると

```bash
react-native run-ios
```

下記のようなエラーが発生しました。

```bash
ld: warning: Could not find or use auto-linked library ‘swiftCoreFoundation’
ld: warning: Could not find or use auto-linked library ‘swiftCompatibility50’
ld: warning: Could not find or use auto-linked library ‘swiftSwiftOnoneSupport’
ld: warning: Could not find or use auto-linked library ‘swiftObjectiveC’
ld: warning: Could not find or use auto-linked library ‘swiftQuartzCore’
ld: warning: Could not find or use auto-linked library ‘swiftCore’
ld: warning: Could not find or use auto-linked library ‘swiftCoreGraphics’
ld: warning: Could not find or use auto-linked library ‘swiftDispatch’
ld: warning: Could not find or use auto-linked library ‘swiftDarwin’
ld: warning: Could not find or use auto-linked library ‘swiftUIKit’
ld: warning: Could not find or use auto-linked library ‘swiftCompatibilityDynamicReplacements’
ld: warning: Could not find or use auto-linked library ‘swiftCoreImage’
ld: warning: Could not find or use auto-linked library ‘swiftFoundation’
ld: warning: Could not find or use auto-linked library ‘swiftMetal’
```

これを解決するため、`/ios/[project name].xcworkspace`ファイルを実行してXcodeを実行します。

![lottie 0.60, iOS ビルドエラー対応 warning: Could not find or use auto-linked - add new file](/assets/images/category/react-native/2019/react-native-lottie/add-new-file.jpg)

上の画像ように`File > New > File...`を選択します。

![lottie 0.60, iOS ビルドエラー対応 warning: Could not find or use auto-linked - add Swift file](/assets/images/category/react-native/2019/react-native-lottie/add-swift-file.jpg)

上の画像ように`Swift File`を選択して右下の`Next`ボタンを押します。

![lottie 0.60, iOS ビルドエラー対応 warning: Could not find or use auto-linked - create new file](/assets/images/category/react-native/2019/react-native-lottie/create-new-file.jpg)

上のように新しファイルを生成する画面が出たら、右下の`Create`を押します。

![lottie 0.60, iOS ビルドエラー対応 warning: Could not find or use auto-linked - Create Bridging Header](/assets/images/category/react-native/2019/react-native-lottie/create-bridging-header.jpg)

上のような画面が出たら、右下の`Create Bridging Header`を選択します。

そして下記のコマンドで実行して、以前実行したプロジェクトをiOSのシミュレータから削除します。

```bash
rm -rf ~/Library/Developer/Xcode/DerivedData/*
```

最後に、下記のように`Product > Clean Build Folder`を選択します。

![lottie 0.60, iOS ビルドエラー対応 warning: Could not find or use auto-linked - Clean Build Folder](/assets/images/category/react-native/2019/react-native-lottie/clean-build-folder.jpg)

次は、下記のコマンドを実行してiOSを実行します。

```bash
react-native run-ios
```

{% include in-feed-ads.html %}

### error: Cycle in dependencies between targets

リアクトネイティブ(React Native)プロジェクトで```react-native-lottie```を実装してよく使いましたが、別のライブラリを入れった後ビルドする時、下記のようなエラーが発生しました。

```bash
Build system information

error: Cycle in dependencies between targets 'LottieLibraryIOS' and 'LottieReactNative'; building could produce unreliable results.
Cycle path: LottieLibraryIOS → LottieReactNative → LottieLibraryIOS
Cycle details:
...
```

リアクトネイティブ(React Native)プロジェクトの```Pods```フォルダや```node_modules```を削除してまたインストールしても問題が続けて発生しました。

下にある説明で私のリアクトネイティブ(React Native)のプロジェクトは問題なくビルドされました。他の方も私と同じ問題が発生したら下記の方法を試してみてください。

リアクトネイティブ(React Native)プロジェクトの```ios/[project_name].xcworkspace```ファイルを実行してxcodeを実行します。

![lottie ビルドエラー対応](/assets/images/category/react-native/2019/react-native-lottie/lottie_fix_error.jpg)

xcodeが実行されたら上のように```File > Workspace Settings...```を選択します。

![lottie ビルドエラー対応: ビルドシステム変更](/assets/images/category/react-native/2019/react-native-lottie/change_build_system.jpg)

上のようにビルドシステム(Build System)を```New Build System (Default)```から ```Legacy Build System```に変更します。

私の場合はこのようにビルドシステム(Build System)を変更した後、リアクトネイティブ(React Native)をビルドしたら無事にビルドされることを確認しました。他の方もこの方法で解決されたらいいと思います。

{% include in-feed-ads.html %}

### アンドロイドビルドエラー

アンドロイドでビルドしたら下記のようにエラーが発生する場合があります。

```bash
Execution failed for task ':app:transformClassesWithDexBuilderForDevDebug'.
```

この場合、リアクトネイティブ(React Native)プロジェクトフォルダの```android/app/build.gradle```を開いて下記のように修正します。

```xml
android{
    ...
    configurations.all {
        resolutionStrategy {
            force 'com.airbnb.android:lottie:2.5.5'
        }
    }
}
```

- 参考: [Java 8 compilation error version 2.5.6](https://github.com/airbnb/lottie-android/issues/822#issuecomment-401812260){:rel="nofollow noreferrer" target="_blank"}

## 完了

これでリアクトネイティブ(React Native)でlottieを使ってマイクロインタラクション(Microinteractions)を実装しました。簡単ですね？lottieでアニメーションを適用するよりアニメーションを作ることがもっと大変と思います。私はアフターエフェクト(After Effects)ができないので[https://lottiefiles.com/](https://lottiefiles.com/){:rel="nofollow noreferrer" target="_blank"}サイトを使ってます。lottieを使って皆さんも皆さんのアプリに面白いマイクロインタラクション(Microinteractions)を入れってみてください。

## 参考

- lottie公式サイト: [https://airbnb.design/lottie/](https://airbnb.design/lottie/){:rel="nofollow noreferrer" target="_blank"}
