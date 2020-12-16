---
layout: 'post'
permalink: '/django/gmail-smtp/'
paginate_path: '/django/:num/gmail-smtp/'
lang: 'ko'
categories: 'django'
comments: true

title: 'Gmail의 smtp를 이용하여 메일 보내기'
description: django 프로젝트에서 Gmail의 smtp로 메일을 발송하는 방법과 개발하면서 겪은 문제점을 공유합니다.
image: '/assets/images/category/django/2020/gmail-smtp/background.jpg'
---

<div id="contents_list" markdown="1">

## 목차

- [개요](#개요)
- [Google Account 설정](#google-account-설정)
- [django 설정](#django-설정)
- [메일 발송](#메일-발송)
- [heroku에서 SMTPAuthenticationError 에러](#heroku에서-smtpauthenticationerror-에러)
- [완료](#완료)

</div>

## 개요

django로 서버사이드를 개발하면서 메일을 발송할 필요가 생겼습니다. 이번 블로그 포스트에서는 django 프로젝트에서 Gmail의 smtp로 메일을 발송하는 방법을 소개하고, 메일을 발송하면서 겪은 문제를 공유합니다.

## Google Account 설정

SMTP를 사용하여 Gmail로 메일을 발송하려면 우선 `Less secure apps & your Google Account`을 설정해야 합니다.

- Less secure apps 설정: [https://support.google.com/accounts/answer/6010255](https://support.google.com/accounts/answer/6010255){:rel="nofollow noreferrer" target="_blank"}

우선 아래에 링크를 통해 Google Account로 이동합니다.

- Google Account: [https://myaccount.google.com/](https://myaccount.google.com/){:rel="nofollow noreferrer" target="_blank"}

로그인 후, Google Account로 가면 아래와 같은 화면을 볼 수 있습니다.

![Google Account 페이지](/assets/images/category/django/2020/gmail-smtp/google-account.jpg)

왼쪽의 `Security` 메뉴를 선택하고 조금 스크롤하면, 아래와 같은 화면을 확인할 수 있습니다.

![Google Account Less secure app](/assets/images/category/django/2020/gmail-smtp/less-secure-app.jpg)

메뉴를 선택하고 하고 들어가서, `Allow less secure apps`을 `ON`으로 상태를 변경해줍니다.

![Google Account Less secure app](/assets/images/category/django/2020/gmail-smtp/less-secure-app-on.jpg)

메뉴 찾기가 어려우신 분들은 아래에 링크를 사용하시기 바랍니다.

- Google Account Less secure app access: [https://myaccount.google.com/lesssecureapps](https://myaccount.google.com/lesssecureapps){:rel="nofollow noreferrer" target="_blank"}

참고로 `2-Step Verification`(2단계 인증)을 사용하고 있는 계정은 설정이 불가합니다.

{% include in-feed-ads.html %}

## django 설정

이제 django 프로젝트의 `[project name]/settings.py`를 열고 아래와 같이 수정합니다.

```python
# send email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.googlemail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'Your email address'
EMAIL_HOST_PASSWORD = 'password'
```

여기서, `EMAIL_HOST_USER`과 `EMAIL_HOST_PASSWORD`에 자신의 구글 계정 정보를 입력합니다.

## 메일 발송

아래에 코드를 사용하여 HTML 메일을 발송할 수 있습니다.

```python
from django.core.mail import send_mail
from django.conf import settings
...
send_mail(subject, message, email_from, recipient_list, html_message=message)
```

- subject: 메일의 제목
- message: 메일 내용
- email_from: 메일을 발송하는 사람(저는 `email_from = settings.EMAIL_HOST_USER` 코드를 사용합니다.)
- recipient_list: 받는 사람 리스트. 메일 주소의 문자열 리스트(`[email, ]`)
- html_message: HTML 문자열

이렇게 하면 문제없이 메일이 발송되는 것을 확인할 수 있습니다.

## heroku에서 SMTPAuthenticationError 에러

로컬에서 잘 테스트하다가 heroku에 프로젝트를 업로드한 후, 같은 메일 기능을 사용했을 때, 아래와 같은 에러 메세지가 나오면서 메일이 발송되지 않았습니다.

```bash
2020-03-02T04:53:02.037241+00:00 app[web.1]:     new_conn_created = self.open()
2020-03-02T04:53:02.037241+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/site-packages/django/core/mail/backends/smtp.py", line 69, in open
2020-03-02T04:53:02.037242+00:00 app[web.1]:     self.connection.login(self.username, self.password)
2020-03-02T04:53:02.037242+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/smtplib.py", line 730, in login
2020-03-02T04:53:02.037242+00:00 app[web.1]:     raise last_exception
2020-03-02T04:53:02.037243+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/smtplib.py", line 721, in login
2020-03-02T04:53:02.037243+00:00 app[web.1]:     initial_response_ok=initial_response_ok)
2020-03-02T04:53:02.037243+00:00 app[web.1]:   File "/app/.heroku/python/lib/python3.6/smtplib.py", line 642, in auth
2020-03-02T04:53:02.037244+00:00 app[web.1]:     raise SMTPAuthenticationError(code, resp)
2020-03-02T04:53:02.037261+00:00 app[web.1]: smtplib.SMTPAuthenticationError: (534, b'....')
```

Gmail과 Google Account에 들어가서 확인해 보니, Heroku 서버의 IP가 차단되어 있는 것을 확인할 수 있었습니다. 이 문제를 해결하기 위해서 우선 아래에 링크로 이동합니다.

- [https://accounts.google.com/b/0/DisplayUnlockCaptcha](https://accounts.google.com/b/0/DisplayUnlockCaptcha){:rel="nofollow noreferrer" target="_blank"}

위에 링크로 접속하면 아래와 같은 화면을 볼 수 있습니다.

![Google Account Less secure app](/assets/images/category/django/2020/gmail-smtp/display-unlock-captcha.jpg)

하단에 있는 `Continue` 버튼을 눌러 줍니다. 그리고 다시 django를 통해 메일을 발송하면 메일이 잘 발송되는 것을 확인할 수 있습니다.

## 완료

이것으로 django 프로젝트에서 Gmail의 SMTP를 사용하여 메일을 발송하는 방법에 대해서 알아보았습니다. 아마 별다른 문제가 없을 거 같지만, 저처럼 구글에서 IP를 차단당하시는 분들이 있다면 위에서 설명한 내용을 시도해 보시기 바랍니다.
