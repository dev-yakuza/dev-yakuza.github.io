---
layout: 'post'
permalink: '/react-native/react-native-linear-gradient/'
paginate_path: '/react-native/:num/react-native-linear-gradient/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'Gradient'
description: let's see how to use react-native-linear-gradient to make the gradient background on RN(React Native) project.
image: '/assets/images/category/react-native/react-native-linear-gradient.png'
---


## Outline
it's difficult to make the gradient background on RN(Reat Native). in this blog, we'll introduce how to make the gradient background by ```react-native-linear-gradient``` library.

- react-native-linear-gradient official site: [https://github.com/react-native-community/react-native-linear-gradient](https://github.com/react-native-community/react-native-linear-gradient){:rel="nofollow noreferrer" target="_blank"}

## Installation
execute belwo command to install ```react-native-linear-gradient``` library to use the gradient on RN(React Native).

```bash
npm install --save react-native-linear-gradient
```

## Link Library
execute below command to link ```react-native-linear-gradient``` to RN(React Native) project.

```bash
react-native link react-native-linear-gradient
```

## How To Use
below source code is about how to make the gradient by ```react-native-linear-gradient``` on RN(React Native). (source code is from react-native-linear-gradient official site)

```js
import LinearGradient from 'react-native-linear-gradient';

// Within your render function
<LinearGradient colors={['#4c669f', '#3b5998', '#192f6a']} style={styles.linearGradient}>
  <Text style={styles.buttonText}>
    Sign in with Facebook
  </Text>
</LinearGradient>

// Later on in your styles..
var styles = StyleSheet.create({
  linearGradient: {
    flex: 1,
    paddingLeft: 15,
    paddingRight: 15,
    borderRadius: 5
  },
  buttonText: {
    fontSize: 18,
    fontFamily: 'Gill Sans',
    textAlign: 'center',
    margin: 10,
    color: '#ffffff',
    backgroundColor: 'transparent',
  },
});
```

we use below source code to make the gradient background.

```js
...
import LinearGradient from 'react-native-linear-gradient';
import styled from 'styled-components/native';
...
const Background = styled(LinearGradient)`
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
`;
...
<Background
  colors={[item.background[0], item.background[1]]}
  start={{
    x: item.direction.start.x,
    y: item.direction.start.y,
  }}
  end={{ x: item.direction.end.x, y: item.direction.end.y }}
/>
...
```

also, when the page that has the gradient background is switched, we applied the animation to switch smoothly the gradient background. we referred below site to make the animation.

- gradient animation example: [AnimatedGradient](https://github.com/dslounge/rn-animated-gradient-example/tree/master/src/ColorExample/AnimatedGradient){:rel="nofollow noreferrer" target="_blank"}


## Completed
let's make RN(React Native) project more beautiful by the gradient background.


## Reference
- react-native-linear-gradient official site: [https://github.com/react-native-community/react-native-linear-gradient](https://github.com/react-native-community/react-native-linear-gradient){:rel="nofollow noreferrer" target="_blank"}
- gradient animation example: [AnimatedGradient](https://github.com/dslounge/rn-animated-gradient-example/tree/master/src/ColorExample/AnimatedGradient){:rel="nofollow noreferrer" target="_blank"}