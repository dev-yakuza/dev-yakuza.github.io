---
layout: 'post'
permalink: '/react-native/react-native-animatable/'
paginate_path: '/react-native/:num/react-native-animatable/'
lang: 'ko'
categories: 'react-native'
comments: true

title: 'react-native-animatable'
description: 'react-native-animatable을 사용해서 간단하게 RN(react native)에 애니메이션을 추가해 보자.'
image: '/assets/images/category/react-native/react-native-animatable.jpg'
---


## 개요
기본적으로 많이 사용되는 애니메이션을 모아둔 [react-native-animatable](https://github.com/oblador/react-native-animatable){:rel="nofollow noreferrer" target="_blank"} 라이브러리를 사용하여 애니메이션을 구현하는 방법에 대해서 설명합니다.

이 블로그에서는 RN(react native)에 ```typescript```와 ```styled-components```가 적용된 프로젝트를 가지고 설명합니다. RN(react native)에 ```typescript```와 ```styled-components```를 적용하는 방법에 대해서는 이전 블로그를 확인해 주세요.

- [typescript]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}
- [styled-components]({{site.url}}/{{page.categories}}/styled-components/){:target="_blank"}

## 라이브러리 설치
react-native-animatable 라이브러리를 사용하기 위해 아래에 명령어로 라이브러리를 설치합니다.

```bash
npm install react-native-animatable --save
```

## 기본 사용법
아래와 같이 애니메이션을 추가하고 싶은 부분에 소스를 추가합니다.

```js
...
import * as Animatable from 'react-native-animatable';
...

render() {
  ...
  return (
    <Animatable.Text animation="zoomInUp">Zoom me up, Scotty</Animatable.Text>
  );
}
```

## 이벤트를 통한 사용법
RN(react native)의 ```ref```를 사용하여 사용자 이벤트가 발생할 때, 애니메이션을 진행할 수 있게 만들 수 있습니다.

```js
...
import * as Animatable from 'react-native-animatable';
...

export default class Page extends React.Component<Props, State> {
  private AnimationRef;
  ...
  render() {
    ...
    return (
      <TouchableWithoutFeedback onPress={this._onPress}>
        <Animatable.View ref={ref => (this.AnimationRef = ref)}>
          <Text>Bounce me!</Text>
        </Animatable.View>
      </TouchableWithoutFeedback>
    );
  }
  ...
  private _onPress = () => {
    this.AnimationRef.bounce();
  }
  ...
}
```

## styled-components
styled-components로 만든 컴포넌트(component)에 애니메이션을 적용하는 방법입니다.

```js
...
import styled from 'styled-components/native';
import * as Animatable from 'react-native-animatable';
...
const StyledImage = Animatable.createAnimatableComponent(styled.Image``);
...
render() {
  ...
  return (
    <StyledImage
      animation="bounceIn"
      delay={1000}
      useNativeDriver={true}
      source={src}
    />
  );
}
...
```

## 사용 가능한 애니메이션
사용 가능한 애니메이션은 ```react-native-animatable```의 공식 저장소(Repository)에서 예제와 함께 확인할 수 있습니다.

- [https://github.com/oblador/react-native-animatable](https://github.com/oblador/react-native-animatable){:rel="nofollow noreferrer" target="_blank"}

아래는 사용 가능한 애니메이션 리스트입니다.

- bounce
- flash
- jello
- pulse
- rotate
- rubberBand
- shake
- swing
- tada
- wobble
- bounceIn
- bounceInDown
- bounceInUp
- bounceInLeft
- bounceInRight
- bounceOut
- bounceOutDown
- bounceOutUp
- bounceOutLeft
- bounceOutRight
- fadeIn
- fadeInDown
- fadeInDownBig
- fadeInUp
- fadeInUpBig
- fadeInLeft
- fadeInLeftBig
- fadeInRight
- fadeInRightBig
- fadeOut
- fadeOutDown
- fadeOutDownBig
- fadeOutUp
- fadeOutUpBig
- fadeOutLeft
- fadeOutLeftBig
- fadeOutRight
- fadeOutRightBig
- flipInX
- flipInY
- flipOutX
- flipOutY
- lightSpeedIn
- lightSpeedOut
- slideInDown
- slideInUp
- slideInLeft
- slideInRight
- slideOutDown
- slideOutUp
- slideOutLeft
- slideOutRight
- zoomIn
- zoomInDown
- zoomInUp
- zoomInLeft
- zoomInRight
- zoomOut
- zoomOutDown
- zoomOutUp
- zoomOutLeft
- zoomOutRight

## 완료
간단한 애니메이션을 빠르게 도입하고 싶을 때, ```react-native-animatable``` 라이브러리를 사용하는 것을 추천합니다.

## 참고
- [https://github.com/oblador/react-native-animatable](https://github.com/oblador/react-native-animatable){:rel="nofollow noreferrer" target="_blank"}