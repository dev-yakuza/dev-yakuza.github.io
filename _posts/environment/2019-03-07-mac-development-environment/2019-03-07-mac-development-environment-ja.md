---
layout: 'post'
permalink: '/environment/mac-development-environment/'
paginate_path: '/environment/:num/mac-development-environment/'
lang: 'ja'
categories: 'environment'
comments: true

title: 'マック(Mac)の開発環境の構築(3) - 開発環境'
description: '新しいマック(Mac)に開発環境を構築しています。現在開発する時使ってる開発環境を設定する方法を説明します。'
image: '/assets/images/category/environment/mac-development-environment/background.jpg'
---

## 概要
新しい(Mac)に開発環境を設定しています。このブログには開発環境を構築する方法を纏めてみます。

このブログはシリーズです。開発環境の別の部分が木になる方は下記の内容を確認してください。

- [マック(Mac)の開発環境の構築(1) - iTermとzsh]({{site.url}}/{{page.categories}}/mac-iterm-zsh/){:target="_blank"}
- [マック(Mac)の開発環境の構築(2) - tools]({{site.url}}/{{page.categories}}/mac-development-tools/){:target="_blank"}
- [マック(Mac)の開発環境の構築(3) - 開発環境]({{site.url}}/{{page.categories}}/mac-development-environment/){:target="_blank"}


## homebrew
マック(Mac)で一番重要なパッケージ管理者のhomebrewを下記のコマンドでインストールします。

```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

下記のコマンドでzsh設定ファイルを開きます。

```bash
code ~/.zshrc
```
設定ファイルの下に下記の内容を追加します。

```bash
export PATH=/usr/local/bin:/usr/local/sbin:$PATH
```


## python3
マック(Mac)には基本的python2がインストールされています。開発する時必要なpython3をインストールしてzshにpython3をデフォルトで設定します。

zsh(iTerm)を再起動して下記のコマンドでpython3をインストールします。

```bash
brew install python3
```

zsh設定ファイルの下に下記の内容を追加してpython3をデフォルトで設定します。

```bash
# code ~/.zshrc
alias python=python3
```

## git flow
下記のコマンドでgit flowをインストールします。

```bash
brew install git-flow
```

## node / npm
下のリンクを押してnodeをダウンロードやインストールします。

- node: [https://nodejs.org/en/download/](https://nodejs.org/en/download/){:rel="nofollow noreferrer" target="_blank"}


## react native
RN(React Native)のインストール関しては別のブログを作成しました。下記のリンクを押してインストール方法を確認してください。

- [RNインストール]({{site.url}}/react-native/installation/){:target="_blank"}


## Laravel
マック(Mac)には基本的phpがインストールされています。下記のコマンドで```composer```をインストールします。

```bash
curl -sS https://getcomposer.org/installer | sudo php -- --install-dir=/usr/local/bin/
```

zsh設定ファイルの下に下記の内容を追加します。

```bash
# code ~/.zshrc
alias composer="php /usr/local/bin/composer.phar"
```

下記のコマンドで権限を変更します。

```bash
sudo chmod -R 777 /Users/[user name]/.composer/
```

下記のコマンドでLaravelをインストールします。

```bash
composer global require laravel/installer
```

zsh設定ファイルを開いて下記の内容を追加します。

```bash
# code ~/.zshrc
export PATH="$HOME/.composer/vendor/bin:$PATH"
```

## mysqlインストール
下記のコマンドでmysqlをインストールします。

```bash
brew install mysql@5.7
```

zsh設定ファイルを開いて下記の内容を追加します。

```bash
# code ~/.zshrc
export PATH="/usr/local/opt/mysql@5.7/bin:$PATH"
export LDFLAGS="-L/usr/local/opt/mysql@5.7/lib"
export CPPFLAGS="-I/usr/local/opt/mysql@5.7/include"
```

下記のコマンドでmysqlサーバーを実行します。

```bash
mysql.server start
```

下記のコマンドでmysqlの設定を進めます。（パスワード設定など）

```bash
mysql_secure_installation
```


## jekyll
以前jekyllインストールに関してブログを作成したことがあります。下記のリンクを確認してインストールしてください。

- [jekyllインストール]({{site.url}}/jekyll/installation/){:target="_blank"}


## zsh設定ファイル
下記はzsh設定ファイルの内容です。

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
# prompt_context(){}
POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(dir_writable dir vcs)
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

