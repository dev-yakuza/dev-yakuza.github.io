---
layout: 'post'
permalink: '/blaboo/development-journal/'
paginate_path: '/blaboo/:num/development-journal/'
lang: 'en'
categories: 'blaboo'
comments: true

title: 'BlaBoo App Development Journal(RN, React Native)'
description: I've use RN(React Native) to develop the App called BlaBoo. in here, I've written the development journal about this app.
image: '/assets/images/category/blaboo/background.png'
---


## Outline
I've studied RN(React Native) so far, but I've never developed the app from start to finish. so I've decided to work on this project by using RN(React Native) to develop the app fastly from start to finish.

## What is BlaBoo?
BlaBoo is a word study app for baby/children that combines the word ```blah blah``` with the word ```boo```.

- BlaBoo introduction page: [BlaBoo](https://dev-yakuza.github.io/app/blaboo/en/){:target="_blank"}

below is BlaBoo's download links.

<div class="download_link_container">
    <a class="download_link_ios" href="https://itunes.apple.com/app/blaboo/id1441741187" target="_blank">
        <img src="/assets/images/apple_download.png" alt="learning words app for children, blaboo iOS download"/>
    </a>
    <a class="download_link_android" href="https://play.google.com/store/apps/details?id=io.github.dev.yakuza.blaboo" target="_blank">
        <img src="/assets/images/google play_download.png" alt="learning words app for children, blaboo Android download"/>
    </a>
</div>

baby/children see the illustrations and if they touch them, the app reads the word with sound.

![BlaBoo for baby/children word study app - development journal](/assets/images/category/blaboo/development-journal/app_concept.png)

## Why did I make it?
actually, there are many word study applications for baby/children. the main focus of this app is the following.

1. to develop the word study app which baby/children can learn foreign languages.
1. to develop and distribute the app with RN(React Native) I studied so far.

living in a foreign country, I looked for many apps to teach my child foreign language and mother tongue, but there were few apps that provide multiple languages in one app. I found the problem and I have a skill to solve it so I decided to make it.

## App Planning
however I didn't have enough time to make the app by myself.so first, I've been benchmarking various apps, and define MVP(Minimum Viable Product) of the app. BlaBoo MVP(Minimum Viable Product) is following.

1. various categories: define categories and choose the words in the category to be displayed.(ex> cars, fruit, vegetable)
1. display the word by the illustration: display the word by the illustration to interest baby/children.
1. support the voice of the word if it is touched: if baby/children touch the illustration, the app reads the word with the voice to make baby/children learn the word alone naturally.
1. support multiple languages: support multiple languages so baby/children can learn one word in several languages.

this is how I define MVP(Minimum Viable Product) and I've sketched the app to design user's movement in the app.

![BlaBoo for baby/children word study app - sketch](/assets/images/category/blaboo/development-journal/hand_sketch.png)

I've downloaded the sketch template in below site.

- [http://sneakpeekit.com/](http://sneakpeekit.com/){:rel="nofollow noreferrer" target="_blank"}

since I made an app as a hobby alone, the planning is not that big. goal, target, business...put them in and just thought simple features and rough sketch. even so I have tried to make my own hypothesis and list what to do, but I am not sure if I should call it a planning.

![BlaBoo for baby/children word study app - planning](/assets/images/category/blaboo/development-journal/plan_trello.png)

## App Design
I've designed the app based on above planning. I'm not a designer so my design is not so pretty. however I can decide basic color and concept of the app.

I've used [sketchapp](https://www.sketchapp.com/){:rel="nofollow noreferrer" target="_blank"} for the app design and donwload the illustraions from [freepik](https://www.freepik.com/){:rel="nofollow noreferrer" target="_blank"}.

![BlaBoo for baby/children word study app - design](/assets/images/category/blaboo/development-journal/sketch_design.png)

## App Development
of course, I've used RN(React Native) for the app development. one developer can make iOS/Android app same time, and learning curve is not high like learning Swift or Kotlin because of javascript. BlaBoo is based on RN(```React Native```) and ```typescript```.

- how to install RN(React Native): [RN installation]({{site.url}}/react-native/installation/){:target="_blank"}
- how to apply typescript to RN(React Native): [typescript]({{site.url}}/react-native/typescript/){:target="_blank"}

also, I've used ```NativeBase``` for basic UI and ```styled-components``` for styling.

- how to use NativeBase in RN(React Native): [nativebase]({{site.url}}/react-native/nativebase/){:target="_blank"}
- how to use styled-components in RN(React Navtive): [styled-components]({{site.url}}/react-native/styled-components/){:target="_blank"}

RN(React Native) doesn't have the navigation system. BlaBoo uses ```react-navigation``` for the navigation system.

- how to use react-navigation: [react-navigation]({{site.url}}/react-native/react-navigation/){:target="_blank"}

I've use ```react-native-tts``` to implement ```TTS(Text To Speech)``` for developing voice feature which is one of MVP(Minimum Viable Product) feautes.

- how to use react-native-tts: [react-native-tts]({{site.url}}/react-native/react-native-tts/){:target="_blank"}

also I've use the locale information from the user device information to set the app and ```react-native-tts``` default language. I use ```react-native-device-info``` to get the user device information.

- how to use react-native-device-info: [react-native-device-info]({{site.url}}/react-native/react-native-device-info/){:target="_blank"}

and if the illustration is touched, the illustration is moved simply. I use ```react-native-animatable``` to insert simple animation to the illustration.

- how to use react-native-animatable: [react-native-animatable]({{site.url}}/react-native/react-native-animatable/){:target="_blank"}

finally, I use Google Firebase to analyze the app and use Google Admob for the advertisement. I use ```react-native-firebase``` for these features.

- how to use react-native-firebase for admob: [react-native-firebase-admob]({{site.url}}/react-native/react-native-firebase-admob/){:target="_blank"}
- how to use react-native-firebase for analytics: [react-native-firebase-analytics]({{site.url}}/react-native/react-native-firebase-analytics/){:target="_blank"}
- how to use react-native-firebase for Crasylytics: [firebase-crashlytics]({{site.url}}/react-native/firebase-crashlytics/){:target="_blank"}

I've written the journal like above,
after all, it seems like there was not much to do except bring and implement open source. thanks to make beautiful and useful open source. to develop the app was not difficult because I used awesome open source and reusable component. just, gathering the illustrations and words took a longer time than developing.

![BlaBoo for baby/children word study app - resource code](/assets/images/category/blaboo/development-journal/resource.png)

## App Registration
so BlaBoo MVP(Minimum Viable Product) is completed. I thought I would register and download the app soon after development, but the process of registering the app took a long time.

I already know Apple App Review is taking a long time, so I registered iOS first, and I registered Android after iOS is registered. Apple App Review took almost 2 months and Android took 2 days.

Apple App Review took a long time because of reject the app by many reasons. my app was rejected on Android because my app is for children but I didn't select ```Designed for Families program``` option

![BlaBoo for baby/children word study app - Google App review reject](/assets/images/category/blaboo/development-journal/google_reject.png)

to register apps, we need to enroll Apple Developer Program and Android Developer(Google Play Developer).

- how to enroll Apple Developer Program: [enroll iOS developer]({{site.url}}/react-native/ios-enroll-developer-program/){:target="_blank"}
- how to enroll Android Developer(Google Play Developer): [enroll Android Developer]({{site.url}}/react-native/android-enroll-google-play-developer/){:target="_blank"}

also, I needed various informations. it took a long time to make these informations.

- how to register iOS app: [register iOS App store]({{site.url}}/react-native/ios-app-store/){:target="_blank"}
- how to register Android app: [register Android App store]({{site.url}}/react-native/android-google-play/){:target="_blank"}

and Apple strict App Review. my app was rejected 5 times. I felt not to register. at that time, I really wanted to stop to register. and final rejection reason was my app doesn't have user interact, so Apple App store doesn't need my app.

OMG. at first, I appealed to Apple like "my app has more categories than this app. my app has more words and multiple language feature than that app." but they didn't approve it easily. rather, if I think other apps are in violation of the app store, report them...but how do I report them those developers have made with many efforts...so I added an weird feature unlike origin plan.

![BlaBoo for baby/children word study app - review feature](/assets/images/category/blaboo/development-journal/add_card_mode.png)

I've added review feature which baby/children can review words studied in categories by card type. the feature is to display 20 cards randomly, and swift left or right to review.

this feature is not at first plan and it is made for approving App Review fastly by designing 1 day and developing 1 day, so it looks like weird in the app. still I think BlaBoo is two apps in one app. however BlaBoo was approved safely App Review after adding this feature.

at first, I felt anger about Apple App Review, but this review made me thought that iOS apps have great UI/UX. after Apple App Review, I thought I'd make the next app more user friendly. thanks Apple App Reviewers.

<div class="download_link_container">
    <a class="download_link_ios" href="https://itunes.apple.com/app/blaboo/id1441741187" target="_blank">
        <img src="/assets/images/apple_download.png" alt="learning words app for children, blaboo iOS download"/>
    </a>
    <a class="download_link_android" href="https://play.google.com/store/apps/details?id=io.github.dev.yakuza.blaboo" target="_blank">
        <img src="/assets/images/google play_download.png" alt="learning words app for children, blaboo Android download"/>
    </a>
</div>

## Finish App Development Journal
there were many things, but I could release the first app safely. maybe, this app looks like not to have enough features, but this app's purpose is not to gather many users for getting money, just I want to use for my child and for developing an app with RN(React Native).

looking back, it took more time to design and to gather the illustrations than development. development took almost 1 week... I saw RN(React Native) development performance.(thanks developers who make many open sources.)

Apple strict App Review. changed App concept quickly, but this experience changed my mind that I could make more user friendly apps. thanks for App reviewers again.


The hypothesis that I can develop the app with free resources at BlaBoo is proven. develop apps using free resources!

## Lastly
well, ```TTS(Text To Speech)``` voice is not friendly. and there is wrong pronunciation. for example, TTS can't pronounce ```spaghetti``` in Korean, so I changed it to ```pasta```. if you want to donate voices, please send email or pull request.

- github: [https://github.com/dev-yakuza/blaboo-translate](https://github.com/dev-yakuza/blaboo-translate){:target="_blank"})
- email: dev.yakuza@gmail.com

I use free illustrations so that doesn't looks like same style. if you want to donate illustrations, please send email or pull.

- github: [https://github.com/dev-yakuza/blaboo-translate](https://github.com/dev-yakuza/blaboo-translate){:target="_blank"})
- email: dev.yakuza@gmail.com

I made BlaBoo support Japanese, English, Korean basically and app download is occured in China and Italy so I added Chinese and Italian. however, I don't know Chinese and Italian so I used google translator. if you catch wrong Chinese or Italian, please feedback me. also if you want to donate other languages, please send email or pull.

- github: [https://github.com/dev-yakuza/blaboo-translate](https://github.com/dev-yakuza/blaboo-translate){:target="_blank"})
- email: dev.yakuza@gmail.com

## Download
<div class="download_link_container">
    <a class="download_link_ios" href="https://itunes.apple.com/app/blaboo/id1441741187" target="_blank">
        <img src="/assets/images/apple_download.png" alt="learning words app for children, blaboo iOS download"/>
    </a>
    <a class="download_link_android" href="https://play.google.com/store/apps/details?id=io.github.dev.yakuza.blaboo" target="_blank">
        <img src="/assets/images/google play_download.png" alt="learning words app for children, blaboo Android download"/>
    </a>
</div>