```js
...
import Tts from 'react-native-tts';
...

export default class Home extends React.Component<Props, State> {
    constructor(props: Props) {
        super(props);
        Tts.setDefaultLanguage('en-IE');
    }
    ...
    private _onPressSpeech = () => {
        Tts.speak('Hello, world!');
    }
}
```