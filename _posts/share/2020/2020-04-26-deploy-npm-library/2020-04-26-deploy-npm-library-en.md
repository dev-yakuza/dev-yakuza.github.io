---
layout: 'post'
permalink: '/share/deploy-npm-library/'
paginate_path: '/share/:num/deploy-npm-library/'
lang: 'en'
categories: 'share'
comments: true

title: Deploy your library to NPM
description: Let's see how to deploy Javascript library which you develop to NPM.
image: '/assets/images/category/share/2020/deploy-npm-library/background.jpg'
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [Create NPM account](#create-npm-account)
- [npm info](#npm-info)
- [npm init](#npm-init)
- [npm login](#npm-login)
- [npmignore](#npmignore)
- [npm publish](#npm-publish)
- [npm version](#npm-version)
- [Completed](#completed)

</div>

## Outline

Until now, when I develop with React Native, I use many open source libraries someone developed. I feel always appreciation developers, and I wanted to pay back. So I decided to develop an open source and made `react-native-image-modal` that is a simple open source.

- NPM: [react-native-image-modal](https://www.npmjs.com/package/react-native-image-modal){:rel="nofollow noreferrer" target="_blank"}

If you want to know how to develop React Native open source library, see the blog post below.

- [Make Opensource for React Native]({{site.url}}/react-native/make-opensource-library/){:target="_blank"}

In this blog post, I will share how to deploy Javascript which you developed to NPM(Node Package Manager).

## Create NPM account

To deploy your library to NPM, you need a NPM service account.

If you don't have NPM account, click the link below to go to NPM service site, and create NPM account.

- NPM service site: [https://www.npmjs.com/](https://www.npmjs.com/){:rel="nofollow noreferrer" target="_blank"}

## npm info

Before deploying your Javascript library, we need to check the package name is deployable. Of course, you can not deploy the same name of the libraries deployed already on  NPM.

Execute the command below to check your Javascript library is deployable.

```bash
npm info [Javascript Package Name]
```

If the name is duplicated, you can see the information of the library which was deployed on NPM.

```bash
npmdeploy@1.0.1 | MIT | deps: 1 | versions: 1
deploy projects easily in the cloud. Optimised for GitLab CI
https://gitlab.com/pushrocks/npmdeploy#README

keywords: deploying, made, easy

dist
.tarball: https://registry.npmjs.org/npmdeploy/-/npmdeploy-1.0.1.tgz
.shasum: c298d768aac7ccb89a38c20a0c904341fc87c484

dependencies:
gitlab: ^1.6.0

maintainers:
- lossless <npm@lossless.digital>

dist-tags:
latest: 1.0.1

published over a year ago by lossless <npm@lossless.digital>
```

If the name is not duplicated, you can see the `404` error like below.

```bash
npm ERR! code E404
npm ERR! 404 'temp-npmdeploy' is not in the npm registry.
npm ERR! 404 You should bug the author to publish it
npm ERR! 404 (or use the name yourself!)
npm ERR! 404
npm ERR! 404 Note that you can also install from a
npm ERR! 404 tarball, folder, http url, or git url.
npm ERR! 404
npm ERR! 404  'temp-npmdeploy@latest' is not in the npm registry.
npm ERR! 404 You should bug the author to publish it (or use the name yourself!)
npm ERR! 404
npm ERR! 404 Note that you can also install from a
npm ERR! 404 tarball, folder, http url, or git url.
```

{% include in-feed-ads.html %}

## npm init

To deploy your Javascript library to NPM, we need to set the information that NPM needs.

Go to your Javascript library folder, and execute the command below.

```bash
# cd ProjectName
npm init
```

After executing the command above, you can see the screen like below. The contents in this part are updatable after, so don't worry about doing wrong.

```bash
This utility will walk you through creating a package.json file.
It only covers the most common items, and tries to guess sensible defaults.

See `npm help json` for definitive documentation on these fields
and exactly what they do.

Use `npm install <pkg>` afterwards to install a package and
save it as a dependency in the package.json file.

Press ^C at any time to quit.
package name: (npmdeploy)
```

NPM asks which you want to make the `package name` based on the folder name, or others. We already found the name which is deployable via `npm info`. Insert it in here.

```bash
version: (1.0.0)
```

Next, NPM asks the version. The version is basically `major.minor.patch`. If your library is already completed to develop, just set `1.0.0`. If your library is still developing and not completed, set the version like `0.0.1` to notice your library is not stable.

```bash
description:
```

Next is the details about Javascript library. Insert the description about your library.

```bash
entry point: (index.js)
```

Set the Entry file(Main file) of your Javascript library.

```bash
test command:
```

Insert your test command for your Javascript library. If you don't have the test command, just insert Enter key.

```bash
git repository:
```

Insert Git repository URL for users to check your Javascript source code. If you don't have, just insert Enter key.

```bash
keywords:
```

Insert the keyword about your Javascript library.(ex> jQuery, react-native, reactjs, etc)

```bash
author:
```

Insert the author information. Normally, `Name <Email Address>` format is used.

```bash
license: (ISC)
```

Next is about your library license. Insert the license according to your library. (ex> MIT, ISC etc)

If you want to know the keyword of the licesen, see the link below.

- [GitHub license type](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/licensing-a-repository#searching-github-by-license-type)

After inserting all, you can see `package.json` file is generated in your library folder.

{% include in-feed-ads.html %}

## npm login

To deploy your library to NPM, we need to login the NPM service by executing the command below.

```bash
npm login
```

When you executed the command above, the login process is started like below.

```bash
Username: dev-yakuza
Password:
Email: (this IS public) dev.yakuza@gmail.com
Logged in as dev-yakuza on https://registry.npmjs.org/.
```

Insert NPM account information created above. After signing in, execute the command below to check login well.

```bash
npm whoami
# dev-yakuza
```

## npmignore

There are some files required for development, not for the library completed to develop. For example, test code or source code for the example it is. We need for these files to write on `.npmignore` file.

Below is my `.npmignore` file that I used when I develop `react-native-image-modal` library.

```bas
node_modules
Develop
DevelopWithExpo
Example
ExampleWithExpo
.github
demo
```

## npm publish

We're ready to deploy your library to NPM. Execute the command below to deploy your library to NPM.

```bash
npm publish
```

If you want to execute the some commands just before deploying, modify `package.json` like below.

```json
"scripts": {
  ...
  "prepare": "rm -rf dist && tsc"
},
```

I used Typescript to develop the library, so I needed to build the Typescript before deployment. as defined `prepare` command in `scripts` of `package.json` file like above, when you execute `npm publish`, before executing `npm publish`, this command is executed.

You just deployed your library to NPM! To use your deployed library, the command below is used just like when you use other libraries via NPM.

```bash
npm install --save [Your Package Name]
```

{% include in-feed-ads.html %}

## npm version

After the library is deployed to NPM, sometimes, you need to update the library. At this time, you need to update the version of the library.

To update the version, you can modify `package.json` file directly(`"version": "0.0.1"`), also, you can use the command like below.

```bash
npm version patch
npm version minor
npm version major
```

If you use the commands according to your situation, you can update the version easily.

## Completed

Done! We've seen how to deploy Javascript library that you develop to NPM. After I developed and deployed the first open source, I felt that I finally join the developer's culture.

![NPM react-native-image-modal](/assets/images/category/share/2020/deploy-npm-library/npm-react-native-image-modal.jpg)

Let's make and deploy your open source to join the beautiful developer's culture!
