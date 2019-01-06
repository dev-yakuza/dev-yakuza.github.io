---
layout: 'post'
permalink: '/laravel/jwt-refresh-token/'
paginate_path: '/laravel/:num/jwt-refresh-token/'
lang: 'ko'
categories: 'laravel'
comments: true

title: 'jwt:토큰 갱신'
description: '토큰 기반 인증 시스템인 jwt(Json Web Token)를 통해 로그인후 얻은 jwt 토큰을 갱신(Refresh)하는 기능을 추가해 보자.'
image: '/assets/images/category/laravel/jwt-refresh-token.jpg'
---


## 개요
jwt 인증 시스템을 통해 로그인후 얻은 jwt 토큰을 갱신(Refresh)하는 방법에 대해서 알아보도록 하겠습니다. 이 블로그는 시리즈로 구성되어 있습니다. jwt 구현을 위한 미들웨어(Middleware) 설치나 회원가입, 로그인, 사용자 정보 얻기 기능에 관해서는 이전 블로그를 참고해주세요.

- [jwt 설치 및 설정]({{site.url}}/{{page.categories}}/jwt/){:target="_blank"}
- [jwt:회원가입]({{site.url}}/{{page.categories}}/jwt-signup){:target="_blank"}
- [jwt:로그인]({{site.url}}/{{page.categories}}/jwt-signin){:target="_blank"}
- [jwt:사용자 정보]({{site.url}}/{{page.categories}}/jwt-user-info){:target="_blank"}

## 저장소(Repository)
우리는 jwt 인증 시스템을 구현한 저장소(Repository)를 만들었습니다. 아래에 링크를 클릭해서 저장소(Repository)를 확인해 보세요.

- laravel-jwt-exercise: [https://github.com/dev-yakuza/laravel-jwt-exercise](https://github.com/dev-yakuza/laravel-jwt-exercise){:rel="nofollow noreferrer" target="_blank"}

## 개발 환경 구성
여기서 설명할 내용은 라라독(Laradock)과 앤서블(Ansible)을 이용하여 만든 라라벨(Laravel) 개발 환경에서 작업합니다. 라라독(Laradock)과 앤서블(Ansible)을 이용한 라라벨(Laravel) 개발 환경에 관해서는 아래에 블로그를 참고하세요.

- [앤서블&라라벨]({{site.url}}/environment/ansible-laravel/){:target="_blank"}

## 컨트롤러 수정
라라벨(Laravel) 프로젝트 폴더의 ```/app/Http/Controllers/JWTAuthController.php``` 컨트롤러(Controller) 파일을 열고 아래의 내용을 추가합니다.

```php
public function refresh() {
    return $this->respondWithToken(Auth::guard('api')->refresh());
}
```

## 라우트 수정
jwt 토큰을 갱신(Refresh)하기 위한 URL을 추가하기 위해 ```/routes/api.php``` 파일을 열고 아래의 내용을 추가합니다.

```php
...
Route::group(['middleware' => 'auth:api'], function(){
    ...
    Route::get('refresh', 'JWTAuthController@refresh')->name('api.jwt.refresh');
    ...
});
...
```

## 테스트
지금까지 개발한 jwt 토큰 갱신(Refresh) 기능을 ```Postman```을 통해 확인합니다.

```bash
# URL
localhost/api/refresh
# header
Authorization
Bearer jwt_token
```

jwt 토큰이 유효하다면 아래와 같이 jwt 토큰을 갱신(Refresh)하여 새로운 토큰을 발급받을 수 있습니다.

![refresh token](/assets/images/category/laravel/jwt-refresh-token/refresh_token.png)

jwt 토큰의 유효기간이 끝났거나, 이전의 jwt 토큰을 사용하면 아래와 같이 ```401``` 에러의 응답(Response)을 확인할 수 있습니다.

![fail to refresh token](/assets/images/category/laravel/jwt-refresh-token/fail_to_refresh_token.png)

## 완료
이것으로 jwt 인증 시스템을 이용하여 로그인후 얻은 jwt 토큰을 갱신(Refresh)하는 방법에 대해서 알아보았습니다. 다음 블로그에서는 jwt 인증 시스템의 마지막 기능인 로그아웃 기능을 추가하는 방법에 대해서 알아보겠습니다.