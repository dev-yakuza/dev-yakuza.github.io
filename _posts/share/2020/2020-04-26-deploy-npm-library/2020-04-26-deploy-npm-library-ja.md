---
layout: 'post'
permalink: '/share/deploy-npm-library/'
paginate_path: '/share/:num/deploy-npm-library/'
lang: 'ja'
categories: 'share'
comments: true

title: NPMに自分のライブラリを配布する
description: 自分が作ったJavascriptライブラリをNPMへ配布する方法について説明します。
image: '/assets/images/category/share/2020/deploy-npm-library/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [NPMアカウントを作る](#npmアカウントを作る)
- [npm info](#npm-info)
- [npm init](#npm-init)
- [npm login](#npm-login)
- [npmignore](#npmignore)
- [npm publish](#npm-publish)
- [npm version](#npm-version)
- [完了](#完了)

</div>

## 概要

今までReact Nativeで開発しながら、他の人が作ったオープンソースをたくさん使いました。いつもこのようにオープンソースだけ使ったので、自分も一回オープンソースを作ってみようと考えて`react-native-image-modal`と言う簡単なオープンソースを作成しました。

- NPM: [react-native-image-modal](https://www.npmjs.com/package/react-native-image-modal){:rel="nofollow noreferrer" target="_blank"}

React Nativeのオープンソースライブラリを開発する方法について知りたい方は下記のブログポストを参考してください。

- [React Native用オープンソースを作る方法]({{site.url}}/react-native/make-opensource-library/){:target="_blank"}

このブログポストでは自分が作成したJavascriptライブラリをNPM(Node Package Manager)へ配布する方法について説明します。

## NPMアカウントを作る

NPMへ自分が作ったJavascriptライブラリを配布するためにはNPMと言うサービスのアカウントが必要です。

NPMのアカウントがいない方は、下記のリンクをクリックしてNPMサービスへ移動した後、NPMアカウントを生成してください。

- NPMサービスサイト: [https://www.npmjs.com/](https://www.npmjs.com/){:rel="nofollow noreferrer" target="_blank"}

## npm info

自分が開発したJavscriptライブラリを配布する前、配布が可能なパッケージ名か確認する必要があります。当然なことですが、NPMに配布されたライブラリと同じ名前を使うことはできないです。

下記のコマンドを使って、自分のJavascriptライブラリ名が使えるか確認します。

```bash
npm info [Javascript Package Name]
```

もし、重複されたら、下記のように、すでにNPMへ配布されたライブラリに関するデータが確認できます。

```bash
npmdeploy@1.0.1 | MIT | deps: 1 | versions: 1
deploy projects easily in the cloud. Optimised for GitLab CI
https://gitlab.com/pushrocks/npmdeploy#README

keywords: deploying, made, easy

dist
.tarball: https://registry.npmjs.org/npmdeploy/-/npmdeploy-1.0.1.tgz
.shasum: c298d768aac7ccb89a38c20a0c904341fc87c484

dependencies:
gitlab: ^1.6.0

maintainers:
- lossless <npm@lossless.digital>

dist-tags:
latest: 1.0.1

published over a year ago by lossless <npm@lossless.digital>
```

もし、重複されてない名前だったら、下記のように`404`エラーが表示されます。

```bash
npm ERR! code E404
npm ERR! 404 'temp-npmdeploy' is not in the npm registry.
npm ERR! 404 You should bug the author to publish it
npm ERR! 404 (or use the name yourself!)
npm ERR! 404
npm ERR! 404 Note that you can also install from a
npm ERR! 404 tarball, folder, http url, or git url.
npm ERR! 404
npm ERR! 404  'temp-npmdeploy@latest' is not in the npm registry.
npm ERR! 404 You should bug the author to publish it (or use the name yourself!)
npm ERR! 404
npm ERR! 404 Note that you can also install from a
npm ERR! 404 tarball, folder, http url, or git url.
```

{% include in-feed-ads.html %}

## npm init

自分が開発したJavascriptライブラリをNPMへ配布するためNPMに必要な情報を設定する必要があります。

自分が開発したJavascriptライブラリフォルダへ移動して、下記のコマンドを実行します。

```bash
# cd ProjectName
npm init
```

上のコマンドを実行すると、下記のような画面が確認されます。下記で説明する内容は後でも変更ができるので、お気軽に進んでください。

```bash
This utility will walk you through creating a package.json file.
It only covers the most common items, and tries to guess sensible defaults.

See `npm help json` for definitive documentation on these fields
and exactly what they do.

Use `npm install <pkg>` afterwards to install a package and
save it as a dependency in the package.json file.

Press ^C at any time to quit.
package name: (npmdeploy)
```

フォルダ名を基準にして`package name`を決定するか、他の名前を設定するか聞いてくれます。私たちは上で`npm info`を使って配布可能な名前を探しましたので、その名前を入力します。

```bash
version: (1.0.0)
```

その後、バージョンを入力する画面がでます。バージョンは基本的`major.minor.patch`を使います。すでに開発が終わって、配布だけ残ってる状況の場合、`1.0.0`をそのまま使います。まだ、開発中で、ライブラリが完璧ではない場合、`0.0.1`を入力して安定されたバージョンではないことを明記します。

```bash
description:
```

Javascriptライブラリに関して説明を作成する部分です。自分のライブラリの説明を作成します。

```bash
entry point: (index.js)
```

開発したJavascriptライブラリのEntryファイル（Mainファイル）を指定します。

```bash
test command:
```

自分が開発したJavascriptライブラリをテストすることができるテストコマンドを入力します。テストを実行するコマンドがない場合、Enterキーを押して進めます。

```bash
git repository:
```

配布するJavascriptのソースコードを確認することができるGitリポジトリのURLを入力します。URLが存在しない場合Enterキーを押して進めます。

```bash
keywords:
```

配布するJavascriptを簡単に分かれるようにキーワードを入力します。(ex> jQuery, react-native, reactjs など)

```bash
author:
```

配布する人の情報を入力します。普通は`Name <Email Address>`の形式を使います。

```bash
license: (ISC)
```

配布するライブラいのライセンスに関する質問です。自分のライブラリのライセンスへ合わせて入力します。(ex> MIT, ISC など)

ライセンスへキーワードに関しては下記のリンクを参考してください。

- [GitHub license type](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/licensing-a-repository#searching-github-by-license-type)

このように全ての項目を入力したら自分のプロジェクト中に`pacakge.json`ファイルが生成されます。

{% include in-feed-ads.html %}

## npm login

NPMへ自分のライブラリを配布するため、下記のコマンドを使ってNPMサービスへログインする必要があります。

```bash
npm login
```

上のコマンドを実行すると下記のようにログインするための手続きが実行されます。

```bash
Username: dev-yakuza
Password:
Email: (this IS public) dev.yakuza@gmail.com
Logged in as dev-yakuza on https://registry.npmjs.org/.
```

上で生成したNPMアカウントの情報を入力してログインします。ログインをしたら、下記のコマンドを実行してログインができたか確認します。

```bash
npm whoami
# dev-yakuza
```

## npmignore

実際開発には必要ですが、開発が終わったライブラリを使う時はいらないファイルたちがあります。例えば、テストコード、例題ソースなどです。このように開発には必要ですが、配布にはいらないファイルたちを`.npmignore`ファイルを使って除くことができます。

下記の内容は自分が開発した`react-native-image-modal`に関する`.npmignore`ファイルです。

```bas
node_modules
Develop
DevelopWithExpo
Example
ExampleWithExpo
.github
demo
```

## npm publish

今NPMhe自分のライブラリを配布する準備が終わりました。下記のコマンドを使って自分のライブラリをNPMへ配布します。

```bash
npm publish
```

ライブラリを配布する前、特定なコマンドを実行する必要がある場合、`package.json`を下記のように修正します。

```json
"scripts": {
  ...
  "prepare": "rm -rf dist && tsc"
},
```

私はTypescriptを使ってライブラリを開発したので、配布する前Typescriptをビルドする必要があります。このように`package.json`の`scripts`へ`prepare`コマンドを定義すると、`npm publish`コマンドを実行する時、該当コマンドが実行されます。.

これで皆さんが開発したライブラリをNPMへ配布しました。配布したライブラリを使うためには皆さんがNPMでライブラリを使う時と同じように使えます。

```bash
npm install --save [Your Package Name]
```

{% include in-feed-ads.html %}

## npm version

NPMへ配布したライブラリを修正して、また配布することがあります。このように再配布する時、バージョン情報を上げる必要があります。

バージョンを上げるために`package.json`ファイルのバージョン(`"version": "0.0.1"`)を直接修正して配布しても大丈夫ですが、下記のコマンドを使ってバージョンをアップデートすることもできます。

```bash
npm version patch
npm version minor
npm version major
```

上のコマンドを必要な状況に合わせて、簡単にバージョンを上げることができます。

## 完了

これで自分が開発したJavascriptライブラリをNPMへデプロイする方法について説明しました。初めてオープンソースを作ってNPMへ配布したら、私も何か開発者の文化へ参加した気がしました。

![NPM react-native-image-modal](/assets/images/category/share/2020/deploy-npm-library/npm-react-native-image-modal.jpg)

皆さんも皆さんだけのオープンソースを作って配布して、美しい開発者の文化へ参加して見ることはどうですか？
