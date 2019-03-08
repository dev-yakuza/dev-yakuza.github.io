---
layout: 'post'
permalink: '/react-native/react-native-device-info/'
paginate_path: '/react-native/:num/react-native-device-info/'
lang: 'ko'
categories: 'react-native'
comments: true

title: 'react-native-device-info'
description: '유저의 디바이스 정보를 얻기 위해 react-native-device-info 라이브러리를 사용해보자'
image: '/assets/images/category/react-native/react-native-device-info.jpg'
---


## 개요
사용자에 디바이스 정보를 얻기위해 RN 프로젝트 [react-native-device-info](https://github.com/rebeccahughes/react-native-device-info){:rel="nofollow noreferrer" target="_blank" } 라이브러리를 사용해 보자.

## 라이브러리 설치
아래에 명령어로 react-native-device-info을 설치합니다.

{% include_relative common/installation.md %}

설치가 완료되면 아래에 명령어로 react-native-device-info 라이브러리와 프로젝트를 연결합니다.

{% include_relative common/link.md %}

## 사용법
우리는 기본적으로 사용한적이 있는 경우만 블로그로 작성합니다. 따라서 여기에 작성된 내용은 우리가 사용할 때마다 추가될 것입니다.

사용법에 대한 자세한 사항은 공식 홈페이지를 참조하세요.
- 공식 사이트: [react-native-device-info](https://github.com/rebeccahughes/react-native-device-info){:rel="nofollow noreferrer" target="_blank" }

## device locale
device locale을 정보를 가져오는 방법.

```js
...
import DeviceInfo from 'react-native-device-info';
...

export default class Home extends React.Component<Props, State> {
    render() {
        const deviceLocale = DeviceInfo.getDeviceLocale();
        // iOS: "en"
        // Android: "en-US"
        ...
    }
}
```

## Unique ID
앱의 Unique ID를 얻습니다.

```js
...
import DeviceInfo from 'react-native-device-info';
...

export default class Home extends React.Component<Props, State> {
    render() {
        const uniqueID = DeviceInfo.getUniqueID();
        // E98948E4-498D-447B-A750-D632C30461A3
        ...
    }
}
```

## 디바이스 구분
아래에 코드로 앱이 스마트폰에서 기동중인지, 태블릿에서 기동중인지 확인할 수 있습니다.

```js
...
import DeviceInfo from 'react-native-device-info';
...

export default class Home extends React.Component<Props, State> {
    render() {
        const isTablet = DeviceInfo.isTablet();
        // tablet: true / phone: false
        ...
    }
}
```


## 에러 대응
잘 개발을 디바이스에서 랜덤하게 crash가 나는 문제가 발생했다. 시뮬레이터에서도 아래에 같은 메세지가 표시되었다.

```
RCTBridge required dispatch_sync to load RCTDevLoadingView. This may lead to deadlocks
```

위에 문제를 해결하기 위해 아래와 같이 ```libRNDeviceInfo.a```를 제일 하단으로 이동시켜 문제를 해결했다.

![RCTBridge required dispatch_sync to load RCTDevLoadingView. error](/assets/images/category/react-native/react-native-device-info/error.png)

아래에 링크는 에러를 고칠때 참고한 내용입니다.

- [github issue](https://github.com/rebeccahughes/react-native-device-info/issues/260#issuecomment-366835600){:rel="nofollow noreferrer" target="_blank" }

## 참고
- 공식 사이트: [react-native-device-info](https://github.com/rebeccahughes/react-native-device-info){:rel="nofollow noreferrer" target="_blank" }