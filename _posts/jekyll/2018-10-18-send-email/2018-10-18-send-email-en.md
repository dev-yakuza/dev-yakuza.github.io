---
layout: 'post'
permalink: '/jekyll/send-email/'
paginate_path: '/jekyll/:num/send-email/'
lang: 'en'
categories: 'jekyll'
comments: true

title: 'Send Email'
description: 'use formspree to add sending email feature to jekyll project.'
image: '/assets/images/category/jekyll/send-email.jpg'
---

## outline
we use [github page](https://pages.github.com/){:rel="nofollow noreferrer" :target="_blank"} for serving this blog. we provide this blog by uploading static files(html, css, javascript) created by jekyll to github page. in other words, we can not create and use server-side-source. so we are not also able to create simple email feature on github page and jekyll.

[formspree service](https://formspree.io/){:rel="nofollow noreferrer" :target="_blank"} helps static page like above situation to be able to create sending email feature. this blog post introduces how to apply formspree service to jekyll for sending email feature.

## formspree service
we can use formspree service without joining up. click below link to go formspree service site.

- formspree service site: [https://formspree.io/](https://formspree.io/){:rel="nofollow noreferrer" :target="_blank"}

## use formspree service
you can see below screen when you click above link to move formspree service.

![formspree service site](/assets/images/category/jekyll/formspree/homepage.png)

click ```Try Formspree!``` link on the left top of the page.

![formspree test site](/assets/images/category/jekyll/formspree/test-site.png)

edit the code under ```Edit your form here``` for your site's form when you see above screen.

```html
<form method="POST" action="https://formspree.io/YOUREMAILHERE">
```
write your email to action attribute of the form tag.

```html
<form method="POST" action="https://formspree.io/dev.yakuza@gmail.com">
```

and then use ```Test it here``` on the right side to send email which you writed.

when you send email, formspree will send email for verifying your email. check your email for confirming that.

we ready to apply formspree service to jekyll project for email feature.

## apply formspree to jekyll
copy-paste the source which you made on Formspree site to ```_layout/contact.html``` file. layout file may vary depending on your theme. below code is what we use really.

{% include_relative common/email_form.md %}

```html
action="https://formspree.io/{{ site.email }}"
```

edit  action attribute of form tag like above to use email which you set ```_config.yml```.

```html
<input type="text" name="_gotcha" style="display:none" />
```

above code is to display ```CAPTCHA``` when send email.

```html
<input type="hidden" name="_subject" value="블로그에서 새로운 연락이 왔습니다." />
```

set email title using above code.

## complete
everything is completed. go to your site and send email for test.

## reference
- official site: [formspree service](https://formspree.io/){:rel="nofollow noreferrer" :target="_blank"}