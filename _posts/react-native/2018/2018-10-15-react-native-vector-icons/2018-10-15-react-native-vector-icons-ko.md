---
layout: 'post'
permalink: '/react-native/react-native-vector-icons/'
paginate_path: '/react-native/:num/react-native-vector-icons/'
lang: 'ko'
categories: 'react-native'
comments: true

title: 'react-native-vector-icons'
description: 'react-native-vector-icons 라이브러리를 사용하여 아이콘을 표시해보자.'
image: '/assets/images/category/react-native/react-native-vector-icons.jpg'
---

<div id="contents_list" markdown="1">

## 목차

1. [개요](#개요)
1. [라이브러리 설치](#라이브러리-설치)
1. [라이브러리 연결](#라이브러리-연결)
    - [0.59 이하](#059-이하)
    - [0.60 이상](#060-이상)
        - [iOS](#ios)
        - [Android](#android)
1. [사용법](#사용법)
1. [Material icons](#material-icons)
1. [참고](#참고)

</div>

## 개요

RN 프로젝트에 벡터 아이콘을 사용하기 위해 [react-native-vector-icons](https://github.com/oblador/react-native-vector-icons){:rel="nofollow noreferrer" target="_blank" } 라이브러리를 사용해 보자.

## 라이브러리 설치

아래에 명령어로 react-native-vector-icons을 설치합니다.

```bash
npm install react-native-vector-icons --save
# For Typescript
npm install --save-dev @types/react-native-vector-icons
```

설치가 완료되면 아래에 명령어로 라이브러리와 프로젝트를 연결합니다.

## 라이브러리 연결

react-native-vector-icons을 사용하기 위해서는 설치한 라이브러리를 연결할 필요가 있습니다.

### 0.59 이하

아래에 명령어를 사용하여 라이브러리를 연결합니다.

```bash
react-native link react-native-vector-icons
```

{% include in-feed-ads.html %}

### 0.60 이상

0.60 이상부터는 수동으로 연결해야 합니다.

#### iOS

iOS에 react-native-vector-icons을 연결하기 위해 `ios/[project].xcworkspace`을 선택하여 Xcode를 실행합니다.

![react-native-vector-icons 설치법 - Xcode Fonts 그룹 추가](/assets/images/category/react-native/2018/react-native-vector-icons/xcode_add_new_group.jpg)

Xcode가 실행되면 위와 같이 프로젝트를 우클릭한 후 `New Group` 메뉴를 선택하고 `Fonts` 라는 이름으로 그룹을 생성합니다.

![react-native-vector-icons 설치법 - Xcode Fonts 경로](/assets/images/category/react-native/2018/react-native-vector-icons/react-native-vector-icons_font_path.jpg)

Fonts 그룹을 생성하였다면, 위와 같이 `node_modules/react-native-vector-icons/Fonts/`로 이동하고 하위에 있는 모든 폰트를 Xcode의 Fonts 그룹으로 드래그합니다.

![react-native-vector-icons 설치법 - Xcode Fonts Copy items if needed](/assets/images/category/react-native/2018/react-native-vector-icons/copy-items-if-needed.jpg)

드래그를 하면 위와 같은 화면을 볼 수 있습니다. `Copy items if needed`가 체크된 상태에서 오른쪽 하단의 `Finish` 버튼을 선택합니다.

마지막으로 `ios/[project]/Info.plist` 파일을 열고 아래의 내용을 추가합니다.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    ...
  <key>UIViewControllerBasedStatusBarAppearance</key>
  <false/>
  <key>UIAppFonts</key>
  <array>
    <string>AntDesign.ttf</string>
    <string>Entypo.ttf</string>
    <string>EvilIcons.ttf</string>
    <string>Feather.ttf</string>
    <string>FontAwesome.ttf</string>
    <string>FontAwesome5_Brands.ttf</string>
    <string>FontAwesome5_Regular.ttf</string>
    <string>FontAwesome5_Solid.ttf</string>
    <string>Foundation.ttf</string>
    <string>Ionicons.ttf</string>
    <string>MaterialCommunityIcons.ttf</string>
    <string>MaterialIcons.ttf</string>
    <string>Octicons.ttf</string>
    <string>SimpleLineIcons.ttf</string>
    <string>Zocial.ttf</string>
    <string>Fontisto.ttf</string>
  </array>
</dict>
```

Xcode에서 `cmd + shift + k`를 눌러 `Clean Build Folder`를 실행합니다.

{% include in-feed-ads.html %}

#### Android

안드로이드는 iOS보다 설정이 간단합니다. `android/app/build.gradle` 파일을 열고 아래에 내용을 추가합니다.

```js
...
apply from: "../../node_modules/react-native/react.gradle"
apply from: "../../node_modules/react-native-vector-icons/fonts.gradle" // add this line
...
```

그리고 `node_modules/react-native-vector-icons/Fonts/` 하위에 파일들을 `android/app/src/main/assets/fonts` 폴더로 복사합니다.(assets/fonts 폴더가 존재하지 않으면 폴더를 생성합니다.)

마지막으로 안드로이드 프로젝트를 Android Studio를 열고 자동으로 Gradle sync가 되는 것을 기다립니다.

안드로이드 프로젝트를 Android Studio를 열기 위해 아래에 명령어를 사용할 수 있습니다.

```bash
# in RN project root folder
open -a /Applications/Android\\ Studio.app ./android
```

## 사용법

우리는 기본적으로 사용한적이 있는 경우만 블로그로 작성합니다. 따라서 여기에 작성된 내용은 우리가 사용할 때마다 추가될 것입니다.

사용법에 대한 자세한 사항은 공식 홈페이지를 참조하세요.

- 공식 사이트: [react-native-vector-icons](https://github.com/oblador/react-native-vector-icons){:rel="nofollow noreferrer" target="_blank" }

{% include in-feed-ads.html %}

## Material icons

Material icon을 사용하는 방법

```js
...
import Icon from 'react-native-vector-icons/FontAwesome';
...

export default class Home extends React.Component<Props, State> {
    render() {
        return (
            <View>
                <Icon name="home" size={24} color="#ffffff" />
            </View>
        );
    }
}
```

## 참고

- 공식 사이트: [react-native-vector-icons](https://github.com/oblador/react-native-vector-icons){:rel="nofollow noreferrer" target="_blank" }
