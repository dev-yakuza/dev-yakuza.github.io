```js
// src/@types/index.d.ts
interface ITheme {
  color: {
    white: string;
    black: string;
  };
  fonts: {
    normal: string;
  };
}
```

```js
// src/Theme.tsx
export default {
  color: {
    white: '#FFFFFF',
    black: '#000000',
  },
  fonts: {
    normal: '14px',
  },
};
```

```js
...
// src/App.tsx
import { ThemeProvider } from 'styled-components';
import styled from 'styled-components/native';
import Theme from './Theme';
...

interface IContainerPorps {
  theme?: ITheme;
}

const Container = styled.View`
  flex: 1;
  justify-content: center;
  align-items: center;
  background-color: ${(props:IContainerProps) => props.theme && props.theme.color.black};
`;
const MainText = styled.Text`
  font-size: 20;
  text-align: center;
  margin: 10px;
  color: red;
`;
...
interface Props {}
interface State {}
export default class App extends React.Component<Props, State> {
  render() {
    return (
      <ThemeProvider theme={Theme}>
        <Container>
          <MainText>Hello world</MainText>
        </Container>
      </ThemeProvider>
    );
  }
}
```