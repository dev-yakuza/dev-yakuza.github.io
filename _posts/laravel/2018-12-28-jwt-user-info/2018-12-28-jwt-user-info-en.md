---
layout: 'post'
permalink: '/laravel/jwt-user-info/'
paginate_path: '/laravel/:num/jwt-user-info/'
lang: 'en'
categories: 'laravel'
comments: true

title: 'jwt:user information'
description: let's see how to get user information from login user in jwt(Json Web Token) which is one of the token based authentication systems.
image: '/assets/images/category/laravel/jwt-user-info.jpg'
---


## Outline
we'll introduce how to get user information from login user in jwt authentication system. this blog is a series. if you want to know how to install jwt middleware and implement signup, signin features, see our previous blogs.

- [jwt installation&settings]({{site.url}}/{{page.categories}}/jwt/){:target="_blank"}
- [jwt:signup]({{site.url}}/{{page.categories}}/jwt-signup){:target="_blank"}
- [jwt:signin]({{site.url}}/{{page.categories}}/jwt-signin){:target="_blank"}

## Repository
we've made the repository of jwt authentication system. click below link to see our repository.

- laravel-jwt-exercise: [https://github.com/dev-yakuza/laravel-jwt-exercise](https://github.com/dev-yakuza/laravel-jwt-exercise){:rel="nofollow noreferrer" target="_blank"}

## Development Environment
in here, we'll use Laravel development environment created by Laradock and Ansible. if you want to know our environment, see our previous blog.

- [Ansible&Laravel]({{site.url}}/environment/ansible-laravel/){:target="_blank"}

## Modify Controller
open ```/app/Http/Controllers/JWTAuthController.php``` file in Laravel project folder and add below code.

```php
public function user() {
    return response()->json(Auth::guard('api')->user());
}
```

this function is to get and response login user information by client(browser) request.

## Modify Route
modify the route to connect the controller function and url. open ```/routes/api.php``` file and add below code.

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
```user``` route which gets user information uses ```auth:api``` middleware. this middleware judges the user is login or not login and if the user was login, the user can get user information. we will make user to redirect ```unauthorized``` and response ```401``` if user was not login.

## Redirect
Laravel ```Auth``` middleware basically has redirect feature. we'll configure the redirect for ```api``` and set ```401``` response. open ```app/Http/Middleware/Authenticate.php``` file and modify it like below.

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

## Test
let's test user information feature via ```Postman```.

```bash
# URL
localhost/api/user
# header
Authorization
Bearer jwt_token
```

if jwt token is valid, you can get user information like below screen.

![get user info](/assets/images/category/laravel/jwt-user-info/get_user_info.png)

if jwt token is expired or user who didn't login requests user information, you can get ```401``` error response.

![fail to get user info](/assets/images/category/laravel/jwt-user-info/fail_to_get_user_info.png)

## Completed
we've done to develop the api which gets user information feature in jwt authentication system. at next blog post, we will introduce how to make jwt token refresh feature after login.