---
layout: 'post'
permalink: '/kumoncho/development-journal/'
paginate_path: '/kumoncho/:num/development-journal/'
lang: 'en'
categories: 'kumoncho'
comments: true

title: 'Kumoncho development journal(RN, React Native)'
description: I've developed the picture fairy tale book app that is called Kumoncho. in here, I wrote the development journal about what I experience.
image: '/assets/images/category/kumoncho/background.png'
---

## Outline
at previous my project, I've developed the app from start to end by myself using RN(React Native). at this project, I wanted to develop the app with someone together. especially, I wanted to work with a designer because the design has taken too much time at previous project. if you want to know more details about previous project, see the development journal about previous project.

- [BlaBoo development journal (RN, React Native)]({{site.url}}/blaboo/development-journal/){:target="_blank"}


## What is Kumoncho?
Kumoncho is the picture fairy tale book about the friendship and courage between prince Ikaros of the cloud kingdom and his cloud friend, Kumoncho.

- Kumoncho landing page: [Kumoncho]( https://dev-yakuza.github.io/app/kumoncho/ko/){:target="_blank"}

you can download to click the link below.

<div class="download_link_container">
    <a class="download_link_ios" href="https://itunes.apple.com/app/kumoncho/id1450902241" target="_blank">
        <img src="/assets/images/apple_download.png" alt="children's picture fairy tale book, Kumoncho iOS download"/>
    </a>
    <a class="download_link_android" href="https://play.google.com/store/apps/details?id=io.github.dev.yakuza.kumoncho" target="_blank">
        <img src="/assets/images/google play_download.png" alt="children's picture fairy tale book, Kumoncho Android download"/>
    </a>
</div>


## Why did I make it?
I've focused to make the app by RN(React Native) by myself at previous project.

- [BlaBoo development journal(RN, React Native)]({{site.url}}/blaboo/development-journal/){:target="_blank"}

so, at this project, I wanted to focus the collaboration with someone. also, I wanted to develop an app more fastly by collaborating the design that has taken too much time at previous project.

lastly, one of my friends wanted to be a cartoonist, but now he live as a web designer not  a cartoonist. however I saw his illustrations and I thought he has the talent. so I
persuaded him to join this project. I persuaded him by saying that the cartoonists should think many episodes and draw many pages, but children's fairy tale book writer think short episode and draw some pages, so you can do this as a hobby after the work.

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/kumoncho/development-journal/profile_shu.png" alt="picture fairy tale book writer, shu profile">
</div>

- Shu: <a href="mailto:meiki.shuzou@gmail.com">meiki.shuzou@gmail.com</a>

fortunately, he said yes. he is in charge of the illustrations and story, and I am in charge of the project directing and development.

starting with this project, we'll make picture fairy tale books for children continuously, and we set the final goal to publish real books. we've released Kumoncho and we already prepared next fairy tale book app.

because he and I work different companies, feedback was mainly sent and received via Line, videoconferencing was held at lunchtime, if necessary. the parts in charge were clearly divided without overlapping, so collaboration was able to proceed without major conflicts.


## App Planning
this project is the picture fairy tale book but my friend have never written and drawn the fairy tale book, and I have never developed it. so I started to research the picture fairy tale book.

our final goal is to publish the book, so I researched the standard ot real fairy tale book.

some of the fairy tale books for children are 16, 24, 48 pages, but the industry standard is 32 pages.(If it is wrong, give me a comment please)

![fairy tale book for children, 32 page](/assets/images/category/kumoncho/development-journal/picture_book.jpg)
(사진 출처: [https://taralazar.com](https://taralazar.com/2009/02/22/picture-book-construction-know-your-layout/){:rel="nofollow noreferrer" target="_blank"})

also we needed to make the difference between our book that will be published(I don't know we can really publish it) and the app. so we decided to make 9 pages app. we set it's not too long and not too short.(the publication book will be 32 pages)

after deciding the pages, my friend could make easily the story and layout of illustrations.


## Story And Illustration
it is first time for me and my friend to make children's picture fairy tale app, so we decided to make the story be in ordinary. as you can see by downloading the app, the story is familiar and ordinary.

<div class="download_link_container">
    <a class="download_link_ios" href="https://itunes.apple.com/app/kumoncho/id1450902241" target="_blank">
        <img src="/assets/images/apple_download.png" alt="children's picture fairy tale book, Kumoncho iOS download"/>
    </a>
    <a class="download_link_android" href="https://play.google.com/store/apps/details?id=io.github.dev.yakuza.kumoncho" target="_blank">
        <img src="/assets/images/google play_download.png" alt="children's picture fairy tale book, Kumoncho Android download"/>
    </a>
</div>

after deciding the story, my friend embodies characters and background by sketching.

![Kumoncho sketch](/assets/images/category/kumoncho/development-journal/sketch.png)

and then he revised the story, and start drawing illustrations.

![Kumoncho illustration](/assets/images/category/kumoncho/development-journal/illustration.png)

I think he has great talent in paintings and stories.


## App Development
of course, I developed the app with RN(React Native). Kumoncho is based on RN(```React Native```) and ```typescript```.

- RN(React Native) installation: [RN installation]({{site.url}}/react-native/installation/){:target="_blank"}
- how to apply typescript to RN(React Native): [typescript]({{site.url}}/react-native/typescript/){:target="_blank"}

and I used ```styled-component``` for styling.

- how to use styled-component at RN(React Navtive): [styled-components]({{site.url}}/react-native/styled-components/){:target="_blank"}

I made the app background be gradient by using ```react-native-linear-gradient```.

- how to make the app background be gradient at RN(React Navtive): [react-native-linear-gradient]({{site.url}}/react-native/react-native-linear-gradient/){:target="_blank"}

at the first time, I've used scroll to transit the pages.

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/kumoncho/development-journal/kumoncho_scroll.gif" alt="fairy tale kumoncho, scroll">
</div>

however, I wanted to transit them more naturally, so I've used the animation of the gradient that I introduced at [react-native-linear-gradient]({{site.url}}/react-native/react-native-linear-gradient/){:target="_blank"}. and I made other images fadein/fadeout effects by using [react-native-animatable]({{site.url}}/react-native/react-native-animatable/){:target="_blank"}.

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/kumoncho/development-journal/kumoncho_swipe.gif" alt="Kumoncho picture book swipe">
</div>

I used user's swipe events to transit the pages.

- how to detect user's swipe events at RN(React Native): [react-native-swipe-gestures]({{site.url}}/react-native/react-native-swipe-gestures/){:target="_blank"}

finally, I used Google Firebase to analyze the app, and Google Admob for the advertisement in the app. I implemented them by using ```react-native-firebase```.

- how to use react-native-firebase for Admob: [react-native-firebase-admob]({{site.url}}/react-native/react-native-firebase-admob/){:target="_blank"}
- how to implement Analytics by react-native-firebase analytics: [react-native-firebase-analytics]({{site.url}}/react-native/react-native-firebase-analytics/){:target="_blank"}
- how to implement Crashlytics by react-native-firebase: [firebase-crashlytics]({{site.url}}/react-native/firebase-crashlytics/){:target="_blank"}

the list below is the libraries that I used to implement  other features in the app.

- send email in RN(React Native): [react-native-mail]({{site.url}}/react-native/react-native-mail/){:target="_blank"}
- induce users to give the rating at RN(React Native): [react-native-rate]({{site.url}}/react-native/react-native-rate/){:target="_blank"}
- controll splash screen at RN(React Native): [react-native-splash-screen]({{site.url}}/react-native/react-native-splash-screen/){:target="_blank"}
- how to implement TTS(Text To Speech) at RN(React Native): [react-native-tts]({{site.url}}/react-native/react-native-tts/){:target="_blank"}


## App Registration
I have terrible experience to register the app at previous project([BlaBoo development journal(RN, React Native)]({{site.url}}/blaboo/development-journal/){:target="_blank"}). because of the experience, I could register the app without big problems at this project.

I tried to register the app to the children category at iOS, but the app was rejected in the review because of outbound link.if the app is in the children category, the app should be implemented Parental Gate feature to protect the links. however, my app didn't have it. I didn't find the library to implement Parental Gate, so I changed normal category to apply for the registration, and it was approved.

<div class="download_link_container">
    <a class="download_link_ios" href="https://itunes.apple.com/app/kumoncho/id1450902241" target="_blank">
        <img src="/assets/images/apple_download.png" alt="children's picture fairy tale book, Kumoncho iOS download"/>
    </a>
    <a class="download_link_android" href="https://play.google.com/store/apps/details?id=io.github.dev.yakuza.kumoncho" target="_blank">
        <img src="/assets/images/google play_download.png" alt="children's picture fairy tale book, Kumoncho Android download"/>
    </a>
</div>


## Lastly
I should analyze and benchmark the competitors(fairy tale books) at the app planning. we've made the big mistake not to decide contents(text length), because we've focused to make the story and illustrations after deciding the page counts.

as you can see ```Story and Illustration``` section, we had only paintings in the illustration at the first time. during the development, we put belatedly the contents(text) to the app for explaining the painting. so it occurred the problem at the layout of the illustrations, and storytelling more weakly.

also, we worked on the book basis, so we didn't think deeply about reading in the app(UX). if you exit the app during reading and start again the app, you should read all pages from the first. even, this app doesn't have the feature to move to the middle of the pages. I think this project is completely failed about UX.

the development also had a problem. after deploying the app, my friend wanted the app supports the tablet, too. RN(React Native) is the cross-platform, so I thought that is not a big deal. actually, the previous project([BlaBoo development journal(RN, React Native)]({{site.url}}/blaboo/development-journal/){:target="_blank"}) is too simple app, so I could simply make the previous project support the tablet. however, this project has many images and the positions of the images, and I didn't design the app with considering the tablet so I failed to support the tablet. I will refactor the app to support the tablet if I have the time , but I should have made it well from the beginning.

<div class="download_link_container">
    <a class="download_link_ios" href="https://itunes.apple.com/app/kumoncho/id1450902241" target="_blank">
        <img src="/assets/images/apple_download.png" alt="children's picture fairy tale book, Kumoncho iOS download"/>
    </a>
    <a class="download_link_android" href="https://play.google.com/store/apps/details?id=io.github.dev.yakuza.kumoncho" target="_blank">
        <img src="/assets/images/google play_download.png" alt="children's picture fairy tale book, Kumoncho Android download"/>
    </a>
</div>

For the last time, if someone works on the publication industry and wants to publish the book of our app, please contact us!

<a href="mailto:dev.yakuza@gmail.com">dev.yakuza@gmail.com</a>
