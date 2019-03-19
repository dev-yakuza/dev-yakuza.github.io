---
layout: 'post'
permalink: '/react-native/react-native-fs/'
paginate_path: '/react-native/:num/react-native-fs/'
lang: 'ja'
categories: 'react-native'
comments: true

title: 'ファイルシステム使用'
description: 'RN(React Native)プロジェクトでreact-native-fsライブラリを使ってファイルを読んだり書いたりしてみましょう。'
image: '/assets/images/category/react-native/react-native-fs.jpg'
---


## 概要
RN(React Native)で開発する時、しばしばファイルシステム(filesystem)を使ってファイルを読んだり書いたりする場合が発生します。```react-native-fs```はRN(React Native)でファイルシステム(filesystem)をもっと簡単に使えるように助けてくれるライブラリです。このブログでは```react-native-fs```を使う方法について説明します。

- react-native-fs公式サイト: [https://github.com/itinance/react-native-fs](https://github.com/itinance/react-native-fs){:rel="nofollow noreferrer" target="_blank"}

## インストール
RN(React Native)でファイルシステム(filesystem)を使うために下記のコマンドを使って```react-native-fs```をインストールします。

```bash
npm install --save react-native-fs
```

インストールが完了されたら、下記のコマンドで```react-native-fs```とRN(React Native)プロジェクトを連結します。

```bash
react-native link react-native-fs
```

## 使い方
ファイルシステム(filesystem)を使ってファイルを読んだり書いたりする色んな方法について[公式サイト](https://github.com/chirag04/react-native-mail){:rel="nofollow noreferrer" target="_blank"}に詳しく載せております。ここには簡単にファイルを読んだり書いたりする部分について説明します。

### ディレクトリ
下は```react-native-fs```が定義してるファイルシステムのディレクトリ/パス(filesystem directory/path)です。

- MainBundlePath: メインバンドルフォルダ(Main Bundle Directory)の絶対位置です(アンドロイドでは使えません。)
- CachesDirectoryPath: キャッシュフォルダ(Cache Directory)の絶対位置です。
- ExternalCachesDirectoryPath: 外部キャッシュフォルダ(External Cache Directory)の絶対位置です。(iOSでは使えません。)
- DocumentDirectoryPath: ドキュメントフォルダ(Document Directory)の絶対位置です。
- TemporaryDirectoryPath: 臨時フォルダ(Temporary Directory)の絶対位置です。(アンドロイドではキャッシュフォルダと同じです。)
- LibraryDirectoryPath: iOSのNSLibraryDirectoryの絶対位置です(アンドロイドでは使えません。)
- ExternalDirectoryPath: 外部ファイル共有フォルダ(External files, shared directory)の絶対位置です。(iOSでは使えません。)
- ExternalStorageDirectoryPath: 外部ストレじ共有フォルダ(External storage, shared directory)の絶対位置です。(iOSでは使えません。)

### フォルダ読み
下はRN(React Native)で```react-native-fs```を使ってフォルダを読む方法に関するコードです。

```js
...
// typescript style
import * as RNFS from 'react-native-fs';
...

//readDir(dirpath: string)
RNFS.readDir(RNFS.DocumentDirectoryPath).then(files => {
    ...
})
.catch(err => {
    ...
    console.log(err.message, err.code);
    ...
});
...
```

### ファイル読み
下はRN(React Native)で```react-native-fs```を使ってファイルを読む方法に関するコードです。

```js
...
// typescript style
import * as RNFS from 'react-native-fs';
...

// readFile(filepath: string, encoding?: string)
RNFS.readFile(filePath, 'ascii').then(res => {
    ...
})
.catch(err => {
    ...
    console.log(err.message, err.code);
    ...
});
...
```

### ファイル書き
下はRN(React Native)で```react-native-fs```を使ってファイルを書く方法に関するコードです。

```js
...
// typescript style
import * as RNFS from 'react-native-fs';
...

// writeFile(filepath: string, contents: string, encoding?: string)
RNFS.writeFile(savePath, contents, 'ascii').then(res => {
    ...
})
.catch(err => {
    ...
    console.log(err.message, err.code);
    ...
});
...
```

### ファイル削除
下はRN(React Native)で```react-native-fs```を使ってファイルを削除する方法に関するコードです。

```js
...
// typescript style
import * as RNFS from 'react-native-fs';
...

// unlink(filepath: string)
RNFS.unlink(`${RNFS.DocumentDirectoryPath}/temp/`).then(res => {
    ...
})
.catch(err => {
    ...
    console.log(err.message, err.code);
    ...
});
...
```

## 他の機能
react-native-fsで使える機能を共通/iOS/アンドロイド別で整理してみました。
詳しく内容は公式サイトを参考してください。

- react-native-fs公式サイト: [https://github.com/itinance/react-native-fs](https://github.com/itinance/react-native-fs){:rel="nofollow noreferrer" target="_blank"}

### 共通
下記のリストは```react-native-fs```でOSと関係なく使える共通な機能です。

- readDir(dirpath: string): パラメータでもらって絶対位置(Absolute path)のフォルダを読む
- readdir(dirpath: string): Nodejsスタイルの```readDir```
- stat(filepath: string): パラメータのファイル位置のファイルのステータスを取得
- readFile(filepath: string, encoding?: string): パラメータのファイル位置のファイルを読む。encodingはutf8(default), ascii, base64を提供するし、base64はバイナリファイルを読む時使う。
- read(filepath: string, length = 0, position = 0, encodingOrOptions?: any): パラメータのファイル位置のファイルに特定位置(position)へ長さが(length)ほどファイルの内容を読む。encodingはreadFileと同じです。
- writeFile(filepath: string, contents: string, encoding?: string): 指定したファイル位置にファイルを記録する。
- appendFile(filepath: string, contents: string, encoding?: string): 指定したファイルにファイルの内容を追加する。
- write(filepath: string, contents: string, position?: number, encoding?: string): ファイルの特定位置(position)へファイル内容を追加する。
- moveFile(filepath: string, destPath: string): ファイルを移動する。
- copyFile(filepath: string, destPath: string): ファイルをコピする。
- unlink(filepath: string): ファイルを削除する。
- exists(filepath: string): ファイルが存在するかどうかファイルが存在するかどうかを確認する。ファイルが存在しない場合```false```をリターンする。
- hash(filepath: string, algorithm: string): パラメータのファイル位置のファイルの当該アルゴリズム(algorithem)のchecksumをリターンする。アルゴリズム(algorithm)はmd5, sha1, sha224, sha256, sha384, sha512が使える。
- touch(filepath: string, mtime?: Date, ctime?: Date): ファイルの修正日(mtime)と生成日(ctime)を更新する。iOSでは生成日(ctime)のみで修正が可能ですが、アンドロイドは修正日(mtime)を使って修正日と生成日をいつも同時に更新する。
- mkdir(filepath: string, options?: MkdirOptions): フォルダを生成する。
- downloadFile(options: DownloadFileOptions): パラメータのオプション(options)中のファイルURLを使ってファイルをダウンロードする。
- stopDownload(jobId: number): パラメータのダウンロードidを使ってダウンロードを中止する。
- getFSInfo(): ファイルシステムの情報(総容量、使える容量)をリターンする。

### iOS専用
下記のリストは```react-native-fs```でiOSのみで使える機能です。

- copyAssetsFileIOS(imageUri: string, destPath: string, width: number, height: number, scale : number = 1.0, compression : number = 1.0, resizeMode : string = 'contain' ): (iOS) iOSのカメラロール(Camera-roll)に存在するファイルをコピします。
- resumeDownload(jobId: number): (iOS) パラメータのダウンロードidを使ってダウンロードを再開します。
- isResumable(jobId: number): (iOS) パラメータのダウンロードidが再開できるかどうか確認します。
- completeHandlerIOS(jobId: number): (iOS) バックグラウンドでダウンロードする時ダウンロードが終わったことを知らせるように設定することが可能です。
- uploadFiles(options: UploadFileOptions): (iOS) ファイルをアップロードします。
- stopUpload(jobId: number): (iOS) ファイルアップロードを中止します。
- pathForGroup(groupIdentifier: string): (iOS) iOSで ```com.apple.security.application-groups```に設定した全てのものをリターンします。

### アンドロイド専用
下記のリストは```react-native-fs```でアンドロイド(Android)のみで使える機能です。

- existsAssets(filepath: string): (アンドロイド) アンドロイドのassetsフォルダにファイルが存在するかどうかを確認する。ファイルが存在しない場合```false```をリターンします。
- readFileAssets(filepath:string, encoding?: string): (アンドロイド) アンドロイドのassetsフォルダ下にあるファイルをファイル位置を使って読む。
- copyFileAssets(filepath: string, destPath: string): (アンドロイド) ファイルをアンドロイドのassetsフォルダ下にコピする。
- readDirAssets(dirpath: string): (アンドロイド) パラメータで貰ったアンドロイドのassetsフォルダ下の相対位置(Relative path)の内容を読む。
- scanFile(path: string): (アンドロイド) ```Media Scanner```を使ってファイルをスキャン(scan)する
- getAllExternalFilesDirs(): (アンドロイド) 全ての共有/外部ストレージの情報をリターンする。


## 完了
RN(React Native)でファイルシステムを使う場合```react-native-fs```を使えることをお勧めします。OSに依存する機能もありますが、大体共通機能でも十分活用できます。リターンバリュー(Return Value)とパラメータ(Parameter)に関する詳しく説明はいませんでした。リターンバリュー(Return Value)とパラメータ(Parmeter)に関する内容は公式サイトを参考してください。


## 参考
- react-native-fs 公式サイト: [https://github.com/itinance/react-native-fs](https://github.com/itinance/react-native-fs){:rel="nofollow noreferrer" target="_blank"}