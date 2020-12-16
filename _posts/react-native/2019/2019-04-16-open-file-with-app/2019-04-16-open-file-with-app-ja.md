---
layout: 'post'
permalink: '/react-native/open-file-with-app/'
paginate_path: '/react-native/:num/open-file-with-app/'
lang: 'ja'
categories: 'react-native'
comments: true

title: '特定のファイルでアプリを開く'
description: 'ウェブやメールでダウンロードした特定なファイルを(エクセル, パワーポイントなど)をリアクトネイティブ(React Native)で作成したアプリに入れる方法について説明します。'
image: '/assets/images/category/react-native/2019/open-file-with-app/background.jpg'
---

## 概要
ウェブやメールで特定のファイルをダウンロードして、そのファイルを自分が作ったアプリで開きたい時があります。例えば、下記のようにpdfやエクセルファイルを特定のアプリを開けます。

アンドロイドの場合、

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2019/open-file-with-app/android-open-with.jpg" alt="アンドロイド - ファイルと一緒にアプリ実行">
</div>

iOSの場合、

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2019/open-file-with-app/iphone-open-with.jpg" alt="iOS - ファイルと一生にアプリを実行">
</div>

上のように特定のファイルを開く時、自分のアプリが表示されるようにする方法とそのファイルを使う方法について説明します。このブログでは`.temp`ファイルを使ってアプリを実行する方法を説明します。

{% include in-feed-ads.html %}

## iOS
iOSでファイルが上手くコピーされたか確認するため、下にあるブログを見てアプリのiTunesファイル共有機能を入れます。

- [iTunesファイルシェア機能]({{site.url}}/{{page.categories}}/react-native-itunes-share-file/){:target="_blank"}

今iOSで特定のファイルを自分のアプリで開けるようにするため、`ios/[project name]/Info.plist`を開いて下記のように修正します。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  ...
  <!-- custom file start -->
	<key>UTExportedTypeDeclarations</key>
	<array>
		<dict>
			<key>UTTypeConformsTo</key>
			<array>
				<string>public.data</string>
			</array>
			<key>UTTypeDescription</key>
			<string>Custom File</string>
			<key>UTTypeIdentifier</key>
			<!-- change custom file extension -->
			<string>com.example.document.temp</string>
			<key>UTTypeTagSpecification</key>
			<dict>
				<key>public.filename-extension</key>
				<!-- change custom file extension -->
				<array>
					<string>temp</string>
				</array>
			</dict>
		</dict>
	</array>
	<key>CFBundleDocumentTypes</key>
	<array>
		<dict>
			<key>CFBundleTypeName</key>
			<string>Custom File</string>
			<key>CFBundleTypeRole</key>
			<string>Editor</string>
			<key>LSHandlerRank</key>
			<string>Owner</string>
			<key>LSItemContentTypes</key>
			<array>
				<!-- change custom file extension -->
				<string>com.example.document.temp</string>
			</array>
		</dict>
	</array>
	<!-- custom file end -->
  ...
</dict>
</plist>
```

もう一度話しますが、上の内容は`.temp`で終わるファイルを自分のアプリで開く場合、使う内容です。`<!-- change custom file extension -->`でコメントアウトがある3つの部分を自分が欲しいファイルで修正して使ってください。

まず、iTunesを開いてファイル共有機能が活性化されたか確認します。

![iOS - itunesファイル共有機能確認](/assets/images/category/react-native/2019/open-file-with-app/itunes-no-file.jpg)

テストのためファイルを`.temp`に修正してiOSで確認できるメールで添付して送信します。メールアプリを開いて先ほど送った`.temp`ファイルを選択して右上の共有ボタアンを押すと下記のように自分のアプリでコピーできることが確認できます。

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2019/open-file-with-app/ios-copy-to.jpg" alt="iOS - ファイルと一緒にアプリを開く">
</div>

上の状態で自分のアプリを選択するとアプリが起動してファイルがコピーされます。

また、iTunesを開いて自分のアプリを選択すると下記のように`Inbox`フォルダが生成されたことが確認できます。

![iOS - itunesファイルコピー確認](/assets/images/category/react-native/2019/open-file-with-app/itunes-inbox-file.jpg)

このファイルを外にコピーして中の内容を確認するとメールで送ったファイルと同じファイルがあることが確認できます。

![iOS - inboxファイル確認](/assets/images/category/react-native/2019/open-file-with-app/check-inbox-file.jpg)

{% include in-feed-ads.html %}

## アンドロイド
アンドロイドはiOSより少し難しいです。まず、`android/app/src/main/AndroidManifest.xml`を開いて下記のように`Intent Filter`を追加します。

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
  package="com.react_native_open_file_with">
  ...
        <intent-filter>
            <action android:name="android.intent.action.MAIN" />
            <category android:name="android.intent.category.LAUNCHER" />
        </intent-filter>
        <!-- custom file start -->
        <intent-filter
          android:icon="@mipmap/ic_launcher"
          android:label="@string/app_name">
            <action android:name="android.intent.action.VIEW" />
            <action android:name="android.intent.action.EDIT" />
            <category android:name="android.intent.category.DEFAULT" />
            <!-- change custom file extension -->
            <data
              android:mimeType="*/*"
              android:host="*"
              android:pathPattern=".*\\.temp"
            />
        </intent-filter>
        <!-- custom file end -->
  ...
</manifest>
```

ここにも`.temp`を欲しいファイル名で修正して使ってください。`MainActivity.java`ファイルを開いて下記の内容を追加します。

```java
...
import android.content.ContentResolver;
import android.content.pm.PackageInfo;
import android.content.pm.PackageManager;
import android.database.Cursor;
import android.net.Uri;
import android.provider.MediaStore;
import android.util.Log;
import java.io.File;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.OutputStream;
...

public class MainActivity extends ReactActivity {
    ...
    @Override
    protected void onResume() {
        super.onResume();
        Uri data = getIntent().getData();
        if(data != null) {
            try {
                importData(data);
            }catch (Exception e) {
                Log.e("File Import Error", e.getMessage());
            }
        }
    }

    private void importData(Uri data) {
        final String scheme = data.getScheme();

        if (ContentResolver.SCHEME_CONTENT.equals(scheme)) {
            try {
                ContentResolver cr = getApplicationContext().getContentResolver();
                InputStream is = cr.openInputStream(data);
                if(is == null) return;

                String name = getContentName(cr, data);

                PackageManager m = getPackageManager();
                String s = getPackageName();
                PackageInfo p = m.getPackageInfo(s, 0);
                s = p.applicationInfo.dataDir;

                InputStreamToFile(is, s + "/files/" + name);
            } catch (Exception e) {
                Log.e("File Import Error", e.getMessage());
            }
        }
    }

    private String getContentName(ContentResolver resolver, Uri uri){
        Cursor cursor = resolver.query(uri, null, null, null, null);
        cursor.moveToFirst();
        int nameIndex = cursor.getColumnIndex(MediaStore.MediaColumns.DISPLAY_NAME);
        if (nameIndex >= 0) {
            return cursor.getString(nameIndex);
        } else {
            return null;
        }
    }

    private void InputStreamToFile(InputStream in, String file) {
        try {
            OutputStream out = new FileOutputStream(new File(file));

            int size = 0;
            byte[] buffer = new byte[1024];

            while ((size = in.read(buffer)) != -1) {
                out.write(buffer, 0, size);
            }

            out.close();
        }
        catch (Exception e) {
            Log.e("MainActivity", "InputStreamToFile exception: " + e.getMessage());
        }
    }
    ...
}
```

上の内容はファイルを選択してアプリを実行する時、そのファイルを自分のアプリフォルダにコピーするコードです。iOSでは自動にアプリフォルダにコピーされますが、アンドロイドは上のようにアプリフォルダにコピーするようにコーディングする必要があります。

iOSでテストしたようにファイルの名前を`.temp`で修正してアンドロイドで確認できるメールに添付して送信します。メールアプリを起動して先送った`.temp`ファイルを選択するか、ダウンロードしたファイルを選択したら下記のように自分のアプリにコピーすることができます。

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2019/open-file-with-app/android-copy-to.jpg" alt="アンドロイド - ファイルと一緒にアプリを開く">
</div>


上の状態で自分のアプリを選択したらアプリが起動されてファイルがコピーされます。ファイルは`/data/user/0/[app package name]/files`に保存されます。

{% include in-feed-ads.html %}

## 活用
このようにコピーしたファイルを`react-native-fs`を使って活用する方法について説明します。ここで紹介するソースコードはリアクトネイティブ(React Native)に下記の内容を設定したプロジェクトです。それそれが気になる方は下記のリンクを確認してください。

- [typescript]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}
- [styled-components]({{site.url}}/{{page.categories}}/styled-components/){:target="_blank"}
- [リアクトネイティブ(React Native)でrootからimportする]({{site.url}}/{{page.categories}}/root-import/){:target="_blank"}
- [react-navigation]({{site.url}}/{{page.categories}}/react-navigation/){:target="_blank"}
- [NativeBase]({{site.url}}/{{page.categories}}/nativebase/){:target="_blank"}

全てのソースは下記のレポジトリ(Repository)で確認することができます。

- githubレポジトリ(Repository): [react_native_open_file_with](https://github.com/dev-yakuza/react_native_open_file_with){:target="_blank"}

リアクトネイティブ(React Native)で`react-native-fs`をインストールする方法は下記のブログを参考してください。

- [ファイルシステム使用]({{site.url}}/{{page.categories}}/react-native-fs/){:target="_blank"}

全体ソースで重要な部分だけ説明します。

```js
private _DOCUMENT_PATH = RNFS.DocumentDirectoryPath;
```

コピーされたファイルは`RNFS.DocumentDirectoryPath`に保存されます。

```js
private _loadFiles = async () => {
    if (Platform.OS === 'ios') {
        await this._moveInboxFiles();
    }

    RNFS.readDir(this._DOCUMENT_PATH)
    .then((srcFiles: Array<RNFS.ReadDirItem>) => {
        let files: Array<RNFS.ReadDirItem> = [];
        srcFiles.map((file: RNFS.ReadDirItem) => {
            if (file.isFile() && file.name.indexOf('.temp') >= 0) {
                files.push(file);
            }
        });
        this.setState({ files });
    })
    .catch(err => {
        console.log(err.message, err.code);
    });
};
```

そのフォルダを読んでファイルの場合ファイルリストに保存します。`iOS`の場合、`RNFS.DocumentDirectoryPath`中で`Inbox`フォルダに保存されます。したがって、ファイルを読む前、下記のようにそのファイルをコピーします。

```js
private _moveInboxFiles = async () => {
    try {
        const inboxFiles = await RNFS.readDir(this._DOCUMENT_PATH + '/Inbox');
        if (inboxFiles) {
            inboxFiles.map(async file => {
                if (file.isFile()) {
                    if (file.isFile()) {
                        await RNFS.moveFile(
                        file.path,
                        `${this._DOCUMENT_PATH}/${file.name}`
                        );
                    }
                }
            });
        }
    } catch (err) {
        console.log(err.message, err.code);
    }
};
```

このファイルは下記のような情報を持っています。必要な情報を自由に使ってください。

```js
const { ctime, mtime, path, name, size } = file;
```

{% include in-feed-ads.html %}

### iOSシミュレータテスト
今まで作った内容をiOSシミュレータで確認する方法を説明します。シミュレータが起動中の状態で下記のコマンドでシミュレータアイディを取得します。

```bash
xcrun simctl list | egrep '(Booted)'
```

私が作ったレポジトリ(Repository)ではnpmコマンドを作っております。`pacakage.json`を確認してください。

- githubレポジトリ(Repository): [react_native_open_file_with](https://github.com/dev-yakuza/react_native_open_file_with){:target="_blank"}

```bash
npm run get-id
iPhone X (5C0277D7-12FA-42DE-AD6D-AC3C74324B4C) (Booted)
```

コマンドを実行したら上のようにシミュレータのアイディを取得することができます。

```bash
cd /Users/[user name]/Library/Developer/CoreSimulator/Devices/5C0277D7-12FA-42DE-AD6D-AC3C74324B4C/data/Containers/Data/Application/
open .
```

そのフォルダに移動してフォルダの中を見たら今日の日付のアプリを探すことができます。アプリの下にある`Documents`フォルダにファイルをコピーします。

![シミュレータファイル](/assets/images/category/react-native/2019/open-file-with-app/simulator-files.jpg)

それでアプリを再実行や私のレポジトリ(Repository)でテストしてる方は右上のリフレッシュボタンを押します。

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2019/open-file-with-app/simulator-file-viewer.jpg" alt="iOS - シミュレータファイル表示">
</div>

そしたら上のようにファイルが上手く表示されることが確認できます。

### アンドロイドテスト
私はアンドロイドはデバイスでテストしました。アンドロイドでも下記のようにファイルが上手く表示することが確認できます。

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2019/open-file-with-app/android-file-viewer.jpg" alt="アンドロイド - デバイスファイル表示">
</div>


## 完了
最近は全てのファイルをサーバーに保存して活用してるのでこのような機能が要らないかもしれないです。それでも覚えておくといつかは使えると思います。これで特定のファイルでアプリを実行して活用する方法について見て見ました。特定のファイルでアプリを実行したい方にちょっとでも参考になったら嬉しいです。