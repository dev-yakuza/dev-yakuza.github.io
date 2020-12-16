---
layout: 'post'
permalink: '/ruby-on-rails/rails-on-mac/'
paginate_path: '/ruby-on-rails/:num/rails-on-mac/'
lang: 'en'
categories: 'ruby-on-rails'
comments: true

title: Start Ruby on Rails on Mac
description: Let's see how to install Ruby on Rails and start a project on Mac.
image: '/assets/images/category/ruby-on-rails/background.jpg'
---

<div id="contents_list" markdown="1">

## Content

- [Outline](#outline)
- [Install Homebrew](#install-homebrew)
- [Install rbenv](#install-rbenv)
- [Initialize rbenv](#initialize-rbenv)
- [Install other versions of Ruby](#install-other-versions-of-ruby)
  - [Fix Error](#fix-error)
- [Change version](#change-version)
- [Install Bundler](#install-bundler)
- [Install Rails](#install-rails)
- [Install yarn](#install-yarn)
- [Create and start Rails project](#create-and-start-rails-project)
- [Completed](#completed)
- [Reference](#reference)

</div>

## Outline

Recently, I have a chance to start Rub on Rails project. In this blog post, I will introduce how to install `Ruby on Rails` on Mac and start a project with installed Rails.

- Rails Official Site: [https://rubyonrails.org/](https://rubyonrails.org/){:rel="nofollow noreferrer" target="_blank"}

This blog post is a series. You can see the other posts in below.

- Start Ruby on Rails on Mac
- [Folder structure in Ruby on Rails]({{site.url}}/{{page.categories}}/folder-structure/){:target="_blank"}
- [Add new web page by Ruby on Rails]({{site.url}}/{{page.categories}}/create-page/){:target="_blank"}
- [Exchange Data between Controller, View and Route]({{site.url}}/{{page.categories}}/data-in-controller-view-route/){:target="_blank"}
- [Use DB on Rails]({{site.url}}/{{page.categories}}/database/){:target="_blank"}

Also, you can see the this blog post sample source code on Github

- [Github source code](https://github.com/dev-yakuza/study-rails){:rel="nofollow noreferrer" target="_blank"}

## Install Homebrew

We will use Mac pacakge manger `Homebrew` to install Rails on Mac. execute the command below to check Homebrew installed on Mac.

```bash
brew --version
```

If Homebrew was installed already, you can see the result below.

```bash
Homebrew 2.2.6
Homebrew/homebrew-core (git revision 93ac3; last commit 2020-02-18)
Homebrew/homebrew-cask (git revision 373c1; last commit 2020-02-18)
```

If you get the result above, go to the next step. If you don't get it, execute the command below to install Homebrew.

```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

After installing, execute the command below to check Homebrew installed.

```bash
brew --version
```

If Homebrew was installed well, you can see the result below.

```bash
Homebrew 2.2.6
Homebrew/homebrew-core (git revision 93ac3; last commit 2020-02-18)
Homebrew/homebrew-cask (git revision 373c1; last commit 2020-02-18)
```

{% include in-feed-ads.html %}

## Install rbenv

Mac has basically `Ruby`. So, you can install Rails directly, but to support various versions of Ruby, we'll install `rbenv` that is ruby version manager.

Execute the command below to install rbenv.

```bash
brew install rbenv ruby-build
```

After installing, you can see the result below.

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

And then, following the above, open `.zshrc` file and modify it like below.

```bash
# code ~/.zshrc
export RUBY_CONFIGURE_OPTS="--with-openssl-dir=$(brew --prefix openssl@1.1)"
```

## Initialize rbenv

After installing rbenv, execute the command below to initialize rbenv.

```bash
rbenv init
```

After executing the command, you can see the result below.

```bash
# Load rbenv automatically by appending
# the following to ~/.zshrc:

eval "$(rbenv init -)"
```

Following the above, open `.zshrc` file and modify it like below.

```bash
# code ~/.zshrc
eval "$(rbenv init -)"
```

After all settings, execute the command below to check all configuration are set well.

```bash
curl -fsSL https://github.com/rbenv/rbenv-installer/raw/master/bin/rbenv-doctor | bash
```

After executing, you can see the result below.

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

## Install other versions of Ruby

Let's see how to install another version of Ruby on Mac. First, execute the command below to check current Ruby version.

```bash
ruby -v
```

After executing, you can see the screen below.

```bash
ruby 2.6.3p62 (2019-04-16 revision 67580) [universal.x86_64-darwin19]
```

Execute the command below to check Ruby versions that we can install via rbenv.

```bash
rbenv install -l
```

After executing, you can see Ruby version list like below.

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

There are so many versions, so execute the command below to get recent stable Ruby version.

```bash
rbenv install -l | sed -n '/^[[:space:]]*[0-9]\{1,\}\.[0-9]\{1,\}\.[0-9]\{1,\}[[:space:]]*$/ h;${g;p;}'
```

And then, you can see the result below.

```bash
2.7.0
```

Execute the command below to install recent stable Ruby.

```bash
rbenv install 2.7.0
```

Also, you can directly install recent stable Ruby via executing the command below.

```bash
rbenv install $(rbenv install -l | sed -n '/^[[:space:]]*[0-9]\{1,\}\.[0-9]\{1,\}\.[0-9]\{1,\}[[:space:]]*$/ h;${g;p;}')
```

Of course, you can install old version Ruby.

```bash
rbenv install 2.3.1
```

After installing, execute the command below to re-configuration new environment.

```bash
rbenv rehash
```

### Fix Error

I got the error message like below when I installed.

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

I've fixed it to modify `./zshrc` file like below.

```bash
# code ~/.zshrc
export CFLAGS=""
```

{% include in-feed-ads.html %}

## Change version

First, execute the command below to check current Ruby version.

```bash
rbenv versions
```

You can see the result like below.

```bash
* system (set by /Users/jeonghean_kim/.rbenv/version)
  2.7.0
```

The `*` mark is currently selected Ruby version.

You can execute the command below to check Ruby version again.

```bash
ruby -v
# ruby 2.6.3p62 (2019-04-16 revision 67580) [universal.x86_64-darwin19]
```

Execute the command below to change Ruby version.

```bash
rbenv global 2.7.0
rbenv rehash
```

And then execute the command below to check version. you can see the version is changed

```bash
ruby -v
# ruby 2.7.0p0 (2019-12-25 revision 647ee6f091) [x86_64-darwin19]
rbenv versions
#   system (set by /Users/jeonghean_kim/.rbenv/version)
# * 2.7.0
```

## Install Bundler

Let's install `Bundler` which is Ruby `Gem` manager. Gem is kind of libraries(packages). Bundler installs and manages the libraries(packages).

Execute the command below to install Bundler.

```bash
gem install bundler
```

After installing, execute the command below to check Bundler installed well.

```bash
bundler -v
# Bundler version 2.1.4
```

## Install Rails

Let's install `Rails`. Execute the command below to install Rails.

```bash
gem install rails
rbenv rehash
```

After installing, you can check Rails install well via executing the command below.

```bash
rails -v
# Rails 6.0.2.1
```

## Install yarn

For creating Rails project and executing it, we need to install `yarn`. yarn is kind of manager to install javascript libraries and manage them.

Execute the command below to install yarn

```bash
brew install yarn
```

{% include in-feed-ads.html %}

## Create and start Rails project

Let's make Rails project. Execute the command below to create new Rails project.

```bash
rails new StudyRails
```

If you got the message like below, when you create Rails project,

```bash
The dependency tzinfo-data (>= 0) will be unused by any of the platforms Bundler is installing for. Bundler is installing for ruby but the dependency is only for x86-mingw32, x86-mswin32, x64-mingw32, java. To add those platforms to the bundle, run `bundle lock --add-platform x86-mingw32 x86-mswin32 x64-mingw32 java`.
```

After creating, execute the command below.

```bash
cd StudyRails
bundle lock --add-platform x86-mingw32 x86-mswin32 x64-mingw32 java
bundle install
```

If you get the error message like below,

```bash
Your Ruby version is 2.6.3, but your Gemfile specified 2.7.0
```

The reason is bundle path is not recognized well. I solved it to add the contents below to `.zshrc` file.

```bash
# code ~/.zshrc
alias bundler=/Users/$USER/.rbenv/shims/bundler
alias ruby=/Users/$USER/.rbenv/shims/ruby
alias bundle=/Users/$USER/.rbenv/shims/bundle
alias gem=/Users/$USER/.rbenv/shims/gem
alias rails=/Users/$USER/.rbenv/shims/rails
```

After creating, execute the command bewlot to start Rails project.

```bash
# cd StudyRails
bundle exec rails server
```

If you get the message like below,

```bash
Warning: the running version of Bundler (2.1.2) is older than the version that created the lockfile (2.1.4). We suggest you to upgrade to the version that created the lockfile by running `gem install bundler:2.1.4`.
```

Execute the commnad below.

```bash
bundle exec rails server
```

After running the server, you can go to `http://127.0.0.1:3000/` on the browser.

![Ruby on Rails result of running the server](/assets/images/category/ruby-on-rails/2020/rails-on-mac/rails-server.jpg)

If you have no problem, you can see Rails page like above.

## Completed

We've seen how to change Ruby version and install Rails to start Rails project. I thought the setting is simple, but I'v had many problem because of path setting on `.zshrc` for jekyll blog.

```bash
export GEM_HOME=$HOME/gems
export PATH=$HOME/gems/bin:$PATH
```

If you have some problem, I recommand you to check zshrc and delete wrong path setting. Now, let's play with Rails project!

## Reference

This blog post is a series. You can see the other posts in below.

- Start Ruby on Rails on Mac
- [Folder structure in Ruby on Rails]({{site.url}}/{{page.categories}}/folder-structure/){:target="_blank"}
- [Add new web page by Ruby on Rails]({{site.url}}/{{page.categories}}/create-page/){:target="_blank"}
- [Exchange Data between Controller, View and Route]({{site.url}}/{{page.categories}}/data-in-controller-view-route/){:target="_blank"}
- [Use DB on Rails]({{site.url}}/{{page.categories}}/database/){:target="_blank"}

Also, you can see the this blog post sample source code on Github

- [Github source code](https://github.com/dev-yakuza/study-rails){:rel="nofollow noreferrer" target="_blank"}
