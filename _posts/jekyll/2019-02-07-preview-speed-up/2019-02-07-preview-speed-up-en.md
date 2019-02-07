---
layout: 'post'
permalink: '/jekyll/preview-speed-up/'
paginate_path: '/jekyll/:num/preview-speed-up/'
lang: 'en'
categories: 'jekyll'
comments: true

title: 'Preview'
description: let's see how to make fast to preview writing post in jekyll.
image: '/assets/images/category/jekyll/preview-speed-up.jpg'
---

## Problem
I use Jekyll to manage this blog. as blog posts became many, it have taken a long time to check new blog post in local. I use Jekyll command below to check the blog post before publishing to the server.

```bash
bundle exec jekyll serve
```

however, as I use many Jekyll plugins and have many posts, it have taken ```209.498985 seconds``` to check new blog post. I think it's ok to publish new blog post, but it's waste to take 200 seconds to just check new blog post.

## Solution
there are many solution, I guess. I use Jekyll settings below to make the build speed up.

first, copied ```_config.yml``` to ```_config-dev.yml``` and add codes below to it.

```yml
# I use Multi-language plugin so I set 3, but normally set 1.
limit_posts: 3
```

and then, I execute Jekyll command below to check a new blog post.

```bash
bundle exec jekyll serve --config _cong-dev.yml
```

this code can make only one blog post is built. after this configuration, I was waiting ```74.639 seconds``` to check a new blog post. and ```minify``` plugin which is one of Jekyll plugins what I use takes a long time, so I set not to minify.

```yml
jekyll-minifier:
  remove_spaces_inside_tags: false
  remove_multi_spaces: false
  remove_comments: false
  compress_css: false
  compress_javascript: false
  compress_json: false
```

after it, the build takes ```50.668 seconds```. it's 20 seconds faster than before.

## Compoleted
the settings I mentioned above reduced 200 sec to 50 sec (1/4). however I think it takes a long time and it's big issue in Jekyll blog.