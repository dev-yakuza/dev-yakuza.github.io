---
layout: 'post'
permalink: '/kumoncho/update-review/'
paginate_path: '/kumoncho/:num/update-review/'
lang: 'en'
categories: 'kumoncho'
comments: true

title: 'Kumoncho Update Reviews(RN, React Native)'
description: I've developed and released the fairy tale picture book called Kumoncho by using RN(React Native). in this blog, I will talk about what I updated after the release.
image: '/assets/images/category/kumoncho/background.png'
---

## 개요
I've made and released the fairy tale picture book called Kumoncho by using RN(React Native). in here, I will introduce what I updated the app after releasing it. if you want to know how I made the app, check the link below!

- [Kumoncho development journal(RN, React Native)]({{site.url}}/kumoncho/development-journal/){:target="_blank"}

before starting it, let's see what Kumoncho is.


## What is Kumoncho?
Kumoncho is the picture fairy tale book about the friendship and courage between prince Ikaros of the cloud kingdom and his cloud friend, Kumoncho.

- Kumoncho landing page: [Kumoncho]( https://dev-yakuza.github.io/app/kumoncho/en/){:target="_blank"}

you can download to click the link below.

<div class="download_link_container">
    <a class="download_link_ios" href="https://itunes.apple.com/app/kumoncho/id1450902241" target="_blank">
        <img src="/assets/images/apple_download.png" alt="children's picture fairy tale book, Kumoncho iOS download"/>
    </a>
    <a class="download_link_android" href="https://play.google.com/store/apps/details?id=io.github.dev.yakuza.kumoncho" target="_blank">
        <img src="/assets/images/google play_download.png" alt="children's picture fairy tale book, Kumoncho Android download"/>
    </a>
</div>


## Problems
already I've mentioned the problems in the development journal, this project was totally failed on UX. you can see the details about it via the link below.

- [Kumoncho development journal(RN, React Native)]({{site.url}}/kumoncho/development-journal/){:target="_blank"}

so in this update, I focused to make UX better. and when I've developed this app, I didn't consider to support the tablet, but my partner wanted to make the app support the tablet, and when I tried to make the app support the tablet, it was failed. so I've done refactoring the app to support the tablet.

lastly, my writer friend wants to be a Micro-interaction expert. so we've added animations to the app, that can be used in the work.


## App Update
Kumoncho v2 updates include the list below.

1. support the tablet
1. animation
1. the feature that change the page.
1. tutorial
1. StatusBar

let's see one by one.


### Support The Tablet
RN(React Native) supports the cross-platform, so we can make universal apps that support the smartphone and the tablet. of course, we need to code by each screen size. RN(React Native) uses basically ```flexbox```, so we can make the responsive app simply.

however, Kumoncho is the children fairy tale picture book and has various layers that have fixed images. I didn't consider the tablet so, I couldn't make the app support the tablet easily beacause of the fixed images.

![children fairy tale picture book Kumoncho layers](/assets/images/category/kumoncho/update-review/kumoncho_layer.png)

Kumoncho has the background layer, main image layer, other images layer and description layer like above. I manage these layers by ```object``` and implement these by using React components.

```js
{
    key: 'page1',
    src: ...,
    description: {
        ja: [...],
        ko: [...],
        en: [...],
    },
    color: ...,
    background: [...],
    direction: {
        start: { ... },
        end: { ... },
    },
    width: ...,
    descriptionImage: ...,
    additionalImages: [
        {...},
        {...},
        {...},
        {...},
    ],
},
```

above is the part of the ```object``` that I used. as you can see, there are no options for the tablets. when I was doing refactoring, I tried to modify React components to distinguish smartphone and tablet. but that was not the fundamental solution, so I've done refactoring ```object```.

```js
{
    key: 'page1',
    background: {
      color: [...],
      direction: {
        start: { ... },
        end: { ... },
      },
    },
    layers: [
      {
        data: ...,
        ...
        style: {
          phone: { ... },
          tablet: { ... },
        },
      },
      {
        images: [
          {
            src: ...,
            style: {
              phone: {...},
              tablet: {...},
            },
          },
          ...
        ],
      },
    ],
    description: {
      text: {
        ja: [...],
        ko: [...],
        en: [...],
      },
      color: ...,
      image: ...,
      style: {
        container: {
          phone: {...},
          tablet: {...},
        },
        label: {
          phone: {...},
          tablet: {...},
        },
      },
    },
},
```

the layer can be the data(animation) or the image, and the style supports the smartphone and the tablet separately. also, the before style supported only the specific style(width or color, etc), but now the style can support everything. now I can focus to develop the app for the smartphone and the tablet separately.


### Animation
Kumoncho is the children fairy tale picture book ```app```, it can provide some features that the paper book can't provide. one of them is the animation feature. I've added the animation that users(children) can be interested in the app more.

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/kumoncho/update-review/kumoncho_animation.gif" alt="children fairy tale picture book Kumoncho animation">
</div>

I've added the animations to each page, so you can see the book more interesting. I use `lottie` to implement the animation. if you want to know how to make it, see the link below.

- [use After Effects(AEF)]({{site.url}}/react-native/react-native-lottie/){:target="_blank"}


### Change Pages
as I've mentioned on the previous blog([Kumoncho development journal(RN, React Native)]({{site.url}}/kumoncho/development-journal/){:target="_blank"}), this project was failed on UX. if users(children) read the book and quit the app in the middle of the book, they should re-read from first. so I've added the page change feature to solve this problem.

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/kumoncho/update-review/kumoncho_page_change.gif" alt="children fairy tale book kumoncho scroll">
</div>

if users(children) double touched the screen, the page list is shown up and if they select the page, the page is changed.


### Tutorial
the current app has two features, double touch and swipe the screen. some users can't understand them easily, so when the app is executed for the first time, I've made the tutorial show up.

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/kumoncho/update-review/kumoncho_tutorial.png" alt="children fairy tale picture book, Kumoncho tutorial">
</div>


### StatusBar
As I was developing around iOS, I didn't really care about Android. iOS Status Bar is transparent so it's not a problem. after the app was released, I got the feedback that wants to make the status bar transparent on Android. so I've made the transparent status bar on Android and hidden the status bar on the Splash screen. if you want to know how to control the status bar on Android, see the link below.

- [Control StatusBar]({{site.url}}/react-native/react-native-status-bar/){:target="_blank"}


## Problem
the problem always comes from Android. the simulator didn't have any problem, but when I tested the app on Android device, I got `OOM(Out Of Memory)` error and the app was crashed. I've debugged and found the cause of the problem was `lottie` animation.

I used the animation with PNG images. I think `lottie` handles them on iOS and Android differently. now, I changed the image from PNG to SVG and the problem is gone.

if you use `lottie` for the animation, I recommend not to use PNG image type.


## Conclusion
I think I make the app UX better than before via this update. also, users(children) can enjoy the app more, because of the animation. now I'm preparing the next fairy tale book app based on this project. if you have any idea or opinion about this app, please leave comments on below.

<div class="download_link_container">
    <a class="download_link_ios" href="https://itunes.apple.com/app/kumoncho/id1450902241" target="_blank">
        <img src="/assets/images/apple_download.png" alt="children's picture fairy tale book, Kumoncho iOS download"/>
    </a>
    <a class="download_link_android" href="https://play.google.com/store/apps/details?id=io.github.dev.yakuza.kumoncho" target="_blank">
        <img src="/assets/images/google play_download.png" alt="children's picture fairy tale book, Kumoncho Android download"/>
    </a>
</div>