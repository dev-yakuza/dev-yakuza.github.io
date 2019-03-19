```js
...
import DeviceInfo from 'react-native-device-info';
...

export default class Home extends React.Component<Props, State> {
    render() {
        const deviceLocale = DeviceInfo.getDeviceLocale();
        // iOS: "en"
        // Android: "en-US"
        ...
    }
}
```