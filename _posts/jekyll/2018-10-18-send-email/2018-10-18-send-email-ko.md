---
layout: 'post'
permalink: '/jekyll/send-email/'
paginate_path: '/jekyll/:num/send-email/'
lang: 'ko'
categories: 'jekyll'
comments: true

title: '이메일 발송 기능'
description: 'jekyll 프로젝트에 formspree 서비스를 이용하여 이메일 발송 기능을 추가해 보자.'
image: '/assets/images/category/jekyll/send-email.jpg'
---

## 개요
우리는 [github page](https://pages.github.com/){:rel="nofollow noreferrer" :target="_blank"}로 블로그를 서비스하고 있습니다. jekyll로 생성한 정적 파일(html, css, javascript)를 github page에 업로드하는 것으로 블로그를 서비스하고 있습니다. 이 말은 서버쪽 소스는 생성, 활용을 할 수 없다는 의미입니다. 그러므로 일반적으로 서버를 통해 이메일을 발송하는 간단한 기능도 github과 jekyll을 이용한 사이트는 구현할 수 없습니다.

[formspree 서비스](https://formspree.io/){:rel="nofollow noreferrer" :target="_blank"}는 이와 같은 정적 페이지에 이메일 전송 기능을 무료로 구현할 수 있도록 도와주는 서비스입니다. 이 블로그에서 formspree를 사용하여 jekyll에서 이메일을 발송하는 기능을 구현하도록 하겠습니다.

## formspree 서비스
formspree 서비스는 회원 가입을 하지 않고도 무료로 사용할 수 있습니다. 아래에 링크를 통해 서비스 사이트로 이동합니다.
- formspree 서비스: [https://formspree.io/](https://formspree.io/){:rel="nofollow noreferrer" :target="_blank"}

## formspree 서비스 이용하기
formspree 서비스 사이트로 이동하면 아래와 같은 화면을 볼 수 있습니다.
![formspree service site](/assets/images/category/jekyll/formspree/homepage.png)

왼쪽 위에 ```Try Formspree!```를 선택합니다.

![formspree test site](/assets/images/category/jekyll/formspree/test-site.png)

위에 화면에서 ```Edit your form here``` 부분을 수정하여 실제로 사용할 form을 작성합니다.

```html
<form method="POST" action="https://formspree.io/YOUREMAILHERE">
```
action부분에 사용할 이메일을 사용할 이메일을 넣습니다.

```html
<form method="POST" action="https://formspree.io/dev.yakuza@gmail.com">
```

그리고 오른쪽에 ```Test it here```을 통해 실제 메일을 발송합니다.

메일을 발송하고 나면 form에 작성한 메일이 실제 자신에 메일인지 formspree이 확인 메일을 발송합니다. 메일을 확인하여 자신에 메일임을 증명합니다.

formspree 서비스를 통해 이메일 발송 기능을 jekyll에 추가할 준비가 완료되었습니다.

## jekyll에 formspree 적용하기
위에서 생성한 html form 소스를 복사하여 ```_layout/contact.html```에 삽입합니다. 레이아웃 파일은 테마에 따라 다를 수 있습니다. 아래에 코드는 우리가 실제로 사용하고 있는 소스입니다.

{% include_relative common/email_form.md %}

```html
action="https://formspree.io/{{ site.email }}"
```

form의 action에 ```_config.yml```에 설정한 이메일을 사용하도록 하였습니다.

```html
<input type="text" name="_gotcha" style="display:none" />
```

위에 코드로 이메일을 발송할때 ```CAPTCHA```를 표시하도록 설정합니다.

```html
<input type="hidden" name="_subject" value="블로그에서 새로운 연락이 왔습니다." />
```

메일에 제목을 설정합니다.

## 완료
모든 설정이 완료되었습니다. 실제 사이트에서 메일이 발송되는지 확인하세요.

## 참고
- 공식 사이트: [formspree 서비스](https://formspree.io/){:rel="nofollow noreferrer" :target="_blank"}