---
layout: 'post'
permalink: '/environment/mac-iterm-zsh/'
paginate_path: '/environment/:num/mac-iterm-zsh/'
lang: 'en'
categories: 'environment'
comments: true

title: 'Development Environment on Mac(1) - iTerm & zsh'
description: I try to set the development environment on new Mac. in here, I'll introduce how to configure iTerm and zsh for Terminal on new Mac.
image: '/assets/images/category/environment/mac-iterm-zsh/background.jpg'
---

## Outline
I try to write how to configure the development environment from very first time on Mac. this blog is a series. if you want to know other development environment, see other blog posts.

- [Development Environment on Mac(1) - iTerm & zsh]({{site.url}}/{{page.categories}}/mac-iterm-zsh/){:target="_blank"}
- [Development Environment on Mac(2) - for tools]({{site.url}}/{{page.categories}}/mac-development-tools/){:target="_blank"}
- [Development Environment on Mac(3) - for development]({{site.url}}/{{page.categories}}/mac-development-environment/){:target="_blank"}

in here, I'll introduce how to configure [iTerm](https://www.iterm2.com/){:rel="nofollow noreferrer" target="_blank"} and [zsh](https://github.com/robbyrussell/oh-my-zsh){:rel="nofollow noreferrer" target="_blank"} on Mac.

- [iTerm](https://www.iterm2.com/){:rel="nofollow noreferrer" target="_blank"}
- [zsh](https://github.com/robbyrussell/oh-my-zsh){:rel="nofollow noreferrer" target="_blank"}


## iTerm Installation
click the link below to go to `iTerm` download page.

- iTerm download: [Download](https://www.iterm2.com/downloads.html){:rel="nofollow noreferrer" target="_blank"}

you can see the screen like below, click `Stable Releases` to download.

![Development Environment on Mac - iTerm download](/assets/images/category/environment/mac-iterm-zsh/iterm-download.png)

unzip `zip` file you downloaded and install it.

![Development Environment on Mac - iTerm full disk access permission](/assets/images/category/environment/mac-iterm-zsh/iterm-full-disk-access.png)

if iTerm asks you `Full Disk Access` permission, click `Open System Preferences` on the right bottom.

![Development Environment on Mac - iTerm full disk access permission setting](/assets/images/category/environment/mac-iterm-zsh/iterm-full-disk-access-grant.png)

you can see the nice explanation and `Security & Privacy` is activated. click the lock shape on the left bottom, and insert your password to make editable.

![Development Environment on Mac - iTerm full disk access permission setting screen](/assets/images/category/environment/mac-iterm-zsh/iterm-full-disk-access-grant-setting.png)

select `Privacy` on the top tab, and click `Full Disk Accesss` on the left list.

![Development Environment on Mac - iTerm full disk access permission setting iTerm select](/assets/images/category/environment/mac-iterm-zsh/iterm-full-disk-access-grant-setting-select-iterm.png)

click `+` button on the right side. go to `Applications`, and select `iTerm` and click `Open`.

![Development Environment on Mac - iTerm quit](/assets/images/category/environment/mac-iterm-zsh/iterm-full-disk-access-grant-setting-quit.png)

if Mac asks you that you want to quit `iTerm`, click `Quit Now` to quit `iTerm`.

after it, check iTerm is executed.

## zsh
zsh makes Terminal easier to use. if you want to know more details, click the link below.

- zsh official site: [zsh](https://github.com/robbyrussell/oh-my-zsh){:rel="nofollow noreferrer" target="_blank"}

you can find the installation on zsh official site like below.

![Development Environment on Mac - zsh installation](/assets/images/category/environment/mac-iterm-zsh/zsh-installation.png)

open iTerm or Terminal and execute the command below.

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

after installing, you can see the screen like below.

![Development Environment on Mac - zsh install completed](/assets/images/category/environment/mac-iterm-zsh/zsh-install-completed.png)

## Configure zsh to iTerm Default Terminal
iTerm's default is to use the basic shell. let's set iTerm uses basically zsh.

![Development Environment on Mac - iTerm zsh configuration](/assets/images/category/environment/mac-iterm-zsh/zsh-install-completed.png)

execute iTerm and click `iTerms2` > `Preferences...` on the left top.

![Development Environment on Mac - iTerm zsh default setting](/assets/images/category/environment/mac-iterm-zsh/iterm-zsh-default-setting-path.png)

you can see the screen like above. click `Profiles` tab on the top. insert `/bin/zsh` in `Command` on `Command` section on the right middle.

after it, restart iTerm. you can see `zsh` is executed by default.

## Configure iTerm Theme.
there are many themes for iTerm. you can configure the theme what you want. in here, I'll introduce how to set `iterm2-solarized` theme.

- [iterm2-solarized](https://gist.github.com/kevin-smets/8568070){:rel="nofollow noreferrer" target="_blank"}

click the link below to download the theme.

- [download iterm2-solarized](https://raw.githubusercontent.com/mbadolato/iTerm2-Color-Schemes/master/schemes/Solarized%20Dark%20-%20Patched.itermcolors){:rel="nofollow noreferrer" target="_blank"}

when you click the link above, you can see the theme file contents. push `command + s` to save it.

![Development Environment on Mac - zsh theme setting](/assets/images/category/environment/mac-iterm-zsh/zsh-theme-setting.png)

before you download it, change to `All Files` on `Format` on the bottom. and check the end of the file is `.itermcolors`.

open Preferences of iTerm again.

![Development Environment on Mac - zsh theme setting on iterm](/assets/images/category/environment/mac-iterm-zsh/zsh-theme-import.png)

click `Profiles` > `Colors` like above, and click `Color Preset...` > `import...` on the right bottom.

select `Solarized Dark - Patched.itermcolors` file you downloaded above.

![Development Environment on Mac - zsh theme Solarized Dark setting on iterm](/assets/images/category/environment/mac-iterm-zsh/zsh-theme-solarized-dark.png)

select `Color Preset...` again, you can see `Solarized Dark`. click it to change the theme.

## Configure Powerlevel9k
to show more information on zsh, let's configure `Powerlevel9k`. you can see the screen like below, when you execute current iTerm.

![Development Environment on Mac - iterm](/assets/images/category/environment/mac-iterm-zsh/normal_iterm.png)

execute the command below to download `Powerlevel9k`.

```bash
git clone https://github.com/bhilburn/powerlevel9k.git ~/.oh-my-zsh/custom/themes/powerlevel9k
```

zsh's configuration file is `~/.zshrc`. open it and set Powerlevel9k.

```bash
vi ~/.zshrc
```

find the theme configuration.

```bash
# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/robbyrussell/oh-my-zsh/wiki/Themes
ZSH_THEME="robbyrussell"
```

change the theme from `ZSH_THEME="robbyrussell"` to `ZSH_THEME="powerlevel9k/powerlevel9k"` and save it.

to restart iTerm, you can see the screen like below.

![Development Environment on Mac - iterm powerlevel9k](/assets/images/category/environment/mac-iterm-zsh/powerlevel9k.png)

you can see user information and `?`. the question mark is shown up when the font is not set. click the link below to go to the font download site.

- [Meslo LG M Regular for Powerline.ttf](https://github.com/powerline/fonts/blob/master/Meslo%20Slashed/Meslo%20LG%20M%20Regular%20for%20Powerline.ttf){:rel="nofollow noreferrer" target="_blank"}

when you click the link above, you can see the screen lik below. click `View Raw` to download the font.

![Development Environment on Mac - iterm donwload font](/assets/images/category/environment/mac-iterm-zsh/download-font.png)

after downloading it, click the font file to execute it.

![Development Environment on Mac - iterm font installation](/assets/images/category/environment/mac-iterm-zsh/install-font.png)

click `Install Font` on the right bottom to install it. after installing, open Preference on iTerm again and click `Profiles` > `Text` > `Change Font`.

![Development Environment on Mac - iterm font installation](/assets/images/category/environment/mac-iterm-zsh/set-font.png)

select `Meslo LG M Regular for Powerline` what we downloaded above.

![Development Environment on Mac - iterm font installation check](/assets/images/category/environment/mac-iterm-zsh/check-font.png)

when you execute iTerm, you can see the screen like above.

I don't like to show my long username, so I configured it not showing up. execute the command below if you want to hide it.

```bash
vi ~/.zshrc
```

add the content below to the bottom.

```bash
prompt_context() {}
```

restart iTerm. you can see the user name not displayed.

![Development Environment on Mac - iterm hide user name](/assets/images/category/environment/mac-iterm-zsh/no-user-name.png)

## Connect vscode and zsh
in here, we'll set `code` command of vscode on zsh, and zsh to vscode's default terminal on vscode.

### Configure vscode command to zsh
execute the command below to open zsh configuration file.

```bash
vi ~/.zshrc
```

add the content below to the bottom of the settings file.

```bash
export PATH="$PATH:/Applications/Visual Studio Code.app/Contents/Resources/app/bin"
```

restart iTerm and execute the command below to check vscode activated.

```
code .
```

### Configure zsh to vscode
click `Code` > `Preferences` > `Settings` on the left top of the vscode.

![Development Environment on Mac - vscode zsh configuration](/assets/images/category/environment/mac-iterm-zsh/vscode-setting.png)

search `shell` and change `/bin/bash` to `/bin/zsh` on `Terminal > Integrated > Shell: Osx`.

![Development Environment on Mac - vscode zsh shell configuration](/assets/images/category/environment/mac-iterm-zsh/vscode-shell-setting.png)

also, search `fontfamily` and set `Meslo LG M for Powerline` on it like below.

![Development Environment on Mac - vscode zsh font 설정](/assets/images/category/environment/mac-iterm-zsh/vscode-zsh-font-setting.png)

after it, to execute Terminal on vscode, you can see zsh executed.

![Development Environment on Mac - vscode zsh configuration completed](/assets/images/category/environment/mac-iterm-zsh/vscode-zsh-font.png)
