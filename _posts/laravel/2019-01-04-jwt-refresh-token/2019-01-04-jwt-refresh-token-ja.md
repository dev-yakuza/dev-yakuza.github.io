---
layout: 'post'
permalink: '/laravel/jwt-refresh-token/'
paginate_path: '/laravel/:num/jwt-refresh-token/'
lang: 'ja'
categories: 'laravel'
comments: true

title: 'jwt:トークン更新'
description: 'トークンベース認証システムであるjwt(Json Web Token)を使ってログインした後取得したjwtトークンを更新(Refresh)する機能を追加して見ましょう。'
image: '/assets/images/category/laravel/jwt-refresh-token.jpg'
---


## 概要
jwt認証システムを使ってログインした後取得したjwtトークンを更新(Refresh)する方法について説明します。このブログはシリーズで構成されています。jwt実装のためミドルウェア(Middleware)のインストールや会員登録、ログイン、ユーザ情報取得機能については以前のブログを参考してください。

- [jwtインストールや設定]({{site.url}}/{{page.categories}}/jwt/){:target="_blank"}
- [jwt:会員登録]({{site.url}}/{{page.categories}}/jwt-signup){:target="_blank"}
- [jwt:ログイン]({{site.url}}/{{page.categories}}/jwt-signin){:target="_blank"}
- [jwt:ユーザ情報]({{site.url}}/{{page.categories}}/jwt-user-info){:target="_blank"}

## リポジトリ(Repository)
私たちはjwt認証システムを実装したリポジトリ(Repository)を作りました。下記のリンクを押してリポジトリ(Repository)を確認してみてください。

- laravel-jwt-exercise: [https://github.com/dev-yakuza/laravel-jwt-exercise](https://github.com/dev-yakuza/laravel-jwt-exercise){:rel="nofollow noreferrer" target="_blank"}

## 開発環境構成
ここで説明する内容はLaradockとアンシブル(Ansible)を使って作ったララベル(Laravel)開発環境上で開発やテストします。Laradockとアンシブル(Ansible)を使ってララベル(Laravel)開発環境については下のブログを参考してください。

- [アンシブル&ララベル]({{site.url}}/environment/ansible-laravel/){:target="_blank"}

## コントローラー修正
ララベル(Laravel)プロジェクトフォルダの```/app/Http/Controllers/JWTAuthController.php```コントローラー(Controller)ファイルを開いて下記の内容を追加します。

```php
public function refresh() {
    return $this->respondWithToken(Auth::guard('api')->refresh());
}
```

## ルート修正
jwtトークンを更新(Refresh)するためのURLを追加するため```/routes/api.php```ファイルを開いて下の内容を追加します。

```php
...
Route::group(['middleware' => 'auth:api'], function(){
    ...
    Route::get('refresh', 'JWTAuthController@refresh')->name('api.jwt.refresh');
    ...
});
...
```

## テスト
今まで開発したjwtトークン更新(Refresh)機能を```Postman```を使って確認します。

```bash
# URL
localhost/api/refresh
# header
Authorization
Bearer jwt_token
```

jwtトークンが有効だったら、下記のようにjwtトークンを更新(Refresh)して新しトークンを発行してもらいます。

![refresh token](/assets/images/category/laravel/jwt-refresh-token/refresh_token.png)

jwtトークンの有効期限が終ったり、以前のjwtトークンを使ったら下記のように```401```エラーの応答(Response)を確認することができます。

![fail to refresh token](/assets/images/category/laravel/jwt-refresh-token/fail_to_refresh_token.png)

## 完了
これでjwt認証システムを使ってログイン後取得したjwtトークンを更新(Refresh)する方法について見て見ました。次のブログではjwt認証システムの最後機能であるログアウト機能を追加する方法に関して見て見ます。