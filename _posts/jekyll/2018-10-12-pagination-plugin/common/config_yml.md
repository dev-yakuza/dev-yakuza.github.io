```yml
plugins:
  - jekyll-paginate-v2

permalink: /:year/:month/
pagination:
  enabled: true
  per_page: 12
  sort_reverse: true
  sort_field: 'date'
  title: ':title'
  trail:
    before: 2
    after: 2
```