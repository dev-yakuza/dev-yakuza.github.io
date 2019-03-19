---
layout: 'post'
permalink: '/react-native/ios-app-crash-debugging/'
paginate_path: '/react-native/:num/ios-app-crash-debugging/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'iOS App crash分析'
description: 'iOS App crashログ(Log)を分析する方法について説明します。'
image: '/assets/images/category/react-native/ios-app-crash-debugging.jpg'
---


## 概要
アプリ審査のためアプリを提出したがApp crash理由で拒絶(reject)されました。親切にも拒絶(reject)の理由とcrashログ(log)ファイルを一緒に送ってくらました。こんな感じで貰ったcrashログ(log)ファイルを分析してどこの部分でエラーが発生したかを探す方法に関して説明します。

## アプリ審査拒絶
アップルのアプリ審査が拒絶(reject)されたらメールを送ってくれます。メールを貰ったらアプリストアコネクト(Appstore connect)に移動してアプリ審査拒絶(reject)の理由を確認します。

![アプリ審査拒絶](/assets/images/category/react-native/ios-app-crash-debugging/app_reject.png)

特にアプリ審査拒絶(reject)理由がApp crashだったら下記のようにApp crash logも一緒に送ってくれます。

```
Guideline 2.1 - Performance - App Completeness

We were unable to review your app as it crashed on launch. We have attached detailed crash logs to help troubleshoot this issue.

Next Steps

To resolve this issue, please revise your app and test it on a device to ensure it will launch without crashing.

Resources

For information on how to symbolicate and read a crash log, please review Tech Note TN2151 Understanding and Analyzing Application Crash Reports.


crashlog-CDDAD5F8-F56A-470D-94BA-55149F76E390.txt
crashlog-D75B7641-0AF7-4DF4-8702-2E6665172390.txt
crashlog-3A0F07E3-874D-462F-9FFF-BCE88C98D224.txt
```

アプリ審査拒絶(reject)内容にある[Tech Note TN2151 Understanding and Analyzing Application Crash Reports](https://appstoreconnect.apple.com/WebObjects/iTunesConnect.woa/ra/ng/app/1441741187/platform/ios/resolutioncenter){:rel="nofollow noreferrer" target="_blank"}リンクを確認したら、App crash logを確認する方法について詳しく説明が出ております。

まず、送ってくれたログ(log)ファイルをダウンロードします。

## シンボルファイルダウンロード
App crash logを分析するためにはアプリのシンボルファイル(```dSYM```)が必要です。アプリストアコネクト(Appstore connect)の```Activity```タブに移動します。

![アプリストアコネクトActivityタブ](/assets/images/category/react-native/ios-app-crash-debugging/appstoreconnect_activity.png)

左にある `` `All Builds```を選択してアプリ審査に提出したビルドのバージョンを選択します。

![シンボルファイルダウンロード](/assets/images/category/react-native/ios-app-crash-debugging/appstoreconnect_download_symbol.png)

右下の```Download dSYM```リンクを押してシンボルファイルをダウンロードして圧縮を解除します。

```
7ED9CAAD-F7F7-31E6-8480-2D358FBEF9C7.dSYM
E3430BAD-2EB8-3B8D-8E04-4BB66E2A4E58.dSYM
```

## ログファイル分析
今からアップルが送ったApp crash logファイルを分析してみます。全てのログ(log)ファイルは下記のようなヘッダー(header)を持ってます。

```
Incident Identifier: 3A0F07E3-874D-462F-9FFF-BCE88C98D224
CrashReporter Key:   28b54437587b1ef1e81059e98250b166b0d343c8
Hardware Model:      xxx
Process:             blaboo [2012]
Path:                /private/var/containers/Bundle/Application/488E158A-64B5-439E-82BC-F702CF26E5DA/blaboo.app/blaboo
Identifier:          io.github.dev-yakuza.blaboo
Version:             1 (1.0.6)
AppStoreTools:       10B63
Code Type:           ARM-64 (Native)
Role:                Non UI
Parent Process:      launchd [1]
Coalition:           io.github.dev-yakuza.blaboo [661]


Date/Time:           2018-12-10 17:20:22.0217 -0800
Launch Time:         2018-12-10 17:20:01.9857 -0800
OS Version:          iPhone OS 12.1 (16B92)
Baseband Version:    7.21.00
Report Version:      104

Exception Type:  EXC_CRASH (SIGKILL)
Exception Codes: 0x0000000000000000, 0x0000000000000000
Exception Note:  EXC_CORPSE_NOTIFY
Termination Reason: Namespace SPRINGBOARD, Code 0x8badf00d
Termination Description: SPRINGBOARD, scene-create watchdog transgression: io.github.dev-yakuza.blaboo exhausted real (wall clock) time allowance of 19.94 seconds | ProcessVisibility: Foreground | ProcessState: Running | WatchdogEvent: scene-create | WatchdogVisibility: Foreground | WatchdogCPUStatistics: ( | "Elapsed total CPU time (seconds): 24.600 (user 24.600, system 0.000), 41% CPU", | "Elapsed application CPU time (seconds): 0.237, 0% CPU" | )
Triggered by Thread:  0
```

ヘッダー(header)にある```Exception Type```を[https://appstoreconnect.apple.com/WebObjects/iTunesConnect.woa/ra/ng/app/1441741187/platform/ios/resolutioncenter](https://appstoreconnect.apple.com/WebObjects/iTunesConnect.woa/ra/ng/app/1441741187/platform/ios/resolutioncenter){:rel="nofollow noreferrer" target="_blank"}サイトで確認することで大まかな情報を取得できます。

例えば、```Bad Memory Access [EXC_BAD_ACCESS // SIGSEGV // SIGBUS]```の場合プロセスが有効してないメモリへアクセスしたとかread-onlyメモリに書く動作をした時発生します。

```
Exception Type:  EXC_CRASH (SIGKILL)
Exception Codes: 0x0000000000000000, 0x0000000000000000
Exception Note:  EXC_CORPSE_NOTIFY
Termination Reason: Namespace SPRINGBOARD, Code 0x8badf00d
Termination Description: SPRINGBOARD, scene-create watchdog transgression: io.github.dev-yakuza.blaboo exhausted real (wall clock) time allowance of 19.94 seconds | ProcessVisibility: Foreground | ProcessState: Running | WatchdogEvent: scene-create | WatchdogVisibility: Foreground | WatchdogCPUStatistics: ( | "Elapsed total CPU time (seconds): 24.600 (user 24.600, system 0.000), 41% CPU", | "Elapsed application CPU time (seconds): 0.237, 0% CPU" | )
Triggered by Thread:  0
```

私たちのアプリは```EXC_CRASH (SIGKILL)```でした。このタイプは```Termination Reason```まで確認しないと分からないです。```Termination Reason```コードが```0x8badf00d```です。上にあるリンクで確認すると```The exception code 0x8badf00d indicates that an application has been terminated by iOS because a watchdog timeout occurred.```でタイムアウトされてエラーが発生したと思うられます。

それじゃ、どこでCrashエラーが発生したか探すためターミナル(terminal)を使ってシンボルファイル(dSYM)が存在しているフォルダに移動します。
그럼 어디에서 crash가 발생했는지 찾아보기 위해 터미널(terminal)을 이용해서 심볼 파일(dSYM)이 존재하는 폴더로 이동합니다.

```bash
# ダウンロードしたファイルファ存在するフォルダに移動します。
cd ~/Desktop/crash/
```

そして、アップルが送ったApp crash logファイルを開いて一番上にある内容を確認します。

```
{
    ...
    "slice_uuid":"7ed9caad-f7f7-31e6-8480-2d358fbef9c7",
    ...
}
...

Thread 0 name:  Dispatch queue: com.apple.main-thread
Thread 0 Crashed:
...
10  Security                      	0x00000001e938b6d8 0x1e9314000 + 489176
11  Security                      	0x00000001e938944c 0x1e9314000 + 480332
12  Security                      	0x00000001e938bcd0 0x1e9314000 + 490704
13  blaboo                        	0x0000000100969608 0x10093c000 + 185864
14  blaboo                        	0x000000010096ddf0 0x10093c000 + 204272
15  blaboo                        	0x000000010097190c 0x10093c000 + 219404
...
```

ここにある```slice_uuid```とマッチングされるシンボルファイル(dSYM)を使ってApp crash logを分析します。あと、```Thread 0 Crashed```で自分のアプリ名前が見える部分を探します。

[Tech Note TN2151 Understanding and Analyzing Application Crash Reports](https://appstoreconnect.apple.com/WebObjects/iTunesConnect.woa/ra/ng/app/1441741187/platform/ios/resolutioncenter){:rel="nofollow noreferrer" target="_blank"}のサイトに書いてるコマンドを使って分析する予定です。

```bash
atos -arch arm64 -o TheElements.app.dSYM/Contents/Resources/DWARF/TheElements -l 0x1000e4000 0x00000001000effdc
```

このコマンドを上で調査した内容で変更したら下記のようです。

```bash
# "slice_uuid":"7ed9caad-f7f7-31e6-8480-2d358fbef9c7",
# 13  blaboo                        	0x0000000100969608 0x10093c000 + 185864
# atos -arch arm64 -o [slice_uuid].dSYM/Contents/Resources/DWARF/[AppName] -l [4番目のテキスト: 0x10093c000] [3番目のテキスト: 0x0000000100969608]
atos -arch arm64 -o 7ED9CAAD-F7F7-31E6-8480-2D358FBEF9C7.dSYM/Contents/Resources/DWARF/blaboo -l 0x10093c000 0x0000000100969608
```

上記のコマンドを実行したら下記のような結果が見れます。


```bash
-[FIRInstanceIDAuthKeychain removeItemsMatchingService:account:error:] (in blaboo) + 136
```

上のようにアプリのcrashが発生した部分を大まかに確認することができます。

## 完了
アップルが送ったApp crash logを分析する方法に関して見てみました。私たちのアプリのApp crash logを分析した結果Admobに問題があるみたいで、確認したらファイアベース(Firebase)からダウンロードしたファイル(```GoogleService-Info.plist```)に```ADMOB_APP_ID```が含まれていなくて問題が発生しました。それでファイアベース(Firebase)から新し```GoogleService-Info.plist```ファイルをダウンロードして提供して解決しました。

## ご参考
- Tech Note TN2151 Understanding and Analyzing Application Crash Reports: [https://appstoreconnect.apple.com/WebObjects/iTunesConnect.woa/ra/ng/app/1441741187/platform/ios/resolutioncenter](https://appstoreconnect.apple.com/WebObjects/iTunesConnect.woa/ra/ng/app/1441741187/platform/ios/resolutioncenter){:rel="nofollow noreferrer" target="_blank"}