---
layout: 'post'
permalink: '/react-native/android-running-on-device/'
paginate_path: '/react-native/:num/android-running-on-device/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'Android build and test'
description: introduce how to build and test RN(react native) project on Android device.
image: '/assets/images/category/react-native/android-running-on-device.jpg'
---


## outline
we will introduce how to build and test RN(react native) project  we've developed on Android device. in this blog, we will use Mac to create Android Signing Key and build. we refer RN(react native) official site so if you want to know details, see official site.

- official site: [https://facebook.github.io/react-native/docs/signed-apk-android](https://facebook.github.io/react-native/docs/signed-apk-android){:rel="nofollow noreferrer" target="_blank"}

## create Android Signing Key
open ```terminal``` program on Mac and go to ```android/app``` in RN(react native) project.

```bash
cd [your path]/android/app
```

execute below command to issue Android Signing Key.

```bash
# keytool -genkey -v -keystore my-release-key.keystore -alias my-key-alias -keyalg RSA -keysize 2048 -validity 10000

keytool -genkey -v -keystore [key-name].keystore -alias [key alias] -keyalg RSA -keysize 2048 -validity 10000

Enter keystore password:
Re-enter new password:
What is your first and last name?
  [Unknown]:
What is the name of your organizational unit?
  [Unknown]:
What is the name of your organization?
  [Unknown]:
What is the name of your City or Locality?
  [Unknown]:
What is the name of your State or Province?
  [Unknown]:
What is the two-letter country code for this unit?
  [Unknown]:
Is CN=*****, OU=Unknown, O=Unknown, L=*****, ST=*****, C=***** correct?
  [no]:

Enter key password for <my-key-alias>
    (RETURN if same as keystore password):
```

after inserting all, you can see ```my-release-key.keystore``` file in ```android/app```

## configure Signing Key
after creating Signing Key, we need to configure it to ```gradle```. open ```android/gradle.properties``` file and add blow code.

```xml
MYAPP_RELEASE_STORE_FILE=my-release-key.keystore
MYAPP_RELEASE_KEY_ALIAS=my-key-alias
MYAPP_RELEASE_STORE_PASSWORD=*****
MYAPP_RELEASE_KEY_PASSWORD=*****
```

add below code to ```android/app/build.gradle``` file.

```xml
...
android {
    ...
    defaultConfig { ... }
    signingConfigs {
        release {
            if (project.hasProperty('MYAPP_RELEASE_STORE_FILE')) {
                storeFile file(MYAPP_RELEASE_STORE_FILE)
                storePassword MYAPP_RELEASE_STORE_PASSWORD
                keyAlias MYAPP_RELEASE_KEY_ALIAS
                keyPassword MYAPP_RELEASE_KEY_PASSWORD
            }
        }
    }
    buildTypes {
        release {
            ...
            signingConfig signingConfigs.release
        }
    }
}
...
```

## build
go to ```android``` folder in RN(react native) project folder and execute below code to build.

```bash
./gradlew assembleRelease
```

you can see built file on below path.

```bash
android/app/build/outputs/apk/release/app-release.apk
```

but we got below error at this section.

```bash
...
Execution failed for task ':app:lintVitalRelease'.
> Lint found fatal errors while assembling a release target.
...
```

it's not good solution, but we add below code to ```android/app/build.gradle```.

```xml
...
android {
  ...
  lintOptions {
      checkReleaseBuilds false
      // Or, if you prefer, you can continue to check for errors in release builds,
      // but continue the build even when errors are found:
      abortOnError false
  }
  ...
}
...
```


## test built file
delete previous app on Android Device and execute below code to test built file.

```bash
react-native run-android --variant=release
```

## error
we've done to follow official site but when we executed below code to build,

```bash
./gradlew assembleRelease
```

and execute below code to test on device directly,

```bash
react-native run-android --variant=release
```

we got below error.

```bash
java.lang.RuntimeException: Unable to load script from assets 'index.android.bundle'. Make sure your bundle is packaged correctly or you're running a packager server.
```

as a workaround, we executed below code first to create ```index.android.bundle```.

```bash
...
react-native bundle --platform android --dev false --entry-file index.js --bundle-output android/app/src/main/assets/index.android.bundle
...
```

and build or

```bash
./gradlew assembleRelease
```

test on device directly.

```bash
react-native run-android --variant=release
```