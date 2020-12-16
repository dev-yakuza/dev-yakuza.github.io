---
layout: 'post'
permalink: '/jekyll/search-bar/'
paginate_path: '/jekyll/:num/search-bar/'
lang: 'ko'
categories: 'jekyll'
comments: true

title: Jekyll 블로그에 검색바 넣기
description: 특별한 플러그인없이 Jekyll 블로그에 검색바를 넣는 방법에 대해서 알아봅시다.
image: '/assets/images/category/jekyll/2020/search-bar/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [데이터 준비](#데이터-준비)
  - [데이터 레이아웃](#데이터-레이아웃)
- [데이터 만들기](#데이터-만들기)
- [검색바 만들기](#검색바-만들기)
  - [HTML 만들기](#html-만들기)
  - [SCSS/CSS 만들기](#scsscss-만들기)
  - [Javascript 작성](#javascript-작성)
  - [검색바 표시](#검색바-표시)
- [완료](#완료)

</div>

## 개요

저는 Jekyll과 GitHub을 이용해서 블로그를 운영하고 있습니다. 블로그 운영 목적은, 정보를 공유하는 목적도 있지만, 자신이 자주 잊어버리는 부분을 기록하고, 필요할 때마다 찾기 위한 목적도 있습니다.

하지만 블로그 내용이 점점 많아지면서, 필요할 때, 빠르게 블로그를 찾는 것이 어려워졌습니다. 그래서 이번에 Jekyll 블로그에 검색바를 넣었습니다.

![Jekyll 블로그에 검색바 넣기 - 검색바](/assets/images/category/jekyll/2020/search-bar/search-bar.jpg)

이번 블로그 포스트에서는 Jekyll 블로그에 플러그인없이 검색바를 만드는 방법에 대해서 소개합니다.

## 데이터 준비

검색 결과를 표시하기 위해서는 검색에 사용될 데이터가 필요합니다. 그 데이터를 만드는 방법에 대해서 알아봅시다.

### 데이터 레이아웃

검색 결과로 표시할 데이터를 Jekyll의 Liquid 문법을 사용하여 JSON 형태로 제작할 예정입니다.

데이터를 생성하기 위해 우선 레이아웃을 만들 필요가 있습니다. 데이터용 레이아웃을 만들기 위해, `_layouts/posts.json` 파일을 생성하고 아래와 같이 수정합니다.

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

위에 소스는 실제로 제 블로그에서 사용하는 소스코드입니다. 여러분들은 여러분들 입맛에 맞게 수정하여 사용하시기 바랍니다.

소스 코드를 좀 더 자세히 살펴보도록 하겠습니다.

```json
{% raw %}
{% if page.target == "home" %}
  {%- assign posts = site.posts -%}
{% else %}
  {%- assign posts = site.posts | where_exp:"item", "item.categories contains page.target" -%}
{% endif %}
{% endraw %}
```

위에 코드는 JSON 데이터로 만들 블로그 포스트들을 가져오는 소스코드입니다. `page.target`이 `home`인 경우 전체 블로그 포스트를, 그렇지 않은 경우 `page.target`이 블로그 포스트의 카테고리(`item.categories`)에 포함이 된 경우만 포스트만 준비합니다. 여기서 사용되는 `page.target`은 Jekyll이 제공하는 기본 변수가 아닌, JSON 데이터를 만들기 위해 만든 변수입니다.

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

이렇게 준비된 데이터를 가지고, 단순히 루프를 돌면서 JSON 형식으로 데이터를 만듭니다.

{% include in-feed-ads.html %}

## 데이터 만들기

위에서 만든 레이아웃을 사용하여 실제 데이터를 만들어 봅시다. 보통의 Jekyll 블로그라면 `_posts` 폴더 하위에 블로그 포스트들을 작성합니다.

```bash
|- _posts
  |- react-native
    |- 2020-01-01-new-blog.md
    |- 2020-01-02-new-blog.md
    |- 2020-01-03-new-blog.md
```

여기에 알아보기 편한 이름으로 JSON 데이터용 파일을 하나 생성합니다.(ex> `posts.md`, `api.md`...)

```bash
|- _posts
  |- react-native
    |- posts.md
    |- 2020-01-01-new-blog.md
    |- 2020-01-02-new-blog.md
    |- 2020-01-03-new-blog.md
```

그리고 그 파일을 열고 아래와 같이 수정합니다.

```md
---
layout: 'posts'
permalink: '/api/react-native/posts.json'
target: 'react-native'
---
```

위에서 생성한 레이아웃을 사용하기 위해 `layout: 'posts'`을 지정하였습니다. 그리고 데이터가 배포될 URL을 지정하기 위해 `permalink`에 특정 URL을 적용하였습니다.

마지막으로 가장 중요한 `target` 변수입니다. 현재 예제에는 `react-native`을 지정하고 있습니다. 위에서 만든 레이아웃을 떠올려 보면, 블로그 포스트의 `categories`에 이렇게 지정한 `target`이 포함된 포스트들만 JSON 데이터를 생성하도록 하였습니다. 즉, `react-native`라는 카테고리를 가지고 있는 포스트들만 JSON 데이터로 생성됩니다.

모든 포스트들을 포함한 JSON 데이터를 생성하고자 한다면, 이 `target`에 `home`이라고 지정하면 됩니다. 이것도 Jekyll의 룰이 아니기 때문에 다른 이름으로 지정하셔도 됩니다.(ex> `all`) 물론, 다른 이름으로 지정하시고 싶으시다면 위에서 만든 `_layouts/posts.json` 파일의 if문도 수정해야 합니다.

## 검색바 만들기

여기서 부터는 단순한 디자인 코딩입니다. HTML과 CSS로 검색바를 디자인하고, jQuery를 사용하여 위에서 만든 JSON 데이터를 가져오도록 할 예정입니다.

### HTML 만들기

화면에 검색바를 표시하기 위해 `_includes/search_bar.html`을 만들고 아래와 같이 수정합니다. 단순한 디자인이므로, 이 코드는 참고만 하시고 여러분이 직접 만드시는 것을 권장합니다.

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

### SCSS/CSS 만들기

각 테마에 디자인을 담당하는 `SCSS` 또는 `CSS` 파일이 있습니다. 제가 사용하는 테마인 경우 `_sass/styles.scss` 파일이 있습니다. 이 파일을 열고 아래와 같이 수정합니다.

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

제가 사용하는 테마는 SCSS를 사용하므로 `SCSS` 형식으로 작성하였습니다. CSS 형식을 사용하는 테마라면, CSS 형식에 맞춰 코드를 작성해 주시기 바랍니다.

### Javascript 작성

이제 우리가 만든 JSON 데이터를 불러오기 위해 Javascript를 작성해 봅시다. 제가 사용하는 테마는 기본적으로 `jQuery`를 사용하고 있으므로 여기에서는 jQuery로 작성된 소스코드를 소개합니다.

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

소스 코드를 자세히 살펴보겠습니다.

```js
var posts = [];
$.get('/api/{{ page.categories }}/posts.json', function (data) {
  posts = data;
});
```

데이터를 담을 변수 `posts`와 위에서 만든 JSON 데이터를 `ajax`를 사용하여 가져온 후, `posts` 변수에 할당하였습니다. `ajax`의 URL은 여러분에 상황에 맞게 수정하시기 바랍니다. 저는 하나의 블로그 포스트는 하나의 카테고리만을 가지고 있기 때문에 위와 같이 사용하였습니다.

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

검색바에서 검색어를 입력하면, 검색어를 소문자로 만들고, 검색 결과 화면을 표시할 HTML을 화면에 표시하도록 하였습니다.

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

그 후, 검색 결과 데이터를 루프 돌면서, 제목과 설명글에 일치하는 항목을 찾습니다.

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

마지막으로, 검색 결과가 없으면 `검색 결과가 없습니다.`를 표시하고, 검색 결과가 있는 경우, 루프를 돌면서 리스트를 표시합니다.

{% include in-feed-ads.html %}

### 검색바 표시

아래에 코드를 사용하여 검색바를 표시하고 싶은 곳에서 표시할 수 있습니다

```rb
{% raw %}
{% include search_bar.html %}
{% endraw %}
```

## 완료

제가 사용하는 소스코드를 소개하다보니, 내용이 생각보다 많이 길어졌습니다. 이번 블로그 포스트에서 가장 중요한 것은 JSON 데이터를 만드는 것입니다. 나머지는 여러분의 멋진 디자인으로 검색바를 만들고, 간단한 자바스크립트 코드로 만들어 놓은 JSON 데이터를 검색하면 됩니다.

이제 여러분의 Jekyll 블로그에 멋진 검색바를 붙여보세요!