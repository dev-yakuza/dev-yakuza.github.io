---
layout: 'post'
permalink: '/react-native/android-google-play/'
paginate_path: '/react-native/:num/android-google-play/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'register Android App store'
description: we'll introduce how to register RN(React Native) Android App to Android App store(Google Play).
image: '/assets/images/category/react-native/android-google-play.jpg'
---


## Outline
we want to register RN(React Native) Android App to Android App store(Google Play). we need to enroll Android Developer(Google Play Developer) to register Android App to Android App store(Google Play). if you didn't enroll Android Developer(Google Play Developer), see our previous blog to enroll Android Developer(Google Play Developer).

- [enroll Android developer]({{site.url}}/{{page.categories}}/android-enroll-google-play-developer/){:target="_blank"}

## Prepare
we need RN(React Native) Android App build to register Android App store(Google Play). if you don't know how to register Android Signing Key and how to build, see our previous blog.

- [Android build and test]({{site.url}}/{{page.categories}}/android-running-on-device/){:target="_blank"}

## Reduce Build File size
in previous blog([Android build and test]({{site.url}}/{{page.categories}}/android-running-on-device/){:target="_blank"}), Android build we generated is not minimum file size. we need to reduce RN(React Native) Android build file size to upload Android App store(Google Play).

open ```android/app/build.gradle``` in RN(React Native) project folder and modify like below.

```
...
defaultConfig {
    ...
    // ndk {
    //     abiFilters "armeabi-v7a", "x86"
    // }
}
...
def enableSeparateBuildPerCPUArchitecture = true
```

and then, execute below command to build RN(React Native) Android App.

```bash
# react-native bundle --platform android --dev false --entry-file index.js --bundle-output android/app/src/main/assets/index.android.bundle
# cd android
./gradlew assembleRelease
```

you can find build files on below path.

```bash
android/app/build/outputs/apk/release/app-armeabi-v7a-release.apk
android/app/build/outputs/apk/release/app-x86-release.apk
```

## Register App
click below link to go to Google Play Console..

- Google Play Console: [https://play.google.com/apps/publish/](https://play.google.com/apps/publish/){:rel="nofollow noreferrer" target="_blank"}

when you go to Google Play Console, you can see below screen.

![Google Play Console Home](/assets/images/category/react-native/android-google-play/google-play-console-home.png)

click ```PUBLISH AN ANDROID APP ON GOOGLE PLAY``` button on top of the screen.

![Google Play Console App Title](/assets/images/category/react-native/android-google-play/app-title.png)

insert App name and default language to display on Android App store(Google Play).

![Google Play Console App info](/assets/images/category/react-native/android-google-play/app-info.png)

insert App information to display on Android App store(Google Play).

- Title: 50 characters
- Short description): 80 characters
- Full description): 4000 characters
- App Screenshots
- App icon: 512x512(32-bit PNG, alpha), 1024x500(JPG or 24-bit PNG), 180x120(JPG or 24-bit PNG), 1280x720(JPG or 24-bit PNG), 4096x4096(JPG or 24-bit PNG)
- Promo Video
- App Category
- Developer's Contact details
- Privacy Policy

if you finished to insert above informations, let's see how to register apk file.

whne you click ```App release``` menu on the left of the screen, you can see below screen.

![Google Play App Register](/assets/images/category/react-native/android-google-play/app-register.png)

click ```MANAGE``` button on the ```Production``` in ```Production track``` section.

![Google Play create production app](/assets/images/category/react-native/android-google-play/app-production.png)

when you see above screen, click ```CREATE RELEASE``` on the bottom of the screen.

![Google Play register app signing key](/assets/images/category/react-native/android-google-play/register-signing-key.png)

if you want to do App Signing by Google Play, click ```FINISH``` button.

![Google Play accept agreement](/assets/images/category/react-native/android-google-play/accept-agreement.png)

when you see above screen, click ```ACCEPT``` button to accept the agreement.

![Google Play apk upload](/assets/images/category/react-native/android-google-play/app_apk.png)

upload ```apk``` file we built.

![Google Play apk release note](/assets/images/category/react-native/android-google-play/app_release_note.png)

insert App release name and note. click ```SAVE``` button on the right bottom of the screen. and then, you can see ```REVIEW``` button activate. click ```REVIEW``` button.

![Google Play register not available](/assets/images/category/react-native/android-google-play/not_yet.png)

we didn't finish all procedures to register app, so ```START ROLLOUT TO PRODUCTION``` button on right bottom of the screen is not activated. click ```Content rating``` on left menu.

![Google Play Content rating](/assets/images/category/react-native/android-google-play/app_content_rating.png)

this screen is the screen to set Content Rating. click ```CONTINUE``` button.

![Google Play insert Content Rating info](/assets/images/category/react-native/android-google-play/app_content_rating_insert_info.png)

insert your email information and select App category.

![Google Play accept Content Rating info](/assets/images/category/react-native/android-google-play/app_content_rating_agreement.png)

select App informations for Google to decide Content rating. after selecting all, click ```SAVE QUESTIONNAIRE``` button and click ```CALCULATE RATING``` if it's activate.

![Google Play completed to select Content rating info](/assets/images/category/react-native/android-google-play/app_content_rating_completed.png)

you can see the result based on the information you selected. after checking the result, click ```APPLYING RATING``` button.

![Google Play completed to set Content rating](/assets/images/category/react-native/android-google-play/calculated_content_rating.png)

completed to set Content rating. iif you have any update to affect Content rating, you should recalculate it by above procedure.

![Google Play Content rating](/assets/images/category/react-native/android-google-play/content_rating.png)

let's go to the end of the procedure. click ```Pricing & distribution``` on left menu.

![Google Play set App price info](/assets/images/category/react-native/android-google-play/app_price_info.png)

this screen is the screen to set App price. we'll provide our app for free so we configured ```FREE```. and there are questions about your app is to target the children, or your app includes advertisements, etc. after selecting all requirements, click ```SAVE DRAFT``` on the bottom of the screen.

## Apply App Review
finally, we're ready to apply App review. click ```App release``` menu.

![Google Play App review](/assets/images/category/react-native/android-google-play/app_review.png)

click ```EDIT RELEASE``` in ```Producion``` section.

![Google Play App review infor](/assets/images/category/react-native/android-google-play/app_review_info.png)

we can see contents we wrote. scroll to the bottom and click ```REVIEW``` button.

![Google Play apply App review](/assets/images/category/react-native/android-google-play/apply_app_review_info.png)

when you see above screen, scroll down and click ```START ROLLOUT TO PRODUCTION```.

![Google Play register App](/assets/images/category/react-native/android-google-play/register_app.png)

if you're ready to apply App review, click ```CONFIRM``` button.

## fix error
when you execute the command below,

```bash
./gradlew assembleRelease
```

sometime, you get the error message like below and build is failed.

```bash
Execution failed for task ':app:transformDexArchiveWithExternalLibsDexMergerForRelease'.
```

add the code below to `android/app/build.gradle` and try to build again.

```js
defaultConfig {
    ...
    multiDexEnabled true
}
```

## Completed
we've done to register App to Android App store(Google Play). App review takes 2 ~ 3 hours. if App review is finished, you can search and download your App in Android App store(Google Play).