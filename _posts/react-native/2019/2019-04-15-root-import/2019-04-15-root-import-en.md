---
layout: 'post'
permalink: '/react-native/root-import/'
paginate_path: '/react-native/:num/root-import/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'Make Import path based on Root in RN(React Native)'
description: let's make Import path based on Root in RN(React Native)
image: '/assets/images/category/react-native/2019/root-import/background.jpg'
---

## Outline
this blog post is the problem about not only RN(React Native) but also Reactjs. when we develop with React, no matter how beautiful the structure of the project may be, the long '../../' folder reference problem does not seem to be solved. in here, I will introduce how to reduce the long folder reference in Import. I hope this blog helpful for both RN(React Native) developers and Reactjs developers.

## Folder Structure
when I develop with RN(React Native), I use the folder structure like below.

```
|-- android/
|-- ios/
|-- src/
|   |-- @types/
|   |-- Assets/
|   |   |-- Images/
|   |-- Component/
|   |   |-- BannerContainer/
|   |   |   |-- index.tsx
|   |   |-- LoadingContainer/
|   |   |   |-- index.tsx
|   |-- Screen/
|   |   |-- Home/
|   |   |   |-- SomeContainer/
|   |   |   |   |-- index.tsx
|   |   |   |-- SomeContainer2/
|   |   |   |   |-- SomeContainerItem/
|   |   |   |   |   |-- index.tsx
|   |   |   |   |-- index.tsx
|   |   |   |-- index.tsx
|   |-- Util/
|-- index.js
```

at the first time, I use `Component`, `Container`, `Screen` folders but some `Container` dependent only one `Screen`, not shared. so I decided to put shared `Component` in `Component` folder and dependent `Component` under dependent `Screen`. of course, `Component` also can have Component(Container).

I have two reasons why I made this folder structure. one is the inconvenience that I try to find Container or Component from Screen, I have to search `Container` folder first and see the Container and search `Component`. now, I can search easily Container in dependent Screen folder. another reason is for copy-pasting. I'm developing many applications alone for the hobby, so many times, I copy the Component from the project to other projects. when `Container` was separately in another folder and if I copy `Screen`, I had to copy the Screen and the Container and the Component each other. now, when I copy the Screen, I just copy the Screen which includes the Containers, so the copy-paste is easier than before. therefore, I got this folder structure finally. below is the structure that I use in Reactjs.

```
|-- android/
|-- ios/
|-- src/
|   |-- @types/
|   |-- Assets/
|   |   |-- Images/
|   |-- Component/
|   |   |-- BannerContainer/
|   |   |   |-- index.tsx
|   |   |-- LoadingContainer/
|   |   |   |-- index.tsx
|   |-- Feature/
|   |   |-- Login/
|   |   |   |-- SomeContainer/
|   |   |   |   |-- index.tsx
|   |   |   |-- SomeContainer2/
|   |   |   |   |-- SomeContainerItem/
|   |   |   |   |   |-- index.tsx
|   |   |   |   |-- index.tsx
|   |   |   |-- index.tsx
|   |-- Util/
|-- index.js
```

as you can see above, I just change `Screen` folder name to `Feature` to manage the contents. what kind of structure do you use? could you share your folder structure on the comment on the bottom of the screen for people refer?(I also want to refer it T^T)

{% include in-feed-ads.html %}

## Problem
as I got this folder structure, if `Screen`(`Feature`) has `Container` and Container has another `Container` and the last Container has `Component`, when I import, `../../..` long path reference problem is occurred. recently, VSCode adds it automatically well, but I still have `../../../` long tail reference.

also, when `Container` or `Component` that depended on `Screen` is changed to common component and move `Component` folder or `Component` is changed to dependent to move `Screen` folder, after moving it, I should change all `import`, so it's a very big problem.

## Solution
my solution is to use `babel-plugin-root-import` and `typescript` configuration to refer the root folder. for example, my `../../../Component/BannerContainer` is to be `~/Component/BannerContainer`.

### babel-plugin-root-import
execute the command below to install `babel-plugin-root-import` for making root folder reference.

```bash
npm install babel-plugin-root-import --save-dev
```

modify `babel.config.js` in RN(React Native) project like below.

```js
module.exports = {
  presets: ['module:metro-react-native-babel-preset'],
  plugins: [
    'babel-plugin-styled-components',
    [
      'babel-plugin-root-import',
      {
        rootPathPrefix: '~',
        rootPathSuffix: 'src',
      },
    ],
  ],
};
```

as you can see my folder structure, `src` folder has all source code. therefore, I use `src` folder not `root` folder.

{% include in-feed-ads.html %}

### typescript
if you're not typescript user, you don't need this section. I use typescript on RN(React Native) project, so I should set root folder reference to typescript configuration. if you want to know how to apply typescript to RN(React Native), see the blog below.

- [typescript]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}

modify `tsconfig.json` in RN(React Native) project like below.

```json
{
  "compilerOptions": {
    ...
    "baseUrl": "./src", // all paths are relative to the baseUrl
    "paths": {
      "~/*": ["*"] // resolve any `~/foo/bar` to `<baseUrl>/foo/bar`
    }
  },
  ...
}
```

## Complete
finally, we can say good-bye to `../../../../` when we import on RN(React Native). the root path reference makes the project clean and makes me feel better. I recommend you to add it before it's too late!