---
published: false
layout: 'post'
permalink: '/environment/mac-development-environment/'
paginate_path: '/environment/:num/mac-development-environment/'
lang: 'ko'
categories: 'environment'
comments: true

title: '맥(Mac) 개발 환경 구축(3) - 개발 환경'
description: '새로운 맥(Mac)에 개발 환경을 구축하려고 합니다. 지금 현재 개발에 사용하고 개발 환경을 설정하는 방법에 대해서 설명합니다.'
image: '/assets/images/category/environment/mac-development-environment/background.jpg'
---

## 개요
맥(Mac)에 새롭게 개발 환경을 구축하고 있습니다. 이 블로그에서는 개발 환경을 구성하는 방법에 대해서 정리합니다.

이 블로그는 연재물입니다. 이전 zsh 설치, 개발 툴에 관해서는 이전 블로그를 확인해 주세요.

- [맥(Mac) 개발 환경 구축(1) - iTerm과 zsh]({{site.url}}/{{page.categories}}/mac-iterm-zsh/){:target="_blank"}
- [맥(Mac) 개발 환경 구축(2) - tools]({{site.url}}/{{page.categories}}/mac-iterm-zsh/){:target="_blank"}


## python3
맥(Mac)에는 기본적으로 python2가 설치되어 있습니다. 개발에 필요한 python3를 설치하고 zsh에 python3을 기본으로 설정하겠습니다.

아래에 명령어로 homebrew를 설치합니다.

```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

아래에 명령어로 zsh 설정 파일을 엽니다.

```bash
code ~/.zshrc
```

설정 파일 하단에 아래에 내용을 추가합니다.

```bash
export PATH=/usr/local/bin:/usr/local/sbin:$PATH
```

zsh를 재실행하고 아래에 명령어로 python3를 설치합니다.

```bash
brew install python3
```

zsh 설정 파일 하단에 아래에 내용을 추가하여 python3을 기본으로 설정합니다.

```bash
# code ~/.zshrc
alias python=python3
```

## git flow
아래에 명령어로 git flow를 설치합니다.

```bash
brew install git-flow
```

## node / npm
아래에 링크를 눌러 node를 다운로드 및 설치합니다.

- node: [https://nodejs.org/ko/download/](https://nodejs.org/ko/download/){:rel="nofollow noreferrer" target="_blank"}


## react native
이전에 RN(React Native) 설치에 관한 블로그를 작성하였습니다. 아래에 링크를 확인하여 설치합니다.

- [RN 설치]({{site.url}}/react-native/installation/){:target="_blank"}


## Laravel
맥(Mac)은 기본적으로 php가 설치되어 있습니다. 아래에 명령어로 ```composer```를 설치합니다.

```bash
curl -sS https://getcomposer.org/installer | sudo php -- --install-dir=/usr/local/bin/
```

zsh 설정 파일 하단에 아래에 내용을 추가합니다.

```bash
# code ~/.zshrc
alias composer="php /usr/local/bin/composer.phar"
```

아래에 명령어로 권한을 변경합니다.

```bash
sudo chmod -R 777 /Users/[user name]/.composer/
```

아래에 명령어로 Laravel을 설치합니다.

```bash
composer global require laravel/installer
```

zsh 설정 파일을 열고 아래에 내용을 추가합니다.

```bash
# code ~/.zshrc
export PATH="$HOME/.composer/vendor/bin:$PATH"
```

## mysql 설치
아래에 명령어로 mysql을 설치합니다.

```bash
brew install mysql@5.7
```

zsh 설정 파일을 열고 아래에 내용을 추가합니다.

```bash
# code ~/.zshrc
export PATH="/usr/local/opt/mysql@5.7/bin:$PATH"
export LDFLAGS="-L/usr/local/opt/mysql@5.7/lib"
export CPPFLAGS="-I/usr/local/opt/mysql@5.7/include"
```

아래에 명령어로 mysql 서버를 실행합니다.

```bash
mysql.server start
```

아래에 명령어를 통해 mysql 설정을 진행합니다.(패스워드 설정 등)

```bash
mysql_secure_installation
```

## zsh 설정 파일
아래는 zsh 설정 파일의 내용입니다.

```bash
# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
export ZSH="/Users/jeonghean_kim/.oh-my-zsh"

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/robbyrussell/oh-my-zsh/wiki/Themes
ZSH_THEME="powerlevel9k/powerlevel9k"

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
prompt_context(){}
# vscode code command
export PATH="$PATH:/Applications/Visual Studio Code.app/Contents/Resources/app/bin"
# brew path
export PATH=/usr/local/bin:/usr/local/sbin:$PATH
# python3 default
alias python=python3
# composer
alias composer="php /usr/local/bin/composer.phar"
# Laravel
export PATH="$HOME/.composer/vendor/bin:$PATH"
# mysql
export PATH="/usr/local/opt/mysql@5.7/bin:$PATH"
```

