---
layout: 'post'
permalink: '/react-native/nativebase/'
paginate_path: '/react-native/:num/nativebase/'
lang: 'ko'
categories: 'react-native'
comments: true

title: 'NativeBase'
description: '기본 Component UI에 NativeBase 라이브러리를 사용해보자.'
image: '/assets/images/category/react-native/nativebase.jpg'
---


## 개요
RN 프로젝트에 material ui components인 [NativeBase](https://nativebase.io/){:rel="nofollow noreferrer" target="_blank" }를 적용해 보자.

## 라이브러리 설치
아래에 명령어로 NativeBase를 설치합니다.

{% include_relative common/installation.md %}

설치가 완료되면 아래에 명령어로 NativeBase와 프로젝트를 연결합니다.

{% include_relative common/link.md %}

## 사용법
우리는 기본적으로 사용한적이 있는 경우만 블로그로 작성합니다. 따라서 여기에 작성된 내용은 우리가 사용할 때마다 추가될 것입니다.

사용법에 대한 자세한 사항은 공식 홈페이지를 참조하세요.
- 공식 사이트: [NativeBase](https://nativebase.io/){:rel="nofollow noreferrer" target="_blank" }

## ActionSheet
ActionSheet를 사용하기 위해서는 프로젝트 전체를 NativeBase의 ```<Root>``` 컴포넌트로 감싸줘야 합니다.

{% include_relative common/action_sheet-1.md %}

ActionSheet를 표시하고 싶은 부분에 아래와 같이 코딩합니다.

{% include_relative common/action_sheet-2.md %}

- options: string 타입으로 된 리스트(string[])나 아이콘을 포함한 리스트(Array<{ text: string, icon?: string, iconColor?: string }>) 형식을 지원합니다.
- cancelButtonIndex: 취소 버튼의 위치입니다.
- destructiveButtonIndex: 삭제 버튼의 위치입니다.(빨간색 글자 버튼을 표시하고 싶은 위치입니다.)
- title: ActionSheet의 제목입니다.
- (buttonIndex: number) => { alert(buttonIndex); }: 선택된 버튼의 index를 넘겨줍니다.

## 참고
- 공식 사이트: [NativeBase](https://nativebase.io/){:rel="nofollow noreferrer" target="_blank" }