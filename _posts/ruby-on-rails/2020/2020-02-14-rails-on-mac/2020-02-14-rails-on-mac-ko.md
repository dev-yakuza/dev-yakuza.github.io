---
layout: 'post'
permalink: '/ruby-on-rails/rails-on-mac/'
paginate_path: '/ruby-on-rails/:num/rails-on-mac/'
lang: 'ko'
categories: 'ruby-on-rails'
comments: true

title: 'Mac에서 Ruby on Rails 시작하기'
description: 'Mac에서 Ruby on Rails를 설치하고 새로운 프로젝트를 시작하는 방법에 대해서 알아봅시다.'
image: '/assets/images/category/ruby-on-rails/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [Homebrew 설치](#homebrew-설치)
- [rbenv 설치하기](#rbenv-설치하기)
- [rbenv 초기화](#rbenv-초기화)
- [다른 버전의 Ruby 설치하기](#다른-버전의-ruby-설치하기)
  - [에러 대응](#에러-대응)
- [버전 변경하기](#버전-변경하기)
- [Bundler 설치하기](#bundler-설치하기)
- [Rails 설치하기](#rails-설치하기)
- [yarn 설치](#yarn-설치)
- [Rails 프로젝트 생성 및 확인](#rails-프로젝트-생성-및-확인)
- [완료](#완료)
- [참고](#참고)

</div>

## 개요

최근 Ruby on Rails를 사용하여 프로젝트를 진행하게 되었습니다. 이번 블로그 포스트에서는 `Ruby on Rails`를 Mac에 설치하는 방법과 설치된 Rails를 사용하여 프로젝트를 시작하는 방법에 대해서 알아보도록 하겠습니다.

- Rails 공식 사이트: [https://rubyonrails.org/](https://rubyonrails.org/){:rel="nofollow noreferrer" target="_blank"}

이 블로그 포스트는 시리즈로 제작되었습니다. 자세한 내용은 아래에 링크를 참고하시기 바랍니다.

- Mac에서 Ruby on Rails 시작하기
- [Ruby on Rails로 생성한 프로젝트의 폴더 구조]({{site.url}}/{{page.categories}}/folder-structure/){:target="_blank"}
- [Ruby on Rails를 사용하여 새로운 웹 페이지 만들기]({{site.url}}/{{page.categories}}/create-page/){:target="_blank"}
- [Controller와 View, Route에서 데이터 교환]({{site.url}}/{{page.categories}}/data-in-controller-view-route/){:target="_blank"}
- [Rails에서 DB 데이터 다루기]({{site.url}}/{{page.categories}}/database/){:target="_blank"}

여기서 사용한 소스코드는 Github에서 확인할 수 있습니다.

- [Github 소스코드](https://github.com/dev-yakuza/study-rails){:rel="nofollow noreferrer" target="_blank"}

## Homebrew 설치

Rails를 Mac에 설치하기 위해서 맥의 패키지 관리자인 `Homebrew`를 이용할 예정입니다. 우선 아래에 명령어로 Mac에 Homebrew가 설치되어있는지 확인합니다.

```bash
brew --version
```

이미 Homebrew가 Mac에 설치되었다면 아래와 같은 화면을 볼 수 있습니다.

```bash
Homebrew 2.2.6
Homebrew/homebrew-core (git revision 93ac3; last commit 2020-02-18)
Homebrew/homebrew-cask (git revision 373c1; last commit 2020-02-18)
```

위와 같은 화면이 나오시는 분들은 다음 단계로 진행하시기 바랍니다. 위와 같은 화면이 나오지 않는 분들은 아래에 명령어로 Homebrew를 설치합니다.

```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

설치가 완료되면 아래에 명령어를 실행하여 설치가 잘 되었는지 확인합니다.

```bash
brew --version
```

설치가 완료되었다면 아래와 같은 화면을 볼 수 있습니다.

```bash
Homebrew 2.2.6
Homebrew/homebrew-core (git revision 93ac3; last commit 2020-02-18)
Homebrew/homebrew-cask (git revision 373c1; last commit 2020-02-18)
```

{% include in-feed-ads.html %}

## rbenv 설치하기

Mac에는 기본적으로 `Ruby`가 설치되어있습니다. 따라서 바로 Rails를 설치해도 되지만, 다양한 Ruby 버전에 대응하기 위해 루비 버전 관리자인 `rbenv`을 설치합니다.

아래에 명령어를 실행하여 rbenv를 설치합니다.

```bash
brew install rbenv ruby-build
```

설치가 완료되면 아래와 같은 화면을 볼 수 있습니다.

```bash
==> Pouring rbenv-1.1.2.catalina.bottle.tar.gz
🍺  /usr/local/Cellar/rbenv/1.1.2: 36 files, 69KB
==> Caveats
==> ruby-build
ruby-build installs a non-Homebrew OpenSSL for each Ruby version installed and these are never upgraded.

To link Rubies to Homebrew's OpenSSL 1.1 (which is upgraded) add the following
to your ~/.zshrc:
  export RUBY_CONFIGURE_OPTS="--with-openssl-dir=$(brew --prefix openssl@1.1)"

Note: this may interfere with building old versions of Ruby (e.g <2.4) that use
OpenSSL <1.1.
```

그리고 위에서 나온 것처럼 `.zshrc` 파일을 열고 아래와 같이 수정합니다.

```bash
# code ~/.zshrc
export RUBY_CONFIGURE_OPTS="--with-openssl-dir=$(brew --prefix openssl@1.1)"
```

## rbenv 초기화

rbenv의 설치가 완료되었다면 아래에 명령어를 실행하여 rbenv을 초기화한다.

```bash
rbenv init
```

위에 명령어를 실행하면 아래와 같은 화면을 볼 수 있다.

```bash
# Load rbenv automatically by appending
# the following to ~/.zshrc:

eval "$(rbenv init -)"
```

위에 설명과 같이 `.zshrc` 파일을 열고 아래와 같이 수정한다.

```bash
# code ~/.zshrc
eval "$(rbenv init -)"
```

모든 설정이 제대로 되었는지 확인하기 위해 아래에 명령어를 실행한다.

```bash
curl -fsSL https://github.com/rbenv/rbenv-installer/raw/master/bin/rbenv-doctor | bash
```

실행이 완료되면 아래와 같은 화면을 볼 수 있다.

```bash
Checking for `rbenv' in PATH: /usr/local/bin/rbenv
Checking for rbenv shims in PATH: OK
Checking `rbenv install' support: /usr/local/bin/rbenv-install (ruby-build 20200115)
Counting installed Ruby versions: none
  There aren't any Ruby versions installed under `/Users/jeonghean_kim/.rbenv/versions'.
  You can install Ruby versions like so: rbenv install 2.2.4
Checking RubyGems settings: OK
Auditing installed plugins: OK
```

## 다른 버전의 Ruby 설치하기

Mac에 다른 버전의 Ruby를 설치하는 방법에 대해서 알아봅시다. 우선 아래에 명령어를 실행하여 현재 Ruby의 버전을 확인합니다.

```bash
ruby -v
```

위에 명령어를 실행하면 아래와 같은 화면을 볼 수 있습니다.

```bash
ruby 2.6.3p62 (2019-04-16 revision 67580) [universal.x86_64-darwin19]
```

아래에 명령어를 사용하여 rbenv를 이용하여 설치 가능한 Ruby의 버전을 확인합니다.

```bash
rbenv install -l
```

위에 명령어를 실행하면 아래와 같이 Ruby의 버전 리스트를 확인할 수 있습니다.

```bash
...
truffleruby-1.0.0-rc3
truffleruby-1.0.0-rc5
truffleruby-1.0.0-rc6
truffleruby-1.0.0-rc7
truffleruby-1.0.0-rc8
truffleruby-1.0.0-rc9
truffleruby-19.0.0
truffleruby-19.1.0
truffleruby-19.2.0
truffleruby-19.2.0.1
truffleruby-19.3.0
truffleruby-19.3.0.2
truffleruby-19.3.1
```

Ruby 버전 리스트가 너무 많기 때문에, 아래에 명령어를 실행하여 가장 최신의 안정된(Stable) Ruby 버전을 검색합니다.

```bash
rbenv install -l | sed -n '/^[[:space:]]*[0-9]\{1,\}\.[0-9]\{1,\}\.[0-9]\{1,\}[[:space:]]*$/ h;${g;p;}'
```

그러면 아래와 같은 결과를 얻을 수 있습니다.

```bash
2.7.0
```

아래에 명령어로 최신 버전의 루비를 설치합니다.

```bash
rbenv install 2.7.0
```

또는 아래의 명령어로 항상 최신 버전의 루비를 설치할 수 있습니다.

```bash
rbenv install $(rbenv install -l | sed -n '/^[[:space:]]*[0-9]\{1,\}\.[0-9]\{1,\}\.[0-9]\{1,\}[[:space:]]*$/ h;${g;p;}')
```

물론, 이전 버전도 설치가 가능합니다.

```bash
rbenv install 2.3.1
```

설치가 완료되면 아래에 명령어를 실행하여 새로운 환경을 재설정합니다.

```bash
rbenv rehash
```

### 에러 대응

저는 설치중에 아래와 같은 에러가 나왔습니다.

```bash
Last 10 log lines:
checking for inttypes.h... yes
checking for stdint.h... yes
checking for unistd.h... yes
checking minix/config.h usability... no
checking minix/config.h presence... no
checking for minix/config.h... no
checking whether it is safe to define __EXTENSIONS__... yes
checking for cd using physical directory... cd -P
checking whether CFLAGS is valid... no
configure: error: something wrong with CFLAGS="-I/usr/local/include -L/usr/local/lib  "
```

아래와 같이 `./zshrc`를 수정하여 해결하였습니다.

```bash
# code ~/.zshrc
export CFLAGS=""
```

{% include in-feed-ads.html %}

## 버전 변경하기

아래에 명령어를 실행하여 현재 설치된 Ruby의 버전을 확인합니다.

```bash
rbenv versions
```

위에 명령어를 실행하면 아래와 같은 결과를 확인할 수 있습니다.

```bash
* system (set by /Users/jeonghean_kim/.rbenv/version)
  2.7.0
```

앞에 `*` 마크가 있는 버전이 현재 선택된 버전입니다.

아래에 명령어를 실행하여 Ruby 버전을 다시 한번 확인할 수 있습니다.

```bash
ruby -v
# ruby 2.6.3p62 (2019-04-16 revision 67580) [universal.x86_64-darwin19]
```

그럼 아래에 명령어를 실행하여 Ruby 버전을 변경한다.

```bash
rbenv global 2.7.0
rbenv rehash
```

그리고 아래에 명령어를 실행하여 버전을 확인해 보면, Ruby 버전이 변경된 것을 확인할 수 있다.

```bash
ruby -v
# ruby 2.7.0p0 (2019-12-25 revision 647ee6f091) [x86_64-darwin19]
rbenv versions
#   system (set by /Users/jeonghean_kim/.rbenv/version)
# * 2.7.0
```

## Bundler 설치하기

Ruby의 `Gem`을 관리하는 `Bundler`를 설치합니다. Gem은 Ruby의 일종의 라이브러리, 패키지들이라고 생각하면 됩니다. Bundler는 이런 라이브러리, 패키지들을 쉽게 설치하고 관리하게 도와줍니다.

아래에 명령어로 Bundler를 설치합니다.

```bash
gem install bundler
```

설치가 끝나면, 아래에 명령어를 실행하여 제대로 설치되었는지 확인합니다.

```bash
bundler -v
# Bundler version 2.1.4
```

## Rails 설치하기

이제 `Rails`를 설치해 봅시다. 아래에 명령어를 사용하여 Rails를 설치합니다.

```bash
gem install rails
rbenv rehash
```

설치가 완료되면 아래에 명령어를 사용하여 Rails가 잘 설치되었는지 확인합니다.

```bash
rails -v
# Rails 6.0.2.1
```

## yarn 설치

Rails 프로젝트를 생성, 실행하기 위해서는 `yarn`의 설치가 필요하다. yarn은 자바스크립트 라이브러리를 설치하거나, 관리할 때 사용합니다.

아래에 명령어를 사용하여 yarn을 설치하도록 한다.

```bash
brew install yarn
```

{% include in-feed-ads.html %}

## Rails 프로젝트 생성 및 확인

이제 설치된 Rails를 사용하여 Rails 프로젝트를 생성해 봅시다. 아래에 명령어를 사용하여 새로운 Rails 프로젝트를 생성합니다.

```bash
rails new StudyRails
```

프로젝트 생성중 아래와 같은 메세지가 보인다면,

```bash
The dependency tzinfo-data (>= 0) will be unused by any of the platforms Bundler is installing for. Bundler is installing for ruby but the dependency is only for x86-mingw32, x86-mswin32, x64-mingw32, java. To add those platforms to the bundle, run `bundle lock --add-platform x86-mingw32 x86-mswin32 x64-mingw32 java`.
```

프로젝트 생성이 끝나면, 아래와 같이 명령어를 실행합니다.

```bash
cd StudyRails
bundle lock --add-platform x86-mingw32 x86-mswin32 x64-mingw32 java
bundle install
```

만약 아래와 같은 에러 메세지가 나온다면,

```bash
Your Ruby version is 2.6.3, but your Gemfile specified 2.7.0
```

bundle의 Path가 잘 인식이 되지 않기 때문입니다. 저는 이 문제를 해결하기 위해서 `.zshrc` 파일에 아래에 내용을 추가하였습니다.

```bash
# code ~/.zshrc
alias bundler=/Users/$USER/.rbenv/shims/bundler
alias ruby=/Users/$USER/.rbenv/shims/ruby
alias bundle=/Users/$USER/.rbenv/shims/bundle
alias gem=/Users/$USER/.rbenv/shims/gem
alias rails=/Users/$USER/.rbenv/shims/rails
```

생성이 완료되었다면, 아래에 명령어를 사용하여 Rails 프로젝트를 실행해 봅니다.

```bash
# cd StudyRails
bundle exec rails server
```

만약 아래와 같은 경고가 나온다면,

```bash
Warning: the running version of Bundler (2.1.2) is older than the version that created the lockfile (2.1.4). We suggest you to upgrade to the version that created the lockfile by running `gem install bundler:2.1.4`.
```

아래에 명령어로 실행해 보시길 바랍니다.

```bash
bundle exec rails server
```

실행이 완료되었다면 브라우저를 사용하여 `http://127.0.0.1:3000/`으로 이동해 봅니다.

![Ruby on Rails 서버 실행 결과](/assets/images/category/ruby-on-rails/2020/rails-on-mac/rails-server.jpg)

이상없이 진행하였다면 위와 같이 Rails의 초기화면을 확인할 수 있습니다.

## 완료

이것으로 Rails 프로젝트를 시작하기 위해, Ruby 버전을 변경하고 Rails를 설치하는 방법에 대해서 알아보았습니다. 저는 간단하게 설정될 줄 알았는데, 이전에 jekyll 블로그 때문에 `.zshrc`에 설정한 Path 때문에 한참 고생했네요.

```bash
export GEM_HOME=$HOME/gems
export PATH=$HOME/gems/bin:$PATH
```

여러분도 혹시 문제가 발생하신다면, zshrc에 이상한 Path가 설정이 되어있나 확인해 보시는 것을 권장합니다. 이제 Rails로 프로젝트를 진행해 봅시다!

## 참고

이 블로그 포스트는 시리즈로 제작되었습니다. 자세한 내용은 아래에 링크를 참고하시기 바랍니다.

- Mac에서 Ruby on Rails 시작하기
- [Ruby on Rails로 생성한 프로젝트의 폴더 구조]({{site.url}}/{{page.categories}}/folder-structure/){:target="_blank"}
- [Ruby on Rails를 사용하여 새로운 웹 페이지 만들기]({{site.url}}/{{page.categories}}/create-page/){:target="_blank"}
- [Controller와 View, Route에서 데이터 교환]({{site.url}}/{{page.categories}}/data-in-controller-view-route/){:target="_blank"}
- [Rails에서 DB 데이터 다루기]({{site.url}}/{{page.categories}}/database/){:target="_blank"}

여기서 사용한 소스코드는 Github에서 확인할 수 있습니다.

- [Github 소스코드](https://github.com/dev-yakuza/study-rails){:rel="nofollow noreferrer" target="_blank"}
