---
layout: 'post'
permalink: '/laravel/jwt-refresh-token/'
paginate_path: '/laravel/:num/jwt-refresh-token/'
lang: 'en'
categories: 'laravel'
comments: true

title: 'jwt:refresh token'
description: let's see how to refresh the issued token in jwt(Json Web Token) which is one of the token based authentication systems.
image: '/assets/images/category/laravel/jwt-refresh-token.jpg'
---


## Outline
we will talk about how to refresh the issued token when user was login in jwt authentication system. this blog is a series. if you want to know how to install jwt middleware, signup, signin and get the user information, see our previous blogs.

- [jwt installation&setting]({{site.url}}/{{page.categories}}/jwt/){:target="_blank"}
- [jwt:signup]({{site.url}}/{{page.categories}}/jwt-signup){:target="_blank"}
- [jwt:signin]({{site.url}}/{{page.categories}}/jwt-signin){:target="_blank"}
- [jwt:user information]({{site.url}}/{{page.categories}}/jwt-user-info){:target="_blank"}

## Repository
we've made the repository of jwt authentication system. click below link to see our repository.

- laravel-jwt-exercise: [https://github.com/dev-yakuza/laravel-jwt-exercise](https://github.com/dev-yakuza/laravel-jwt-exercise){:rel="nofollow noreferrer" target="_blank"}

## Development Environment
in here, we'll use Laravel development environment created by Laradock and Ansible. if you want to know our environment, see our previous blog.

- [Ansible&Laravel]({{site.url}}/environment/ansible-laravel/){:target="_blank"}

## Modify Controller
open ```/app/Http/Controllers/JWTAuthController.php``` file in Laravel project folder and add below code.

```php
public function refresh() {
    return $this->respondWithToken(Auth::guard('api')->refresh());
}
```

## Modify Route
open ```/routes/api.php``` file for the url which is to refresh jwt token, and add below code.

```php
...
Route::group(['middleware' => 'auth:api'], function(){
    ...
    Route::get('refresh', 'JWTAuthController@refresh')->name('api.jwt.refresh');
    ...
});
...
```

## Test
let's test jwt token refresh feature we've developed via ```Postman```.

```bash
# URL
localhost/api/refresh
# header
Authorization
Bearer jwt_token
```

if jwt token is valid, jwt token is refreshed and issues new token like below screen.

![refresh token](/assets/images/category/laravel/jwt-refresh-token/refresh_token.png)

if jwt token is expired or previous jwt token, you can get ```401``` error response.

![fail to refresh token](/assets/images/category/laravel/jwt-refresh-token/fail_to_refresh_token.png)

## Completed
we've seen how to refresh jwt token which user got after login in jwt authentication system. at next blog post, we will introduce how to add logout feature which is last feature in jwt authentication system.