---
layout: 'post'
permalink: '/react-native/root-import/'
paginate_path: '/react-native/:num/root-import/'
lang: 'ko'
categories: 'react-native'
comments: true

title: 'RN(React Native)에서 root import하기'
description: 'RN(React Native) 프로젝트에서 import를 할때, root 폴더 기준으로 import할 수 있도록 프로젝트를 설정해 봅시다.'
image: '/assets/images/category/react-native/2019/root-import/background.jpg'
---

## 개요
이번 블로그는 RN(React Native)만의 문제는 아니고, React로 개발을 하다보면 격는 문제를 해결해 보려고 합니다. React로 개발할 때, 프로젝트 구조를 아무리 이쁘게 만들어도 `import`할 때, 길어지는 `../../../` 폴더 참조 문제는 해결되지 않는거 같습니다. 이 블로그에서는 길어지는 이 폴더 참조 문제를 조금이라도 해결해 보고자 작성하였습니다. RN(React Native) 사용자뿐만 아니라 Reactjs 개발자분들도 참고가 되시면 좋겠습니다.

## 폴더 구조
저는 RN(React Native)로 개발을 할 때, 아래와 같은 폴더 구조를 사용하고 있습니다.

```
|-- android/
|-- ios/
|-- src/
|   |-- @types/
|   |-- Assets/
|   |   |-- Images/
|   |-- Component/
|   |   |-- BannerContainer/
|   |   |   |-- index.tsx
|   |   |-- LoadingContainer/
|   |   |   |-- index.tsx
|   |-- Screen/
|   |   |-- Home/
|   |   |   |-- SomeContainer/
|   |   |   |   |-- index.tsx
|   |   |   |-- SomeContainer2/
|   |   |   |   |-- SomeContainerItem/
|   |   |   |   |   |-- index.tsx
|   |   |   |   |-- index.tsx
|   |   |   |-- index.tsx
|   |-- Util/
|-- index.js
```

처음에는 `Component`, `Container`, `Screen`으로 나누어 쓰다가 `Container`가 특정 `Screen`에 종속적으로 사용되지, 여러 `Screen`에서 사용되는 경우가 적었습니다. 그래서 여러 `Screen`에서 공통적으로 사용되는 부분을 `Component`로 구분하고 종속적인 Container(Component)는 Screen폴더 하위에 두고 사용하고 있습니다. 물론 `Component`하위에도 Component(Container)에 종속된 Component들이 하위에 존재할 수 있습니다.

이렇게 한 이유는 두가지 정도가 있는데 하나는 `Screen`에 종속된 `Container`를 찾기위해 `Container` 폴더까지가서 찾아보고 다시 `Component` 폴더까지 가서 찾아봐야하는 불편함이 있었습니다. 지금은 종속된 Container는 Screen폴더 하위에 있으므로 찾는 수고가 덜해졌습니다. 또 다른 하나는 복사 붙여넣기를 편하게 하기 위해서 입니다. 혼자 여러 앱을 취미로 개발하다보니 한 프로젝트에서 사용하는 Component를 복사해서 다른 프로젝트로 붙여넣는 경우가 많이 발생했습니다. `Container` 폴더를 따로 들고 있는 때는, `Screen`을 복사하게 된다면 Screen 복사하고 포함된 Container 복사하고 Component를 복사했어야 했었습니다. 지금은 Screen 하나만 복사하면 포함되어 있는 Container들이 같이 복사가 되어 좀 더 편하게 복사-붙여넣기를 할 수 있게 되었습니다. 이런 불편함을 해소하고자 위와 같은 프로젝트 구조를 가지게 되었습니다. 참고로 Reactjs는 아래와 같은 폴더 구조를 사용하고 있습니다.

```
|-- android/
|-- ios/
|-- src/
|   |-- @types/
|   |-- Assets/
|   |   |-- Images/
|   |-- Component/
|   |   |-- BannerContainer/
|   |   |   |-- index.tsx
|   |   |-- LoadingContainer/
|   |   |   |-- index.tsx
|   |-- Feature/
|   |   |-- Login/
|   |   |   |-- SomeContainer/
|   |   |   |   |-- index.tsx
|   |   |   |-- SomeContainer2/
|   |   |   |   |-- SomeContainerItem/
|   |   |   |   |   |-- index.tsx
|   |   |   |   |-- index.tsx
|   |   |   |-- index.tsx
|   |-- Util/
|-- index.js
```

위와 같이 `Screen`이라고 관리하던 폴더를 `Feature`라는 폴더명으로 관리하고 있습니다. 여러분들은 어떤 폴더 구조들을 사용하고 계신가요? 많은 분들이 참고할 수 있게 제일 하단에 있는 코멘트에 여러분에 폴더 구조를 공유해 주세요!(저도 참고하고 싶어요ㅠㅠ)

{% include in-feed-ads.html %}

## 문제점
이렇게 폴더 구조를 가지고 가다보니 `Screen`(`Feature`) 하위에 `Container`가 있고 이 Container가 다른 `Container`를 가지고 있고 최종 Container가 `Component`를 가지게 된다면 `import`를 할 때, `../../..`가 한없이 길어지는 폴더 참조 문제가 발생하게 되었습니다. 요즘은 vscode가 자동으로 잘 작성해줘서 편해지긴 했지만, 여전히 끝도 없는 `../../../`은 보기에도 불편하게 되었습니다.

또한 `Screen`에 종속되어 있던 `Container` 또는 `Component`가 공통적으로 사용되게 되어 `Component` 폴더로 이동시키거나 반대로 `Component`가 `Screen`에 종속되어 `Screen` 하위 폴더로 이동시킬 경우 `import`의 폴더 참조 위치가 변경되기 때문에 일일이 수정해주어야 하는 불편함이 있었습니다.


## 해결책
저는 이 문제를 해결하기 위해 `babel-plugin-root-import`과 `typescript`의 설정으로 root폴더부터 참조하도록 수정하였습니다. 예를 들어 `../../../Component/BannerContainer` 였던 부분이 `~/Component/BannerContainer`로 참조 가능하게 되었습니다. 아래에 설정하는 방법에 대해 설명합니다.

### babel-plugin-root-import
root 폴더부터 참조할 수 있게 하기 위해 `babel-plugin-root-import`를 아래에 명령어로 설치합니다.

```bash
npm install babel-plugin-root-import --save-dev
```

RN(React Native) 프로젝트의 `babel.config.js`를 열고 아래와 같이 수정합니다.

```js
module.exports = {
  presets: ['module:metro-react-native-babel-preset'],
  plugins: [
    'babel-plugin-styled-components',
    [
      'babel-plugin-root-import',
      {
        rootPathPrefix: '~',
        rootPathSuffix: 'src',
      },
    ],
  ],
};
```

제 폴더 구조를 보면 알수 있지만 `src` 폴더에 모든 소스를 넣고 관리하고 있습니다. 따라서 저는 `root` 폴더가 아닌 `src` 폴더를 기준으로 동작하도록 설정하였습니다.

{% include in-feed-ads.html %}

### typescript
typescript를 사용하지 않는다면 위에 설정만으로 해결됩니다. 저는 RN(React Native) 프로젝트에서 typescript를 사용하므로 typescript가 root 폴더를 인식하도록 설정해주어야 합니다. RN(React Native)에 typescript를 적용하는 방법은 아래에 블로그를 참고하시기 바랍니다.

- [typescript]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}

RN(React Native) 프로젝트의 `tsconfig.json` 파일을 열고 아래와 같이 수정합니다.

```json
{
  "compilerOptions": {
    ...
    "baseUrl": "./src", // all paths are relative to the baseUrl
    "paths": {
      "~/*": ["*"] // resolve any `~/foo/bar` to `<baseUrl>/foo/bar`
    }
  },
  ...
}
```

## 완료
이로써 RN(React Native) 프로젝트에서 `import`할 때, 길고 길던 `../../../../`와 작별을 고하게 되었습니다. 좀 더 프로젝트를 깔끔하게 관리하게 된거 같아 기분이 좋네요. 여러분도 더 늦기 전에 이 부분을 추가하시길 권장합니다!
