---
layout: 'post'
permalink: '/environment/mac-development-environment/'
paginate_path: '/environment/:num/mac-development-environment/'
lang: 'en'
categories: 'environment'
comments: true

title: 'Development Environment on Mac(3) - for development'
description: I'm setting the development environment on new Mac. in here, I'll introduce how to configure the development environment what I use.
image: '/assets/images/category/environment/mac-development-environment/background.jpg'
---

## Outline
I got a new Mac, so I'am configuring the development environment on it. in this blog post, I'll show how to set the development environment what I use.

this blog is a series. if you want to know other development environment, see other blog posts.

- [Development Environment on Mac(1) - iTerm & zsh]({{site.url}}/{{page.categories}}/mac-iterm-zsh/){:target="_blank"}
- [Development Environment on Mac(2) - for tools]({{site.url}}/{{page.categories}}/mac-development-tools/){:target="_blank"}
- [Development Environment on Mac(3) - for development]({{site.url}}/{{page.categories}}/mac-development-environment/){:target="_blank"}


## homebrew
execute the command below to install homebrew which is the package manager in Mac.

```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

execute the command below to open zsh configuration file.

```bash
code ~/.zshrc
```

add the content below to the bottom of the configuration file.

```bash
export PATH=/usr/local/bin:/usr/local/sbin:$PATH
```

## python3
Mac has basically python2. in here, I'll introduce how to install python3 and configure python3 to zsh default.

open zsh(iTerm) and execute the command below to install python3.

```bash
brew install python3
```

add the below to the bottom of zsh configuration file to set python3 to default.

```bash
# code ~/.zshrc
alias python=python3
```

## git flow
execute the command below to install git flow.

```bash
brew install git-flow
```

## node / npm
click the link below to download and install node.

- node: [https://nodejs.org/en/download/](https://nodejs.org/en/download/){:rel="nofollow noreferrer" target="_blank"}


## react native
I wrote about how to install RN(React Native) on another blog post. click the link below to check how to install RN(React Native).

- [RN installation]({{site.url}}/react-native/installation/){:target="_blank"}


## Laravel
Mac has basically php. execute the command below to install `composer`.

```bash
curl -sS https://getcomposer.org/installer | sudo php -- --install-dir=/usr/local/bin/
```

open zsh configuration file and add the content below to the bottom of it.

```bash
# code ~/.zshrc
alias composer="php /usr/local/bin/composer.phar"
```

execute the command below to change the permission.

```bash
sudo chmod -R 777 /Users/[user name]/.composer/
```

execute the command below to install Laravel

```bash
composer global require laravel/installer
```

add the content below to the bottom of zsh settings file.

```bash
# code ~/.zshrc
export PATH="$HOME/.composer/vendor/bin:$PATH"
```


## mysql installation
execute the command below to install mysql.

```bash
brew install mysql@5.7
```

open zsh configuration file and add the below to the bottom of it.

```bash
# code ~/.zshrc
export PATH="/usr/local/opt/mysql@5.7/bin:$PATH"
export LDFLAGS="-L/usr/local/opt/mysql@5.7/lib"
export CPPFLAGS="-I/usr/local/opt/mysql@5.7/include"
```

execute the command below to start mysql server.

```bash
mysql.server start
```

execute the command below to start mysql configuration(set password, etc).

```bash
mysql_secure_installation
```

## jekyll
I have the blog post about how to install jekyll. click the link below to see how to install it.

- [jekyll installation]({{site.url}}/jekyll/installation/){:target="_blank"}

## zsh configuration file
the below is zsh configuration file's contents.

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

