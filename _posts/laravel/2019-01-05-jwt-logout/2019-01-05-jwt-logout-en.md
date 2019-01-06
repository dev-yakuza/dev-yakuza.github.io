---
layout: 'post'
permalink: '/laravel/jwt-logout/'
paginate_path: '/laravel/:num/jwt-logout/'
lang: 'en'
categories: 'laravel'
comments: true

title: 'jwt:logout'
description: let's see how to make logout feature in jwt(Json Web Token) authentication system.
image: '/assets/images/category/laravel/jwt-logout.jpg'
---


## Outline
we will introduce how to implement logout feature in jwt authentication system. this blog is a series. if you want to know how to install jwt middleware or how to add signup, signin, getting user information feature, refresh jwt token, see our previous blogs.

- [jwt installation&settings]({{site.url}}/{{page.categories}}/jwt/){:target="_blank"}
- [jwt:signup]({{site.url}}/{{page.categories}}/jwt-signup){:target="_blank"}
- [jwt:signin]({{site.url}}/{{page.categories}}/jwt-signin){:target="_blank"}
- [jwt:user information]({{site.url}}/{{page.categories}}/jwt-user-info){:target="_blank"}
- [jwt:refresh token]({{site.url}}/{{page.categories}}/jwt-refresh-token){:target="_blank"}

## Repository
we've made the repository of jwt authentication system. click below link to see our repository.

- laravel-jwt-exercise: [https://github.com/dev-yakuza/laravel-jwt-exercise](https://github.com/dev-yakuza/laravel-jwt-exercise){:rel="nofollow noreferrer" target="_blank"}

## Development Environment
in here, we'll use Laravel development environment created by Laradock and Ansible. if you want to know our environment, see our previous blog.

- [Ansible&Laravel]({{site.url}}/environment/ansible-laravel/){:target="_blank"}

## Modify Controller
open ```/app/Http/Controllers/JWTAuthController.php``` controller file in Laravel project folder, and add below code.

```php
public function logout() {
    Auth::guard('api')->logout();

    return response()->json([
        'status' => 'success',
        'message' => 'logout'
    ], 200);
}
```

## Modify Route
open ```/routes/api.php``` file, and add below code for the url which is for logout.

```php
...
Route::group(['middleware' => 'auth:api'], function(){
    ...
    Route::get('logout', 'JWTAuthController@logout')->name('api.jwt.logout');
    ...
});
...
```

## Test
let's check logout feature via ```Postman```.

```bash
# URL
localhost/api/logout
# header
Authorization
Bearer jwt_token
```

if jwt token is valid, you can successfully logout.

![logout](/assets/images/category/laravel/jwt-logout/logout.png)

if jwt token is expired or previous jwt token, you can get ```401``` error response.

![fail to logout](/assets/images/category/laravel/jwt-logout/fail_to_logout.png)

## Completed
we've implemented a token based authentication system by adding jwt authentication system to Laravel project. we will use this jwt authentication system to develop RN(React Native) app.