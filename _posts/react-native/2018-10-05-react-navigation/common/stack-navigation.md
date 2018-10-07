```js
// src/App.tsx
import * as React from 'react';
import { ThemeProvider } from 'styled-components';

import Theme from './Theme';

import Navigator from './Screen/Navigator';

interface Props {}
interface State {}

export default class App extends React.Component<Props, State> {
  render() {
    return (
      <ThemeProvider theme={Theme}>
        <Navigator />
      </ThemeProvider>
    );
  }
}
```

```js
// src/Screen/Navigator.tsx
import { createStackNavigator } from 'react-navigation';

import Home from './Home';
import Second from './Second';

export default createStackNavigator(
  {
    Home: Home,
    Second: Second,
  },
  {
    initialRouteName: 'Home',
  }
);
```

```js
// src/Screen/Home/index.tsx
import * as React from 'react';
import { NavigationScreenProp, NavigationState } from 'react-navigation';
import { Text, SafeAreaView, Button } from 'react-native';
import styled from 'styled-components';

interface IAppStyledProps {
  theme?: ITheme;
}
const Container = styled(SafeAreaView)`
  flex: 1;
  justify-content: center;
  align-items: center;
  background-color: ${(props: IAppStyledProps) =>
    props.theme && props.theme.color.white};
`;
const StyledText = styled(Text)`
  font-size: 14px;
  color: ${(props: IAppStyledProps) => props.theme && props.theme.color.black};
`;
interface Props {
  navigation: NavigationScreenProp<NavigationState>;
}
interface State {}

export default class Home extends React.Component<Props, State> {
  render() {
    return (
      <Container>
        <StyledText>Home screen!</StyledText>
        <Button
          title="Go to Second"
          onPress={() => this.props.navigation.navigate('Second')}
        />
      </Container>
    );
  }
}

```

```js
// src/Screen/Second/index.tsx
import * as React from 'react';
import { NavigationScreenProp, NavigationState } from 'react-navigation';
import { Text, SafeAreaView, Button } from 'react-native';
import styled from 'styled-components';

interface IAppStyledProps {
  theme?: ITheme;
}
const Container = styled(SafeAreaView)`
  flex: 1;
  justify-content: center;
  align-items: center;
  background-color: ${(props: IAppStyledProps) =>
    props.theme && props.theme.color.white};
`;
const StyledText = styled(Text)`
  font-size: 14px;
  color: ${(props: IAppStyledProps) => props.theme && props.theme.color.black};
`;
interface Props {
  navigation: NavigationScreenProp<NavigationState>;
}
interface State {}

export default class Second extends React.Component<Props, State> {
  render() {
    return (
      <Container>
        <StyledText>Second screen!</StyledText>
        <Button
          title="Go back"
          onPress={() => this.props.navigation.goBack()}
        />
      </Container>
    );
  }
}

```