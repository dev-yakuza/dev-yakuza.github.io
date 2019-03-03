---
layout: 'post'
permalink: '/react-native/react-native-itunes-share-file/'
paginate_path: '/react-native/:num/react-native-itunes-share-file/'
lang: 'ko'
categories: 'react-native'
comments: true

title: 'iTunes 파일 공유 기능'
description: 'iTunes를 통해 RN(React Native)으로 제작한 앱에 파일을 공유하는 방법에 대해서 알아봅니다.'
image: '/assets/images/category/react-native/react-native-itunes-share-file/background.jpg'
---


## 개요
RN(React Native)으로 제작한 앱에 PC에 있는 파일을 iTunes를 통해 넣고 싶은 경우가 있습니다. 예를 들어 [OPlayer](https://itunes.apple.com/app/oplayer-video-player-classic-media-streaming/id344784375?mt=8&ign-mpt=uo%3D8){:rel="nofollow noreferrer" target="_blank"}나 [GomPlayer](https://itunes.apple.com/app/gom-player/id672542880?mt=8){:rel="nofollow noreferrer" target="_blank"}와 같은 비디오 앱은 비디오 파일을 iTunes를 통해 앱에 넣을 수 있습니다.

이 블로그에서는 이렇게 PC에 있는 파일을 iTunes를 통해 앱에 넣는 기능을 알아보겠습니다.


## 기능 설명
어떤 기능인지 아직 잘 모르시는 분들을 위해 추가할 기능에 대해서 조금 더 설명하도록 하겠습니다. 사용하고 있는 iOS 기기를 USB를 통해 PC와 연결하면 iTunes가 활성화됩니다.

![itunes에 휴대폰 연결](/assets/images/category/react-native/react-native-itunes-share-file/connect-itunes.png)

iOS 기기와 PC가 잘 연결되었다면, iTunes 위에 핸드폰 모양에 아이콘이 있습니다. 아이콘을 선택합니다.

![itunes에 휴대폰 정보](/assets/images/category/react-native/react-native-itunes-share-file/iphone-info.png)

iOS 기기의 정보가 보인다면, 왼쪽 메뉴의 ```File Sharing```을 선택합니다. 그러면 iTunes를 통해 파일을 공유할 수 있는 앱들의 리스트가 보입니다.

![itunes 파일 업로드](/assets/images/category/react-native/react-native-itunes-share-file/upload-file.png)

여기에서는 ```OPlayer```를 선택하고, PC에 있는 ```video.mp4``` 파일을 드래그로 업로드했습니다.

이번 블로그에서는 이렇게 앱에서 필요한 파일을 사용자가 iTunes를 통해 PC에서 업로드 할 수 있는 기능을 소개하려고 합니다.


## 디바이스 준비
이 기능을 테스트하기 위해서는 앱을 디바이스에서 설치해야합니다. iOS 디바이스에 앱을 설치하는 방법은 아래에 블로그를 참고하시기 바랍니다.

- [iOS 디바이스 테스트]({{site.url}}/{{page.categories}}/ios-test-on-device/){:target="_blank"}


## info.plist 수정
이 기능은 특별히 소스코드를 수정할 필요가 없습니다. ```info.plist```를 수정하기만 하면 간단하게 iTunes 파일 공유 기능을 추가할 수 있습니다.

RN(React Native)의 ```ios/[project name]/info.plist```를 열고 아래에 내용을 추가합니다.

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

## 파일 활용
위와 같이 ```info.plist```를 수정하는 것 만으로, iTunes를 통한 파일을 업로드하는 기능을 구현할 수 있습니다. 또한, ```react-native-fs```를 활용하면 iTunes를 통해 업로드한 파일을 활용할 수 있습니다.

- [파일 시스템 사용]({{site.url}}/{{page.categories}}/react-native-fs/){:target="_blank"}

iTunes를 통해 업로드한 폴더는 ```react-native-fs```의 ```DocumentDirectoryPath```를 통해 접근할 수 있습니다.


## 시뮬레이터
위에서 설명한 내용으로는 RN(React Native)를 디바이스에 설치하고 iTunes를 통해 파일을 업로드해야 합니다. 그러면 이 기능을 가진 앱은 항상 디바이스에서 테스트해야 할거 같지만, 사실 시뮬레이터에서도 테스트가 가능합니다.

일단 아래에 명령어로 현재 프로젝트를 실행합니다.

```bash
react-native run-ios
```

현재 프로젝트가 설치된 시뮬레이터가 실행되면 아래에 명령어를 통해 시뮬레이터의 id를 구합니다.

```bash
xcrun simctl list | egrep '(Booted)'
```

그리고 ```react-native-device-info``` 라이브러리를 통해 앱의 ```unique id```를 얻습니다.

- [react-native-device-info]({{site.url}}/{{page.categories}}/react-native-device-info/){:target="_blank"}

이렇게 시뮬레이터의 id, 앱의 unique id를 구했다면, ```/Users/[user name]/Library/Developer/CoreSimulator/Devices/[simulator id]/data/Container/Data/Application/[app id]/Documents/``` 폴더에 원하는 파일을 업로드하면 디바이스에 iTunes를 통해 파일을 업로드한 것과 동일하게 동작합니다.


## 완료
음악 앱이나, 영화 앱 등, 유저가 특정 파일을 앱에 iTunes를 통해 넣어야 하는 경우, 어떻게 구현하는지에 대해서 알아보았습니다. 또한 그렇게 업로드한 파일을 접근하는 방법과 시뮬레이터에서 테스트하는 방법까지 알아보았습니다. 여러분도 특정 파일이 필요하지만, 서버가 준비되지 않은 경우, 위와 같은 방법으로 해결해 보시는건 어떨가요