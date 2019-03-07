---
layout: 'post'
permalink: '/environment/mac-iterm-zsh/'
paginate_path: '/environment/:num/mac-iterm-zsh/'
lang: 'ja'
categories: 'environment'
comments: true

title: 'マック(Mac)の開発環境の構築(1) - iTermとzsh'
description: '新しいマック(Mac)に開発環境を構築してみようかと思います。マック(Mac)にiTermとzshを設定して新しいターミナル環境を構築します。'
image: '/assets/images/category/environment/mac-iterm-zsh/background.jpg'
---

## 概要
新しいマック(Mac)に開発環境を最初から構築した内容を纏めてみようかと思います。このブログはシリーズです。開発環境の別の部分が木になる方は下記の内容を確認してください。

- [マック(Mac)の開発環境の構築(1) - iTermとzsh]({{site.url}}/{{page.categories}}/mac-iterm-zsh/){:target="_blank"}
- [マック(Mac)の開発環境の構築(2) - tools]({{site.url}}/{{page.categories}}/mac-development-tools/){:target="_blank"}
- [マック(Mac)の開発環境の構築(3) - 開発環境]({{site.url}}/{{page.categories}}/mac-development-environment/){:target="_blank"}

このブログでは新しいマック(Mac)に[iTerm](https://www.iterm2.com/){:rel="nofollow noreferrer" target="_blank"}と[zsh](https://github.com/robbyrussell/oh-my-zsh){:rel="nofollow noreferrer" target="_blank"}を設定する方法について説明します。

- [iTerm](https://www.iterm2.com/){:rel="nofollow noreferrer" target="_blank"}
- [zsh](https://github.com/robbyrussell/oh-my-zsh){:rel="nofollow noreferrer" target="_blank"}


## iTermインストール
下記のリンクを押して`iTerm`ダウンロードページに移動します。

- iTermダウンロード: [ダウンロードページ](https://www.iterm2.com/downloads.html){:rel="nofollow noreferrer" target="_blank"}

下記の画面が見えたら、`Stable Releases`を押してダウンロードします。

![マック(mac)の開発環境の設定 - iTermダウンロード](/assets/images/category/environment/mac-iterm-zsh/iterm-download.png)

ダウンロードした`zip`ファイルを圧縮解除してインストールします。

![マック(mac)の開発環境の設定 - iTerm full disk access権限](/assets/images/category/environment/mac-iterm-zsh/iterm-full-disk-access.png)

上のようにiTermで`Full Disk Access`の権限を要請する時、右下の`Open System Preferences`を洗濯します。

![マック(mac)の開発環境の設定 - iTerm full disk access権限設定](/assets/images/category/environment/mac-iterm-zsh/iterm-full-disk-access-grant.png)

上のように親切な説明と`Security & Privacy`が実行されます。左下の錠前形を押して暗号を入力して修正できるようにします。

![マック(mac)の開発環境の設定 - iTerm full disk access権限設定画面](/assets/images/category/environment/mac-iterm-zsh/iterm-full-disk-access-grant-setting.png)

上部のタプで`Privacy`を洗濯して、左リストにある`Full Disk Access`を選択します。

![マック(mac)の開発環境の設定 - iTerm full disk access権限設定iTerm選択](/assets/images/category/environment/mac-iterm-zsh/iterm-full-disk-access-grant-setting-select-iterm.png)

右の`+`ボタンを押します。`Applications`を移動して、`iTerm`を選択して`Open`を押します。

![マック(mac)の開発環境の設定 - iTerm終了](/assets/images/category/environment/mac-iterm-zsh/iterm-full-disk-access-grant-setting-quit.png)

上のように`iTerm`を終了するかを聞かれる画面が見えたら`Quit Now`を押して`iTerm`を終了させます。

iTermを実行して問題なく実行されるか確認します。

## zsh
zshはターミナルをもっと使いやすくしてくれます。下記のリンクを押したら詳しく内容を確認することができます。

- zsh公式サイト: [zsh](https://github.com/robbyrussell/oh-my-zsh){:rel="nofollow noreferrer" target="_blank"}

zshの公式サイトを見たらインストール方法が下記のように表示しております。

![マック(mac)の開発環境の設定 - zshインストール](/assets/images/category/environment/mac-iterm-zsh/zsh-installation.png)

インストールしたiTermやターミナルを開いて下記のコマンドを実行します。

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

インストールが完了したら会のような画面が見えます。

![マック(mac)の開発環境の設定 - zshインストール完了](/assets/images/category/environment/mac-iterm-zsh/zsh-install-completed.png)

## iTermでzshをデフォルトで設定
iTermの基本的shellを使うようになっております。iTermが基本的zshを使うように設定します。

![マック(mac)の開発環境の設定 - iTerm zsh設定](/assets/images/category/environment/mac-iterm-zsh/zsh-install-completed.png)

iTermを実行して左上にある`iTerms2` > `Preferences...`を選択します。

![マック(mac)の開発環境の設定 - iTerm zshデフォルト設定](/assets/images/category/environment/mac-iterm-zsh/iterm-zsh-default-setting-path.png)

上のように設定画面が表示されたら、上部にある`Profiles`のタプを選択します。右にある`Command`設定で`Command`を選択して`/biz/zsh`を入力して終了します。

また、iTermを実行したら`zsh`が基本的実行されることを確認することができます。

## iTermテーマ設定
iTermはたくさんのテーマ(Theme)があります。皆さんが好きなテーマを設定して使ったらいいと思います。ここには`iterm2-solarized`のテーマを設定する方法について説明します。

- [iterm2-solarized](https://gist.github.com/kevin-smets/8568070){:rel="nofollow noreferrer" target="_blank"}

下記のリンクを押してテーマをダウンロードします。

- [iterm2-solarizedダウンロード](https://raw.githubusercontent.com/mbadolato/iTerm2-Color-Schemes/master/schemes/Solarized%20Dark%20-%20Patched.itermcolors){:rel="nofollow noreferrer" target="_blank"}

上のリンクを選択したらテーマファイルの内容が見えます。`command + s`を押してダウンロードします。

![マック(mac)の開発環境の設定 - zshテーマ設定](/assets/images/category/environment/mac-iterm-zsh/zsh-theme-setting.png)

ダウンロード時下にある`Format`を`All Files`で設定します。ファイルの後ろが`.itermcolors`であるか確認します。

また、iTermのPreferencesを開きます。

![マック(mac)の開発環境の設定 - iTermでzshテーマ設定](/assets/images/category/environment/mac-iterm-zsh/zsh-theme-import.png)

上のように`Profiles` > `Colors`を選択して右下にある`Color Preset...` > `import...`を選択します。

上部でダウンロードした`Solarized Dark - Patched.itermcolors`ファイルを選択します。

![マック(mac)の開発環境の設定 - iTermでzshテーマSolarized Dark設定](/assets/images/category/environment/mac-iterm-zsh/zsh-theme-solarized-dark.png)

また、`Color Preset...`を選択したら以前と違って`Solarized Dark`が追加されたことが確認できます。`Solarized Dark`を選択してテーマを設定します。

## Powerlevel9k設定
ターミナルでもっt詳しい情報を見るため`Powerlevel9k`を設定します。iTermを実行したら今は下記のように見ます。

![マック(mac)の開発環境の設定 - iTerm](/assets/images/category/environment/mac-iterm-zsh/normal_iterm.png)

下記のコマンドで`Powerlevel9k`をダウンロードします。

```bash
git clone https://github.com/bhilburn/powerlevel9k.git ~/.oh-my-zsh/custom/themes/powerlevel9k
```

zshの設定ファイルは`~/.zshrc`です。このファイルを開いてPowerlevel9kを設定します。

```bash
vi ~/.zshrc
```

設定ファイルにテーマ設定部分を探します。

```bash
# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/robbyrussell/oh-my-zsh/wiki/Themes
ZSH_THEME="robbyrussell"
```

テーマを`ZSH_THEME="robbyrussell"`から`ZSH_THEME="powerlevel9k/powerlevel9k"`に変更します。

iTermを再起動したら下記のような画面が見えます。

![マック(mac)の開発環境の設定 - iTerm powerlevel9k](/assets/images/category/environment/mac-iterm-zsh/powerlevel9k.png)

上のようにユーザ情報と`?`が見えます。?はフォントが設定されてないからです。下記のリンクを押してフォントダウンロードサイトに移動します。

- [Meslo LG M Regular for Powerline.ttf](https://github.com/powerline/fonts/blob/master/Meslo%20Slashed/Meslo%20LG%20M%20Regular%20for%20Powerline.ttf){:rel="nofollow noreferrer" target="_blank"}

上のリンクを押したら下記のように見えます。`View Raw`を押してフォントをダウンロードします。

![マック(mac)の開発環境の設定 - iTermダウンロードフォント](/assets/images/category/environment/mac-iterm-zsh/download-font.png)

ダウンロードが完了したらダウンロードしたフォントファイルを選択して実行します。

![マック(mac)の開発環境の設定 - iTermフォントインストール](/assets/images/category/environment/mac-iterm-zsh/install-font.png)

右下の`Install Font`を押してフォントをインストールします。インストールが終わったら、またiTermのPreferenceを開いて`Profiles` > `Text` > `Change Font`を選択します。

![マック(mac)の開発環境の設定 - iTermフォントインストール](/assets/images/category/environment/mac-iterm-zsh/set-font.png)

上部でダウンロードした`Meslo LG M Regular for Powerline`を選択します。

![マック(mac)の開発環境の設定 - iTermフォントインストール確認](/assets/images/category/environment/mac-iterm-zsh/check-font.png)

iTermを確認すると上のような画面が見えます。

私はここでユーザ名がな長いからユーザ名を非表示するように設定しました。下記のコマンドを実行します。

```bash
vi ~/.zshrc
```

下記の内容を一番下へ追加します。

```bash
prompt_context() {}
```

また、iTermを実行したらユーザ名が非表示されたことが確認できます。

![マック(mac)の開発環境の設定 - iTermユーザ名非表示](/assets/images/category/environment/mac-iterm-zsh/no-user-name.png)

## vscodeとの連動
zshでvscodeの`code`のコマンドを使えるように設定してvscodeには基本ターミナルをzshで設定する方法について説明します。

### zshでvscodeのコマンド設定
下記のコマンドでzsh設定を

```bash
vi ~/.zshrc
```

一番下に下記の内容を追加します。

```bash
export PATH="$PATH:/Applications/Visual Studio Code.app/Contents/Resources/app/bin"
```

iTermを再起動して下記のコマンドでvscodeが実行されるか確認します。

```
code .
```

### vscodeにzshを設定
vscodeを実行して右上の`Code` > `Preferences` > `Settings`を選択します。

![マック(mac)の開発環境の設定 - vscode zsh設定](/assets/images/category/environment/mac-iterm-zsh/vscode-setting.png)

検索バーへ`shell`を検索して`Terminal > Integrated > Shell: Osx`の部分を`/bin/bash`から`/bin/zsh`に変更します。

![マック(mac)の開発環境の設定 - vscode zsh shell設定](/assets/images/category/environment/mac-iterm-zsh/vscode-shell-setting.png)

また、fontfamilyを検索して`Meslo LG M for Powerline`を設定します。

![マック(mac)の開発環境の設定 - vscode zsh font設定](/assets/images/category/environment/mac-iterm-zsh/vscode-zsh-font-setting.png)

vscodeのターミナルを実行したら、zshが実行されることが確認できます。

![マック(mac)の開発環境の設定 - vscode zsh設定完了](/assets/images/category/environment/mac-iterm-zsh/vscode-zsh-font.png)
