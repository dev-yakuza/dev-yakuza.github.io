---
layout: 'post'
permalink: '/blaboo/update-review/'
paginate_path: '/blaboo/:num/update-review/'
lang: 'en'
categories: 'blaboo'
comments: true

title: 'BlaBoo Update Reviews'
description: I've developed and released the app called BlaBoo by using RN(React Native). in this blog, I will talk about what I updated after the release.
image: '/assets/images/category/blaboo/update-review/app_concept.png'
---


## Outline
I've created and released the app called BlaBoo by using RN(React Native). in here, I will introduce how I manage and what I updated the app after releasing. before starting it, see what BlaBoo is simply.


## What is BlaBoo?
BlaBoo is a word study app for baby/children that combines the word ```blah blah``` with the word ```boo```.

- BlaBoo introduction page: [BlaBoo](https://dev-yakuza.github.io/app/blaboo/en/){:target="_blank"}

below is BlaBoo's download links.

<div class="download_link_container">
    <a class="download_link_ios" href="https://itunes.apple.com/app/blaboo/id1441741187" target="_blank">
        <img src="/assets/images/apple_download.png" alt="learning words app for children, blaboo iOS download"/>
    </a>
    <a class="download_link_android" href="https://play.google.com/store/apps/details?id=io.github.dev.yakuza.blaboo" target="_blank">
        <img src="/assets/images/google play_download.png" alt="learning words app for children, blaboo Android download"/>
    </a>
</div>

baby/children see the illustrations and if they touch them, the app reads the word with sound.

![BlaBoo for baby/children word study app - development journal](/assets/images/category/blaboo/development-journal/app_concept.png)

if you want to know more details about developing of BlaBoo, see my previous blog post.

- [BlaBoo App Development Journal(RN, React Native)]({{site.url}}/react-native/development-journal/){:target="_blank"}


## Manage The App
when I planned BlaBoo app, I thought this app is very simple so I won't need to manage this app. just, I thought people who need this app will download and delete it.

however, when I released the app and saw people downloaded it, I couldn't stop to manage and develop the app.

![babies/children word learning app BlaBoo development journal](/assets/images/category/blaboo/update-review/blaboo_analytics.png)


## Update
I've made BlaBoo supports English, Japanese and Korean at the first release. I could check the words by my eyes, so I thought core feature that is the voice pronunciation has no problem.

but after the release, first download occured at China, so I updated  to support Chinese by using Google Translator as soon as possible.

- [Chinese promotion site](https://dev-yakuza.github.io/app/blaboo/zh/){:target="_blank"}

![BlaBoo Update Strategy - Chinese](/assets/images/category/blaboo/update-review/blaboo_zh.png)

I couldn't know that the words and the site translation are not wrong. fortunately, one of my friends is Taiwanese and he tested the app and said it's OK. however, he didn't test everything so I still have worries about it.

but I thought it's better to support own language than to have a little bit wrong words. after this, I was checking the countries downloaded the app, and translating the app to that country's languages.

there was a problem with adding Vietnamese during this update. after translating the words, I've recognized the app couldn't pronounce Vietnamese during the test. I found the cause of the problem. the cause of the problem is  that the library doesn't support Vietnamese.

BlaBoo uses the library below for TTS(Text To Speech) feature.

- [react-native-tts]({{site.url}}/react-native/react-native-tts/){:target="_blank"}

this library has the language-coutnry lists to support it.

```js
{language: "ar-SA", id: "com.apple.ttsbundle.Maged-compact", quality: 300, name: "Maged"}
{language: "cs-CZ", id: "com.apple.ttsbundle.Zuzana-compact", quality: 300, name: "Zuzana"}
{language: "da-DK", id: "com.apple.ttsbundle.Sara-compact", quality: 300, name: "Sara"}
{language: "de-DE", id: "com.apple.ttsbundle.Anna-compact", quality: 300, name: "Anna"}
{language: "el-GR", id: "com.apple.ttsbundle.Melina-compact", quality: 300, name: "Melina"}
{language: "en-AU", id: "com.apple.ttsbundle.Karen-compact", quality: 300, name: "Karen"}
{language: "en-GB", id: "com.apple.ttsbundle.Daniel-compact", quality: 300, name: "Daniel"}
{language: "en-IE", id: "com.apple.ttsbundle.Moira-compact", quality: 300, name: "Moira"}
{language: "en-US", id: "com.apple.ttsbundle.Samantha-compact", quality: 300, name: "Samantha"}
{language: "en-ZA", id: "com.apple.ttsbundle.Tessa-compact", quality: 300, name: "Tessa"}
{language: "es-ES", id: "com.apple.ttsbundle.Monica-compact", quality: 300, name: "Monica"}
{language: "es-MX", id: "com.apple.ttsbundle.Paulina-compact", quality: 300, name: "Paulina"}
{language: "fi-FI", id: "com.apple.ttsbundle.Satu-compact", quality: 300, name: "Satu"}
{language: "fr-CA", id: "com.apple.ttsbundle.Amelie-compact", quality: 300, name: "Amelie"}
{language: "fr-FR", id: "com.apple.ttsbundle.Thomas-compact", quality: 300, name: "Thomas"}
{language: "he-IL", id: "com.apple.ttsbundle.Carmit-compact", quality: 300, name: "Carmit"}
{language: "hi-IN", id: "com.apple.ttsbundle.Lekha-compact", quality: 300, name: "Lekha"}
{language: "hu-HU", id: "com.apple.ttsbundle.Mariska-compact", quality: 300, name: "Mariska"}
{language: "id-ID", id: "com.apple.ttsbundle.Damayanti-compact", quality: 300, name: "Damayanti"}
{language: "it-IT", id: "com.apple.ttsbundle.Alice-compact", quality: 300, name: "Alice"}
{language: "ja-JP", id: "com.apple.ttsbundle.Kyoko-compact", quality: 300, name: "Kyoko"}
{language: "ko-KR", id: "com.apple.ttsbundle.Yuna-compact", quality: 300, name: "Yuna"}
{language: "nl-BE", id: "com.apple.ttsbundle.Ellen-compact", quality: 300, name: "Ellen"}
{language: "nl-NL", id: "com.apple.ttsbundle.Xander-compact", quality: 300, name: "Xander"}
{language: "no-NO", id: "com.apple.ttsbundle.Nora-compact", quality: 300, name: "Nora"}
{language: "pl-PL", id: "com.apple.ttsbundle.Zosia-compact", quality: 300, name: "Zosia"}
{language: "pt-BR", id: "com.apple.ttsbundle.Luciana-compact", quality: 300, name: "Luciana"}
{language: "pt-PT", id: "com.apple.ttsbundle.Joana-compact", quality: 300, name: "Joana"}
{language: "ro-RO", id: "com.apple.ttsbundle.Ioana-compact", quality: 300, name: "Ioana"}
{language: "ru-RU", id: "com.apple.ttsbundle.Milena-compact", quality: 300, name: "Milena"}
{language: "sk-SK", id: "com.apple.ttsbundle.Laura-compact", quality: 300, name: "Laura"}
{language: "sv-SE", id: "com.apple.ttsbundle.Alva-compact", quality: 300, name: "Alva"}
{language: "th-TH", id: "com.apple.ttsbundle.Kanya-compact", quality: 300, name: "Kanya"}
{language: "tr-TR", id: "com.apple.ttsbundle.Yelda-compact", quality: 300, name: "Yelda"}
{language: "zh-CN", id: "com.apple.ttsbundle.Ting-Ting-compact", quality: 300, name: "Ting-Ting"}
{language: "zh-HK", id: "com.apple.ttsbundle.Sin-Ji-compact", quality: 300, name: "Sin-Ji"}
{language: "zh-TW", id: "com.apple.ttsbundle.Mei-Jia-compact", quality: 300, name: "Mei-Jia"}
```

I checked the language-country code to use the site below.

- [https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html){:rel="nofollow noreferrer" target="_blank"}

I searched Vietnamese-Vietnam at this site, and I could know Vietnamese-Vietnam is ```vi-VN```. however I couldn't find it on the list above. I should execute ```git checkout .``` to reset everything. it was so painful.

after this experience, if I find the downloads occur at new countries, I search the language-country code and check the language-country code exists in ```react-native-tts``` support list.


## Android Bug
after releasing the app, it looked like no problems. I am an iPhone user, so I couldn't test the app on Android enoughly. one day, one of my friends said some illustrations were not able to be touched. if he didn't mention it, my app will be as a trash app forever in Android app market.

I used the bounceIn animation when the illustraions show up in BlaBoo. I used ```react-native-animatable``` library to implement it.

- how to use react-native-animatable: [react-native-animatable]({{site.url}}/react-native/react-native-animatable/){:target="_blank"}

I use an image list and ```map``` to display the illustrations on one view. when page is changed, I just switch the image list to show new images.

```js
{pageData.things.map((lineData: Array<IThing>, lineIndex: number) =>
    lineData.map((item: IThing, index: number) => (
        <Animatable.View
            key={`${pageIndex}-${lineIndex}-${index}`}
            animation="bounceIn"
            delay={(index + 2) * 100}
            useNativeDriver={true}>
                <Thing
                    row={item.row}
                    column={item.column}
                    width={this._calculateWidth(pageData.lines[lineIndex])}
                    height={thingHeight}
                    marginRow={item.marginRow}
                    marginColumn={item.marginColumn}
                    src={item.src}
                    locale={locale}
                    text={item[locale]}
                />
        </Animatable.View>
    ))
)}
```

however, on Android, the image list was changed, but previous ```Animatable.View``` was still on the screen above the new images. ```react-native-animatable``` provides ```useNativeDriver``` option for the animation performance. as you can see above, of course I used it for the performance.

I didn't know the exact reason, but if I removed this option, the app worked fine. however, I counldn't find the fundamental reason and I didn't have enough time to analize it. however, I couldn't find the fundamental reason and didn't have enough time to analyze it, but the app was already released and it was big issue. so I decided to remove ```Animatable.View``` and updated the app. it was a bit disappointing that the animation feature was removed. but the risk of using the feature was too high without knowing the exact cause. so I decided to remove it completely. if someone has same experience and know why, please share your solution!.


## Update Review
now, I use the procedure below to update the app.

1. check the countries that download is occured.
1. check the translation is already exists for the country.
1. if it was not, check the language-country code.
1. check the library(```react-native-tts```) supports the language-country code.
1. if it supports, translate the app, website and app store information.
1. Test
1. release iOS and Android

it looks very simple, but it is from my several fails. if you'll plan or develop the app to use ```react-native-tts``` for multi-language feature,  I recommend you to check the language is supported by the library.

the list below is what I updated after first release.

1. keep Splash screen for one second(use [react-native-splash-screen]({{site.url}}/react-native/react-native-splash-screen/){:target="_blank"} library)
1. user commented to want more numbers in the app review, so I added more numbers
1. a tester couldn't find ```start``` button on the first screen, so I added the animation to it for finding easily.
1. Added Chinese, Italian, Hindi, Dutch, Thai and German
1. added the feature to induce users to give the app reviews(the library: [react-native-rate]({{site.url}}/react-native/react-native-rate/){:target="_blank"})
1. supported the tablet.
1. fix some bug

the app download links.

<div class="download_link_container">
    <a class="download_link_ios" href="https://itunes.apple.com/app/blaboo/id1441741187" target="_blank">
        <img src="/assets/images/apple_download.png" alt="learning words app for children, blaboo iOS download"/>
    </a>
    <a class="download_link_android" href="https://play.google.com/store/apps/details?id=io.github.dev.yakuza.blaboo" target="_blank">
        <img src="/assets/images/google play_download.png" alt="learning words app for children, blaboo Android download"/>
    </a>
</div>

## The End
In fact, the biggest reason I've written this blog is you help me to borrow your help. as I mentioned above, I used Google Translator to translate other languages except English, Japanese and Korean. I think it's not big deal that the website and the app store text have some wrong characters. however, I think BlaBoo app is the learning words app, so wrong words in the app are not acceptable. but, I don't know every languages, and I don't have money to pay to translate them all. so I was writing this blog to borrow your help.

the repository link below is multi-language files in BlaBoo app. if you know other country languages, please see it and modify it if it is wrong.

- github: [https://github.com/dev-yakuza/blaboo-translate](https://github.com/dev-yakuza/blaboo-translate){:target="_blank"})

your help is one developer's hope, and helps many people can learn correct words.
