```html
{% raw %}<head>
    ...
    <title>{{page.title}} - {{page.description}}</title>
    <meta name="description" content="{{ page.excerpt | default: site.description | strip_html | normalize_whitespace | truncate: 160 | escape }}">
    ...
</head>{% endraw %}
```