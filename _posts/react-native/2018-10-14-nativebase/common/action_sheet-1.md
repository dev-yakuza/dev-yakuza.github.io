```js
import * as React from 'react';
import { Root } from 'native-base';
import { ThemeProvider } from 'styled-components';

import Theme from './Theme';

import Navigator from './Screen/Navigator';

interface Props {}
interface State {}

export default class App extends React.Component<Props, State> {
  render() {
    return (
      <Root>
        <ThemeProvider theme={Theme}>
          <Navigator />
        </ThemeProvider>
      </Root>
    );
  }
}

```