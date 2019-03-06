---
published: false
layout: 'post'
permalink: '/environment/mac-development-tools/'
paginate_path: '/environment/:num/mac-development-tools/'
lang: 'ko'
categories: 'environment'
comments: true

title: '맥(Mac) 개발 환경 구축(2) - tools'
description: '새로운 맥(Mac)에 개발 환경을 구축하려고 합니다. 맥(Mac)에서 사용하고 있는 툴들을 정리하였습니다.'
image: '/assets/images/category/environment/mac-development-tools/background.jpg'
---

## 개요
맥(Mac)에 새롭게 개발 환경을 구축하고 있습니다. 이 블로그에서는 개발과 커뮤니케이션에 사용하고 있는 툴들을 정리합니다.

이 블로그는 연재물입니다. 이전 zsh 설치에 관해서는 이전 블로그를 확인해 주세요.

- [맥(Mac) 개발 환경 구축(1) - iTerm과 zsh]({{site.url}}/{{page.categories}}/mac-iterm-zsh/){:target="_blank"}


## 커뮤니케이션 툴
아래는 개발할 때 사용하는 커뮤니케이션 툴을 나열하였습니다.

- Line: App store에서 다운로드
- Kakaotalk: App store에서 다운로드
- Slack: App store에서 다운로드


## 개발툴
아래는 실제 개발에 사용하는 툴을 나열하였습니다.

- android studio: [https://developer.android.com/studio](https://developer.android.com/studio){:rel="nofollow noreferrer" target="_blank"}
- xcode: App store에서 다운로드
- vscode: [https://code.visualstudio.com/download](https://code.visualstudio.com/download){:rel="nofollow noreferrer" target="_blank"}


### vscode
아래는 vscode에서 사용하는 플로그인 리스트 입니다.

- Active File In StatusBar
- Babel ES6/ES7
- Bracket Pair Colorizer
- Debugger for Chrome
- IntelliSense for CSS, SCSS class names in HTML, Slim and SCSS
- Node.js Modlues Intellisense
- npm Intellisense
- Path Intellisense
- PHP Intellisense
- Prettier - Code Formatter
- Python
- Trailing Spaces
- TSLint
- vscode-icons

위에 리스트를 모두 설치한 후, 아래의 명령어로 vscode 설정 파일을 엽니다.

```bash
code ~/Library/Application\ Support/Code/User/settings.json
```

vscode의 설정 파일 내용에 아래의 내용을 복사 붙여넣습니다.

```json
{
  "terminal.integrated.shell.osx": "/bin/zsh",
  "terminal.integrated.fontFamily": "Meslo LG M for Powerline",
  "window.zoomLevel": 2,
  "workbench.iconTheme": "vscode-icons",
  "editor.fontFamily": "'D2Coding ligature'",
  "editor.fontLigatures": true,
  "window.restoreWindows": "all",
  "prettier.eslintIntegration": true,
  "javascript.format.enable": false,
  "editor.formatOnSave": true,
  "files.exclude": {
    "**/.git": true,
    "**/.svn": true,
    "**/.DS_Store": true,
    "*/node_modules": true,
    "**/.idea": true,
    "**/.vscode": false,
    "**/yarn.lock": true,
    "**/tmp": true,
    "node_modules": true
  },
  "files.watcherExclude": {
    "**/.git/objects/**": true,
    "**/node_modules/**": true,
    "**/tmp": true,
    "**/build": true
  },
  "files.trimTrailingWhitespace": true,
  "search.exclude": {
    "**/node_modules": true,
    "**/bower_components": true,
    "**/.git": true,
    "**/.DS_Store": true,
    "**/tmp": true,
    "**/coverage": true,
    "**/build": true,
    "**/Pods": true,
    "**/*.xcodeproj": true,
    "**/*.xcworkspace": true,
    "**/.meteor": true
  },
  "extensions.autoUpdate": true,
  "prettier.singleQuote": true,
  "prettier.trailingComma": "es5",
  "prettier.jsxBracketSameLine": true,
  "[markdown]": {
    "editor.formatOnSave": false
  }
}
```


## DB 툴
아래는 실제 개발에 사용하는 DB 툴을 나열하였습니다.

- sequel pro: [https://www.sequelpro.com/](https://www.sequelpro.com/){:rel="nofollow noreferrer" target="_blank"}
- DB Browser For SQLite: [https://sqlitebrowser.org/](https://sqlitebrowser.org/){:rel="nofollow noreferrer" target="_blank"}


## 보조 프로그램
아래는 실제 개발시 사용하는 보조 프로그램을 나열하였습니다.

- Postman: [https://www.getpostman.com/downloads/](https://www.getpostman.com/downloads/){:rel="nofollow noreferrer" target="_blank"}
- Beyond Compare: [https://www.scootersoftware.com/download.php](https://www.scootersoftware.com/download.php){:rel="nofollow noreferrer" target="_blank"}
- Sourcetree: [https://www.sourcetreeapp.com/](https://www.sourcetreeapp.com/){:rel="nofollow noreferrer" target="_blank"}


## 폰트
아래는 개발툴에 사용하는 폰트입니다.

- D2Coding: [https://github.com/naver/d2codingfont](https://github.com/naver/d2codingfont){:rel="nofollow noreferrer" target="_blank"}


