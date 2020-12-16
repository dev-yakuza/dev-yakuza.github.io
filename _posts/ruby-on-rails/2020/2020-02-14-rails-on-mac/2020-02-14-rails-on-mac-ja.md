---
layout: 'post'
permalink: '/ruby-on-rails/rails-on-mac/'
paginate_path: '/ruby-on-rails/:num/rails-on-mac/'
lang: 'ja'
categories: 'ruby-on-rails'
comments: true

title: 'MacでRuby on Railsを始める'
description: 'MacにRuby on Railsをインストールして、新いプロジェクトを始める方法について説明します。'
image: '/assets/images/category/ruby-on-rails/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [Homebrewインストール](#homebrewインストール)
- [rbenvインストール](#rbenvインストール)
- [rbenv初期化](#rbenv初期化)
- [他のバージョンのRubyをインストール](#他のバージョンのrubyをインストール)
  - [エラー対応](#エラー対応)
- [バージョン変更](#バージョン変更)
- [Bundlerインストール](#bundlerインストール)
- [Railsインストール](#railsインストール)
- [yarnインストール](#yarnインストール)
- [Railsプロジェクトの生成や確認](#railsプロジェクトの生成や確認)
- [完了](#完了)
- [参考](#参考)

</div>

## 概要

最近Ruby on Railsを使ってプロジェクトを進めることになりました。このブログポストでは`Ruby on Rails`をMacにインストールする方法とインストールしたRailsを使ってプロジェクトを始める方法について説明します。

- Rails公式サイト: [https://rubyonrails.org/](https://rubyonrails.org/){:rel="nofollow noreferrer" target="_blank"}

このブログポストはシリーズで作成されてます。詳しく内容は下記のリンクを参考してください。

- MacでRuby on Railsを始める
- [Railsで作ったプロジェクトのフォルダ構造]({{site.url}}/{{page.categories}}/folder-structure/){:target="_blank"}
- [Ruby on Railsを使って新しウェブページを作る]({{site.url}}/{{page.categories}}/create-page/){:target="_blank"}
- [ControllerとView、Routeとのデータ交換]({{site.url}}/{{page.categories}}/data-in-controller-view-route/){:target="_blank"}
- [RailsでDBを使う方法]({{site.url}}/{{page.categories}}/database/){:target="_blank"}

ここで使ったソースコードはGithubで確認できます。

- [Github ソースコード](https://github.com/dev-yakuza/study-rails){:rel="nofollow noreferrer" target="_blank"}

## Homebrewインストール

RailsをMacにインストールするためにはMacのパッケージ管理者である`Homebrew`を使え予定です。まず、下記のコマンドで、MacにHomebrewがインストールされたか確認します。

```bash
brew --version
```

既にHomebrewがMacにインストールされたら下記のような画面をみることができます。

```bash
Homebrew 2.2.6
Homebrew/homebrew-core (git revision 93ac3; last commit 2020-02-18)
Homebrew/homebrew-cask (git revision 373c1; last commit 2020-02-18)
```

上のような画面がかでる方は、次のステップに進んでください。上のような画面が出ない方は、下記のコマンドでHomebrewをインストールします。

```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

インストールが終わったら、下記のコマンドを実行してインストールがされたか確認します。

```bash
brew --version
```

インストールされたら、下記のような画面が見えます。

```bash
Homebrew 2.2.6
Homebrew/homebrew-core (git revision 93ac3; last commit 2020-02-18)
Homebrew/homebrew-cask (git revision 373c1; last commit 2020-02-18)
```

{% include in-feed-ads.html %}

## rbenvインストール

Macには基本的`Ruby`がインストールされております。だから、すぐRailsをインストールしてもいいですが、色んなRubyのバージョンを使うため、ルビバージョン管理者である`rbenv`をインストールします。

下記のコマンドを実行してrbenvをインストールします。

```bash
brew install rbenv ruby-build
```

インストールが終わったら下記のような画面が見えます。

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

そして、上で出たように`.zshrc`を開いて下記の内容を追加します。

```bash
# code ~/.zshrc
export RUBY_CONFIGURE_OPTS="--with-openssl-dir=$(brew --prefix openssl@1.1)"
```

## rbenv初期化

rbenvのインストールが終わったら、下記のコマンドを実行してrbenvを初期化します。

```bash
rbenv init
```

上のコマンドを実行したら下記のような画面が見えます。

```bash
# Load rbenv automatically by appending
# the following to ~/.zshrc:

eval "$(rbenv init -)"
```

上の説明通り、`.zshrc`ファイルを開いて下記の内容を追加します。

```bash
# code ~/.zshrc
eval "$(rbenv init -)"
```

全ての設定がうまくできたか確認するため下記のコマンドを実行します。

```bash
curl -fsSL https://github.com/rbenv/rbenv-installer/raw/master/bin/rbenv-doctor | bash
```

実行が終わったら、下記のような画面が確認できます。

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

## 他のバージョンのRubyをインストール

Macに他のバージョンのRubyをインストールする方法について見てみましょう。まず、下記のコマンドを実行して現在のRubyのバージョンを確認します。

```bash
ruby -v
```

上のコマンドを実行したら下記のような画面が見えます。

```bash
ruby 2.6.3p62 (2019-04-16 revision 67580) [universal.x86_64-darwin19]
```

下記のコマンドを使ってrbenvを使ってインストールできるRubyのバージョンを確認します。

```bash
rbenv install -l
```

上のコマンドを実行したら、下記のようなRubyのバージョンリストが確認できます。

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

Rubyのバージョンリストが多いなので、下記のコマンドを実行して一番最新の安定(Stable)されたRubyのバージョンを検索します。

```bash
rbenv install -l | sed -n '/^[[:space:]]*[0-9]\{1,\}\.[0-9]\{1,\}\.[0-9]\{1,\}[[:space:]]*$/ h;${g;p;}'
```

そしたら、下記のような結果が見えます。

```bash
2.7.0
```

下記のコマンドで一番最新のRubyをインストールします。

```bash
rbenv install 2.7.0
```

または、下記のコマンドでいつも、最新のRubyをインストールすることができます。

```bash
rbenv install $(rbenv install -l | sed -n '/^[[:space:]]*[0-9]\{1,\}\.[0-9]\{1,\}\.[0-9]\{1,\}[[:space:]]*$/ h;${g;p;}')
```

もちろん、古いバージョンもインストールできます。

```bash
rbenv install 2.3.1
```

インストールが終わったら、下記のコマンドを実行して新い環境を再設定します。

```bash
rbenv rehash
```

### エラー対応

私はインストール中、下記のエラーが出ました。

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

下記のように`./zshrc`を修正して解決しました。

```bash
# code ~/.zshrc
export CFLAGS=""
```

{% include in-feed-ads.html %}

## バージョン変更

下記のコマンドを実行して現在インストールされたRubyのバージョンを確認します。

```bash
rbenv versions
```

上のコマンドを実行したら下記のような結果が見えます。

```bash
* system (set by /Users/jeonghean_kim/.rbenv/version)
  2.7.0
```

前に`*`マークがついてるバージョンが現在選択されたバージョンになります。

下記のコマンドを実行してRubyのバージョンをもう一度確認します。

```bash
ruby -v
# ruby 2.6.3p62 (2019-04-16 revision 67580) [universal.x86_64-darwin19]
```

それで、下記のコマンドを実行してRubyのバージョンを変更します。

```bash
rbenv global 2.7.0
rbenv rehash
```

そして下記のコマンドを実行してバージョンを確認してみると、Rubyのバージョンが変わったことが確認できます。

```bash
ruby -v
# ruby 2.7.0p0 (2019-12-25 revision 647ee6f091) [x86_64-darwin19]
rbenv versions
#   system (set by /Users/jeonghean_kim/.rbenv/version)
# * 2.7.0
```

## Bundlerインストール

Rubyの`Gem`を管理する`Bundler`をインストールします。GemはRubyのライブラリ、パッケージと考えるといいと思います。Bundlerはこのようなライブラリ、パッケージを簡単にインストールや管理することができるようにしてくれます。

下記のコマンドでBundlerをインストールします。

```bash
gem install bundler
```

インストールが終わったら、下記のコマンドを実行してBundlerがうまくインストールされたか確認します。

```bash
bundler -v
# Bundler version 2.1.4
```

## Railsインストール

今度は`Rails`をインストールしてみます。下記のコマンドを使ってRailsをインストールします。

```bash
gem install rails
rbenv rehash
```

インストールが終わったら、下記のコマンドを使ってRailsがうまくインストールされたか確認します。

```bash
rails -v
# Rails 6.0.2.1
```

## yarnインストール

Railsプロジェクトを生成、実行するためには`yarn`のインストールが必要です。yarnはjavascriptのライブラリをインストールや管理する時使うものになります。

下記のコマンドを使ってyarnをインストールします。

```bash
brew install yarn
```

{% include in-feed-ads.html %}

## Railsプロジェクトの生成や確認

インストールしたRailsを使ってRailsプロジェクトを生成してみましょう。下記のコマンドを使って新いRailsプロジェクトを生成します。

```bash
rails new StudyRails
```

プロジェクトを生成中に下記のようなメッセージが見える方は、

```bash
The dependency tzinfo-data (>= 0) will be unused by any of the platforms Bundler is installing for. Bundler is installing for ruby but the dependency is only for x86-mingw32, x86-mswin32, x64-mingw32, java. To add those platforms to the bundle, run `bundle lock --add-platform x86-mingw32 x86-mswin32 x64-mingw32 java`.
```

プロジェクトの生成が終わった後、下記のコマンドを実行します。

```bash
cd StudyRails
bundle lock --add-platform x86-mingw32 x86-mswin32 x64-mingw32 java
bundle install
```

もし、下記のようなエラーメッセージが表示されると、

```bash
Your Ruby version is 2.6.3, but your Gemfile specified 2.7.0
```

bundleのPathがうまく認識されないので、問題が発生します。私はこの問題を解決するため、`.zshrc`ファイルに下記の内容を追加しました。

```bash
# code ~/.zshrc
alias bundler=/Users/$USER/.rbenv/shims/bundler
alias ruby=/Users/$USER/.rbenv/shims/ruby
alias bundle=/Users/$USER/.rbenv/shims/bundle
alias gem=/Users/$USER/.rbenv/shims/gem
alias rails=/Users/$USER/.rbenv/shims/rails
```

生成が終わったら、下記のコマンドでRailsプロジェクトを実行します。

```bash
# cd StudyRails
bundle exec rails server
```

もし下記のようなワーニングがでったら、

```bash
Warning: the running version of Bundler (2.1.2) is older than the version that created the lockfile (2.1.4). We suggest you to upgrade to the version that created the lockfile by running `gem install bundler:2.1.4`.
```

下記のコマンドで実行してみてください。

```bash
bundle exec rails server
```

実行が終わったら、ブラウザを使って`http://127.0.0.1:3000/`に移動してみます。

![Ruby on Rails サーバー実行結果](/assets/images/category/ruby-on-rails/2020/rails-on-mac/rails-server.jpg)

問題なく進めたら、上のようにRailsの初期画面を確認することができます。

## 完了

これでRailsプロジェクトを始めるため、Rubyのバージョンを変えってRailsをインストールする方法についてみてみました。私は簡単に設定できると思いましたが、以前jekyllのブログのため、`.zshrc`に設定したPathの問題で結構黒しました。

```bash
export GEM_HOME=$HOME/gems
export PATH=$HOME/gems/bin:$PATH
```

皆さんももし、変な問題が発生したら、zshrcに変なPathが設定されたか確認してみてください。これでRailsを進めてみましょう！

## 参考

このブログポストはシリーズで作成されてます。詳しく内容は下記のリンクを参考してください。

- MacでRuby on Railsを始める
- [Railsで作ったプロジェクトのフォルダ構造]({{site.url}}/{{page.categories}}/folder-structure/){:target="_blank"}
- [Ruby on Railsを使って新しウェブページを作る]({{site.url}}/{{page.categories}}/create-page/){:target="_blank"}
- [ControllerとView、Routeとのデータ交換]({{site.url}}/{{page.categories}}/data-in-controller-view-route/){:target="_blank"}
- [RailsでDBを使う方法]({{site.url}}/{{page.categories}}/database/){:target="_blank"}

ここで使ったソースコードはGithubで確認できます。

- [Github ソースコード](https://github.com/dev-yakuza/study-rails){:rel="nofollow noreferrer" target="_blank"}