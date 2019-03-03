---
layout: 'post'
permalink: '/react-native/react-native-itunes-share-file/'
paginate_path: '/react-native/:num/react-native-itunes-share-file/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'iTunesファイルシェア機能'
description: 'iTunesを使ってRN(React Native)で開発したアプリへファイルをシェアする方法について説明します。'
image: '/assets/images/category/react-native/react-native-itunes-share-file/background.jpg'
---


## 概要
RN(React Native)で作成したアプリへPCにあるファイルをiTunesを使って入れたい場合があります。例えば[OPlayer](https://itunes.apple.com/app/oplayer-video-player-classic-media-streaming/id344784375?mt=8&ign-mpt=uo%3D8){:rel="nofollow noreferrer" target="_blank"}や[GomPlayer](https://itunes.apple.com/app/gom-player/id672542880?mt=8){:rel="nofollow noreferrer" target="_blank"}みたいにビデオアプリはビデオファイルをiTunesを使ってアプリへ入れることができます。

このブログではこのようにPCにあるファイルをiTunesを使ってアプリへ入れる機能を説明します。


## 機能説明
どのような機能か分からない方のため追加する機能についてもうちょっと説明します。使ってるiOSのデバイスをUSBを使ってPCと連結したらiTunesが実行されます。

![itunesとデバイス連結](/assets/images/category/react-native/react-native-itunes-share-file/connect-itunes.png)

iOSデバイスとPCが上手く連結されたら、iTunes上に携帯形のアイコンが出ます。このアイコンを洗濯します。

![itunesの携帯情報](/assets/images/category/react-native/react-native-itunes-share-file/iphone-info.png)

iOSデバイスの情報が見えたら、左メニューの```File Sharing```を選択します。そしたらiTunesを使ってファイルを共有することができるアプリのリストが見えます。

![itunesファイルアップロード](/assets/images/category/react-native/react-native-itunes-share-file/upload-file.png)

ここでは```OPlayer```を選択して、PCにある```video.mp4```ファイルをドラッグしてアップロードしました。

このブログではこのようにアプリ中で使うファイルをユーザがiTunesを使ってPCからアップロードできる機能を紹介します。


## デバイス準備
この機能をテストするためにはアプリをデバイスにインストールする必要があります。iOSデバイスにアプリをインストールする方法については下記のブログを参考してください。

- [iOSデバイステスト]({{site.url}}/{{page.categories}}/ios-test-on-device/){:target="_blank"}


## info.plist修正
この機能は特にソースコードを修正する必要がありません。```info.plist```を修正することで簡単にiTunesファイルシェア機能を追加することができます。

RN(React Native)の```ios/[project name]/info.plist```を開いて下記の内容を追加します。

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    ...
    <key>UIFileSharingEnabled</key>
    <true/>
    ...
</dict>
</plist>
```

## ファイル活用
上記のように```info.plist```を修正するだけで、iTunesを使ってファイルアップロードする機能を実装できます。また、```react-native-fs```を活用したらiTunesを使ってアップロードしたファイルを活用することができます。

- [ファイルシステム使い方]({{site.url}}/{{page.categories}}/react-native-fs/){:target="_blank"}

iTunesを使ってアップロードしたフォルダは```react-native-fs```の```DocumentDirecotryPath```を使ってアクセスすることができます。


## シミュレータ
上で説明した内容はRN(React Native)をデバイスへインストールしてiTunesを使ってファイルをアップロードしなければならないです。そしたら、この機能を持ってるアプリはいつもデバイスでテストしなければならないみたいですが、実際はシミュレータでもテストが可能です。

一旦下記のコマンドで現在のプロジェクトを実行します。

```bash
react-native run-ios
```

現在のプロジェクトがインストールされたシミュレータが実行されたら下記のコマンドを使ってシミュレータのidを取得します。

```bash
xcrun simctl list | egrep '(Booted)'
```

そして```react-native-device-info```ライブラリを使ってアプリの```unique id```を取得します。

- [react-native-device-info]({{site.url}}/{{page.categories}}/react-native-device-info/){:target="_blank"}

このようにシミュレータのidアプリのunique idを取得したら、```/Users/[user name]/Library/Developer/CoreSimulator/Devices/[simulator id]/data/Container/Data/Application/[app id]/Documents/```のフォルダへファイルをアップロードしたらデバイスにiTunesを使ってファイルアップロードした時と同じように動作します。


## 完了
音楽アプリや、動画アプリなど、ユーザが特定ファイルをアプリにiTunesを使って入れる場合、どう実装するかを説明しました。また、このようにアップロードしたファイルをアクセスする方法やシミュレータでテストする方法まで調べ見ました。皆さんも特定ファイルが必要ですが、サーバーがない場合、上の方法で解決してみたらどうでしょうか。