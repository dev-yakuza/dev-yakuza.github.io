---
layout: 'post'
permalink: '/jekyll/search-bar/'
paginate_path: '/jekyll/:num/search-bar/'
lang: 'en'
categories: 'jekyll'
comments: true

title: Display SearchBar on Jekyll
description: Let's see how to show SearchBar on Jekyll without specific plugins.
image: '/assets/images/category/jekyll/2020/search-bar/background.jpg'
---

<div id="contents_list" markdown="1">

## Contents

- [Outline](#outline)
- [Prepare data](#prepare-data)
  - [Data layout](#data-layout)
- [Make data](#make-data)
- [Create SearchBar](#create-searchbar)
  - [Create HTML](#create-html)
  - [Create SCSS/CSS](#create-scsscss)
  - [Create Javascript](#create-javascript)
  - [Display SearchBar](#display-searchbar)
- [Complete](#complete)

</div>

## Outline

I use Jekyll and GitHub for this blog. The purpos to write blog posts is not only to share the information, but also tor write what I often forget, and find it whenever I need.

However, as the blog posts are many, when I need it, I couldn't search the blog post fastly. So, recently, I added SearchBar on Jekyll blog!

![Display SearchBar on Jekyll blog - search bar](/assets/images/category/jekyll/2020/search-bar/search-bar.jpg)

In this blog post, I will show you how to make SearchBar on Jekyll blog without any plugins

## Prepare data

To show search results, we need the data for searching. Let's see how to make the data.

### Data layout

I use Jekyll Liquid to make JSON data for the search data.

We need to make a layout to create the data. To make a data layout, create `_layouts/posts.json` file and modify it like below.

```json
{% raw %}
[
  {% if page.target == "home" %}
    {%- assign posts = site.posts -%}
  {% else %}
    {%- assign posts = site.posts | where_exp:"item", "item.categories contains page.target" -%}
  {% endif %}
  {%- for subPost in posts -%}
  {
      "title": "{{ subPost.title | xml_escape }}",
      "description": "{{ subPost.description | xml_escape }}",
      "url": "{{ site.url }}/{{subPost.lang}}{{ subPost.url }}",
      "date": "{{ subPost.last_modified_at | date_to_xmlschema }}",
      "category": "{{ subPost.categories }}"
  }
  {%- unless forloop.last -%},{%- endunless -%}
  {%- endfor -%}
]
{% endraw %}
```

The source code above is that I use on my blog. Modify it for your environment.

Let's see the detail of the source code.

```json
{% raw %}
{% if page.target == "home" %}
  {%- assign posts = site.posts -%}
{% else %}
  {%- assign posts = site.posts | where_exp:"item", "item.categories contains page.target" -%}
{% endif %}
{% endraw %}
```

The source code above is to get the blog posts for the data. If `page.target` is `home`, the data will be all blog posts. If it is not, the data will be the blog posts which categories(`item.categories`) include `page.target`. In here, `page.target` is not Jekyll variable. It is just a custom variable for the JSON data.

```json
{% raw %}
{%- for subPost in posts -%}
{
    "title": "{{ subPost.title | xml_escape }}",
    "description": "{{ subPost.description | xml_escape }}",
    "url": "{{ site.url }}/{{subPost.lang}}{{ subPost.url }}",
    "date": "{{ subPost.last_modified_at | date_to_xmlschema }}",
    "category": "{{ subPost.categories }}"
}
{%- unless forloop.last -%},{%- endunless -%}
{%- endfor -%}
{% endraw %}
```

And then, loop this data to make JSON data.

{% include in-feed-ads.html %}

## Make data

Let's make real data by using the layout above.If you use Jekyll blog normally, you have the blog posts under `_posts` folder like below.

```bash
|- _posts
  |- react-native
    |- 2020-01-01-new-blog.md
    |- 2020-01-02-new-blog.md
    |- 2020-01-03-new-blog.md
```

In here, create a file, named what you recognize easily, for JSON data. (ex> `posts.md`, `api.md`...)

```bash
|- _posts
  |- react-native
    |- posts.md
    |- 2020-01-01-new-blog.md
    |- 2020-01-02-new-blog.md
    |- 2020-01-03-new-blog.md
```

And then, open the file and modify it like below.

```md
---
layout: 'posts'
permalink: '/api/react-native/posts.json'
target: 'react-native'
---
```

To use the layout created above, I configured `layout: 'posts'`, and set `permalink` to make a specific URL that the data will be deployed.

Lastly, I set `target` variable that is most important. In this example, I set `react-native`. As thinking about the layout above, if the blog posts, that have `categories` include `target`, will be the JSON data. That means the blog posts, that have `react-native` category, will be the JSON data.

If you want to make the JSON data includes all blog post, set `home` on this `target`. This is also not Jekyll rule, so you can use any name. (ex> `all`) Of course, when you use other names, you should change `if` statement in `_layouts/posts.json` file.

## Create SearchBar

From here, it is simply design coding. We will create the searchbar with HTML and CSS, use jQuery to get the JSON data.

### Create HTML

Open `_includes/search_bar.html` file and modify it like below to display the searchbar. This is a simple design, so just refer to it. I recommend you to make own yours.

```html
<div class="container">
  <div class="row">
    <div class="col-12">
      <div id="search-bar">
        <i class="fa fa-search" aria-hidden="true"></i>
        <input id="search" type="text" placeholder="Search..." />
        <div id="search-result"></div>
      </div>
    </div>
  </div>
</div>
```

{% include in-feed-ads.html %}

### Create SCSS/CSS

Each Jekyll theme has `SCSS` or `CSS` file for the design. In my case, there is `_sass/styles.scss` file. just open the design file and modify it like below.

```css
#search-bar {
  margin: 32px auto;
  border: 1px solid #ccc;
  border-radius: 20px;
  padding: 0 20px;

  & #search {
    width: calc(100% - 30px);
    border: none;
    line-height: 44px;
    outline: none;
    border-style: none;
  }
  & #search-result {
    display: none;
    position: absolute;
    top: 80px;
    width: calc(100% - 70px);
    max-height: 325px;
    overflow-y: auto;
    background-color: white;
    box-shadow: 0px 4px 8px 0 #ccc;
    z-index: 99999;
    & .result-item {
      display: block;
      padding: 8px 16px;
      text-decoration: none;
      & .title,
      .description {
        width: 100%;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
      }
      & .title {
        color: #f74094;
        padding-bottom: 4px;
        font-size: 16px;
      }
      & .description {
        color: #757575;
        font-size: 16px;
      }
    }
  }
}
```

In my theme use SCSS, so I've written `SCSS`. If your theme has CSS, modify this to CSS.

### Create Javascript

Next, let's make Javascript to load the JSON data. The theme, which I use, uses `jQuery` basically, so I introduce jQuery code in here

```js
$(function () {
  var posts = [];
  $.get(lang + '/api/{{ page.categories }}/posts.json', function (data) {
    posts = data;
  });
  $('#search').on('keyup', function () {
    var keyword = this.value.toLowerCase();
    var searchResult = [];

    if (keyword.length > 0) {
      $('#search-result').show();
    } else {
      $('#search-result').hide();
    }
    $('.result-item').remove();

    for (var i = 0; i < posts.length; i++) {
      var post = posts[i];
      if (
        post.title.toLowerCase().indexOf(keyword) >= 0 ||
        post.description.toLowerCase().indexOf(keyword) >= 0
      ) {
        searchResult.push(post);
      }
    }
    if (searchResult.length === 0) {
      $('#search-result').append(
        '<div class="result-item"><div class="description">There is no search result.</div></div>'
      );
    } else {
      for (var i = 0; i < searchResult.length; i++) {
        $('#search-result').append(
          '<a class="result-item" href="' +
            searchResult[i].url +
            '"><div class="title">【' + searchResult[i].category + '】' +
            searchResult[i].title +
            '</div><div class="description">' +
            searchResult[i].description +
            '</div></a>'
        );
      }
    }
  });
});
```

Let's see the details of the code.

```js
var posts = [];
$.get('/api/{{ page.categories }}/posts.json', function (data) {
  posts = data;
});
```

Define `posts` variable and get the JSON data via `ajax`, assigned it on `posts` variable. Modify `ajax` URL to your situation. In my case, I use only one category for one blog post, so I made the URL like above.

```js
$('#search').on('keyup', function () {
  var keyword = this.value.toLowerCase();
  var searchResult = [];

  if (keyword.length > 0) {
    $('#search-result').show();
  } else {
    $('#search-result').hide();
  }
  $('.result-item').remove();
  ...
});
```

When the users insert the search keywords, make it to lower case, and make HTML of the result to show.

```js
$('#search').on('keyup', function () {
  ...
  for (var i = 0; i < posts.length; i++) {
    var post = posts[i];
    if (
      post.title.toLowerCase().indexOf(keyword) >= 0 ||
      post.description.toLowerCase().indexOf(keyword) >= 0
    ) {
      searchResult.push(post);
    }
  }
  ...
});
```

After then, loop the data and search the data which title or description matched.

```js
$('#search').on('keyup', function () {
 ...
  if (searchResult.length === 0) {
    ...
  } else {
    ...
  }
});
```

Lastly, If there are no results, show `there is no search result`, if there are results, loop them to make list, and display them.

{% include in-feed-ads.html %}

### Display SearchBar

You can use the source code below to display the search bar on where you want to show it.

```rb
{% raw %}
{% include search_bar.html %}
{% endraw %}
```

## Complete

I've introduced my source code, so the blog post became a little bit longer. In this blog post, most important is to make JSON data. Others are to create own your beautiful design of the search bar, and make simple Javascript code to get and search the JSON data.

Let's make own your beautiful search bar for your Jekyll blog!
