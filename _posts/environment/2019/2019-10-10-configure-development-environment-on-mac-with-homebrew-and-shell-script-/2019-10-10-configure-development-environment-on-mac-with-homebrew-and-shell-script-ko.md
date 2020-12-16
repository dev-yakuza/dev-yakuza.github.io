---
layout: 'post'
permalink: '/environment/configure-development-environment-on-mac-with-homebrew-and-shell-script/'
paginate_path: '/environment/:num/configure-development-environment-on-mac-with-homebrew-and-shell-script/'
lang: 'ko'
categories: 'environment'
comments: true

title: 'Homebrew와 Shell Script를 사용하여 맥(Mac) 개발 환경 구축 자동화하기'
description: 'Homebrew와 Shell Script를 사용하여 맥 개발 환경 구축을 자동화해 봅니다. 이렇게 만든 Brefile과 Shell Script로 새로운 맥에 개발 환경을 구축해 봅니다.'
image: '/assets/images/category/environment/2019/configure-development-environment-on-mac-with-homebrew-and-shell-script/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

1. [개요](#개요)
1. [개발 환경 구성](#개발-환경-구성)
1. [Brewfile](#brewfile)
    - [brew](#brew)
    - [cask](#cask)
    - [mas](#mas)
1. [Shell Script](#shell-script)
    - [Homebrew와 Brewfile 설치](#homebrew와-brewfile-설치)
    - [보안 및 개인 정보 보호](#보안-및-개인-정보-보호)
    - [폰트](#폰트)
    - [zsh](#zsh)
    - [VSCode 설정](#vscode-설정)
    - [iTerm2](#iterm2)
    - [jekyll 개발 환경](#jekyll-개발-환경)
    - [react-native 개발 환경](#react-native-개발-환경)
    - [python 개발 환경](#python-개발-환경)
    - [Xcode](#xcode)
1. [개발 환경 설정 저장(Github)](#개발-환경-설정-저장github)
1. [맥 초기화 및 최신 OS 설치](#맥-초기화-및-최신-os-설치)
1. [새로운 맥에 개발 환경 설정하기](#새로운-맥에-개발-환경-설정하기)
    - [iTerm2 수동 설정](#iterm2-수동-설정)
1. [완료](#완료)

</div>

## 개요

맥(Mac)에 새롭게 개발 환경을 구축하려고 합니다. 아래의 블로그 포스트 리스트는 이전에 새 맥에 개발 환경을 수동으로 구축하기 정리한 블로그입니다.

- [맥(Mac) 개발 환경 구축(1) - iTerm과 zsh]({{site.url}}/{{page.categories}}/mac-iterm-zsh/){:target="_blank"}
- [맥(Mac) 개발 환경 구축(2) - tools]({{site.url}}/{{page.categories}}/mac-development-tools/){:target="_blank"}
- [맥(Mac) 개발 환경 구축(3) - 개발 환경]({{site.url}}/{{page.categories}}/mac-development-environment/){:target="_blank"}

이번 블로그 포스트에서는 위에 블로그 포스트 리스트에 있는 개발 환경을 Homebrew와 Shell Script로 자동화하여 좀 더 쉽게 개발 환경을 구축할 수 있도록 해 보았습니다.

## 개발 환경 구성

지금 현재 제가 개발하기 위한 개발 환경 구성입니다.

- [git-flow](https://github.com/nvie/gitflow){:rel="nofollow noreferrer" target="_blank"}
- [mysql 5.7](https://www.mysql.com/){:rel="nofollow noreferrer" target="_blank"}
- [python3](https://www.python.org/){:rel="nofollow noreferrer" target="_blank"}
- [node](https://nodejs.org/){:rel="nofollow noreferrer" target="_blank"}
- [watchman](https://facebook.github.io/watchman/){:rel="nofollow noreferrer" target="_blank"}
- [php](https://www.php.net){:rel="nofollow noreferrer" target="_blank"}
- [zsh](https://www.zsh.org/){:rel="nofollow noreferrer" target="_blank"}
- [oh my zsh](https://ohmyz.sh/){:rel="nofollow noreferrer" target="_blank"}
- [ruby](https://www.ruby-lang.org/){:rel="nofollow noreferrer" target="_blank"}
- [ngrok](https://ngrok.com/){:rel="nofollow noreferrer" target="_blank"}
- [jdk](https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html){:rel="nofollow noreferrer" target="_blank"}
- [android studio](https://developer.android.com/studio){:rel="nofollow noreferrer" target="_blank"}
- [sequel pro](https://www.sequelpro.com/){:rel="nofollow noreferrer" target="_blank"}
- [db browser for sqlite](https://sqlitebrowser.org/){:rel="nofollow noreferrer" target="_blank"}
- [mysql workbrench](https://www.mysql.com/products/workbench/){:rel="nofollow noreferrer" target="_blank"}
- [sketchapp](https://www.sketch.com/){:rel="nofollow noreferrer" target="_blank"}
- [postman](https://www.getpostman.com/){:rel="nofollow noreferrer" target="_blank"}
- [sourcetree](https://www.sourcetreeapp.com/){:rel="nofollow noreferrer" target="_blank"}
- [chrome](https://www.google.com/chrome/){:rel="nofollow noreferrer" target="_blank"}
- [iterm2](https://www.iterm2.com/){:rel="nofollow noreferrer" target="_blank"}
- [xcode](https://developer.apple.com/xcode/){:rel="nofollow noreferrer" target="_blank"}
- [LINE](https://line.me/){:rel="nofollow noreferrer" target="_blank"}
- [KakaoTalk](https://www.kakaocorp.com/service/KakaoTalk){:rel="nofollow noreferrer" target="_blank"}
- [Slack](https://slack.com/){:rel="nofollow noreferrer" target="_blank"}
- [Trello](https://trello.com/){:rel="nofollow noreferrer" target="_blank"}
- [react native](https://facebook.github.io/react-native/){:rel="nofollow noreferrer" target="_blank"}
- [laravel](https://laravel.com/){:rel="nofollow noreferrer" target="_blank"}
- [jekyll](https://jekyllrb.com/){:rel="nofollow noreferrer" target="_blank"}

지금부터 위에 개발 환경들을 Homebrew와 Shell Script를 사용하여 자동으로 구성하도록 만들어 보겠습니다.

{% include in-feed-ads.html %}

## Brewfile

Homebrew를 사용하여 사용할 툴(tool)들을 자동으로 다운로드 할 수 있습니다. 이렇게 Homebrew로 자동으로 다운로드 하고 싶은 툴들을 정의하는 파일이 `Brewfile`입니다. 아래에 명령어로 현재 사용하고 있는 맥의 툴들을 정의하는 Brewfile을 생성할 수 있습니다.

```bash
brew bundle dump
```

이렇게 생성된 Brewfile을 확인해 본 결과, 툴이 전부 담겨있지 않았습니다. 그래서 추가로 원하는 툴을 넣고 만든 Brewfile이 아래와 같습니다.

```bash
brew "mas"
brew "git-flow"
brew "mysql@5.7"
brew "python3"
brew "node"
brew "watchman"
brew "php"
# zsh is default in MacOS Catalina
# brew "zsh"
brew "ruby"

mas "LINE", id: 539883307
mas "KakaoTalk", id: 869223134
mas "Slack", id: 803453959
mas "Trello", id: 1278508951

cask "ngrok"
tap "adoptopenjdk/openjdk"
cask "adoptopenjdk8"
cask "android-studio"
cask "sequel-pro"
cask "db-browser-for-sqlite"
cask "mysqlworkbench"
cask "sketch"
cask "postman"
cask "sourcetree"
cask "google-chrome"
cask "iterm2"
```

이렇게 원하는 툴들을 정의하는 방법에 대해서 자세히 알아 봅시다.

### brew

Homebrew에서 정식적으로 다운로드가 가능한 파일은 `brew "node"`와 같이 작성합니다. 작성해야할 툴에 이름을 정확히 알지 못한다면 아래에 명령어로 이름을 검색할 수 있습니다.

```bash
brew search node
```

그러면 아래와 같은 결과물을 확인할 수 있습니다.

```bash
==> Formulae
heroku/brew/heroku-node        libbitcoin-node                node                           node@10                        node_exporter                  nodeenv
leafnode                       llnode                         node-build                     node@8                         nodebrew                       nodenv

==> Casks
nodebox                                                        nodeclipse                                                     soundnode
```

검색 결과를 보면 `Formulae`와 `Casks`, 두가지 리스트를 확인할 수 있습니다. Homebrew에서 공식적으로 지원하는 툴들은 `Formulae` 리스트안에 있습니다. 이렇게 Homebrew가 공식적으로 지원하는 툴들은 Brewfile에 아래와 같이 작성해 두면 나중에 명령어 한번으로 모두 다운로드 할 수 있습니다.

```bash
brew "mas"
brew "git-flow"
brew "mysql@5.7"
brew "python3"
brew "node"
brew "watchman"
brew "php"
# zsh is default in MacOS Catalina
# brew "zsh"
brew "ruby"
```

### cask

그럼 `Casks`는 뭘까요? Casks는 Homebrew에서는 정식적으로 지원하지 않지만 Homebrew를 사용하여 다운로드 받을 수 있는 툴들을 의미합니다. 즉, 웹에서 다운로드하는 툴들을 설치할 수 있도록 지원하는 것이 Casks입니다.

예를 들어 구글의 `Chrome` 브라우저는 Homebrew에서 공식적으로 지원하지 않지만, Homebrew의 Casks를 사용하여 설치할 수 있습니다.

```bash
brew search chrome
```

이렇게 구글 Chrome을 검색해 보면 아래와 같은 결과를 얻을 수 있습니다.

```bash
==> Formulae
chrome-cli                                                                                     chrome-export

==> Casks
chrome-devtools                                dmm-player-for-chrome                          mkchromecast                                   homebrew/cask-versions/google-chrome-dev
chrome-remote-desktop-host                     epichrome                                      homebrew/cask-versions/google-chrome-beta
chromedriver                                   google-chrome                                  homebrew/cask-versions/google-chrome-canary
```

이 중에서 우리가 사용할 Chrome 브라우저는 `google-chrome`입니다. 아래의 Homebew 명령어를 통해 Chrome 브라우저를 설치 할 수 있습니다.

```bash
brew cask install google-chrome
```

이렇게 Homebrew에서는 공식적으로 지원하진 않지만, 다운로드 가능한 툴들은 Casks를 사용하여 Brewfile에 작성해 둡니다.

```bash
cask "ngrok"
tap "adoptopenjdk/openjdk"
cask "adoptopenjdk8"
cask "android-studio"
cask "sequel-pro"
cask "db-browser-for-sqlite"
cask "mysqlworkbench"
cask "sketch"
cask "postman"
cask "sourcetree"
cask "google-chrome"
cask "iterm2"
```

### mas

만약 사용하려는 툴이 맥의 `App store`에 있는 경우는 어떻게 할까요? 이것도 Homebrew를 사용하면 다운로드할 수 있습니다. Homebrew를 사용하여 App store에 존재하는 툴을 다운로드하기 위해서는 `mas`를 이용해야 합니다.

아래에 명령어로 `mas`를 설치할 수 있습니다.

```bash
brew install mas
```

이렇게 mas를 설치한 후 아래에 명령어로 mas로 설치 가능한 툴을 검색할 수 있습니다.

```bash
mas search xcode
```

이렇게 `xcode`를 검색하면 아래와 같은 결과를 볼 수 있습니다.

```bash
 497799835  Xcode                                                                (11.1)
1183412116  Swiftify for Xcode                                                   (5.1)
...
```

이렇게 검색된 툴은 아래에 명령어를 사용하여 설치 할 수 있습니다.

```bash
mas install 497799835
```

mas를 사용하여 다운로드 할 툴들을 아래와 같이 Brewfile에 작성해 둡니다.

```bash
mas "LINE", id: 539883307
mas "KakaoTalk", id: 869223134
mas "Slack", id: 803453959
mas "Trello", id: 1278508951
```

물론 이 부분은 mas가 없으면 설치를 할 수 없으므로 Brewfile 제일 상단에 mas를 설치하도록 설정합니다.

```bash
brew "mas"
...
```

이렇게 만든 Brewfile은 아래에 명령어를 통해 설치할 수 있습니다.

```bash
brew bundle --file=./Brewfile
```

이 명령어를 사용하려면 물론 Homebrew가 맥에 설치되 있어야 합니다. Homebrew 설치 및 사용할 툴들을 상세 설정하기 위해서 Shell Script를 만들어 봅시다.

{% include in-feed-ads.html %}

## Shell Script

Brewfile을 이용하면 쉽게 사용할 툴들을 설치 할 수 있습니다. 하지만, 설치뿐만 아니라 여러 설정들을 하기 위해서는 Shell Scrpit를 사용할 필요가 있습니다.

### Homebrew와 Brewfile 설치

우선 `./install.sh` 파일을 생성하고 아래와 같이 Homebrew를 설치하고, Brewfile을 실행하여 필요한 툴들을 설치하도록 작성합니다.

```bash
# !/bin/bash

# install brew
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

# install via brew
brew bundle --file=./Brewfile
```

이렇게 작성한 스크립트는 아래와 같이 명령어를 실행함으로써 사용할 수 있습니다.

```bash
./install.sh
```

### 보안 및 개인 정보 보호

Casks로 다운로드한 툴들은 웹에서 다운로드한 툴과 동일하기 때문에 실행을 하면 `Security` 문제로 실행이 되지 않습니다. 보통 이럴 경우, `설정 > 보안 및 개인 정보 보호`의 `확인 없이 열기`를 눌러 툴을 실행해야 합니다.

![맥(mac) 개발환경 설정 - 확인 없이 열기](/assets/images/category/environment/2019/configure-development-environment-on-mac-with-homebrew-and-shell-script/open-without-check-ko.jpg)

이 부분도 아래에 명령어를 통해 해결할 수 있습니다.

```bash
# sudo xattr -dr com.apple.quarantine /Applications/[App name]
sudo xattr -dr com.apple.quarantine /Applications/Sourcetree.app
```

또한 아래에 명령어로 툴들을 실행할 수 있습니다.

```bash
# open /Applications/[App name]
open /Applications/Sourcetree.app
```

이 내용을 `./install.sh`에 아래와 같이 작성합니다.

```bash
...
sudo xattr -dr com.apple.quarantine /Applications/Sequel\ Pro.app
open /Applications/Sequel\ Pro.app
sudo xattr -dr com.apple.quarantine /Applications/DB\ Browser\ for\ SQLite.app
open /Applications/DB\ Browser\ for\ SQLite.app
sudo xattr -dr com.apple.quarantine /Applications/MySQLWorkbench.app
open /Applications/MySQLWorkbench.app
sudo xattr -dr com.apple.quarantine /Applications/Sketch.app
open /Applications/Sketch.app
sudo xattr -dr com.apple.quarantine /Applications/Postman.app
open /Applications/Postman.app
sudo xattr -dr com.apple.quarantine /Applications/Sourcetree.app
open /Applications/Sourcetree.app
sudo xattr -dr com.apple.quarantine /Applications/Google\ Chrome.app
open /Applications/Google\ Chrome.app
sudo xattr -dr com.apple.quarantine /Applications/Android\ Studio.app
open /Applications/Android\ Studio.app
sudo xattr -dr com.apple.quarantine /Applications/iTerm.app
open /Applications/iTerm.app
```

open 명령어를 사용하여 툴을 실행하는 이유는 맥 하단에 있는 `Dock`에 고정하기 위해서 입니다.

{% include in-feed-ads.html %}

### 폰트

VSCode의 소스 코드 폰트로 `D2coding`를 사용하기 위해 zsh와 iTerm2에서 `Meslo LG M Regular for Powerline` 폰트를 사용하기 위해 미리 다운로드하여 `./fonts/` 폴더에 복사하였습니다.

- [D2coding](https://github.com/naver/d2codingfont){:rel="nofollow noreferrer" target="_blank"}
- [Meslo LG M Regular for Powerline](https://github.com/powerline/fonts/blob/master/Meslo%20Slashed/Meslo%20LG%20M%20Regular%20for%20Powerline.ttf){:rel="nofollow noreferrer" target="_blank"}

이렇게 미리 다운로드받은 폰트를 새로운 맥에 설치하기 위해 아래와 같이 복사 명령어를 실행합니다.

```bash
...
cp -a ./fonts/. ~/Library/Fonts
```

이 명령어를 `./install.sh`에 추가합니다.

### zsh

zsh 툴의 설정에 관한 내용을 정리하기 위해 `./zsh/` 폴더를 생성합니다. `./zsh/install.sh` 파일을 생성하고 아래와 같이 수정합니다.

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

위의 명령어는 oh my zsh를 설치하는 명렁어입니다.

그리고 현재 사용하고 있는 `~/.zshrc` 설정을 `./zsh/` 폴더로 복사합니다. 제가 사용하고 있는 설정은 아래와 같습니다.

```bash
# If you come from bash you might have to change your $PATH.
export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
export ZSH="$HOME/.oh-my-zsh"

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/robbyrussell/oh-my-zsh/wiki/Themes
ZSH_THEME="powerlevel10k/powerlevel10k"

# Set list of themes to pick from when loading at random
# Setting this variable when ZSH_THEME=random will cause zsh to load
# a theme from this variable instead of looking in ~/.oh-my-zsh/themes/
# If set to an empty array, this variable will have no effect.
# ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion.
# Case-sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to change how often to auto-update (in days).
# export UPDATE_ZSH_DAYS=13

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# You can set one of the optional three formats:
# "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# or set a custom format using the strftime function format specifications,
# see 'man strftime' for details.
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load?
# Standard plugins can be found in ~/.oh-my-zsh/plugins/*
# Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(git)

# python virtualenv
plugins=(virtualenv)

source $ZSH/oh-my-zsh.sh

# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='mvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# ssh
# export SSH_KEY_PATH="~/.ssh/rsa_id"

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"

# remove user name in zsh
# prompt_context(){}
POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(virtualenv dir_writable dir vcs)
POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=(status time battery)

# vscode code command
export PATH="$PATH:/Applications/Visual Studio Code.app/Contents/Resources/app/bin"
# brew path
export PATH=/usr/local/bin:/usr/local/sbin:$PATH
# python3 default
alias python=python3
alias pip=pip3
# composer
alias composer="php /usr/local/bin/composer.phar"
# Laravel
export PATH="$HOME/.composer/vendor/bin:$PATH"
# mysql
export PATH="/usr/local/opt/mysql@5.7/bin:$PATH"
# jekyll
export GEM_HOME=$HOME/gems
export PATH=$HOME/gems/bin:$PATH
# Android path for React Native
export ANDROID_HOME=$HOME/Library/Android/sdk
export PATH=$PATH:$ANDROID_HOME/emulator
export PATH=$PATH:$ANDROID_HOME/tools
export PATH=$PATH:$ANDROID_HOME/tools/bin
export PATH=$PATH:$ANDROID_HOME/platform-tools
```

이 파일을 복사하기 위해 아래에 명령어를 `./zsh/install.sh`에 추가합니다.

```bash
...
cp ./zsh/.zshrc ~/.zshrc
```

마지막으로 zsh 테마를 설치하기 위해 아래에 명령어를 `./zsh/install.sh`에 추가합니다.

```bash
...
git clone https://github.com/romkatv/powerlevel10k.git /Users/$USER/.oh-my-zsh/themes/powerlevel10k
```

이렇게 완성된 `./zsh/install.sh`는 아래와 같습니다.

```bash
# !/bin/bash

#install oh my zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

# copy my zsh settings
cp ./zsh/.zshrc ~/.zshrc

# install zsh theme
git clone https://github.com/romkatv/powerlevel10k.git /Users/$USER/.oh-my-zsh/themes/powerlevel10k
```

이렇게 완성된 `./zsh/install.sh` 스크립트를 `./install.sh`에서 실행하도록 `./install.sh` 파일을 아래와 같이 수정합니다.

```bash
...
# configure zsh
chmod 755 ./zsh/install.sh
./zsh/install.sh
```

{% include in-feed-ads.html %}

### VSCode 설정

VSCode의 설치 및 설정에 관한 정보를 관리하기 위해 `./vscode/` 폴더를 생성하고 `./vscode/install.sh` 파일을 생성합니다.

일단 VSCode를 설치하고 실행하기 위해 아래에 명령어를 추가합니다.

```bash
# !/bin/bash
brew cask install visual-studio-code

sudo xattr -dr com.apple.quarantine /Applications/Visual\ Studio\ Code.app
```

그리고 사용하고 있는 `Extension`들을 설치하기 위해 아래와 같이 명령어를 추가합니다.

```bash
...
# install vscode extensions
code --install-extension AlanWalk.markdown-toc
code --install-extension christian-kohler.npm-intellisense
code --install-extension christian-kohler.path-intellisense
code --install-extension CoenraadS.bracket-pair-colorizer
code --install-extension DavidAnson.vscode-markdownlint
code --install-extension dzannotti.vscode-babel-coloring
code --install-extension esbenp.prettier-vscode
code --install-extension felixfbecker.php-intellisense
code --install-extension fterrag.vscode-php-cs-fixer
code --install-extension gencer.html-slim-scss-css-class-completion
code --install-extension jcbuisson.vue
code --install-extension leizongmin.node-module-intellisense
code --install-extension mf.vscode-styled-components
code --install-extension ms-python.python
code --install-extension ms-vscode.vscode-typescript-tslint-plugin
code --install-extension msjsdiag.debugger-for-chrome
code --install-extension redhat.vscode-yaml
code --install-extension RoscoP.ActiveFileInStatusBar
code --install-extension shardulm94.trailing-spaces
code --install-extension vscode-icons-team.vscode-icons
```

VSCode의 extension을 설치하기 위해서는 `code --install-extension [extension id]`와 같이 명령어를 실행해야 합니다. 여기서 `extension id`는 아래와 같이 Extension 상세 페이지에서 Extension 이름 옆에서 확인할 수 있습니다.

![맥(mac) 개발환경 설정 - vscode  extension 설치](/assets/images/category/environment/2019/configure-development-environment-on-mac-with-homebrew-and-shell-script/vscode-install-extension.jpg)

마지막으로 현재 사용하고 있는 VSCode의 설정을 `./vscode/` 폴더에 복사합니다. VSCode의 설정은 아래에 폴더 위치에 있습니다.

```bash
~/Library/Application\ Support/Code/User/settings.json
```

이렇게 복사한 `settings.json` 파일을 새로운 맥에서 설정하기 위해 아래에 명령어를 `./vscode/install.sh`에 추가합니다.

```bash
...
cp ./vscode/settings.json ~/Library/Application\ Support/Code/User/settings.json
```

최종 완성된 `./vscode/install.sh`은 아래와 같습니다.

```bash
# !/bin/bash
brew cask install visual-studio-code

sudo xattr -dr com.apple.quarantine /Applications/Visual\ Studio\ Code.app

# install vscode extensions
code --install-extension AlanWalk.markdown-toc
code --install-extension christian-kohler.npm-intellisense
code --install-extension christian-kohler.path-intellisense
code --install-extension CoenraadS.bracket-pair-colorizer
code --install-extension DavidAnson.vscode-markdownlint
code --install-extension dzannotti.vscode-babel-coloring
code --install-extension esbenp.prettier-vscode
code --install-extension felixfbecker.php-intellisense
code --install-extension fterrag.vscode-php-cs-fixer
code --install-extension gencer.html-slim-scss-css-class-completion
code --install-extension jcbuisson.vue
code --install-extension leizongmin.node-module-intellisense
code --install-extension mf.vscode-styled-components
code --install-extension ms-python.python
code --install-extension ms-vscode.vscode-typescript-tslint-plugin
code --install-extension msjsdiag.debugger-for-chrome
code --install-extension redhat.vscode-yaml
code --install-extension RoscoP.ActiveFileInStatusBar
code --install-extension shardulm94.trailing-spaces
code --install-extension vscode-icons-team.vscode-icons

# copy vscode settings
cp ./vscode/settings.json ~/Library/Application\ Support/Code/User/settings.json
```

이 `./vscode/install.sh`를 호출하도록 `./install.sh`에 아래와 같이 추가합니다.

```bash
...
# configure VSCode
chmod 755 ./vscode/install.sh
./vscode/install.sh
```

{% include in-feed-ads.html %}

### iTerm2

iTerm2의 설치와 설정을 관리하기 위해 `./iterm2/` 폴더를 생성합니다. 그리고 현재의 iTerm2를 실행합니다.

![맥(mac) 개발환경 설정 - iterm2 설정](/assets/images/category/environment/2019/configure-development-environment-on-mac-with-homebrew-and-shell-script/iterm2-preference.jpg)

iTerm2의 현재 설정을 내보내기 위해서 `Preferences... > General > Preferences`를 선택합니다.

![맥(mac) 개발환경 설정 - iterm2 설정 내보내기](/assets/images/category/environment/2019/configure-development-environment-on-mac-with-homebrew-and-shell-script/iterm2-preference-expert.jpg)

위와 같은 화면에서 `Load preferences from a custom folder or URL`에 체크합니다. 그리고 `Browse` 버튼을 눌러 위에서 만든 `./iterm2/` 폴더를 설정합니다.

설정을 완료하면 `Save Current Settings to Folder` 버튼을 눌러 현재의 iTerm2의 설정을 내보냅니다.

이렇게 설정을 내보내면, `./iterm2/com.googlecode.iterm2.plist` 파일이 생성되는 것을 확인할 수 있습니다.

이제 `./iterm2/install.sh` 파일을 생성하고 아래와 같이 추가합니다.

```bash
# !/bin/bash

cp ./iterm2/com.googlecode.iterm2.plist ~/Library/Application\ Support/iTerm2/DynamicProfiles/

chsh -s /bin/zsh
```

위에서 생성한 `com.googlecode.iterm2.plist` 파일을 복사하는 명령어와 zsh를 기본 쉘로 설정하기 위한 명령어(`chsh -s /bin/zsh`)를 추가하였습니다.

이제 `./install.sh`에 아래에 내용을 추가합니다.

```bash
...
# copy iterm2 configuration
chmod 755 ./iterm2/install.sh
./iterm2/install.sh
```

### jekyll 개발 환경

저는 `jekyll`을 사용하여 블로그를 운영하고 있습니다. jekyll을 설치하기 위해 `./jekyll/install.sh` 파일을 생성하고 아래와 같이 수정하였습니다.

```bash
# !/bin/bash

sudo gem install bundler jekyll
```

이렇게 생성한 파일을 실행하기 위해 `./install.sh`에 아래와 같이 추가합니다.

```bash
...
# install jekyll
chmod 755 ./jekyll/install.sh
./jekyll/install.sh
```

### react-native 개발 환경

저는 앱 개발에 `React Native`를 사용합니다. React Native를 설치하기 위해 `./react-native/install.sh` 파일을 생성하고 아래와 같이 수정합니다.

```bash
# !/bin/bash
npm install -g react-native-cli

npm config set save-exact=true

sudo gem install cocoapods
```

- npm install -g react-native-cli: react-native-cli를 설치합니다.
- npm config set save-exact=true: react-native의 버전때문에 발생하는 문제를 줄이기 위해 npm 모듈을 설치할 때 package.json에 버전을 고정하도록 합니다.
- sudo gem install cocoapods: iOS의 pod를 사용하기 위해 cocoapods를 설치합니다.

이제 `./install.sh` 파일을 열고 아래와 같이 수정합니다.

```bash
...
# install react-native
chmod 755 ./react-native/install.sh
./react-native/install.sh
```

### python 개발 환경

python 개발 환경에 필요한 라이브러리들을 설치하기 위해 `./python/install.sh` 파일을 생성하고 아래와 같이 수정합니다.

```bash
# !/bin/bash
pip install virtualenv pylint autopep8
```

이렇게 생성한 파일을 실행하기 위해 `./install.sh` 파일을 생성하고 아래와 같이 추가합니다.


```bash
...
# install python3
chmod 755 ./python/install.sh
./python/install.sh
```

### Xcode

이제 마지막으로 `Xcode`를 설치하기 위해 `./xcode/install.sh` 파일을 생성하고 아래와 같이 수정합니다.

```bash
# !/bin/bash

mas install 497799835

sudo xcodebuild -license accept
```

- mas install 497799835: Homebrew의 mas를 사용하여 Xcode를 설치합니다.
- sudo xcodebuild -license accept: 명령어를 통해 Xcode의 라이센스를 동의합니다.

이렇게 생성한 스크립트를 실행하기 위해 `./install.sh`를 다음과 같이 수정합니다.

```bash
...
# install xcode
chmod 755 ./xcode/install.sh
./xcode/install.sh
```

{% include in-feed-ads.html %}

## 개발 환경 설정 저장(Github)

이렇게 만든 개발 환경 설정을 `Github`에 저장합니다. 지금까지 만든 저의 설정 내용은 아래에 링크를 통해 확인할 수 있습니다.

- [https://github.com/dev-yakuza/development-environment-for-mac-os](https://github.com/dev-yakuza/development-environment-for-mac-os){:target="_blank"}

## 맥 초기화 및 최신 OS 설치

맥을 초기화하고 최신 OS를 설치하기 위해 맥을 재부팅하고, 재부팅할 때 `Command + Option + r` 버튼을 눌러 인터넷을 통한 초기화를 시도합니다. 자세한 내용은 아래의 링크를 참고하세요

- [https://support.apple.com/ko-kr/HT201314](https://support.apple.com/ko-kr/HT201314){:rel="nofollow noreferrer" target="_blank"}

## 새로운 맥에 개발 환경 설정하기

이렇게 맥을 초기화 및 최신 OS를 설치한 후, 터미널을 실행하고 아래의 명령어로 git의 버전을 확인합니다.

```bash
git --version
```

아직 맥에 git이 설치되어 있지 않았기 때문에 git을 설치한다는 안내창이 나옵니다. 안내 창을 통해 git을 설치합니다.

git의 설치가 완료되면, git clone 명령어를 실행하여 미리 만든 개발 환경 스크립트를 복사합니다.

```bash
git clone https://github.com/dev-yakuza/development-environment-for-mac-os.git
```

모두 복사되었다면 이제 아래에 명령어를 통해 개발 환경을 자동으로 설정합니다.

```bash
./development-environment-for-mac-os/install.sh
```

스크립트가 실행될 때, 관리자 권한이 필요한 명령어들이 있어 중간중간 관리자의 패스워드를 입력해 주어야 합니다.

### iTerm2 수동 설정

아쉽게도 iTerm2는 수동으로 테마와 폰트를 설정해야 합니다. 아래와 같이 새로운 맥에서 수동으로 테마와 폰트를 설정해야 합니다.

![맥(mac) 개발환경 설정 - iterm2 테마 수동으로 설정](/assets/images/category/environment/2019/configure-development-environment-on-mac-with-homebrew-and-shell-script/iterm2-theme.jpg)

![맥(mac) 개발환경 설정 - iterm2 폰트 수동으로 설정](/assets/images/category/environment/2019/configure-development-environment-on-mac-with-homebrew-and-shell-script/iterm2-font.jpg)

## 완료

이번 맥 OS인 카탈리나(Catalina)로 업데이트하면서, 맥에 개발 환경을 처음부터 구성하게 되었습니다. 매번 수동으로 하나씩 하나씩 설치하던 것을 좀 더 효율적으로 할 방법이 없나 생각하다가 이번 블로그를 작성하게 되었습니다.

이제 Homebrew와 Shell Script를 사용하여 맥을 좀 더 쉽게 재설정하게 되었습니다. 여러분도 여러분만의 Brewfile과 Shell Script를 작성하여 좀 더 쉽게 개발 환경을 재설정 해 보세요~
