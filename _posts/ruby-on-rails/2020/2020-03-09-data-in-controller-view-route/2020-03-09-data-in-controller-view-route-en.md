---
layout: 'post'
permalink: '/ruby-on-rails/data-in-controller-view-route/'
paginate_path: '/ruby-on-rails/:num/data-in-controller-view-route/'
lang: 'en'
categories: 'ruby-on-rails'
comments: true

title: 'Exchange Data between Controller, View and Route'
description: Let's see how to exchange Data between Controller, View and Route in Ruby on Rails.
image: '/assets/images/category/ruby-on-rails/2020/data-in-controller-view-route/background.jpg'
---

<div id="contents_list" markdown="1">

## Content

- [Outline](#outline)
- [Variable](#variable)
- [Send Data from Controller to View](#send-data-from-controller-to-view)
- [Sned Data from View to Controller](#sned-data-from-view-to-controller)
  - [GET request](#get-request)
  - [POST request](#post-request)
- [Complete](#complete)
- [Reference](#reference)

</div>

## Outline

In this blog post, I will show how to exchange Data between Controller and View, and how to use Route for that.

This blog post is a series. You can see the other posts in below.

- [Start Ruby on Rails on Mac]({{site.url}}/{{page.categories}}/folder-structure/){:target="_blank"}
- [Folder structure in Ruby on Rails]({{site.url}}/{{page.categories}}/folder-structure/){:target="_blank"}
- [Add new web page by Ruby on Rails]({{site.url}}/{{page.categories}}/create-page/){:target="_blank"}
- Exchange Data between Controller, View and Route
- [Use DB on Rails]({{site.url}}/{{page.categories}}/database/){:target="_blank"}

Also, you can see the this blog post sample source code on Github

- [Github source code](https://github.com/dev-yakuza/study-rails){:rel="nofollow noreferrer" target="_blank"}

## Variable

Before seeing Data exchanging, let's see Variable types in Ruby. In Ruby, you can use Variable types like below.

| Name | Description | Assignment |
|---|
| Local Variable | - Variable exists in specific action(area)<br/>As this variable is used only within a specific action, you can not use it out of the action. | var = 1 |
| Instance Variable | - You can only use this variable in an object.<br/>- Variable area is in the object pointed `self`. | @var = 1 |
| Class Variable | - Variable is shared in all objects of the class.<br/>- You can access it i via Class method.<br/>- This variable is defined as betwenn Class definition and Class method definition. | @@var = 1 |
| Global Variable | - You can use this variable in everywhere the program. | $var = 1 |

{% include in-feed-ads.html %}

## Send Data from Controller to View

The reason that I introduced Variable above is that we use Instance Variable to send Data from Controller to View. Let's see how to send Data from Controller to View. Open `app/controllers/home_controller.rb` file and modify it like below.

```rb
class HomeController < ApplicationController
    def index
        @name = 'dev-yakuza'
    end
end
```

And then, we need to modify the View file of the Action. Open `app/views/home/index.erb` file and modify it like below.

```rb
Hello <%= @name %>!!
```

And, execute the command below to start Rails server.

```bash
bundle exec rails s
# bundle exec rails server
```

After it, open `http://127.0.0.1:3000/` on the browser. You can see the Instance Variable works fine like below.

![Ruby on Rails result of server starting - Exchange Data between Controller and View](/assets/images/category/ruby-on-rails/2020/data-in-controller-view-route/result-data-controller-view.jpg)

We use Instance Variable to send Data from Controller to View like above.

## Sned Data from View to Controller

It is easy to send Data from Controller to View by using the Instance Variable. Because when Rails gets the Request via URL, the Controller works first and shows View with Data.

Sending Data from View to Controller means that User sends Data via View. View is already displayed on the user browser, so Sending Data from View to Controller is only that the user inserts Data.

To send Data from View to Controller, it's the same as sending Data in a web service, so we can use GET / POST Request to send it.

### GET request

Let's modify View file for GET request. Open `app/views/home/index.erb` file and modify it like below.

```rb
Hello <%= @name %>!!<br/>
<a href="/?name=yakuza">Display yakuza</a>
```

And then, modify Controller to get the GET parameters. Open `app/controllers/home_controller.rb` file and modify it like below.

```rb
class HomeController < ApplicationController
    def index
        name = params[:name]
        @name = name ? name : 'dev-yakuza'
    end
end
```

It is the GET method, so we've passed Data using the URL with &#60;a&#62; tag(`name=yakuza`).

{% include in-feed-ads.html %}

### POST request

Let's make POST request to send Data. Open `app/views/home/index.erb` file and modify it like below.

```rb
Hello <%= @name %>!!<br/>
<a href="/?name=yakuza">Display yakuza</a><br/>
<form action="/" method="POST">
  <label for="name">name:</label>
  <input type="text" name="name" />
  <input type="submit" />
</form>
```

And when you open the browser, you can see the screen like below.

![POST request - before inserting the data](/assets/images/category/ruby-on-rails/2020/data-in-controller-view-route/before-send-data.jpg)

And then, when you insert Data and click `Submit` button, you can get the error like below.

![POST request - sending data error screen](/assets/images/category/ruby-on-rails/2020/data-in-controller-view-route/send-data-error.jpg)

As you can see the error message(`Routing Error`), we got this error message becuase, we didn't set Route configuration.

First, check ourRoute file, open `config/routes.rb` file.

```rb
Rails.application.routes.draw do
  get '/', to: 'home#index'
end
```

As you see above, we configured that Rails can get `get` request on `/` URL, so when Rails get POST request, `Routing Error` is occurred.

Let's set to get POST request. Open `config/routes.rb` and modify it like below.

```rb
Rails.application.routes.draw do
  get '/', to: 'home#index'
  post '/', to: 'home#index'
end
```

And then, to click `submit` button again, you can see the error message like below.

![POST request - send data error screen, authenticity token](/assets/images/category/ruby-on-rails/2020/data-in-controller-view-route/send-data-error-authenticity-token.jpg)

Like other language frameworks, Rails also protects the service from Security vulnerability basically. In here, to protect from `CSRF - Cross-site request forgery`, Rails requires specific Key when the data is sent via POST.

To solve this error, when you send Data via POST, you should set `form_authenticity_token` to `authenticity_token` parameter for Rails.

Open `app/views/home/index.erb` file again and modify it like below.

```rb
Hello <%= @name %>!!<br/>
<a href="/?name=yakuza">Display yakuza</a><br/>
<form action="/" method="POST">
  <input type="hidden" name="authenticity_token" value="<%= form_authenticity_token %>" />
  <label for="name">name:</label>
  <input type="text" name="name" />
  <input type="submit" />
</form>
```

And open `http://127.0.0.1:3000/` on the browser. Insert Data and click Submit button, you can send Data well and see the screen like below.

![POST request - success to send data](/assets/images/category/ruby-on-rails/2020/data-in-controller-view-route/result-post-data.jpg)

## Complete

We've seen how to exchange Data between Controller and View.

To send Data from Controller to View, we've used Instance variable. To send Data from View to Controller, we've used GET/POST method.
And we've seen how to make POST URL on Route.

In next blog post, I will introduce how to save Data in Database, and show it to View.

## Reference

This blog post is a series. You can see the other posts in below.

- [Start Ruby on Rails on Mac]({{site.url}}/{{page.categories}}/folder-structure/){:target="_blank"}
- [Folder structure in Ruby on Rails]({{site.url}}/{{page.categories}}/folder-structure/){:target="_blank"}
- [Add new web page by Ruby on Rails]({{site.url}}/{{page.categories}}/create-page/){:target="_blank"}
- Exchange Data between Controller, View and Route
- [Use DB on Rails]({{site.url}}/{{page.categories}}/database/){:target="_blank"}

Also, you can see the this blog post sample source code on Github

- [Github source code](https://github.com/dev-yakuza/study-rails){:rel="nofollow noreferrer" target="_blank"}
