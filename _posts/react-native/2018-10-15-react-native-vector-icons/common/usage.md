```js
...
import Icon from 'react-native-vector-icons/FontAwesome';
...

export default class Home extends React.Component<Props, State> {
    render() {
        return (
            <View>
                <Icon name="home" size={24} color="#ffffff" />
            </View>
        );
    }
}
```