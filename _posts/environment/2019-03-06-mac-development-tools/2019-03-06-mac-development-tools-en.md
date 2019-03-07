---
layout: 'post'
permalink: '/environment/mac-development-tools/'
paginate_path: '/environment/:num/mac-development-tools/'
lang: 'en'
categories: 'environment'
comments: true

title: 'Development Environment on Mac(2) - for tools'
description: now I'm configuring the development environment on new Mac. in here, I'll introduce the tools that I use when I develop.
image: '/assets/images/category/environment/mac-development-tools/background.jpg'
---

## Outline
now I'm setting the development environment on new Mac. in this blog, I'll show the tools what I use.

this blog is a series. if you want to know other development environment, see other blog posts.

- [Development Environment on Mac(1) - iTerm & zsh]({{site.url}}/{{page.categories}}/mac-iterm-zsh/){:target="_blank"}
- [Development Environment on Mac(2) - for tools]({{site.url}}/{{page.categories}}/mac-development-tools/){:target="_blank"}
- [Development Environment on Mac(3) - for development]({{site.url}}/{{page.categories}}/mac-development-environment/){:target="_blank"}


## Communication Tools
the below is what I use for communication when I develop.

- Line: Download from App store
- Kakaotalk: Download from App store
- Slack: Download from App store


## Development Tools
the below is the development tools what I use.

- android studio: [https://developer.android.com/studio](https://developer.android.com/studio){:rel="nofollow noreferrer" target="_blank"}
- xcode: Download from App store
- vscode: [https://code.visualstudio.com/download](https://code.visualstudio.com/download){:rel="nofollow noreferrer" target="_blank"}


### vscode
this is vscode plugin list what I use.

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

after installing all, execute the command below to open vscode configuration file.

```bash
code ~/Library/Application\ Support/Code/User/settings.json
```

copy-paste the below to vscode setting file.

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


## DB Tools
the below is the DB tools what I use.

- sequel pro: [https://www.sequelpro.com/](https://www.sequelpro.com/){:rel="nofollow noreferrer" target="_blank"}
- DB Browser For SQLite: [https://sqlitebrowser.org/](https://sqlitebrowser.org/){:rel="nofollow noreferrer" target="_blank"}
- workbench: [https://www.mysql.com/products/workbench/](https://www.mysql.com/products/workbench/){:rel="nofollow noreferrer" target="_blank"}

## Support Program
this is the support programs for developing.

- Postman: [https://www.getpostman.com/downloads/](https://www.getpostman.com/downloads/){:rel="nofollow noreferrer" target="_blank"}
- Beyond Compare: [https://www.scootersoftware.com/download.php](https://www.scootersoftware.com/download.php){:rel="nofollow noreferrer" target="_blank"}
- Sourcetree: [https://www.sourcetreeapp.com/](https://www.sourcetreeapp.com/){:rel="nofollow noreferrer" target="_blank"}


## Font
this is the font for the development tools.

- D2Coding: [https://github.com/naver/d2codingfont](https://github.com/naver/d2codingfont){:rel="nofollow noreferrer" target="_blank"}


