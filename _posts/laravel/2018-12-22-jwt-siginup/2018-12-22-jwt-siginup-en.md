---
layout: 'post'
permalink: '/laravel/jwt-signup/'
paginate_path: '/laravel/:num/jwt-signup/'
lang: 'en'
categories: 'laravel'
comments: true

title: 'jwt:signup'
description: let's make signup feature by using jwt(Json Web Token) whicih is a token based authentication system.
image: '/assets/images/category/laravel/jwt-signup.jpg'
---


## Outline
we try to make signup feature by using jwt(Json Web Token) which is a token based authentication system. in this blog, we will apply [tymon/jwt-auth](https://github.com/tymondesigns/jwt-auth){:rel="nofollow noreferrer" target="_blank"} middleware to Laravel project to make jwt token system. if you want to know how to insall and configure ```tymon/jwt-auth```, see our previous blog.

- [jwt installation&settings]({{site.url}}/{{page.categories}}/jwt/){:target="_blank"}

## Repository
we've made the repository of jwt authentication system. click below link to see our repository.

- laravel-jwt-exercise: [https://github.com/dev-yakuza/laravel-jwt-exercise](https://github.com/dev-yakuza/laravel-jwt-exercise){:rel="nofollow noreferrer" target="_blank"}

## Development Environment
in here, we'll use Laravel development environment created by Laradock and Ansible. if you want to know our environment, see our previous blog.

- [Ansible&Laravel]({{site.url}}/environment/ansible-laravel/){:target="_blank"}

## Connect Database
signup feature which we will develop from now need the database to store the user information. if you don't know how to connect the database to Laravel, see below blog.

- [Ansible&Laravel]({{site.url}}/environment/ansible-laravel/){:target="_blank"}

## Create Table
Laravel basically provides the migration(the file to create DB table). so if you execute below command, you could use basic user table.

```bash
# vagrant up
# vagrant ssh
# sudo docker exec -it laradock_workspace_1 bash
php artisan migrate
```

## Create Controller
execute below command to create the controller which implements jwt authentication system.

```bash
# vagrant up
# vagrant ssh
# sudo docker exec -it laradock_workspace_1 bash
php artisan make:controller JWTAuthController
```

modify ```app/http/Controllers/JWTAuthController.php``` like below.

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

let's see the controller detaily.

```php
$validator = Validator::make($request->all(), [
    'name' => 'required|string|max:100',
    'email' => 'required|email|max:255|unique:users',
    'password' => 'required|string|min:8|max:255|confirmed',
    'password_confirmation' => 'required|string|min:8|max:255',
]);
```

use ```Validator``` to validate request (```$request```) values from the client(browser).

```php
if($validator->fails()) {
    return response()->json([
        'status' => 'error',
        'messages' => $validator->messages()
    ], 200);
}
```

if the validation is failed above, send the response with fail messag to the client(browser).

```php
$user = new User;
$user->fill($request->all());
$user->password = bcrypt($request->password);
$user->save();
```

if the validation is success, create new user and store it.

```php
$user->fill($request->all())
```

at this time, use ```fillable``` feature defined in the model to fill the data from the request which client has sent.

```php
return response()->json([
    'status' => 'success',
    'data' => $user
], 200);
```

when the data is created successfully, send the response to the client(browser) with the data.

## Connect Route
configure the route to connect URL and the controller which we've made until now. open ```routes/api.php``` file and modify it like below.

```php
Route::post('register', 'JWTAuthController@register')->name('api.jwt.register');
```

when Laravel receives the request at ```register``` URL, it calls ```register``` function in ```JWTAuthController```.

## Test
we use ```Postman``` to test API. if you don't have ```Postman```, click below link to download it. you can also use ```curl``` instead of Postman.

- Postman: [https://www.getpostman.com/](https://www.getpostman.com/){:rel="nofollow noreferrer" target="_blank"}

now you can open ```Postman``` and send the post request to ```localhost/api/register``` url.

![postman register api test](/assets/images/category/laravel/jwt-signup/register_api_test.png)

if the data is successfully created, you can see the response which we configured above. if it's failed, you can see the screen like below.

![postman register api test fail](/assets/images/category/laravel/jwt-signup/register_api_test_fail.png)

## Completed
until now, we've developed jwt authentication system which is one of token based authentication systems. next blog post, we will introduce how to make login procedure in jwt authentication system.

## Reference
- tymon/jwt-auth: [https://github.com/tymondesigns/jwt-auth](https://github.com/tymondesigns/jwt-auth){:rel="nofollow noreferrer" target="_blank"}
- Postman: [https://www.getpostman.com/](https://www.getpostman.com/){:rel="nofollow noreferrer" target="_blank"}