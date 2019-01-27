---
published: false
layout: 'post'
permalink: '/react-native/react-native-fs/'
paginate_path: '/react-native/:num/react-native-fs/'
lang: 'ko'
categories: 'react-native'
comments: true

title: '파일 시스템 사용'
description: 'RN(React Native) 프로젝트에서 react-native-fs 라이브러리를 사용하여 파일을 읽고 써봅시다.'
image: '/assets/images/category/react-native/react-native-fs.jpg'
---


## 개요
RN(React Native)로 개발할 때, 종종 파일 시스템(filesystem)을 이용하여 파일을 읽고 쓸 경우가 생깁니다. ```react-native-fs```는 RN(React Naitve)에서 파일 시스템(filesystem)을 쉽고 간단하게 사용할 수 있도록 도와주는 라이브러리입니다. 이 블로그에서는 ```react-native-fs```를 사용하는 방법에 대해서 알아보겠습니다.

- react-native-fs 공식 사이트: [https://github.com/itinance/react-native-fs](https://github.com/itinance/react-native-fs){:rel="nofollow noreferrer" target="_blank"}

## 설치
RN(React Native)에서 파일 시스템(filesystem)을 사용하기 위해 아래에 명령어를 통해 ```react-native-fs```를 설치합니다.

```bash
npm install --save react-native-fs
```

설치가 완료되면 아래에 명령어로 ```react-native-fs```를 RN(React Native) 프로젝트와 연결합니다.

```bash
react-native link react-native-fs
```

## 사용 방법
파일시스템(filesystem)을 이용하여 파일을 읽고 쓰는 다양한 방법이 [공식 사이트](https://github.com/chirag04/react-native-mail){:rel="nofollow noreferrer" target="_blank"}에 자세히 나와있습니다. 여기에서는 간단하게 파일을 읽고 쓰는 부분에 대해서 알아보겠습니다.

### 디렉토리
아래는 ```react-native-fs```에서 정의하는 파일시스템의 디렉토리/패스(filesystem directory/path)입니다.

- MainBundlePath: 메인 번들 폴더(Main Bundle Directory)의 절대 위치입니다.(안드로이드에서는 사용이 불가능합니다.)
- CachesDirectoryPath: 캐시 폴더(Cache Directory)의 절대 위치입니다.
- ExternalCachesDirectoryPath: 외부 캐시 폴더(External Cache Directory)의 절대 위치입니다.(iOS에서는 사용이 불가능합니다.)
- DocumentDirectoryPath: 도큐먼트 폴더(Document Directory)의 절대 위치입니다.
- TemporaryDirectoryPath: 임시 폴더(Temporary Directory)의 절대 위치입니다.(안드로이드는 캐시 폴더가 전달됩니다.)
- LibraryDirectoryPath: iOS의 NSLibraryDirectory
- ExternalDirectoryPath:
- ExternalStorageDirectoryPath:
- PicturesDirectoryPath:
- FileProtectionKeys:

### 폴더 읽기
아래는 RN(React Native)에서 ```react-native-fs```를 사용하여 폴더를 읽는 방법에 대한 코드입니다.



## 완료
위에서 구현한 ```react-native-mail``` 기능을 실행하면 아래와 같은 화면을 볼수 있습니다.(사진 출처: [공식 사이트](https://github.com/chirag04/react-native-mail){:rel="nofollow noreferrer" target="_blank"})

![react-native-mail 스크린샷](/assets/images/category/react-native/react-native-mail/screenshot.png)

## 참고
- react-native-mail 공식 사이트: [https://github.com/chirag04/react-native-mail](https://github.com/chirag04/react-native-mail){:rel="nofollow noreferrer" target="_blank"}