---
layout: 'post'
permalink: '/environment/mac-development-tools/'
paginate_path: '/environment/:num/mac-development-tools/'
lang: 'ja'
categories: 'environment'
comments: true

title: 'マック(Mac)の開発環境の構築(2) - tools'
description: '新しマック(Mac)に開発環境を構築してみようかと思います。私がマック(Mac)で使ってる開発ツールを纏めてみました。'
image: '/assets/images/category/environment/mac-development-tools/background.jpg'
---

## 概要
マック(Mac)で新しく開発環境を構築しています。このブログでは開発やコミュニケーションで使ってるツールを纏めてみました。

このブログはシリーズです。開発環境の別のところが木になる方は下記の内容を参考してください。

- [マック(Mac)の開発環境の構築(1) - iTermとzsh]({{site.url}}/{{page.categories}}/mac-iterm-zsh/){:target="_blank"}
- [マック(Mac)の開発環境の構築(2) - tools]({{site.url}}/{{page.categories}}/mac-development-tools/){:target="_blank"}
- [マック(Mac)の開発環境の構築(3) - 開発環境]({{site.url}}/{{page.categories}}/mac-development-environment/){:target="_blank"}


## コミュニケーションツール
下記のツールは開発する時使ってるコミュニケーションツールです。

- Line: App storeからダウンロード
- Kakaotalk: App storeからダウンロード
- Slack: App storeからダウンロード


## 開発ツール
下記は実際開発する時使ってるツールです。

- android studio: [https://developer.android.com/studio](https://developer.android.com/studio){:rel="nofollow noreferrer" target="_blank"}
- xcode: App storeからダウンロード
- vscode: [https://code.visualstudio.com/download](https://code.visualstudio.com/download){:rel="nofollow noreferrer" target="_blank"}


### vscode
下記はvscodeで使ってるプラグインのリストです。

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

上にあるリストを全てインストールした後、下記のコマンドでvscodeの設定ファイルを開きます。

```bash
code ~/Library/Application\ Support/Code/User/settings.json
```

vscodeの設定ファイルに下記の内容をコピペします。

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


## DBツール
下は実際開発に使ってるDBツールです。

- sequel pro: [https://www.sequelpro.com/](https://www.sequelpro.com/){:rel="nofollow noreferrer" target="_blank"}
- DB Browser For SQLite: [https://sqlitebrowser.org/](https://sqlitebrowser.org/){:rel="nofollow noreferrer" target="_blank"}
- workbench: [https://www.mysql.com/products/workbench/](https://www.mysql.com/products/workbench/){:rel="nofollow noreferrer" target="_blank"}

## 補助プログラム
下記は開発する時使ってる補助プログラムです。

- Postman: [https://www.getpostman.com/downloads/](https://www.getpostman.com/downloads/){:rel="nofollow noreferrer" target="_blank"}
- Beyond Compare: [https://www.scootersoftware.com/download.php](https://www.scootersoftware.com/download.php){:rel="nofollow noreferrer" target="_blank"}
- Sourcetree: [https://www.sourcetreeapp.com/](https://www.sourcetreeapp.com/){:rel="nofollow noreferrer" target="_blank"}


## フォント
下記のフォントは開発ツールで使ってるフォントです。

- D2Coding: [https://github.com/naver/d2codingfont](https://github.com/naver/d2codingfont){:rel="nofollow noreferrer" target="_blank"}


