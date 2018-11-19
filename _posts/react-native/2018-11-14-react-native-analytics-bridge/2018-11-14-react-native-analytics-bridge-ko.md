---
layout: 'post'
permalink: '/react-native/react-native-analytics-bridge/'
paginate_path: '/react-native/:num/react-native-analytics-bridge/'
lang: 'ko'
categories: 'react-native'
comments: true

title: 'Google Analytics'
description: 'RN(react native)로 개발한 앱을 구글 애널리틱스(Google Analytics)를 이용하여 앱을 분석해 봅시다.'
image: '/assets/images/category/react-native/react-native-analytics-bridge.jpg'
---


## 개요
구글 애널리틱스([Google Analytics](https://marketingplatform.google.com/about/analytics/){:rel="nofollow noreferrer" target="_blank"})를 사용하여 RN(react native)로 제작한 앱을 분석할 수 있습니다. 구글 애널리틱스(Google Analytics)를 이용하여 RN(react native)를 분석해 봅시다.

## 라이브러리 설치
RN(react native)와 구글 애널리틱스(Google Analytics)를 연동하기 위해서는 [GoogleAnalyticsBridge](https://github.com/idehub/react-native-google-analytics-bridge#installation-and-linking-libraries){:rel="nofollow noreferrer" target="_blank"} 라이브러리를 설치해야 합니다. 아래에 코드를 이용하여 ```GoogleAnalyticsBridge``` 라이브러리를 설치해 주십시오.

```bash
npm install --save react-native-google-analytics-bridge
```

아래에 명령어로 RN(react native)와 ```GoogleAnalyticsBridge```를 연결합니다.

```bash
react-native link react-native-google-analytics-bridge
```

react-native-google-analytics-bridge 라이브러리를 사용할 준비가 되었습니다. 이제 구글 애널리틱스(Google Analytics)에 연동할 준비를 해야합니다.

## Google Analytics
아래에 링크를 눌러 구글 애널리틱스(Google Analytics)로 이동하여 로그인합니다.

- 구글 애널리틱스(Google Analytics): [https://analytics.google.com/analytics/web/](https://analytics.google.com/analytics/web/){:rel="nofollow noreferrer" target="_blank"}

로그인후 왼쪽 하단의 ```Admin``` 메뉴를 선택합니다.

![create account for mobile](/assets/images/category/react-native/react-native-analytics-bridge/create-account-for-mobile.png)

왼쪽 상단의 ```+ Create Account```를 선택합니다.

![click create account](/assets/images/category/react-native/react-native-analytics-bridge/click-create-account.png)

RN(react native)로 만든 자신의 앱 정보를 입력하고 제일 하단에 있는 ```Get Tracking ID```버튼을 눌러 트랙킹 아이디(Tracking ID)를 생성합니다.

![insert-app-info](/assets/images/category/react-native/react-native-analytics-bridge/insert-app-info.png)

react-native-google-analytics-bridge 라이브러리와 구글 애널리틱스(Google Analytics)를 연동하기 위한 준비가 끝났습니다. 이제 실제로 트랙킹 아이디(Tracking ID)를 이용하여 RN(react native)로 만든 앱을 분석해 보도록하겠습니다.

## 분석 코드
RN(react native)로 개발된 프로젝트에서 구글 애널리틱스(Google Analytics)로 분석하고 싶은 페이지에 아래의 코드를 추가합니다.

```js
...
import { GoogleAnalyticsTracker } from "react-native-google-analytics-bridge";
...

...
let tracker = new GoogleAnalyticsTracker("UA-12345-1");
tracker.trackScreenView("Home");
...
```

네, 이제 전부입니다. 간단하죠? 아래 코드에 자신의 구글 애널리틱스(Google Analytics) 트랙킹 아이디(Tracking ID)를 입력합니다.

```js
new GoogleAnalyticsTracker("자신의 트랙킹 아이디")
```

트랙킹 하고 싶은 페이지를 식별하기 위한 제목을 입력해 줍니다.

```js
tracker.trackScreenView("Home");
```

우리는 이 코드를 ```render()```함수에서 사용하고 있습니다. 어디가 적절한 위치인지는 여러분이 판단해서 추가하면 될거 같습니다.

좀 더 깊은 분석을 하고 싶은 분은 공식 홈페이지를 참조해서 react-native-google-analytics-bridge의 다양한 기능을 활용해 보세요.

- [react-native-google-analytics-bridge](https://github.com/idehub/react-native-google-analytics-bridge#usage){:rel="nofollow noreferrer" target="_blank"}

## 알림
우리는 앱 분석뿐만아니라 구글 파이어베이스(Google firebase)의 다양한 기능을 사용하기 위해서 react-native-firebase를 통해 앱을 분석하기로 했습니다. 다른 기능을 위해 react-native-firebase 라이브러리를 설정하기만 해도 자동으로 앱을 분석해줍니다. react-native-firebase 라이브러리 설정에 관해서는 [Firebase Admob]({{site.url}}/{{page.categories}}/react-native-firebase-admob/){:target="_blank"} 블로그를 참고하시기바랍니다.

## 참고
- 공식 사이트: [GoogleAnalyticsBridge](https://github.com/idehub/react-native-google-analytics-bridge#installation-and-linking-libraries){:rel="nofollow noreferrer" target="_blank"}
