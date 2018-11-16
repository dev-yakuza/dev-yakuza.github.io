---
layout: 'post'
permalink: '/jekyll/pagination-plugin/'
paginate_path: '/jekyll/:num/pagination-plugin/'
lang: 'en'
categories: 'jekyll'
comments: true

title: 'pagination plugin'
description: how to use pagination plugin for jekyll project's pagination.
image: '/assets/images/category/jekyll/pagination.jpg'
---

## outline
jekyll basically provides pagination plugin but we use [jekyll-paginate-v2](https://github.com/sverrirs/jekyll-paginate-v2){:rel="nofollow noreferrer" target="_blank"}.
this blog introduces how to use jekyll-paginate-v2.

## plugin installation and configuration
install and configure jekyll-paginate-v2.

### plugin installation
install jekyll-paginate-v2 plugin with below code.

{% include_relative common/installation.md %}

### plugin configuration
write below contents to ```_config.yml``` file.

{% include_relative common/config_yml.md %}

- permalink: this is page default link. if this is not set, plugin is not working.
- pagination: these are plugin options. if you want more informations, see officail site.([jekyll-paginate-v2:options](https://github.com/sverrirs/jekyll-paginate-v2/blob/master/README-GENERATOR.md){:rel="nofollow noreferrer" target="_blank"})
- enabled: activate plugin.
- per_page: post count per page.
- sort_reverse: indicates whether to reverse sort. we set `` `true``` for newest.
- sort_field: plugin uses the field when sort. we use ```date``` field to show latest posts.
- title: the title of the page created by pagination. this option will set ```page.title``` variable.(ex> :title - page :num)
- trail: before/after pagination count of selected page.

## page configuration
configurations are for showing pagination. page which has pagination and page which will be called from pagination page need to be configured.

### pagination page
set below code to the page which has pagination.(ex> category pages)

{% include_relative common/page_setting.md %}

- enabled: activate pagination.
- category: posts in this category will be paginated.
- permalink: the url of pages created by pagination feature.(ex> /:num/)

### pages called from pagination
configure below option to the pages called from pagination.(ex> post page)

{% include_relative common/called_page_setting.md %}

- paginate_path: options for including page number in the url of the page called from pagination.

## reference
- official site: [jekyll-paginate-v2](https://github.com/sverrirs/jekyll-paginate-v2/blob/master/README-GENERATOR.md){:rel="nofollow noreferrer" target="_blank"}
- official site - options: [jekyll-paginate-v2:options](https://github.com/sverrirs/jekyll-paginate-v2/blob/master/README-GENERATOR.md){:rel="nofollow noreferrer" target="_blank"}