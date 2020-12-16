```js
...
import { ActionSheet } from 'native-base';
...

render() {
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
}
```