---
layout: 'post'
permalink: '/jekyll/search-bar/'
paginate_path: '/jekyll/:num/search-bar/'
lang: 'ja'
categories: 'jekyll'
comments: true

title: Jekyllブログへ検索バーを入れる
description: 特にプラグインを入れなくて、Jekyllブログへ検索バーを入れる方法について説明します。
image: '/assets/images/category/jekyll/2020/search-bar/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [データの準備](#データの準備)
  - [データレイアウト](#データレイアウト)
- [デーアを作る](#デーアを作る)
- [検索バーを作る](#検索バーを作る)
  - [HTMLを作る](#htmlを作る)
  - [SCSS/CSSを作る](#scsscssを作る)
  - [Javascriptを作成](#javascriptを作成)
  - [検索バーを表示](#検索バーを表示)
- [完了](#完了)

</div>

## 概要

私はJekyllとGitHubを使ってブログを運営しています。ブログの運営目的は、情報の共有もありますが、自分がよく忘れる部分を残して、必要な時探して見るためもあります。

しかしブログポストが多くなって、必要な時、早くブログを探すことが大変になりました。それで、今回Jekyllブログへ検索バーを入れることにしました。

![Jekyllブログへ検索バーを入れる - 検索バー](/assets/images/category/jekyll/2020/search-bar/search-bar.jpg)

今回のブログポストではJekyllブログへプラグインを使わなく、検索バーを作る方法について紹介します。

## データの準備

検索結果を表示するためには検索へ使うデータが必要です。そのデータを作る方法について説明します。

### データレイアウト

検索結果を表示するデータをJekyllのLiquid文法を使ってJSON形で作成する予定です。

データを生成するためにはまず、レイアウトを作る必要があります。データ用のレイアウトを作るため、`_layouts/posts.json`ファイルを生成して下記のように修正します。

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

上のソースコードは実際私がこのブログで使ってるソースコードです。皆さんは皆さんのブログに合わせて、カスタマイズして使ってください。

ソースコードを詳しく見てみます。

```json
{% raw %}
{% if page.target == "home" %}
  {%- assign posts = site.posts -%}
{% else %}
  {%- assign posts = site.posts | where_exp:"item", "item.categories contains page.target" -%}
{% endif %}
{% endraw %}
```

上のコードはJSONデータで吐き出すブログポストたちを持ってくるソースコードです。`page.target`が`home`の場合、全てのブログポストを、`home`じゃない場合は`page.target`がブログポストのカテゴリー(`item.categories`)に含まれたポストだけを用意します。ここで使った`page.target`はJekyllga提供する基本変数ではなく、JSONデータを作るため作った変数です。

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

このように準備したデータを持って、単純にループをしながら、JSONの形のデータを作ります。

{% include in-feed-ads.html %}

## デーアを作る

上で作ったレイアウトを使って実際データを作って見ます。普通のJekyllブログなら、`_posts`フォルダの下にブログポストを作成します。

```bash
|- _posts
  |- react-native
    |- 2020-01-01-new-blog.md
    |- 2020-01-02-new-blog.md
    |- 2020-01-03-new-blog.md
```

ここに分かりやすい名前でJSONデータ用のファイルを1個生成します。(ex> `posts.md`, `api.md`...)

```bash
|- _posts
  |- react-native
    |- posts.md
    |- 2020-01-01-new-blog.md
    |- 2020-01-02-new-blog.md
    |- 2020-01-03-new-blog.md
```

そしてそのファイルを開いて下記のように修正します。

```md
---
layout: 'posts'
permalink: '/api/react-native/posts.json'
target: 'react-native'
---
```

上で生成したレイアウトを使うため`layout: 'posts'`を指定しました。そして、データが配布されるURLを指定するため`permalink`へ特定なURLを適用しました。

最後に最も重要な`target`変数です。現在の例題では`react-native`を指定してます。上で作ったレイアウトを覚えてみると、ブログポストの`categories`へこのように指定した`target`が含まれたポストだけJSONデータで生成されるようにしましあ。つまり、`react-native`と言うカテゴリーを持ってるポストだけJSONデータで生成されます。

全てのポストを持ってるJSONデータを生成したい場合、この`target`へ`home`と指定します。この`home`もJekyllのルールではないので、他の名前を使っても大丈夫です。(ex> `all`)もちろん、他の名前を使った場合は上で作った`_layouts/posts.json`ファイルのif文も修正しなきゃならないです。

## 検索バーを作る

ここからは単純なデザインコーディングです。HTMLとCSSで検索バーをデザインして、jQueryを使って上で作ったJSONデータを撮ってくる予定です。

### HTMLを作る

画面へ検索バーを表示するため`_includes/search_bar.html`を作って下記のように修正します。単純なデザインなので、このコードは参考だけして皆さんが直接作ることをおすすめします。

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

### SCSS/CSSを作る

各テーマへデザインを担当する`SCSS`や`CSS`ファイルがあると思います。私が使ってるテーマの場合、`_sass/styles.scss`のファイルがデザインを担当してます。このようなファイルを開いて下記のように修正します。

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

私が使ってるテーマはSCSSを使ってますので、`SCSS`の形で作成しました。CSSの形を使ってるテーマの場合はCSS形式に合わせてコードを作成してください。

### Javascriptを作成

次は、上で作ったJSONデータを読んでくるJavascriptを作成してみます。私が使ってるテーマは基本的`jQuery`を使ってるので、ここにはjQueryで作成されたソースコードを紹介します。

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

ソースコードを詳しく見ます。

```js
var posts = [];
$.get('/api/{{ page.categories }}/posts.json', function (data) {
  posts = data;
});
```

データを保管する変数`posts`と上で作ったJSONデータを`ajax`を使って取ってきた後、`posts`へ保存しました。`ajax`のURLは皆さんの状況に合わせて変更してください。私は1つのブログポストは1つのカテゴリーだけ使ってるので上のように使いました。

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

検索バーへ検索語を入力すると、検索語を小文字にして、検索結果を画面へ表示するためのHTMLを画面に表示させます。

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

その後、検索結果のデータをループしながら、タイトルと説明文へ一致する項目を探します。

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

最後は検索結果がない場合は`検索結果がありません。`を表示して、検索結果がある場合は、ループをしながらリストを表示します。

{% include in-feed-ads.html %}

### 検索バーを表示

下記のコードを使って検索バーを表示したい場所へ表示することができます。

```rb
{% raw %}
{% include search_bar.html %}
{% endraw %}
```

## 完了

私が作ったソースコードを紹介したので、内容が考えたより多くなりました。このブログポストで最も重要なことはJSONデータを作ることです。他のものは皆さんの素敵なデザインで検索バーを作って、簡単なJavascriptコードを作ったJSONデータを検索します。

皆さんも皆さんのJekyllブログへ素敵な検索バーを入れてみてください！
