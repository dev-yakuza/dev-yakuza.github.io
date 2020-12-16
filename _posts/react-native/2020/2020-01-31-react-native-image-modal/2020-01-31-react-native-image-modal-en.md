---
layout: 'post'
permalink: '/react-native/react-native-image-modal/'
paginate_path: '/react-native/:num/react-native-image-modal/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'react-native-image-modal'
description: let's see how to use react-native-image-modal to show full size image modal and pinch zoom in/out.
image: '/assets/images/category/react-native/2020/react-native-image-modal/background.jpg'
---

<div id="contents_list" markdown="1">

## Content

- [Outline](#outline)
- [Prview](#prview)
- [Installation](#installation)
- [How to use](#how-to-use)
- [Properties](#properties)
- [Features](#features)
- [Example project](#example-project)
- [Contribute](#contribute)
- [Completed](#completed)

</div>

## Outline

I need a component which is when an image is selected, the image is shown up full size and supported to pinch zoom in/out. I think there are many nice components include this feature, but I've made `react-native-image-modal` component for open source.

This blog post is about how to use `react-native-image-modal` which I've made.

- Github: [react-native-image-modal](https://github.com/dev-yakuza/react-native-image-modal){:target="_blank"}

## Prview

Let's see what react-native-image-modal. react-native-image-modal works like below.

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2020/react-native-image-modal/pinch-zoom-and-move.gif" alt="react-native-image-modal 동작 화면">
</div>

{% include in-feed-ads.html %}

## Installation

Execute the command below to install react-native-image-modal.

```bash
npm install --save react-native-image-modal
```

## How to use

Add the code below to where you want to show full size image with react-native-image-modal.

```js
import ImageModal from 'react-native-image-modal';
```

And add the code below.

```js
{% raw %}
<ImageModal
  swipeToDismiss={false}
  resizeMode="contain"
  imageBackgroundColor="#000000"
  style={{
    width: imageWidth,
    height: 250,
  }}
  source={{
    uri:
      'https://cdn.pixabay.com/photo/2018/01/11/09/52/three-3075752_960_720.jpg',
  }}
/>
{% endraw %}
```

## Properties

Basically, you can use all React Native Image component props for an original image.(not full size modal image)
Below is react-native-image-modal specific Props.

| Prop | required | Type | Description |
|------|----------|------|-------------|
| swipeToDismiss | X | boolean | set `true` to swipe to dismiss (`default: true`)  |
| imageBackgroundColor | X | string | background color for `the original image` |
| overlayBackgroundColor | X | string | backgroud color for `the full size modal`(`default: #000000`)  |
| onLongPressOriginImage | X | () => void | long press event callback for `the original image`  |
| renderHeader | X | (close: () => void) => JSX.Element | Array<JSX.Element> | You can customize the header of `the full size modal` with react native components |
| renderFooter | X | (close: () => void) => JSX.Element | Array<JSX.Element> | You can customize the footer of `the full size modal` with react native components |
| onTap | X | (eventParams: {locationX: number; locationY: number; pageX: number; pageY: number;}) => void  | one tap event callback for `the full size modal` |
| onDoubleTap | X | () => void | double tap event callback for `the full size modal` |
| onLongPress | X | () => void | long press event callback for `the full size modal` |
| onOpen | X | () => void | open event callback for `the full size modal` |
| didOpen | X | () => void | event callback after open for `the full size modal`  |
| onMove | X | (position: {type: string; positionX: number; positionY: number; scale: number; zoomCurrentDistance: number;}) => void  | move event callback for `the full size modal` |
| responderRelease | X | (vx?: number, scale?: number) => void | responder release event callback for `the full size modal` |
| willClose | X | () => void | event callback before close for `the full size modal` |
| onClose | X | () => void | close event callback for `the full size modal` |

{% include in-feed-ads.html %}

## Features

react-native-image-modal has features like below.

- Open/close the image modal

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2020/react-native-image-modal/open-and-close-image-modal.gif" alt="react-native-image-modal Open/close the image modal">
</div>

- Image pinch zomm in/out and move

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2020/react-native-image-modal/pinch-zoom-and-move.gif" alt="react-native-image-modal pinch Image pinch zomm in/out and move">
</div>

- Image double taps zoom in/out

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2020/react-native-image-modal/double-tap-zoom.gif" alt="react-native-image-modal Image double taps zoom in/out">
</div>

- Swipe to close the modal

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2020/react-native-image-modal/swipe-to-dismiss.gif" alt="react-native-image-modal Swipe to close the modal">
</div>

{% include in-feed-ads.html %}

## Example project

Github repository has an example project.

- Github: [react-native-image-modal](https://github.com/dev-yakuza/react-native-image-modal){:target="_blank"}

Clone Github repository to check the example source code.

```bash
git clone https://github.com/dev-yakuza/react-native-image-modal.git
```

Install libraries for the example project.

```bash
cd Example
npm install

# iOS
cd ios
pod install
```

Execute the command below to execute the project.

```bash
# Example folder
# iOS
npm run ios
# Android
npm run android
```

## Contribute

This is my first open source, so it is not perfect. If you find bugs or wrong code, please give me a pull request.

For contributing easily, I share how to develop this project in here.

- Clone the project.

```bash
git clone https://github.com/dev-yakuza/react-native-image-modal.git
```

- Execute the command below to make the development environment and start Typescript.

```bash
npm install
npm start
```

- Execute the command below to start a project for the development.

```bash
cd Develop
npm install

# android
npm run android

# ios
cd ios
pod install
cd ..
npm run ios
```

## Completed

We've seen how to use react-native-image-modal which is my first open source project. I hope this is helpful for many people.