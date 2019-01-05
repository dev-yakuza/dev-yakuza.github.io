---
layout: 'post'
permalink: '/laravel/jwt-signup/'
paginate_path: '/laravel/:num/jwt-signup/'
lang: 'ja'
categories: 'laravel'
comments: true

title: 'jwt:会員登録'
description: 'トークンベース認証システムであるjwt(Json Web Token)を使って会員登録を実装してみます。'
image: '/assets/images/category/laravel/jwt-signup.jpg'
---


## 概要
トークンベース認証システムであるjwt(Json Web Token)を使って会員登録機能を実装してみようかと思います。このブログではjwtトークンシステムを[tymon/jwt-auth](https://github.com/tymondesigns/jwt-auth){:rel="nofollow noreferrer" target="_blank"}ミドルウェア(Middleware)を使ってララベル(Laravel)に適用しました。ララベル(Laravel)プロジェクトにjwtミドルウェア(Middleware)である```tymon/jwt-auth```をインストールや設定については以前のブログを参考してください。

- [jwtインストールや設定]({{site.url}}/{{page.categories}}/jwt/){:target="_blank"}

## リポジトリ(Repository)
私たちはjwt認証システムを実装したリポジトリ(Repository)を作りました。下記のリンクを押してリポジトリ(Repository)を確認してみてください。

- laravel-jwt-exercise: [https://github.com/dev-yakuza/laravel-jwt-exercise](https://github.com/dev-yakuza/laravel-jwt-exercise){:rel="nofollow noreferrer" target="_blank"}

## 開発環境構成
ここで説明する内容はLaradockとアンシブル(Ansible)を使って作ったララベル(Laravel)開発環境上で開発やテストします。Laradockとアンシブル(Ansible)を使ってララベル(Laravel)開発環境については下のブログを参考してください。

- [アンシブル&ララベル]({{site.url}}/environment/ansible-laravel/){:target="_blank"}

## データベース連結
今から実装する会員登録機能は会員の情報を記録するテータベース(Database)が必要になります。ララベル(Laravel)とデータベースを連携する方法に関しては下記のブログを参考してください。

- [アンシブル&ララベル]({{site.url}}/environment/ansible-laravel/){:target="_blank"}

## テーブル生成
ララベル(Laravel)は基本的にユーザーに関してマイグレーション(Migration - DBテーブルを生成するためのファイル)とモデル(Model)を提供してます。したがって、下記のコマンドを使ってララベル(Laravel)が提供してる基本ユーザーテーブルを使えます。

```bash
# vagrant up
# vagrant ssh
# sudo docker exec -it laradock_workspace_1 bash
php artisan migrate
```

## コントローラー生成
jwt認証システムを実装するコントローラー(Controller)を下記のようにartisanコマンドで生成します。

```bash
# vagrant up
# vagrant ssh
# sudo docker exec -it laradock_workspace_1 bash
php artisan make:controller JWTAuthController
```

生成された```app/http/Controllers/JWTAuthController.php```を下記のように修正します。

```php
...
use Illuminate\Support\Facades\Validator;
use App\User;

class JWTAuthController extends Controller
{
    public function register(Request $request) {
        $validator = Validator::make($request->all(), [
            'name' => 'required|string|max:100',
            'email' => 'required|email|max:255|unique:users',
            'password' => 'required|string|min:8|max:255|confirmed',
            'password_confirmation' => 'required|string|min:8|max:255',
        ]);

        if($validator->fails()) {
            return response()->json([
                'status' => 'error',
                'messages' => $validator->messages()
            ], 200);
        }

        $user = new User;
        $user->fill($request->all());
        $user->password = bcrypt($request->password);
        $user->save();

        return response()->json([
            'status' => 'success',
            'data' => $user
        ], 200);
    }
}
```

修正したコントローラー(Controller)を詳しく見てみます。

```php
$validator = Validator::make($request->all(), [
    'name' => 'required|string|max:100',
    'email' => 'required|email|max:255|unique:users',
    'password' => 'required|string|min:8|max:255|confirmed',
    'password_confirmation' => 'required|string|min:8|max:255',
]);
```

クライアント(Client, ブラウザ)から来たリクエスト(```$request```)を```Validator```を使って値を検証します。

```php
if($validator->fails()) {
    return response()->json([
        'status' => 'error',
        'messages' => $validator->messages()
    ], 200);
}
```

上でリクエスト(Request)を検証して失敗した場合、失敗メッセージと一緒にリクエスト(Request)に関して応答(Response)をクライアント(Client, ブラウザ)に送ります。

```php
$user = new User;
$user->fill($request->all());
$user->password = bcrypt($request->password);
$user->save();
```

クライアント(Client, ブラウザ)から来たリクエスト(Request)の検証に成功した場合、新しユーザーを生成してデータベースに保存します。

```php
$user->fill($request->all())
```

この時、モデル(Model)に設定した```fillable```機能を使ってクライアント(Client, ブラウザ)が送ったリクエスト(Request)中で必要な内容でデーターを入力します。

```php
return response()->json([
    'status' => 'success',
    'data' => $user
], 200);
```

データを成功的に生成した場合、そのデータと一緒にクライアント(Client, ブラウザ)のリクエスト(Request)に関して応答(Response)を送ります。

## ルーティング連結
今まで生成したコントローラー(Controller)をルーティング設定をしてURLと連結します。```routes/api.php```ファイルを開いて下記のように修正します。

```php
Route::post('register', 'JWTAuthController@register')->name('api.jwt.register');
```

ララベル(Laravel)に```register```のURLで```post```でリクエスト(Request)が来たら```JWTAuthController```の```register```である関数をコールするように連携します。

## テスト
私たちはAPIテストをするため```Postman```を使います。```Postman```が無い方は下記のリンクを押してインストールしてください。テストする時、Postmanではなく```curl```を使っても構いません。

- Postman: [https://www.getpostman.com/](https://www.getpostman.com/){:rel="nofollow noreferrer" target="_blank"}

インストールした```Postman```を開いて下記のように```localhost/api/register```のURLに```post```リクエスト(Request)を送ります。

![postman register api test](/assets/images/category/laravel/jwt-signup/register_api_test.png)

データが成功的に登録されたら私たちが設定した形式で応答(Response)が来ることを確認出来ます。失敗したら下記のような画面が見えます。

![postman register api test fail](/assets/images/category/laravel/jwt-signup/register_api_test_fail.png)

## 完了
今までトークンベース認証システムであるjwt認証システムを使って会員登録部分を開発しました。次のブログではjwt認証システムを使ってログイン手続きを処理する部分について見てみます。

## 参考
- tymon/jwt-auth: [https://github.com/tymondesigns/jwt-auth](https://github.com/tymondesigns/jwt-auth){:rel="nofollow noreferrer" target="_blank"}
- Postman: [https://www.getpostman.com/](https://www.getpostman.com/){:rel="nofollow noreferrer" target="_blank"}