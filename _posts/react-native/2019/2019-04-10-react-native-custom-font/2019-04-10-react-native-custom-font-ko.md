---
layout: 'post'
permalink: '/react-native/react-native-custom-font/'
paginate_path: '/react-native/:num/react-native-custom-font/'
lang: 'ko'
categories: 'react-native'
comments: true

title: 'RN(Reacct Native)에서 커스텀 폰트 사용하기'
description: 'RN(React Native) 프로젝트에서 커스텀 폰트를 적용하고 사용하는 방법에 대해서 알아봅시다.'
image: '/assets/images/category/react-native/2019/react-native-custom-font/background.jpg'
---

## 개요
앱을 개발하다보면 특정 폰트를 적용할 경우가 발생합니다. 이 블로그에서는 RN(React Native)에 어떻게 특정 폰트를 적용하고 사용하는지 설명하려고 합니다. 저는 보통 구글의 `Noto Sans` 폰트를 사용하고 있습니다.

- 구글 Noto KR 폰트: [https://fonts.google.com/specimen/Noto+Sans+KR](https://fonts.google.com/specimen/Noto+Sans+KR){:rel="nofollow noreferrer" target="_blank"}
- 구글 Noto JP 폰트: [https://fonts.google.com/specimen/Noto+Sans+JP](https://fonts.google.com/specimen/Noto+Sans+JP){:rel="nofollow noreferrer" target="_blank"}

이 블로그에서는 폰트가 적용되었는지 확실하게 구분되게 하기 위해 아래에 폰트를 적용하고 사용하는 방법에 대해서 설명합니다.

- Dancing Script: [https://fonts.google.com/specimen/Dancing+Script](https://fonts.google.com/specimen/Dancing+Script){:rel="nofollow noreferrer" target="_blank"}

## 폰트 다운로드
RN(React Native)에서 사용하고자 하는 폰트를 다운로드합니다. 여기에서는 개요에서 소개한 `Dancing Script` 폰트를 사용합니다. 아래에 링크를 눌러 폰트 페이지로 이동합니다.

- Dancing Script: [https://fonts.google.com/specimen/Dancing+Script](https://fonts.google.com/specimen/Dancing+Script){:rel="nofollow noreferrer" target="_blank"}

위에 링크를 선택하면 아래와 같은 화면을 볼 수 있습니다.

![RN(React Native) 커스텀 폰트 적용 - google dancing script](/assets/images/category/react-native/2019/react-native-custom-font/google-dancing-script-font-site.jpg)

오른쪽 위에 `SELECT THIS FONT`를 선택합니다.

![RN(React Native) 커스텀 폰트 적용 - 폰트 선택](/assets/images/category/react-native/2019/react-native-custom-font/font-select.jpg)

그러면 위와 같이 오른쪽 하단에 `Family Selected`가 활성화 됩니다. `Family Selected`를 클릭합니다.

![RN(React Native) 커스텀 폰트 적용 - 폰트 다운로드](/assets/images/category/react-native/2019/react-native-custom-font/download-font.jpg)

위와 같은 화면이 보이면, 오른쪽 위에 있는 다운로드 버튼을 눌러 폰트를 다운로드 합니다.

{% include in-feed-ads.html %}

## 폰트 적용
다운로드 받은 폰트를 각 OS에 맞게 설정해야 합니다. 우선 공통된 js 소스부터 수정하도록 하겠습니다.

### javascript 소스 수정
폰트를 적용하기 위해 아래와 같이 소스 코드를 수정합니다.

```js
import * as React from 'react';
import { Platform } from 'react-native';
import Styled from 'styled-components/native';

const instructions = Platform.select({
  ios: 'Press Cmd+R to reload,\n' + 'Cmd+D or shake for dev menu',
  android:
    'Double tap R on your keyboard to reload,\n' +
    'Shake or press menu button for dev menu',
});

const Container = Styled.View`
    flex: 1;
    justify-content: center;
    align-items: center;
    background-color: #F5FCFF;
`;
const Welcome = Styled.Text`
  font-size: 20px;
  text-align: center;
  margin: 10px;
  font-family: 'DancingScript-Bold'; // <<<<<<<<<<<<< Add here
`;
const Instructions = Styled.Text`
  text-align: center;
  color: #333333;
  margin-bottom: 5px;
  font-family: 'DancingScript-Regular'; // <<<<<<<<<<<<< Add here
`;

interface Props {}
interface State {}

export default class App extends React.Component<Props, State> {
  render() {
    return (
      <Container>
        <Welcome>Welcome to React Native!</Welcome>
        <Instructions>To get started, edit App.js</Instructions>
        <Instructions>{instructions}</Instructions>
      </Container>
    );
  }
}
```

저는 보통 RN(React Naitve) 프로젝트에 `typescript`와 `styled-components`를 사용하여 개발하고 있습니다. 그래서 소스의 형태가 조금 다를 수 있습니다. RN(React Native) 프로젝트에 `typescript`와 `styled-components`를 사용하는 방법에 대해서 궁금하신 분들은 아래에 링크를 참고하시기 바랍니다.

- [typescript]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}
- [styled-components]({{site.url}}/{{page.categories}}/styled-components/){:target="_blank"}

### iOS
RN(React Native) 프로젝트를 실행하면 아래와 같이 기본 폰트가 적용된 화면을 볼 수 있습니다.(또는 폰트를 찾을수 없어 에러가 발생합니다.)

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2019/react-native-custom-font/ios-basic-font.jpg" alt="RN(React Native) 커스텀 폰트 ios 적용 - 기본 폰트">
</div>

다운로드 받은 폰트 파일을 `ios/Fonts` 폴더를 만들고 그 안에 복사합니다.

![RN(React Native) 커스텀 폰트 ios 적용 - 폰트 복사](/assets/images/category/react-native/2019/react-native-custom-font/ios-copy-fonts.jpg)

폰트 파일을 복사하였다면 `ios/project_name.xcodeproj`이나 `ios/project_name.xcworkspace`을 실행하여 xcode를 실행합니다.

![RN(React Native) 커스텀 폰트 ios 적용 - xcode에 폰트 넣기](/assets/images/category/react-native/2019/react-native-custom-font/ios-create-reference.jpg)

왼쪽 상단에 자신의 프로젝트명을 오른쪽 클릭하여 `Add Files to "project_name"...`을 선택합니다.

![RN(React Native) 커스텀 폰트 ios 적용 - xcode에 폰트 추가](/assets/images/category/react-native/2019/react-native-custom-font/ios-add-font.jpg)

위와 같이 파일 선택화면이 나오면 우리가 추가한 `ios/Fonts` 폴더를 선택하고 `Create folder references`를 선택한 후, `Add`를 눌러 폴더를 추가합니다.

![RN(React Native) 커스텀 폰트 ios 적용 - Info.plist에 폰트 추가](/assets/images/category/react-native/2019/react-native-custom-font/ios-add-font-to-info-plist.jpg)

왼쪽 상단에 프로젝트명을 선택하고 `TARGETS`도 자신의 프로젝트명을 선택합니다. 상단 메뉴에서 `Info`를 선택하여 `Info.plist`의 내용을 확인합니다. `Info.plist`에 `Fonts provided by application`을 추가하고 위와 같이 폰트 파일을 추가합니다.

RN(React Native) 프로젝트를 다시 실행하면 아래와 같이 폰트 파일이 적용된 것을 확인할 수 있습니다.

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2019/react-native-custom-font/ios-font-applied.jpg" alt="RN(React Native) 커스텀 폰트 ios 적용">
</div>

{% include in-feed-ads.html %}

### 안드로이드
안드로이드에서 RN(React Native) 프로젝트를 실행하면 아래와 같이 기본 폰트가 적용된 화면을 볼 수 있습니다.

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2019/react-native-custom-font/android-basic-font.jpg" alt="RN(React Native) 커스텀 폰트 안드로이드 적용 - 기본 폰트">
</div>

안드로이드는 iOS보다 간단하게 적용할 수 있습니다. `android/app/src/main/assets/fonts` 폴더를 생성한 후 다운로드 받은 폰트 파일을 추가합니다.

![RN(React Native) 커스텀 폰트 안드로이드 적용 - 폰트 추가](/assets/images/category/react-native/2019/react-native-custom-font/android-add-font.jpg)

그리고 RN(React Native) 프로젝트를 실행하면 아래와 같이 폰트가 적용된 것을 확인할 수 있습니다.

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2019/react-native-custom-font/android-font-applied.jpg" alt="RN(React Native) 커스텀 폰트 안드로이드 적용 - 커스텀 폰트 적용">
</div>

## Github 저장소(Repository)
위에서 작업한 내용을 github에 공개하였습니다. 혹시 잘 안되시는 분들은 저장소(Repository)를 복사(Clone)하셔서 직접 확인해 보시기 바랍니다.

- github 저장소(Repository): [react_native_custom_font](https://github.com/dev-yakuza/react_native_custom_font){:target="_blank"}

## 완료
이로써 RN(React Native) 프로젝트에 커스텀 폰트를 적용하는 방법에 대해서 알아보았습니다. 앱을 아름답게 표현하기 위해서는 역시 폰트도 굉장히 중요한거 같네요. 여러분도 커스텀 폰트 적용으로 앱을 좀 더 아릅답게 만들어보세요!
