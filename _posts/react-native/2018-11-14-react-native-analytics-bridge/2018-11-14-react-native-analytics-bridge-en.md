---
layout: 'post'
permalink: '/react-native/react-native-analytics-bridge/'
paginate_path: '/react-native/:num/react-native-analytics-bridge/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'Google Analytics'
description: let's analyze RN(react native) app using Google Analytics.
image: '/assets/images/category/react-native/react-native-analytics-bridge.jpg'
---


## outline
we can analyze RN(react native) app by Google Analytics([Google Analytics](https://marketingplatform.google.com/about/analytics/){:rel="nofollow noreferrer" target="_blank"}). let's see how to analyze RN(react native) by Google Analytics.

## install library
we need to install [GoogleAnalyticsBridge](https://github.com/idehub/react-native-google-analytics-bridge#installation-and-linking-libraries){:rel="nofollow noreferrer" target="_blank"} library to connect Google Analytics to RN(react native) app. execute below code to install ```GoogleAnalyticsBridge```

```bash
npm install --save react-native-google-analytics-bridge
```

and execute below command to link ```GoogleAnalyticsBridge``` library to RN(react native).

```bash
react-native link react-native-google-analytics-bridge
```

we were ready to use react-native-google-analytics-bridge library. let's configure Google Analytics.

## Google Analytics
click below link to go to Google Analytics and login.

- Google Analytics: [https://analytics.google.com/analytics/web/](https://analytics.google.com/analytics/web/){:rel="nofollow noreferrer" target="_blank"}

after login, click ```Admin``` menu on the left bottom of the screen.

![create account for mobile](/assets/images/category/react-native/react-native-analytics-bridge/create-account-for-mobile.png)

click ```+ Create Account``` on the left top of the screen.

![click create account](/assets/images/category/react-native/react-native-analytics-bridge/click-create-account.png)

insert your RN(react native) app information and click ```Get Tracking ID``` on the bottom of the screen.

![insert-app-info](/assets/images/category/react-native/react-native-analytics-bridge/insert-app-info.png)

completed to ready to connect Google Analytics to react-native-google-analytics-bridge library. let's analyze RN(react native) app to use Tracking ID.

## code for analyzation.
insert below code to where you want to analyze RN(react native) app by Google Analytics.

```js
...
import { GoogleAnalyticsTracker } from "react-native-google-analytics-bridge";
...

...
let tracker = new GoogleAnalyticsTracker("UA-12345-1");
tracker.trackScreenView("Home");
...
```

yes, that's all. it's very simple, isn't it? insert your Google Analytics Tracking ID to below code.

```js
new GoogleAnalyticsTracker("your Tracking ID")
```

and then, insert the title of the page to analyze.

```js
tracker.trackScreenView("Home");
```

we inserted above code to ```render()```. we don't know where is best place for this code, so that is your responsibility.

if you want to analyze deeply, see official site to check details about react-native-google-analytics-bridge features.

- [react-native-google-analytics-bridge](https://github.com/idehub/react-native-google-analytics-bridge#usage){:rel="nofollow noreferrer" target="_blank"}

## reference
- official site: [GoogleAnalyticsBridge](https://github.com/idehub/react-native-google-analytics-bridge#installation-and-linking-libraries){:rel="nofollow noreferrer" target="_blank"}
