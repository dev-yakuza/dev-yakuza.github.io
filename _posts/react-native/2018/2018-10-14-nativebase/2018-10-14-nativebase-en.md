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

<div id="contents_list" markdown="1">

## Contents

1. [outline](#outline)
1. [library installation](#library-installation)
    - [over 0.60](#over-060)
    - [under 0.59](#under-059)
1. [how to use](#how-to-use)
1. [ActionSheet](#actionsheet)
    - [Functional Components - Root](#functional-components---root)
    - [Class Components - Root](#class-components---root)
    - [Functional Components - ActionSheet](#functional-components---actionsheet)
    - [Class Components - ActionSheet](#class-components---actionsheet)
1. [reference](#reference)

</div>

## outline

let's apply [NativeBase](https://nativebase.io/){:rel="nofollow noreferrer" target="_blank" } which is material ui components to RN project.

## library installation

install NativeBase library with below code

{% include_relative common/installation.md %}

after installing, link the library to the project with below code.

### over 0.60

```bash
cd ios
pod install
cd ..
```

### under 0.59

{% include_relative common/link.md %}

## how to use

we only write a blog post if we have used libraries. so we will add contents to here when we use.

if you want to knwo how to use, see official site.

- official site: [NativeBase](https://nativebase.io/){:rel="nofollow noreferrer" target="_blank" }

{% include in-feed-ads.html %}

## ActionSheet

if you want to use ActionSheet feature, you should wrap root component of the project by NativeBase's ```<Root>``` component.

### Functional Components - Root

```js
import React from 'react';
import { Root } from 'native-base';
import { ThemeProvider } from 'styled-components';

import Theme from './Theme';

import Navigator from './Screen/Navigator';

interface Props {}
interface State {}

const App = ({}: Props) => {
  return (
    <Root>
    <ThemeProvider theme={Theme}>
        <Navigator />
    </ThemeProvider>
    </Root>
  );
};

export default App;
```

### Class Components - Root

{% include_relative common/action_sheet-1.md %}

write below code to display ActionSheet.

### Functional Components - ActionSheet

```js
...
import { ActionSheet } from 'native-base';
...
    const ActionButtons = ['English', '日本語', '한국어', 'Cancel'];

    const cancelButtonIndex = ActionButtons.length - 1;

    return (
      <Container>
          <Button
            onPress={() =>
              ActionSheet.show(
                {
                  options: ActionButtons,
                  cancelButtonIndex: cancelButtonIndex,
                  destructiveButtonIndex: cancelButtonIndex,
                },
                (buttonIndex: number) => {
                  alert(buttonIndex);
                }
              )
            }>
            Test
          </Button>
      </Container>
    );
};
```

### Class Components - ActionSheet

{% include_relative common/action_sheet-2.md %}

- options: this is the button list which can be string type list(string[]) or list includes icons(Array<{ text: string, icon?: string, iconColor?: string }>)
- cancelButtonIndex: cancel button index.
- destructiveButtonIndex: delete button index(index of red color text button)
- title: ActionSheet's title
- (buttonIndex: number) => { alert(buttonIndex); }: if button is selected, selected button index is passed.

## reference

- official site: [NativeBase](https://nativebase.io/){:rel="nofollow noreferrer" target="_blank" }
