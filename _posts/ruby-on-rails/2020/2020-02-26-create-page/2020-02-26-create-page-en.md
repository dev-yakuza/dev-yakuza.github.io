---
layout: 'post'
permalink: '/ruby-on-rails/create-page/'
paginate_path: '/ruby-on-rails/:num/create-page/'
lang: 'en'
categories: 'ruby-on-rails'
comments: true

title: Add new web page by Ruby on Rails
description: Let's see how to make and add new web page via Ruby on Rails.
image: '/assets/images/category/ruby-on-rails/2020/create-page/background.jpg'
---

<div id="contents_list" markdown="1">

## Content

- [Outline](#outline)
- [Controller](#controller)
  - [Controller creating error](#controller-creating-error)
  - [Controller files](#controller-files)
  - [Add Action to Controller](#add-action-to-controller)
- [View](#view)
  - [Connect Controller and View](#connect-controller-and-view)
- [Routes](#routes)
- [Check it](#check-it)
- [Completed](#completed)
- [Reference](#reference)

</div>

## Outline

In this blog post, I will introduce how to make and add new web page in Ruby on Rails.

This blog post is a series. You can see the other posts in below.

- [Start Ruby on Rails on Mac]({{site.url}}/{{page.categories}}/folder-structure/){:target="_blank"}
- [Folder structure in Ruby on Rails]({{site.url}}/{{page.categories}}/folder-structure/){:target="_blank"}
- Add new web page by Ruby on Rails
- [Exchange Data between Controller, View and Route]({{site.url}}/{{page.categories}}/data-in-controller-view-route/){:target="_blank"}
- [Use DB on Rails]({{site.url}}/{{page.categories}}/database/){:target="_blank"}

Also, you can see the this blog post sample source code on Github

- [Github source code](https://github.com/dev-yakuza/study-rails){:rel="nofollow noreferrer" target="_blank"}

Ruby on Rails also has `MVC pattern`(Model-View-Controller pattern) like other language frameworks. So, if you want to make a new web page, you need to create `View` and `Controller`.

## Controller

First, execute the command below to create a Controller.

```bash
# cd StudyRails
bundle exec rails generate controller home
```

You can also use the `g` command instead of generate command like below.

```bash
bundle exec rails g controller home
```

### Controller creating error

If the command does not do anything, stop the executed command and execute the command below.

```bash
rake app:update:bin
```

And then, you can see the message like below, insert `Y` to move on.

```bash
/StudyRails/bin/rails? (enter "h" for help) [Ynaqdhm]
/StudyRails/bin/rake? (enter "h" for help) [Ynaqdhm]
```

And then, execute the command below to create a Controller.

```bash
# cd StudyRails
bundle exec rails generate controller home
```

Again, if you got the message like below and the Controller is not created,

```bash
error Couldn't find an integrity file
error Found 1 errors.


========================================
  Your Yarn packages are out of date!
  Please run `yarn install --check-files` to update.
========================================


To disable this check, please change `check_yarn_integrity`
to `false` in your webpacker config file (config/webpacker.yml).
```

Execute the command below that is in the message.

```bash
yarn install --check-files
```

And then, execute the command below again to create a Controller.

```bash
# cd StudyRails
bundle exec rails generate controller home
# bundle exec rails g controller home
```

If you don't have any problem, you can see the message like below.

```bash
create  app/controllers/home_controller.rb
invoke  erb
create    app/views/home
invoke  test_unit
create    test/controllers/home_controller_test.rb
invoke  helper
create    app/helpers/home_helper.rb
invoke    test_unit
invoke  assets
invoke    scss
create      app/assets/stylesheets/home.scss
```

{% include in-feed-ads.html %}

### Controller files

If you create a Controller via Rails command, you can see the files created like below.

```bash
├── app
│   ├── assets
│   │   ├── stylesheets
│   │   │   ├── home.scss
│   ├── controllers
│   │   ├── home_controller.rb
│   ├── helpers
│   │   ├── home_helper.rb
│   ├── views
│   │   ├── home
├── test
│   ├── controllers
│   │   ├── home_controller_test.rb
```

We'll use`app/controllers/home_controller.rb` in the created files to do almost things.

### Add Action to Controller

open `app/controllers/home_controller.rb` file and modify it like below.

```rb
class HomeController < ApplicationController
    def index
    end
end
```

In here, we add index function to home_controller. In Rails, the function added in the Controller is called Action.

## View

You can see the folder like below if you created the Controller via Rails command.

```bash
├── app
│   ├── views
│   │   ├── home
```

We'll make View file for home_controller.rb in home folder and connect it to the Controller Action.

Create `index.erb` file in home folder and modify it like below.

```rb
Hello Rails!!
```

### Connect Controller and View

We don't need to do anything to connect the Controller and View. If the Controller Action name(Function name - `def index`) and View file name(`index.erb`) is same, Rails automatically connects both.

{% include in-feed-ads.html %}

## Routes

The `Routes` do the role to connect URL and the Controller in Rails. open `config/routes.rb` file and modify it like below to connect the URL and Controller.

```rb
Rails.application.routes.draw do
  get '/', to: 'home#index'
end
```

If Rails receives `GET` request on `/` URL, Rails executes `index` action in `home_controller`. Also, Rails try to find the same name file of index action, and responses `home/index.erb` to display it.

## Check it

We've done to display the new web page. Execute the command below to start Rails server.

```bash
rails server
```

Or, you can execute the simple command like below.

```bash
rails s
```

And the open the browser and go to `http://127.0.0.1:3000/`, you can see the screen like below that we've created above.

![result of executing Ruby on Rails](/assets/images/category/ruby-on-rails/2020/create-page/rails-server.jpg)

## Completed

We've seen how to create a new web page in Ruby on Rails.

we've created a Controller and defined an Action(function) and created a View file same name of the Action(function), and lastly, connected URL and the Controller for displaying the new web page.

Now, we can make web pages! Next, let's see how to use Data in Rails!

## Reference

This blog post is a series. You can see the other posts in below.

- [Start Ruby on Rails on Mac]({{site.url}}/{{page.categories}}/folder-structure/){:target="_blank"}
- [Folder structure in Ruby on Rails]({{site.url}}/{{page.categories}}/folder-structure/){:target="_blank"}
- Add new web page by Ruby on Rails
- [Exchange Data between Controller, View and Route]({{site.url}}/{{page.categories}}/data-in-controller-view-route/){:target="_blank"}
- [Use DB on Rails]({{site.url}}/{{page.categories}}/database/){:target="_blank"}

Also, you can see the this blog post sample source code on Github

- [Github source code](https://github.com/dev-yakuza/study-rails){:rel="nofollow noreferrer" target="_blank"}
