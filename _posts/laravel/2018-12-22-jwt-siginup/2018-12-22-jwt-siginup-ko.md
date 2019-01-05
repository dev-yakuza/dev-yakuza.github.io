---
layout: 'post'
permalink: '/laravel/jwt-signup/'
paginate_path: '/laravel/:num/jwt-signup/'
lang: 'ko'
categories: 'laravel'
comments: true

title: 'jwt:회원가입'
description: '토큰 기반 인증 시스템인 jwt(Json Web Token)을 이용하여 회원가입을 구현해 봅니다.'
image: '/assets/images/category/laravel/jwt-signup.jpg'
---


## 개요
토큰 기반 인증 시스템인 jwt(Json Web Token)을 사용하여 회원가입 기능을 구현하려고 합니다. 이 블로그에서는 jwt 토큰 시스템을 [tymon/jwt-auth](https://github.com/tymondesigns/jwt-auth){:rel="nofollow noreferrer" target="_blank"} 미들웨어(Middleware)로 사용하여 라라벨(Laravel)에 적용하였습니다. 라라벨(Laravel) 프로젝트에 jwt 미들웨어(Middleware)인 ```tymon/jwt-auth```을 설치하고 설정하는 방법에 대해서는 이전 블로그를 참고해 주세요.

- [jwt 설치 및 설정]({{site.url}}/{{page.categories}}/jwt/){:target="_blank"}

## 저장소(Repository)
우리는 jwt 인증 시스템을 구현한 저장소(Repository)를 만들었습니다. 아래에 링크를 클릭해서 저장소(Repository)를 확인해 보세요.

- laravel-jwt-exercise: [https://github.com/dev-yakuza/laravel-jwt-exercise](https://github.com/dev-yakuza/laravel-jwt-exercise){:rel="nofollow noreferrer" target="_blank"}

## 개발 환경 구성
여기서 설명할 내용은 라라독(Laradock)과 앤서블(Ansible)을 이용하여 만든 라라벨(Laravel) 개발 환경에서 작업합니다. 라라독(Laradock)과 앤서블(Ansible)을 이용한 라라벨(Laravel) 개발 환경에 관해서는 아래에 블로그를 참고하세요.

- [앤서블&라라벨]({{site.url}}/environment/ansible-laravel/){:target="_blank"}

## 데이터베이스 연결
지금부터 구현할 회원가입 기능은 회원의 정보를 기록할 데이터베이스(Database)가 필요합니다. 라라벨(Laravel)과 데이터베이스를 연결하는 방법에 대해서는 아래에 블로그를 참고하세요.

- [앤서블&라라벨]({{site.url}}/environment/ansible-laravel/){:target="_blank"}

## 테이블 생성
라라벨(Laravel)은 기본적으로 사용자에 관한 마이그레이션(Migration - DB 테이블을 생성하기 위한 파일)과 모델(Model)를 제공합니다. 따라서 아래에 명령어를 사용하여 라라벨(Laravel)이 제공하는 기본 사용자 테이블을 사용할 수 있습니다.

```bash
# vagrant up
# vagrant ssh
# sudo docker exec -it laradock_workspace_1 bash
php artisan migrate
```

## 컨트롤러 생성
jwt 인증 시스템을 구현할 컨트롤러(Controller)를 아래와 같이 artisan 명령어로 생성합니다.

```bash
# vagrant up
# vagrant ssh
# sudo docker exec -it laradock_workspace_1 bash
php artisan make:controller JWTAuthController
```

생성된 ```app/http/Controllers/JWTAuthController.php```를 아래와 같이 수정합니다.

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

수정한 컨트롤러(Controller)를 자세히 살펴보겠습니다.

```php
$validator = Validator::make($request->all(), [
    'name' => 'required|string|max:100',
    'email' => 'required|email|max:255|unique:users',
    'password' => 'required|string|min:8|max:255|confirmed',
    'password_confirmation' => 'required|string|min:8|max:255',
]);
```

클라이언트(Client, 브라우저)에서 들어온 요청(```$request```)을 ```Validator```를 이용하여 값을 검증합니다.

```php
if($validator->fails()) {
    return response()->json([
        'status' => 'error',
        'messages' => $validator->messages()
    ], 200);
}
```

위에서 요청(Request)을 검증하여 실패한 경우, 실패 메세지와 함께 요청(Requst)에 대한 응답(Response)을 클라이언트(Client, 브라우저)에 보냅니다.

```php
$user = new User;
$user->fill($request->all());
$user->password = bcrypt($request->password);
$user->save();
```

클라이언트(Client, 브라우저)에서 온 요청(Request)의 검증이 성공한 경우, 새로운 유저를 생성하여 데이터베이스에 저장합니다.

```php
$user->fill($request->all())
```

이때, 모델(Model)에서 설정한 ```fillable``` 기능을 사용하여 클라이언트(Client, 브라우저)가 보낸 요청(Request)중 필요한 내용으로 데이터를 채웁니다.

```php
return response()->json([
    'status' => 'success',
    'data' => $user
], 200);
```

데이터를 성공적으로 생성한 경우 해당 데이터와 함께 클라이언트(Client, 브라우저)의 요청(Request)에 대한 응답(Response)를 보냅니다.

## 라우트 연결
지금까지 생성한 컨트롤러(Controller)를 라우트 설정을 통해 URL을 연결시킵니다. ```routes/api.php``` 파일을 열고 아래와 같이 수정합니다.

```php
Route::post('register', 'JWTAuthController@register')->name('api.jwt.register');
```

라라벨(Laravel)에 ```register```라는 URL에 ```post``` 요청(Request)이 오면 ```JWTAuthController```의 ```register```라는 함수를 호출하도록 연결하였습니다.

## 테스트
우리는 API 테스트를 위해 ```Postman```을 사용합니다. ```Postman```이 없는 경우 아래에 링크를 눌러 설치해 주세요. 테스트는 Postman이 아니라 ```curl```을 사용하셔도 됩니다.

- Postman: [https://www.getpostman.com/](https://www.getpostman.com/){:rel="nofollow noreferrer" target="_blank"}

이제 ```Postman```을 열고 아래와 같이 ```localhost/api/register```의 URL로 ```post``` 요청(Request)을 보냅니다.

![postman register api test](/assets/images/category/laravel/jwt-signup/register_api_test.png)

데이터가 성공적으로 등록이 되어 우리가 설정한 형식으로 응답(Response)이 오는 것을 확인할 수 있습니다. 실패한 경우 아래와 같은 화면을 볼 수 있습니다.

![postman register api test fail](/assets/images/category/laravel/jwt-signup/register_api_test_fail.png)

## 완료
지금까지 토큰 기반 인증 시스템인 jwt 인증 시스템을 사용하여 회원가입 부분을 개발하였습니다. 다음 블로그에서는 jwt 인증 시스템을 이용하여 로그인 절차를 처리하는 부분에 대해서 알아보도록 하겠습니다.

## 참고
- tymon/jwt-auth: [https://github.com/tymondesigns/jwt-auth](https://github.com/tymondesigns/jwt-auth){:rel="nofollow noreferrer" target="_blank"}
- Postman: [https://www.getpostman.com/](https://www.getpostman.com/){:rel="nofollow noreferrer" target="_blank"}