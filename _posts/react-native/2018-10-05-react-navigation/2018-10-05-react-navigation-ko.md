---
layout: 'post'
permalink: '/react-native/react-navigation/'
paginate_path: '/react-native/:num/react-navigation/'
lang: 'ko'
categories: 'react-native'
comments: true

title: 'react-navigation'
description: 'react-navigation을 활용하여 어플을 개발해 보자.'
image: '/assets/images/category/react-native/react-navigation.jpg'
---


## react-native 프로젝트 생성
typescript와 styled-components를 적용한 프로젝트에서 진행합니다. RN에 typescript와 styled-components를 적용하는 방법은 이전 블로그를 참고하세요.
- [typescript]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}
- [styled-components]({{site.url}}/{{page.categories}}/styled-components/){:target="_blank"}

## react-navigation 설치
react-navigation 라이브러리를 아래에 명령어를 통해 설치합니다.

```bash
npm install --save react-navigation
npm install --save react-native-gesture-handler
```

## react-native-gesture-handler 라이브러리 연결
아래에 명령어를 통해 ```react-native-gesture-handler``` 라이브러리를 RN(react-native) 프로젝트에 연결합니다.

```bash
react-native link react-native-gesture-handler
```

## 사용법
react-navigation를 사용하는 여러가지 방법들이 공식 홈페이지에 자세히 나와있습니다. 자세한 내용은 링크를 참고해주세요.

- 공식 홈페이지: [https://reactnavigation.org/docs](https://reactnavigation.org/docs){:rel="nofollow noreferrer" target="_blank" }

우리는 공식 홈페이지를 참고하여 기본적인 사용법을 정리한 저장소(Repository)를 만들었습니다. ```react-navigation```을 사용하기 전에 이 저장소(Repository)를 확인한다면 기본적인 구조를 잡을 때, 도움이 될거 같습니다.

- react-navigation-exercise: [https://github.com/dev-yakuza/react-navigation-exercise](https://github.com/dev-yakuza/react-navigation-exercise){:rel="nofollow noreferrer" target="_blank" }

이 저장소(Repository)에 구현된 내용을 설명하도록 하겠습니다.

### 사용할 네비게이션
사용할 네비게이션(Navigation)을 추가(import)하여 사용합니다.

```js
import {
  createSwitchNavigator,
  createBottomTabNavigator,
  createStackNavigator,
  createAppContainer,
} from 'react-navigation';
```

### createAppContainer
앱(App)에서 ```react-navigation```을 사용하기 위해서는 ```createAppContainer```을 최상위 네비게이션(Navigation)에 사용해야 합니다.

### createSwitchNavigator
앱(App)이 기본적으로 로그인 기능을 가지고 있다면 ```createSwitchNavigator``` 사용을 권장합니다. 우리의 저장소(Repository)는 Switch Navigation을 기본 네비게이션(Navigation)으로 사용하고 있습니다.

```js
export default createAppContainer(
  createSwitchNavigator(
    {
      AuthLoading,
      Auth,
      MainNavi,
    },
    {
      initialRouteName: 'AuthLoading',
    }
  )
);
```

### createStackNavigator
이 ```createStackNavigator```는 뷰(View) 위에 다른 뷰(View)를 쌓는(Stack) 네비게이션(Navigation)입니다. 우리는 이 네비게이션(Navigation)을 사용하여 탭 네비게이션(Tab Navigation)위에 전체 화면의 뷰(View)를 표시할 때, 탭 네비게이션(Tab Navigation)안에서 다른 뷰(View)를 표시할 때 사용합니다.

```js
const MainNavi = createStackNavigator({
  MainTab: {
    screen: MainTab,
    navigationOptions: ({ navigation }) => ({
      header: null,
    }),
  },
  FullDetail,
});
```

### createBottomTabNavigator
이 ```createBottomTabNavigator```를 사용하여 하단에 탭 네비게이션(Tab Navigation)을 표시합니다.

```js
const MainTab = createBottomTabNavigator({
  FirstTabStack,
  SecondTab,
  ThirdTab,
});
```

### 네비게이션 전환
뷰(View)에서 다른 뷰(View)로 전환할 때, 아래에 코드를 사용합니다.

```js
this.props.navigation.navigate('MainTab');
```

## Navigation bar 숨기기
아래에 코드로 navigation bar를 숨길 수 있습니다.

```js
...
export default class Home extends React.Component<Props, State> {
  static navigationOptions = { header: null };

  render() {
    return (
      <Container>
        <StyledText>Home screen!</StyledText>
      </Container>
    );
  }
}
...
```

- static navigationOptions: 네비게이션의 옵션을 설정합니다.
- { header: null }: navigation header bar를 비활성화합니다.

## 참고
- 공식 홈페이지: [react-navigation](https://reactnavigation.org/docs){:rel="nofollow noreferrer" target="_blank" }