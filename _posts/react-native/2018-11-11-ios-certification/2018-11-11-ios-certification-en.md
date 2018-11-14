---
layout: 'post'
permalink: '/react-native/ios-certification/'
paginate_path: '/react-native/:num/ios-certification/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'iOS Certification'
description: if you enrolled Apple Developer Program, let's see how to configure iOS developer Certification.
image: '/assets/images/category/react-native/ios-certification.jpg'
---


## outline
this blog post is for developers who already enrolled Apple Developer Program.
if you don't enroll Apple Developer Program, see previous blog post [enroll iOS developer]({{site.url}}/{{page.categories}}/ios-enroll-developer-program/) and enroll Apple Developer Program.

let's see how to create iOS developer certification and configure it.

## donwload certification
if you get purchase approved email from Apple after buying Apple Developer Program, go to ```Account``` page on Apple Developer site([https://developer.apple.com/](https://developer.apple.com/){:rel="nofollow noreferrer" :target="_blank"})

![apple developer site after enrolling](/assets/images/category/react-native/ios-certification/apple-developer-site-after-enrolling.png)

you can see different screen before you enroll Apple Developer Program. click ```Certificates, IDs & Profiles``` to go to the certification page.

![download certification](/assets/images/category/react-native/ios-certification/download-certification.png)

you have already one certification. select the certification and click ```Download``` button and save it on your PC. if you don't have the certification, create it by following create certification section.

this certification is for development. if you already have this one, you need to create production certification. so create it by following create certification section.

## create certification
execute ```Keychain Access``` program on your Mac.

![Keychain Access](/assets/images/category/react-native/ios-certification/en-keychain.png)

after Keychain is executed, click ```Keychain accesss``` > ```Certification Assistant``` > ```Request a Certificate From a Certificate Authority...``` on the left top of the PC screen.

![Request a Certificate From a Certificate Authority...](/assets/images/category/react-native/ios-certification/en-request-certification.png)

if you click ```Request a Certificate From a Certificate Authority...``` menu, you can see ```Certificate Assistant``` like below screen.

![insert certification info to Keychain access](/assets/images/category/react-native/ios-certification/en-certification-info.png)

inser ```User Email Address``` and ```Common Name```. select ```Saved to disk``` and ```Let me specify key pair information```. click ```Continue``` button and save the file to your PC.

![Keychain Access select key](/assets/images/category/react-native/ios-certification/en-certification-key.png)

click ```Continue``` if you are same value in ```Key Size``` and ```Algorithm```.

![completed to creact keychain](/assets/images/category/react-native/ios-certification/en-certification-completed.png)

completed to create KeyChain Certification file.

![download certification](/assets/images/category/react-native/ios-certification/download-certification.png)

go to ```Account``` page in Apple Developer site([https://developer.apple.com/](https://developer.apple.com/){:rel="nofollow noreferrer" :target="_blank"}) and select ```Certificates, IDs & Profiles``` menu. click ```+``` button on the right top of the screen.

![certification selection](/assets/images/category/react-native/ios-certification/select-certification.png)

click ```iOS App Development```. scroll down and click ```Continue``` button in ```Select Type``` page.

if you want to create a production certification, click ```App Store and ad Hoc``` in ```Production``` section.

next screen is detail about how to create certification file(CSR file). we already created this file by ```Keychain Access``` so just scroll down and click ```Continue```.

![create csr file](/assets/images/category/react-native/ios-certification/create-csr-file.png)

click ```Choose File``` to select certification file(CSR file) created by ```Keychain Access``` and click ```Continue`` to go to the next page.

![choose csr file](/assets/images/category/react-native/ios-certification/choose-csr-file.png)

completed to create certification. click ```Download``` to save certification to your PC.

![complete create certification file](/assets/images/category/react-native/ios-certification/complete-create-certification.png)

## register certification
we need to insert certification created above to ```Keychain Access```. execute ```Keychain Access``` program.

![keychain acceess](/assets/images/category/react-native/ios-certification/en-keychain.png)

after ```Keychain Access``` is executed, click ```My certificates``` on the left bottom of the screen and drag your certification which you made via Apple Developer site before to here for adding.

![Keychain Access my certificates](/assets/images/category/react-native/ios-certification/en-keychain-certification.png)

## configure Apple Developer account
we need to connect Apple Developer Account to the iOS project. execute ```iOS/projectname.xcodeproj``` in RN(react native) project folder.

after xcode is executed, click ```projectname``` on the left top and select ```General``` tab.

![xcode certification](/assets/images/category/react-native/ios-certification/xcode-certification.png)

click ```Team``` dropdown menu in ```Signing``` on above screen.

![xcode certification add new](/assets/images/category/react-native/ios-certification/xcode-certification-add-new.png)

if you have already connected Apple Developer Account, just select that account. if you don't have connected, select ```Add an Account```.

![xcode certification login](/assets/images/category/react-native/ios-certification/xcode-certification-login.png)

login Apple Developer account. if you don't have Apple Developer account, see [iOS device test]({{site.url}}/{{page.categories}}/ios-test-on-device/){:target="_blank"} blog post and create Apple Developer account.

![xcode certification add new](/assets/images/category/react-native/ios-certification/xcode-certification-add-new.png)

click dropdown menu beside ```Team``` and select Apple Developer account we created above.

connet also Apple Developer account to Test section.

![xcode certification add test](/assets/images/category/react-native/ios-certification/xcode-certification-add-test.png)

completed to connect Apple Developer account. let's see about how to make Provisioning Profiles for production build.

## create Provisioning Profiles
scroll down ```Account``` page in Apple Developer site and click ```Provisioning Profiles``` menu.

we need development Provisioing Profile and production Provisioning Profile. so do below procedure double times for development and production.

![provisioning profiles](/assets/images/category/react-native/ios-certification/provisioning-profiles.png)

select ```All``` menu in Provisioning Profiles section.

![provisioning profiles detail](/assets/images/category/react-native/ios-certification/provisioning-profiles-detail.png)

you can see above screen. click ```+``` button for adding new Provisioning Profile

![provisioning profiles ios](/assets/images/category/react-native/ios-certification/provisioning-profiles-ios.png)

select ```iOS App Development``` and click ```Continue```.

if you want to create Production Provisioning Profiles, select ```App Store``` in ```Distribution``` section.

![provisioning profiles app id](/assets/images/category/react-native/ios-certification/provisioning-profiles-app-id.png)

select ```Bundle Identifier``` when we use in development. you can find ```Bundle Identifier``` in ```Identity``` section on xcode ```General``` tab.

![xcode bundle identifier](/assets/images/category/react-native/ios-certification/xcode-certification.png)

click ```Continue``` button and select Apple Develop account and test device.

![provisioning profiles name](/assets/images/category/react-native/ios-certification/provisioning-profiles-name.png)

insert Provisioning Profile name and click ```Continue```.

completed to create Provisioning Profile. click ```Download``` and save it on your PC.

## connect Provisioning Profiles
xcode has default setting which manage automatically ```Signing```(```Automatically manage signing``` in ```Signing``` section)

![xcode bundle identifier](/assets/images/category/react-native/ios-certification/xcode-certification.png)

if you don't have any problem in this status, you develop and build in this status.(you don't have any red error text in ```Signing``` section) we have Provisioning Profile connection error so we unchecked this option and connect Provisioning Profile manually.

below is about how to connect Provisioning Profile manually.

![xcode bundle identifier](/assets/images/category/react-native/ios-certification/xcode-certification.png)

uncheck ```Automatically manage signing``` in ```Signing``` section.

![disable automatically manage signing](/assets/images/category/react-native/ios-certification/disable_auto.png)

you can see ```Signing(Debug)``` and ```Signing(Release)``` after unchecking. click ```Provision Profile``` and select ```Import Profile``` and choose Provisioning Profile created above in both. in Test, do same procedure.

![disable automatically manage signing test](/assets/images/category/react-native/ios-certification/disable_auto_test.png)

## completed
completed all settings. we are ready to develop and release. next, we will introduce how to use ```TestFlight``` and release.