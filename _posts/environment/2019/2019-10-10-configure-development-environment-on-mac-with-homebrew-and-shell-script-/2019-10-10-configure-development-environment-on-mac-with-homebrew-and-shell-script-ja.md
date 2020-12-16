---
layout: 'post'
permalink: '/environment/configure-development-environment-on-mac-with-homebrew-and-shell-script/'
paginate_path: '/environment/:num/configure-development-environment-on-mac-with-homebrew-and-shell-script/'
lang: 'ja'
categories: 'environment'
comments: true

title: 'HomebrewとShell Scriptを使ってマック(Mac)の開発環境構築を自動化する'
description: 'HomebrewとShell Scriptを使ってマック(Mac)の開発環境構築を自動化する方法を共有します。このように作ったBrefileとShell Scriptを使って新しマック(Mac)に開発環境を設定してみます。'
image: '/assets/images/category/environment/2019/configure-development-environment-on-mac-with-homebrew-and-shell-script/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

1. 概要](#概要)
1. [開発環境の構成](#開発環境の構成)
1. [Brewfile](#brewfile)
    - [brew](#brew)
    - [cask](#cask)
    - [mas](#mas)
1. [Shell Script](#shell-script)
    - [HomebrewとBrewfileのインストール](#homebrewとbrewfileのインストール)
    - [セキュリティとプライバシー](#セキュリティとプライバシー)
    - [フォント](#フォント)
    - [zsh](#zsh)
    - [VSCode設定](#vscode設定)
    - [iTerm2](#iterm2)
    - [jekyll開発環境](#jekyll開発環境)
    - [react-native開発環境](#react-native開発環境)
    - [python開発環境](#python開発環境)
    - [Xcode](#xcode)
1. [開発環境の設定を保存(Github)](#開発環境の設定を保存github)
1. [マックの初期化や最新OSインストール](#マックの初期化や最新osインストール)
1. [新しマックに開発環境を設定する](#新しマックに開発環境を設定する)
    - [iTerm2手動設定](#iterm2手動設定)
1. [完了](#完了)

</div>

## 概要

マック(Mac)に新しく開発環境を構築しております。下記のブログポストリストは以前新しマック(Mac)に開発環境を手動で構築した内容を纏めたブログです。

- [マック(Mac)の開発環境の構築(1) - iTermとzsh]({{site.url}}/{{page.categories}}/mac-iterm-zsh/){:target="_blank"}
- [マック(Mac)の開発環境の構築(2) - tools]({{site.url}}/{{page.categories}}/mac-development-tools/){:target="_blank"}
- [マック(Mac)の開発環境の構築(3) - 開発環境]({{site.url}}/{{page.categories}}/mac-development-environment/){:target="_blank"}

今回のブログポストでは上記のプログポストリストにある開発環境をHomebrewとShell Scriptで自動化してもっと簡単に開発環境を構築できるようにしてみました。

## 開発環境の構成

今現在私が使ってる開発環境の構成です。

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

今から上にある開発環境をHomebrewとShell Scriptを使って自動で構築できるようにしてみます。

{% include in-feed-ads.html %}

## Brewfile

Homebrewを使って使うツール(tool)を自動にダウンロードすることができます。このようにHomebrewで自動にダウンロードしたいツールを定義するファイルが`Brewfile`です。下記のコマンドで現在使ってるマックのツールを定義するBrewfileを生成することができます。

```bash
brew bundle dump
```

このコマンドで生成されたBrewfileを確認しましたが、使ってるツールが全部入ってないでした。それで追加で欲しいツールを入れて作ったBrewfileが下記になります。

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

このように使いたいツールを定義する方法について詳しく説明します。

### brew

Homebrewで正式的ダウンロードが可能なファイルは`brew "node"`ように作成します。定義するツールの名前を正確に分からない場合、下記のコマンドで名前を検索することができます。

```bash
brew search node
```

そしたら、下記のような結果を見ることができます。

```bash
==> Formulae
heroku/brew/heroku-node        libbitcoin-node                node                           node@10                        node_exporter                  nodeenv
leafnode                       llnode                         node-build                     node@8                         nodebrew                       nodenv

==> Casks
nodebox                                                        nodeclipse                                                     soundnode
```

検索結果をみたら`Formulae`と`Casks`、2つのリストが見えます。Homebrewが公式的サポートするツールは`Formulae`のリスト中にあります。このようにHomebrewが公式的サポートするツールはBrewfile中に下記のように作成しておいたら、将来に一個のコマンドを実行すると全てダウンロードすることができます。

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

そしたら`Casks`は何でしょうか？CasksはHomebrewで公式的はサポートしないですが、Homebrewを使ってダウンロードできるツールを意味します。つまり、ウェブでダウンロードできるツールをHomebrewでインストールできるようにする機能がCasksです。

例えば、グーグルの`Chrome`ブラウザはHomebrewが公式的サポートしてないですが、HomebrewのCasksを使ってインストールすることができます。

```bash
brew search chrome
```

このようにグーグルのChromeを検索して見ると下記のような結果が見えます。

```bash
==> Formulae
chrome-cli                                                                                     chrome-export

==> Casks
chrome-devtools                                dmm-player-for-chrome                          mkchromecast                                   homebrew/cask-versions/google-chrome-dev
chrome-remote-desktop-host                     epichrome                                      homebrew/cask-versions/google-chrome-beta
chromedriver                                   google-chrome                                  homebrew/cask-versions/google-chrome-canary
```

この中で私たちが使うChromeブラウザは`google-chrome`です。下記のHomebrewコマンドを使ってChromeブラウザをインストールすることができます。

```bash
brew cask install google-chrome
```

このようにHomebrewが公式的サポートしてないですが、ダウンロードが可能なツールをCasksを使ってBrewfileに作成します。

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

もし、使いたいツールがマック(Mac)の`App store`にある場合、どうしたらいいでしょうか？これもHomebrewを使ってダウンロードすることができます。Homebrewを使ってApp storeにあるツールをダウンロードするためには`mas`を使います。

下記のコマンドで`mas`をインストールします。

```bash
brew install mas
```

このようにmasをインストールした後、下記のコマンドでmasでインストールできるツールを検索することができます。

```bash
mas search xcode
```

このように`xcode`を検索したら下記のような結果が出ます。

```bash
 497799835  Xcode                                                                (11.1)
1183412116  Swiftify for Xcode                                                   (5.1)
...
```

このように検索出来たツールは下記のコマンドでインストールすることが出来ます。

```bash
mas install 497799835
```

masを使ってダウンロードできるツールを下記のようにBrewfileに作成します。

```bash
mas "LINE", id: 539883307
mas "KakaoTalk", id: 869223134
mas "Slack", id: 803453959
mas "Trello", id: 1278508951
```

もちろん、この部分はmasがないとインストール出来ないので、Brewfileの一番上にmasをインストールするように設定します。

```bash
brew "mas"
...
```

このように作ったBrewfileは下記のコマンドでインストールすることが出来ます。

```bash
brew bundle --file=./Brewfile
```

このコマンドを使うためにはもちろんHomebrewがマックにインストールされないとダメです。Homebrewのインストールや使うツールを細かく設定するためShell Scriptを作ってみましょう。

{% include in-feed-ads.html %}

## Shell Script

Brewfileを使ったら使うツールを簡単にインストールすることが出来ます。しかし、インストールだけではなく色んな設定もするためにはShell Scriptを使う必要があります。

### HomebrewとBrewfileのインストール

まず、`./install.sh`ファイルを生成して下記のようにHomebrewをインストールして、Brewfileを実行して必要なツールをインストールするように作成します。

```bash
# !/bin/bash

# install brew
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

# install via brew
brew bundle --file=./Brewfile
```

このように作成したスクリプトは下記のコマンドで実行出来ます。

```bash
./install.sh
```

### セキュリティとプライバシー

Casksでダウンロードしたツールはウェブでダウンロードしたツールと同じなので実行すると`Security`の問題で実行が出来ません。普通はこの時、`設定 > セキュリティとプライバシー`を開いて`許可`ボタンを押してツールを実行します。

![マック(mac)の開発環境設定 - セキュリティとプライバシーの許可](/assets/images/category/environment/2019/configure-development-environment-on-mac-with-homebrew-and-shell-script/open-without-check-ja.jpg)

この部分も下記のコマンドで解決出来ます。

```bash
# sudo xattr -dr com.apple.quarantine /Applications/[App name]
sudo xattr -dr com.apple.quarantine /Applications/Sourcetree.app
```

また、下記のコマンドでツールを実行することも出来ます。

```bash
# open /Applications/[App name]
open /Applications/Sourcetree.app
```

この内容を`./install.sh`に下記のように作成します。

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

openコマンドを使ってツールを実行する理由はマックの下にある`Dock`に固定するためです。

{% include in-feed-ads.html %}

### フォント

VSCodeのソースコードフォントで`D2coding`を使うためzshとiTerm2で`Meslo LG M Regular for Powerline`フォントを使うためフォントを事前にダウンロードして`./fonts/`フォルダにコピーします。

- [D2coding](https://github.com/naver/d2codingfont){:rel="nofollow noreferrer" target="_blank"}
- [Meslo LG M Regular for Powerline](https://github.com/powerline/fonts/blob/master/Meslo%20Slashed/Meslo%20LG%20M%20Regular%20for%20Powerline.ttf){:rel="nofollow noreferrer" target="_blank"}

このように事前にダウンロードしたフォントを新しマックでインストールするためには下記のコマンドを実行します。

```bash
...
cp -a ./fonts/. ~/Library/Fonts
```

このコマンドを`./install.sh`ファイルに追加します。

### zsh

zshのツールの設定を管理するため`./zsh/`フォルダを生成します。`./zsh/install.sh`ファイルを生成下記のように修正します。

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

このコマンドはoh my zshをインストールするコマンドです。

そして現在使ってる`~/.zshrc`設定を`./zsh/`フォルダにコピーします。私が使ってる設定は下記のようです。

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

このファイルをコピーするため下記のコマンドを`./zsh/install.sh`に追加します。

```bash
...
cp ./zsh/.zshrc ~/.zshrc
```

最後にはzshテーマをインストールするため下記のコマンドを`./zsh/install.sh`に追加します。

```bash
...
git clone https://github.com/romkatv/powerlevel10k.git /Users/$USER/.oh-my-zsh/themes/powerlevel10k
```

完成した`./zsh/install.sh`は下記のようです。

```bash
# !/bin/bash

#install oh my zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

# copy my zsh settings
cp ./zsh/.zshrc ~/.zshrc

# install zsh theme
git clone https://github.com/romkatv/powerlevel10k.git /Users/$USER/.oh-my-zsh/themes/powerlevel10k
```

完成した`./zsh/install.sh`スクリプトを`./install.sh`で実行するため`./install.sh`ファイルを下記のように修正します。

```bash
...
# configure zsh
chmod 755 ./zsh/install.sh
./zsh/install.sh
```

{% include in-feed-ads.html %}

### VSCode設定

VSCodeのインストールや設定を管理するため`./vscode/`フォルダを作って、`./vscode/install.sh`ファイルを生成します。

VSCodeをインストールして実行するため下記のようにコマンドを追加します。

```bash
# !/bin/bash
brew cask install visual-studio-code

sudo xattr -dr com.apple.quarantine /Applications/Visual\ Studio\ Code.app
```

そして使ってる`Extension`をインストールするため下記のようにコマンドを追加します。

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

VSCodeのextensionをインストールするためには`code --install-extension [extension id]`なようにコマンドを作ります。ここで`extension id`は下記のようにExtensionの詳細ページでExtensionの名前の横で確認できます。

![マック(mac)の開発環境設定 - vscode  extension インストール](/assets/images/category/environment/2019/configure-development-environment-on-mac-with-homebrew-and-shell-script/vscode-install-extension.jpg)

最後には現在使ってるVSCodeの設定を`./vscode/`フォルダにコピーします。VSCodeの設定は下記のフォルダにあります。

```bash
~/Library/Application\ Support/Code/User/settings.json
```

このようにコピーした`settings.json`ファイルを新しマックで設定するため下記のコマンドを`./vscode/install.sh`に追加します。

```bash
...
cp ./vscode/settings.json ~/Library/Application\ Support/Code/User/settings.json
```

最終完成した`./vscode/install.sh`は下記のようです。

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

この`./vscode/install.sh`を実行するため`./install.sh`ファイルの下に下記のように追加します。

```bash
...
# configure VSCode
chmod 755 ./vscode/install.sh
./vscode/install.sh
```

{% include in-feed-ads.html %}

### iTerm2

iTerm2のインストールや設定を管理するため`./iterm2/`フォルダを生成します。そして現在のiTerm2を実行します。

![マック(mac)の開発環境設定 - iterm2 設定](/assets/images/category/environment/2019/configure-development-environment-on-mac-with-homebrew-and-shell-script/iterm2-preference.jpg)

iTerm2の現在設定をエクスポートするため`Preferences... > General > Preferences`を選択します。

![マック(mac)の開発環境設定 - iterm2 設定エクスポート 내보내기](/assets/images/category/environment/2019/configure-development-environment-on-mac-with-homebrew-and-shell-script/iterm2-preference-expert.jpg)

上の画面で`Load preferences from a custom folder or URL`をチェックします。そして`Browse`ボタンを押して上部で作った`./iterm2/`フォルダを設定します。

設定を完了したら`Save Current Settings to Folder`ボタンを押して現在のiTerm2の設定をエクスポートします。

このように設定をエクスポートすると、`./iterm2/com.googlecode.iterm2.plist`ファイルが生成されることが確認できます。

次は、`./iterm2/install.sh`ファイルを生成して下記のように追加します。

```bash
# !/bin/bash

cp ./iterm2/com.googlecode.iterm2.plist ~/Library/Application\ Support/iTerm2/DynamicProfiles/

chsh -s /bin/zsh
```

上部で生成した`com.googlecode.iterm2.plist`ファイルをコピーするコマンドとzshを基本Shellで設定するコマンド(`chsh -s /bin/zsh`)を追加しました。

次は`./install.sh`ファイルしたに下記の内容を追加します。

```bash
...
# copy iterm2 configuration
chmod 755 ./iterm2/install.sh
./iterm2/install.sh
```

### jekyll開発環境

私は`jekyll`を使ってブログを運営しています。jekyllをインストールするため`./jekyll/install.sh`ファイルを生成して下記のように修正します。

```bash
# !/bin/bash

sudo gem install bundler jekyll
```

生成したフィルを実行するため`./install.sh`ファイルの下に下記のように追加します。

```bash
...
# install jekyll
chmod 755 ./jekyll/install.sh
./jekyll/install.sh
```

### react-native開発環境

私はアプリ開発に`React Native`を使ってます。React Nativeをインストールすため`./react-native/install.sh`ファイルを生成して下記のように修正します。

```bash
# !/bin/bash
npm install -g react-native-cli

npm config set save-exact=true

sudo gem install cocoapods
```

- npm install -g react-native-cli: react-native-cliをインストールします。
- npm config set save-exact=true: react-nativeのバージョンのせいで発生する問題を減らすためnpmモジュールをインストールする時package.jsonにバージョンを固定するようにします。
- sudo gem install cocoapods: iOSのpodを使うためcocoapodsをインストールします。

次は`./install.sh`ファイルを開いて下記のように修正します。

```bash
...
# install react-native
chmod 755 ./react-native/install.sh
./react-native/install.sh
```

### python開発環境

python開発環境に必要なライブラリをインストールするため`./python/install.sh`ファイルを生成して下記のように修正します。

```bash
# !/bin/bash
pip install virtualenv pylint autopep8
```

生成したファイルを実行するため`./install.sh`ファイルを生成して下記のように追加します。

```bash
...
# install python3
chmod 755 ./python/install.sh
./python/install.sh
```

### Xcode

これが最後です。`Xcode`をインストールするため`./xcode/install.sh`ファイルを生成して下記のように修正します。

```bash
# !/bin/bash

mas install 497799835

sudo xcodebuild -license accept
```

- mas install 497799835: Homebrewのmasを使ってXcodeをインストールします。
- sudo xcodebuild -license accept: コマンドを使ってXcodeのライセンスに同意します。

生成したスクリプトを実行するため`./install.sh`を下記のように修正します。

```bash
...
# install xcode
chmod 755 ./xcode/install.sh
./xcode/install.sh
```

{% include in-feed-ads.html %}

## 開発環境の設定を保存(Github)

このように作った開発環境の設定を`Github`に保存します。今まで作った私の設定内容は下記のリンクで確認することができます。

- [https://github.com/dev-yakuza/development-environment-for-mac-os](https://github.com/dev-yakuza/development-environment-for-mac-os){:target="_blank"}

## マックの初期化や最新OSインストール

マックを初期化して最新のOSをインストールするためマックを再起動します。再起動する時`Command + Option + r`を押してインターネット経由で macOS 復元を試します。詳しく内容は下記のリンクを確認してください。

- [https://support.apple.com/ja-jp/HT201314](https://support.apple.com/ja-jp/HT201314){:rel="nofollow noreferrer" target="_blank"}

## 新しマックに開発環境を設定する

このようにマックを初期化や最新のOSをインストールした後、ターミナルを実行して下記のコマンドでgitのバージョンを確認します。

```bash
git --version
```

まだ、マックにgitがインストールされてないので、gitをインストールする案内メッセージが出ます。案内メッセージを使ってgitをインストールします。

gitのインストールが終わったら、git cloneコマンドを実行して上で作った開発環境のスクリプトをコピーします。

```bash
git clone https://github.com/dev-yakuza/development-environment-for-mac-os.git
```

コピーが終わったら、下記のコマンドで開発環境を児童に設定します。

```bash
./development-environment-for-mac-os/install.sh
```

スクリプトが実行する際、管理者権限が必要なコマンドがあるので途中に管理者のパスワードを入力する必要があります。

### iTerm2手動設定

残念ですがiTerm2は手動でテーマとフォントを設定する必要があります。下記のように新しマックに手動でテーマとフォントを設定します。

![マック(mac)の開発環境設定 - iterm2のテーマを手動で設定](/assets/images/category/environment/2019/configure-development-environment-on-mac-with-homebrew-and-shell-script/iterm2-theme.jpg)

![マック(mac)の開発環境設定 - iterm2のフォントを手動で設定](/assets/images/category/environment/2019/configure-development-environment-on-mac-with-homebrew-and-shell-script/iterm2-font.jpg)

## 完了

今回、マックのOSであるカタリナ(Catalina)をアップデートする際、マックの開発環境を最初から構築することになりました。毎回毎回、手動で一つ一つづつインストールしたものをちょっと効率的できる方法がないか探してみて、今回のブログを作成することになりました。

今後はHomebrewとShell Scriptを使ってマックをもっと簡単に再設定ができるようになりました。皆さんも皆さんのBrewfileとShell Scriptを作って簡単にマックの開発環境が設定できるようにしてみてください。
