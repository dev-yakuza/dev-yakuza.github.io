---
layout: 'post'
permalink: '/jekyll/utterances/'
paginate_path: '/jekyll/:num/utterances/'
lang: 'ja'
categories: 'jekyll'
comments: true

title: Jekyllブログにコメント機能
description: utterancesのサービスを使ってJekyllのプロジェクトへコメント機能を追加してみましょう。
image: '/assets/images/category/jekyll/2021/utterances/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [utterances連動](#utterances連動)
- [スクリプト生成](#スクリプト生成)
- [Jekyllブログに適用](#jekyllブログに適用)
- [完了](#完了)

</div>

## 概要

今までJekyllブログのコメントサービスに[Disqus](https://disqus.com/){:rel="nofollow noreferrer" target="_blank"}を使いました。`Disqus`を使ってJekyllブログにコメント機能を入れる方法については下記のリンクを参考してください。

- [Disqusコメント]({{site.url}}/{{page.categories}}/disqus/){:target="_blank"}

しかし、最近`Disqus`が広告をつけはじめました。広告を消すためには有料でサービスを利用する必要があります。これで他のコメントサービスを探して、`GitHub`の機能を使ってコメントサービスを実装した`utterances`を見つけました。

- [utterances](https://utteranc.es/){:rel="nofollow noreferrer" target="_blank"}

このブログポストでは`utterances`を使ってJekyllブログにコメント機能を実装する方法について説明します。

## utterances連動

utterancesは基本的GitHubのIssueを作ってコメントを生成します。utterancesがGitHubのIssueを作れるようにするためGitHubと連動をして、権限を許可する必要があります。下記のリンクをクリックしてutterancesのGitHub Appページへ移動します。

- GitHub App: [utterances](https://github.com/apps/utterances){:rel="nofollow noreferrer" target="_blank"}

utterancesのGitHub Appページに移動すると次のような画面が見えます。

![utterances GitHub App page](/assets/images/category/jekyll/2021/utterances/utterances-github-app-configure.jpg)

右にある`Configure`ボタンを選択します。

![utterances select organization](/assets/images/category/jekyll/2021/utterances/utterances-connect-organization.jpg)

次はutterancesがGitHubのIssueを作る権限を許可するアカウントを選択します。

![utterances select repository](/assets/images/category/jekyll/2021/utterances/utterances-select-repository.jpg)

アカウントを選択したら、次はutterancesがアクセス可能なリポジトリ(Repository)を選択します。

{% include in-feed-ads.html %}

## スクリプト生成

このようにutterancesがGitHubのIssueを生成するようになりました。このように生成されたGitHubのIssueを画面に表示するためutterancesのスクリプトを生成してみましょう。

utterancesのスクリプトを生成するため、下記のリンクを使って公式ページに移動します。

- 公式ページ: [utterances](https://utteranc.es/){:rel="nofollow noreferrer" target="_blank"}

公式ページに移動して、少しスクロールをすると、下記のようにリポジトリ（Repository）入力する画面を見つけることができます。

![utterances insert repository](/assets/images/category/jekyll/2021/utterances/utterances-insert-repository.jpg)

`Repo`の下にある入力に上でIssueを生成できるように権限を与えたリポジトリを`[User Name]/[Repository]`の形式でn湯りょくします。入力が終わったら、下にある`Blog Post ↔️ Issue Mapping`の項目に行きます。

![utterances mapping repository](/assets/images/category/jekyll/2021/utterances/utterances-mapping-repository.jpg)

GitHubのIssueの中で当該ページのコメントだけを表示するための方法を選択する項目です。私は`Issue title contains page URL`を選択しましたが、好きな項目を選べれば良いです。

また、少しスクロールすると、`Issue Label`の項目が見えます。

![utterances issue label](/assets/images/category/jekyll/2021/utterances/utterances-issue-label.jpg)

GitHubでIssueが生成される時、他のIssueと区別するため当該Issueにラベルを入れるオプションです。私は特に設定しなくて進めました。

次は表示されるコメントのテーマを設定する項目が見えます。

![utterances select theme](/assets/images/category/jekyll/2021/utterances/utterances-select-theme.jpg)

自分のブログのテーマに合わせてオプションを選択します。私は`GitHub Light`のテーマを選択して進めました。このように全ての項目に自分のブログに合わせて選択をしたら、下に次のようにutterancesスクリプトが生成されることが確認できます。

![utterances script](/assets/images/category/jekyll/2021/utterances/utterances-script.jpg)

{% include in-feed-ads.html %}

## Jekyllブログに適用

このように生成されたスクリプトをJekyllブログに追加して画面に表示してみましょう。私は[Clean Blog](http://jekyllthemes.org/themes/clean-blog/){:rel="nofollow noreferrer" target="_blank"}テーマを使ってます。Jekyllブログにテーマを設定する方法については下記のリンクを参考してください。

- [テーマ設定]({{site.url}}/{{page.categories}}/theme/){:target="_blank"}

自分のテーマでブログの内容を表示するテンプレートを探してコピーしたスクリプトを追加します。私は`_layouts/post.html`ファイルに次のように追加しました。

```html
<div class="col-lg-8 col-md-10 mx-auto">
  <hr />
  {% if page.comments %}
  <script src="https://utteranc.es/client.js"
    repo="dev-yakuza/dev-yakuza.github.io"
    issue-term="url"
    label="comment"
    theme="github-light"
    crossorigin="anonymous"
    async>
  </script>
  {% endif %}
</div>
```

これで`utterances`を使ってJekyllブログにコメント機能を追加してみました。次は追加した内容がうまく表示されるか確認するため次のコマンドを実行してJekyllブログを実行します。

```bash
bundle exec jekyll serve
```

問題なく実行されたら、ブログページに次のようにutterancesのコメント機能が表示されることが確認できます。

![utterances comment on jekyll](/assets/images/category/jekyll/2021/utterances/utterances-comment-on-jekyll.jpg)

## 完了

これでJekyllブログにutterancesを使ってコメント機能を実装する方法についてみてみました。皆さんもJekyllブログを使っていたら、utterancesを使ってコメント機能を入れてみてください！
