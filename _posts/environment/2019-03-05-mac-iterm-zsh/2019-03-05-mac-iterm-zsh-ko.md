---
layout: 'post'
permalink: '/environment/mac-iterm-zsh/'
paginate_path: '/environment/:num/mac-iterm-zsh/'
lang: 'ko'
categories: 'environment'
comments: true

title: '맥(Mac) 개발 환경 구축(1) - iTerm과 zsh'
description: '새로운 맥(Mac)에 개발 환경을 구축하려고 합니다. 맥(Mac)에 iTerm와 zsh를 설정하여 새로운 터미널 환경을 구축합니다.'
image: '/assets/images/category/environment/mac-iterm-zsh/background.jpg'
---

## 개요
새로운 맥(Mac)에 개발 환경을 처음부터 구축한 내용을 정리하려고 합니다. 이 블로그는 연재물입니다. 개발 환경에 다른 부분을 확인하고 싶으신 분들은 아래에 내용을 참고하세요.

- [맥(Mac) 개발 환경 구축(1) - iTerm과 zsh]({{site.url}}/{{page.categories}}/mac-iterm-zsh/){:target="_blank"}
- [맥(Mac) 개발 환경 구축(2) - tools]({{site.url}}/{{page.categories}}/mac-development-tools/){:target="_blank"}
- [맥(Mac) 개발 환경 구축(3) - 개발 환경]({{site.url}}/{{page.categories}}/mac-development-environment/){:target="_blank"}

이번 블로그에서는 새로운 맥(Mac)에 [iTerm](https://www.iterm2.com/){:rel="nofollow noreferrer" target="_blank"}와 [zsh](https://github.com/robbyrussell/oh-my-zsh){:rel="nofollow noreferrer" target="_blank"}를 설정하는 방법에 대해서 알아봅니다.

- [iTerm](https://www.iterm2.com/){:rel="nofollow noreferrer" target="_blank"}
- [zsh](https://github.com/robbyrussell/oh-my-zsh){:rel="nofollow noreferrer" target="_blank"}



## iTerm 설치

아래에 링크를 통해 `iTerm` 다운로드 페이지로 이동합니다.

- iTerm 다운로드: [다운로드 페이지](https://www.iterm2.com/downloads.html){:rel="nofollow noreferrer" target="_blank"}

아래와 같이 화면이 보인다면, `Stable Releases`를 다운로드합니다.

![맥(mac) 개발환경 설정 - iTerm 다운로드](/assets/images/category/environment/mac-iterm-zsh/iterm-download.png)

다운로드 받은 `zip` 파일을 압축해제하고 설치합니다.

![맥(mac) 개발환경 설정 - iTerm full disk access 권한 요청](/assets/images/category/environment/mac-iterm-zsh/iterm-full-disk-access.png)

위와 같이 iTerm에서 `Full Disk Access`를 요청합니다. 오른쪽 하단의 `Open System Preferences`를 선택합니다.

![맥(mac) 개발환경 설정 - iTerm full disk access 권한 설정](/assets/images/category/environment/mac-iterm-zsh/iterm-full-disk-access-grant.png)

위와 같이 친절한 설명과 함께 `Security & Privacy`가 활성화 됩니다. 왼쪽 하단의 자물쇠 모양을 선택하고 암호를 입력하여 수정 가능한 상태를 만듭니다.

![맥(mac) 개발환경 설정 - iTerm full disk access 권한 설정 화면](/assets/images/category/environment/mac-iterm-zsh/iterm-full-disk-access-grant-setting.png)

상단 탭에서 `Privacy`를 선택하고, 왼쪽 리스트에서 `Full Disk Accesss`를 선택합니다.

![맥(mac) 개발환경 설정 - iTerm full disk access 권한 설정 iTerm 선택](/assets/images/category/environment/mac-iterm-zsh/iterm-full-disk-access-grant-setting-select-iterm.png)

오른쪽의 `+` 버튼을 누릅니다. `Applications`로 이동한 후, `iTerm`를 선택하고 `Open`을 선택합니다.

![맥(mac) 개발환경 설정 - iTerm 종료](/assets/images/category/environment/mac-iterm-zsh/iterm-full-disk-access-grant-setting-quit.png)

위와 같이 `iTerm` 종료 여부를 물어보면 `Quit Now` 버튼을 `iTerm`을 종료합니다.

iTerm을 실행하여 문제 없이 실행되는지 확인합니다.

## zsh

zsh는 터미널을 좀 더 사용하기 편하게 만들어 줍니다. 아래에 링크를 클릭하면 자세한 내용을 확인하실 수 있습니다.

- zsh 공식 사이트: [zsh](https://github.com/robbyrussell/oh-my-zsh){:rel="nofollow noreferrer" target="_blank"}

zsh 공식 사이트에 보면 설치 방법이 아래와 같이 나와 있습니다.

![맥(mac) 개발환경 설정 - zsh 설치](/assets/images/category/environment/mac-iterm-zsh/zsh-installation.png)

설치한 iTerm 또는 Terminal을 열고 아래에 명령어를 실행합니다.

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

설치가 완료되면 아래와 같은 화면을 볼 수 있습니다.

![맥(mac) 개발환경 설정 - zsh 설치 완료](/assets/images/category/environment/mac-iterm-zsh/zsh-install-completed.png)

## iTerm에서 zsh 디폴트 설정

iTerm은 기본 shell을 사용하도록 되어있습니다. iTerm이 기본적으로 zsh를 사용하도록 설정합니다.

![맥(mac) 개발환경 설정 - iTerm zsh 설정](/assets/images/category/environment/mac-iterm-zsh/zsh-install-completed.png)

iTerm을 실행하고 왼쪽 상단의 `iTerms2` > `Preferences...`를 선택합니다.

![맥(mac) 개발환경 설정 - iTerm zsh 디폴트 설정](/assets/images/category/environment/mac-iterm-zsh/iterm-zsh-default-setting-path.png)

위와 같이 설정 화면이 나오면, 상단에 `Profiles` 탭을 선택합니다. 오른쪽 중간에 있는 `Command` 설정에서 `Command`를 선택하고 `/bin/zsh`를 입력하고 종료합니다.

다시 iTerm을 시작하면 `zsh`가 기본으로 실행되는 것을 확인할 수 있습니다.

## iTerm테마 설정

iTerm는 많은 테마(Theme)를 가지고 있습니다. 여러분이 원하는 테마를 설정하여 사용하시면 됩니다. 여기에서는 `iterm2-solarized` 테마를 설정하는 방법을 소개합니다.

- [iterm2-solarized](https://gist.github.com/kevin-smets/8568070){:rel="nofollow noreferrer" target="_blank"}

아래에 링크를 클릭하여 테마를 다운로드합니다.

- [iterm2-solarized 다운로드](https://raw.githubusercontent.com/mbadolato/iTerm2-Color-Schemes/master/schemes/Solarized%20Dark%20-%20Patched.itermcolors){:rel="nofollow noreferrer" target="_blank"}

위에 링크를 선택하면 테마 파일 내용이 보입니다. `command + s`를 눌러 다운로드합니다.

![맥(mac) 개발환경 설정 - zsh 테마 설정](/assets/images/category/environment/mac-iterm-zsh/zsh-theme-setting.png)

다운로드시 하단의 `Format`을 `All Files`로 설정합니다. 파일명 확장자가 `.itermcolors`인지 확인합니다.

다시 iTerm의 Preferences를 엽니다.

![맥(mac) 개발환경 설정 - iterm에 zsh 테마 설정](/assets/images/category/environment/mac-iterm-zsh/zsh-theme-import.png)

위와 같이 `Profiles` > `Colors`를 선택하고 오른쪽 하단의 `Color Preset...` > `import...`를 선택합니다.

위에서 다운로드한 `Solarized Dark - Patched.itermcolors` 파일을 선택합니다.

![맥(mac) 개발환경 설정 - iterm에 zsh 테마 Solarized Dark 설정](/assets/images/category/environment/mac-iterm-zsh/zsh-theme-solarized-dark.png)

다시 `Color Preset...`을 선택하면 이전과 다르게 `Solarized Dark`가 추가된 것을 확인할 수 있습니다. `Solarized Dark`를 선택하여 테마를 설정합니다.

## Powerlevel9k 설정

터미널에 더 많은 정보를 보여주기위해 `Powerlevel9k`를 설정합니다. iTerm을 실행하면 지금은 아래와 같은 화면이 보입니다.

![맥(mac) 개발환경 설정 - iterm](/assets/images/category/environment/mac-iterm-zsh/normal_iterm.png)

아래에 명령어를 통해 `Powerlevel9k`를 다운로드합니다.

```bash
git clone https://github.com/bhilburn/powerlevel9k.git ~/.oh-my-zsh/custom/themes/powerlevel9k
```

zsh의 설정 파일은 `~/.zshrc`입니다. 이 파일을 열고 Powerlevel9k을 설정합니다.

```bash
vi ~/.zshrc
```

설정 파일에 테마 설정 부분을 찾습니다.

```bash
# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/robbyrussell/oh-my-zsh/wiki/Themes
ZSH_THEME="robbyrussell"
```

테마를 `ZSH_THEME="robbyrussell"`에서 `ZSH_THEME="powerlevel9k/powerlevel9k"`로 교체하고 저장합니다.

iTerm을 재시작하면 아래와 같은 화면을 볼 수 있습니다.

![맥(mac) 개발환경 설정 - iterm powerlevel9k](/assets/images/category/environment/mac-iterm-zsh/powerlevel9k.png)

위와 같이 유저 정보와 `?`가 보입니다. ?는 폰트가 설정되지 않았기 때문입니다. 아래에 링크를 눌러 폰트 다운로드 사이트로 이동합니다.

- [Meslo LG M Regular for Powerline.ttf](https://github.com/powerline/fonts/blob/master/Meslo%20Slashed/Meslo%20LG%20M%20Regular%20for%20Powerline.ttf){:rel="nofollow noreferrer" target="_blank"}

위에 링크를 누르면 아래와 같이 보입니다. `View Raw`를 눌러 폰트를 다운로드합니다.

![맥(mac) 개발환경 설정 - iterm 다운로드 폰트](/assets/images/category/environment/mac-iterm-zsh/download-font.png)

다운로드가 완료되면 다운로드한 폰트 파일을 선택하여 실행합니다.

![맥(mac) 개발환경 설정 - iterm 폰트 설치](/assets/images/category/environment/mac-iterm-zsh/install-font.png)

오른쪽 하단의 `Install Font`를 눌러 폰트를 설치합니다. 설치가 완료되면, 다시 iTerm의 Preference를 열고 `Profiles` > `Text` > `Change Font`를 선택합니다.

![맥(mac) 개발환경 설정 - iterm 폰트 설치](/assets/images/category/environment/mac-iterm-zsh/set-font.png)

위에서 다운로드한 `Meslo LG M Regular for Powerline`를 선택합니다.

![맥(mac) 개발환경 설정 - iterm 폰트 설치 확인](/assets/images/category/environment/mac-iterm-zsh/check-font.png)

iTerm을 확인하면 위와 같은 화면을 볼 수 있습니다.

저는 여기서 사용자 명이 길기때문에 사용자 명을 표시하지 않도록 설정하였습니다. 아래에 명령어를 실행합니다.

```bash
vi ~/.zshrc
```

아래에 내용을 제일 하단에 추가합니다.

```bash
prompt_context() {}
```

다시 iTerm을 실행하면 사용자명이 표시되지 않는 것을 확인할 수 있습니다.

![맥(mac) 개발환경 설정 - iterm 사용자명 숨김](/assets/images/category/environment/mac-iterm-zsh/no-user-name.png)

## vscode와의 연동

zsh에서 vscode의 `code` 명령어를 사용할 수 있게 설정하고 vscode에서는 기본 터미널을 zsh으로 설정하는 방법에 대해서 알아봅니다.

### zsh에 vscode 명령어 설정

아래의 명령어로 zsh설정을 엽니다.

```bash
vi ~/.zshrc
```

제일 하단에 아래에 내용을 추가합니다.

```bash
export PATH="$PATH:/Applications/Visual Studio Code.app/Contents/Resources/app/bin"
```

iTerm을 재시작하고 아래에 명령어로 vscode가 활성화되는지 확인합니다.

```
code .
```

### vscode에 zsh 설정

vscode를 실행하고 왼쪽 상단의 `Code` > `Preferences` > `Settings`를 선택합니다.

![맥(mac) 개발환경 설정 - vscode zsh 설정](/assets/images/category/environment/mac-iterm-zsh/vscode-setting.png)

검색창에 `shell`을 검색하고 `Terminal > Integrated > Shell: Osx` 부분을 `/bin/bash`에서 `/bin/zsh`로 교체합니다.

![맥(mac) 개발환경 설정 - vscode zsh shell설정](/assets/images/category/environment/mac-iterm-zsh/vscode-shell-setting.png)

또한 fontfamily를 검색하고 `Meslo LG M for Powerline`을 설정합니다.

![맥(mac) 개발환경 설정 - vscode zsh font 설정](/assets/images/category/environment/mac-iterm-zsh/vscode-zsh-font-setting.png)

이제 vscode를 실행하면 아래와 같이 zsh가 실행되는 것을 확인할 수 있습니다.

![맥(mac) 개발환경 설정 - vscode zsh 설정 완료](/assets/images/category/environment/mac-iterm-zsh/vscode-zsh-font.png)
