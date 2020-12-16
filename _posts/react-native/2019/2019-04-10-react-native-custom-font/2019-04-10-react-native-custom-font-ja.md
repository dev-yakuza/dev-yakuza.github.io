---
layout: 'post'
permalink: '/react-native/react-native-custom-font/'
paginate_path: '/react-native/:num/react-native-custom-font/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'リアクトネイティブ(React Native)でカスタムフォントを使う方法'
description: 'リアクトネイティブ(React Native)プロジェクトでカスタムフォントを適用して使う方法について説明します。'
image: '/assets/images/category/react-native/2019/react-native-custom-font/background.jpg'
---

## 概要
アプリを開発する時、フォントを適用する場合があります。ここにはリアクトネイティブ(React Native)ではどうやってフォントを適用して使うかを紹介します。私は普通グーグルの`Noto Sans`フォントを使っています。

- グーグルのNoto JPフォント: [https://fonts.google.com/specimen/Noto+Sans+JP](https://fonts.google.com/specimen/Noto+Sans+JP){:rel="nofollow noreferrer" target="_blank"}
- グーグルのNoto KRフォント: [https://fonts.google.com/specimen/Noto+Sans+KR](https://fonts.google.com/specimen/Noto+Sans+KR){:rel="nofollow noreferrer" target="_blank"}

このブログではフォントが適用されたかはっきりするため、下記のフォントを適用して使う方法を説明します。

- Dancing Script: [https://fonts.google.com/specimen/Dancing+Script](https://fonts.google.com/specimen/Dancing+Script){:rel="nofollow noreferrer" target="_blank"}

## フォントダウンロード
リアクトネイティブ(React Native)で使いたいフォントをダウンロードします。ここでは概要でも紹介した`Dancing Script`フォントを使います。下記のリンクを押してダウンロードページに移動します。

- Dancing Script: [https://fonts.google.com/specimen/Dancing+Script](https://fonts.google.com/specimen/Dancing+Script){:rel="nofollow noreferrer" target="_blank"}

上のリンクを選択したら下記のような画面が見えます。

![リアクトネイティブ(React Native)カスタムフォント適用 - google dancing script](/assets/images/category/react-native/2019/react-native-custom-font/google-dancing-script-font-site.jpg)

右上の`SELECT THIS FONT`を選択します

![リアクトネイティブ(React Native)カスタムフォント適用 - フォント選択](/assets/images/category/react-native/2019/react-native-custom-font/font-select.jpg)

そしたら上のように右下に`Family Selected`が表示されます。`Family Selected`をクリックします。

![リアクトネイティブ(React Native)カスタムフォント適用 - フォントダウンロード](/assets/images/category/react-native/2019/react-native-custom-font/download-font.jpg)

上のような画面が見えたら、右上にあるダウンロードボタンを押してフォントをダウンロードします。


{% include in-feed-ads.html %}

## フォント適用
ダウンロードしたフォントを各OSに合わせて設定する必要があります。その前、共通であるJSソースから修正します。

### javascriptソース修正
フォントを適用するため下記のようにソースコードを修正します。

```js
import * as React from 'react';
import { Platform } from 'react-native';
import Styled from 'styled-components/native';

const instructions = Platform.select({
  ios: 'Press Cmd+R to reload,\n' + 'Cmd+D or shake for dev menu',
  android:
    'Double tap R on your keyboard to reload,\n' +
    'Shake or press menu button for dev menu',
});

const Container = Styled.View`
    flex: 1;
    justify-content: center;
    align-items: center;
    background-color: #F5FCFF;
`;
const Welcome = Styled.Text`
  font-size: 20px;
  text-align: center;
  margin: 10px;
  font-family: 'DancingScript-Bold'; // <<<<<<<<<<<<< Add here
`;
const Instructions = Styled.Text`
  text-align: center;
  color: #333333;
  margin-bottom: 5px;
  font-family: 'DancingScript-Regular'; // <<<<<<<<<<<<< Add here
`;

interface Props {}
interface State {}

export default class App extends React.Component<Props, State> {
  render() {
    return (
      <Container>
        <Welcome>Welcome to React Native!</Welcome>
        <Instructions>To get started, edit App.js</Instructions>
        <Instructions>{instructions}</Instructions>
      </Container>
    );
  }
}
```

私は普通RN(React Naitve)プロジェクトに`typescript`と`styled-components`を使って開発しています。それでソースの形がちょっと違うかも知れないです。リアクトネイティブ(React Native)プロジェクトに`typescript`と`styled-components`を適用する方法に関しては下記のブログを参考してください。

- [typescript]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}
- [styled-components]({{site.url}}/{{page.categories}}/styled-components/){:target="_blank"}

### iOS
リアクトネイティブ(React Native)プロジェクトを実行したら下記のように基本フォントが適用された画面が見えます。(またはフォントが見つからないのでエラーが発生します。)

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2019/react-native-custom-font/ios-basic-font.jpg" alt="リアクトネイティブ(React Native)カスタムフォントios適用 - 基本フォント">
</div>

ダウンロードしたフォントファイルを`ios/Fonts`フォルダを作ってその中にコピーします。

![リアクトネイティブ(React Native)カスタムフォントios適用 - フォントコピー](/assets/images/category/react-native/2019/react-native-custom-font/ios-copy-fonts.jpg)

フォントファイルをコピーしたら`ios/project_name.xcodeproj`や`ios/project_name.xcworkspace`を実行してxcodeを実行します。

![リアクトネイティブ(React Native)カスタムフォントios適用 - xcodeにフォントを入れる](/assets/images/category/react-native/2019/react-native-custom-font/ios-create-reference.jpg)

左上に自分のプロジェクト名を右クリックして`Add Files to "project_name"...`を選択します。

![リアクトネイティブ(React Native)カスタムフォントios適用 - xcodeにフォント追加](/assets/images/category/react-native/2019/react-native-custom-font/ios-add-font.jpg)

上のようなファイル選択画面が見えたら上で追加した`ios/Fonts`フォルダを選択して`Create folder references`を選択した後、`Add`を押してフォルダを追加します。

![リアクトネイティブ(React Native)カスタムフォントios適用 - Info.plistにフォントを追加](/assets/images/category/react-native/2019/react-native-custom-font/ios-add-font-to-info-plist.jpg)

左上にあるプロジェクト名を選択して`TARGETS`も自分のプロジェクトを選択します。上部にあるメニューで`Info`を選択して`Info.plist`の内容を確認します。`Info.plist`に`Fonts provided by application`を追加して上のようにフォントファイルを追加します。

リアクトネイティブ(React Native)プロジェクトをまた実行したら下のようにフォントが適用されたことが確認できます。

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2019/react-native-custom-font/ios-font-applied.jpg" alt="リアクトネイティブ(React Native)カスタムフォントios適用">
</div>

{% include in-feed-ads.html %}

### アンドロイド
アンドロイドでリアクトネイティブ(React Native)プロジェクトを実行したら下記のように基本フォントが適用された画面が見えます。

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2019/react-native-custom-font/android-basic-font.jpg" alt="リアクトネイティブ(React Native)カスタムフォントアンドロイド適用 - 基本フォント">
</div>

アンドロイドはiOSよりもっと簡単に適用できます。`android/app/src/main/assets/fonts`フォルダを生成した後ダウンロードしたフォントファイルをコピーします。

![リアクトネイティブ(React Native)カスタムフォントアンドロイド適用 - フォント追加](/assets/images/category/react-native/2019/react-native-custom-font/android-add-font.jpg)

そしてリアクトネイティブ(React Native)プロジェクトを実行したら下記のようにフォントが適用されたことを確認できます。

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2019/react-native-custom-font/android-font-applied.jpg" alt="リアクトネイティブ(React Native)カスタムフォントアンドロイド適用 - カスタムフォント適用">
</div>

## Githubレポジトリ(Repository)
上の内容で作ったプロジェクトをgithubに公開しています。もし、うまく行かない方はレポジトリ(Repository)をコピー(Clone)して直接確認してみてください。

- githubレポジトリ(Repository): [react_native_custom_font](https://github.com/dev-yakuza/react_native_custom_font){:target="_blank"}

## 完了
これでリアクトネイティブ(React Native)プロジェクトにカスタムフォントを適用する方法について見てみました。アプリを美しく表現するにはやはりフォントもとても重要と思います。皆さんもカスタムフォントを適用してアプリをもっと美しく作ってみてください。
