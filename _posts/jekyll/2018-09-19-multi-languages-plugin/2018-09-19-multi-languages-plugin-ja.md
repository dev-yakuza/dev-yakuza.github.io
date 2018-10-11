---
layout: 'post'
permalink: '/jekyll/multi-languages-plugin/'
paginate_path: '/jekyll/:num/multi-languages-plugin/'
lang: 'ja'
categories: 'jekyll'
comments: true

title: '多言語プラグイン'
description: 'jekyllの多言語を対応するために使うプラグインを紹介します。多言語プラグインjekyll-polyglotのインストールと設定について確認します。'
image: '/assets/images/category/jekyll/multi-languages-plugin.jpg'
---


## 多言語プラグイン
jekyllの多言語を対応するためにプラグインのインストールと設定に関して紹介します。様々な多言語プラグインがありますが、ここには[jekyll-polyglot](https://github.com/untra/polyglot){:rel="nofollow noreferrer" target="_blank"}を紹介します。

他の多言語プラグインが知りたい方は[awesome-jekyll-plugins](https://github.com/planetjekyll/awesome-jekyll-plugins#multi-language--multi-lingual){:rel="nofollow noreferrer" target="_blank"}をご参考してください。

## プラグインインストール
- コンソールへ下記のコマンドを打ちてプラグインをインストールします。

{% include_relative common/install_plugin.md %}

- ```_config.yml```へプラグインをセッティングします。

{% include_relative common/set_plugin.md %}

## プラグインのグローバル設定
- ```_config.yml```ファイルへ下記のように設定します。

{% include jekyll/configuration_multi_languages.md %}

- languages: サイトで対応する多言語リストです。
- default_lang: 対応する多言語中でデフォルト言語を設定します。
- exclude_from_localization: 多言語を対応したく無いフォルダリストを設定します。
- parallel_localization: trueに設定するとjekyllがページをコンパイルする時fork()を使ってサイトを同時にコンパイルします。Windows OSはfork()が無いのでfalseで設定しないとエラーが出ます。

## ページ設定

- ```_posts```フォルダへ下記のようにフォルダとファイルを作ります。

{% include_relative common/folder_structure.md %}

- 2018-09-19-multi-languages-plugin: 管理のために```_posts```フォルダ下へポストタイトルでフォルダを作ります。
- common: 多言語ファイルで共通で使うファイルを保存します。例えば、今見てるフォルダ構造は```folder_structure.md```へ作成して```{% raw %}{% include_relative common/folder_structure.md % }{% endraw %}```を使って表示してます。
- 2018-09-19-multi-languages-plugin-[言語].md: ```_config.yml```の```languages```へ設定した言語別ページを作成します。
- 各言語ページ上部へ各ページの言語を設定します。

```yml
---
layout: 'post'
lang: 'ja'
...
---
```

## 確認
全ての設定を完了しました。各ページを確認する方法に関して紹介します。

- ページ設定を通じて生成されたページは下記のようにURLでアクセスが可能です。

{% include_relative common/page_link.md %}

- ```_config.yml```の```default_lang```へ設定した言語は```http://site_url/path```で直接アクセスができます。
- ```default_lang```以外の言語は```http://site_url/[言語]/path```で各言語のページへアクセスができます。
- jekyllのテストサーバーを起動するとかビルドをしたら、```_site```フォルダ下へ多言語フォルダを確認することができます。
    - サーバー起動コマンド: {% include jekyll/test_server_command.md %}
    - ビルドコマンド: {% include jekyll/build_command.md %}

