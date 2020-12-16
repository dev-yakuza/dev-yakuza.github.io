---
layout: 'post'
permalink: '/react-native/make-opensource-library/'
paginate_path: '/react-native/:num/make-opensource-library/'
lang: 'ko'
categories: 'react-native'
comments: true

title: React Native용 오픈소스 만들기
description: React Native용 오픈 소스를 제작하는 방법에 대해서 공유합니다.
image: '/assets/images/category/react-native/2020/make-opensource-library/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [NPM](#npm)
- [GitHub 저장소](#github-저장소)
- [package.json](#packagejson)
- [개발 환경 구성](#개발-환경-구성)
- [라이브러리 개발하기](#라이브러리-개발하기)
- [배포하기](#배포하기)
- [완료](#완료)

</div>

## 개요

React Native로 개발을 해보면서, 언제나 남들이 만들어 놓은 오픈 소스를 가져다 사용하였습니다. 마음 한 구석에 나도 오픈소스 만들어봐야지 하는 마음이 있었으나, 시간이 없다는 핑계로 잘 실천하지 못했습니다.

하지만 시간이 생겨 정작 만들어 보려고 하니, 어디서부터 어떻게 만들어야할지 막막했습니다. 여러분도 저처럼 오픈소스를 만들어보고 싶지만, 어떻게 시작해야할지 막막한 분들을 위해, 오픈 소스를 어떻게 만드는지에 대해서 공유합니다.

아래 링크는 제가 만든 오픈 소스입니다.

- NPM: [react-native-image-modal](https://www.npmjs.com/package/react-native-image-modal){:rel="nofollow noreferrer" target="_blank"}

## NPM

이번 블로그에서 소개할 오픈 소스 제작 방법은 React Native의 Javascript 부분만을 다루고 있습니다. 네이티브 모듈을 제작하는 방법은 포함되어 있지 않음을 알려드립니다.

앞으로 제작할 Javascript 오픈 소스를 사용하기 위해서는, NPM(Node Package Manager)에 배포할 필요가 있습니다.

- NPM: [react-native-image-modal](https://www.npmjs.com/package/react-native-image-modal){:rel="nofollow noreferrer" target="_blank"}

오픈 소스 제작에 앞서 아래에 블로그 포스트를 확인하여, 자신이 개발할 오픈소스를 NPM에 배포 가능한 상태로 준비하시기를 권장합니다.

- [NPM에 자신의 라이브러리 배포하기]({{site.url}}/share/deploy-npm-library/){:target="_blank"}

## GitHub 저장소

오픈소스를 공유하기 위한 최고의 방법은 GitHub죠. 지금부터 제작할 오픈소스 라이브러리의 소스코드를 공유하기 위해 GitHub 저장소(Repository)를 생성합니다.

아직 GitHub의 계정을 가지고 계시지 않는다면, 아래에 링크를 통해 무료로 회원가입하시기 바랍니다.

- GitHub:[https://github.com/](https://github.com/){:rel="nofollow noreferrer" target="_blank"}

GitHub의 저장소를 생성할 때, NPM에 이미 배포된 라이브러리와 중복되지 않는 이름으로 생성하도록 합니다. NPM에서 중복 여부를 확인하는 방법에 대해서는 아래에 블로그 포스트를 참고하시기 바랍니다.

- NPM에 자신의 라이브러리 배포하기: [npm info]({{site.url}}/share/deploy-npm-library/#npm-info){:target="_blank"}

GitHub 저장소를 만들었다면, 자신의 로컬 PC에 Clone합니다.

```bash
git clone [Your repository URL]
```

{% include in-feed-ads.html %}

## package.json

Javascript 오픈 소스를 개발하고 배포하기 위해서는 `package.json` 파일이 필요합니다. 아래에 명령어를 사용하여 package.json 파일을 생성합니다.

```bash
# cd [Your Project folder]
npm init
```

package.json 파일 생성에 대한 자세한 설명은 아래에 링크를 참고하시기 바랍니다.

- NPM에 자신의 라이브러리 배포하기: [npm init]({{site.url}}/share/deploy-npm-library/#npm-init){:target="_blank"}

## 개발 환경 구성

저는 `Typescript`로 React Native의 라이브러리를 개발하려고 합니다. 지금부터 Typescript와 React Native를 개발할 환경을 구축해 봅시다.

우선 아래에 명령어를 사용하여 React Native 프로젝트를 생성합니다.

```bash
react-native init Develop
```

이 프로젝트는 React Native 라이브러리를 개발할 때 사용할 예정입니다. 다음으로 `tsconfig.json` 파일을 생성하고 아래와 같이 수정합니다.

```json
{
  "compilerOptions": {
    "module": "esnext",
    "target": "es5",
    "lib": ["es6", "dom", "es2016", "es2017"],
    "sourceMap": true,
    "allowJs": false,
    "jsx": "react-native",
    "declaration": true,
    "declarationMap": true,
    "moduleResolution": "node",
    "forceConsistentCasingInFileNames": true,
    "noImplicitReturns": true,
    "noImplicitThis": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    "suppressImplicitAnyIndexErrors": true,
    "noUnusedLocals": true,
    "outDir": "dist",
    "skipLibCheck": true,
    "allowSyntheticDefaultImports": true,
    "removeComments": true
  },
  "include": ["src"],
  "exclude": ["node_modules", "Develop", "DevelopWithExpo", "Example", "ExampleWithExpo", "dist"]
}
```

옵션에 대한 자세한 설명은 생략하도록 하겠습니다. 다만, `"include": ["src"],`를 통해 `src` 폴더에 있는 파일들을 빌드할 예정이며 `"outDir": "dist",` 옵션을 통해 빌드한 결과물은 `dist` 폴더에 저장할 예정입니다.

다음으로 `package.json` 파일을 열고 아래와 같이 수정합니다.

```json
{
  ...
  "main": "dist/index.js",
  "types": "dist/index.d.ts",
  "scripts": {
    "lint": "eslint --ext .tsx --ext .ts src/",
    "format": "prettier --check ./src",
    "start": "rm -rf Develop/dist && tsc -w --outDir Develop/dist",
    "start:expo": "rm -rf DevelopWithExpo/dist && tsc -w --outDir DevelopWithExpo/dist",
    "prepare": "rm -rf dist && tsc"
  },
  "lint-staged": {
    "src/**/*.{ts,tsx}": [
      "eslint --ext .tsx --ext .ts src/ --fix"
    ],
    "./src/**": [
      "prettier --write ."
    ]
  },
  "husky": {
    "hooks": {
      "pre-commit": "lint-staged"
    }
  },
  ...
  "peerDependencies": {
    "react": "*",
    "react-native": "*"
  },
  "devDependencies": {
    "@types/react": "*",
    "@types/react-native": "*",
    "@typescript-eslint/eslint-plugin": "2.25.0",
    "@typescript-eslint/parser": "2.25.0",
    "eslint": "6.8.0",
    "eslint-plugin-prettier": "3.1.2",
    "eslint-plugin-react": "7.19.0",
    "eslint-plugin-react-hooks": "2.5.1",
    "husky": "4.2.3",
    "lint-staged": "10.0.9",
    "prettier": "2.0.2",
    "react": "*",
    "react-native": "*",
    "typescript": "^3.7.5"
  },
}
```

하나하나 자세히 살펴보도록 하겠습니다.

```json
"main": "dist/index.js",
"types": "dist/index.d.ts",
```

NPM에게 라이브러리의 메인 파일이 뭔지, 타입 파일이 무엇인지 알려주었습니다.

```json
"scripts": {
  "lint": "eslint --ext .tsx --ext .ts src/",
  "format": "prettier --check ./src",
  "start": "rm -rf Develop/dist && tsc -w --outDir Develop/dist",
  "start:expo": "rm -rf DevelopWithExpo/dist && tsc -w --outDir DevelopWithExpo/dist",
  "prepare": "rm -rf dist && tsc"
},
```

라이브러리를 개발하면서 사용할 명령어들입니다.

`lint`와 `format`는 `eslint`와 `prettier`을 통해 개발중인 소스코드의 Formatting을 검사하는 명령어 입니다.
또한 아래에 `lint-staged`와 `husky` 설정을 통해 `git commit`시 Formatting을 실행하도록 하였습니다.

```json
"lint-staged": {
  "src/**/*.{ts,tsx}": [
    "eslint --ext .tsx --ext .ts src/ --fix"
  ],
  "./src/**": [
    "prettier --write ."
  ]
},
"husky": {
  "hooks": {
    "pre-commit": "lint-staged"
  }
},
```

자세한 내용은 아래에 블로그 포스트를 참고하시기 바랍니다.

- [React Native에서 ESLint, Prettier를 프로처럼 사용하기]({{site.url}}/{{page.categories}}/eslint-prettier-husky-lint-staged/){:target="_blank"}

라이브러리를 개발할 때, `npm start` 명령어를 통해 Typescript를 빌드하면서 개발할 예정입니다. 또한 `npm publish`로 개발한 라이브러리를 배포하게 되는데, `prepare` 명령어를 선언하여 배포전에 Typescript를 자동으로 빌드하도록 설정하였습니다.

자세한 내용은 아래에 블로그를 참고하시기 바랍니다.

- NPM에 자신의 라이브러리 배포하기: [npm publish]({{site.url}}/share/deploy-npm-library/#npm-publish){:target="_blank"}

개발에 필요한 라이브러리들을 `devDepenencies`에 선언하였습니다. 이제 아래에 명령어를 통해 필요한 라이브러리들을 설치합니다.

```bash
npm install
```

설치가 완료되면 `.gitignore` 파일과 `.prettierignore` 파일을 생성하고 `node_modules`를 추가합니다.

이제 개발할 준비가 끝났습니다. 다음으로, 어떤식으로 라이브러리를 개발하게 되는지 살펴봅시다.

{% include in-feed-ads.html %}

## 라이브러리 개발하기

위에서 설정한 개발 환경을 보면, 우리는 `src` 폴더에 개발할 소스코드를 추가해야합니다. `src` 폴더에 `index.tsx` 파일을 생성하고, 아래와 같이 수정합니다.

```js
import React from 'react';
import { View, Text } from 'react-native';

const LibraryName = (): JSX.Element => {
  return (
    <View>
      <Text>Hello World!</Text>
    </View>
  );
};

export default LibraryName;
```

그리고 `Develop` 폴더의 `App.js` 파일을 열고 아래와 같이 수정합니다.

```js
import React from 'react';
import {StyleSheet,   SafeAreaView} from 'react-native';

import LibraryName from './dist';

const App = () => {
  return (
    <SafeAreaView style={styles.container}>
      <LibraryName />
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

export default App;
```

그리고 아래에 명령어를 사용하여 개발한 Typescript를 빌드합니다.

```bash
npm start
```

위에서 만든 `package.json`의 `start` 명령어를 보면 다음과 같습니다.

```bash
"start": "rm -rf Develop/dist && tsc -w --outDir Develop/dist",
```

명령어를 자세히 보면, `Develop/dist` 폴더를 삭제한 후, `tsc`를 사용하여 빌드한 후, 결과물을 `Develop/dist` 폴더에 저장하도록 하였습니다. 또한 `-w` 옵션을 사용하여, 소스코드가 변경이 되면, 다시 빌드하도록 설정하였습니다. 따라서 위에 명령어를 사용한 후, 개발을 진행하면 됩니다.

그리고 다른 `Terminal` 또는 `CMD`를 열고 아래에 명령어를 실행합니다.

```bash
cd Develop
npm run ios
# npm run android
```

그러면 우리가 개발하고 있는 라이브러리가 아래와 같이 잘 표시되는 것을 확인할 수 있습니다.

![React Native용 오픈소스 만들기 - Hello world](/assets/images/category/react-native/2020/make-opensource-library/hello-world.jpg)

다시, `src/index.tsx` 파일을 열고 파일 내용을 수정하면 시뮬레이터 내용이 잘 갱신되는 것을 확인할 수 있습니다.

## 배포하기

이렇게 개발된 라이브러리를 배포하기 위해서는 아래에 명령어들을 사용해야 합니다.

```bash
npm login
npm publish
```

명령어에 대한 자세한 내용은 아래에 블로그를 참고하시기 바랍니다.

- [NPM에 자신의 라이브러리 배포하기]({{site.url}}/share/deploy-npm-library/){:target="_blank"}

## 완료

React Native의 라이브러리를 개발하는 방법에 대해서 간략히 살펴보았습니다. `NPM`에 배포를 해야하기 때문에, NPM에 관한 블로그와 같이 보셔야 좀 더 이해하기 쉬울거 같네요.

여러분도 시간이 생기시면, 멋진 오픈소스를 개발하여, 개발자 문화에 동참해 보시는건 어떨까요?
