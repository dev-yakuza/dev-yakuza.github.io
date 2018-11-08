```js
...
export default class Home extends React.Component<Props, State> {
  static navigationOptions = { header: null };

  render() {
    return (
      <Container>
        <StyledText>Home screen!</StyledText>
      </Container>
    );
  }
}
...
```