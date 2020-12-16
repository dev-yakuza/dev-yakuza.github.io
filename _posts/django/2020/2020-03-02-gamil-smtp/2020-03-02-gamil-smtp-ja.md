---
layout: 'post'
permalink: '/django/gmail-smtp/'
paginate_path: '/django/:num/gmail-smtp/'
lang: 'ja'
categories: 'django'
comments: true

title: 'Gmailのsmtpを使ってメールを送信する'
description: djangoプロジェクトでGmailのsmtpを使ってメールを送信する方法と開発した時あた問題を共有します。
image: '/assets/images/category/django/2020/gmail-smtp/background.jpg'
---

<div id="contents_list" markdown="1">

## 目次

- [概要](#概要)
- [Google Account設定](#google-account設定)
- [django設定](#django設定)
- [メール送信](#メール送信)
- [herokuでSMTPAuthenticationErrorエラー](#herokuでsmtpauthenticationerrorエラー)
- [完了](#完了)

</div>

## 概要

djangoでサーバサイドを開発した時メールを送信する必要がありました。今回のブログポストではdjangoプロジェクトでGmailのsmtpを使ってメールを送信する方法を紹介します。それと、メール送信機能を開発した時あた問題点も共有します。

## Google Account設定

SMTPを使ってGmailでメールを送信したい場合、まず`Less secure apps & your Google Account`を設定する必要があります。

- Less secure apps 設定: [https://support.google.com/accounts/answer/6010255](https://support.google.com/accounts/answer/6010255){:rel="nofollow noreferrer" target="_blank"}

まず、下記のリンクを使ってGoogle Accountに移動します。

- Google Account: [https://myaccount.google.com/](https://myaccount.google.com/){:rel="nofollow noreferrer" target="_blank"}

ログインした後、Google Accountで移動すると、下記のような画面が見えます。

![Google Account ページ](/assets/images/category/django/2020/gmail-smtp/google-account.jpg)

左の`Security`メニューを選択して少しスクロールすると、下記の画面が確認できます。

![Google Account Less secure app](/assets/images/category/django/2020/gmail-smtp/less-secure-app.jpg)

メニューを選択して入って、`Allow less secure apps`を`ON`の状態で変更します。

![Google Account Less secure app](/assets/images/category/django/2020/gmail-smtp/less-secure-app-on.jpg)

メニューがどこにあるかよく分からない方は下記のリンクを使ってください。

- Google Account Less secure app access: [https://myaccount.google.com/lesssecureapps](https://myaccount.google.com/lesssecureapps){:rel="nofollow noreferrer" target="_blank"}

参考で`2-Step Verification`（２段階認証）を使ってるアカウントは設定ができないので注意してください。

{% include in-feed-ads.html %}

## django設定

djangoプロジェクトの`[project name]/settings.py`を開いて下記のように修正します。

```python
# send email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.googlemail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'Your email address'
EMAIL_HOST_PASSWORD = 'password'
```

ここで、 `EMAIL_HOST_USER`と`EMAIL_HOST_PASSWORD`を自分のグーグルアカウント情報で変更します。

## メール送信

下記のコードを使ってHTMLメールを送信することができます。

```python
from django.core.mail import send_mail
from django.conf import settings
...
send_mail(subject, message, email_from, recipient_list, html_message=message)
```

- subject: メールのタイトル
- message: メールの内容
- email_from: メールを発送した方(私は`email_from = settings.EMAIL_HOST_USER`コードを使ってます。)
- recipient_list: メールを受ける方のリスト。メールアカウントのリスト(`[email, ]`)
- html_message: HTMLメッセージ

これで問題なく、メールを送信することができます。

## herokuでSMTPAuthenticationErrorエラー

ローカルでは上手く使いましたが、herokuにデプロイした後、下記のようなエラーが出て、メールが送信されませんでした。

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

GmailとGoogle Accountへ入って確認したら、HerokuサーバのIPがブロックされたことが確認できました。この問題を解決するため、下記のリンクに移動します。

- [https://accounts.google.com/b/0/DisplayUnlockCaptcha](https://accounts.google.com/b/0/DisplayUnlockCaptcha){:rel="nofollow noreferrer" target="_blank"}

上のリンクを移動すると下記のような画面が確認できます。

![Google Account Less secure app](/assets/images/category/django/2020/gmail-smtp/display-unlock-captcha.jpg)

下にある`Continue`ボタンを押します。そして、また、djangoを使ってメールを送信するとメールが残と送信されることが確認できます。

## 完了

これでdjangoプロジェクトでGmailのSMTPを使ってメールを送信する方法について見てみました。特に問題ないと思いますが、私みたいに、IPをブロックされる方は上に紹介した内容を試してみてください。
