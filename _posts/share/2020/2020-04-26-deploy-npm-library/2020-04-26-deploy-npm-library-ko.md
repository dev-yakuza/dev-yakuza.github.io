---
layout: 'post'
permalink: '/share/deploy-npm-library/'
paginate_path: '/share/:num/deploy-npm-library/'
lang: 'ko'
categories: 'share'
comments: true

title: NPM에 자신의 라이브러리 배포하기
description: 자신이 개발한 Javascript 라이브러리를 NPM에 배포하는 방법에 대해서 알아봅니다.
image: '/assets/images/category/share/2020/deploy-npm-library/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [NPM 계정 만들기](#npm-계정-만들기)
- [npm info](#npm-info)
- [npm init](#npm-init)
- [npm login](#npm-login)
- [npmignore](#npmignore)
- [npm publish](#npm-publish)
- [npm version](#npm-version)
- [완료](#완료)

</div>

## 개요

지금까지 React Native로 개발하면서, 남들이 만들어 놓은 오픈 소스를 많이 사용하였습니다. 언제나 이렇게 오픈 소스만 사용하다가, 나도 한번 오픈 소스를 제작해봐야지 마음 먹고 `react-native-image-modal`이라는 간단한 오픈 소스를 제작해 보았습니다.

- NPM: [react-native-image-modal](https://www.npmjs.com/package/react-native-image-modal){:rel="nofollow noreferrer" target="_blank"}

React Native의 오픈 소스 라이브러리를 제작하는 방법에 대해서 궁금하신 분들은 아래에 블로그를 참고하시기 바랍니다.

- [React Native용 오픈소스 만들기]({{site.url}}/react-native/make-opensource-library/){:target="_blank"}

이번 블로그 포스트에서는 자신이 제작한 Javascript 라이브러리를 NPM(Node Package Manager)에 배포하는 방법에 대해서 알아봅니다.

## NPM 계정 만들기

NPM에 자신이 만든 Javascript 라이브러리를 배포하기 위해서는 NPM 서비스의 계정이 필요합니다.

NPM의 계정이 존재하지 않는 분들은, 아래에 링크를 클릭하여 NPM 서비스로 이동한 후, NPM 계정을 생성합니다.

- NPM 서비스 사이트: [https://www.npmjs.com/](https://www.npmjs.com/){:rel="nofollow noreferrer" target="_blank"}

## npm info

자신이 개발한 Javscript 라이브러리를 배포하기전에, 배포가 가능한 패키지명인지 확인할 필요가 있습니다. 당연하지만, 현재 NPM에 배포된 라이브러리와 동일한 이름을 사용할 수 없습니다.

아래에 명령어를 사용하여 자신의 Javascript 라이브러리명이 사용 가능한지 확인해 봅니다.

```bash
npm info [Javascript Package Name]
```

만약, 중복된 이름이라면 아래와 같이, 이미 NPM에 배포된 라이브러리에 대한 정보를 확인할 수 있습니다.

```bash
npmdeploy@1.0.1 | MIT | deps: 1 | versions: 1
deploy projects easily in the cloud. Optimised for GitLab CI
https://gitlab.com/pushrocks/npmdeploy#README

keywords: deploying, made, easy

dist
.tarball: https://registry.npmjs.org/npmdeploy/-/npmdeploy-1.0.1.tgz
.shasum: c298d768aac7ccb89a38c20a0c904341fc87c484

dependencies:
gitlab: ^1.6.0

maintainers:
- lossless <npm@lossless.digital>

dist-tags:
latest: 1.0.1

published over a year ago by lossless <npm@lossless.digital>
```

만약 중복된 이름이 아니라면 아래와 같이 `404` 에러를 확인할 수 있습니다.

```bash
npm ERR! code E404
npm ERR! 404 'temp-npmdeploy' is not in the npm registry.
npm ERR! 404 You should bug the author to publish it
npm ERR! 404 (or use the name yourself!)
npm ERR! 404
npm ERR! 404 Note that you can also install from a
npm ERR! 404 tarball, folder, http url, or git url.
npm ERR! 404
npm ERR! 404  'temp-npmdeploy@latest' is not in the npm registry.
npm ERR! 404 You should bug the author to publish it (or use the name yourself!)
npm ERR! 404
npm ERR! 404 Note that you can also install from a
npm ERR! 404 tarball, folder, http url, or git url.
```

{% include in-feed-ads.html %}

## npm init

자신이 개발한 Javascript 라이브러리를 NPM에 배포하기 위해서 NPM에 필요한 정보를 설정할 필요가 있습니다.

자신이 개발한 Javascript 라이브러리 폴더로 이동한 후, 아래에 명령어를 실행합니다.

```bash
# cd ProjectName
npm init
```

위의 명령어를 실행하면, 다음과 같은 화면을 볼 수 있습니다. 아래에 설명하는 내용은 추후에도 변경할 수 있으니, 부담없이 진행하시기 바랍니다.

```bash
This utility will walk you through creating a package.json file.
It only covers the most common items, and tries to guess sensible defaults.

See `npm help json` for definitive documentation on these fields
and exactly what they do.

Use `npm install <pkg>` afterwards to install a package and
save it as a dependency in the package.json file.

Press ^C at any time to quit.
package name: (npmdeploy)
```

폴더명을 기준으로 `package name`을 결정할지, 다른 이름으로 설정할지 물어봅니다. 우리는 위에서 `npm info`로 배포 가능한 이름을 찾았습니다. 해당 이름을 입력합니다.

```bash
version: (1.0.0)
```

그 다음, 버전을 물어봅니다. 버전은 기본적으로 `major.minor.patch`를 사용합니다. 이미 개발이 완료되었고, 배포만을 남겨둔 상황이라면 `1.0.0`을 그대로 사용하면 됩니다. 아직 개발중이고, 완벽하지 않다면 `0.0.1`을 지정하여 안정적인 버전이 아님을 명시합니다.

```bash
description:
```

Javascript 라이브러리에 대한 설명을 작성하는 부분입니다. 자신의 라이브러리에 대한 설명을 작성합니다.

```bash
entry point: (index.js)
```

개발한 Javascript 라이브러리의 Entry 파일(메인 파일)을 지정합니다.

```bash
test command:
```

자신이 개발한 Javascript 라이브러리를 테스트할 수 있는 테스트 명령어를 입력합니다. 테스트를 실행할 명령어가 없다면, Enter 키를 눌러 진행합니다.

```bash
git repository:
```

배포하려는 Javascript의 소스코드를 확인할 수 있는 Git 저장소의 URL을 입력합니다. URL이 존재하지 않느다면 Enter 키를 눌러 진행합니다.

```bash
keywords:
```

배포하려는 Javascript를 쉽게 알 수 있는 키워드를 입력합니다. (ex> jQuery, react-native, reactjs 등)

```bash
author:
```

배포하는 사람에 대한 정보를 입력합니다. 보통 `Name <Email Address>` 형식을 사용합니다.

```bash
license: (ISC)
```

배포하려는 라이브러리의 라이센스에 관한 질문입니다. 자신의 라이브러리의 라이센스에 맞게 작성합니다. (ex> MIT, ISC 등)

라이센스에 키워드에 관해서는 아래의 링크를 참고하시기 바랍니다.

- [GitHub license type](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/licensing-a-repository#searching-github-by-license-type)

이렇게 모든 항목을 입력하면 자신의 프로젝트 폴더안에 `package.json` 파일이 생성된 것을 확인할 수 있습니다.

{% include in-feed-ads.html %}

## npm login

NPM에 자신의 라이브러리를 배포하기 위해서는, 아래에 명령어를 사용하여 NPM 서비스에 로그인 할 필요가 있습니다.

```bash
npm login
```

위에 명령어를 실행하면 아래와 같이 로그인을 하기위한 절차가 실행됩니다.

```bash
Username: dev-yakuza
Password:
Email: (this IS public) dev.yakuza@gmail.com
Logged in as dev-yakuza on https://registry.npmjs.org/.
```

위에서 생성한 NPM 계정의 정보를 입력하여 로그인합니다. 로그인을 하였다면 아래에 명령어를 실행하여 제대로 로그인되었는지 확인합니다.

```bash
npm whoami
# dev-yakuza
```

## npmignore

실제 개발에는 필요하나, 개발이 완료된 라이브러리를 사용할 때는 필요없는 파일들이 있습니다. 예를 들어 테스트 코드, 예제 소스들이 이에 해당할 수 있습니다. 이렇게 개발에는 필요하나, 배포에는 불필요한 파일들을 `.npmignore` 파일을 통해 제외 시킬 수 있습니다.

아래에 내용은 제가 개발한 `react-native-image-modal`에 대한 `.npmignore` 파일입니다.

```bas
node_modules
Develop
DevelopWithExpo
Example
ExampleWithExpo
.github
demo
```

## npm publish

이제 NPM에 자신의 라이브러리를 배포할 준비가 되었습니다. 아래에 명령어를 통해 자신의 라이브러리를 NPM에 배포해 봅시다.

```bash
npm publish
```

라이브러리를 배포하기 전에 특정 명령어를 실행할 필요가 있다면 `package.json`을 아래와 같이 수정합니다.

```json
"scripts": {
  ...
  "prepare": "rm -rf dist && tsc"
},
```

저는 Typescript로 라이브러리를 개발했기 때문에, 배포전에 Typescript를 빌드할 필요가 있었습니다. 이렇게 `package.json`의 `scripts`에 `prepare` 명령어를 선언하면, `npm publish` 명령어를 실행할 때, 해당 명령어를 실행하게 됩니다.

이것으로 여러분이 개발한 라이브러리를 NPM에 배포하였습니다. 배포된 라이브러리를 사용하기 위해서는 여러분이 NPM 라이브러리를 사용하는 것과 동일하게 사용이 가능합니다.

```bash
npm install --save [Your Package Name]
```

{% include in-feed-ads.html %}

## npm version

NPM에 배포한 라이브러리를 수정하고 다시 배포해야할 일이 발생할 수 있습니다. 이렇게 재배포를 할 경우, 버전을 올려줄 필요가 있습니다.

버전을 올리기 위해서는 `package.json` 파일의 버전(`"version": "0.0.1"`)을 직접 수정하고 배포해도 되지만 아래에 명령어를 통해 버전을 업데이트할 수 있습니다.

```bash
npm version patch
npm version minor
npm version major
```

위에 명령어를 필요한 상황에 맞게 사용하시면, 쉽게 버전을 올릴 수 있습니다.

## 완료

이것으로 자신이 개발한 Javascript 라이브러리를 NPM에 배포하는 방법에 대해서 알아보았습니다. 처음으로 오픈소스를 제작하고 NPM에 배포하다보니 나도 뭔가 개발자 문화에 동참하는 기분이 들었습니다.

![NPM react-native-image-modal](/assets/images/category/share/2020/deploy-npm-library/npm-react-native-image-modal.jpg)

여러분도 여러분만의 오픈소스를 제작하고 배포하여, 아름다운 개발자 문화에 동참해 보시는건 어떨까요?
