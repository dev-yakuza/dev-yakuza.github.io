---
layout: 'post'
permalink: '/react-native/react-native-swipe-gestures/'
paginate_path: '/react-native/:num/react-native-swipe-gestures/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'Swipe Detection'
description: let's see how to use react-native-gestures to detect user swipe event on RN(React Native) project
image: '/assets/images/category/react-native/react-native-swipe-gestures.jpg'
---


## Outline
when I was developing RN(React Native) project, I needed to detect user swipe direction to do different actions in the app. so I searched and found ```react-native-swipe-gestures```. in this blog, we'll see how to install and use ```react-native-swipe-gestures```.

- react-native-swipe-gestures official site: [https://github.com/glepur/react-native-swipe-gestures](https://github.com/glepur/react-native-swipe-gestures){:rel="nofollow noreferrer" target="_blank"}

## Installation
execute below command to install ```react-native-gestures``` library.

```bash
npm install --save react-native-swipe-gestures
```

## How To Use
add below soure where you want to detect user swipe events.

{% raw %}
```js
...
import GestureRecognizer from 'react-native-swipe-gestures';
...

render() {
  <GestureRecognizer
          onSwipeLeft={this._onSwipeLeft}
          onSwipeRight={this._onSwipeRight}
          config={{
            velocityThreshold: 0.3,
            directionalOffsetThreshold: 80,
          }}
          style={{
            flex: 1,
          }}>
          ...
  </GestureRecognizer>
}
...
private _onSwipeLeft = gestureState => {
  ...
  this.setState({
    ...
  });
};

private _onSwipeRight = gestureState => {
  ...
  this.setState({
    ...
  });
  ...
};
```
{% endraw %}

## Completed
we saw how to install and use ```react-native-swipe-gestures``` to detect user swipe events on RN(React Native). I've found myself doing copy-paste not to make simple code...```react-native-swipe-gestures``` source code is not long, so I think to make it yourself is also funny.


## Reference
- react-native-swipe-gestures official site: [https://github.com/glepur/react-native-swipe-gestures](https://github.com/glepur/react-native-swipe-gestures){:rel="nofollow noreferrer" target="_blank"}