---
layout: 'post'
permalink: '/react-native/make-opensource-library/'
paginate_path: '/react-native/:num/make-opensource-library/'
lang: 'en'
categories: 'react-native'
comments: true

title: Make Opensource for React Native
description: Let's see how to make an opensource for React Naitve.
image: '/assets/images/category/react-native/2020/make-opensource-library/background.jpg'
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [NPM](#npm)
- [GitHub repository](#github-repository)
- [package.json](#packagejson)
- [Development environment](#development-environment)
- [Develop library](#develop-library)
- [Deploy](#deploy)
- [Completed](#completed)

</div>

## Outline

When I develop the projects by React Native, always I use many open sources created by other people. So, I felt I should pay back by developing an open source, but I didn't because of no time(it is just excused)

However, when I had the extra time, and I tried to develop the open-source, I had no idea how to start it. I think you want to make an opensource, but don't know how to make it just like me, so I share how to make the open source for you.

The link below is my open source.

- NPM: [react-native-image-modal](https://www.npmjs.com/package/react-native-image-modal){:rel="nofollow noreferrer" target="_blank"}

## NPM

In this blog post, I will introduce how to make Javascript library of React Native, not Native modules.

To deploy Javascript open source, you need to deploy it to NPM(Node Pacakge Manager).

- NPM: [react-native-image-modal](https://www.npmjs.com/package/react-native-image-modal){:rel="nofollow noreferrer" target="_blank"}

Before creating an open source, I recommend you see the blog post below to prepare your open source for deploying on NPM.

- [Deploy your library to NPM]({{site.url}}/share/deploy-npm-library/){:target="_blank"}

## GitHub repository

To share the open soruce, GitHub is best way. To share your open source, create GitHub repository.

If you don't have GitHub account, click the link below to create free account.

- GitHub:[https://github.com/](https://github.com/){:rel="nofollow noreferrer" target="_blank"}

When you create GitHub repository, you should make a name not duplicated with libraries deployed already on NPM. You can see the link below about how to search a package name not duplicated on NPM.

- Deploy your library to NPM: [npm info]({{site.url}}/share/deploy-npm-library/#npm-info){:target="_blank"}

If you make GitHub repository, clone it on your local PC.

```bash
git clone [Your repository URL]
```

{% include in-feed-ads.html %}

## package.json

To develop and deploy Javascript open source, you need `package.json` file. Execute the command below to create package.json file.

```bash
# cd [Your Project folder]
npm init
```

If you want to know details about how to make package.json file, see the link below.

- Deploy your library to NPM: [npm init]({{site.url}}/share/deploy-npm-library/#npm-init){:target="_blank"}

## Development environment

I used `Typescript` to develop React Native library. In here I will show you how to make the development environment to develop React Native library by Typescript.

First, execute the command below to make React Native project.

```bash
react-native init Develop
```

This project is for developing React Native library. Next, create `tsconfig.json` file and modify it like below.

```json
{
  "compilerOptions": {
    "module": "esnext",
    "target": "es5",
    "lib": ["es6", "dom", "es2016", "es2017"],
    "sourceMap": true,
    "allowJs": false,
    "jsx": "react-native",
    "declaration": true,
    "declarationMap": true,
    "moduleResolution": "node",
    "forceConsistentCasingInFileNames": true,
    "noImplicitReturns": true,
    "noImplicitThis": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    "suppressImplicitAnyIndexErrors": true,
    "noUnusedLocals": true,
    "outDir": "dist",
    "skipLibCheck": true,
    "allowSyntheticDefaultImports": true,
    "removeComments": true
  },
  "include": ["src"],
  "exclude": ["node_modules", "Develop", "DevelopWithExpo", "Example", "ExampleWithExpo", "dist"]
}
```

I skip explaining about the options. Important options are that I will build files on `src` via `"include": ["src"],` option, and save the result files of build on `dist` folder by `"outDir": "dist",` option.

Next, open `package.json` file and modify it like below.

```json
{
  ...
  "main": "dist/index.js",
  "types": "dist/index.d.ts",
  "scripts": {
    "lint": "eslint --ext .tsx --ext .ts src/",
    "format": "prettier --check ./src",
    "start": "rm -rf Develop/dist && tsc -w --outDir Develop/dist",
    "start:expo": "rm -rf DevelopWithExpo/dist && tsc -w --outDir DevelopWithExpo/dist",
    "prepare": "rm -rf dist && tsc"
  },
  "lint-staged": {
    "src/**/*.{ts,tsx}": [
      "eslint --ext .tsx --ext .ts src/ --fix"
    ],
    "./src/**": [
      "prettier --write ."
    ]
  },
  "husky": {
    "hooks": {
      "pre-commit": "lint-staged"
    }
  },
  ...
  "peerDependencies": {
    "react": "*",
    "react-native": "*"
  },
  "devDependencies": {
    "@types/react": "*",
    "@types/react-native": "*",
    "@typescript-eslint/eslint-plugin": "2.25.0",
    "@typescript-eslint/parser": "2.25.0",
    "eslint": "6.8.0",
    "eslint-plugin-prettier": "3.1.2",
    "eslint-plugin-react": "7.19.0",
    "eslint-plugin-react-hooks": "2.5.1",
    "husky": "4.2.3",
    "lint-staged": "10.0.9",
    "prettier": "2.0.2",
    "react": "*",
    "react-native": "*",
    "typescript": "^3.7.5"
  },
}
```

Let's see one by one!

```json
"main": "dist/index.js",
"types": "dist/index.d.ts",
```

These notice the library's main file and type file to NPM.

```json
"scripts": {
  "lint": "eslint --ext .tsx --ext .ts src/",
  "format": "prettier --check ./src",
  "start": "rm -rf Develop/dist && tsc -w --outDir Develop/dist",
  "start:expo": "rm -rf DevelopWithExpo/dist && tsc -w --outDir DevelopWithExpo/dist",
  "prepare": "rm -rf dist && tsc"
},
```

These are the command for developing.

The `lint` and `format` commands format the developing source code via `eslint` and `prettier`.
Also, The `lint-sgate` and `husky` below format the source code when you execute `git commit`.

```json
"lint-staged": {
  "src/**/*.{ts,tsx}": [
    "eslint --ext .tsx --ext .ts src/ --fix"
  ],
  "./src/**": [
    "prettier --write ."
  ]
},
"husky": {
  "hooks": {
    "pre-commit": "lint-staged"
  }
},
```

If you want to know more about thease commands, see the blog post below.

- [Use ESLint, Prettier like Pro on React Native]({{site.url}}/{{page.categories}}/eslint-prettier-husky-lint-staged/){:target="_blank"}

When you develop the library, you'll execute `npm start` to build the source code via Typescript. Also, when you execute `npm publish` command to deploy your library, the command in `prepare` will be executed automatically to build the source code via Typescript before deploying the library.

If you want to know more about `npm publish` and `prepare`, see the blog post below.

- Deploy your library to NPM: [npm publish]({{site.url}}/share/deploy-npm-library/#npm-publish){:target="_blank"}

The libraries required for developing are defined on `devDepenencies`. Execute the command below to install the libraries.

```bash
npm install
```

After installing, create `.gitignore` file and `.prettierignore` file, and add `node_modules` to them.

Done! we're ready to develop. Next, let's see how to develop the library.

{% include in-feed-ads.html %}

## Develop library

As you see the development environment settings above, we need to create the source code in `src` folder. Create `index.tsx` file on `src` folder, and modify it like below.

```js
import React from 'react';
import { View, Text } from 'react-native';

const LibraryName = (): JSX.Element => {
  return (
    <View>
      <Text>Hello World!</Text>
    </View>
  );
};

export default LibraryName;
```

And then, open `App.js` file in `Develop` folder and modify it like below.

```js
import React from 'react';
import {StyleSheet,   SafeAreaView} from 'react-native';

import LibraryName from './dist';

const App = () => {
  return (
    <SafeAreaView style={styles.container}>
      <LibraryName />
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

export default App;
```

And execute the command below to build the source code via Typescript.

```bash
npm start
```

The `start` command in `package.json` is below as we created above.

```bash
"start": "rm -rf Develop/dist && tsc -w --outDir Develop/dist",
```

As you see the details of the command, the command deletes `Develop/dist` folder, build via `tsc`, and save the build result files on `Develop/dist` folder. Also, we used `-w` option, so when the source code is modified, Typescript will rebuild it. Therefore, to develop the library, we need to execute this command.

And then, open another `Terminal` or `CMD`, and execute the command below.

```bash
cd Develop
npm run ios
# npm run android
```

After executing, we can see the library on the screen like below

![Make Opensource for React Native - Hello world](/assets/images/category/react-native/2020/make-opensource-library/hello-world.jpg)

Again, when you open `src/index.tsx` file and modify it, you can see the modification on the simulator automatically.

## Deploy

After developing the library, we need to execute the commands like below to deploy it.

```bash
npm login
npm publish
```

About more details, see the blog post below.

- [Deploy your library to NPM]({{site.url}}/share/deploy-npm-library/){:target="_blank"}

## Completed

We've seen how to develop React Native library. To deploy `NPM`, we should see the blog post about NPM, so it makes a little bit difficult.

If you have time, develop a great open source and join the great developer culture!
