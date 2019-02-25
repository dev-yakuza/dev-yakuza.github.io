---
layout: 'post'
permalink: '/react-native/react-native-lottie/'
paginate_path: '/react-native/:num/react-native-lottie/'
lang: 'ko'
categories: 'react-native'
comments: true

title: '애프터이펙트(AEF) 사용'
description: 'RN(React Native) 프로젝트에서 어도비 애프터이펙트(Adobe After Effects)로 제작한 애니메이션을 적용해 보자.'
image: '/assets/images/category/react-native/react-native-lottie.jpg'
---


## 개요
최근 앱에 생동감을 넣기 위해 마이크로 인터렉션(Microinteractions)을 많이 사용하고 있습니다. 이번 블로그에서는 ```어도비 애프터이펙트(Adobe After Effects)```에서 작성한 애니메이션을 에어비엔비(Airbnb)가 만든 ```lottie``` 라이브러리를 사용하여 RN(React Native)에 적용하는 방법에 대해서 알아보겠습니다.

- lottie 공식 사이트: [https://airbnb.design/lottie/](https://airbnb.design/lottie/){:rel="nofollow noreferrer" target="_blank"}

## 설치
RN(React Native)에서 ```lottie``` 라이브러리를 사용하기 위해 아래의 명령어를 실행하여 ```lottie-react-native``` 라이브러리를 설치합니다.

```bash
npm install --save lottie-react-native
```

## 라이브러리 연결
RN(React Native)에서 ```lottie``` 라이브러리를 사용하기 위해 ```lottie-react-native``` 라이브러리를 설치를 완료하였다면 아래에 방법으로 OS에 맞게 라이브러리를 연결합니다.

### iOS
RN(React Native)에서 ```lottie``` 라이브러리를 iOS에 사용하기 위해 아래와 같이 ```lottie-react-native``` 라이브러리를 RN(React Native) 프로젝트와 연결합니다.

```bash
react-native link lottie-ios
react-native link lottie-react-native
```

그리고 ```ios/[project_name].xcodeproj```이나 ```ios/[project_name].xcworkspace``` 파일을 실행하여 xcode를 실행합니다. 그리고 아래와 같이 추가 설정을 해줍니다.

![lottie ios 추가 설정](/assets/images/category/react-native/react-native-lottie/ios-settings.png)

1. 왼쪽 메뉴에 프로젝트명 선택
1. ```TARGETS```에서 프로젝트명 선택
1. 상단 메뉴에서 ```General``` 선택
1. 스크롤해서 하단으로 이동하면 ```Embedded Binaries``` 항목이 보임. ```+``` 버튼을 누르고 ```Lottie.framework```를 검색, ```ios```용을 선택하여 추가

![lottie ios framework 추가 설정](/assets/images/category/react-native/react-native-lottie/add-lottie-framework.png)

### 안드로이드
위에 ```iOS``` 과정을 거쳤다면 ```lottie``` 라이브러리를 안드로이드에서 사용하기 위해 추가적으로 해줄 과정이 없습니다. 아래에 명령어를 실행했을때, 안드로이드는 ```lottie-react-native```와 연결이 되었습니다.

```bash
react-native link lottie-react-native
```

## 사용 방법
RN(React Native)에서 lottie를 사용하기 위해서는 어도비 애프터이펙트(Adobe After Effects)로 만든 애니메이션 파일이 필요합니다. 어도비 애프터이펙트(Adobe After Effects)에서 lottie에 필요한 애니메이션 파일을 만드는 방법에 대해서는 이 블로그에서 다루지 않습니다. 아래에 링크를 참고하여 어도비 애프터이펙트(Adobe After Effects)에서 lottie 애니메이션 파일을 생성하세요.

- [https://github.com/airbnb/lottie-web](https://github.com/airbnb/lottie-web){:rel="nofollow noreferrer" target="_blank"}

또는 아래에 사이트에서 필요한 마이크로 인터렉션(Microinteractions) 파일을 검색하세요.

- [https://lottiefiles.com/](https://lottiefiles.com/){:rel="nofollow noreferrer" target="_blank"}

어도비 애프터이펙트(Adobe After Effects) 또는 사이트에서 다운로드한 파일은 ```json``` 형식으로 되어있습니다.

RN(React Native)에서 lottie를 이용하여 마이크로 인터렉션(Microinteractions)을 적용하기 위해 아래와 같이 코드를 작성합니다.

```js
...
import LottieView from 'lottie-react-native';
...
export default class BasicExample extends React.Component {
  render() {
    return (
      <LottieView
        source={require('./animation.json')}
        autoPlay
        loop
      />
    );
  }
}
...
```

## 애니메이션 파일에 이미지가 포함된 경우
어도비의 애프터이펙트(AEF)를 사용하여 애니메이션을 제작하다보면, 애니메이션에 이미지를 포함해야 하는 경우가 발생합니다.

이미지를 포함한 애니메이션을 lottie용으로 내보내면 아래와 같이 이미지가 포함된 ```data.json```을 확인 할 수 있습니다.

```json
// data.json
{
  ...
  "assets": [
    {
      "id": "image_0",
      "w": 588,
      "h": 792,
      "u": "images/",
      "p": "main_character.png",
      "e": 0
    }
  ]
  ...
```

이미지가 포함된 애니메이션 파일은 보통의 파일과는 다르게 이미지 파일을 따로 추가해 주는 과정이 필요합니다.


### iOS
RN(React Native) 프로젝트 폴더에서 ```ios/[project name].xcworkspace```(또는 ```ios/xcodeproj```)를 선택하여 xcode를 실행합니다.

![lottie ios 이미지 추가](/assets/images/category/react-native/react-native-lottie/lottie_ios_image_add.png)

위와 같이 왼쪽 메뉴에서 프로젝트를 선택하고 ```Resources``` 폴더를 우클릭하여 ```Add Files to [project name]```을 선택합니다.

![lottie ios 이미지 추가 - 파일 선택](/assets/images/category/react-native/react-native-lottie/lottie_ios_image_add_select_file.png)

추가하고 싶은 파일을 선택하고, 하단에 ```Copy items if needed``` 옵션을 선택하고 추가합니다.

위와 같이 ```Resources``` 폴더가 보이지 않는 경우, 왼쪽 메뉴에서 프로젝트명을 우클릭한 후, ```New Group without Folder```를 선택하고 추가된 그룹명을 ```Resources```로 수정합니다.

![lottie ios 이미지 추가 - resources 그룹 추가](/assets/images/category/react-native/react-native-lottie/lottie_ios_image_add_resources_group.png)


### 안드로이드
안드로이드는 iOS보다 간단합니다. RN(React Native) 프로젝트의 ```android/app/src/main/assets```에 애니메이션에 포함된 이미지를 넣을 폴더를 생성합니다. 여기에서는 ```images``` 폴더를 생성하였습니다. 그리고 해당 폴더에 이미지를 복사합니다. (```android/app/src/main/assets/images```)

복사를 완료하였다면, 아래와 같이 소스코드에 ```imageAssetsFolder={'images'}```를 추가합니다.

```js
<LottieView
  source={require('./animation.json')}
  autoPlay
  loop
  imageAssetsFolder={'images'}
/>
```

### Git 저장소
애니메이션 파일에 이미지가 포함된 경우에 ```Lottie```를 사용하는 방법에 관한 git 저장소(Repository)를 만들었습니다. 아래에 링크를 통해 예제를 확인하실 수 있습니다.

- git 저장소: [react_native_lottie_exercise](https://github.com/dev-yakuza/react_native_lottie_exercise){:rel="nofollow noreferrer" target="_blank"}


## 에러 대응
RN(React Native) 프로젝트에 ```react-native-lottie```를 구현해서 잘 사용하다가 다른 라이브러리를 설치하고 빌드할 때, 아래와 같은 에러가 발생하였다.

```bash
Build system information

error: Cycle in dependencies between targets 'LottieLibraryIOS' and 'LottieReactNative'; building could produce unreliable results.
Cycle path: LottieLibraryIOS → LottieReactNative → LottieLibraryIOS
Cycle details:
...
```

RN(React Native) 프로젝트의 ```Pods``` 폴더나 ```node_modules```를 지우고 다시 설치해도 계속 문제가 발생하였다.

아래에서 설명하는 방법으로 제 RN(React Native) 프로젝트는 정상적으로 빌드가 되었습니다. 다른 분들도 저와 같은 문제가 있으시면 아래에 방법을 한번 시도해 보시기 바랍니다.

RN(React Native) 프로젝트의 ```ios/[project_name].xcworkspace``` 파일을 실행하여 xcode를 실행합니다.

![lottie 빌드 에러 대응](/assets/images/category/react-native/react-native-lottie/lottie_fix_error.png)

xcode가 실행되면 위와 같이 ```File > Workspace Settings...```를 선택합니다.

![lottie 빌드 에러 대응: 빌드 시스템 변경](/assets/images/category/react-native/react-native-lottie/change_build_system.png)

위와 같이 빌드 시스템(Build System)을 ```New Build System (Default)``` 에서 ```Legacy Build System```으로 변경합니다.

저의 경우는 위와 같이 빌드 시스템(Build System)을 변경한 후 RN(React Native)를 빌드하면 정상적으로 빌드되는 것을 확인하였습니다. 다른 분들도 이 방법으로 해결이 되었으면 좋겠습니다.

### 안드로이드 빌드 에러
안드로이드에서 빌드하다 보면 아래와 같은 에러가 발생할 경우가 있습니다.

```bash
Execution failed for task ':app:transformClassesWithDexBuilderForDevDebug'.
```

이 경우, RN(React Native) 프로젝트 폴더의 ```android/app/build.gradle```를 열고 아래와 같이 수정합니다.

```xml
android{
    ...
    configurations.all {
        resolutionStrategy {
            force 'com.airbnb.android:lottie:2.5.5'
        }
    }
}
```

- 참고: [Java 8 compilation error version 2.5.6 ](https://github.com/airbnb/lottie-android/issues/822#issuecomment-401812260){:rel="nofollow noreferrer" target="_blank"}



## 완료
이것으로 RN(React Native)에 lottie를 이용하여 마이크로 인터렉션(Microinteractions)을 구현했습니다. 간단하죠? lottie로 애니메이션을 적용하는 것보다 애니메이션을 만드는게 더 힘들거 같습니다. 저는 애프터 이펙트(After Effects)를 사용할지 모르기 때문에 [https://lottiefiles.com/](https://lottiefiles.com/){:rel="nofollow noreferrer" target="_blank"} 사이트를 이용하고 있습니다. lottie를 이용하여 여러분도 여러분의 앱에 재미있는 마이크로 인터렉션(Microinteractions) 적용해 보세요.


## 참고
- lottie 공식 사이트: [https://airbnb.design/lottie/](https://airbnb.design/lottie/){:rel="nofollow noreferrer" target="_blank"}