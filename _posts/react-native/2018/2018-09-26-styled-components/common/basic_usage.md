```js
// src/App.tsx
...
import styled from 'styled-components/native';
...
const Container = styled.View`
  flex: 1;
  justify-content: center;
  align-items: center;
  background-color: #f5fcff;
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
      <Container>
        <MainText>Hello world</MainText>
      </Container>
    );
  }
}
```