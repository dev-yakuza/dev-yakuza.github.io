---
layout: 'post'
permalink: '/django/pre-commit/'
paginate_path: '/django/:num/pre-commit/'
lang: 'ja'
categories: 'django'
comments: true

title: '[Django] pre-commitの使い方'
description: Djangoプロジェクトでpre-commitを使ってGitにコミットする時、flake8を自動で実行するように設定してみましょう。
image: '/assets/images/category/django/2021/pre-commit/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [pre-commitのインストール](#pre-commitのインストール)
- [pre-commitの設定](#pre-commitの設定)
- [flake8の設定](#flake8の設定)
- [pre-commitの実行](#pre-commitの実行)
- [完了](#完了)

</div>

## 概要

以前のブログポストではPythonの静的コード解析である`flake8`を使ってコードのスタイルを統一して、潜在的なバグも減らす方法について調べてみました。

- [[Django] flake8の使い方]({{site.url}}/{{page.categories}}/flake8/){:target="_blank"}

今回のブログポストでは`pre-commit`を使ってソースコードをGitにコミットする時、設定したflake8を自動で実行する方法について調べてみます。

- pre-commit: [https://pre-commit.com/](https://pre-commit.com/){:rel="nofollow noreferrer" target="_blank"}

## pre-commitのインストール

pre-commitを使ってflake8を自動で実行するためには、pre-commitをインストールする必要があります。次のコマンドを使ってpre-commitをインストールします。

```bash
pip install pre-commit
```

インストールを完了したら、忘れないように`requirements.txt`にも保存しておきます。

```bash
pip freeze > requirements.txt
```

これでpre-commitをインストールする方法についてみて見ました。

## pre-commitの設定

pre-commitを使ってflake8を自動で実行するためには、pre-commitの設定ファイルを作成する必要があります。次のコマンドを使ってpre-commitの設定ファイルを生成します。

```bash
pre-commit sample-config > .pre-commit-config.yaml
```

生成された`.pre-commit-config.yaml`ファイルを開いてみると次のようです。

```yml
# See https://pre-commit.com for more information
# See https://pre-commit.com/hooks.html for more hooks
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v3.2.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
```

pre-commitが提供するサンプル内容を確認することができます。

{% include in-feed-ads.html %}

## flake8の設定

次はpre-commitの設定ファイルにflake8を設定する方法について見てみます。pre-commitの設定ファイルである`.pre-commit-config.yaml`は基本的下記のような構造を持ってます。

```yml
repos:
  - repo: repo-url
    rev: version
    hooks:
      - id: hook-id
```

- repo: pre-commitが提供する昨日のRepository URL
- rev: 使う機能のバージョン
- id: pre-commitが提供する機能

pre-commitは基本的提供する機能があります。次のリンクをみてどの機能が提供されてるか確認できます。

- hooks: [https://pre-commit.com/hooks.html](https://pre-commit.com/hooks.html){:rel="nofollow noreferrer" target="_blank"}

私たちはこの中でflake8を使う予定です。`.pre-commit-config.yaml`ファイルを開いて次のように修正します。

```yml
repos:
  - repo: https://gitlab.com/pycqa/flake8
    rev: 3.8.4
    hooks:
      - id: flake8
```

pre-commitが提供するrepoのURLとバージョン、flake8のhookを設定しました。この部分はflake8の公式ドキュメントでも確認できます。

- flake8 hooks: [https://flake8.pycqa.org/en/latest/user/using-hooks.html](https://flake8.pycqa.org/en/latest/user/using-hooks.html){:rel="nofollow noreferrer" target="_blank"}

このように設定したファイルを実際GitのCommit hookに登録するため、次のコマンドを実行します。

```bash
pre-commit install
```

これでpre-commitを使ってflake8を使う準備ができました。

## pre-commitの実行

そしたら私たちが設定したpre-commitがうまく動作するか確認しましょう。次のコマンドを実行して私たちが設定した`.pre-commit-config.yaml`ファイルを基準でpre-commitを実行します。

```bash
pre-commit run --all-files
```

コマンドを実行すると次のような結果を確認することができます。

```bash
flake8...................................................................Passed
```

これで私たちが設定したpre-commitがうまく動作することが確認できます。ここだで私たちが設定した内容をGitにコミットします。

```bash
git add .
git commit -m 'Add pre-commit for flake8'
git push origin main
```

## 完了

これでpre-commitを使ってGitにコミットする時、flake8を実行する方法について調べてみました。注意する店は、新しくRepositoryをCloneした場合、忘れなく`pre-commit install`を実行してpre-commitの設定内容をGit hooksに登録する必要があります。

```bash
git clone repository_url
# virtualenv venv
# source venv/bin/activate
pip install -r requirement.txt
pre-commit install
```

今から自動化されたflake8でもっと生産性を高くして開発をしてみて下さい。
