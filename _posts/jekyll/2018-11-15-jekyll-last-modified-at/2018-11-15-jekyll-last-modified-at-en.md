---
layout: 'post'
permalink: '/jekyll/jekyll-last-modified-at/'
paginate_path: '/jekyll/:num/jekyll-last-modified-at/'
lang: 'en'
categories: 'jekyll'
comments: true

title: 'jekyll-last-modified-at'
description: 'use last modified date of the file to generate sitemap.xml'
image: '/assets/images/category/jekyll/jekyll-last-modified-at.jpg'
---

## outline
in our blog, we use

```<lastmod>{% raw %}{{ site.time | date: '%Y-%m-%d' }}{% endraw %}</lastmod>```

this code for sitemap.xml. this means last modified date of all pages is last build date of jekyll. so we were wondering google crawler is too busy to crawl actually modified page because of actually not modified page. therefore, we decided to use ```jekyll-last-modified-at``` plugin to generate the actually modified date to sitemap.xml

## plugin
you can see all details about ```jekyll-last-modified-at``` to click below link. we will introduce how to install and use ```jekyll-last-modified-at```.

- jekyll-last-modified-at: [https://github.com/gjtorikian/jekyll-last-modified-at](https://github.com/gjtorikian/jekyll-last-modified-at){:rel="nofollow noreferrer" :target="_blank"}

## install plugin
execute below command to install ```jekyll-last-modified-at``` plugin.

```bash
gem install jekyll-last-modified-at
```

## how to use
insert one of below codes you want to show the date.

```html
{% raw %}
{% last_modified_at %}

{% last_modified_at %Y:%B:%A:%d:%S:%R %}

{{ page.last_modified_at }}

{{ page.last_modified_at | date: '%Y:%B:%A:%d:%S:%R' }}
{% endraw %}
```

we changed the code in ```sitemap.xml`` like below.

```xml
<!-- <lastmod>{% raw %}{{ site.time | date: '%Y-%m-%d' }}{% endraw %}</lastmod> -->
<lastmod>{% raw %}{{ post.last_modified_at | date: '%Y-%m-%d' }}{% endraw %}</lastmod>
```

## check
we checked the code is changed to the modified file date.

```bash
bundle exec jekyll build
```

we don't know actually this affects to google crawler, but we satisfy it because of done it like a programmer.