---
layout: 'post'
permalink: '/react-native/react-native-itunes-share-file/'
paginate_path: '/react-native/:num/react-native-itunes-share-file/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'iTunes file sharing feature'
description: let's see how to share files vie iTunes on RN(React Native) project.
image: '/assets/images/category/react-native/react-native-itunes-share-file/background.jpg'
---


## Outline
sometimes, we need to upload files to RN(React Native) app from PC via iTunes. for example, the video app like [OPlayer](https://itunes.apple.com/app/oplayer-video-player-classic-media-streaming/id344784375?mt=8&ign-mpt=uo%3D8){:rel="nofollow noreferrer" target="_blank"} or [GomPlayer](https://itunes.apple.com/app/gom-player/id672542880?mt=8){:rel="nofollow noreferrer" target="_blank"} can be uploaded the video files vi iTunes.

in this blog, I'll introduce how to implement the feature to upload the file from PC to the app via iTunes.


## More Details
someone doesn't understand what this feature yet, so I'll explain more details about what we implement. when you connect your iOS device to PC via USB, you can see iTunes is executed.

![connect iOS device to itunes](/assets/images/category/react-native/react-native-itunes-share-file/connect-itunes.png)

after connecting iOS device to PC, you can see the phone icon on the top of iTunes. click the icon.

![device info on itunes](/assets/images/category/react-native/react-native-itunes-share-file/iphone-info.png)

you can see iOS device info. click ```File Sharing``` on the left menu. you can see the app list that has the file sharing feature via iTunes.

![itunes file sharing](/assets/images/category/react-native/react-native-itunes-share-file/upload-file.png)

in here, I selected ```OPlayer``` app and dragged```video.mp4``` file from PC to the app for uploading.

in this blog, we'll talk about how to implement this feature that users upload the files from PC to the app via iTunes.


## Prepare Device
we need to install the app on the device for testing. if you don't know how to install RN(React Native) app on iOS device, see the blog post below.

- [iOS device test]({{site.url}}/{{page.categories}}/ios-test-on-device/){:target="_blank"}


## Modify info.plist
we don't need to modify the source code for this feature. we just need to modify ```info.plist``` to implement iTunes file sharing feature.

open ```ios/[project name]/info.plist``` file in RN(React Native) project modify it like below.

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    ...
    <key>UIFileSharingEnabled</key>
    <true/>
    ...
</dict>
</plist>
```

## How To Use
you can implement iTunes file sharing feature to modify ```info.plist```. also you can use the file uploaded via iTunes by using ```react-native-fs```.

- [How to use filesystem]({{site.url}}/{{page.categories}}/react-native-fs/){:target="_blank"}

you can access the file uploaded via iTunes by using ```DocumentDirectoryPath``` of ```react-native-fs```.


## Simulator
According to what we said above, you should install RN(React Native) app to the device and upload the file via iTunes. it looks like always test on the device, in fact we can test this feature on the simulator.

execute the command below to start the project.

```bash
react-native run-ios
```

after the simulator is executed with the app, execute the command below to get the simulator id.

```bash
xcrun simctl list | egrep '(Booted)'
```

and then, implement ```react-native-device-info``` library to get the app ```unique id```.

- [react-native-device-info]({{site.url}}/{{page.categories}}/react-native-device-info/){:target="_blank"}

after getting the simulator id and app unique id, you can copy the file to ```/Users/[user name]/Library/Developer/CoreSimulator/Devices/[simulator id]/data/Container/Data/Application/[app id]/Documents/``` folder. it's same action that you upload the file via iTunes.


## Completed
we've talked about how to implement the feature that the app need to be uploaded the files by users like music app or movie app. also, we've talked about how to acceess the files and how to test on the simulator. if you also need the users need specific files to use your app but you don't have the server, it's one of the good solution to solve it.