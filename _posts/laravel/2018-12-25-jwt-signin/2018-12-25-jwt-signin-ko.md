---
layout: 'post'
permalink: '/laravel/jwt-signin/'
paginate_path: '/laravel/:num/jwt-signin/'
lang: 'ko'
categories: 'laravel'
comments: true

title: 'jwt:로그인'
description: '토큰 기반 인증 시스템인 jwt(Json Web Token)을 이용하여 로그인 절차를 구현해 봅니다.'
image: '/assets/images/category/laravel/jwt-signin.png'
---


## 개요
jwt 인증 시스템을 통해 로그인 절차를 구현해 보려고합니다. 이 블로그는 시리즈로 구성되어 있습니다. jwt 구현을 위한 미들웨어(Middleware) 설치나 회원가입 구현에 관해서는 이전 블로그를 참고해주세요.

- [jwt 설치 및 설정]({{site.url}}/{{page.categories}}/jwt/){:target="_blank"}
- [jwt:회원가입]({{site.url}}/{{page.categories}}/jwt-signup){:target="_blank"}

## 저장소(Repository)
우리는 jwt 인증 시스템을 구현한 저장소(Repository)를 만들었습니다. 아래에 링크를 클릭해서 저장소(Repository)를 확인해 보세요.

- laravel-jwt-exercise: [https://github.com/dev-yakuza/laravel-jwt-exercise](https://github.com/dev-yakuza/laravel-jwt-exercise){:rel="nofollow noreferrer" target="_blank"}

## 개발 환경 구성
여기서 설명할 내용은 라라독(Laradock)과 앤서블(Ansible)을 이용하여 만든 라라벨(Laravel) 개발 환경에서 작업합니다. 라라독(Laradock)과 앤서블(Ansible)을 이용한 라라벨(Laravel) 개발 환경에 관해서는 아래에 블로그를 참고하세요.

- [앤서블&라라벨]({{site.url}}/environment/ansible-laravel/){:target="_blank"}

## 모델 수정
jwt 인증 시스템의 인증에 사용되는 모델(Model)을 아래와 같이 수정합니다.

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

라라벨(Laravle)의 인증 기능을 사용하기 위해 모델(Model)을 ```Authenticatable```에서 상속받았습니다. 또한 jwt 미들웨어(Middleware)의 인터페이스를 ```JWTSubject```를 통해 구현합니다.

```php
public function getJWTIdentifier() {
    return $this->getKey();
}

public function getJWTCustomClaims() {
    return [];
}
```

위에 함수는 jwt 미들웨어(Middleware)의 인터페이스를 구현한 부분입니다.

```php
public function getJWTIdentifier() {
    return $this->getKey();
}
```

이 부분은 jwt의 토큰을 습득하기 위한 함수입니다.

```php
public function getJWTCustomClaims() {
    return [];
}
```

이 함수를 설명하기 위해 jwt 토큰을 잠시 설명하겠습니다. jwt는 크게 ```헤더(header).내용(payload).서명(signature)```으로 구성되어 있습니다. 그중 ```내용(Payload)```에 사용될 정보의 일부를 ```Claim```이라고 하며, ```key-value``` 형식으로 구성되어있습니다. jwt는 기본적으로 ```내용(Payload)```에 아래와 같은 정보(```Claim```)를 가지고 있습니다.

- iss(Issuer): 토큰 발급자
- sub(Subject): 토큰 제목(기본값은 user id)
- iat(Issued At): 토큰 발행일(unix timestamp)
- exp(Expiry): 토큰의 만료시간
- nbf(Not Before): 토큰을 사용할 수 있는 시작 시간
- jti(JWT Id): JWT의 고유 식별자. 주로 중복적인 처리를 방지하기 위하여 사용.
- prv: 사용자 공급자 클래스(User Provider class)의 해쉬값. 다중 guard를 사용하기 위해 ```tymondesigns/jwt-auth```에 추가한 특별한 코드.([자세한 설명](https://github.com/tymondesigns/jwt-auth/pull/1167){:rel="nofollow noreferrer" target="_blank"})

이 정보 이외에 추가적으로 jwt토큰에 정보를 추가하고 싶다면 ```getJWTCustomClaims()``` 함수에 반환값(Return value)을 수정하면 됩니다.

```php
public function getJWTCustomClaims() {
    return [
        'firstname' => $this->firstname,
        'lastname' => $this->lastname,
        'email' => $this->email
    ];
}
```

## guard 수정
라라벨(Laravel)의 인증을 담당하고 있는 ```config/auth.php``` 파일의 ```guard```를 아래와 같이 수정합니다.

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

## 컨트롤러 수정
이전 블로그에서 생성한 ```app/Http/Controllers/JWTAuthController.php``` 컨트롤러에 로그인 함수를 추가합니다

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

우선 요청(Request)의 입력 데이터를 확인합니다.

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

그리고 사용자의 ```email```과 ```password```로 로그인 시킵니다.

```php
if (! $token = Auth::guard('api')->attempt(['email' => $request->email, 'password' => $request->password])) {
    return response()->json(['error' => 'Unauthorized'], 401);
}
```

로그인에 성공하면 요청(Request)에 대한 jwt 토큰을 반환(Response)합니다.

```php
return response()->json([
    'access_token' => $token,
    'token_type' => 'bearer',
    'expires_in' => Auth::guard('api')->factory()->getTTL() * 60
]);
```

## 라우트 연결
컨트롤러(Controller)에서 생성한 로그인 함수를 ```routes/api.php```에서 URL과 연결합니다.

```php
Route::post('login', 'JWTAuthController@login')->name('api.jwt.login');
```

## 테스트
이제 지금까지 만든 jwt 인증 시스템의 로그인 기능을 ```Postman```을 통해 확인합니다. ```localhost/api/login``` URL에 ```email```과 ```password```를 입력하고 ```POST```로 요청(Request)을 보내면 아래와 같은 결과를 확인할 수 있습니다.

![postman login api test](/assets/images/category/laravel/jwt-signin/login.png)

응답(Response)으로 받은 ```access_token```키를 [https://jwt.io/](https://jwt.io/){:rel="nofollow noreferrer" target="_blank"}에서 확인해보면 아래와 같은 결과를 얻을 수 있습니다.

![check access_key](/assets/images/category/laravel/jwt-signin/check_access_key.png)

## 완료
이것으로 jwt 인증 시스템을 이용하여 로그인 기능을 구현해보았습니다. 다음 블로그에서는 ```access token```을 이용한 사용자 정보를 얻는 방법에 대해서 알아보도록 하겠습니다.

## 참고
- JSON Web Token (JWT): [https://tools.ietf.org/html/rfc7519#section-4.1](https://tools.ietf.org/html/rfc7519#section-4.1){:rel="nofollow noreferrer" target="_blank"}
- jwt-auth prv: [https://github.com/tymondesigns/jwt-auth/issues/1344](https://github.com/tymondesigns/jwt-auth/issues/1344){:rel="nofollow noreferrer" target="_blank"}
- jwt-auth Creating Tokens: [https://github.com/tymondesigns/jwt-auth/wiki/Creating-Tokens](https://github.com/tymondesigns/jwt-auth/wiki/Creating-Tokens){:rel="nofollow noreferrer" target="_blank"}

