---
layout: 'post'
permalink: '/react-native/react-navigation-v5/'
paginate_path: '/react-native/:num/react-navigation-v5/'
lang: 'en'
categories: 'react-native'
comments: true

title: 'react-navigation V5'
description: Let's see how to install react-navigaion V5 and how to use it.
image: '/assets/images/category/react-native/2018/react-navigation-v5/background.jpg'
---

<div id="contents_list" markdown="1">

## Content

- [Outline](#outline)
- [Create react-native project](#create-react-native-project)
- [Install react-navigation V5](#install-react-navigation-v5)
- [Install additional Navigations](#install-additional-navigations)
  - [Stack Navigation](#stack-navigation)
  - [Drawer Navigation](#drawer-navigation)
  - [Bottom Tab Navigation](#bottom-tab-navigation)
  - [Material Bottom Tab Navigation](#material-bottom-tab-navigation)
  - [Material Top Tab Navigation](#material-top-tab-navigation)
- [How to use](#how-to-use)
  - [react-native-gesture-handler](#react-native-gesture-handler)
  - [NavigationContainer](#navigationcontainer)
  - [Auth process](#auth-process)
  - [How to use Stack Navigation](#how-to-use-stack-navigation)
  - [How to use Drawer Navigation](#how-to-use-drawer-navigation)
  - [How to use Bottom Tab Navigation](#how-to-use-bottom-tab-navigation)
  - [How to use Material Bottom Tab Navigation](#how-to-use-material-bottom-tab-navigation)
  - [How to useMaterial Top Tab Navigation](#how-to-usematerial-top-tab-navigation)
  - [Drawer Open](#drawer-open)
  - [DrawerActions](#draweractions)
  - [setParams / getParams](#setparams--getparams)
- [Typescript](#typescript)
  - [navigation](#navigation)
  - [route](#route)
- [Completed](#completed)
- [Reference](#reference)

</div>

## Outline

react-navigation had big changes in V5. V4 was similar with V3, but V5 is like another Navigation. SO, I'm writing a blog post about react-navigation V5.

If you want to know previous versions(V3, V4), see the link below.

- [react-navigation]({{site.url}}/{{page.categories}}/react-navigation/){:target="_blank"}

Below is react-navigation V5 official site.

- Official site: [https://reactnavigation.org](https://reactnavigation.org){:rel="nofollow noreferrer" target="_blank" }

Let's see how to use react-navigation V5!

## Create react-native project

The source code in this blog post is applied typescript and styled-components. If you want to know how to install typescript and styled-components, see the links below.

- [typescript]({{site.url}}/{{page.categories}}/typescript/){:target="_blank"}
- [styled-components]({{site.url}}/{{page.categories}}/styled-components/){:target="_blank"}
- [root-import]({{site.url}}/{{page.categories}}/root-import/){:target="_blank"}

{% include in-feed-ads.html %}

## Install react-navigation V5

Execute the command below to install react-navigation v5.

```bash
npm install --save @react-navigation/native
```

Also, execute the command below to install required libraries for react-navigation V5.

```bash
npm install --save react-native-reanimated react-native-gesture-handler react-native-screens react-native-safe-area-context @react-native-community/masked-view
```

After installing, go to iOS folder and execute the command below.

```bash
# cd ios
pod install
```

## Install additional Navigations

From react-navigation V4, we need to install Navigations to use it. V5 is same. We need to install additional navigaiton libraries to use Navigations.

### Stack Navigation

Stack Navigation is like below.

<div class="half_image_container">
  <img class="half_image" src="/assets/images/category/react-native/2018/react-navigation-v5/stack.gif" alt="React Navigation V5 stack Navigation">
</div>
[picture: [reactnavigation.org Official site](https://reactnavigation.org/docs/stack-navigator){:rel="nofollow noreferrer" target="_blank" }]

Execute the command below to install an additional library to use Stack Navigation.

```bash
npm install --save @react-navigation/stack
```

### Drawer Navigation

Drawer Navigation is mainly used for Menu. Normally, Users swipe the screen to show Drawer Navigation.

<div class="half_image_container">
  <img class="half_image" src="/assets/images/category/react-native/2018/react-navigation-v5/drawer.gif" alt="React Navigation V5 drawer Navigation">
</div>
[picture: [reactnavigation.org Official site](https://reactnavigation.org/docs/drawer-navigator){:rel="nofollow noreferrer" target="_blank" }]

Execute the command below to install an additional library to use Drawer Navigation.

```bash
npm install --save @react-navigation/drawer
```

### Bottom Tab Navigation

Bottom Tab Navigation looks like below.

<div class="half_image_container">
  <img class="half_image" src="/assets/images/category/react-native/2018/react-navigation-v5/bottom-tabs-demo.gif" alt="React Navigation V5 bottom-tabs-demo Navigation">
</div>
[Picture: [reactnavigation.org Official site](https://reactnavigation.org/docs/bottom-tab-navigator){:rel="nofollow noreferrer" target="_blank" }]

Execute the command below to install an additional library to use Bottom Tab Navigation.

```bash
npm install --save @react-navigation/bottom-tabs
```

{% include in-feed-ads.html %}

### Material Bottom Tab Navigation

Material Bottom Tab Navigation is Bottom Tab Navigation with Google Material design like below.

<div class="half_image_container">
  <img class="half_image" src="/assets/images/category/react-native/2018/react-navigation-v5/material-bottom-tabs.gif" alt="React Navigation V5 Material Bottom Tab Navigation">
</div>
[picture: [reactnavigation.org Official site](https://reactnavigation.org/docs/material-bottom-tab-navigator){:rel="nofollow noreferrer" target="_blank" }]

Execute the command below to install an additional library to use Material Bottom Tab Navigation.

```bash
npm install --save @react-navigation/material-bottom-tabs react-native-paper
```

And we need to install `react-native-vector-icons` library to use this Navigation. see the link below to install react-native-vector-icons.

- [react-native-vector-icons]({{site.url}}/{{page.categories}}/react-native-vector-icons/){:target="_blank"}

### Material Top Tab Navigation

Material Top Tab Navigation is Top Tab navigation with Google Material design like below.

<div class="half_image_container">
  <img class="half_image" src="/assets/images/category/react-native/2018/react-navigation-v5/material-top-tabs.gif" alt="React Navigation V5 material-top-tabs Navigation">
</div>
[그림: [reactnavigation.org 공식 홈페이지](https://reactnavigation.org/docs/material-top-tab-navigator){:rel="nofollow noreferrer" target="_blank" }]

Execute the command below to isntall an additional library to use Material Top Tab Navigation.

```bash
npm install --save @react-navigation/material-top-tabs react-native-tab-view
```

## How to use

There are details about how to use react-navigation in Official site. You can see the details on the link below.

- Official site: [https://reactnavigation.org/docs](https://reactnavigation.org/docs){:rel="nofollow noreferrer" target="_blank" }

I've made a repository by referrering the official site contents. If you see the repository before making applications, it helps you think about a navigation structure.

- react-navigation-exercise V5: [https://github.com/dev-yakuza/react-navigation-v5-exercise](https://github.com/dev-yakuza/react-navigation-v5-exercise){:rel="nofollow noreferrer" target="_blank" }

In below, I will introduce how to implement the navigation in the repository.

{% include in-feed-ads.html %}

### react-native-gesture-handler

To use react-navigation, we need to import `react-native-gesture-handler`. Open `index.js` or `App.js` file(top parenet component of react-navigation), and modify it like below.

```js
import 'react-native-gesture-handler';
...
```

### NavigationContainer

In V4, we needed to use `createAppContainer` in the last of the module to use Navigations.

```js
{% raw %}
import {createAppContainer} from 'react-navigation';
...
export default createAppContainer(
  ...
);
{% endraw %}
```

In V5, we need to use `NavigationContainer` in the last of the module like V4.

```js
{% raw %}
import React from 'react';
import {NavigationContainer} from '@react-navigation/native';
...
export default () => {
  return (
    <NavigationContainer>
      ...
    </NavigationContainer>
  );
};
{% endraw %}
```

Did you feel already what different is? The previous react-navigation is like a configuration. V5 is like using React Components.

### Auth process

In V4, react-navigation provides `createSwitchNavigator` to process the Auth parts.

```js
{% raw %}
import {createSwitchNavigator, createAppContainer} from 'react-navigation';
...
import AuthLoading from './AuthLoading';
import Auth from './Auth';
...
export default createAppContainer(
  createSwitchNavigator(
    {
      AuthLoading,
      Auth,
      MainNavi,
    },
    {
      initialRouteName: 'AuthLoading',
    },
  ),
);
{% endraw %}
```

We can use createSwitchNavigator like above. AuthLoading component checks the user already logged in or not, If not logged in, show Auth screen, If logged in, show MainNavi screen.

In V5, `createSwitchNavigator` does not exist, so If you want to implement Auth process like above, you should make it on the navigation.

```js
{% raw %}
import React, {useContext} from 'react';
import {NavigationContainer} from '@react-navigation/native';
...
import {UserContext} from '~/Context/User';
...
export default () => {
  const {userInfo} = useContext<IUserContext>(UserContext);

  return (
    <NavigationContainer>
      {userInfo ? <MainNavi /> : <LoginStackNavi />}
    </NavigationContainer>
  );
};
{% endraw %}
```

In V5, createSwitchNavigator is gone, but V5 is like React components unlike V4.  So we can implement that Navigation component checks the login status and displays the screen depends on the status.

You can see the details about this in the official site, too.

- Official site: [react-navigation - Auth flow](https://reactnavigation.org/docs/auth-flow){:rel="nofollow noreferrer" target="_blank" }

### How to use Stack Navigation

In react-navigation V4, you used Stack Navigation like below.

```js
{% raw %}
...
import {createStackNavigator} from 'react-navigation-stack';
...
const MainNavi = createStackNavigator({
  MainTab: {
    screen: MainTab,
    navigationOptions: ({navigation}) => ({
      header: null,
    }),
  },
  FullDetail,
});
...
{% endraw %}
```

In react-navigation V5, you can use Stack Navigation like below.

```js
{% raw %}
...
import {
  createStackNavigator,
} from '@react-navigation/stack';
...
const Stack = createStackNavigator();
...
const LoginStackNavi = () => {
  return (
    <Stack.Navigator
      screenOptions={{
        headerStyle: {
          backgroundColor: '#f4511e',
        },
        headerTintColor: '#fff',
        headerTitleStyle: {
          fontWeight: 'bold',
        },
      }}>
      <Stack.Screen
        name="SignIn"
        component={SignIn}
        options={{
          headerShown: false,
        }}
      />
      <Stack.Screen
        name="SignUp"
        component={SignUp}
        options={{headerBackTitleVisible: false}}
      />
      <Stack.Screen name="ResetPassword" component={ResetPassword} />
    </Stack.Navigator>
  );
};
{% endraw %}
```

In react-navigation V5, If you want to apply the properties for the common header, you can use `screenOptions` in `Stack.Navigator`.

If you want to set the header properties to the specific screen, you can use `options` in `Stack.Screen`.

The example above includes to hide Header Bar by using `headerShown` in `options`.

```js
{% raw %}
<Stack.Screen
  name="SignIn"
  component={SignIn}
  options={{
    headerShown: false,
  }}
/>
{% endraw %}
```

Also, it includes to hide Back Button title by using `headerBackTitleVisible` in `options`.

```js
{% raw %}
<Stack.Screen
  name="SignUp"
  component={SignUp}
  options={{headerBackTitleVisible: false}}
/>
{% endraw %}
```

{% include in-feed-ads.html %}

### How to use Drawer Navigation

In react-navigation V5, you can implement Drawer Navigation like below.

```js
{% raw %}
...
import {
  createDrawerNavigator,
  DrawerContentScrollView,
  DrawerItemList,
  DrawerItem,
  DrawerContentComponentProps,
  DrawerContentOptions,
  DrawerNavigationProp,
} from '@react-navigation/drawer';
...
const Drawer = createDrawerNavigator();
...
const CustomDrawerContent = (
  props: DrawerContentComponentProps<DrawerContentOptions>,
  logout: () => void,
) => {
  return (
    <DrawerContentScrollView {...props}>
      <DrawerItemList {...props} />
      <DrawerItem label="Logout" onPress={() => logout()} />
    </DrawerContentScrollView>
  );
};
const DrawNavi = () => {
  const {logout} = useContext<IUserContext>(UserContext);

  return (
    <Drawer.Navigator
      drawerContent={props => CustomDrawerContent(props, logout)}>
      <Drawer.Screen name="TabNavi" component={TabNavi} />
      <Drawer.Screen name="MaterialTabNavi" component={MaterialTabNavi} />
      <Drawer.Screen
        name="MaterialTopTabNaviStackNavi"
        component={MaterialTopTabNaviStackNavi}
      />
    </Drawer.Navigator>
  );
};
...
{% endraw %}
```

This example is a little bit complicated because of `Logout` feature. Except for the logout feature, it looks like below.

```js
{% raw %}
...
import {
  createDrawerNavigator,
} from '@react-navigation/drawer';
...
const Drawer = createDrawerNavigator();
...
const DrawNavi = () => {
  return (
    <Drawer.Navigator>
      <Drawer.Screen name="TabNavi" component={TabNavi} />
      <Drawer.Screen name="MaterialTabNavi" component={MaterialTabNavi} />
      <Drawer.Screen
        name="MaterialTopTabNaviStackNavi"
        component={MaterialTopTabNaviStackNavi}
      />
    </Drawer.Navigator>
  );
};
...
{% endraw %}
```

It is very similar to Stack Navigation. The example above is to add `Logout` menu to Drawer Navigation and press it to logout, so it became complicated.

### How to use Bottom Tab Navigation

In react-navigation V5, you can implement Bottom Tab Navigation.

```js
{% raw %}
...
import {createBottomTabNavigator} from '@react-navigation/bottom-tabs';
import Icon from 'react-native-vector-icons/MaterialIcons';
...
const Tab = createBottomTabNavigator();
...
const TabNavi = () => {
  return (
    <Tab.Navigator>
      <Tab.Screen
        name="TabFirstStackNavi"
        component={TabFirstStackNavi}
        options={{
          tabBarLabel: 'Frist',
          tabBarIcon: ({color}) => <Icon name="home" color={color} size={26} />,
        }}
      />
      <Tab.Screen
        name="TabSecond"
        component={TabSecond}
        options={{
          tabBarLabel: 'Second',
          tabBarIcon: ({color}) => (
            <Icon name="people" color={color} size={26} />
          ),
        }}
      />
      <Tab.Screen
        name="TabThird"
        component={TabThird}
        options={{
          tabBarLabel: 'Third',
          tabBarIcon: ({color}) => (
            <Icon name="message" color={color} size={26} />
          ),
        }}
      />
      <Tab.Screen
        name="TabFourth"
        component={TabFourth}
        options={{
          tabBarLabel: 'Fourth',
          tabBarIcon: ({color}) => (
            <Icon name="settings" color={color} size={26} />
          ),
        }}
      />
    </Tab.Navigator>
  );
};
...
{% endraw %}
```

In the example above, I used `options` in `Tab.Screen` to show Label and Icon.

```js
{% raw %}
<Tab.Screen
  ...
  options={{
    tabBarLabel: 'Fourth',
    tabBarIcon: ({color}) => (
      <Icon name="settings" color={color} size={26} />
    ),
  }}
/>
```

{% include in-feed-ads.html %}

### How to use Material Bottom Tab Navigation

In react-navigation V5, you can implement Bottom Tab Navigation.

```js
...
import {createMaterialBottomTabNavigator} from '@react-navigation/material-bottom-tabs';
import Icon from 'react-native-vector-icons/MaterialIcons';
...
const MaterialTab = createMaterialBottomTabNavigator();
...
const MaterialTabNavi = () => {
  return (
    <MaterialTab.Navigator>
      <MaterialTab.Screen
        name="TabFirstStackNavi"
        component={TabFirstStackNavi}
        options={{
          tabBarColor: '#281b39',
          tabBarLabel: 'Frist',
          tabBarIcon: ({color}) => <Icon name="home" color={color} size={26} />,
        }}
      />
      <MaterialTab.Screen
        name="TabSecond"
        component={TabSecond}
        options={{
          tabBarColor: '#0e141d',
          tabBarLabel: 'Second',
          tabBarIcon: ({color}) => (
            <Icon name="people" color={color} size={26} />
          ),
        }}
      />
      <MaterialTab.Screen
        name="TabThird"
        component={TabThird}
        options={{
          tabBarColor: '#E64A19',
          tabBarLabel: 'Third',
          tabBarIcon: ({color}) => (
            <Icon name="message" color={color} size={26} />
          ),
        }}
      />
      <MaterialTab.Screen
        name="TabFourth"
        component={TabFourth}
        options={{
          tabBarColor: '#524365',
          tabBarLabel: 'Fourth',
          tabBarIcon: ({color}) => (
            <Icon name="settings" color={color} size={26} />
          ),
        }}
      />
    </MaterialTab.Navigator>
  );
};
{% endraw %}
```

You should set Tab Bar icon to use Material Bottom Tab Navigation.

```js
{% raw %}
<MaterialTab.Screen
  ...
  options={{
    ...
    tabBarIcon: ({color}) => (
      <Icon name="settings" color={color} size={26} />
    ),
  }}
/>
{% endraw %}
```

Also, you can set `tabBarColor` to change the tab bar color by touching the tab.

```js
{% raw %}
<MaterialTab.Screen
  ...
  options={{
    ...
    tabBarColor: '#524365',
    ...
  }}
/>
{% endraw %}
```

tabBarIcon option is the required option, but tabBarColor is you can implement only you need.

### How to useMaterial Top Tab Navigation

In react-navigation V5, you can implement Material Top Tab Navigation like below.

```js
{% raw %}
...
import {createMaterialTopTabNavigator} from '@react-navigation/material-top-tabs';
...
const MaterailTopTab = createMaterialTopTabNavigator();
...
const MaterialTopTabNavi = () => {
  return (
    <MaterailTopTab.Navigator>
      <MaterailTopTab.Screen name="TabFirst" component={TabFirst} />
      <MaterailTopTab.Screen name="TabSecond" component={TabSecond} />
      <MaterailTopTab.Screen name="TabThird" component={TabThird} />
      <MaterailTopTab.Screen name="TabFourth" component={TabFourth} />
    </MaterailTopTab.Navigator>
  );
};
...
const MaterialTopTabNaviStackNavi = ({navigation}: DrawerProp) => {
  return (
    <Stack.Navigator
      screenOptions={{
        headerLeft: (props: StackHeaderLeftButtonProps) => (
          <IconButton
            iconName="menu"
            onPress={() => navigation.openDrawer()}
            color="black"
          />
        ),
      }}>
      <Stack.Screen name="MaterialTopTabNavi" component={MaterialTopTabNavi} />
    </Stack.Navigator>
  );
};
...
{% endraw %}
```

Simply, We can use Material Top Tab Navigation like below.

```js
{% raw %}
const MaterialTopTabNavi = () => {
  return (
    <MaterailTopTab.Navigator>
      <MaterailTopTab.Screen name="TabFirst" component={TabFirst} />
      <MaterailTopTab.Screen name="TabSecond" component={TabSecond} />
      <MaterailTopTab.Screen name="TabThird" component={TabThird} />
      <MaterailTopTab.Screen name="TabFourth" component={TabFourth} />
    </MaterailTopTab.Navigator>
  );
};
{% endraw %}
```

However, the above is not shown up perfectly in `Notch Design`.

![material top navigation issue in notch design](/assets/images/category/react-native/2018/react-navigation-v5/notch-design-material-top-navigation-problem.jpg)

To solve this problem, I recommend you wrap it by Stack Navigation like below.

```js
{% raw %}
...
const MaterialTopTabNavi = () => {
  return (
    <MaterailTopTab.Navigator>
      <MaterailTopTab.Screen name="TabFirst" component={TabFirst} />
      <MaterailTopTab.Screen name="TabSecond" component={TabSecond} />
      <MaterailTopTab.Screen name="TabThird" component={TabThird} />
      <MaterailTopTab.Screen name="TabFourth" component={TabFourth} />
    </MaterailTopTab.Navigator>
  );
};
...
const MaterialTopTabNaviStackNavi = ({navigation}: DrawerProp) => {
  return (
    <Stack.Navigator
      screenOptions={{
        headerLeft: (props: StackHeaderLeftButtonProps) => (
          <IconButton
            iconName="menu"
            onPress={() => navigation.openDrawer()}
            color="black"
          />
        ),
      }}>
      <Stack.Screen name="MaterialTopTabNavi" component={MaterialTopTabNavi} />
    </Stack.Navigator>
  );
};
...
{% endraw %}
```

If you warp with Stack Navigation, you can see the result like below.

![notch design에서 material top navigation의 문제점 해결](/assets/images/category/react-native/2018/react-navigation-v5/solution-notch-design-material-top-navigation-problem.jpg)

{% include in-feed-ads.html %}

### Drawer Open

If you only use Drawer Navigation, you can see the result like below.

<div class="half_image_container">
  <img class="half_image" src="/assets/images/category/react-native/2018/react-navigation-v5/drawer.gif" alt="React Navigation V5 drawer Navigation">
</div>
[picture: [reactnavigation.org Official site](https://reactnavigation.org/docs/drawer-navigator){:rel="nofollow noreferrer" target="_blank" }]

To open Drawer navigaiton, you need to swipe left to right.

However, we implement it by adding a menu icon on the left of the Navigation Header and touching it to show Drawer Navigation, normally.

So, I've implemented it by adding the menu icon to the left of the navigation header and calling `openDrawer` function if it is touched.

```js
{% raw %}
...
import {
  ...
  DrawerNavigationProp,
} from '@react-navigation/drawer';
...
type TypeDrawerProp = DrawerNavigationProp<
  {
    TabNavi: undefined;
    MaterialTabNavi: undefined;
    MaterialTopTabNaviStackNavi: undefined;
    Logout: undefined;
  },
  'TabNavi'
>;
interface DrawerProp {
  navigation: TypeDrawerProp;
}
...
const MaterialTopTabNaviStackNavi = ({navigation}: DrawerProp) => {
  return (
    <Stack.Navigator
      screenOptions={{
        headerLeft: (props: StackHeaderLeftButtonProps) => (
          <IconButton
            iconName="menu"
            onPress={() => navigation.openDrawer()}
            color="black"
          />
        ),
      }}>
      <Stack.Screen name="MaterialTopTabNavi" component={MaterialTopTabNavi} />
    </Stack.Navigator>
  );
};
{% endraw %}
```

### DrawerActions

In the example above, if the screen is under Drawer Navigation directly, you can open the Drawer using the navigation Props.
However, like below, if the screen is not under Drawer Navigation directly, you can not open and close the Drawer navigation.

```js
{% raw %}
...
const MainTabs = () => {
  return (
    <BottomTab.Navigator tabBarOptions={{activeTintColor: 'black'}}>
      <BottomTab.Screen name="MyFeed" component={MyFeed}/>
      <BottomTab.Screen name="Feeds" component={Feeds}/>
      <BottomTab.Screen name="Upload" component={Upload}/>
      <BottomTab.Screen name="Notification" component={Notification}/>
      <BottomTab.Screen name="Profile" component={Profile}/>
    </BottomTab.Navigator>
  );
};
...
const MainNavigator = () => {
  return (
    <Drawer.Navigator
      drawerPosition="right"
      drawerType="slide"
      drawerContent={props => <CustomDrawer props={props} />}>
      <Drawer.Screen name="MainTabs" component={MainTabs} />
    </Drawer.Navigator>
  );
};
{% endraw %}
```

Because, The screen can only get the parenet Navigation Props. In the example above, the parent of `Profile` screen in `MainTab` is Bottom Tab navigation not Drawer Navigation. In this case, we can not use `navigation.openDrawer()`.

In this case, we can use `DrawerActions`.

If the screen is not directly under Drawer Navigation, but is the children of Drawer Navigation, You can open the Drawer like below.

```js
{% raw %}
...
import {DrawerActions} from '@react-navigation/native';
...
type NavigationProp = StackNavigationProp<ProfileTabParamList, 'Profile'>;
interface Props {
  navigation: NavigationProp;
}

const Profile = ({navigation}: Props) => {
  return (
    <ScrollView>
      ...
      <IconButton
        iconName="menu"
        onPress={() => navigation.dispatch(DrawerActions.openDrawer())}
      />
      ...
    </ScrollView>
  );
});

export default Profile;
{% endraw %}
```

You can open the Drawer Navigation by using `navigation.dispatch(DrawerActions.openDrawer())`. You can also use the functions below.

```js
navigation.dispatch(DrawerActions.openDrawer());
navigation.dispatch(DrawerActions.closeDrawer());
navigation.dispatch(DrawerActions.toggleDrawer());
```

{% include in-feed-ads.html %}

### setParams / getParams

In react-navigation V4, you used the code below to exchange Data between the screens.

```js
...
navigation.setParams({
  showSearch: false,
});
...
const showSearch = navigation.getParam('showSearch');
```

In react-navigation V5, you can use `setParams`, but you can not use `getParams`.

```js
navigation.setParams({
  showSearch: false,
});
```

In react-navigation V5, you can use `route.params` instead of `getParams`.

```js
...
import { RouteProp } from '@react-navigation/native';
...

type ProfileScreenRouteProp = RouteProp<MovieNaviParamList, 'MovieDetail'>;
interface Props {
  route: ProfileScreenRouteProp;
}

const MovieDetail = ({ route }: Props) => {
  const { id } = route.params;
  ...
});

export default MovieDetail;
```

It looks a little bit complicated because of Typescript.

```js
const MovieDetail = ({ route, navigation }) => {
  const { id } = route.params;
  ...
});
```

It looks like above. You can use route Props that comes with navigation Props.

## Typescript

Let's see how to use Typescript in react-navigation v5.

### navigation

To navigate the screen, you use the source code with navigation Props like below.

```js
const Feeds = ({navigation}: Props) => {
  ...
  navigation.navigate('FeedListOnly');
  ...
});
```

For this, you should write Typescript like below.

```js
...
import {StackNavigationProp} from '@react-navigation/stack';
...
// Stack Navigation
type NavigationProp = StackNavigationProp<FeedsTabParamList, 'Feeds'>;
interface Props {
  navigation: NavigationProp;
}

const Feeds = ({navigation}: Props) => {
  ...
  navigation.navigate('FeedListOnly');
  ...
});
```

In above, FeedsTabParamList is a common Type, so make `@types/index.d.ts` file and modify it like below.

```js
type FeedsTabParamList = {
  Feeds: undefined;
  FeedListOnly: undefined;
};
```

This Stack Navigation has `Feeds` and `FeedListOnly` screens. In this case, it doesn't have the parameters to navigate the screen, so set `undefined`.

If the screen need the parameters,

```js
type FeedsTabParamList = {
  Feeds: undefined;
  FeedListOnly: {
    id: number;
  };
};
```

Define the type like above,

```js
const Feeds = ({navigation}: Props) => {
  ...
  navigation.navigate('FeedListOnly', {
    id: 1,
  });
  ...
});
```

And navigate the screen with the parameter. It looks very complicated but it is for checking types correctly.

In above, I introduced Stack Navigation, and you can also use each Navigation Props like below.

```js
import {BottomTabNavigationProp} from '@react-navigation/bottom-tabs';
import {DrawerNavigationProp} from '@react-navigation/drawer';
import {MaterialBottomTabNavigationProp} from '@react-navigation/material-bottom-tabs';
import {MaterialTopTabBarProps} from '@react-navigation/material-top-tabs';
```

The usage is the same as Stack Navigation.

```js
type NavigationProp = BottomTabNavigationProp<FeedsTabParamList, 'Feeds'>;
type NavigationProp = DrawerNavigationProp<FeedsTabParamList, 'Feeds'>;
type NavigationProp = MaterialBottomTabNavigationProp<FeedsTabParamList, 'Feeds'>;
type NavigationProp = MaterialTopTabBarProps<FeedsTabParamList, 'Feeds'>;
```

### route

In above, you can use `navigation.setParams` to send tha data between the screens. At this time, you use `route.params`.

To use `route` Props, you use Typescript like below.

```js
...
import { RouteProp } from '@react-navigation/native';
...
type ProfileScreenRouteProp = RouteProp<MovieNaviParamList, 'MovieDetail'>;
interface Props {
  route: ProfileScreenRouteProp;
}

const MovieDetail = ({ route }: Props) => {
  const { id } = route.params;
  ...
});

export default MovieDetail;
```

In here, `MovieNaviParamList` is also used for many screens, so make `@types/index.d.ts` file and modify it like below.

```js
type MovieNaviParamList = {
  MovieHome: undefined;
  MovieDetail: {
    id: number;
  };
};
```

## Completed

We've seen how to install react-navigation V5 and how to implement it. I was surprised by the differences between V4 and V5, but V5 looks like React Components, so I think it is more friendly to React development.

I think all previous features can be implemented. In the react-navigation V5 example, I've implemented the previous example of react-navigation V4. If you want to use react-navigation V5, see the example below first!

- react-navigation-exercise V5: [https://github.com/dev-yakuza/react-navigation-v5-exercise](https://github.com/dev-yakuza/react-navigation-v5-exercise){:rel="nofollow noreferrer" target="_blank" }

## Reference

- Official site: [react-navigation](https://reactnavigation.org/docs){:rel="nofollow noreferrer" target="_blank" }
