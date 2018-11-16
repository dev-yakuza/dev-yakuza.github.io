---
layout: 'post'
permalink: '/jekyll/multi-languages-plugin/'
paginate_path: '/jekyll/:num/multi-languages-plugin/'
lang: 'en'
categories: 'jekyll'
comments: true

title: 'Multi-languages plugin'
description: introduce multi-languages plugin to make jekyll supports multi-languages. let's see how to install and configure multi-languages plugin jekyll-polyglot.
image: '/assets/images/category/jekyll/multi-languages-plugin.jpg'
---


## Multi-languages plugin
Let's see how to install and configure multi-languages plugin to make jekyll support multi-languages. There are many plugins for multi-languages but we introduce [jekyll-polyglot](https://github.com/untra/polyglot){:rel="nofollow noreferrer" target="_blank"} at here.

If you wanna know other multi-languages plugin, see [awesome-jekyll-plugins](https://github.com/planetjekyll/awesome-jekyll-plugins#multi-language--multi-lingual){:rel="nofollow noreferrer" target="_blank"}.

## Install the plugin
- execute below command on console for installing the plugin.

{% include_relative common/install_plugin.md %}

- configure below options on ```_config.yml``` file.

{% include_relative common/set_plugin.md %}

## Plugin global settings
configure below options on ```_config.yml``` file.

{% include jekyll/configuration_multi_languages.md %}

- languages: these are multi-languages list which support on the site.
- default_lang: Default languages in supported multi-languages.
- exclude_from_localization: excluded folder list which you don't want to localize.
- parallel_localization: when this is set true, jekyll will compile parallely using fork(). Windows OS doesn't support fork() so must set false.

## Page settings

- Try to make below folder structure under the ```_posts``` folder.

{% include_relative common/folder_structure.md %}

- 2018-09-19-multi-languages-plugin: make the folder which is set same post name under the ```_posts``` folder for managment.
- common: save common files which multi-languages file use. For example, the directory structure which you see now on, write to ```folder_structure.md``` and use ```{% raw %}{% include_relative common/folder_structure.md %}{% endraw %}``` on multi-languages files for displaying it.
- 2018-09-19-multi-languages-plugin-[language].md: make each multi-languages pages per ```languages``` configurations in ```_config.yml```.
- set specific page language at the top of each language pages.

```yml
---
layout: 'post'
lang: 'en'
...
---
```

## Check it out
We finished to set every configurations. Let's check each page languages.

- You can access pages created by plugins via below URL.

{% include_relative common/page_link.md %}

- The page which is set ```default_lang``` in ```_config.yml``` file can be acceessed directly by ```http://site_url/path```.
- The other pages except ```default_lang``` can be accessed by ```http://site_url/[언어]/path```.
- You can see multi-languages folders in ```_site``` folder after executing jekyll test server or building the site.
    - Execute jekyll test server: {% include jekyll/test_server_command.md %}
    - Build jekyll site: {% include jekyll/build_command.md %}

