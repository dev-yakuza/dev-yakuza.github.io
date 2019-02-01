---
published: false
layout: 'post'
permalink: '/react-native/react-native-linear-gradient/'
paginate_path: '/react-native/:num/react-native-linear-gradient/'
lang: 'ko'
categories: 'react-native'
comments: true

title: '그라데이션'
description: 'RN(React Native) 프로젝트에서 react-native-linear-gradient을 사용해서 그라데이션 백그라운드(background)를 만들어 보자.'
image: '/assets/images/category/react-native/react-native-linear-gradient.jpg'
---


## 개요
RN(React Native) 프로젝트를 진행하다 유저의 스와이프(Swipe) 방향에 따라 다른 동작을 하는 기능을 추가하게 되었습니다. 그래서 검색해 보니 ```react-native-swipe-gestures```라는 라이브러리를 발견하고 적용해 보았습니다. 이 블로그는 ```react-native-swipe-gestures```를 설치하고 사용하는 방법에 대해서 설명합니다.

- react-native-swipe-gestures 공식 사이트: [https://github.com/glepur/react-native-swipe-gestures](https://github.com/glepur/react-native-swipe-gestures){:rel="nofollow noreferrer" target="_blank"}

## 설치
아래에 명령어를 통해 ```react-native-swipe-gestures``` 라이브러리를 설치합니다.

```bash
npm install --save react-native-swipe-gestures
```

## 사용 방법
RN(React Native)에서 유저의 스와이프(Swipe)를 감지하기 위해 아래와 같이 소스를 수정합니다.

{% raw %}
```js
...
import GestureRecognizer from 'react-native-swipe-gestures';
...

render() {
  <GestureRecognizer
          onSwipeLeft={this._onSwipeLeft}
          onSwipeRight={this._onSwipeRight}
          config={{
            velocityThreshold: 0.3,
            directionalOffsetThreshold: 80,
          }}
          style={{
            flex: 1,
          }}>
          ...
  </GestureRecognizer>
}
...
private _onSwipeLeft = gestureState => {
  ...
  this.setState({
    ...
  });
};

private _onSwipeRight = gestureState => {
  ...
  this.setState({
    ...
  });
  ...
};
```
{% endraw %}

## 완료
이것으로 RN(React Native)에서 유저의 스와이프(Swipe) 동작을 감지하는 방법에 대해서 알아보았습니다. 간단한 기능도 점점 코딩을 하지 않고 복사 붙여넣기를 하고 있는 제 자신을 발견했네요... ```react-native-swipe-gestures``` 소스가 그리 길지 않으므로 소스를 보고 직접 구현하시는 것도 재미있을거 같습니다.


## 참고
- react-native-swipe-gestures 공식 사이트: [https://github.com/glepur/react-native-swipe-gestures](https://github.com/glepur/react-native-swipe-gestures){:rel="nofollow noreferrer" target="_blank"}