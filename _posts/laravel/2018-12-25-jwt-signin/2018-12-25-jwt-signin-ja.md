---
layout: 'post'
permalink: '/laravel/jwt-signin/'
paginate_path: '/laravel/:num/jwt-signin/'
lang: 'ja'
categories: 'laravel'
comments: true

title: 'jwt:ログイン'
description: 'トークンベース認証システムであるjwt(Json Web Token)を使ってログイン手続きを実装して見ましょう。'
image: '/assets/images/category/laravel/jwt-signin.png'
---


## 概要
jwt認証システムを使ってログイン機能を実装してみようかと思います。このブログはシリーズで構成されています。jwt実装のためミドルウェア(Middleware)インストールや会員登録機能の実装に関しては以前のブログを確認してください。

- [jwtインストールや設定]({{site.url}}/{{page.categories}}/jwt/){:target="_blank"}
- [jwt:会員登録]({{site.url}}/{{page.categories}}/jwt/jwt-siginup){:target="_blank"}

## リポジトリ(Repository)
私たちはjwt認証システムを実装したリポジトリ(Repository)を作りました。下記のリンクを押してリポジトリ(Repository)を確認してみてください。

- laravel-jwt-exercise: [https://github.com/dev-yakuza/laravel-jwt-exercise](https://github.com/dev-yakuza/laravel-jwt-exercise){:rel="nofollow noreferrer" target="_blank"}

## 開発環境構成
ここで説明する内容はLaradockとアンシブル(Ansible)を使って作ったララベル(Laravel)開発環境上で開発やテストします。Laradockとアンシブル(Ansible)を使ってララベル(Laravel)開発環境については下のブログを参考してください。

- [アンシブル&ララベル]({{site.url}}/environment/ansible-laravel/){:target="_blank"}

## モデル修正
jwt認証システムの認証に使わられるモデル(Model)を下記のように修正します。

```php
<?php
...
use Illuminate\Foundation\Auth\User as Authenticatable;
use Tymon\JWTAuth\Contracts\JWTSubject;
...
class User extends Authenticatable implements JWTSubject
{
    ...
    public function getJWTIdentifier() {
        return $this->getKey();
    }

    public function getJWTCustomClaims() {
        return [];
    }
}
```

ララベル(Laravel)の認証機能を使うためにモデル(Model)を```Authenticatable```から継承しました。
また、jwtミドルウェア(Middleware)のインタフェースを```JWTSubject```を通じて実装します。

```php
public function getJWTIdentifier() {
    return $this->getKey();
}

public function getJWTCustomClaims() {
    return [];
}
```

上の関数はjwtミドルウェア(Middleware)のインタフェースを実装した部分です。

```php
public function getJWTIdentifier() {
    return $this->getKey();
}
```

この部分はjwtのトークンを取得するための関数です。

```php
public function getJWTCustomClaims() {
    return [];
}
```

この関数を説明するためjwtトークンを少し説明します。jwtは大きく```ヘッダー(header).内容(payload).署名(signature)```で構成されています。その中```内容(Payload)```に使われる情報の一部を```Claim```と呼ばれ、```key-value```形式で構成されています。jwtは基本的に```内容(Payload)```に下記のような情報(```Claim```)を持ってます。

- iss(Issuer): トークン発行者
- sub(Subject): トークンのタイトル(デフォルトはuser id)
- iat(Issued At): トークン発行日(unix timestamp)
- exp(Expiry): トークンの有効期限
- nbf(Not Before): トークンを使えるスタート時間
- jti(JWT Id): JWTのユニーク識別子。 主に重複的な処理を防止するために使う。
- prv: ユーザープロバイダクラス(User Provider class)のハッシュ。複数のguardを使うために```tymondesigns/jwt-auth```に追加された特別なコード。([詳しく説明はこちらへ](https://github.com/tymondesigns/jwt-auth/pull/1167){:rel="nofollow noreferrer" target="_blank"})

この情報以外、追加的にjwtトークンに情報を追加したい時、```getJWTCustomClaims()```関数に戻り値(Return value)を修正します。

```php
public function getJWTCustomClaims() {
    return [
        'firstname' => $this->firstname,
        'lastname' => $this->lastname,
        'email' => $this->email
    ];
}
```

## guard修正
ララベル(Laravel)の認証を担当してる```config/auth.php```ファイルの```guard```を下記のように修正します。

```php
'guards' => [
    'web' => [
        'driver' => 'session',
        'provider' => 'users',
    ],

    'api' => [
        'driver' => 'jwt',
        'provider' => 'users',
    ],
],
```

## コントローラー修正
以前のブログで生成した```app/Http/Controllers/JWTAuthController.php```コントローラーにログイン関数を追加します。

```php
public function login(Request $request) {
    $validator = Validator::make($request->all(), [
        'email' => 'required|email|max:255',
        'password' => 'required|string|min:8|max:255',
    ]);

    if($validator->fails()) {
        return response()->json([
            'status' => 'error',
            'messages' => $validator->messages()
        ], 200);
    }

    if (! $token = Auth::guard('api')->attempt(['email' => $request->email, 'password' => $request->password])) {
        return response()->json(['error' => 'Unauthorized'], 401);
    }

    return $this->respondWithToken($token);
}

protected function respondWithToken($token) {
    return response()->json([
        'access_token' => $token,
        'token_type' => 'bearer',
        'expires_in' => Auth::guard('api')->factory()->getTTL() * 60
    ]);
}
```

まず、リクエスト(Request)の入力データを確認します。

```php
$validator = Validator::make($request->all(), [
    'email' => 'required|email|max:255',
    'password' => 'required|string|min:8|max:255',
]);

if($validator->fails()) {
    return response()->json([
        'status' => 'error',
        'messages' => $validator->messages()
    ], 200);
}
```

そしてユーザの```email```と```password```でログインさせます。

```php
if (! $token = Auth::guard('api')->attempt(['email' => $request->email, 'password' => $request->password])) {
    return response()->json(['error' => 'Unauthorized'], 401);
}
```

ログインに成功したらリクエスト(Request)に関してjwtトークンをリターン(Response)します。

```php
return response()->json([
    'access_token' => $token,
    'token_type' => 'bearer',
    'expires_in' => Auth::guard('api')->factory()->getTTL() * 60
]);
```

## ルート連結
コントローラー(Controller)に生成したログイン関数を```routes/api.php```でURLと連携する必要があります。

```php
Route::post('login', 'JWTAuthController@login')->name('api.jwt.login');
```

## テスト
今まで開発したjwt認証システムのログイン機能を```Postman```を使って確認します。```localhost/api/login```のURLに```email```と```password```を入力して```POST```でリクエスト(Request)を送ったら下記のような結果を確認することができます。

![postman login api test](/assets/images/category/laravel/jwt-signin/login.png)

応答(Response)で貰った```access_token```キーを[https://jwt.io/](https://jwt.io/){:rel="nofollow noreferrer" target="_blank"}で確認すると下記のような結果を見ることができます。

![check access_key](/assets/images/category/laravel/jwt-signin/check_access_key.png)

## 完了
これでjwt認証システムを利用してログイン機能を実装して見ました。次のブログでは```access token```を使ってユーザの情報を取得する方法に関して見てみます。

## 参考
- JSON Web Token (JWT): [https://tools.ietf.org/html/rfc7519#section-4.1](https://tools.ietf.org/html/rfc7519#section-4.1){:rel="nofollow noreferrer" target="_blank"}
- jwt-auth prv: [https://github.com/tymondesigns/jwt-auth/issues/1344](https://github.com/tymondesigns/jwt-auth/issues/1344){:rel="nofollow noreferrer" target="_blank"}
- jwt-auth Creating Tokens: [https://github.com/tymondesigns/jwt-auth/wiki/Creating-Tokens](https://github.com/tymondesigns/jwt-auth/wiki/Creating-Tokens){:rel="nofollow noreferrer" target="_blank"}

