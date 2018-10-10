---
layout: 'post'
permalink: '/react-native/styled-components/'
paginate_path: '/react-native/:num/styled-components/'
lang: 'ko'
categories: 'react-native'
comments: true

title: 'styled-components'
description: 'react-native 스타일링을 위해 styled-components 라이브러리를 활용하는 방법에 대해 알아보자.'
image: '/assets/images/category/react-native/styled-components.jpg'
---


## react-native 프로젝트 생성
typescript를 적용한 프로젝트에서 진행합니다. RN에 typescript를 적용하는 방법은 이전 블로그를 참고하세요.
- [typescript]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}

## styled-components 라이브러리 설치
styled-components 라이브러리와 typescript 연동을 위한 라이브러리를 설치합니다.

{% include_relative common/installation.md %}

- styled-components: styled-components 라이브러리입니다.
- @types/styled-components: typescript에 필요한 styled-components의 타입입니다.
- babel-plugin-styled-components: 필수는 아니지만 디버깅시 class명을 확인하기 쉽게 만들어 줍니다. ```.babelrc```에 아래와 같이 설정해 줍니다.

{% include_relative common/babel-plugin-styled-components.md %}

## 사용법
styled-components는 전체 스타일을 관리하기 위한 ```theme``` 기능을 제공합니다. ```theme```을 사용하는 방법과 기본적인 사용법을 알아봅니다.

### 기본 사용법
- 기본 스타일 적용

{% include_relative common/basic_usage.md %}

- props를 이용해 동적으로 스타일 적용

{% include_relative common/dynamic_styling.md %}

### Theme 사용법
공식 사이트에는 typescript를 이용하여 theme을 사용하는 방법이 자세히 나와있습니다.
- 공식 사이트: [styled-components#typescript](https://www.styled-components.com/docs/api#typescript){:rel="nofollow noreferrer" target="_blank"}
- 예제 참고 사이트: [Styled-Components-Typescript-Example](https://github.com/patrick91/Styled-Components-Typescript-Example){:rel="nofollow noreferrer" target="_blank"}

공식 사이트와 예제 사이트를 참고하면 styled-components를 사용하기 위해서는 상대 경로로 지정해야하는 문제가 있다.

그래서 우리는 공식 사이트 방식이 아닌 "props를 이용해 동적으로 스타일 적용"방법을 응용해서 사용합니다.

{% include_relative common/theme_usage.md %}

## 참고
- styled-components 공식 사이트: [styled-components](https://www.styled-components.com/docs){:rel="nofollow noreferrer" target="_blank"}
- 예제 참고 사이트: [Styled-Components-Typescript-Example](https://github.com/patrick91/Styled-Components-Typescript-Example){:rel="nofollow noreferrer" target="_blank"}