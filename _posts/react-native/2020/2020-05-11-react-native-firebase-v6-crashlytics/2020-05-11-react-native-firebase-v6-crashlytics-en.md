---
layout: 'post'
permalink: '/react-native/react-native-firebase-v6-crashlytics/'
paginate_path: '/react-native/:num/react-native-firebase-v6-crashlytics/'
lang: 'en'
categories: 'react-native'
comments: true

title: react-native-firebase V6 Crashlytics
description: Let's see how to use react-native-firebase(V6) for Firebase Crashlytics.
image: '/assets/images/category/react-native/2020/react-native-firebase-v6-crashlytics/background.jpg'
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [Install and prepare react-natiev-firebase](#install-and-prepare-react-natiev-firebase)
- [Install library](#install-library)
- [Configure Firebase project](#configure-firebase-project)
- [Completed](#completed)

</div>

## Outline

In this blog post, I will show how to configure `react-native-firebase` to use [Crashlytics](https://firebase.google.com/docs/crashlytics){:rel="nofollow noreferrer" target="_blank"} in [Firebase](https://firebase.google.com/){:rel="nofollow noreferrer" target="_blank"}.

- react-native-firebase(V6): [https://rnfirebase.io/](https://rnfirebase.io/){:rel="nofollow noreferrer" target="_blank"}

This blog post is a series. If you want to know more, see the blog posts below.

- [react-native-firebase V6 installation]({{site.url}}/{{page.categories}}/react-native-firebase-v6-installation/){:target="_blank"}
- react-native-firebase V6 Crashlytics
- [react-native-firebase V6 Admob]({{site.url}}/{{page.categories}}/react-native-firebase-v6-admob/){:target="_blank"}

If you want to know how to use react-native-firebase previous version(V5), see the blog posts below.

- [Firebase Analytics]({{site.url}}/{{page.categories}}/react-native-firebase-analytics/){:target="_blank"}
- [Firebase Crashlytics]({{site.url}}/{{page.categories}}/firebase-crashlytics/){:target="_blank"}
- [Firebase Admob]({{site.url}}/{{page.categories}}/react-native-firebase-admob/){:target="_blank"}
- [Push message via react-native-firebase(V5)]({{site.url}}/{{page.categories}}/react-native-firebase-fcm/){:target="_blank"}

## Install and prepare react-natiev-firebase

see the blog post to install react-native-firebase, and prepare Firebase project.

- [react-native-firebase V6 설치]({{site.url}}/{{page.categories}}/react-native-firebase-v6-installation/){:target="_blank"}

## Install library

execute the command below to install `crashlytics` in `react-native-firebase`.

```bash
npm install --save @react-native-firebase/crashlytics
```

Execute the command below to bind react-native-firebase Crashlytics to iOS project.

```bash
cd ios
pod install
```

## Configure Firebase project

Next, we need to configure Google Firebase project for Crashlytics. Go to Firebase Console, and click `Crashlytics` menu on the left.

![crashlytics add sdk](/assets/images/category/react-native/2020/react-native-firebase-v6-crashlytics/crashlytics-add-sdk.jpg)

Click `Add SDK` on the top to add SDK. Also, change iOS/Android by selecting the project beside `Crashlytics` title, and click `Add SDK` to add iOS, and Android both.

## Completed

Done! We've configured react-native-firebase to use Firebase Crashlytics.

![crashlytics integration](/assets/images/category/react-native/2020/react-native-firebase-v6-crashlytics/crashlytics-integration.jpg)

If you configured react-native-firebase Crashlytics, and start React Native project well, you can see the screen like above.