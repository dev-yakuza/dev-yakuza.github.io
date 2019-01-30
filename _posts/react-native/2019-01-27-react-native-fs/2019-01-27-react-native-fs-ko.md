---
layout: 'post'
permalink: '/react-native/react-native-fs/'
paginate_path: '/react-native/:num/react-native-fs/'
lang: 'ko'
categories: 'react-native'
comments: true

title: '파일 시스템 사용'
description: 'RN(React Native) 프로젝트에서 react-native-fs 라이브러리를 사용하여 파일을 읽고 써봅시다.'
image: '/assets/images/category/react-native/react-native-fs.jpg'
---


## 개요
RN(React Native)로 개발할 때, 종종 파일 시스템(filesystem)을 이용하여 파일을 읽고 쓸 경우가 생깁니다. ```react-native-fs```는 RN(React Naitve)에서 파일 시스템(filesystem)을 쉽고 간단하게 사용할 수 있도록 도와주는 라이브러리입니다. 이 블로그에서는 ```react-native-fs```를 사용하는 방법에 대해서 알아보겠습니다.

- react-native-fs 공식 사이트: [https://github.com/itinance/react-native-fs](https://github.com/itinance/react-native-fs){:rel="nofollow noreferrer" target="_blank"}

## 설치
RN(React Native)에서 파일 시스템(filesystem)을 사용하기 위해 아래에 명령어를 통해 ```react-native-fs```를 설치합니다.

```bash
npm install --save react-native-fs
```

설치가 완료되면 아래에 명령어로 ```react-native-fs```를 RN(React Native) 프로젝트와 연결합니다.

```bash
react-native link react-native-fs
```

## 사용 방법
파일시스템(filesystem)을 이용하여 파일을 읽고 쓰는 다양한 방법이 [공식 사이트](https://github.com/chirag04/react-native-mail){:rel="nofollow noreferrer" target="_blank"}에 자세히 나와있습니다. 여기에서는 간단하게 파일을 읽고 쓰는 부분에 대해서 알아보겠습니다.

### 디렉토리
아래는 ```react-native-fs```에서 정의하는 파일시스템의 디렉토리/패스(filesystem directory/path)입니다.

- MainBundlePath: 메인 번들 폴더(Main Bundle Directory)의 절대 위치입니다.(안드로이드에서는 사용이 불가능합니다.)
- CachesDirectoryPath: 캐시 폴더(Cache Directory)의 절대 위치입니다.
- ExternalCachesDirectoryPath: 외부 캐시 폴더(External Cache Directory)의 절대 위치입니다.(iOS에서는 사용이 불가능합니다.)
- DocumentDirectoryPath: 도큐먼트 폴더(Document Directory)의 절대 위치입니다.
- TemporaryDirectoryPath: 임시 폴더(Temporary Directory)의 절대 위치입니다.(안드로이드는 캐시 폴더가 전달됩니다.)
- LibraryDirectoryPath: iOS의 NSLibraryDirectory의 절대 위치입니다.(안드로이드에서는 사용이 불가능합니다.)
- ExternalDirectoryPath: 외부 파일 공유 폴더(External files, shared directory)의 절대 위입니다.(iOS에서는 사용이 불가능합니다.)
- ExternalStorageDirectoryPath: 외부 저장소 공유 폴더(External storage, shared directory)의 절대 위치입니다.(iOS에서는 사용이 불가능합니다.)

### 폴더 읽기
아래는 RN(React Native)에서 ```react-native-fs```를 사용하여 폴더를 읽는 방법에 대한 코드입니다.

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

### 파일 읽기
아래는 RN(React Native)에서 ```react-native-fs```를 사용하여 파일을 읽는 방법에 대한 코드입니다.

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

### 파일 쓰기
아래는 RN(React Native)에서 ```react-native-fs```를 사용하여 파일을 쓰는 방법에 대한 코드입니다.

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

### 파일 삭제
아래는 RN(React Native)에서 ```react-native-fs```를 사용하여 파일을 삭제하는 방법에 대한 코드입니다.

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

## 다른 기능들
react-native-fs에서 사용 가능한 기능을 공통/iOS/안드로이드별로 정리하였습니다.
자세한 내용은 공식 사이트를 참고하세요.

- react-native-fs 공식 사이트: [https://github.com/itinance/react-native-fs](https://github.com/itinance/react-native-fs){:rel="nofollow noreferrer" target="_blank"}

### 공통
아래의 리스트는 ```react-native-fs```에서 OS와 상관없이 공통으로 사용이 가능한 기능입니다.

- readDir(dirpath: string): 파라메터로 전달받은 절대 위치(Absolute path)의 폴더를 읽는다.
- readdir(dirpath: string): Nodejs 스타일의 ```readDir```
- stat(filepath: string): 전달받은 파일 위치의 파일 상태를 가져온다.
- readFile(filepath: string, encoding?: string): 전달 받은 파일 위치의 파일을 읽는다. encoding은 utf8(default), ascii, base64를 지원하며 base64는 바이너리 파일을 읽는데 사용된다.
- read(filepath: string, length = 0, position = 0, encodingOrOptions?: any): 전달받은 파일 위치의 파일에 특정 위치(position)에서 길이(length)만큼 파일 내용을 읽어온다. encoding은 readFile과 동일하다.
- writeFile(filepath: string, contents: string, encoding?: string): 지정한 파일 위치에 파일을 기록합니다.
- appendFile(filepath: string, contents: string, encoding?: string): 지정한 파일에 전달한 파일 내용을 추가합니다.
- write(filepath: string, contents: string, position?: number, encoding?: string): 파일의 특정 위치(position)에 전달받은 파일 내용을 추가합니다.
- moveFile(filepath: string, destPath: string): 파일을 이동시킵니다.
- copyFile(filepath: string, destPath: string): 파일을 복사합니다.
- unlink(filepath: string): 파일을 삭제합니다.
- exists(filepath: string): 파일의 존재 여부를 확인합니다. 파일이 존재하지 않는 경우 ```false```를 반환합니다.
- hash(filepath: string, algorithm: string): 전달받은 파일 위치의 파일에서 해당 알고리즘(algorithm)의 checksum을 반환합니다. 알고리즘(algorithm)에는 md5, sha1, sha224, sha256, sha384, sha512가 사용 가능합니다.
- touch(filepath: string, mtime?: Date, ctime?: Date): 파일의 수정일(mtime)과 생성일(ctime)을 갱신합니다. iOS에서는 생성일(ctime)만 수정하는 것이 가능하며, 안드로이드에서는 수정일(mtime)을 이용하여 수정일과 생성일을 항상 동시에 갱신합니다.
- mkdir(filepath: string, options?: MkdirOptions): 폴더를 생성합니다.
- downloadFile(options: DownloadFileOptions): 전달받은 옵션(options)안의 파일 URL을 이용하여 파일을 다운로드합니다.
- stopDownload(jobId: number): 전달받은 다운로드 아이디를 이용하여 다운로드를 중지합니다.
- getFSInfo(): 파일 시스템의 정보(총 용량, 사용 가능한 용량)를 반환합니다.

### iOS 전용
아래의 리스트는 ```react-native-fs```에서 iOS에서만 사용 가능한 기능들입니다.

- copyAssetsFileIOS(imageUri: string, destPath: string, width: number, height: number, scale : number = 1.0, compression : number = 1.0, resizeMode : string = 'contain' ): (iOS) iOS의 카메라롤(Camera-roll)에 존재하는 파일을 복사합니다.
- resumeDownload(jobId: number): (iOS) 전달받은 다운로드 아이디를 이용하여 다운로드를 다시 시작합니다.
- isResumable(jobId: number): (iOS) 전달받은 다운로드 아이디를 이용하여 다시 다운로드가 가능한지 여부를 확인합니다.
- completeHandlerIOS(jobId: number): (iOS) 백그라운드에서 다운로드를 진행하는 경우 다운로드가 완료되었음을 알려주도록 설정이 가능합니다.
- uploadFiles(options: UploadFileOptions): (iOS) 파일을 업르드합니다.
- stopUpload(jobId: number): (iOS) 파일 업로드를 중지합니다.
- pathForGroup(groupIdentifier: string): (iOS) iOS에서 ```com.apple.security.application-groups``` 설정한 모든 값을 반환합니다.

### 안드로이드 전용
아래의 리스트는 ```react-native-fs```에서 안드로이드(Android)에서만 사용 가능한 기능들입니다.

- existsAssets(filepath: string): (안드로이드) 안드로이드의 assets 폴더의 파일이 존재하는지 여부를 확인합니다. 파일이 존재하지 않는 경우 ```false```를 반환합니다.
- readFileAssets(filepath:string, encoding?: string): (안드로이드) 안드로이드의 assets 폴더의 하위에 있는 파일을 파일 위치를 통해 읽어온다.
- copyFileAssets(filepath: string, destPath: string): (안드로이드) 파일을 안드로이드의 assets 폴더 하위로 복사합니다.
- readDirAssets(dirpath: string): (안드로이드) 파라메터로 전달받은 안드로이드의 assets 폴더 하위의 상대 위치(Relative path)의 내용을 읽는다.
- scanFile(path: string): (안드로이드) ```Media Scanner```를 이용하여 파일을 스캔(scan)합니다.
- getAllExternalFilesDirs(): (안드로이드) 모든 공유/외부 스토리의 정보를 반환합니다.


## 완료
RN(React Native)에서 파일 시스템을 활용할 경우 ```react-native-fs```를 사용하는 것을 추천합니다. OS에 의존하는 기능들도 있지만, 대부분 공통 기능들로도 충분히 활용이 가능합니다. 반환값(Return Value)이나 파라메터(Parameter)에 대한 자세한 설명은 하지않았습니다. 반환값(Return Value)이나 파라메터(Parmeter)에 대한 자세한 내용은 공식 사이트를 참고하시기 바랍니다.


## 참고
- react-native-fs 공식 사이트: [https://github.com/itinance/react-native-fs](https://github.com/itinance/react-native-fs){:rel="nofollow noreferrer" target="_blank"}