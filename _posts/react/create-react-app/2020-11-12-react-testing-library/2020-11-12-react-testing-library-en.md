---
layout: 'post'
permalink: '/react/create-react-app/react-testing-library/'
paginate_path: '/react/:num/create-react-app/react-testing-library/'
lang: 'en'
categories: 'react'
comments: true

title: 'Test with react-testing-library in create-react-app'
description: Let's see how to use react-testing-library to test the React project created by create-react-app.
image: '/assets/images/category/react/create-react-app/typescript/background.jpg'
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [react-testing-library](#react-testing-library)
- [Create Counter app](#create-counter-app)
  - [Button component](#button-component)
  - [App component](#app-component)
- [Test](#test)
  - [Test Button component](#test-button-component)
  - [Test App component](#test-app-component)
- [Code coverage](#code-coverage)
- [Completed](#completed)

</div>

## create-react-app series

This blog post is a series. You can see other blog posts of the series on the list.

- [What is React]({{site.url}}/{{page.categories}}/create-react-app/react/){:target="_blank"}
- [create-react-app]({{site.url}}/{{page.categories}}/create-react-app/start/){:target="_blank"}
- [TypeScript in create-react-app]({{site.url}}/{{page.categories}}/create-react-app/typescript/){:target="_blank"}
- [[TypeScript] Make Import path based on Root in create-react-app]({{site.url}}/{{page.categories}}/create-react-app/root-import/){:target="_blank"}
- [styled-components in create-react-app]({{site.url}}/{{page.categories}}/create-react-app/styled-components/){:target="_blank"}
- [Jest]({{site.url}}/{{page.categories}}/create-react-app/jest/){:target="_blank"}
- Test with react-testing-library in create-react-app

## Outline

In previous blog post, I introduced how to use `Jest`(JavaScript test framework) to test the JavaScript. In this blog post, I will show you how to use `react-testing-library` to test the React project that is created by `create-react-app`.

You can see the source code of the blog post in the link below.

- GitHub: [https://github.com/dev-yakuza/study-create-react-app/tree/main/6.react-test](https://github.com/dev-yakuza/study-create-react-app/tree/main/6.react-test){:rel="noopener" target="_blank"}

## react-testing-library

`Jest` which I introduced on the previous blog post, is a JavaScript test framework, is used to test JavaScript. `react-testing-library` the I'll introduce on this blog post is a test library optimized for testing React.

- react-testing-library: [https://testing-library.com/docs/react-testing-library/intro/](https://testing-library.com/docs/react-testing-library/intro/){:rel="noopener" target="_blank"}

If you create the React project by create-react-app, `react-testing-library` is also installed automatically like `Jest`. So you don't need any installation to use `react-testing-library`.

In this blog, you can see an example about how to use react-testing-library.

{% include in-feed-ads.html %}

## Create Counter app

Let's prepare a React project to learn how to use react-testing-library. In this blog post, we'll create the Counter app like below.

![Counter app](/assets/images/category/react/create-react-app/react-testing-library/counter.jpg)

Execute the command below to create the React project with TypeScript.

```bash
npx create-react-app react-test --template=typescript
```

And then, modify `tsconfig.json` file like below to use the absolute path importing.

```json
{
  "compilerOptions": {
    ...
    "jsx": "react-jsx",
    "baseUrl": "src"
  },
  ...
}
```

Lastly, execute the command below to install `styled-components` to use it on the React project.

```bash
npm install --save styled-components
npm install --save-dev @types/styled-components jest-styled-components
```

### Button component

Let's make the Button component that is used for the plus/minus buttons on the Counter App. Create `./src/Components/Button/index.tsx` file and modify it like below.

```js
import React from "react";
import Styled from "styled-components";

interface ContainerProps {
  readonly backgroundColor?: string;
}

const Container = Styled.div<ContainerProps>`
  padding: 10px 15px;
  border-radius: 5px;
  background-color: ${(props) => props.backgroundColor};
  color: white;
  font-weight: bold;
  cursor: pointer;
`;

interface Props {
  readonly label: string;
  readonly backgroundColor?: string;
  readonly onClick?: () => void;
}
export const Button = ({ label, backgroundColor, onClick }: Props) => {
  return (
    <Container backgroundColor={backgroundColor} onClick={onClick}>
      {label}
    </Container>
  );
};
```

This blog post is about how to use react-testing-library, so I skip the details about how to make a React component.

{% include in-feed-ads.html %}

### App component

Let's make the Counter App with the button component we've created above. Open `./src/App.tsx` file and modify it like below.

```js
import React, { useState } from "react";
import Styled from "styled-components";

import { Button } from "Components/Button";

const Container = Styled.div`
  display: flex;
  min-height: 100vh;
  align-items: center;
  justify-content: center;
  background-color: #F5F5F5;
`;

const Label = Styled.div`
  margin: 10px;
  width: 40px;
  text-align: center;
`;

function App() {
  const [count, setCount] = useState(0);
  return (
    <Container>
      <Button
        label="-"
        backgroundColor="#FF1744"
        onClick={() => setCount(count - 1)}
      />
      <Label>{count}</Label>
      <Button
        label="+"
        backgroundColor="#304FFE"
        onClick={() => setCount(count + 1)}
      />
    </Container>
  );
}

export default App;
```

After modifying, execute the command below to check the app is working well.

```bash
npm start
```

If you don't have any problem, you can see the screen like below on your browser.

![create-react-app with typescript](/assets/images/category/react/create-react-app/root-import/project.jpg)

{% include in-feed-ads.html %}

## Test

Let's test the Counter App with Jest and react-testing-library. First, delete the `./src/App.test.tsx` file, and execute the command below to start Jest.

```bash
npm run test
```

### Test Button component

Let's test the Button component. To test Button component, create `./src/Components/Button/index.test.tsx` file and modify it like below.

```js
import React from 'react';
import { render, screen } from '@testing-library/react';
import 'jest-styled-components';

import { Button } from './index';

describe('<Button />', () => {
  it('renders component correctly', () => {
    const { container } = render(<Button label="button" />);

    const button = screen.getByText('button');
    expect(button).toBeInTheDocument();

    expect(container).toMatchSnapshot();
  });
});
```

We need to import the React library to test React project.

```js
import React from 'react';
```

We'll use `render` and `screen` in react-testing-library to test.

```js
import { render, screen } from '@testing-library/react';
```

We've used `styled-components` to design the component. So I added the library to test it.

```js
import 'jest-styled-components';
```

Next, import the Button component which we want to test, and prepare the test code with `describe` and `it` of Jest.

```js
import { Button } from './index';

describe('<Button />', () => {
  it('renders component correctly', () => {
    ...
  });
});
```

Fist, use `render` of react-testing-library to render the component to check the component is displayed well on the screen.

```js
const { container } = render(<Button label="button" />);
```

When we render the component with `render` of `react-testing-library` to test the component rendering, the `render` returns an object which helps us to test. In here, we'll do the snapshot test so with `container`.

We need to set `label` props to display Button component. And the Button component will be displayed with `label`, so we can find the Button component with `label` text, and check it on the screen.

```js
const button = screen.getByText('button');
expect(button).toBeInTheDocument();
```

For this, we use `screen.getByText` of react-testing-library to find the component via `label` text on the screen, and check it displayed on the screen with `toBeInTheDocument`.

Lastly, use `toMatchSnapshot` to save a snapshot.

```js
expect(container).toMatchSnapshot();
```

This snapshot will help us that some changes affect the screen or not.

And save the file, the test code will be run automatically, because we've executed the `npm run test` command above. And you can see the result below on the console.

```bash
 PASS  src/Components/Button/index.test.tsx
  <Button />
    ✓ renders component correctly (27 ms)

Test Suites: 1 passed, 1 total
Tests:       1 passed, 1 total
Snapshots:   1 passed, 1 total
Time:        2.46 s
```

{% include in-feed-ads.html %}

Next, let's test other props of Button component. Add the test code below to check `backgroundColor` props of Button component.

```js
it('renders component with backgroundColor', () => {
  render(<Button label="button" backgroundColor="#FF1744" />);

  const button = screen.getByText('button');
  expect(button).toHaveStyleRule('background-color', '#FF1744');
});
```

First, render the Button component with `backgroundColor`.

```js
render(<Button label="button" backgroundColor="#FF1744" />);
```

After it, find Button component by finding the `label`, and use `toHaveStyleRule` provided `jest-styled-components` to check the style exists.

```js
const button = screen.getByText('button');
expect(button).toHaveStyleRule('background-color', '#FF1744');
```

And save the file, the test code will be run automatically, because we've executed the `npm run test` command above. And you can see the result below on the console.

```bash
 PASS  src/Components/Button/index.test.tsx
  <Button />
    ✓ renders component correctly (33 ms)
    ✓ renders component with backgroundColor (6 ms)

Test Suites: 1 passed, 1 total
Tests:       2 passed, 2 total
Snapshots:   1 passed, 1 total
Time:        3.669 s
Ran all test suites.
```

{% include in-feed-ads.html %}

Lastly, Let's test the click event in Button component. Add the test code below to test the click event in Button component.

```js
import { render, screen, fireEvent } from '@testing-library/react';
...
it('clicks', () => {
  const onClick = jest.fn();
  render(<Button label="button" onClick={onClick} />);

  expect(onClick).toHaveBeenCalledTimes(0);
  const button = screen.getByText('button');
  fireEvent.click(button);
  expect(onClick).toHaveBeenCalledTimes(1);
});
```

When you test the user event, you need to import `fireEvent` from react-testing-library.

```js
import { render, screen, fireEvent } from '@testing-library/react';
```

And bind the `Mock Function` of Jest to the event function.

```js
const onClick = jest.fn();
render(<Button label="button" onClick={onClick} />);
```

If we bind `Mock Function` to the user event, we can know the user clicks the Button component by checking the function call counts. At a first time, the click event doesn't occurs, so the function call counts is `0`.

```js
expect(onClick).toHaveBeenCalledTimes(0);
```

Next, use `fireEvent` of react-testing-library to click the Button component, and check the function call count is increased.

```js
const button = screen.getByText('button');
fireEvent.click(button);
expect(onClick).toHaveBeenCalledTimes(1);
```

And save the file, the test code will be run automatically, because we've executed the `npm run test` command above. And you can see the result below on the console.

```bash
 PASS  src/Components/Button/index.test.tsx
  <Button />
    ✓ renders component correctly (27 ms)
    ✓ renders component with backgroundColor (4 ms)
    ✓ clicks (7 ms)

Test Suites: 1 passed, 1 total
Tests:       3 passed, 3 total
Snapshots:   1 passed, 1 total
Time:        3.634 s
Ran all test suites.
```

Done! we've written the test code for the Button component.

{% include in-feed-ads.html %}

### Test App component

Next, let's test the App component. The App component doesn't have any Props, but has the State to use dynamic data.

To test the App component, create `./src/App.test.tsx` file and modify it like below.

```js

import React from 'react';
import { render, screen } from '@testing-library/react';
import 'jest-styled-components';

import App from './App';

describe('<App />', () => {
  it('renders component correctly', () => {
    const { container } = render(<App />);

    const minusButton = screen.getByText('-');
    expect(minusButton).toBeInTheDocument();
    expect(minusButton).toHaveStyleRule('background-color', '#FF1744');
    const plusButton = screen.getByText('+');
    expect(plusButton).toBeInTheDocument();
    expect(plusButton).toHaveStyleRule('background-color', '#304FFE');
    const label = screen.getByText('0');
    expect(label).toBeInTheDocument();

    expect(container).toMatchSnapshot();
  });
});
```

I'll skip the details that I already explained in the Button component. First, I wrote the test code about the App component is displayed well like the Button component test code. App component has two buttons that have different `label` and `backgroundColor`, and has the Count label. The Count is initialized with `0`, so we can write the test code to check `0` is displayed on the screen.

```js
const minusButton = screen.getByText('-');
expect(minusButton).toBeInTheDocument();
expect(minusButton).toHaveStyleRule('background-color', '#FF1744');

const plusButton = screen.getByText('+');
expect(plusButton).toBeInTheDocument();
expect(plusButton).toHaveStyleRule('background-color', '#304FFE');

const label = screen.getByText('0');
expect(label).toBeInTheDocument();
```

And save the file, the test code will be run automatically, because we've executed the `npm run test` command above. And you can see the result below on the console.

```bash
 PASS  src/App.test.tsx
  <App />
    ✓ renders component correctly (34 ms)

 › 1 snapshot written.
Snapshot Summary
 › 1 snapshot written from 1 test suite.

Test Suites: 1 passed, 1 total
Tests:       1 passed, 1 total
Snapshots:   1 written, 1 total
Time:        3.316 s
```

Next, let's click the minus button to change the value on the screen via State. To test the minus button, add the test code like below.

```js
import { render, screen, fireEvent } from '@testing-library/react';
...
it('clicks minus button', () => {
  render(<App />);

  const minusButton = screen.getByText('-');
  const label = screen.getByText('0');
  expect(label).toBeInTheDocument();

  fireEvent.click(minusButton);
  expect(label.textContent).toBe("-1");
  fireEvent.click(minusButton);
  expect(label.textContent).toBe("-2");
});
```

use `fireEvent` to click the button, and check the value is changed well.

And save the file, the test code will be run automatically, because we've executed the `npm run test` command above. And you can see the result below on the console.

```bash
 PASS  src/App.test.tsx
  <App />
    ✓ renders component correctly (43 ms)
    ✓ clicks minus button (17 ms)

Test Suites: 1 passed, 1 total
Tests:       2 passed, 2 total
Snapshots:   1 passed, 1 total
Time:        3.82 s
```

{% include in-feed-ads.html %}

Next, let's test the plus button like the minus button test. Add the test code below to test the plus button.

```js
it('clicks plus button', () => {
  render(<App />);

  const plusButton = screen.getByText('+');
  const label = screen.getByText('0');
  expect(label).toBeInTheDocument();

  fireEvent.click(plusButton);
  expect(label.textContent).toBe("1");
  fireEvent.click(plusButton);
  expect(label.textContent).toBe("2");
});
```

The test code is same as the minus button test. Click the plus button and check the value is changed well.

And save the file, the test code will be run automatically, because we've executed the `npm run test` command above. And you can see the result below on the console.

```bash
 PASS  src/App.test.tsx
  <App />
    ✓ renders component correctly (36 ms)
    ✓ clicks minus button (14 ms)
    ✓ clicks plus button (8 ms)

Test Suites: 1 passed, 1 total
Tests:       3 passed, 3 total
Snapshots:   1 passed, 1 total
Time:        3.705 s
```

Done! we've written all test code for the Counter App. Also, we check the test code is working well.

## Code coverage

Cancel the current command and execute the command below to see the code coverage.

```bash
npm run test -- --coverage
```

After it, you can see that there are all test code for all source code like below.

```bash
 PASS  src/Components/Button/index.test.tsx
 PASS  src/App.test.tsx
----------|---------|----------|---------|---------|-------------------
File      | % Stmts | % Branch | % Funcs | % Lines | Uncovered Line #s
----------|---------|----------|---------|---------|-------------------
All files |     100 |      100 |     100 |     100 |
 App.tsx  |     100 |      100 |     100 |     100 |
----------|---------|----------|---------|---------|-------------------

Test Suites: 2 passed, 2 total
Tests:       6 passed, 6 total
Snapshots:   2 passed, 2 total
Time:        2.752 s, estimated 3 s
```

## Completed

We've seen how to use Jest and react-testing-library to test the React project created by create-react-app. The test code in here is not a perfect solution, and there are many way to write the test code to do same test case.

Also, we've seen the code coverage that shows our test code covers all source code. However, the code coverage is just for checking. You shouldn't trust it 100%. Even if the code coverage says 100%, it doesn't mean your app doesn't have bugs, and your test code covers all test case, so just use the code coverage as one indicator.
