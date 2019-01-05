---
published: false
layout: 'post'
permalink: '/laravel/jwt-refresh-token/'
paginate_path: '/laravel/:num/jwt-refresh-token/'
lang: 'ko'
categories: 'laravel'
comments: true

title: 'jwt:사용자 정보'
description: '토큰 기반 인증 시스템인 jwt(Json Web Token)를 통해 로그인한 사용자의 정보를 얻는 방법에 대해서 알아봅시다.'
image: '/assets/images/category/laravel/jwt-refresh-token.jpg'
---


## 개요
jwt 인증 시스템을 통해 로그인한 사용자의 정보를 얻는 방법에 대해서 알아보려고 합니다. 이 블로그는 시리즈로 구성되어 있습니다. jwt 구현을 위한 미들웨어(Middleware) 설치나 회원가입, 로그인 구현에 관해서는 이전 블로그를 참고해주세요.

- [jwt 설치 및 설정]({{site.url}}/{{page.categories}}/jwt/){:target="_blank"}
- [jwt:회원가입]({{site.url}}/{{page.categories}}/jwt/jwt-siginup){:target="_blank"}
- [jwt:로그인]({{site.url}}/{{page.categories}}/jwt/jwt-signin){:target="_blank"}

## 저장소(Repository)
우리는 jwt 인증 시스템을 구현한 저장소(Repository)를 만들었습니다. 아래에 링크를 클릭해서 저장소(Repository)를 확인해 보세요.

- laravel-jwt-exercise: [https://github.com/dev-yakuza/laravel-jwt-exercise](https://github.com/dev-yakuza/laravel-jwt-exercise){:rel="nofollow noreferrer" target="_blank"}

## 개발 환경 구성
여기서 설명할 내용은 라라독(Laradock)과 앤서블(Ansible)을 이용하여 만든 라라벨(Laravel) 개발 환경에서 작업합니다. 라라독(Laradock)과 앤서블(Ansible)을 이용한 라라벨(Laravel) 개발 환경에 관해서는 아래에 블로그를 참고하세요.

- [앤서블&라라벨]({{site.url}}/environment/ansible-laravel/){:target="_blank"}

## 컨트롤러 수정
라라벨(Laravel) 프로젝트 폴더의 ```/app/Http/Controllers/JWTAuthController.php``` 파일을 열고 아래의 내용을 추가합니다.


```php
public function user() {
    return response()->json(Auth::guard('api')->user());
}
```

클라이언트(Client, 브라우저)의 요청(Request)으로 로그인한 유저의 정보를 얻어 응답(Response)하는 함수입니다.

## 라우트 수정
컨트롤러(Controller)에 추가한 함수를 URL과 연결하기 위해 라우트(Route)를 수정합니다. ```/routes/api.php``` 파일을 열고 아래의 내용을 추가합니다.

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

사용자 정보를 얻기 위한 ```user``` 라우트(Route)는 미들웨어(Middleware)로 ```auth:api```를 사용합니다. 이 미들웨어(Middleware)에 의해 로그인한 사용자와 로그인하지 않은 사용자가 판단되며 로그인한 사용자만 사용자 정보를 얻을 수 있습니다. 로그인하지 않은 사용자는 ```unauthorized``` 라우트(Route)로 리다이렉트(Redirect)를 시키고 그에 따라 ```401```를 응답(Response)할 예정입니다.

## 리다이렉트
라라벨(Laravel)의 ```Auth``` 미들웨어(Middleware)는 기본적으로 리다이렉트(Redirect) 기능을 가지고 있습니다. 우리는 여기에 ```api```용 리다이렉트(Redirect)를 설정하고 ```401``` 에러를 응답(Response)하도록 설정하려 합니다. ```app/Http/Middleware/Authenticate.php``` 파일을 열고 아래와 같이 수정합니다.

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

## 테스트
지금까지 개발한 사용자 정보 보기 기능을 ```Postman```을 통해 확인합니다.

```bash
# URL
localhost/api/user
# header
Authorization
Bearer jwt_token
```
jwt 토큰이 유효하다면 아래와 같이 사용자의 정보를 얻을 수 있습니다.

![get user info](/assets/images/category/laravel/jwt-user-info/get_user_info.png)

jwt 토큰의 유효기간이 끝났거나, 로그인하지 않은 사용자가 정보를 요청(Request)하면 아래와 같이 ```401``` 에러의 응답(Response)을 확인할 수 있습니다.

![fail to get user info](/assets/images/category/laravel/jwt-user-info/fail_to_get_user_info.png)

## 완료
이것으로 jwt 인증 시스템을 이용하여 로그인한 사용자의 정보를 얻는 api를 개발하였습니다. 다음 블로그에서는 로그인 후 api를 통해 얻은 jwt 토큰을 갱신(Refresh)하는 기능을 추가하도록 하겠습니다.