---
layout: 'post'
permalink: '/laravel/jwt-user-info/'
paginate_path: '/laravel/:num/jwt-user-info/'
lang: 'ja'
categories: 'laravel'
comments: true

title: 'jwt:ユーザ情報'
description: 'トークンベース認証システムであるjwt(Json Web Token)を使ってログインしたユーザ情報を取得する方法についてみてみましょう。'
image: '/assets/images/category/laravel/jwt-user-info.jpg'
---


## 概要
jwt認証システムを使ってログインしたユーザの情報を取得する方法についてみてみようかと思います。このブログはシリーズで構成されています。jwt実装のためミドルウェア(Middleware)インストールや会員登録、ログインの実装については以前のブログを参考してください。

- [jwtインストールや設定]({{site.url}}/{{page.categories}}/jwt/){:target="_blank"}
- [jwt:会員登録]({{site.url}}/{{page.categories}}/jwt/jwt-siginup){:target="_blank"}
- [jwt:ログイン]({{site.url}}/{{page.categories}}/jwt/jwt-signin){:target="_blank"}

## リポジトリ(Repository)
私たちはjwt認証システムを実装したリポジトリ(Repository)を作りました。下記のリンクを押してリポジトリ(Repository)を確認してみてください。

- laravel-jwt-exercise: [https://github.com/dev-yakuza/laravel-jwt-exercise](https://github.com/dev-yakuza/laravel-jwt-exercise){:rel="nofollow noreferrer" target="_blank"}

## 開発環境構成
ここで説明する内容はLaradockとアンシブル(Ansible)を使って作ったララベル(Laravel)開発環境上で開発やテストします。Laradockとアンシブル(Ansible)を使ってララベル(Laravel)開発環境については下のブログを参考してください。

- [アンシブル&ララベル]({{site.url}}/environment/ansible-laravel/){:target="_blank"}

## コントローラー修正　
ララベル(Laravel)プロジェクトフォルダの```/app/Http/Controllers/JWTAuthController.php```ファイルを開いて下記の内容を追加します。

```php
public function user() {
    return response()->json(Auth::guard('api')->user());
}
```

クライアント(Client, ブラウザ)のリクエスト(Request)でログインしたユーザの情報と取得して応答(Response)する関数です。
의 요청(Request)으로 로그인한 유저의 정보를 얻어 응답(Response)하는 함수입니다.

## ルート修正
コントローラー(Controller)に追加した関数をURLと連携するためルート(Route)を修正します。```/routes/api.php```ファイルを開いて下の内容を追加します。

```php
Route::get('unauthorized', function() {
    return response()->json([
        'status' => 'error',
        'message' => 'Unauthorized'
    ], 401);
})->name('api.jwt.unauthorized');

Route::group(['middleware' => 'auth:api'], function(){
    Route::get('user', 'JWTAuthController@user')->name('api.jwt.user');
});
```

ユーザ情報を取得するため```user```ルート(Route)はミドルウェア(Middleware)で```auth:api```を使います。このミドルウェア(Middleware)によってログインしたユーザとログインしてないユーザを判断してログインしたユーザだけユーザ情報を取得することが出来ます。ログインしてないユーザは```unauthorized```ルート(Route)にリダイレクト(Redirect)をさせて```401```を応答(Response)する予定です。

## リダイレクト
ララベル(Laravel)の```Auth```ミドルウェア(Middleware)は基本的にリダイレクト(Redirect)機能を持ってます。私たちはここに```api```用リダイレクト(Redirect)を設定して```401```エラーを応答(Response)するように設定します。```app/Http/Middleware/Authenticate.php```ファイルを開いて下記のように修正します。

```php
protected function redirectTo($request)
{
    if (! $request->expectsJson()) {
        if ($request->is('api/*')) {
            return route('api.jwt.unauthorized');
        }
        return route('login');
    }
}
```

## テスト
今まで開発したユーザ情報取得機能を```Postman```を使って確認します。

```bash
# URL
localhost/api/user
# header
Authorization
Bearer jwt_token
```

jwtトークンが有効だったら、下記のようにユーザの情報を取得します。

![get user info](/assets/images/category/laravel/jwt-user-info/get_user_info.png)

jwtトークンの有効期限が終わったり、ログインしてないユーザが情報をリクエスト(Request)すると下記のように```401```エラーの応答(Response)を確認することが出来ます。

![fail to get user info](/assets/images/category/laravel/jwt-user-info/fail_to_get_user_info.png)

## 完了
これでjwt認証システムを使ってログインしたユーザの情報を取得するapiを開発しました。次のブログではログインした後、apiを使って取得したjwtトークンを更新(Refresh)する機能を追加してみます。