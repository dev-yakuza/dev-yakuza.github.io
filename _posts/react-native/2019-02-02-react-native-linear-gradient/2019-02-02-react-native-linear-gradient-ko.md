---
layout: 'post'
permalink: '/react-native/react-native-linear-gradient/'
paginate_path: '/react-native/:num/react-native-linear-gradient/'
lang: 'ko'
categories: 'react-native'
comments: true

title: '그라데이션(Gradient)'
description: 'RN(React Native) 프로젝트에서 react-native-linear-gradient을 사용해서 그라데이션(Gradient) 백그라운드(background)를 만들어 보자.'
image: '/assets/images/category/react-native/react-native-linear-gradient.png'
---


## 개요
RN(React Native)에서 백그라운드로 그라데이션(Gradaient)을 넣기가 쉽지 않습니다. 이 블로그에서는 ```react-native-linear-gradient```을 사용하여 RN(React Native) 프로젝트에 그라데이션(Gradient) 배경을 넣는 방법에 대해서 소개하겠습니다.

- react-native-linear-gradient 공식 사이트: [https://github.com/react-native-community/react-native-linear-gradient](https://github.com/react-native-community/react-native-linear-gradient){:rel="nofollow noreferrer" target="_blank"}

## 설치
RN(React Native)에서 그라데이션(Gradient)을 사용하기 위해 아래에 명령어를 통해 ```react-native-linear-gradient``` 라이브러리를 설치합니다.

```bash
npm install --save react-native-linear-gradient
```

## 라이브러리 연결
RN(React Native)에서 ```react-native-linear-gradient```를 사용하기 위해 아래에 명령어로 ```react-native-linear-gradient``` 라이브러리와 RN(React Native) 프로젝트를 연결합니다.

```bash
react-native link react-native-linear-gradient
```

## 사용 방법
RN(React Native)에서 ```react-native-linear-gradient```를 사용하여 그라데이션(Gradient)을 구현하는 방법은 아래와 같습니다. (소스코드는 react-native-linear-gradient 공식 사이트에서 가져왔습니다.)

```js
import LinearGradient from 'react-native-linear-gradient';

// Within your render function
<LinearGradient colors={['#4c669f', '#3b5998', '#192f6a']} style={styles.linearGradient}>
  <Text style={styles.buttonText}>
    Sign in with Facebook
  </Text>
</LinearGradient>

// Later on in your styles..
var styles = StyleSheet.create({
  linearGradient: {
    flex: 1,
    paddingLeft: 15,
    paddingRight: 15,
    borderRadius: 5
  },
  buttonText: {
    fontSize: 18,
    fontFamily: 'Gill Sans',
    textAlign: 'center',
    margin: 10,
    color: '#ffffff',
    backgroundColor: 'transparent',
  },
});
```

우리는 배경화면 그라데이션(Gradient)을 사용하기 위해 아래의 소스코드를 사용하고 있습니다.

```js
...
import LinearGradient from 'react-native-linear-gradient';
import styled from 'styled-components/native';
...
const Background = styled(LinearGradient)`
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
`;
...
<Background
  colors={[item.background[0], item.background[1]]}
  start={{
    x: item.direction.start.x,
    y: item.direction.start.y,
  }}
  end={{ x: item.direction.end.x, y: item.direction.end.y }}
/>
...
```

또한 페이지 전환시 배경 그라데이션(Gradient)을 자연스럽게 전환하기 위해 애니메이션을 적용했습니다. 애니메이션은 아래에 사이트를 참고하여 제작하였습니다.

- 그라데이션 애니메이션 예제: [AnimatedGradient](https://github.com/dslounge/rn-animated-gradient-example/tree/master/src/ColorExample/AnimatedGradient){:rel="nofollow noreferrer" target="_blank"}


## 완료
RN(React Native)로 개발한 앱에 그라데이션(Gradient) 배경을 활용하여 좀 더 이쁜 앱을 만들어 보세요.


## 참고
- react-native-linear-gradient 공식 사이트: [https://github.com/react-native-community/react-native-linear-gradient](https://github.com/react-native-community/react-native-linear-gradient){:rel="nofollow noreferrer" target="_blank"}
- 그라데이션 애니메이션 예제: [AnimatedGradient](https://github.com/dslounge/rn-animated-gradient-example/tree/master/src/ColorExample/AnimatedGradient){:rel="nofollow noreferrer" target="_blank"}