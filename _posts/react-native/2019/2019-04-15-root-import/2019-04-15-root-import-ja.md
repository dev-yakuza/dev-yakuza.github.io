---
layout: 'post'
permalink: '/react-native/root-import/'
paginate_path: '/react-native/:num/root-import/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'リアクトネイティブ(React Native)でrootからimportする'
description: 'リアクトネイティブ(React Native)プロジェクトでimportをする時、rootフォルダを基準にしてimportが出来るようにプロジェクトを設定してみましょう。'
image: '/assets/images/category/react-native/2019/root-import/background.jpg'
---

## 概要
このブログではリアクトネイティブ(React Native)だけの問題ではなく、Reactで開発する時、問題を解決してみようかと思います。Reactで開発する時、プロジェクトの構造を綺麗にしても`import`する時、長くなる`../../../`フォルダの参照問題は解決できないです。このブログでは長くなるこのフォルダの参照問題を少しでも解決してみようかと思って作成しました。リアクトネイティブ(React Native)の開発者だけではなくReactjs開発者にも参考になると嬉しいです。

## フォルダの構造
私はリアクトネイティブ(React Native)で開発する時、下記のようなフォルダ構造を使っています。

```
|-- android/
|-- ios/
|-- src/
|   |-- @types/
|   |-- Assets/
|   |   |-- Images/
|   |-- Component/
|   |   |-- BannerContainer/
|   |   |   |-- index.tsx
|   |   |-- LoadingContainer/
|   |   |   |-- index.tsx
|   |-- Screen/
|   |   |-- Home/
|   |   |   |-- SomeContainer/
|   |   |   |   |-- index.tsx
|   |   |   |-- SomeContainer2/
|   |   |   |   |-- SomeContainerItem/
|   |   |   |   |   |-- index.tsx
|   |   |   |   |-- index.tsx
|   |   |   |-- index.tsx
|   |-- Util/
|-- index.js
```

最初は`Component`、`Container`、`Screen`で分けって開発しましたが、`Container`が特定な`Screen`に従属的に使えって、色んな`Screen`で使う場合が少なかったです。それで色んな`Screen`で共通的使う部分を`Component`に入れって、従属的なContainer(Component)はScreenフォルダの下に置いています。もちろん、`Component`の下にもComponent(Container)に従属してるComponentが存在しています。

このようにした理由は二つぐらいあります。一つは`Screen`に従属されてる`Container`を探すため、`Container`フォルダまで探して、また`Component`フォルダまで探さなきゃならない不便さがありました。今は従属されてるContainerはScreenフォルダ下にあるので探す時、楽になりました。もう一つはコピペーを楽にするためです。一人で臭味で色んなアプリを開発してるので一つのプロジェクトで作ったComponentをコピーして他のプロジェクトにペーストする場合があります。`Container`フォルダを別で管理する時、`Screen`をコピーするようになったら、Screenをコピーしてそこに必要なContainerをコピーしてComponentもコピーする必要がありました。今はScreen一つだけコピーすればContainerが一緒にコピーされるのでコピペーがちょっと楽になりました。このような不便さを解決するため上のようなプロジェクトの構造を持てるようになりました。参考ですがReactjsは下記のよなフォルダ構造を使っています。

```
|-- android/
|-- ios/
|-- src/
|   |-- @types/
|   |-- Assets/
|   |   |-- Images/
|   |-- Component/
|   |   |-- BannerContainer/
|   |   |   |-- index.tsx
|   |   |-- LoadingContainer/
|   |   |   |-- index.tsx
|   |-- Feature/
|   |   |-- Login/
|   |   |   |-- SomeContainer/
|   |   |   |   |-- index.tsx
|   |   |   |-- SomeContainer2/
|   |   |   |   |-- SomeContainerItem/
|   |   |   |   |   |-- index.tsx
|   |   |   |   |-- index.tsx
|   |   |   |-- index.tsx
|   |-- Util/
|-- index.js
```

上のように`Screen`で管理してるフォルダを`Feature`の名前のフォルダで管理しています。皆さんはどんなフォルダ構造を使っていますか？色んな人たちが参考できるように一番下のコメントに皆さんのフォルダ構造を共有してみてください！(私も参考したいですT^T)

{% include in-feed-ads.html %}

## 問題
このようにフォルダを持って流ので`Screen`(`Feature`)の下に`Container`があてContainerがまた他の`Container`を持てるし最後のContainerが`Component`を持てる場合`import`をする時、`../../../`が結構長くなるフォルダ参照問題が発生します。最近はvscodeが良くなって自動に追加してくれるけど、`../../../`の問題はまだのこています。

また、`Screen`に従属されてる`Container`や`Component`が共通化されて`Component`フォルダに移動する場合、逆に`Component`が`Screen`に従属されることになって`Screen`のフォルダに移動する場合、`import`のフォルダ参照の位置が変わって変更するのが大変です。

## 解決策
私はこの問題を解決するため`babel-plugin-root-import`と`typescript`の設定でrootフォルダから参照出来るように修正しました。例えば、`../../../Component/BannerContainer`の部分が`~/Component/BannerContainer`ように参照できます。下記で設定する方法について説明します。

### babel-plugin-root-import
rootフォルダから参照出来るようにするため`babel-plugin-root-import`を下記のコマンドでインストールします。

```bash
npm install babel-plugin-root-import --save-dev
```

リアクトネイティブ(React Native)プロジェクトの`babel.config.js`を開いて下記のように修正します。

```js
module.exports = {
  presets: ['module:metro-react-native-babel-preset'],
  plugins: [
    'babel-plugin-styled-components',
    [
      'babel-plugin-root-import',
      {
        rootPathPrefix: '~',
        rootPathSuffix: 'src',
      },
    ],
  ],
};
```

私のフォルダの構造を見れば分かると思いますが、私は全てのソースを`src`に入れって管理しています。したがって、私は`root`フォルダではなく`src`フォルダを基準にして動作するように設定しました。

{% include in-feed-ads.html %}

### typescript
typescriptを使ってない方は上の設定だけで大丈夫です。私はリアクトネイティブ(React Native)プロジェクトでtypescriptを使って流のでtypescriptがrootフォルダを認識するように設定する必要があります。リアクトネイティブ(React Native)にtypescriptを提供する方法は下記のブログを参考してください。

- [typescript]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}

リアクトネイティブ(React Native)プロジェクトの`tsconfig.json`ファイルを開いて下記のように修正します。

```json
{
  "compilerOptions": {
    ...
    "baseUrl": "./src", // all paths are relative to the baseUrl
    "paths": {
      "~/*": ["*"] // resolve any `~/foo/bar` to `<baseUrl>/foo/bar`
    }
  },
  ...
}
```

## 完了
これでリアクトネイティブ(React Native)プロジェクトで`import`する時、長かった`../../../../`とはバイバイしました。もっとプロジェクトが綺麗に管理出来るように見えて嬉しいです。皆さんも遅くなる前この部分を追加することをお勧めします！
