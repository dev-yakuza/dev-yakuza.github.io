---
published: false
layout: 'post'
permalink: '/html-css-js/protect-tabnabbing/'
paginate_path: '/html-css-js/:num/protect-tabnabbing/'
lang: 'ko'
categories: 'html-css-js'
comments: true

title: '특정 파일로 앱 열기'
description: '웹이나 이메일로 받은 특정 파일(엑셀, 파워포인트 등)을 RN(React Native)로 제작한 앱으로 공유하는 방법에 대해서 설명합니다.'
image: '/assets/images/category/html-css-js/2019/protect-tabnabbing/background.jpg'
---

{% include in-feed-ads.html %}

https://medium.com/@youngminhong/tabnabbing-%EA%B3%B5%EA%B2%A9-%EB%B0%A9%EC%96%B4-%EB%8C%80%EC%B1%85-%EC%A0%95%EB%A6%AC-9276ebf63f94

https://developers.google.com/web/tools/lighthouse/audits/noopener?hl=ko

https://blog.coderifleman.com/2017/05/30/tabnabbing_attack_and_noopener/?fbclid=IwAR3tHOPKgv08gLPOwAouOLhFNYciJ8qGvq9_pgTPC14xyDK8Y_vG9TsdIjc
## 개요
웹이나 이메일에서 특정 파일을 다운로드 받아, 그 파일을 자신이 만든 앱으로 열고 싶을 때가 있습니다. 예를 들어 아래와 같이 pdf이나 엑셀 파일을 특정 앱으로 열도록 할 수 있습니다.

안드로이드인 경우

![안드로이드 - 파일과 함께 앱 열기](/assets/images/category/react-native/2019/open-file-with-app/android-open-with.jpg)

iOS인 경우

![iOS - 파일과 함께 앱 열기](/assets/images/category/react-native/2019/open-file-with-app/ios-open-with.jpg)


위와 같이 특정 파일을 열때, 자신의 앱이 표시되도록 하는 방법과 그 파일을 활용하는 방법에 대해서 설명합니다. 이 블로그에서는 `.temp`의 파일로 파일


## iOS
iOS에서 파일이 잘 앱으로 복사되었는지 확인하기 위해, 아래에 블로그를 통해 앱의 iTunes 파일 공유 기능을 활성화시킵니다.

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

![iOS - 파일과 함께 앱 열기](/assets/images/category/react-native/2019/open-file-with-app/iphone-open-with.jpg)

위에서 자신의 앱을 선택하면 앱이 실행되며 파일이 복사됩니다.

다시 iTunes를 열어 자신의 앱을 선택하면 아래와 같이 `Inbox` 폴더가 생성되어있는 것을 확인할 수 있습니다.

![iOS - itunes 파일 복사 확인](/assets/images/category/react-native/2019/open-file-with-app/itunes-inbox-file.jpg)

그 파일을 밖으로 복사하여 안에 내용을 확인하면 이메일로 보낸 파일과 동일함을 알 수 있습니다.

![iOS - inbox 파일 확인](/assets/images/category/react-native/2019/open-file-with-app/check-inbox-file.jpg)


## 안드로이드
안드로이드는 iOS보다 조금 더 복잡합니다. 우선 `android/app/src/main/AndroidManifest.xml`을 열고 아래와 같이 `Intert Filter`를 추가합니다.

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


