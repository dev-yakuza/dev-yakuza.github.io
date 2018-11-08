---
layout: 'post'
permalink: '/react-native/nativebase/'
paginate_path: '/react-native/:num/nativebase/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'NativeBase'
description: 'use NativeBase library for basic component UI.'
image: '/assets/images/category/react-native/nativebase.jpg'
---


## outline
let's apply [NativeBase](https://nativebase.io/){:rel="nofollow noreferrer" :target="_blank" } which is material ui components to RN project.

## library installation
install NativeBase library with below code

{% include_relative common/installation.md %}

after installing, link the library to the project with below code.

{% include_relative common/link.md %}

## how to use
we only write a blog post if we have used libraries. so we will add contents to here when we use.

if you want to knwo how to use, see official site.
- official site: [NativeBase](https://nativebase.io/){:rel="nofollow noreferrer" :target="_blank" }

## ActionSheet
if you want to use ActionSheet feature, you should wrap root component of the project by NativeBase's ```<Root>``` component.

{% include_relative common/action_sheet-1.md %}

write below code to display ActionSheet.

{% include_relative common/action_sheet-2.md %}

- options: this is the button list which can be string type list(string[]) or list includes icons(Array<{ text: string, icon?: string, iconColor?: string }>)
- cancelButtonIndex: cancel button index.
- destructiveButtonIndex: delete button index(index of red color text button)
- title: ActionSheet's title
- (buttonIndex: number) => { alert(buttonIndex); }: if button is selected, selected button index is passed.

## reference
- official site: [NativeBase](https://nativebase.io/){:rel="nofollow noreferrer" :target="_blank" }