---
layout: 'post'
permalink: '/react-native/react-native-firebase-analytics/'
paginate_path: '/react-native/:num/react-native-firebase-analytics/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'Firebase Analytics'
description: 'react-native-firebaseライブラリを使ってもっと詳しくアプリを分析してみましょう。'
image: '/assets/images/category/react-native/react-native-firebase-analytics.jpg'
---


## 概要
以前のブログ[Firebase Admob]({{site.url}}/{{page.categories}}/react-native-firebase-admob/){:target="_blank"}で```react-native-firebase```を設定する方法を説明しました。以前のブログでも話ししましたが、ファイアベースアナリティクス(Firebase Analytics)は```react-native-firebase```を設定するだけで自動に分析をしてくれます。しかし、私たちが実際ファイアベースアナリティクス(Firebase Analytics)で分析結果を見た結果、自動で分析されたものでは足りないところが多くて今回のブログを作成することにしました。

今回のブログでは```react-native-firebase```を使ってファイアベースアナリティクス(Firebase Analytics)でもっと詳しく分析するための方法について説明します。

## ライブラリ設定
ここで説明する内容は```react-native-firebase```ライブラリを使ってファイアベースアナリティクス(Firebase Analytics)です。したがって、基本的に```react-native-firebase```を設定する必要があります。```react-native-firebase```を設定する方法は以前のブログ[Firebase Admob]({{site.url}}/{{page.categories}}/react-native-firebase-admob/){:target="_blank"}を参考してください。このブログでは```react-native-firebase```ライブラリ設定については省略します。

## デバッグビュー(DebugView)
ファイアベースアナリティクス（Firebase Analytics）はアプリが記録するイベントを約1時間の間に収集した後、一括アップロードします。したがって、分析されたデータを見るためには約1時間の時間を待てる必要があります。しかし、開発する時、テストする時こんな時間を待てる時間がないです。だから、ファイアベースアナリティクス(Firebase Analytics)はデバッグが可能なデバッグビュー(DebugView)を提供してます。デバッグビュー(DebugView)を利用したら収集したデータのアップロード時間を最小化してほぼリアルタイムで分析をすることができます。

今後```react-native-firebase```ライブラリの機能を使ってファイアベースアナリティクス(Firebase Analytics)で追加する分析機能たちをすぐに確認できるようにデバッグビュー（DebugView)を設定して進めます。

### iOS
ファイアベースアナリティクス(Firebase Analytics)でデバッグビュー(DebugView)機能を使うためにiOSで下記のような設定をします。

- RN(react native)プロジェクトフォルダで```ios/[project].xcworkspace```ファイルを開いてxcodeを実行します。
- 上部のメニューの```Product``` > ```Scheme``` > ```Edit Scheme...```を選択します。
    ![xcode edit scheme](/assets/images/category/react-native/react-native-firebase-analytics/edit-scheme.png)
- アクティブされた```Edit schema...```ウィンドウの左メニュー中で```Run```を選択して右の```Arguments```タブを選択します。
    ![edit scheme arguments](/assets/images/category/react-native/react-native-firebase-analytics/edit-scheme-arguments.png)
- 選択した```Arguments```タブ中にある```Arguments Passed On Launch```の```+```ボタンを押して下の内容を追加します。(マイナス(```-```)符号も一緒にコピペします。)
    ```bash
    -FIRDebugEnabled
    ```
    ![edit scheme arguments FIRDebugEnabled](/assets/images/category/react-native/react-native-firebase-analytics/edit-scheme-FIRDebugEnabled.png)

### Android
アンドロイドはiOSよりもっとシンプルです。アンドロイドエミュレータ(Android Emulator)やデバイス(Device)を起動して下記のコマンドを実行します。

```bash
adb shell setprop debug.firebase.analytics.app <package_name>
```

ファイアベースアナリティクス(Firebase Analytics)の```DebugView```を中止したいときは下のコマンドを実行します。

```bash
adb shell setprop debug.firebase.analytics.app .none.
```

### テスト
まずファイアベースコンソル(Firebase Console)のファイアベースアナリティクス(Firebase Analytics)の```DebugView```メニューへ移動します。

![firebase analytics debugview](/assets/images/category/react-native/react-native-firebase-analytics/firebase-analytics-debugview.png)

現在はiOS, Android両方起動してない状態ですので```DebugView```が待機状態であります。iOSやアンドロイドを起動します。

![firebase analytics debugview analytics](/assets/images/category/react-native/react-native-firebase-analytics/debugview-analytics.png)

しばらくして上のようなほぼリアルタイムで分析される画面が見えます。

## 画面分析
ファイアベースアナリティクス(Firebase Analytics)でユーザがどんな画面を見たかを記録してくれる```screen_view```と呼ぶイベント(Event)があります。

ファイアベースコンソル(Firebase Console)で```Analytics```の```Events```メニューを選択したら下のような画面が見えます。

![google firebase console Analytics Events menu](/assets/images/category/react-native/react-native-firebase-analytics/analytics-events.png)

画面に見える```Event```リストで```screen_view```を選択します。

![Firebase Analytics Events screen_view](/assets/images/category/react-native/react-native-firebase-analytics/analytics-events-screen_view.png)

少しスクロールして下に行ったら```User engagement``` > ```Screen classs```の項目が見えます。

![Firebase Analytics Events screen_view screen class to screen name](/assets/images/category/react-native/react-native-firebase-analytics/screen_view-class-to-name.png)

User engagementを```Screen class```から```Screen name```で変更します。

![Firebase Analytics Events screen name no data](/assets/images/category/react-native/react-native-firebase-analytics/screen_name-no-data.png)

ここまで来たらなんか足りないことを感じると思います。```Screen class```では本当に基本になるclassだけ確認されて```Screen name```には何もデータがなくユーザがどんな画面を見たかが分析出来ないです。

それで私たちは```react-native-firebase```が提供してる```setCurrentScreen```を使ってユーザが見た画面を分析することにしました。

私たちは分析したいアプリの画面へ下記のようなコードを追加しました。

```js
render() {
    firebase.analytics().setCurrentScreen('HOME');
    ...
    return (
        ...
    );
}
```

react-native-firebaseが提供する```setCurrentScreen```でアプリの画面の名前を入力します。

そしてテストして分析されたら下記のように私たちが```setCurrentScreen```で入力したアプリの画面の名前を確認することができます。

![Firebase Analytics Events screen name with data](/assets/images/category/react-native/react-native-firebase-analytics/screen_name-with-data.png)

ファイアベースアナリティクス(Firebase Analytics)の```DebugView```でもリアルタイムで分析されることを確認することができます。

![Firebase Analytics Events screen name on debug view](/assets/images/category/react-native/react-native-firebase-analytics/screen_name-on-debugview.png)

DebugViewでそのイベント(screen_view)を選択したら上のような詳細画面が見えます。


## カスタムイベント分析
上に紹介しした```setCurrentScreen```ではユーザが見た画面の分析はできますが、その画面でユーザが何のアクションをしたかはわかりません。今回は```logEvent```を使ってファイアベースアナリティクス(Firebase Analytics)でカスタムイベント(Custom Event)を分析する方法を説明します。

私たちはファイアベースアナリティクス(Firebase Analytics)で分析したいカスタムイベント(Custom Event)を下のコードを使って追加しました。

```js
private _onSpeech = (Tts, text: string) => {
    firebase.analytics().logEvent('onPressSoundButton', { target: text });
    ...
}
```

logEventは最初パラメータは英語100文字と特殊文字アンダーバー(_)のみで使えます。(```up to 100 characters is the maximum character length supported for event parameters.```)しかし、私たちのアプリは多言語を提供してますのでどの言語でどんなアクションをしたかを分析したくなりました。そして２つ目のパラメータを使ってカスタムイベント(Custom Event)でカスタムパラメータ(Custom Parameter)を追加しました。２つ目のパラメータはオブジェクト(Object)タイプですので自由にカスタムパラメータ(Custom Parameter)を作って分析に活用することができます

上のようにカスタムイベント(Custom Event)へカスタムパラメータ(Custom Parameter)を追加したらファイアベースコンソル(Firebase Console)でも追加する必要があります。

![Firebase Analytics Events custom event](/assets/images/category/react-native/react-native-firebase-analytics/custom-event-custom-parameter.png)

上のように```Analytics```メニューの```Events```へ移動してイベント(Event)リスト中で追加したカスタムイベント(Custom Event)へマウスを移動します。

![Firebase Analytics custom parameter menu](/assets/images/category/react-native/react-native-firebase-analytics/custom-parameter-menu.png)

マウスを移動したらその項目の右へ```...```ボタンが表示されます。そのボタンを押して見えるメニューの```Edit parameter reporting```を選択します。

![Firebase Analytics custom parameter edit parameter reporting](/assets/images/category/react-native/react-native-firebase-analytics/custom-parameter-edit-parameter-reporting.png)

左にある検索バーへ分析したいカスタムイベント(Custom Event)のカスタムパラメータ(Custom Parameter)を入力して```ADD```を押してカスタムパラメータ(Custom Parameter)を追加します。

![Firebase Analytics add custom parameter](/assets/images/category/react-native/react-native-firebase-analytics/add-custom-parameter.png)

追加が完了されたらテストを進めます。データが溜まった後（約1日）、```Events```メニューで追加したカスタムイベント(Custom Event)を選択します。

![Firebase Analytics custom parameter](/assets/images/category/react-native/react-native-firebase-analytics/custom-parameter.png)

少しスクロールして下に行くと私たちが追加したカスタムパラメータ(Custom Parameter)の分析結果を確認することができます。

![Firebase Analytics custom parameter result](/assets/images/category/react-native/react-native-firebase-analytics/custom-parameter-result.png)

ファイアベースアナリティクス(Firebase Analytics)の```DebugView```でもリアルタイムで分析されることが確認できます。

![Firebase Analytics Events custom event on debug view](/assets/images/category/react-native/react-native-firebase-analytics/custom_event-on-debugview.png)

DebugViewでそのカスタムイベント(Custom Event)を選択したら上のように追加したカスタムパラメータ(Custom Parameter)が一緒に見える詳細画面が見えます。

## 参考
- ファイアベースデバッグイベント: [https://firebase.google.com/docs/analytics/debugview](https://firebase.google.com/docs/analytics/debugview){:rel="nofollow noreferrer" target="_blank"}
- react-native-firebase: [https://rnfirebase.io/docs/v5.x.x/analytics/reference/analytics](https://rnfirebase.io/docs/v5.x.x/analytics/reference/analytics){:rel="nofollow noreferrer" target="_blank"}