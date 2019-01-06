---
layout: 'post'
permalink: '/laravel/jwt-logout/'
paginate_path: '/laravel/:num/jwt-logout/'
lang: 'ja'
categories: 'laravel'
comments: true

title: 'jwt:ログワウと'
description: 'jwt(Json Web Token)認証システムのログアウト機能を実装する方法について見て見ます。'
image: '/assets/images/category/laravel/jwt-logout.jpg'
---


## 概要
jwt認証システムへログアウト機能を追加する方法について説明します。このブログはシリーズで構成されています。jwt実装のためミドルウェア(Middleware)のインストールや会員登録、ログイン、ユーザ情報取得、jwtトークン更新機能については以前のブログを確認してください。

- [jwtインストールや設定]({{site.url}}/{{page.categories}}/jwt/){:target="_blank"}
- [jwt:会員登録]({{site.url}}/{{page.categories}}/jwt-signup){:target="_blank"}
- [jwt:ログイン]({{site.url}}/{{page.categories}}/jwt-signin){:target="_blank"}
- [jwt:ユーザ情報]({{site.url}}/{{page.categories}}/jwt-user-info){:target="_blank"}
- [jwt:トークン更新]({{site.url}}/{{page.categories}}/jwt-refresh-token){:target="_blank"}

## リポジトリ(Repository)
私たちはjwt認証システムを実装したリポジトリ(Repository)を作りました。下記のリンクを押してリポジトリ(Repository)を確認してみてください。

- laravel-jwt-exercise: [https://github.com/dev-yakuza/laravel-jwt-exercise](https://github.com/dev-yakuza/laravel-jwt-exercise){:rel="nofollow noreferrer" target="_blank"}

## 開発環境構成
ここで説明する内容はLaradockとアンシブル(Ansible)を使って作ったララベル(Laravel)開発環境上で開発やテストします。Laradockとアンシブル(Ansible)を使ってララベル(Laravel)開発環境については下のブログを参考してください。

- [アンシブル&ララベル]({{site.url}}/environment/ansible-laravel/){:target="_blank"}

## コントローラー修正
ララベル(Laravel)プロジェクトフォルダの```/app/Http/Controllers/JWTAuthController.php```コントローラー(Controller)ファイルを開いて下記の内容を追加します。

```php
public function logout() {
    Auth::guard('api')->logout();

    return response()->json([
        'status' => 'success',
        'message' => 'logout'
    ], 200);
}
```

## ルート修正
ログアウトのためのURLを追加するため```/routes/api.php```ファイルを開いて下記の内容を追加します。

```php
...
Route::group(['middleware' => 'auth:api'], function(){
    ...
    Route::get('logout', 'JWTAuthController@logout')->name('api.jwt.logout');
    ...
});
...
```

## テスト
今まで開発したログアウト機能を```Postman```を使って確認します。

```bash
# URL
localhost/api/logout
# header
Authorization
Bearer jwt_token
```

jwtトークンが有効だったら下記のように成功的ログアウトが出来ます。

![logout](/assets/images/category/laravel/jwt-logout/logout.png)

jwtトークの有効期限が終ったり、以前のjwtトークンを使ったら下記のように```401```エラーの応答(Response)を確認することが出来ます。

![fail to logout](/assets/images/category/laravel/jwt-logout/fail_to_logout.png)

## 完了
これでララベル(Laravel)にjwt認証システムを追加してトークンベース認証システムを実装しました。私たちはこのjwt認証システムを使ってRN(React native)アプリを開発する予定です。