---
published: false
layout: 'post'
permalink: '/react-native/react-native-rate/'
paginate_path: '/react-native/:num/react-native-rate/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'アプリストアレビュー'
description: 'RN(React Native)プロジェクトでreact-native-rateを使ってアプリストアのレビューを作成するように誘導する方法について説明します。'
image: '/assets/images/category/react-native/react-native-rate.jpg'
---


## 概要
RN(React Native)でアプリを開発してリリースしたらアプリストアでレビューを作成してくれた方々が出ました。そのレビューをみたら開発したやりがいも感じるし、ユーザが必要な機能についても理解することができました。しかし、今までは特にアプリ中でアプリレビューを作成するように誘導してないのでアプリレビュー作成を誘導したらもっとたくさんのユーザのご意見を貰うことが出来ると思いました。

このブログでは```react-native-rate```ライブラリを使ってRN(React Native)で開発したアプリからアプリストアレビュー作成を誘導する方法について説明します。

- react-native-rate公式サイト: [https://github.com/KjellConnelly/react-native-rate](https://github.com/KjellConnelly/react-native-rate){:rel="nofollow noreferrer" target="_blank"}

## インストール
RN(React Native)で```react-native-rate```ライブラリを使うため、下記のコマンドで```react-native-rate```ライブラリをインストールします。

```bash
npm install react-native-rate --save
```

## ライブラリ連結
ライブラリインストールが終わったら、下記のコマンドで```react-native-rate```ライブラリをRN(React Native)プロジェクトと連結します。

```bash
react-native link react-native-rate
```

## 使い方
下記のソースコードは[react-native-rate公式サイト](https://github.com/KjellConnelly/react-native-rate){:rel="nofollow noreferrer" target="_blank"}の一部をコピーした内容です。

```js
import Rate, { AndroidMarket } from 'react-native-rate'
...
render() {
    return (
            <Button title="Rate App" onPress={()=>{
                let options = {
                    AppleAppID:"2193813192",
                    GooglePackageName:"com.mywebsite.myapp",
                    AmazonPackageName:"com.mywebsite.myapp",
                    OtherAndroidURL:"http://www.randomappstore.com/app/47172391",
                    preferredAndroidMarket: AndroidMarket.Google,
                    preferInApp:false,
                    openAppStoreIfInAppFails:true,
                    fallbackPlatformURL:"http://www.mywebsite.com/myapp.html",
                }
                Rate.rate(options, success=>{
                    if (success) {
                        // this technically only tells us if the user successfully went to the Review Page. Whether they actually did anything, we do not know.
                        this.setState({rated:true})
                    }
                })
            } />
    )
}
```

このソースを見たらわかると思いますが、アプリレビュー作成を誘導したい時色んなオプションと一緒に```Rate.rate()```を実行すればいいです。下のソースコードは実際私たちが使ってるソースコードの一部です。

```js
import { Alert, AsyncStorage } from 'react-native';
import Rate, { AndroidMarket } from 'react-native-rate';
...
const isAlreadyRate = await AsyncStorage.getItem('isAlreadyRate');
const countStartApp = await AsyncStorage.getItem('countStartApp');
const count = countStartApp ? parseInt(countStartApp) : 1;
...
if (!isAlreadyRate && count % 3 === 0) {
  ...
  Alert.alert('App Rating', 'Please give us your opinion!', [
    {
      text: 'Later',
      onPress: () => console.log('Cancel Pressed'),
      style: 'cancel',
    },
    {
      text: 'OK',
      onPress: () => {
        setTimeout(() => {
          let options = {
            AppleAppID: '***************',
            GooglePackageName: '******************',
            preferredAndroidMarket: AndroidMarket.Google,
            preferInApp: false,
            openAppStoreIfInAppFails: true,
          };
          Rate.rate(options, success => {
            if (success) {
              AsyncStorage.setItem('isAlreadyRate', 'true');
            }
          });
        }, 500);
      },
    },
  ]);
}
await AsyncStorage.setItem('countStartApp', `${count + 1}`);
```

私たちは```AsyncStorage```にアプリレビューをしたかどうかを保存してアプリレビューをしたユーザはアプリレビューの誘導をしないように処理しています。また、アプリの実行回数が3の倍数の場合アプリレビューの誘導ダイアログを表示して既存のUXを邪魔しないようにしています。

上記で見た```react-native-rate```公式サイトソースには色んな設定がありますが、私たちはiOSのアプリストアとアンドロイドのGoogle Playストアだけ使ってるので、```AppleAppID```と```GooglePackageName```オプションだけ使います。AppleAppIDはアプリストアダウンロードリンクのURL後ろの部分を見るか、Appstore Connectにある```アプリ情報```から確認することができます。


## 完了
アプリのロードマップも重要ですが、やはり一番重要なことはユーザのご意見じゃないかなと思います。ユーザがもっと簡単にご意見を伝えることが出来るように案内することもアプリ開発中で重要に考慮する項目じゃないかなと思います。```react-native-rate```を使って皆さんもユーザがもっと簡単に意見を出せるように誘導してみてください。


## 参考
- react-native-rate公式サイト: [https://github.com/KjellConnelly/react-native-rate](https://github.com/KjellConnelly/react-native-rate){:rel="nofollow noreferrer" target="_blank"}