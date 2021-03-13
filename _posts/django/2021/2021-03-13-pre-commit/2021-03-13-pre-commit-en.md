---
layout: 'post'
permalink: '/django/pre-commit/'
paginate_path: '/django/:num/pre-commit/'
lang: 'en'
categories: 'django'
comments: true

title: '[Django] how to use pre-commit'
description: Let's see how to use pre-commit to execute the flake8 when you commit to Git.
image: '/assets/images/category/django/2021/pre-commit/background.jpg'
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [pre-commit installation](#pre-commit-installation)
- [pre-commit configuration](#pre-commit-configuration)
- [flake8 configuration](#flake8-configuration)
- [Execute pre-commit](#execute-pre-commit)
- [Completed](#completed)

</div>

## Outline

On the previous blog post, I've introduced how to configure the static code analysis `flake8` to make the same code style and reduce the potential bugs.

- [[Django] how to use flake8]({{site.url}}/{{page.categories}}/flake8/){:target="_blank"}

In this blog post, I will show you how to use `pre-commit` to execute the flake8 when you commit the source code to Git.

- pre-commit: [https://pre-commit.com/](https://pre-commit.com/){:rel="nofollow noreferrer" target="_blank"}

## pre-commit installation

To execute the flake8 automatically by pre-commit, we need to install the pre-commit. Execute the command below to install the pre-commit.

```bash
pip install pre-commit
```

After installing, don't forget to store it to `requirements.txt`.

```bash
pip freeze > requirements.txt
```

Done! we've seen how to install the pre-commit.

## pre-commit configuration

To use the pre-commit to execute the flake8 automatically, we need to create the configuratoin file of the pre-commit. Execute the command below to create a configuration file of the pre-commit.

```bash
pre-commit sample-config > .pre-commit-config.yaml
```

When you open the created `.pre-commit-config.yaml` file, you can see the contents like below.

```yml
# See https://pre-commit.com for more information
# See https://pre-commit.com/hooks.html for more hooks
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v3.2.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
```

We can see the sample of the configuration file provided by the pre-commit.

{% include in-feed-ads.html %}

## flake8 configuration

The pre-commit configuration file `.pre-commit-config.yaml` has the structure below basically.

```yml
repos:
  - repo: repo-url
    rev: version
    hooks:
      - id: hook-id
```

- repo: Repository URL from the pre-commit
- rev: Version of the feature
- id: Feature from pre-commit

The pre-commit provides some features. You can see them on the link below.

- hooks: [https://pre-commit.com/hooks.html](https://pre-commit.com/hooks.html){:rel="nofollow noreferrer" target="_blank"}

We'll use the flake8. Open the `.pre-commit-config.yaml` file and modify it like below.

```yml
repos:
  - repo: https://gitlab.com/pycqa/flake8
    rev: 3.8.4
    hooks:
      - id: flake8
```

I've configured the repo URL, version and flake8 hook of the pre-commit. You can see the configuration on the flake8 official documentation.

- flake8 hooks: [https://flake8.pycqa.org/en/latest/user/using-hooks.html](https://flake8.pycqa.org/en/latest/user/using-hooks.html){:rel="nofollow noreferrer" target="_blank"}

To apply the configurations to Git Commit hook, execute the command below.

```bash
pre-commit install
```

Done! we've ready to use the pre-commit to use the flake8

## Execute pre-commit

Let's check the configuration we've set is working well. Execute the command below, that is executed based on `.pre-commit-config.yaml` file, to start the pre-commit.

```bash
pre-commit run --all-files
```

You can see the result when you execute the command.

```bash
flake8...................................................................Passed
```

We've checked the pre-commit, that we've configured, is working well. Commit the configurations to Git.

```bash
git add .
git commit -m 'Add pre-commit for flake8'
git push origin main
```

## Completed

We've seen how to configure the pre-commit to execute the flake8 when we commit to Git. Note that if you clone the repository, don't forget to execute `pre-commit install` to register the pre-commit configuration to Git hooks.

```bash
git clone repository_url
# virtualenv venv
# source venv/bin/activate
pip install -r requirement.txt
pre-commit install
```

So let's do more productive development with automated flake8!
