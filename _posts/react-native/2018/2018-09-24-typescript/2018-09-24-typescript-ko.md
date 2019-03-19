---
layout: 'post'
permalink: '/react-native/typescript/'
paginate_path: '/react-native/:num/typescript/'
lang: 'ko'
categories: 'react-native'
comments: true

title: 'typescript'
description: 'react-native 프로젝트에 typescript를 적용하여 개발해 보자.'
image: '/assets/images/category/react-native/typescript.jpg'
---


## react-native 프로젝트 생성
아래에 명령어를 이용하여 RN 프로젝트를 생성합니다.

{% include react-native/create_new_project.md %}

## typescript에 필요한 라이브러리 설치
typescript가 동작할 수 있도록 필요한 라이브러리을 설치합니다.

{% include_relative common/install_modules.md %}

### typescript 라이브러리
- typescript: typescript를 설치한다.
- @types/react: typescript에 필요한 react의 type을 설치한다.
- @types/react-native: typescript에 필요한 react-native의 type을 설치한다.

## typescript 설정
typescript를 설정하여 react-native가 동작하도록 만듭니다.

### tsconfig.json 만들기
프로젝트 root 폴더에 ```tsconfig.json```파일을 생성하고 아래에 내용을 복사합니다.

{% include_relative common/tsconfig_json.md %}

자세한 내용은 공식 홈페이지를 참조하세요.
- [typescript - tsconfig.json](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html){:rel="nofollow noreferrer" target="_blank"}
- [typescript - compile options](https://www.typescriptlang.org/docs/handbook/compiler-options.html){:rel="nofollow noreferrer" target="_blank"}

### tslint.json 만들기
typescript 개발을 편리하게 하기 위해 tslint를 적용합니다. 아래에 내용을 프로젝트 root폴더에 ```tslint.json```을 생성하고 복사합니다.

{% include_relative common/tslint_json.md %}

자세한 내용은 공식 홈페이지를 참조하세요.
- [typescript - tslint](https://github.com/Microsoft/TypeScript-React-Starter#overriding-defaults){:rel="nofollow noreferrer" target="_blank"}
- [tslint - configuration](https://palantir.github.io/tslint/usage/configuration/){:rel="nofollow noreferrer" target="_blank"}

### rn-cli.config.js 만들기
[Bruno Lemos](https://www.facebook.com/brunolemos?fref=gc&dti=586400221495560){:rel="nofollow noreferrer" target="_blank"}님께서 ```No need for rn-cli.config.js anymore since v0.57```라고 페이스북(facebook)에 댓글을 주셔서 확인해 본 결과 RN(react native) 버전 0.57 이상에서는 ```rn-cli.config.js```가 필요 없는게 되었네요. 모두 참고 하시기 바랍니다.

~~typescript를 런타임중에 인식할 수 있게 도와주는 라이브러리을 위한 설정 파일입니다. 프로젝트 root폴더에 ```rn-cli.config.js``` 파일에 아래에 내용을 작성합니다.~~

{% include_relative common/rn_cli_config.md %}

## typescript로 코딩하기
App.js를 App.tsx로 파일명을 수정하고 typescript 형식으로 코딩합니다.

{% include_relative common/typescript_code.md %}