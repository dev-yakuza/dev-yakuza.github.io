---
layout: 'post'
permalink: '/react-native/open-file-with-app/'
paginate_path: '/react-native/:num/open-file-with-app/'
lang: 'ko'
categories: 'react-native'
comments: true

title: '특정 파일로 앱 열기'
description: '웹이나 이메일로 받은 특정 파일(엑셀, 파워포인트 등)을 RN(React Native)로 제작한 앱으로 공유하는 방법에 대해서 설명합니다.'
image: '/assets/images/category/react-native/2019/open-file-with-app/background.jpg'
---

## 개요
웹이나 이메일에서 특정 파일을 다운로드 받아, 그 파일을 자신이 만든 앱으로 열고 싶을 때가 있습니다. 예를 들어 아래와 같이 pdf이나 엑셀 파일을 특정 앱으로 열도록 할 수 있습니다.

안드로이드인 경우

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2019/open-file-with-app/android-open-with.jpg" alt="안드로이드 - 파일과 함께 앱 열기">
</div>

iOS인 경우

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2019/open-file-with-app/iphone-open-with.jpg" alt="iOS - 파일과 함께 앱 열기">
</div>

위와 같이 특정 파일을 열때, 자신의 앱이 표시되도록 하는 방법과 그 파일을 활용하는 방법에 대해서 설명합니다. 이 블로그에서는 파일 확장자명이 `.temp`인 경우 앱을 실행하는 방법을 다루겠습니다.

{% include in-feed-ads.html %}

## iOS
iOS에서 파일이 앱으로 복사되었는지 확인하기 위해, 아래에 블로그를 통해 앱의 iTunes 파일 공유 기능을 활성화시킵니다.

- [iTunes 파일 공유 기능]({{site.url}}/{{page.categories}}/react-native-itunes-share-file/){:target="_blank"}

이제 iOS에서 특정 파일을 자신의 앱으로 열게 하기 위해, `ios/[project name]/Info.plist`를 열고 아래에 내용을 추가합니다.

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

다시 한번 말씀 드리지만, 위에 내용은 `.temp`로 끝나는 파일을 자신의 앱으로 열 경우에 사용하는 내용입니다. `<!-- change custom file extension -->`으로 주석이 달린 3곳을 자신이 원하는 파일로 수정하여 사용하시기 바랍니다.

우선 iTunes를 열어 파일 공유 기능이 활성화 되어 있는지 확인합니다.

![iOS - itunes 파일 공유 기능 확인](/assets/images/category/react-native/2019/open-file-with-app/itunes-no-file.jpg)

테스트를 위해 아무 파일이나 파일 확장자를 `.temp`로 수정한 후 iOS에서 확인이 가능한 이메일 파일을 첨부하여 발송합니다. 이메일 앱을 열고 방금전 보낸 `.temp`파일을 선택하고 오른쪽 위에 공유 버튼을 누르면 아래와 같이 자신의 앱으로 파일을 복사할 수 있습니다.

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2019/open-file-with-app/ios-copy-to.jpg" alt="iOS - 파일과 함께 앱 열기">
</div>

위에서 자신의 앱을 선택하면 앱이 실행되며 파일이 복사됩니다.

다시 iTunes를 열어 자신의 앱을 선택하면 아래와 같이 `Inbox` 폴더가 생성되어있는 것을 확인할 수 있습니다.

![iOS - itunes 파일 복사 확인](/assets/images/category/react-native/2019/open-file-with-app/itunes-inbox-file.jpg)

그 파일을 밖으로 복사하여 안에 내용을 확인하면 이메일로 보낸 파일과 동일함을 알 수 있습니다.

![iOS - inbox 파일 확인](/assets/images/category/react-native/2019/open-file-with-app/check-inbox-file.jpg)

{% include in-feed-ads.html %}

## 안드로이드
안드로이드는 iOS보다 조금 더 복잡합니다. 우선 `android/app/src/main/AndroidManifest.xml`을 열고 아래와 같이 `Intent Filter`를 추가합니다.

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

여기에서도 `.temp`를 원하는 파일명으로 수정하여 사용하시기 바랍니다. `MainActivity.java` 파일을 열고 아래 내용을 추가합니다.

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

위에 내용은 파일을 선택하여 앱을 실행할 경우, 해당 파일을 자신의 앱 폴더로 복사하는 코드입니다. iOS에서는 자동으로 앱 폴더로 복사하지만, 안드로이드는 위와 같이 앱 폴더로 복사하도록 코딩해야 합니다.

iOS에서 테스트한 것과 동일하게 아무 파일이나 파일 확장자를 `.temp`로 수정한 후 안드로이드에서 확인이 가능한 이메일 파일을 첨부하여 발송합니다. 이메일 앱을 열고 방금전 보낸 `.temp`파일을 선택하거나, 다운로드 받은 파일을 선택하면 아래와 같이 자신의 앱으로 파일을 복사할 수 있습니다.

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2019/open-file-with-app/android-copy-to.jpg" alt="안드로이드 - 파일과 함께 앱 열기">
</div>

위에서 자신의 앱을 선택하면 앱이 실행되며 파일이 복사됩니다. 파일은 `/data/user/0/[app package name]/files`에 저장이 됩니다.

{% include in-feed-ads.html %}

## 활용
이렇게 자신에 앱으로 복사한 파일을 `react-native-fs`를 사용하여 활용하는 방법에 대해서 알아봅시다. 여기서 소개할 소스코드는 RN(React Native)에 아래에 내용이 설정된 프로젝트입니다. 각각에 대해 궁금하신 분들은 아래에 링크를 확인하세요.

- [typescript]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}
- [styled-components]({{site.url}}/{{page.categories}}/styled-components/){:target="_blank"}
- [RN(React Native)에서 root import하기]({{site.url}}/{{page.categories}}/root-import/){:target="_blank"}
- [react-navigation]({{site.url}}/{{page.categories}}/react-navigation/){:target="_blank"}
- [NativeBase]({{site.url}}/{{page.categories}}/nativebase/){:target="_blank"}

전체 소스는 아래에 저장소(Repository)에서 확인할 수 있습니다.

- github 저장소(Repository): [react_native_open_file_with](https://github.com/dev-yakuza/react_native_open_file_with){:target="_blank"}

RN(React Native)에 `react-native-fs`를 설치하는 방법은 아래에 블로그를 참고하시기 바랍니다.

- [파일 시스템 사용]({{site.url}}/{{page.categories}}/react-native-fs/){:target="_blank"}

전체 소스에서 중요 부분만 설명하도록 하겠습니다.

```js
private _DOCUMENT_PATH = RNFS.DocumentDirectoryPath;
```

복사된 파일은 `RNFS.DocumentDirectoryPath`에 저장됩니다.

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

해당 폴더에 파일을 읽고 파일인 경우 파일 리스트에 저장합니다. `iOS`인 경우, `RNFS.DocumentDirectoryPath`안에 `Inbox` 폴더에 저장됩니다. 따라서 파일을 읽기 전에 아래와 같이 해당 파일들을 복사합니다.

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

이 파일들은 아래와 같은 정보를 가지고 있습니다. 필요한 정보를 자유롭게 사용하시면 됩니다.

```js
const { ctime, mtime, path, name, size } = file;
```

{% include in-feed-ads.html %}

### iOS 시뮬레이터 테스트
지금까지 작업한 내용을 iOS 시뮬레이터에서 확인하는 방법에 대해서 설명합니다. 시뮬레이터가 기동중인 상태에서 아래에 명령어로 시뮬레이터 아이디를 얻습니다.

```bash
xcrun simctl list | egrep '(Booted)'
```

제가 작성한 저장소(Repository)에서는 npm 명령어로 만들어 두었습니다. `pacakage.json`을 확인해 주세요.

- github 저장소(Repository): [react_native_open_file_with](https://github.com/dev-yakuza/react_native_open_file_with){:target="_blank"}

```bash
npm run get-id
iPhone X (5C0277D7-12FA-42DE-AD6D-AC3C74324B4C) (Booted)
```

명령어를 사용하면 위와 같이 시뮬레이터의 아이디를 얻을 수 있습니다.

```bash
cd /Users/[user name]/Library/Developer/CoreSimulator/Devices/5C0277D7-12FA-42DE-AD6D-AC3C74324B4C/data/Containers/Data/Application/
open .
```

해당 폴더로 이동하고 폴더안을 보면 아래와 같이 현재 날짜의 앱을 찾을 수 있습니다. 앱 하단의 `Documents`에 파일을 복사합니다.

![시뮬레이터 파일](/assets/images/category/react-native/2019/open-file-with-app/simulator-files.jpg)

그리고 앱을 재실행 또는 제 저장소(Repository)로 테스트를 하시는 분은 오른쪽 위에 새로고침 버튼을 선택합니다.

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2019/open-file-with-app/simulator-file-viewer.jpg" alt="iOS - 시뮬레이터 파일 표시">
</div>

그러면 위와 같이 파일이 잘 표시되는 것을 확인할 수 있습니다.


### 안드로이드 테스트
저는 안드로이드는 디바이스에서 테스트했습니다. 안드로이드도 아래와 같이 파일이 표시되는 것을 확인할 수 있습니다.

<div class="half_image_container">
    <img class="half_image" src="/assets/images/category/react-native/2019/open-file-with-app/android-file-viewer.jpg" alt="안드로이드 - 디바이스 파일 표시">
</div>


## 완료
요즘은 모든 파일을 서버에 저장하고 활용하기 때문에 이와 같은 처리가 필요없는 경우가 많습니다. 그래도 잘 알아두면 유용하게 사용하실 수 있을거 같네요. 이로써 특정 파일로 앱을 실행하고 활용하는 방법에 대해서 알아보았습니다. 특정 파일로 앱 실행에 어려움을 겪는 분들에게 참고가 되면 좋겠습니다.