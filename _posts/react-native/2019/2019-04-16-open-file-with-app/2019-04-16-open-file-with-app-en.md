---
layout: 'post'
permalink: '/react-native/open-file-with-app/'
paginate_path: '/react-native/:num/open-file-with-app/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'Open the app with the specific file'
description: this blog post is about how to open RN(React Native) app with the specific file(like excel, powerpoint, etc).
image: '/assets/images/category/react-native/2019/open-file-with-app/background.jpg'
---

## Outline
sometimes, we download the specific file from the web or the email, and want to open them with our app. for example, open the specific app with pdf file or excel file like below.

in Android,

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2019/open-file-with-app/android-open-with.jpg" alt="Android - open the app with file">
</div>

in iOS,

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2019/open-file-with-app/iphone-open-with.jpg" alt="iOS - open the app with file">
</div>

this blog is about how to open your app when we open the specific file like above and how to use the specific file in your app. in this blog, we'll use `.temp` file to execute the app.

{% include in-feed-ads.html %}

## iOS
let's activate iTunes file share feature to check the specific file is copied well in iOS.

- [iTunes file sharing feature]({{site.url}}/{{page.categories}}/react-native-itunes-share-file/){:target="_blank"}

and then, modify `ios/[project name]/Info.plist` like below to open the app with the specific file on iOS.

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

I mention again, above is to open the app with `.temp` file. change 3 parts(`<!-- change custom file extension -->` comments) to the file type you want to use.

first, open iTunes to check the file share feature is activated.

![iOS - check itunes file share feature](/assets/images/category/react-native/2019/open-file-with-app/itunes-no-file.jpg)

for testing, change a file name to `.temp` and send an email with it. open the email app on iOS and select `.temp` file. when you click the share button on the right top, you can see that you can copy the file to your app.

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2019/open-file-with-app/ios-copy-to.jpg" alt="iOS - open the app with the custom file">
</div>

if you select your app, the file will be copied in your app.

open iTunes again, and select your app. you cann see `Inbox` folder is created.

![iOS - check file is copied on itunes](/assets/images/category/react-native/2019/open-file-with-app/itunes-inbox-file.jpg)

copy that folder to outside. you can see the same file which you sent via the email.

![iOS - check the inbox file](/assets/images/category/react-native/2019/open-file-with-app/check-inbox-file.jpg)

{% include in-feed-ads.html %}

## Android
Android is more difficult than iOS. first, add `Intent Filter` in `android/app/src/main/AndroidManifest.xml`.

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

in here also, you would change `.temp` to the file name that you want to use. open and edit `MainActivity.java` file like below.

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

above is when you open the app with the file, copy the file to your app. on iOS, the file is copied automatically, but on Android, we need the code the file is copied on the app.

rename any file to `.temp` and send the email with it like iOS test. open the email app and select `.temp` file that you sent or download the file and select it. you can see your app on the copy menu.

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2019/open-file-with-app/android-copy-to.jpg" alt="Android - open the app with the custom file">
</div>

the file is copied when you select your app on the menu. the file is located on `/data/user/0/[app package name]/files`.

{% include in-feed-ads.html %}

## How To Use.
let's see how to use the file that is copied on above with `react-native-fs`. I'll use RN(React Native) project that applied below list. if you want to know more details, see the links.

- [typescript]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}
- [styled-components]({{site.url}}/{{page.categories}}/styled-components/){:target="_blank"}
- [Make Import path based on Root in RN(React Native)]({{site.url}}/{{page.categories}}/root-import/){:target="_blank"}
- [react-navigation]({{site.url}}/{{page.categories}}/react-navigation/){:target="_blank"}
- [NativeBase]({{site.url}}/{{page.categories}}/nativebase/){:target="_blank"}

you can see full source code on the repository below.

- github repository: [react_native_open_file_with](https://github.com/dev-yakuza/react_native_open_file_with){:target="_blank"}

you can see how to install `react-native-fs` on the blog post below.

- [Use Filesystem]({{site.url}}/{{page.categories}}/react-native-fs/){:target="_blank"}

let's see the main part of the source code.

```js
private _DOCUMENT_PATH = RNFS.DocumentDirectoryPath;
```

you can access the copied file by `RNFS.DocumentDirectoryPath`.

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

read the folder and if it is the file, push the file to the file list. in `iOS`, the file is located on `Inbox` in `RNFS.DocumentDirectoryPath`. so, before reading the files, copy the files from `Inbox`.

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

these files have the information below. you can use them.

```js
const { ctime, mtime, path, name, size } = file;
```

{% include in-feed-ads.html %}

### Test On iOS Simulator
let's see how to test on iOS simulator. after executing the simulator, execute the code below to get the simulator id.

```bash
xcrun simctl list | egrep '(Booted)'
```

I made npm command in my repository. check `package.json`.

- github repository: [react_native_open_file_with](https://github.com/dev-yakuza/react_native_open_file_with){:target="_blank"}

```bash
npm run get-id
iPhone X (5C0277D7-12FA-42DE-AD6D-AC3C74324B4C) (Booted)
```

after executing the command, you can get the simulator id.

```bash
cd /Users/[user name]/Library/Developer/CoreSimulator/Devices/5C0277D7-12FA-42DE-AD6D-AC3C74324B4C/data/Containers/Data/Application/
open .
```

you can see the app created at today on the folder above. copy the file to `Documents` folder in the app folder.

![copy the file to the simulator](/assets/images/category/react-native/2019/open-file-with-app/simulator-files.jpg)

after it, execute the app or if you use my repository, select the refresh button on the right top.

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2019/open-file-with-app/simulator-file-viewer.jpg" alt="iOS - show file list on the simulator">
</div>

after then, you can see the file list like above.

### Test on Android
I've tested Android on the device. you can see the file list is displayed well on Android.

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2019/open-file-with-app/android-file-viewer.jpg" alt="Android - show file list on Android device">
</div>


## Completed
recently, we save and use all files on the servers, so this feature may not be needed. however, I think someday we can use it if we know it. we saw how to open the app with the specific file and use it. I hope this blog post is helpful for someone to implement to open the app with a specific file.