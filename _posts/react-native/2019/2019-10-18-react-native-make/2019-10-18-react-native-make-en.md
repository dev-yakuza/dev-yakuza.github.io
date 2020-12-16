---
layout: 'post'
permalink: '/react-native/react-native-make/'
paginate_path: '/react-native/:num/react-native-make/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'App icon & Splash image in React Native'
description: Let's see how to make App icon and Splash image via react-native-make library in React Native.
image: '/assets/images/category/react-native/2019/react-native-make/background.jpg'
---

<div id="contents_list" markdown="1">

## Content

- [Outline](#outline)
- [Install react-native-make](#install-react-native-make)
- [App icon](#app-icon)
- [Splash image](#splash-image)
  - [Create Splash image](#create-splash-image)
  - [iOS](#ios)
  - [react-native-splash-screen](#react-native-splash-screen)
- [Completed](#completed)

</div>

## Outline

To make App icon and Splash image in React Native, I use [generator-rn-toolbox](https://github.com/bamlab/generator-rn-toolbox){:rel="nofollow noreferrer" target="_blank" } until now. the links below are about it.

- [App icon]({{site.url}}/{{page.categories}}/app-icon/){:target="_blank"}
- [Splash image]({{site.url}}/{{page.categories}}/splash-image/){:target="_blank"}

Until now, I was using generator-rn-toolbox well, I got a comment on my blog post, that there is a new library, from generator-rn-toolbox developer who is very kind.

![use react-native-make to make App icon and Splash image - developer comment](/assets/images/category/react-native/2019/react-native-make/comment.jpg)

I have checked it. generator-rn-toolbox is `Deprecated`, and he has made and provided new [react-native-make](https://github.com/bamlab/react-native-make){:rel="nofollow noreferrer" target="_blank" }.

In this blog post, I will introduce how to make App icon and Splash image via react-native-make library, and compare the previous library.

## Install react-native-make

Execute the command below to install react-native-make.

```bash
npm install --save-dev @bam.tech/react-native-make
```

That's all. We are ready to use react-native-make. A comparison with the previous generator-rn-toolbox is below.

When install generator-rn-toolbox, we need to install globally like below.

```bash
npm install -g yo generator-rn-toolbox
```

And then, we need to install additional library, imagemagick, like below.

```bash
brew install imagemagick
```

By comparison, we can install react-native-make locally and don't need to install any additional libraries.

## App icon

When you use react-native-make to create App icon, you need a `1024x1024 px` size `png` image.

If the file is ready, execute the command below to make App icon.

```bash
# react-native set-icon --path [path-to-image]
react-native set-icon --path [path-to-image] --background ["color"]
```

For example,

```bash
# react-native set-icon --path ./src/Assets/images/app_icon.jpg
react-native set-icon --path ./src/Assets/images/app_icon.jpg --background "#FFFFFF"
```

{% include in-feed-ads.html %}

## Splash image

### Create Splash image

When you use react-native-make to make Splash image, you need a minimum `3000x3000px` size `png` file.

If the image is ready, execute the command below to create Splash image.

```bash
# react-native set-splash --path [path-to-image]
# react-native set-splash --path [path-to-image] --resize [contain|cover|center]
react-native set-splash --path [path-to-image] --resize [contain|cover|center] --background ["background-color"]
```

For exmaple,

```bash
# react-native set-splash --path ./src/Assets/images/splash.jpg
# react-native set-splash --path ./src/Assets/images/splash.jpg --resize cover
react-native set-splash --path ./src/Assets/images/splash.jpg --resize center --background "#FFFFFF"
```

The resize option default is `contain`. And, if you use cover option, the main image should be located 1/3 padding on background image, not to crop the main image.

You can see the image status by each option on the link below.

- [resize-modes](https://github.com/bamlab/react-native-make/blob/master/docs/set-splash.md#resize-modes){:rel="nofollow noreferrer" target="_blank" }

In my case, I use multiple colors background in Splash image. In this case, `cover` options is the best choice to create Splash image.

### iOS

To use Splash image on iOS, you need to set the Storyboard for Splash image. Execute the Xcode by opening `./ios/[Project Name].xcworkspace` file to set the Storyboard.

![App icon & Splash image in React Native - add storyboard on iOS ](/assets/images/category/react-native/2019/react-native-make/add_files.jpg)


When the Xcode is executed, right-click the project name on the left top, and click the `Add Files to "Project Name"` menu.

And then select the `ios/SplashScreen.storyboard` file to add it.

![App icon & Splash image in React Native - setting launch_screen_file](/assets/images/category/react-native/2019/react-native-make/create-splash-screen.jpg)


After adding the file, insert `SplashScreen` on `Launch Screen File` field in `General` tab.

### react-native-splash-screen

The reason to make Splash image and to apply it is to manage login or data processing in the background of Splash image.

For this, react-native-make uses [react-native-splash-screen](https://github.com/crazycodeboy/react-native-splash-screen){:rel="nofollow noreferrer" target="_blank"}.

We can use `react-native-splash-screen` to easily control Splash image in React Native not only for react-native-make. I've written the blog post about this subject. you can see this on the link below.

- [App Splash screen]({{site.url}}/{{page.categories}}/react-native-splash-screen/){:target="_blank"}

## Completed

For me who design and develop the app by alone, when I created App icon and Splash image, generator-rn-toolbox is very helpful. And I think the new react-native-make is also very helpful.

Let's try to use react-native-make to easily make App icon and Splash image!
