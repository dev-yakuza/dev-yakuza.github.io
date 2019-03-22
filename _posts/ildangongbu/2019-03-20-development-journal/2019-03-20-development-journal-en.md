---
layout: 'post'
permalink: '/ildangongbu/development-journal/'
paginate_path: '/ildangongbu/:num/development-journal/'
lang: 'en'
categories: 'ildangongbu'
comments: true

title: '「일단공부(Il-Dan-Gong-Bu)」 App Development Journal(RN, React Native)'
description: I've use RN(React Native) to develop the App called 「일단공부(Il-Dan-Gong-Bu)」. in here, I've written the development journal about this app.
image: '/assets/images/category/ildangongbu/background.png'
---

## Outline
this is my third application by RN(React Native). the links below are the app development journal about my previous applications. if you want to know more details, please check it out.

- [BlaBoo App Development Journal(RN, React Native)]({{site.url}}/blaboo/development-journal/){:target="_blank"}
- [Kumoncho App Development Journal(RN, React Native)]({{site.url}}/kumoncho/development-journal/){:target="_blank"}

this application is for only Koreans who want to learn Japanese words, so I think you guys don't need this. I just hope this development journal is interesting to you.


## what is 「일단공부(Il-Dan-Gong-Bu)」?
Koreans can study JLPT Japanese words by level on 「일단공부(Il-Dan-Gong-Bu)」, alos this app has a review feature to memorize the words.

- 「일단공부(Il-Dan-Gong-Bu)」 introduce web page: [「일단공부(Il-Dan-Gong-Bu)」](https://dev-yakuza.github.io/app/ildangongbu/){:target="_blank"}

you can download the app via the links below.

<div class="download_link_container">
    <a class="download_link_ios" href="https://itunes.apple.com/app/id1456091125" target="_blank">
        <img src="/assets/images/apple_download.png" alt="JLPT Japanese words app, 「일단공부(Il-Dan-Gong-Bu)」 ios download"/>
    </a>
    <a class="download_link_android" href="https://play.google.com/store/apps/details?id=io.github.dev.yakuza.ildangongbu" target="_blank">
        <img src="/assets/images/google play_download.png" alt="JLPT Japanese words app, 「일단공부(Il-Dan-Gong-Bu)」 Android download"/>
    </a>
</div>


## Why did I make it?
I am Korean who lives in Japan. normally, I study Japanese words on the subway with the word book. I think you heard about Japanese subway. if you don't, just see this link([https://www.kawaiikakkoiisugoi.com/2011/06/14/tokyo-subway-packers-push-people-around/](https://www.kawaiikakkoiisugoi.com/2011/06/14/tokyo-subway-packers-push-people-around/){:rel="nofollow noreferrer" target="_blank"}). not everyday, not every subways, but it's very hard to study on the train. and the book has Japanese words and Korean meanings, so I try not to see the meanings but my eyes catch it...

so I want to simple app that makes me study Japanese on the train!

![JLPT Japanese words app, 「일단공부(Il-Dan-Gong-Bu)」 ](/assets/images/category/ildangongbu/background.png)


## App Planning
I just set MVP(Minimum Viable Product) like below.

1. show JLPT Japanese words by Level
1. show the amount to study one day(15 words)
1. show Japanese word list without the meanings.
1. if users click the show meaning button, the meaning is shown up.
1. if click the meaning, the app reads the word.
1. the app has the test feature to review the words
1. if users have wrong words in the test, the app shows the wrong word list.
1. the review feature by level and all words.
1. in the review feature, the words that are often wrong are shown up often.

it looks the app has many features. I tried to make the simple app, but I want to use it by myself, so I added various of the features. actually, I wanted to add more...but at a first, MVP, MVP!

## Design
my design sense is zero...I made many patterns and colors to find fittable with my app...still, the design is difficult for me.

![JLPT Japanese words app 「일단공부(Il-Dan-Gong-Bu)」 design](/assets/images/category/ildangongbu/development-journal/ildangongbu-design.png)

I used `sketchapp` for the design. and I choose the best simple design in my patterns and removed some screen.

![JLPT Japanese words app 「일단공부(Il-Dan-Gong-Bu)」 final design](/assets/images/category/ildangongbu/development-journal/ildangongbu-final-design.png)

I respect the designers!


## App Development
of course, I've used RN(React Native) for the app development. 「일단공부(Il-Dan-Gong-Bu)」 is based on RN(```React Native```) and ```typescript```.

- how to install RN(React Native): [RN installation]({{site.url}}/react-native/installation/){:target="_blank"}
- how to apply typescript to RN(React Native): [typescript]({{site.url}}/react-native/typescript/){:target="_blank"}

also, I've used ```NativeBase``` for basic UI and ```styled-components``` for styling.

- how to use NativeBase in RN(React Native): [nativebase]({{site.url}}/react-native/nativebase/){:target="_blank"}
- how to use styled-components in RN(React Navtive): [styled-components]({{site.url}}/react-native/styled-components/){:target="_blank"}

I choose ```react-navigation``` for 「일단공부(Il-Dan-Gong-Bu)」 navigation system.

- how to use react-navigation: [react-navigation]({{site.url}}/react-native/react-navigation/){:target="_blank"}

I've use ```react-native-tts``` to implement ```TTS(Text To Speech)``` for developing voice feature which is one of MVP(Minimum Viable Product) feautes.

- how to use react-native-tts: [react-native-tts]({{site.url}}/react-native/react-native-tts/){:target="_blank"}

I used sqlite DB for the words and deployed the app with it. if you want to know how to use sqlite in RN(React Native), see the link below.

- how to use react-native-sqlite-storage: [react-native-sqlite-storage]({{site.url}}/react-native/react-native-sqlite-storage/){:target="_blank"}

finally, I use Google Firebase to analyze the app and use Google Admob for the advertisement. I use ```react-native-firebase``` for these features.

- how to use react-native-firebase for admob: [react-native-firebase-admob]({{site.url}}/react-native/react-native-firebase-admob/){:target="_blank"}
- how to use react-native-firebase for analytics: [react-native-firebase-analytics]({{site.url}}/react-native/react-native-firebase-analytics/){:target="_blank"}
- how to use react-native-firebase for Crasylytics: [firebase-crashlytics]({{site.url}}/react-native/firebase-crashlytics/){:target="_blank"}


## Lastly
this app is so simple. the design took a long time in this project. also, `react-native-sqlite-storage` has a performance issue on Android. my app loads the data from local, but looks like loading from the server. I'm not sure my code is the best way for the performance...I'll tune the sql statement again. if it has still the problem, I'll check the source code of the library.


this app is for Koreans...so, just download it to check how you can use RN(React Native).

<div class="download_link_container">
    <a class="download_link_ios" href="https://itunes.apple.com/app/id1456091125" target="_blank">
        <img src="/assets/images/apple_download.png" alt="JLPT Japanese words app, 「일단공부(Il-Dan-Gong-Bu)」 ios download"/>
    </a>
    <a class="download_link_android" href="https://play.google.com/store/apps/details?id=io.github.dev.yakuza.ildangongbu" target="_blank">
        <img src="/assets/images/google play_download.png" alt="JLPT Japanese words app, 「일단공부(Il-Dan-Gong-Bu)」 Android download"/>
    </a>
</div>