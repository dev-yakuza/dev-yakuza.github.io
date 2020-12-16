---
layout: 'post'
permalink: '/react-native/eslint-prettier-husky-lint-staged/'
paginate_path: '/react-native/:num/eslint-prettier-husky-lint-staged/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'React NativeでESLint, Prettierを使う方法'
description: 'React NativeのプロジェクトへESLintとPrettierを適用する方法と、Husky, lint-stagedでプロみたいに使う方法について説明します。'
image: '/assets/images/category/react-native/2018/eslint-prettier-husky-lint-staged/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [React Nativeプロジェクト準備](#react-nativeプロジェクト準備)
- [ESLint](#eslint)
  - [ESLintインストール](#eslintインストール)
  - [ESLintの設定](#eslintの設定)
  - [ESLintの詳細設定](#eslintの詳細設定)
  - [ESLintの実行準備](#eslintの実行準備)
  - [ESLint実行](#eslint実行)
  - [eslint --fix](#eslint---fix)
  - [VSCodeでESLintを使う方法](#vscodeでeslintを使う方法)
- [Prettier](#prettier)
  - [Prettierのインストール](#prettierのインストール)
  - [Prettierの設定](#prettierの設定)
  - [ESLintへPrettierを設定する](#eslintへprettierを設定する)
  - [Prettierの実行準備](#prettierの実行準備)
  - [Prettier実行](#prettier実行)
  - [prettier --write](#prettier---write)
  - [VSCodeでPrettierを使う方法](#vscodeでprettierを使う方法)
- [ESLintとPrettierをプロみたいに使う方法](#eslintとprettierをプロみたいに使う方法)
  - [Husky](#husky)
  - [lint-staged](#lint-staged)
  - [Huskyとlint-stagedを使う方法](#huskyとlint-stagedを使う方法)
- [問題解決](#問題解決)
- [完了](#完了)

</div>

## 概要

このブログポストではESLintとPrettierが何かを説明して、React NativeでESLintとPrettierを使う方法について説明します。

また、Huskyとlint-stagedが何かを説明して、プロみたいに使うための設定についても説明します。

ここで説明するESLintとPrettierの設定は下記のGithubリポジトリで確認できます。

- Github: [react-native-eslintrc-prettier](https://github.com/dev-yakuza/react-native-eslintrc-prettier){:rel="nofollow noreferrer" target="_blank"}

## React Nativeプロジェクト準備

このブログポストで紹介する内容は、React NativeへTypescriptが適用された状態でESLintを適用する方法に関して説明します。

React NativeへTypescriptを適用する方法に関しては下記のリンクを確認してください。

- [React NativeへTypescriptを適用する方法]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}

## ESLint

ESLintとはES(EcmaScript) + Lint(エラーコード表示)の合成語で`Javascript`のコードを分析して、コードのスタイルを統一してくれるツールです。

### ESLintインストール

下記のコマンドを使ってESLintをReact Nativeのプロジェクトへインストールします。（React Nativeは基本的ESLintがインストールされてるので、このコマンドはスキップしても良いです。）

```bash
# cd SampleApp
npm install --save-dev eslint
```

{% include in-feed-ads.html %}

### ESLintの設定

次はReact NativeのプロジェクトへESLintを設定する方法について説明します。

下記のコマンドでESLintを初期化します。

```bash
# cd SampleApp
npx eslint --init
```

上のコマンドを実行すると、下記のような画面が確認できます。

```bash
? How would you like to use ESLint? (Use arrow keys)
  To check syntax only
  To check syntax and find problems
❯ To check syntax, find problems, and enforce code style
```

ここでは文法をチェックするだけではなく、自動で修正までやらせるため`To check syntax, find problems, and enforce code style`を選択します。

```bash
? What type of modules does your project use? (Use arrow keys)
❯ JavaScript modules (import/export)
  CommonJS (require/exports)
  None of these
```

React Nativeでは主に`import/export`を使うので`JavaScript modules (import/export)`を選択して次に進めます。

```bash
? Which framework does your project use? (Use arrow keys)
❯ React
  Vue.js
  None of these
```

React NativeはReactを基盤にするので`React`を選択して進めます。

```bash
? Does your project use TypeScript? (y/N)
```

このブログポストでは`Typescript`が適用されたReact NativeプロジェクトへESLintを適用してるので、`y`を選択します。

```bash
? Where does your code run? (Press <space> to select, <a> to toggle all, <i> to invert selection)
 ◯ Browser
❯◉ Node
```

ESLintを適用するソースコードがブラウザで実行されるかどうかを聞いてる画面です。React Nativeはブラウザでは実行されないので、`Node`を選択して進めます。

他の選択肢とは違ってBrowserでスペースバーを一回押して、Nodeでもう一回押して選択します。

```bash
? How would you like to define a style for your project? (Use arrow keys)
  Use a popular style guide
❯ Answer questions about your style
  Inspect your JavaScript file(s)
```

どのスタイルガイドを使うのか選択する画面です。私は`Answer questions about your style`を選択して私が使いたいスタイルを適用するようにします。

```bash
? What format do you want your config file to be in? (Use arrow keys)
❯ JavaScript
  YAML
  JSON
```

ESLintへ設定内容を保存するファイル形式を選択する画面です。React Nativeには既に`.eslintrc.js`ファイルが存在します。このファイルを上書きするた`Javascript`を選択して進めます。

```bash
? What style of indentation do you use? (Use arrow keys)
  Tabs
❯ Spaces
```

IndentationへTabと使うのかSpaceを使うのか選択する質問がでます。私はSpaceを好むので`Spaces`を選択して進めます。

```bash
? What quotes do you use for strings? (Use arrow keys)
  Double
❯ Single
```

文字列へDouble Quotes(`"`)を使うのかSingle Quote(`'`)を使うのか選択する画面がでます。私はSingle Quoteを好むので`Single`を選択して進めます。

```bash
? What line endings do you use? (Use arrow keys)
❯ Unix
  Windows
```

Line endingへ使う形式を選択する質問がでます。私はMacのユーザなので`Unix`を選択して進めます。

```bash
? Do you require semicolons? (Y/n)
```

最後にSemicolon(`;`)を使うかどうかを選択する質問が出ます。私はSemicolonを使うので`Y`を選択して進めます。

```bash
The config that you've selected requires the following dependencies:

eslint-plugin-react@latest @typescript-eslint/eslint-plugin@latest @typescript-eslint/parser@latest
Warning: React version not specified in eslint-plugin-react settings. See https://github.com/yannickcr/eslint-plugin-react#configuration .
Successfully created .eslintrc.js file in /Users/jeonghean_kim/projects/poma_app
```

全ての設定が完了すると上のような画面が出ます。上のメッセージでも分かると思いますが、Warningが表示されてます。このような問題を解決するためにも詳細設定をする必要があります。

{% include in-feed-ads.html %}

### ESLintの詳細設定

私は`Answer questions about your style`を選択してESLintを設定しました。基本的な設定がされたので`React`と`Typescript`を使うための詳細設定が必要です。

下記のコマンドで設定に必要な追加プラグインをインストールします。

```bash
npm install --save-dev eslint-plugin-react @typescript-eslint/eslint-plugin @typescript-eslint/parser eslint-plugin-react-hooks
```

詳細設定をするため、`.eslintrc.js`ファイルを開いて下記のように修正します。

```js
module.exports = {
  env: {
    es6: true,
    node: true,
    jest: true,
  },
  extends: [
    'eslint:recommended',
    'plugin:react/recommended',
    'plugin:@typescript-eslint/eslint-recommended',
    'plugin:@typescript-eslint/recommended',
    'plugin:@typescript-eslint/recommended-requiring-type-checking',
  ],
  ...
  parserOptions: {
    project: './tsconfig.json',
    ...
  },
  plugins: ['react', 'react-hooks', '@typescript-eslint'],
  ...
  rules: {
    indent: ['error', 2, { SwitchCase: 1 }],
    quotes: ['error', 'single', { avoidEscape: true }],
    ...,
    'no-empty-function': 'off',
    '@typescript-eslint/no-empty-function': 'off',
    '@typescript-eslint/no-empty-function': 'off',
    'react/display-name': 'off',
    'react/prop-types': 'off',
  },
  settings: {
    react: {
      version: 'detect',
    },
  },
};
```

### ESLintの実行準備

次はESLintをReact Nativeのプロジェクトを検査するため下記のように`package.json`ファイルを修正します。

```json
{
  ...
  "scripts": {
    ...
    "lint": "eslint --ext .tsx --ext .ts src/",
    ...
  },
  ...
}
```

私は全てのソースコードを`src`フォルダでまとめて管理をしてるので、上のようにフォルダを指定しました。もし、rootフォルダでファイルを管理してる場合は下記のように基本設定をそのまま使ってください。

```json
{
  ...
  "scripts": {
    ...
    "lint": "eslint .",
    ...
  },
  ...
}
```

{% include in-feed-ads.html %}

### ESLint実行

下記のコマンドを使ってESLintを実行してみます。

```bash
npm run lint
```

そしたら下記のような結果が表示されます。

```bash
   1:8   error  A space is required after '{'                             object-curly-spacing
   1:50  error  A space is required before '}'                            object-curly-spacing
   2:8   error  A space is required after '{'                             object-curly-spacing
   2:29  error  A space is required before '}'                            object-curly-spacing
   ...
  11:25  error  Unable to resolve path to module './RequestSite'          import/no-unresolved
  11:25  error  Missing file extension for "./RequestSite"                import/extensions
  12:25  error  Unable to resolve path to module './CheckServer'          import/no-unresolved
  12:25  error  Missing file extension for "./CheckServer"                import/extensions

✖ 22 problems (22 errors, 0 warnings)
  4 errors and 0 warnings potentially fixable with the `--fix` option.
```

上のように私たちが設定したESLint設定によるソースコードの問題点を確認できます。

### eslint --fix

上に表示されたエラーはESLintの設定を守らなかったので、発生しました。もちろんソースコードを開いて1つづつ修正してもいいですが、下記のコマンドを使って全てのエラーを早く直すことができます。

```bash
# npx eslint . --fix
npx eslint ./src/**/*.tsx --fix
```

たくさんのエラーが出ますが、自動で修正してくれます。本当に修正されたか確認するため下記のコマンドを実行してみます。

```bash
npm run lint
```

そしたら依然と違ってエラーメッセージが表示されないことが確認できます。

もし, まだエラ〜メッセージが表示される場合は、該当するソースコードを開いて修正してください。

### VSCodeでESLintを使う方法

もし, 皆さんがVSCodeを使う場合、`ESLint`のExtensionを使うことをおすすめします。ESLintのExtensionをインストールすると、ファイルを保存する時`eslint --fix`と同じようにESLintに合わせて自動的に修正して保存することができます。

![VSCode ESLint Extension](/assets/images/category/react-native/2018/eslint-prettier-husky-lint-staged/vscode-eslint-extension.jpg)

インストールが終わったらVSCodeの設定ファイルを開いて下記のように修正します。

```json
{
  ...
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": true
  },
  ...
}
```

このように修正すると、ファイルを保存する時ESLintの設定に合わせて修正してくれます。

{% include in-feed-ads.html %}

## Prettier

PrettierとはCode Formatterとして、定義されたルールによるコードスタイルを統一してくれるツールです。ESLintがJavascriptのCode Formatterだったら、Prettierは全てのコードスタイルを扱うCode Formatterです。

### Prettierのインストール

下記のコマンドでPrettierを使うためのライブラリをインストールします。

```bash
npm install --save-dev prettier eslint-plugin-prettier
```

### Prettierの設定

React Nativeでプロジェクトを生成したら基本的`.prettierrc.js`ファイルが生成されます。該当ファイルを開いてみると下記のようです。

```js
module.exports = {
  bracketSpacing: false,
  jsxBracketSameLine: true,
  singleQuote: true,
  trailingComma: 'all',
};
```

このファイルを`ESLint`と一緒に使うため下記のように修正します。

```js
module.exports = {
  jsxBracketSameLine: true,
  singleQuote: true,
  trailingComma: 'all',
  printWidth: 100,
};
```

{% include in-feed-ads.html %}

### ESLintへPrettierを設定する

PrettierをESLintと一緒に使うためESLintの設定へPrettierを設定する必要があります。`.eslintrc.js`ファイルを開いて下記のように修正します。

```js
module.exports = {
  ...
  plugins: ['react', 'react-hooks', '@typescript-eslint', 'prettier'],
  rules: {
    ...
    'prettier/prettier': 'error',
  },
  ...
};
```

### Prettierの実行準備

このPrettierでソースコードをFormattingするために下記のように`package.json`ファイルを修正します。

```json
{
  ...
  "scripts": {
    ...
    "format": "prettier --check ./src",
    ...
  },
  ...
}
```

{% include in-feed-ads.html %}

### Prettier実行

次は下記のコマンドでPrettierを実行してみます。

```bash
npm run format
```

そしたら下記のような結果が見えます。

```bash
...
src/Screen/ResetPassword/index.tsx
src/Screen/SignUp/index.tsx
src/Screen/SiteViewer/index.tsx
src/Util/Validation/index.tsx
Code style issues found in the above file(s). Forgot to run Prettier?
```

Prettierは上のようにFormattingが間違ったファイルリストを探してくれます。

### prettier --write

上に表示されたファイルリストはPrettierの設定を守らなかったので、発生しました。この問題があるファイルたちを下記のコマンドで直す音ができます。

```bash
npx prettier --write ./src
```

修正が完了されたら下記のような画面が見えます。

```bash
...
src/Screen/RequestSite/index.tsx 235ms
src/Screen/ResetPassword/index.tsx 92ms
src/Screen/SignUp/index.tsx 174ms
src/Screen/SiteViewer/index.tsx 124ms
src/Theme.tsx 12ms
src/Util/Validation/index.tsx 11ms
```

また、下記のコマンドを使ってコードを検査してみます。

```bash
npm run format
```

以前と違って下記のようなメッセージを確認することができます。

```bash
...
Checking formatting...
All matched files use Prettier code style!
```

### VSCodeでPrettierを使う方法

もし、皆さんがVSCodeを使う場合、`Prettier`のExtensionを使うことをおすすめします。Prettier Extensionをインストールすると、ファイルを保存する時、`prettier --write`と同じようにPrettierのルールに合わせて自動的に修正して保存してくれます。

![VSCode Prettier extension](/assets/images/category/react-native/2018/eslint-prettier-husky-lint-staged/vscode-prettier-extension.jpg)

インストールが完了されたらVSCodeの設定ファイルを開いて下記のように修正します。

```json
{
  ...
  "editor.formatOnSave": true,
  ...
}
```

このように修正すると、Prettierの設定に合わせて自動的に修正してくれます。

{% include in-feed-ads.html %}

## ESLintとPrettierをプロみたいに使う方法

今までESLintとPrettierが何のものか、そしてどう使うのかをみてみました。次は自船実戦でプロみたいに使うため、`Husky`と`lint-staged`を活用する方法について説明します。

### Husky

GitはHookと言う機能を持ってます。Gitでイベント(コミット、プシューなど)を実行する時、そのイベントへHookを設定してHookに設定されたスクリプトを実行することができます。

HuskyとはGit Hookを簡単に使えようにしてくれるツールです。

そしたらHuskyを使うために下記のコマンドでHuskyをインストールします。

```bash
npm install --save-dev husky
```

### lint-staged

Huskyと一緒によく使う`lint-staged`はGitのStagedされたファイルたちへコマンドを実行するようにしてくれるルールです。

GitのStagedされた状態とは`git add`のコマンドで修正したファイルをコミットするため追加された状態を言います。このようにStaged状態でファイルを修正する場合は`git add`でまた追加する必要があります。

lint-stagedはStagedされたファイルを修正する後、またgit addをしなくても問題ないようにしてくるツールです。

そしたらHuskyと一緒に`lint-staged`を使うため下記のコマンドでlint-stagedをインストールします。

```bash
npm install --save-dev lint-staged
```

{% include in-feed-ads.html %}

### Huskyとlint-stagedを使う方法

次はHuskyとlint-stagedを使うためGitのCommitをする時、ESLintとPrettierを実行するように設定してみます。

Huskyとlint-stagedを設定するため`package.json`ファイルを開いて下記のように修正します。

```json
{
  ...
  "lint-staged": {
    "src/**/*.{ts,tsx}": [
      "eslint --ext .tsx --ext .ts src/ --fix"
    ],
    "./src/**": [
      "prettier --write ."
    ]
  },
  "husky": {
    "hooks": {
      "pre-commit": "lint-staged"
    }
  },
  ...
}
```

Huskyを使ってGitのCommitを実行する前(`pre-commit`)にlint-stagedを実行するようにしました。lint-stagedの設定ではソースコード(`src/**/*.{ts,tsx}`, `*`)が追加/変更された場合、`eslint --fix`と`prettier --write`を実行するようにしますした。

次からはGitのCommitを使ってソースコードをレポジトリ(Repository)へ上げる前にESLintとPrettierを実行してソースコードをいつも上手く整理された上帝で管理することができます。

## 問題解決

上の設定を使ったReact Nativeで下記のようなエラーが発生しました。

```bash
husky > pre-commit (node v13.8.0)
  ✔ Preparing...
  ❯ Running tasks...
    ↓ Running tasks for src/**/*.{ts,tsx} [skipped]
      → No staged files match src/**/*.{ts,tsx}
    ❯ Running tasks for *
      ✖ prettier --write .
  ↓ Applying modifications... [skipped]
    → Skipped because of errors from tasks.
  ✔ Reverting to original state...
  ✔ Cleaning up...
...
src/Theme.tsx 4ms
tsconfig.json 5ms
[error] No parser could be inferred for file: src/image.jpg
```

このように`Prettier`が分析できないファイルとか、チェックする必要がないファイルのせいでエラーが発生する場合があります。
この時は`.prettierignore`ファイルを生成して下記のように修正します。

```bash
*.jpg
```

まず、私は`.prettierignore`ファイルを作って`.gitignore`ファイル内容をコピペしました。そして一番下にエラーが発生してるファイルを追加しました。

## 完了

これでReact NativeのプロジェクトへESLintとPrettierを設定してHuskyとlint-stagedを使って自動化する方法についてみてみました。

上で説明したESLintの設定とPrettierの設定は下記のGithubレポジトリで確認できます。もし、気になる方は下記のリンクを確認してください。

- Github: [react-native-eslintrc-prettier](https://github.com/dev-yakuza/react-native-eslintrc-prettier){:rel="nofollow noreferrer" target="_blank"}