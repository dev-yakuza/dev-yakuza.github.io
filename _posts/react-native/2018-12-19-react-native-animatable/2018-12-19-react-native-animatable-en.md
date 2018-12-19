---
layout: 'post'
permalink: '/react-native/react-native-animatable/'
paginate_path: '/react-native/:num/react-native-animatable/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'react-native-animatable'
description: let's see how to use react-native-animatable to add simply animations to RN(react native).
image: '/assets/images/category/react-native/react-native-animatable.jpg'
---


## outline
to add simply animations to RN(react native), we'll introduce how to use [react-native-animatable](https://github.com/oblador/react-native-animatable){:rel="nofollow noreferrer" target="_blank"} which has gathered basic useful animations.

in this blog, we'll explain with RN(react native) applied ```typescript``` and ```styled-components```. if you don't know how to apply ```typescript``` and ```styled-components``` to RN(react native), see our previous blogs.

- [typescript]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}
- [styled-components]({{site.url}}/{{page.categories}}/styled-components/){:target="_blank"}

## install the library
execute below command to install react-native-animatable library.

```bash
npm install react-native-animatable --save
```

## basic usage
add source like below to where you want to add an animation.

```js
...
import * as Animatable from 'react-native-animatable';
...

render() {
  ...
  return (
    <Animatable.Text animation="zoomInUp">Zoom me up, Scotty</Animatable.Text>
  );
}
```

## usage with event
we can make animations start when user event is occurred by using RN(react native) ```ref```.

```js
...
import * as Animatable from 'react-native-animatable';
...

export default class Page extends React.Component<Props, State> {
  private AnimationRef;
  ...
  render() {
    ...
    return (
      <TouchableWithoutFeedback onPress={this._onPress}>
        <Animatable.View ref={ref => (this.AnimationRef = ref)}>
          <Text>Bounce me!</Text>
        </Animatable.View>
      </TouchableWithoutFeedback>
    );
  }
  ...
  private _onPress = () => {
    this.AnimationRef.bounce();
  }
  ...
}
```

## styled-components
below is the way to apply an animation to the styled-components.

```js
...
import styled from 'styled-components/native';
import * as Animatable from 'react-native-animatable';
...
const StyledImage = Animatable.createAnimatableComponent(styled.Image``);
...
render() {
  ...
  return (
    <StyledImage
      animation="bounceIn"
      delay={1000}
      useNativeDriver={true}
      source={src}
    />
  );
}
...
```

## animation list
you can see animations with examples at ```react-native-animatable``` official repository.

- [https://github.com/oblador/react-native-animatable](https://github.com/oblador/react-native-animatable){:rel="nofollow noreferrer" target="_blank"}

below is animation list.

- bounce
- flash
- jello
- pulse
- rotate
- rubberBand
- shake
- swing
- tada
- wobble
- bounceIn
- bounceInDown
- bounceInUp
- bounceInLeft
- bounceInRight
- bounceOut
- bounceOutDown
- bounceOutUp
- bounceOutLeft
- bounceOutRight
- fadeIn
- fadeInDown
- fadeInDownBig
- fadeInUp
- fadeInUpBig
- fadeInLeft
- fadeInLeftBig
- fadeInRight
- fadeInRightBig
- fadeOut
- fadeOutDown
- fadeOutDownBig
- fadeOutUp
- fadeOutUpBig
- fadeOutLeft
- fadeOutLeftBig
- fadeOutRight
- fadeOutRightBig
- flipInX
- flipInY
- flipOutX
- flipOutY
- lightSpeedIn
- lightSpeedOut
- slideInDown
- slideInUp
- slideInLeft
- slideInRight
- slideOutDown
- slideOutUp
- slideOutLeft
- slideOutRight
- zoomIn
- zoomInDown
- zoomInUp
- zoomInLeft
- zoomInRight
- zoomOut
- zoomOutDown
- zoomOutUp
- zoomOutLeft
- zoomOutRight

## completed
if you want to use simple animations fastly, we recommend to use ```react-native-animatable```.

## reference
- [https://github.com/oblador/react-native-animatable](https://github.com/oblador/react-native-animatable){:rel="nofollow noreferrer" target="_blank"}