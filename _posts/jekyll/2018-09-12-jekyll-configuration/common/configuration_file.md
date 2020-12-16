```yml
title: ...
email: 'dev.yakuza@gmail.com'
description: ...
baseurl: ...
url: https://dev-yakuza.github.io
twitter_username: ...
github_username: ...
author: dev.yakuza@gmail.com

markdown: kramdown
plugins:
  - jekyll-feed
  - jekyll-paginate-v2
  - jekyll-polyglot
  - jekyll-seo-tag

exclude:
  - Gemfile
  - Gemfile.lock

# pagination
permalink: /:year/:month/
pagination:
  enabled: true
  per_page: 12
  sort_reverse: true
  limit: 0
  sort_field: 'date'
  permalink: '/page/:num/'
  title: ':title'
  trail:
    before: 2
    after: 2

# multilang
languages: ['ja', 'ko', 'en']
default_lang: 'ja'
exclude_from_localization: ['javascript', 'images', 'css']
parallel_localization: false

```