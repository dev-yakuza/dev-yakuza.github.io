---
layout: 'post'
permalink: '/ruby-on-rails/folder-structure/'
paginate_path: '/ruby-on-rails/:num/folder-structure/'
lang: 'en'
categories: 'ruby-on-rails'
comments: true

title: Folder structure in Ruby on Rails
description: Let's see the folder structure in the project which is created by Ruby on Rails.
image: '/assets/images/category/ruby-on-rails/2020/folder-structure/background.jpg'
---

<div id="contents_list" markdown="1">

## Content

- [Outline](#outline)
- [Project structure](#project-structure)
- [Controller related](#controller-related)
- [View related](#view-related)
- [URL related](#url-related)
- [Completed](#completed)
- [Reference](#reference)

</div>

## Outline

In this blog post, I'll introduce the folder structure of the Rails project.

This blog post is a series. You can see the other posts in below.

- [Start Ruby on Rails on Mac]({{site.url}}/{{page.categories}}/folder-structure/){:target="_blank"}
- Folder structure in Ruby on Rails
- [Add new web page by Ruby on Rails]({{site.url}}/{{page.categories}}/create-page/){:target="_blank"}
- [Exchange Data between Controller, View and Route]({{site.url}}/{{page.categories}}/data-in-controller-view-route/){:target="_blank"}
- [Use DB on Rails]({{site.url}}/{{page.categories}}/database/){:target="_blank"}

Also, you can see the this blog post sample source code on Github

- [Github source code](https://github.com/dev-yakuza/study-rails){:rel="nofollow noreferrer" target="_blank"}

## Project structure

After creating a new Rails project, you can see the project like below. Below is a summary of the important parts of the project.

```bash
├── Gemfile
├── Gemfile.lock
├── README.md
├── Rakefile
├── app
│   ├── controllers
│   │   ├── application_controller.rb
│   │   └── concerns
│   ├── models
│   │   ├── application_record.rb
│   │   └── concerns
│   └── views
│       └── layouts
│           ├── application.html.erb
│           ├── mailer.html.erb
│           └── mailer.text.erb
├── babel.config.js
├── bin
├── config
│   ├── locales
│   │   └── en.yml
│   ├── routes.rb
├── config.ru
├── db
│   ├── development.sqlite3
│   └── seeds.rb
├── lib
├── log
│   └── development.log
├── package.json
├── postcss.config.js
├── public
├── storage
├── temp
├── test
├── vendor
└── yarn.lock
```

{% include in-feed-ads.html %}

## Controller related

Ruby on Rails is following `MVC pattern`(Model-View-Controller pattern) like other language frameworks. So, we can make web services by creating Model, View, and Controller in Ruby on Rails.

You can see the folders after creating Controller in Ruby on Rails.

```bash
├── app
│   ├── assets
│   │   ├── stylesheets
│   │   │   ├── home.scss
│   ├── controllers
│   │   ├── home_controller.rb
│   ├── helpers
│   │   ├── home_helper.rb
├── test
│   ├── controllers
│   │   ├── home_controller_test.rb
```

In next blog post, I'll introduce how to create Controller via Rails command. After creating Controller via Rails command, you can see the folders and files like above. In here, above is the example of creating home_controller.

If you want to know how to create Controller, see the link below.

- [Add new web page by Ruby on Rails - Controller]({{site.url}}/{{page.categories}}/create-page/#controller){:target="_blank"}

## View related

You will create View file on the folder below. The View file is to display the screen in Ruby on Rails.

```bash
├── app
│   ├── views
│   │   ├── home
```

Here is the example after creating home_controller. You can not find home folder. If you create home_controller via Rails command, Rails automatically creates home foder for View files.

If you want to know how to create Controller and View, see the link below.

- [Add new web page by Ruby on Rails - View]({{site.url}}/{{page.categories}}/create-page/#view){:target="_blank"}

## URL related

Rails is a framework to make web services with Ruby language. So, Rails has URL management feature.

On Rails, routes.rb file in config folder manages URLs.

```bash
├── config
│   ├── routes.rb
```

If you want to know how to add a new URL, see the link below.

- [Add new web page by Ruby on Rails - Route]({{site.url}}/{{page.categories}}/create-page/#routes){:target="_blank"}

{% include in-feed-ads.html %}

## Database

Below is related to Database in Ruby on Rails.

```bash
├── app
│   ├── models
│   │   ├── post.rb
├── config
│   ├── database.yml
├── db
│   ├── migrate
│   │   ├── 20200313092804_create_posts.rb
├── test
│   ├── fixtures
│   │   ├── posts.yml
│   ├── models
│   │   ├── post_test.rb
```

- config/database.yml: Database connection info file.
- app/models/post.rb: Model file
- db/migrate/20200313092804_create_posts.rb: Migration file to create the table.
- test/fixtures/posts.yml: Dummy data file for testing.
- test/models/post_test.rb: Unit test file for Model

If you want to know how to configure Database, and how to use Data, see the link below.

- [How to handle Data in Rails]({{site.url}}/{{page.categories}}/data){:target="_blank"}

## Completed

We've seen the folder structure in Ruby on Rails. Next, I'll introduce how to make Controller, View and Model for the web service.

## Reference

This blog post is a series. You can see the other posts in below.

- [Start Ruby on Rails on Mac]({{site.url}}/{{page.categories}}/folder-structure/){:target="_blank"}
- Folder structure in Ruby on Rails
- [Add new web page by Ruby on Rails]({{site.url}}/{{page.categories}}/create-page/){:target="_blank"}
- [Exchange Data between Controller, View and Route]({{site.url}}/{{page.categories}}/data-in-controller-view-route/){:target="_blank"}
- [Use DB on Rails]({{site.url}}/{{page.categories}}/database/){:target="_blank"}

Also, you can see the this blog post sample source code on Github

- [Github source code](https://github.com/dev-yakuza/study-rails){:rel="nofollow noreferrer" target="_blank"}
