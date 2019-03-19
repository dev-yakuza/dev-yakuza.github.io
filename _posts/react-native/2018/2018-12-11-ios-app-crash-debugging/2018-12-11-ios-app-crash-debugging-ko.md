---
layout: 'post'
permalink: '/react-native/ios-app-crash-debugging/'
paginate_path: '/react-native/:num/ios-app-crash-debugging/'
lang: 'ko'
categories: 'react-native'
comments: true

title: 'iOS App crash 분석'
description: 'iOS App crash 로그(Log)를 분석하는 방법에 대해서 알아봅니다.'
image: '/assets/images/category/react-native/ios-app-crash-debugging.jpg'
---


## 개요
앱 심사를 위해 앱을 제출했지만 App crash 이유로 거절(reject)되었습니다. 친절하게 거절(reject) 이유와 함께 crash 로그(log) 파일을 함께 보내주었습니다. 이렇게 받은 crash 로그(log) 파일을 분석하여 어떤 부분에서 에러가 발생했는지 찾는 방법에 대해서 설명하겠습니다.

## 앱 심사 거절
애플의 앱 심사가 거절(reject)되면 메일을 발송해줍니다. 메일을 받았다면 앱스토어 커넥트(Appstore connect)로 이동하여 앱 심사 거절(reject) 이유를 확인합니다.

![앱 심사 거절](/assets/images/category/react-native/ios-app-crash-debugging/app_reject.png)

특히 앱 심사 거절(reject) 이유가 App crash라면 아래와 같이 App crash log도 함께 보내줍니다.

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

앱 심사 거절(reject) 내용에 첨부되어있는 [Tech Note TN2151 Understanding and Analyzing Application Crash Reports](https://appstoreconnect.apple.com/WebObjects/iTunesConnect.woa/ra/ng/app/1441741187/platform/ios/resolutioncenter){:rel="nofollow noreferrer" target="_blank"} 링크를 확인해보면, App crash log를 확인하는 방법에 대해서 자세히 나와있습니다.

우선 보내준 로그(log) 파일을 다운로드 받습니다.

## 심볼 파일 다운로드
App crash log를 분석하기 위해서는 앱의 심볼 파일(```dSYM```)이 필요합니다. 앱스토어 커넥트(Appstore connect)의 ```Activity```탭으로 이동합니다.

![앱스토어 커넥트 Activity 탭](/assets/images/category/react-native/ios-app-crash-debugging/appstoreconnect_activity.png)

왼쪽에 ```All Builds```를 선택하고 앱 심사에 제출한 빌드의 버전을 선택합니다.

![심볼 파일 다운로드](/assets/images/category/react-native/ios-app-crash-debugging/appstoreconnect_download_symbol.png)

오른쪽 하단에 ```Download dSYM``` 링크를 눌러 심볼 파일을 다운로드하고 압축을 해제합니다.

```
7ED9CAAD-F7F7-31E6-8480-2D358FBEF9C7.dSYM
E3430BAD-2EB8-3B8D-8E04-4BB66E2A4E58.dSYM
```

## 로그 파일 분석
이제 애플에서 보내준 App crash log 파일을 분석해 보겠습니다. 모든 로그(log) 파일은 아래와 같이 헤더(header)를 가지고 있습니다.

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

헤더(header)에 있는 ```Exception Type```을 [https://appstoreconnect.apple.com/WebObjects/iTunesConnect.woa/ra/ng/app/1441741187/platform/ios/resolutioncenter](https://appstoreconnect.apple.com/WebObjects/iTunesConnect.woa/ra/ng/app/1441741187/platform/ios/resolutioncenter){:rel="nofollow noreferrer" target="_blank"} 사이트에서 확인하는 것으로 대략적인 정보를 얻을 수 있습니다.

예를 들어 ```Bad Memory Access [EXC_BAD_ACCESS // SIGSEGV // SIGBUS]```인 경우는 프로세스가 유효하지 않은 메모리에 접근하려했거나 read-only 메모리에 쓰기 동작을 수행할 때 발생합니다.

```
Exception Type:  EXC_CRASH (SIGKILL)
Exception Codes: 0x0000000000000000, 0x0000000000000000
Exception Note:  EXC_CORPSE_NOTIFY
Termination Reason: Namespace SPRINGBOARD, Code 0x8badf00d
Termination Description: SPRINGBOARD, scene-create watchdog transgression: io.github.dev-yakuza.blaboo exhausted real (wall clock) time allowance of 19.94 seconds | ProcessVisibility: Foreground | ProcessState: Running | WatchdogEvent: scene-create | WatchdogVisibility: Foreground | WatchdogCPUStatistics: ( | "Elapsed total CPU time (seconds): 24.600 (user 24.600, system 0.000), 41% CPU", | "Elapsed application CPU time (seconds): 0.237, 0% CPU" | )
Triggered by Thread:  0
```

우리 앱은 ```EXC_CRASH (SIGKILL)```이네요. 이 타입은 ```Termination Reason```까지 확인해야 알 수 있습니다. ```Termination Reason``` 코드가 ```0x8badf00d```입니다. 위에 링크에서 확인해보면 ```The exception code 0x8badf00d indicates that an application has been terminated by iOS because a watchdog timeout occurred.```으로 타임아웃이 떨어져 에러가 발생한것으로 추정됩니다.

그럼 어디에서 crash가 발생했는지 찾아보기 위해 터미널(terminal)을 이용해서 심볼 파일(dSYM)이 존재하는 폴더로 이동합니다.

```bash
# 다운로드한 파일이 존재하는 폴더로 이동합니다.
cd ~/Desktop/crash/
```

그리고 애플이 보내준 App crash log 파일을 열고 제일 상단에 내용을 확인합니다.

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

여기에 표시된 ```slice_uuid```와 매칭이되는 심볼 파일(dSYM)을 이용해서 App crash log를 분석합니다. 또한 ```Thread 0 Crashed```에서 자신의 앱 이름가 보이는 부분을 찾습니다.

[Tech Note TN2151 Understanding and Analyzing Application Crash Reports](https://appstoreconnect.apple.com/WebObjects/iTunesConnect.woa/ra/ng/app/1441741187/platform/ios/resolutioncenter){:rel="nofollow noreferrer" target="_blank"} 사이트에서 소개된 아래에 명령어를 통해 분석을 할 예정입니다.

```bash
atos -arch arm64 -o TheElements.app.dSYM/Contents/Resources/DWARF/TheElements -l 0x1000e4000 0x00000001000effdc
```

이 명령어를 위에서 조사한 내용으로 변경하면 아래와 같습니다.

```bash
# "slice_uuid":"7ed9caad-f7f7-31e6-8480-2d358fbef9c7",
# 13  blaboo                        	0x0000000100969608 0x10093c000 + 185864
# atos -arch arm64 -o [slice_uuid].dSYM/Contents/Resources/DWARF/[AppName] -l [4번째 문자열: 0x10093c000] [3번째 문자열: 0x0000000100969608]
atos -arch arm64 -o 7ED9CAAD-F7F7-31E6-8480-2D358FBEF9C7.dSYM/Contents/Resources/DWARF/blaboo -l 0x10093c000 0x0000000100969608
```

위와 같이 명령어를 입력하면 아래와 같은 결과를 볼 수 있습니다.

```bash
-[FIRInstanceIDAuthKeychain removeItemsMatchingService:account:error:] (in blaboo) + 136
```

위와 같이 앱의 crash가 발생한 부분을 대략적으로 확인할 수 있습니다.

## 완료
애플이 보내준 App crash log를 분석하는 방법에 대해서 알아봤습니다. 우리 앱의 App crash log를 분석해본 결과 Admob에서 문제가 발생하는 것 같아 확인해 본 결과 파이어베이스(Firebase)에서 다운받은 파일(```GoogleService-Info.plist```)에 ```ADMOB_APP_ID```가 포함되어 있지 않았었습니다. 그래서 파이어베이스(Firebase)에서 새롭게 ```GoogleService-Info.plist``` 파일을 다운로드받아 적용했습니다.

## 참고
- Tech Note TN2151 Understanding and Analyzing Application Crash Reports: [https://appstoreconnect.apple.com/WebObjects/iTunesConnect.woa/ra/ng/app/1441741187/platform/ios/resolutioncenter](https://appstoreconnect.apple.com/WebObjects/iTunesConnect.woa/ra/ng/app/1441741187/platform/ios/resolutioncenter){:rel="nofollow noreferrer" target="_blank"}