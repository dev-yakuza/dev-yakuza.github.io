---
layout: 'post'
permalink: '/react-native/react-native-fs/'
paginate_path: '/react-native/:num/react-native-fs/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'Use Filesystem'
description: let's read and write the file by react-native-fs on RN(React Native) project.
image: '/assets/images/category/react-native/react-native-fs.jpg'
---


## Outline
sometimes, I need to read or write files to use the filesystem when I develop RN(React Native) project. ```react-native-fs``` is the library that can make you use the filesystem easily on RN(React Native). in this blog, we'll introduce how to use ```react-native-fs```.

- react-native-fs official site: [https://github.com/itinance/react-native-fs](https://github.com/itinance/react-native-fs){:rel="nofollow noreferrer" target="_blank"}

## Installation
execute below command to install ```react-native-fs``` to use the filesystem on RN(React Native).

```bash
npm install --save react-native-fs
```

after installing, execute below command to link ```react-native-fs``` to RN(React Native) project.

```bash
react-native link react-native-fs
```

## How To Use
you can see many features about how to read and write files on [official site](https://github.com/chirag04/react-native-mail){:rel="nofollow noreferrer" target="_blank"}. in here, we'll introduce simply how to read and write files.

### Directory
below list is the filesystem directory/path defined at ```react-native-fs```.

- MainBundlePath: absolute path of Main Bundle Directory. (not available on Android)
- CachesDirectoryPath: absolute paht of Cache Directory.
- ExternalCachesDirectoryPath: absolute path of External Cache Directory. (not available on iOS)
- DocumentDirectoryPath: absolute path of Document Directory.
- TemporaryDirectoryPath: absolute path of Temporary Directory. (same with Cache Directory on Android)
- LibraryDirectoryPath: absolute path of iOS NSLibraryDirectory. (not available on Android)
- ExternalDirectoryPath: absolute path of External files, shared directory. (not available on iOS)
- ExternalStorageDirectoryPath: absolute path of External storage, shared directory. (not available on iOS)

### Read Folder
below code is about how to read the folder by ```react-native-fs``` on RN(React Native) project.

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

### Read File
below code is about how to read the file by ```react-native-fs``` on RN(React Native) project.

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

### Write File
below code is about how to write the file by ```react-native-fs``` on RN(React Native) project.


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

### Delete File
below code is about how to delete the file by ```react-native-fs``` on RN(React Native) project.


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

## Other Features
below is features about common/iOS/Android.
if you want more details, see official site.

- react-native-fs official site: [https://github.com/itinance/react-native-fs](https://github.com/itinance/react-native-fs){:rel="nofollow noreferrer" target="_blank"}

### Common
below is common features which are not depend on OS at ```react-native-fs```.

- readDir(dirpath: string): read the folder of absolute path.
- readdir(dirpath: string): Nodejs style of ```readDir```
- stat(filepath: string): get file status of absolute path.
- readFile(filepath: string, encoding?: string): read the file of absolute path. encoding can be utf8(default), ascii and base64. base64 can be used for the binary file.
- read(filepath: string, length = 0, position = 0, encodingOrOptions?: any): read length bytes from the position of the file. encoding is same with readFile.
- writeFile(filepath: string, contents: string, encoding?: string): write the file on specifi file path.
- appendFile(filepath: string, contents: string, encoding?: string): add file contents to the file on the specific path.
- write(filepath: string, contents: string, position?: number, encoding?: string): add file contents to the position of the file.
- moveFile(filepath: string, destPath: string): move the file.
- copyFile(filepath: string, destPath: string): copy the file.
- unlink(filepath: string): delete the file.
- exists(filepath: string): check if file is exists. if file is not exists, return ```false```.
- hash(filepath: string, algorithm: string): get checksum of the file. the algorithm can be md5, sha1, sha224, sha256, sha384 and sha512.
- touch(filepath: string, mtime?: Date, ctime?: Date): renew file modified time(mtime) and created time(ctime). to renew only file created time(ctime) is possible on iOS, but Android renews file modified time and created time by file modified time(mtime) parameter.
- mkdir(filepath: string, options?: MkdirOptions): create the folder.
- downloadFile(options: DownloadFileOptions): download form the url in options parameter.
- stopDownload(jobId: number): stop to download by using download ID parameter.
- getFSInfo(): get the filesystem info(total space, free space).

### iOS Only
you can use below features of ```react-native-fs`` on only iOS.

- copyAssetsFileIOS(imageUri: string, destPath: string, width: number, height: number, scale : number = 1.0, compression : number = 1.0, resizeMode : string = 'contain' ): (iOS) copy the file that is exists on iOS Camera-roll.
- resumeDownload(jobId: number): (iOS) resume to download by using the download ID.
- isResumable(jobId: number): (iOS) check if download ID is possible to resume to download.
- completeHandlerIOS(jobId: number): (iOS) you can set the handler to know background download is completed.
- uploadFiles(options: UploadFileOptions): (iOS) upload the file.
- stopUpload(jobId: number): (iOS) stop to upload the file.
- pathForGroup(groupIdentifier: string): (iOS) get all values of  ```com.apple.security.application-groups```.

### Android Only
you can use below features of ```react-native-fs`` on only Android.

- existsAssets(filepath: string): (Android) check if the file is exists in Android assets folder. if the file is not exists, return ```false```.
- readFileAssets(filepath:string, encoding?: string): (Android) read the file in Android assets folder.
- copyFileAssets(filepath: string, destPath: string): (Android) copy the file from Android assets folder to destination path.
- readDirAssets(dirpath: string): (Android) read the folder in Android assets folder.
- scanFile(path: string): (Android) scan files by using ```Media Scanner```.
- getAllExternalFilesDirs(): (Android) get all shared/external files and directories.


## Completed
if you want to use the filesystem on RN(React Native), we recommend to use ```react-native-fs```. there are features depends on OS, but there are also many common features. we've not explain details about return values and parameters. if you want to know the details about return values and parameters, see the official site.


## Reference
- react-native-fs official site: [https://github.com/itinance/react-native-fs](https://github.com/itinance/react-native-fs){:rel="nofollow noreferrer" target="_blank"}