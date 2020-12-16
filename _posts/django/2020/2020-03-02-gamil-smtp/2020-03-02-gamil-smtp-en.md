---
layout: 'post'
permalink: '/django/gmail-smtp/'
paginate_path: '/django/:num/gmail-smtp/'
lang: 'en'
categories: 'django'
comments: true

title: Send email via Gmail SMTP
description: Let's see how to send email via Gmail SMTP on django project, and I share my issue when I sent email.
image: '/assets/images/category/django/2020/gmail-smtp/background.jpg'
---

<div id="contents_list" markdown="1">

## Content

- [Outline](#outline)
- [Google Account Settings](#google-account-settings)
- [django settings](#django-settings)
- [Send Email](#send-email)
- [SMTPAuthenticationError error on Heroku](#smtpauthenticationerror-error-on-heroku)
- [Completed](#completed)

</div>

## Outline

I had a chance to send email on django project. In this blog post, I'll introduce how to send email on django project via Gamil SMTP, and I'll share my problem when I sent email.

## Google Account Settings

If you want to send email via Gmail SMTP, first you should configure `Less secure apps & your Google Account` on your Google Account.

- Less secure apps configuration: [https://support.google.com/accounts/answer/6010255](https://support.google.com/accounts/answer/6010255){:rel="nofollow noreferrer" target="_blank"}

First, Click the link below to go to Google Account.

- Google Account: [https://myaccount.google.com/](https://myaccount.google.com/){:rel="nofollow noreferrer" target="_blank"}

After login, you can see the screen like below.

![Google Account page](/assets/images/category/django/2020/gmail-smtp/google-account.jpg)

Click `Security` menu on the left side, and scroll to bottom, you can see the screen like below.

![Google Account Less secure app](/assets/images/category/django/2020/gmail-smtp/less-secure-app.jpg)

Click the menu and change `Allow less secure apps` status to `ON`.

![Google Account Less secure app](/assets/images/category/django/2020/gmail-smtp/less-secure-app-on.jpg)

If you couldn't find the menu, use the link below.

- Google Account Less secure app access: [https://myaccount.google.com/lesssecureapps](https://myaccount.google.com/lesssecureapps){:rel="nofollow noreferrer" target="_blank"}

If your account is configured `2-Step Verification`, you can not use the account.

{% include in-feed-ads.html %}

## django settings

open `[project name]/settings.py` file and modify it like below.

```python
# send email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.googlemail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'Your email address'
EMAIL_HOST_PASSWORD = 'password'
```

In here, you should change `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD` to your Google account.

## Send Email

You can send HTML email via the code below.

```python
from django.core.mail import send_mail
from django.conf import settings
...
send_mail(subject, message, email_from, recipient_list, html_message=message)
```

- subject: email title
- message: email contents
- email_from: from who (I use `email_from = settings.EMAIL_HOST_USER` code.)
- recipient_list: recipient list. It's email string list(`[email, ]`)
- html_message: HTML string

You can send email without any problem.

## SMTPAuthenticationError error on Heroku

I've sent email on Local without any problem, but after deployig to Heroku, I got the error message like below, and couldn't send email.

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

When I checked Gmail and Google account, I saw Google blocked Heroku server IP. I used the link below to solve this issue.

- [https://accounts.google.com/b/0/DisplayUnlockCaptcha](https://accounts.google.com/b/0/DisplayUnlockCaptcha){:rel="nofollow noreferrer" target="_blank"}

If you click the link above, you can see the screen like below.

![Google Account Less secure app](/assets/images/category/django/2020/gmail-smtp/display-unlock-captcha.jpg)

Click the `Continue` button on the bottom, and then send email via django again, you can see the email sent well.

## Completed

We've seen how to send email via Gmail SMTP on django project. I think you don't have any problem, but If you have the problem like me, please try the solution that I mentioned.
